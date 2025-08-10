# In threat-feed-app/database.py
import sqlite3
import os

DATABASE_NAME = 'threat_history.db'

def init_db():
    """Initializes the database and creates the necessary tables."""
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    # Table to store metadata for each scan
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS scans (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            scan_type TEXT NOT NULL,
            scan_time TEXT NOT NULL,
            article_count INTEGER NOT NULL
        )
    ''')
    # Table to store the articles found in each scan
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS articles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            scan_id INTEGER NOT NULL,
            source TEXT NOT NULL,
            title TEXT NOT NULL,
            link TEXT NOT NULL,
            published TEXT NOT NULL,
            FOREIGN KEY (scan_id) REFERENCES scans (id)
        )
    ''')
    conn.commit()
    conn.close()
    print("Database initialized successfully.")

def delete_db():
    """Deletes the entire database file."""
    if os.path.exists(DATABASE_NAME):
        os.remove(DATABASE_NAME)
        print("Database deleted successfully.")
    else:
        print("Database file not found.")

# When you run this file directly, it will initialize the database.
if __name__ == '__main__':
    init_db()