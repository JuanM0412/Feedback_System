from sqlalchemy import Column, Integer, String, Text
from src.core.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True)
    password = Column(String(255))
    username = Column(String(100))
    evaluation_rubric = Column(Text)
    business_summary = Column(Text)
    folder_id = Column(Text, nullable=True)
    sheet_id = Column(Text, nullable=True)