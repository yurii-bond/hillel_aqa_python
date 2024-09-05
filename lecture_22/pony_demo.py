from pony.orm import Database, Required, Set, db_session

db = Database(
    provider='postgres',
    user='p14s',
    password='aswdertf',
    host='localhost',
    database='demo_hillel'
)

class Department(db.Entity):
    name = Required(str)
    employees = Set('Employee')

class Employee(db.Entity):
    name = Required(str)
    department = Required('Department')

# Creates tables
db.generate_mapping(create_tables=True)

with db_session:
    it_department = Department(name='IT')
    john = Employee(name='John', department=it_department)
    db.commit()

@db_session
def add_employee():
    devops_departament = Department(name='DevOps')
    bob = Employee(name='Bob', department=devops_departament)
    db.commit()

add_employee()

with db_session:
    employees = Employee.select(lambda e: e.name == 'Bob')
    print(employees.order_by(Employee.name).get_sql())
    sorted_emp = employees.order_by(Employee.name).get_sql()
    print(employees)