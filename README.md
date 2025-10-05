# Personal Expense Tracker

A comprehensive personal expense tracking application with both **command-line** and **web** interfaces. Built with Python, SQLite, and FastAPI.

## 🚀 Features

### Core Functionality
- ✅ **Add expenses** with amount, date, note, and category
- ✅ **View and list** all expenses with filtering
- ✅ **Edit and update** existing expenses
- ✅ **Delete** expenses
- ✅ **Generate summaries** (total spending, by category, by month)
- ✅ **Filter expenses** by date range and category
- ✅ **Export data** to CSV format
- ✅ **Data validation** (positive amounts, ISO dates)

### Two Interfaces
1. **🖥️ Command Line Interface (CLI)** - Perfect for quick operations and automation
2. **🌐 Web Interface** - User-friendly browser-based UI with forms and tables

## 📋 Requirements

- Python 3.8+
- SQLite (included with Python)

## 🛠️ Installation

1. **Clone or download** this project to your local machine

2. **Navigate to the project directory:**
   ```bash
   cd expense_tracker
   ```

3. **Create and activate virtual environment:**
   ```bash
   python -m venv .venv
   
   # On Windows (Git Bash/CMD):
   .venv/Scripts/activate
   
   # On macOS/Linux:
   source .venv/bin/activate
   ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Install the package in development mode:**
   ```bash
   pip install -e .
   ```

## 🚀 Quick Start

### Web Interface (Recommended)

1. **Start the web server:**
   ```bash
   .venv/Scripts/uvicorn expense_tracker.web:app --host 127.0.0.1 --port 8000 --reload
   ```

2. **Open your browser** and go to: http://127.0.0.1:8000/

3. **Use the web interface to:**
   - Add expenses using the form
   - View expenses in a sortable table
   - Filter by date range or category
   - Edit or delete expenses
   - Export data to CSV
   - View spending summaries

### Command Line Interface

```bash
# Add an expense
.venv/Scripts/python cli.py add 25.50 -n "Lunch at cafe" -c food

# Add with specific date
.venv/Scripts/python cli.py add 120.00 -d 2025-10-01 -n "Monthly subscription" -c utilities

# List all expenses
.venv/Scripts/python cli.py list

# Get spending summary
.venv/Scripts/python cli.py summary

# View specific expense
.venv/Scripts/python cli.py get 1

# Update an expense
.venv/Scripts/python cli.py update 1 --amount 30.00 --note "Updated lunch cost"

# Delete an expense
.venv/Scripts/python cli.py delete 1
```

## 📊 Usage Examples

### Web Interface Screenshots
- **Main Dashboard**: Add expenses, view list, see summaries
- **Filtering**: Filter by date range or category
- **Export**: Download your data as CSV

### CLI Examples

```bash
# Add a coffee expense
$ .venv/Scripts/python cli.py add 4.75 -n "Morning coffee" -c beverages
Added: Expense(id=1, amount=4.75, date='2025-10-05', note='Morning coffee', category='beverages')

# Add a grocery expense with specific date
$ .venv/Scripts/python cli.py add 67.32 -d 2025-10-04 -n "Weekly groceries" -c food
Added: Expense(id=2, amount=67.32, date='2025-10-04', note='Weekly groceries', category='food')

# List all expenses
$ .venv/Scripts/python cli.py list
ID      DATE            AMOUNT  CATEGORY        NOTE
2       2025-10-04      67.32   food            Weekly groceries
1       2025-10-05      4.75    beverages       Morning coffee

# Get summary
$ .venv/Scripts/python cli.py summary
Total: 72.07

By category:
  food: 67.32
  beverages: 4.75
```

## 🗂️ Project Structure

```
expense_tracker/
├── cli.py                      # Command-line interface
├── expense_tracker/
│   ├── __init__.py            # Package initialization
│   ├── db.py                  # Database operations (SQLite)
│   └── web.py                 # FastAPI web application
├── templates/
│   ├── index.html             # Main web interface
│   └── edit.html              # Edit expense form
├── static/                    # Static files (CSS, JS, images)
├── tests/
│   └── test_db.py            # Unit tests
├── requirements.txt           # Python dependencies
├── setup.py                  # Package setup
├── README.md                 # This file
└── .gitignore                # Git ignore rules
```

## 💾 Data Storage

- **Database**: SQLite database stored at `d:/.expense_tracker.db` by default
- **Schema**: Simple expenses table with id, amount, date, note, category columns
- **Backup**: The SQLite file can be copied for backup/restore
- **Configuration**: Database path can be changed via `EXPENSE_DB` environment variable

## 🔧 API Endpoints (Web Interface)

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Main dashboard with expense list and forms |
| POST | `/add` | Add new expense |
| GET | `/edit/{id}` | Edit expense form |
| POST | `/edit/{id}` | Update expense |
| POST | `/delete` | Delete expense |
| GET | `/export` | Export expenses to CSV |

Query parameters for filtering:
- `start` - Start date (YYYY-MM-DD)
- `end` - End date (YYYY-MM-DD)  
- `category` - Filter by category

## 🧪 Testing

Run the unit tests:
```bash
.venv/Scripts/pytest tests/ -v
```

## 🔒 Data Validation

- **Amount**: Must be positive number
- **Date**: Must be in ISO format (YYYY-MM-DD)
- **Category**: Optional, can be any string
- **Note**: Optional, can be any string

## 🛠️ Development

### Running in Development Mode

```bash
# Start web server with auto-reload
.venv/Scripts/uvicorn expense_tracker.web:app --reload --host 127.0.0.1 --port 8000

# Run tests
.venv/Scripts/pytest

# Run CLI commands
.venv/Scripts/python cli.py --help
```

### Dependencies

- **FastAPI**: Modern web framework for the API
- **Uvicorn**: ASGI server for FastAPI
- **Jinja2**: Template engine for HTML rendering
- **SQLite3**: Database (built into Python)
- **pytest**: Testing framework

## 🐛 Troubleshooting

### Common Issues

1. **Port 8000 already in use**:
   ```bash
   # Find process using port 8000
   netstat -ano | findstr ":8000"
   # Kill the process by PID
   taskkill /PID <PID> /F
   ```

2. **SQLite permission errors**:
   - Ensure the directory for the database file is writable
   - Check that no other process is using the database file

3. **Module not found errors**:
   ```bash
   # Reinstall in development mode
   pip install -e .
   ```

### Getting Help

- Check the terminal output for error messages
- Ensure virtual environment is activated
- Verify all dependencies are installed: `pip list`

## 📝 License

This project is provided as-is for personal use and learning purposes.

## 🤝 Contributing

This is a personal expense tracker project. Feel free to fork and modify for your own needs!

---

**Happy expense tracking! 💰📊**