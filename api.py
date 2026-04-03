from fastapi import FastAPI
import sqlite3

app = FastAPI(title="Titanic Data API")

def get_db():
    conn = sqlite3.connect('titanic.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.get("/survival-by-class")
def get_survival_rates():
    """Calculates survival rates based on passenger class."""
    conn = get_db()
    cursor = conn.cursor()
    # SQL query to get survival percentage by class
    cursor.execute("""
        SELECT Pclass, AVG(Survived) as survival_rate 
        FROM passengers 
        GROUP BY Pclass
    """)
    rows = cursor.fetchall()
    conn.close()
    
    # Format the data for the API
    return {f"Class_{row['Pclass']}": round(row['survival_rate'] * 100, 2) for row in rows}