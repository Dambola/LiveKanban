from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from contextlib import contextmanager

SQLALCHEMY_DATABASE_URI='sqlite:///app.db'

Engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=True)
Base = declarative_base()
Session = sessionmaker(Engine, expire_on_commit=False)

@contextmanager
def scoped_session():
    """Provide a transactional scope around a series of operations."""
    session = Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()