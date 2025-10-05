import tempfile
import os
import time
from expense_tracker.db import ExpenseDB

def test_add_and_get():
    fp = tempfile.NamedTemporaryFile(delete=False)
    fp.close()
    try:
        db = ExpenseDB(path=fp.name)
        e = db.add_expense(10.0, '2025-10-05', 'test', 'misc')
        assert e.id is not None
        got = db.get_expense(e.id)
        assert got.amount == 10.0
        assert got.note == 'test'
        # Clear any references to allow file cleanup
        db = None
        time.sleep(0.1)  # Give Windows time to release file handles
    finally:
        try:
            os.unlink(fp.name)
        except PermissionError:
            # WAL mode auxiliary files may still be open, try to clean them up
            for suffix in ['-wal', '-shm']:
                try:
                    os.unlink(fp.name + suffix)
                except (FileNotFoundError, PermissionError):
                    pass
            # Try main file again
            try:
                time.sleep(0.2)
                os.unlink(fp.name)
            except PermissionError:
                pass  # Accept that cleanup may not work on Windows

def test_update_and_delete():
    fp = tempfile.NamedTemporaryFile(delete=False)
    fp.close()
    try:
        db = ExpenseDB(path=fp.name)
        e = db.add_expense(5.0, '2025-10-01', '', None)
        updated = db.update_expense(e.id, amount=7.0, note='updated')
        assert updated.amount == 7.0
        ok = db.delete_expense(e.id)
        assert ok
        assert db.get_expense(e.id) is None
        # Clear references to allow file cleanup
        db = None
        time.sleep(0.1)
    finally:
        try:
            os.unlink(fp.name)
        except PermissionError:
            # WAL mode auxiliary files may still be open
            for suffix in ['-wal', '-shm']:
                try:
                    os.unlink(fp.name + suffix)
                except (FileNotFoundError, PermissionError):
                    pass
            try:
                time.sleep(0.2)
                os.unlink(fp.name)
            except PermissionError:
                pass  # Accept that cleanup may not work on Windows
