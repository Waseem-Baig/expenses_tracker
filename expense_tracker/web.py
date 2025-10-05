from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse, PlainTextResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from expense_tracker.db import ExpenseDB
from typing import Optional

app = FastAPI(title="Expense Tracker")
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get('/', response_class=HTMLResponse)
def index(request: Request, start: Optional[str] = None, end: Optional[str] = None, category: Optional[str] = None):
    db = ExpenseDB()
    expenses = db.filter_expenses(start_date=start, end_date=end, category=category)
    total = db.total_spent()
    by_cat = db.summary_by_category()
    by_month = db.summary_by_month()
    return templates.TemplateResponse('index.html', {'request': request, 'expenses': expenses, 'total': total, 'by_cat': by_cat, 'by_month': by_month})


@app.post('/add')
def add(amount: float = Form(...), date: str = Form(...), note: str = Form(''), category: str = Form(None)):
    db = ExpenseDB()
    try:
        db.add_expense(amount, date, note, category)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    return RedirectResponse(url='/', status_code=303)


@app.post('/delete')
def delete(id: int = Form(...)):
    db = ExpenseDB()
    db.delete_expense(id)
    return RedirectResponse(url='/', status_code=303)


@app.get('/edit/{id}', response_class=HTMLResponse)
def edit_get(request: Request, id: int):
    db = ExpenseDB()
    e = db.get_expense(id)
    if not e:
        raise HTTPException(status_code=404)
    return templates.TemplateResponse('edit.html', {'request': request, 'e': e})


@app.post('/edit/{id}')
def edit_post(id: int, amount: float = Form(...), date: str = Form(...), note: str = Form(''), category: str = Form(None)):
    db = ExpenseDB()
    try:
        db.update_expense(id, amount=amount, date=date, note=note, category=category)
    except Exception as exc:
        raise HTTPException(status_code=400, detail=str(exc))
    return RedirectResponse(url='/', status_code=303)


@app.get('/export')
def export(start: Optional[str] = None, end: Optional[str] = None, category: Optional[str] = None):
    db = ExpenseDB()
    csv_data = db.export_csv(start_date=start, end_date=end, category=category)
    return PlainTextResponse(csv_data, media_type='text/csv')
