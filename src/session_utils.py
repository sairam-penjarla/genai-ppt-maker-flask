import sqlite3
import json
from typing import List, Dict
from custom_logger import logger

class sessionUtilities:
    def __init__(self, db_name: str = "sessions.db"):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name, check_same_thread=False)
        logger.info(f"Connected to the database: {self.db_name}")
        self.create_tables()

    def create_tables(self):
        # Create tables if they don't exist
        logger.info("Creating tables if they don't exist...")
        with self.conn:
            self.conn.execute('''
                              CREATE TABLE IF NOT EXISTS sessions (
                              session_id TEXT,
                              prompt TEXT,
                              slides_planning TEXT,
                              slides_content TEXT
                              )''')
            
        logger.info("Tables created or already exist.")

    def add_slides(self, session_id: str, prompt: str, slides_planning:str, slides_content: str):
        logger.info(f"Adding slides data to session: {session_id}...")
        with self.conn:
            self.conn.execute(
                '''INSERT INTO sessions 
                   (session_id, prompt, slides_planning, slides_content) 
                   VALUES (?, ?, ?, ?)''',
                (session_id, prompt, slides_planning, slides_content)
            )

    def get_session_data(self, session_id: str):
        """
        Retrieve conversation data for the given session_id.
        Returns a dictionary where each key is a prompt and the value is a dictionary containing:
        - slides_planning: List of slides_planning entries for the prompt.
        - slides_content: List of slides_content entries for the prompt.
        """
        logger.info(f"Retrieving slide data for session: {session_id}")
        session_data = []
        with self.conn:
            results = self.conn.execute(
                '''SELECT prompt, slides_planning, slides_content
                FROM sessions
                WHERE session_id = ?''', (session_id,)
            ).fetchall()

            
            if results:
                logger.info(f"Retrieved {len(results)} entries for session_id: {session_id}")
                # Create a dictionary to organize data by prompt
                for row in results:
                    prompt = row[0]
                    slides_planning = row[1]
                    slides_content = row[2]
                    
                    request = {
                        prompt : {
                                    "slides_planning": slides_planning,
                                    "slides_content": slides_content
                                }
                    }
                    session_data.append(request)
                
            return session_data
            

    
    def close(self):
        # Close the database connection
        logger.info("Closing database connection...")
        self.conn.close()
        logger.info("Database connection closed.")

    def get_session_meta_data(self) -> Dict[str, str]:
        """
        Fetch the very first prompt for each session_id.
        
        Returns:
            Dict[str, str]: A dictionary where keys are session_ids and values are the first prompts.
        """
        # Query to get the first prompt for each session_id based on rowid
        query = '''
        SELECT session_id, MIN(rowid) as first_rowid
        FROM sessions
        GROUP BY session_id
        '''
        
        # Execute the query to get the first rowid for each session_id
        cursor = self.conn.cursor()
        cursor.execute(query)
        session_first_rows = cursor.fetchall()

        # Prepare the result dictionary
        result = {}
        for session_id, first_rowid in session_first_rows:
            # Query to get the prompt for the first rowid of the session
            cursor.execute(
                '''
                SELECT prompt
                FROM sessions
                WHERE session_id = ? AND rowid = ?
                ''',
                (session_id, first_rowid)
            )
            row = cursor.fetchone()
            if row:
                result[session_id] = row[0]  # Map session_id to the first prompt

        return result

    def delete_all_sessions(self):
        try:
            self.conn.execute("DELETE FROM sessions")
            self.conn.commit()
            return {"message": "All sessions deleted successfully."}, 200
        except Exception as e:
            print(f"Error deleting all sessions: {e}")
            return {"error": "Failed to delete sessions."}, 500

    def delete_session(self, session_id: str):
        try:
            self.conn.execute("DELETE FROM sessions WHERE session_id = ?", (session_id,))
            self.conn.commit()
            return {"message": "Session deleted successfully."}, 200
        except Exception as e:
            print(f"Error deleting session {session_id}: {e}")
            return {"error": "Failed to delete session."}, 500