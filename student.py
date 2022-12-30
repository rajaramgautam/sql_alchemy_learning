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


# This code will do migration
# Base.metadata.create_all(engine)


# creating instance of the class Student
student1 = Student(name="Rajaram", age=27, grade="Masters")

student2 = Student(name="Aaravi", age=22, grade="Bachelors")
student3 = Student(name="Aayara", age=22, grade="Bachelors")
student4 = Student(name="Aarvik", age=22, grade="Bachelors")

# inserting data into table student
# session.add(student1)

# inserting more than one row at a time
session.add_all([student2, student3, student4])

# commit
session.commit()
