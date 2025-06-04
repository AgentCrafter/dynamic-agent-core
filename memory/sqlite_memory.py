import os
import sqlite3
from datetime import datetime

class SQLiteMemory:
    def __init__(self, db_path='agent_memory.db'):
        self.db_path = os.path.join(os.path.dirname(__file__), db_path)
        self.conn = sqlite3.connect(self.db_path, check_same_thread=False)
        self._init_db()

    def _init_db(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS memory (
                task TEXT,
                result TEXT,
                timestamp TEXT,
                status TEXT
            )
        ''')
        self.conn.commit()

    def save_task(self, task, result, status):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO memory (task, result, timestamp, status) VALUES (?, ?, ?, ?)",
                       (task, result, timestamp, status))
        self.conn.commit()

    def get_all_tasks(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT task, result, timestamp, status FROM memory")
        return cursor.fetchall()

    def reset_memory(self):
        try:
            self.conn.close()
            if os.path.exists(self.db_path):
                os.remove(self.db_path)
                print("[Memory] Database file deleted. Starting fresh.")
            self.conn = sqlite3.connect(self.db_path, check_same_thread=False)
            self._init_db()
        except Exception as e:
            print(f"[Memory] Failed to reset memory: {e}")
