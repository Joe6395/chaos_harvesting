from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, DateTime, func
from app.db import engine

Base = declarative_base()

class Insight(Base):
    __tablename__ = "insights"
    id = Column(Integer, primary_key=True, index=True)
    source = Column(String, index=True)
    content = Column(Text)
    created_at = Column(DateTime, default=func.now())

Base.metadata.create_all(bind=engine)