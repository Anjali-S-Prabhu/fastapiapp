from sqlalchemy import Column,Integer,String
from database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(225), unique=True, index=True)
    email = Column(String(225), unique=True, index=True)
    hashed_password = Column(String(255), nullable=False)
    role = Column(String(225), nullable=False,default="Candidate")
    