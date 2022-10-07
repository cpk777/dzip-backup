from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import DDL

# The following lines of code perform the SQLAlchemy standard connection:
conn_str = 'clickhouse://default:@localhost/default'
engine = create_engine(conn_str)
session = sessionmaker(bind=engine)()

# Create a new database
database = 'test'
engine.execute(DDL(f'CREATE DATABASE IF NOT EXISTS {database}'))