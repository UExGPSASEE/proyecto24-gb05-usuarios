from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configura la URL de conexión a PostgreSQL
DATABASE_URL = "postgresql://postgres:12345@localhost:5432/ASEE"

# Crea la base de datos con SQLAlchemy
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
