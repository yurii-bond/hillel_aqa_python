from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

# З'єднання з базою даних PostgreSQL (замініть дані на ваші)
DATABASE_URL = "postgresql://p14s:aswdertf@localhost/demo_hillel"
engine = create_engine(DATABASE_URL)

# Створення базового класу для визначення моделей даних
Base = declarative_base()

# Визначення моделей даних (таблиць) за допомогою класів
class Department(Base):
    __tablename__ = 'departments_new'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    # Встановлення відношення "один до багатьох" з таблицею Employee
    employees = relationship("Employee", back_populates="department")

class Employee(Base):
    __tablename__ = 'employees_new'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    department_id = Column(Integer, ForeignKey('departments_new.id'))

    # Встановлення відношення "багато до одного" з таблицею Department
    department = relationship("Department", back_populates="employees")

# Створення таблиць у базі даних
Base.metadata.create_all(engine)

# Створення сесії для взаємодії з базою даних
Session = sessionmaker(bind=engine)
session = Session()

# Додавання департаментів та співробітників до бази даних
it_department = Department(name='IT')
hr_department = Department(name='HR')

john = Employee(name='John', department=it_department)
alice = Employee(name='Alice', department=hr_department)
bob = Employee(name='Bob', department=it_department)

session.add_all([it_department, hr_department, john, alice, bob])
session.commit()

# Вибірка співробітників та їх департаментів
employees = session.query(Employee).all()
for employee in employees:
    print(f"Ім'я: {employee.name}, Департамент: {employee.department.name}")

# # Transaction
# session.begin()
# session.commit()
# session.rollback()
# session.close()

# Закриття сесії
session.close()