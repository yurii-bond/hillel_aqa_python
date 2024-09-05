from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker

from lecture_22.my_models import User, Base

DATABASE_URL = "postgresql+psycopg2://p14s:aswdertf@localhost/demo_hillel"
engine = create_engine(DATABASE_URL)

# Creates tables in the DB
Base.metadata.create_all(engine)

# Creates session
Session = sessionmaker(bind=engine)
session = Session()


# INSERT
new_user = User(name='John', age=30)
session.add(new_user)
session.add_all([
    User(name='Alice', age=25),
    User(name='Bob', age=35),
    User(name='Jack', age=40)
])
session.commit()

# UPDATE
user = session.query(User).filter_by(name='John').first()
# user = session.query(User)
# print(user)
# for u in user:
#     print(u)
#     print(u.id)
#     print(u.name)
#     print(u.age)
user.age = 31
session.commit()

# DELETE
session.delete(user)
session.commit()

# Get all records
all_usrs = session.query(User).all()
print(all_usrs)

# SORTING
sorted_users = session.query(User).order_by(User.age.asc()).all()
print(sorted_users)

# Get average
average_age = session.query(func.avg(User.age)).scalar()
print('Average age of all users is:', average_age)

# Get count
user_count = session.query(func.count(User.id)).scalar()
print('Users quantity:', user_count)