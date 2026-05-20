from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# PostgreSQL Connection
DATABASE_URL = "postgresql://postgres:$Cooby04@localhost/studentsdb"

# Engine
engine = create_engine(DATABASE_URL)

# Base Class
Base = declarative_base()

# Table Model
class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

# Create Table
Base.metadata.create_all(bind=engine)

# Session
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()

# INSERT DATA DIRECTLY
student1 = Student(name="Suchi", age=21)
student2 = Student(name="Ravi", age=22)

# Add data
session.add(student1)
session.add(student2)

# Save permanently
session.commit()

print("Data Inserted Successfully")