from sqlalchemy import create_engine
import pandas as pd
import os

def load_postgres_table(db_name: str,
                        table_name: str):
    engine = create_engine(f'postgresql://postgres:@localhost/{db_name}')
    return pd.read_sql_table(table_name, engine)

def load_csv_data(dataset_name: str):
    current_directory = os.path.join(os.getcwd(), 'data', dataset_name)
    return pd.read_csv(current_directory)