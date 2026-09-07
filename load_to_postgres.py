from dotenv import load_dotenv
import os
from sqlalchemy import create_engine
from sqlalchemy import schema

load_dotenv()

postgres_host = os.getenv("POSTGRES_HOST")
postgres_port = os.getenv("POSTGRES_PORT")
postgres_db = os.getenv("POSTGRES_DB")
postgres_user = os.getenv("POSTGRES_USER")
postgres_password = os.getenv("POSTGRES_PASSWORD")

connection_string = f"postgresql://{postgres_user}:{postgres_password}@{postgres_host}:{postgres_port}/{postgres_db}"
engine = create_engine(connection_string)

def load_data_to_postgres(dataframe, table_name, engine, schema, if_exists='replace', index=False):
    """
    Load a pandas DataFrame to a PostgreSQL table.

    :param dataframe: The pandas DataFrame to load.
    :param table_name: The name of the target table in PostgreSQL.
    :param engine: SQLAlchemy engine object for the PostgreSQL connection.
    :param schema: The schema name for the target table.
    :param if_exists: What to do if the table already exists ('fail', 'replace', 'append').
    :param index: Whether to write the DataFrame's index as a column.
    """
    try:
        dataframe.to_sql(table_name, engine, schema=schema, if_exists=if_exists, index=index)
        print(f"Data loaded successfully into {table_name} table.")
        return True
    except Exception as e:
        print(f"Error loading data into PostgreSQL: {e}")
        return False