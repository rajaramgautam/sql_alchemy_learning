from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(
    'postgresql://rajaramgautam:Aarvik2021@localhost:5432/alchemy', echo=False)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)
    grade = Column(String(50))


# Update data
student = session.query(Student).filter(Student.name == "Rajaram").first()
student.name = "Aarvik"
session.commit()
