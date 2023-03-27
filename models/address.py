from sqlalchemy import Table, Column, Integer, String, REAL, TEXT
from config.database import meta

address = Table(
    "address", meta,
    Column('id', Integer, primary_key=True),
    Column('latitude', REAL, nullable=False),
    Column('longitude', REAL, nullable=False),
    Column('street', TEXT, nullable=False),
    Column('city', String(50), nullable=False),
    Column('state', String(100), nullable=False),
    Column('zip_code', Integer, nullable=False),
)