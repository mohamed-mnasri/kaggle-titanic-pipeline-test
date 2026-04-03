import pandas as pd
import sqlite3

def run_pipeline():
    print("🚀 Starting ETL Pipeline...")
    
    # 1. EXTRACT: Read the famous Kaggle Titanic CSV directly from the web
    url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
    df = pd.read_csv(url)
    print(f"📥 Extracted {len(df)} rows.")

    # 2. TRANSFORM: Clean missing data and group by passenger class
    df['Age'] = df['Age'].fillna(df['Age'].mean()) # Fill missing ages
    df['Survived_Status'] = df['Survived'].map({1: 'Survived', 0: 'Died'})
    
    # 3. LOAD: Save to a local SQLite database
    conn = sqlite3.connect('titanic.db')
    df.to_sql('passengers', conn, if_exists='replace', index=False)
    conn.close()
    
    print("✅ ETL Complete! Data loaded into titanic.db")

if __name__ == "__main__":
    run_pipeline()