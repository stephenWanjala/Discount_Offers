import pandas as pd
import sqlite3
import os

def export_db_to_excel(db_path, excel_path):
    """
    Export all tables from the SQLite database to an Excel file.
    
    Args:
        db_path (str): Path to the SQLite database file.
        excel_path (str): Path where the Excel file will be saved.
    """
    # Connect to the SQLite database
    conn = sqlite3.connect(db_path)
    
    # Fetch all table names
    query = "SELECT name FROM sqlite_master WHERE type='table';"
    tables = pd.read_sql(query, conn)
    
    # Create a Pandas Excel writer
    with pd.ExcelWriter(excel_path, engine='openpyxl') as writer:
        for table_name in tables['name']:
            # Read the table into a DataFrame
            df = pd.read_sql(f"SELECT * FROM {table_name};", conn)
            # Write the DataFrame to a sheet in the Excel file
            df.to_excel(writer, sheet_name=table_name, index=False)
    
    # Close the database connection
    conn.close()
