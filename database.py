from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = "sqlite:///.book.db"  # SQLite database location

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={
        "check_same_thread": False
    },  # SQLite specific argument: allows connections to be shared across threads
)
SessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine
)  # Create a configured "Session" class
Base = declarative_base()  # Base class for our classes definitions
