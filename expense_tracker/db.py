import sqlite3
import sqlite3
from dataclasses import dataclass
from typing import List, Optional
import datetime
import csv
import io
import os

DB_PATH = os.environ.get('EXPENSE_DB', 'd:/.expense_tracker.db')


@dataclass
class Expense:
    id: Optional[int]
    amount: float
    date: str  # ISO date yyyy-mm-dd
    note: str
    category: Optional[str] = None


class ExpenseDB:
    def __init__(self, path: str = DB_PATH):
        self.path = path
        # ensure DB schema exists - do this immediately in constructor thread
        self._ensure_schema()

    def _get_conn(self):
        # create a fresh connection per call in the current thread
        # Allow cross-thread but ensure each call gets a brand new connection
        conn = sqlite3.connect(self.path, check_same_thread=False, timeout=30.0)
        conn.row_factory = sqlite3.Row
        # Set some connection-level settings for better concurrency
        conn.execute("PRAGMA journal_mode=WAL")
        conn.execute("PRAGMA synchronous=NORMAL") 
        return conn
    
    def _ensure_schema(self):
        # ensure DB schema exists - separate method for thread safety
        with self._get_conn() as conn:
            cur = conn.cursor()
            cur.execute("""
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                amount REAL NOT NULL,
                date TEXT NOT NULL,
                note TEXT,
                category TEXT
            )
            """)
            conn.commit()

    def add_expense(self, amount: float, date: str, note: str = "", category: Optional[str] = None) -> Expense:
        # validate
        if amount <= 0:
            raise ValueError("Amount must be positive")
        try:
            datetime.date.fromisoformat(date)
        except Exception:
            raise ValueError("Date must be ISO format YYYY-MM-DD")
        with self._get_conn() as conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO expenses (amount, date, note, category) VALUES (?, ?, ?, ?)",
                        (amount, date, note, category))
            conn.commit()
            eid = cur.lastrowid
            return Expense(id=eid, amount=amount, date=date, note=note, category=category)

    def list_expenses(self, limit: Optional[int] = None) -> List[Expense]:
        with self._get_conn() as conn:
            cur = conn.cursor()
            q = "SELECT * FROM expenses ORDER BY date DESC, id DESC"
            if limit:
                q += f" LIMIT {int(limit)}"
            cur.execute(q)
            rows = cur.fetchall()
            return [Expense(id=r["id"], amount=r["amount"], date=r["date"], note=r["note"], category=r["category"]) for r in rows]

    def filter_expenses(self, start_date: Optional[str] = None, end_date: Optional[str] = None, category: Optional[str] = None) -> List[Expense]:
        with self._get_conn() as conn:
            cur = conn.cursor()
            parts = []
            params = []
            if start_date:
                parts.append("date >= ?")
                params.append(start_date)
            if end_date:
                parts.append("date <= ?")
                params.append(end_date)
            if category:
                parts.append("category = ?")
                params.append(category)
            q = "SELECT * FROM expenses"
            if parts:
                q += " WHERE " + " AND ".join(parts)
            q += " ORDER BY date DESC, id DESC"
            cur.execute(q, params)
            rows = cur.fetchall()
            return [Expense(id=r["id"], amount=r["amount"], date=r["date"], note=r["note"], category=r["category"]) for r in rows]

    def get_expense(self, eid: int) -> Optional[Expense]:
        with self._get_conn() as conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM expenses WHERE id = ?", (eid,))
            r = cur.fetchone()
            if not r:
                return None
            return Expense(id=r["id"], amount=r["amount"], date=r["date"], note=r["note"], category=r["category"]) 

    def update_expense(self, eid: int, amount: Optional[float] = None, date: Optional[str] = None, note: Optional[str] = None, category: Optional[str] = None) -> Expense:
        e = self.get_expense(eid)
        if not e:
            raise KeyError(f"Expense {eid} not found")
        new_amount = amount if amount is not None else e.amount
        new_date = date if date is not None else e.date
        new_note = note if note is not None else e.note
        new_cat = category if category is not None else e.category
        # validate
        if new_amount <= 0:
            raise ValueError("Amount must be positive")
        try:
            datetime.date.fromisoformat(new_date)
        except Exception:
            raise ValueError("Date must be ISO format YYYY-MM-DD")
        with self._get_conn() as conn:
            cur = conn.cursor()
            cur.execute("""
            UPDATE expenses SET amount=?, date=?, note=?, category=? WHERE id=?
            """, (new_amount, new_date, new_note, new_cat, eid))
            conn.commit()
            return Expense(id=eid, amount=new_amount, date=new_date, note=new_note, category=new_cat)

    def delete_expense(self, eid: int) -> bool:
        with self._get_conn() as conn:
            cur = conn.cursor()
            cur.execute("DELETE FROM expenses WHERE id=?", (eid,))
            conn.commit()
            return cur.rowcount > 0

    def summary_by_category(self):
        with self._get_conn() as conn:
            cur = conn.cursor()
            cur.execute("SELECT category, SUM(amount) as total FROM expenses GROUP BY category")
            return {row['category'] or 'Uncategorized': row['total'] for row in cur.fetchall()}

    def total_spent(self):
        with self._get_conn() as conn:
            cur = conn.cursor()
            cur.execute("SELECT SUM(amount) as total FROM expenses")
            r = cur.fetchone()
            return r['total'] if r and r['total'] is not None else 0.0

    def summary_by_month(self):
        with self._get_conn() as conn:
            cur = conn.cursor()
            cur.execute("SELECT SUBSTR(date,1,7) as month, SUM(amount) as total FROM expenses GROUP BY month ORDER BY month DESC")
            return {row['month']: row['total'] for row in cur.fetchall()}

    def export_csv(self, start_date: Optional[str] = None, end_date: Optional[str] = None, category: Optional[str] = None) -> str:
        rows = self.filter_expenses(start_date=start_date, end_date=end_date, category=category)
        out = io.StringIO()
        writer = csv.writer(out)
        writer.writerow(['id','date','amount','category','note'])
        for e in rows:
            writer.writerow([e.id, e.date, e.amount, e.category or '', e.note])
        return out.getvalue()

    def close(self):
        # no persistent connection to close
        return
