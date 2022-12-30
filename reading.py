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


# Get all data
students = session.query(Student)

for student in students:
    print(student.id, student.name, student.age, student.grade)

# Get data in order
students = session.query(Student).order_by(Student.name)
for student in students:
    print(student.id, student.name, student.age, student.grade)


# Get data by filtering
students = session.query(Student).filter((Student.name == "Aarvik"))


for student in students:
    print(student.name, student.age)

# Count the number of results
student_count = session.query(Student).count()
print(student_count)
