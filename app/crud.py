from app.models import Insight
from app.db import SessionLocal

def save_insight(source: str, content: str):
    db = SessionLocal()
    insight = Insight(source=source, content=content)
    db.add(insight)
    db.commit()
    db.refresh(insight)
    db.close()
    return insight