import argparse
from expense_tracker.db import ExpenseDB
import sys

def print_exp(e):
    cat = e.category if e.category else ''
    print(f"{e.id}\t{e.date}\t{e.amount:.2f}\t{cat}\t{e.note}")


def main(argv=None):
    argv = argv or sys.argv[1:]
    parser = argparse.ArgumentParser(prog='expense', description='Personal Expense Tracker')
    sub = parser.add_subparsers(dest='cmd')

    add = sub.add_parser('add')
    add.add_argument('amount', type=float)
    add.add_argument('--date', '-d', default=None)
    add.add_argument('--note', '-n', default='')
    add.add_argument('--category', '-c', default=None)

    listp = sub.add_parser('list')
    listp.add_argument('--limit', '-l', type=int, default=None)

    getp = sub.add_parser('get')
    getp.add_argument('id', type=int)

    update = sub.add_parser('update')
    update.add_argument('id', type=int)
    update.add_argument('--amount', type=float, default=None)
    update.add_argument('--date', default=None)
    update.add_argument('--note', default=None)
    update.add_argument('--category', default=None)

    delete = sub.add_parser('delete')
    delete.add_argument('id', type=int)

    summary = sub.add_parser('summary')

    args = parser.parse_args(argv)
    db = ExpenseDB()

    if args.cmd == 'add':
        date = args.date or __import__('datetime').date.today().isoformat()
        try:
            e = db.add_expense(args.amount, date, args.note, args.category)
            print('Added:', e)
        except Exception as ex:
            print('Error:', ex)
            return 2
    elif args.cmd == 'list':
        rows = db.list_expenses(limit=args.limit)
        print('ID\tDATE\tAMOUNT\tCATEGORY\tNOTE')
        for r in rows:
            print_exp(r)
    elif args.cmd == 'get':
        r = db.get_expense(args.id)
        if not r:
            print('Not found')
            return 1
        print_exp(r)
    elif args.cmd == 'update':
        try:
            r = db.update_expense(args.id, amount=args.amount, date=args.date, note=args.note, category=args.category)
            print('Updated:', r)
        except Exception as ex:
            print('Error:', ex)
            return 2
    elif args.cmd == 'delete':
        ok = db.delete_expense(args.id)
        print('Deleted' if ok else 'Not found')
    elif args.cmd == 'summary':
        print('Total:', db.total_spent())
        print('By category:')
        for k, v in db.summary_by_category().items():
            print(f"  {k}: {v:.2f}")
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
