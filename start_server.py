#!/usr/bin/env python3
"""Start the expense tracker server"""

import sys
import os
import subprocess

# Change to the correct directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

try:
    # Try to start the server
    print("🚀 Starting Expense Tracker Server...")
    print("🌟 Server will be available at: http://127.0.0.1:8000")
    print("✨ Your professional black theme UI is ready!")
    
    subprocess.run([
        sys.executable, "-m", "uvicorn", 
        "expense_tracker.web:app", 
        "--host", "127.0.0.1", 
        "--port", "8000",
        "--reload"
    ])
    
except KeyboardInterrupt:
    print("\n👋 Server stopped.")
except Exception as e:
    print(f"❌ Error: {e}")
    print("\n📦 Make sure you have installed the dependencies:")
    print("pip install fastapi uvicorn jinja2")