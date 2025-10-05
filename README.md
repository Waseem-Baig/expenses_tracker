# 💰 Professional Expense Tracker

A sleek and modern personal expense tracking application featuring a **stunning professional black theme UI**. Built with Python, FastAPI, and SQLite for powerful expense management with both command-line and web interfaces.

## ✨ Features

### 🎨 **Professional Black Theme UI**

- **Complete Black Design** - Elegant pure black background with professional grey text hierarchy
- **Modern Card Layout** - Clean, professional cards without distracting animations
- **Responsive Design** - Perfect on desktop, tablet, and mobile devices
- **Professional Tables** - Clean black tables with excellent readability
- **Category Badges** - Color-coded category indicators with professional styling

### 💼 **Core Functionality**

- ✅ **Add expenses** with amount, date, note, and category
- ✅ **View and manage** expenses in a beautiful professional interface
- ✅ **Edit and update** existing expenses with ease
- ✅ **Delete** expenses with confirmation
- ✅ **Real-time summaries** (total spending, by category, by month)
- ✅ **Advanced filtering** by date range and category
- ✅ **CSV export** for data analysis
- ✅ **Data validation** and error handling

### 🚀 **Two Powerful Interfaces**

1. **🌐 Professional Web Interface** - Beautiful black theme UI for daily use
2. **🖥️ Command Line Interface (CLI)** - Perfect for quick operations and automation

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

### 🌐 Professional Web Interface (Recommended)

1. **Start the server using the simple startup script:**

   ```bash
   cd expense_tracker
   python start_server.py
   ```

2. **Open your browser** and go to: **http://127.0.0.1:8000**

3. **Enjoy the Professional Black Theme UI:**
   - 🎨 **Beautiful Interface** - Clean, professional black design
   - 💰 **Add Expenses** - Intuitive forms with professional styling
   - 📊 **View Data** - Elegant tables with perfect readability
   - 🔍 **Smart Filtering** - Filter by date range and category
   - ✏️ **Edit/Delete** - Manage expenses with professional controls
   - 📥 **Export CSV** - Download your data for analysis
   - 📈 **Live Summaries** - Real-time spending insights

### 🎯 Alternative Startup Methods

**Method 1: Direct uvicorn command**

```bash
python -m uvicorn expense_tracker.web:app --host 127.0.0.1 --port 8000 --reload
```

**Method 2: Using the startup script (Recommended)**

```bash
python start_server.py
```

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

### 🎨 **Professional Web Interface**

- **🏠 Main Dashboard**: Professional black theme with summary cards showing total spent, categories, and monthly data
- **➕ Add Expenses**: Clean form with professional styling for amount, date, category, and notes
- **📋 Expense Table**: Beautiful black tables with professional typography and hover effects
- **🔍 Smart Filtering**: Filter by date range and category with professional input fields
- **📥 CSV Export**: Download your expense data with a single click
- **🏷️ Category Badges**: Color-coded professional badges for easy expense categorization
- **📱 Responsive Design**: Perfect experience on all devices with the same professional theme

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
├── start_server.py            # 🚀 Easy server startup script (RECOMMENDED)
├── cli.py                     # 🖥️ Command-line interface
├── expense_tracker/
│   ├── __init__.py           # Package initialization
│   ├── db.py                 # 💾 Database operations (SQLite)
│   └── web.py                # 🌐 FastAPI web application
├── templates/
│   ├── index.html            # 🏠 Main dashboard with professional black theme
│   └── edit.html             # ✏️ Edit expense form
├── static/
│   ├── style.css             # 🎨 Professional black theme CSS
│   └── app.js                # ⚡ JavaScript functionality
├── tests/
│   └── test_db.py           # 🧪 Unit tests
├── requirements.txt          # 📦 Python dependencies
├── setup.py                  # ⚙️ Package setup
├── README.md                 # 📖 This file
└── .gitignore               # 🚫 Git ignore rules (comprehensive)
```

## 💾 Data Storage

- **Database**: SQLite database stored at `d:/.expense_tracker.db` by default
- **Schema**: Simple expenses table with id, amount, date, note, category columns
- **Backup**: The SQLite file can be copied for backup/restore
- **Configuration**: Database path can be changed via `EXPENSE_DB` environment variable

## 🔧 API Endpoints (Web Interface)

| Method | Endpoint     | Description                                |
| ------ | ------------ | ------------------------------------------ |
| GET    | `/`          | Main dashboard with expense list and forms |
| POST   | `/add`       | Add new expense                            |
| GET    | `/edit/{id}` | Edit expense form                          |
| POST   | `/edit/{id}` | Update expense                             |
| POST   | `/delete`    | Delete expense                             |
| GET    | `/export`    | Export expenses to CSV                     |

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

### 🎨 **Professional Black Theme**

The application features a stunning **complete black theme** designed for professional use:

- **🖤 Pure Black Backgrounds** - `#000000` throughout the interface
- **📝 Professional Grey Text** - Multiple shades for perfect hierarchy
- **🎯 Clean Design** - No distracting animations or flashy effects
- **💼 Business Ready** - Professional styling suitable for work environments
- **👁️ Easy on Eyes** - Reduced eye strain with dark theme
- **📱 Responsive** - Maintains professional appearance on all devices

### 🛠️ **Running in Development Mode**

```bash
# Start with the easy startup script (Recommended)
python start_server.py

# Alternative: Direct uvicorn command with auto-reload
python -m uvicorn expense_tracker.web:app --reload --host 127.0.0.1 --port 8000

# Run tests
pytest tests/ -v

# Use CLI commands
python cli.py --help
```

### 📦 **Dependencies**

- **FastAPI** - Modern, fast web framework for building APIs
- **Uvicorn** - Lightning-fast ASGI server for FastAPI
- **Jinja2** - Powerful template engine for HTML rendering
- **SQLite3** - Lightweight database (built into Python)
- **pytest** - Professional testing framework

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

## 🎯 **Why Choose This Expense Tracker?**

- **🎨 Professional Design** - Beautiful black theme that's easy on the eyes
- **⚡ Fast & Reliable** - Built with modern FastAPI framework
- **💾 Secure Storage** - Local SQLite database keeps your data private
- **📱 Responsive** - Works perfectly on desktop, tablet, and mobile
- **🚀 Easy to Use** - Intuitive interface with professional styling
- **📊 Powerful Features** - Filtering, categorization, export, and summaries
- **🔧 Developer Friendly** - Clean code structure with comprehensive documentation

## 🌟 **Getting Started is Easy!**

1. **Clone** this repository
2. **Install** dependencies: `pip install -r requirements.txt`
3. **Run** the server: `python start_server.py`
4. **Open** http://127.0.0.1:8000 in your browser
5. **Enjoy** your professional expense tracker! 🎉

---

**✨ Start managing your expenses with style! Your professional black theme expense tracker awaits. 💰�**
