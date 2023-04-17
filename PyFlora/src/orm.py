from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


db_path = "PyFlora/src/pyflora.db"
#'sqlite:///my_database.db'


# In this model, we define the User class as a subclass of Base from declarative_base().
# We also define the __tablename__ attribute to specify the name of the SQLite table.
# Finally, we define the id, name, and age columns using the Column class.

Base = declarative_base()


# create a model for a User table:

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    username = Column(String)
    surname = Column(String)

    def __repr__(self):
        return f"<User(name='{self.name}', age={self.age})>"


class Plant(Base):
    __tablename__ = 'plants'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    image_path = Column(String)

    def __repr__(self):
        return f"<Post(title='{self.title}')>"


class Bucket(Base):
    __tablename__ = 'buckets'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    planted_plant = Column(String)

    def __repr__(self):
        return f"<Post(title='{self.title}')>"



# create an engine that connects to the SQLite database:
engine = create_engine(db_path, echo=True)


# Next, create the tables in the database using the
Base.metadata.create_all(bind=engine)


# create session with db
Session = sessionmaker(bind=engine)
session = Session()


# Create a new user
def create_user(name, email, password, username, surname):
    user = User(name, email, password, username, surname)
    session.add(user)
    session.commit()


# Read all users
def read_users():
    users = session.query(User).all()
    for user in users:
        print(user)


# Update a user
def update_user_by_name(name, email, password, username, surname):
    
    user = session.query(User).filter_by(name).first()
    user.name = name
    user.email = email
    user.password = password
    user.username = username
    user.surname = surname
    
    session.commit()

# Delete a user
def delete_user_by_name(name):
    user = session.query(User).filter_by(name).first()
    session.delete(user)
    session.commit()


# Create a new plant
def create_plant(name, image_path):
    plant = Plant(name,image_path)
    session.add(plant)
    session.commit()


# Read all plants
def read_plants():
    plants = session.query(Plant).all()
    for plant in plants:
        print(plant)


# Update a plant
def update_plant_by_name(name, image_path):
    
    plant = session.query(Plant).filter_by(name).first()
    plant.name = name
    plant.image_path = image_path
    
    session.commit()


# Delete a plant
def delete_plant_by_name(name):
    plant = session.query(Plant).filter_by(name).first()
    session.delete(plant)
    session.commit()


# Create a new plant
def create_plant(name, image_path):
    plant = Plant(name,image_path)
    session.add(plant)
    session.commit()


# Read all plants
def read_plants():
    plants = session.query(Plant).all()
    for plant in plants:
        print(plant)


# Update a plant
def update_plant_by_name(name, image_path):
    
    plant = session.query(Plant).filter_by(name).first()
    plant.name = name
    plant.image_path = image_path
    
    session.commit()


# Delete a plant
def delete_plant_by_name(name):
    plant = session.query(Plant).filter_by(name).first()
    session.delete(plant)
    session.commit()


# Create a new bucket
def create_bucket(name, planted_plant):
    bucket = Bucket(name, planted_plant)
    session.add(bucket)
    session.commit()


# Read all buckets
def read_buckets():
    buckets = session.query(Bucket).all()
    for bucket in buckets:
        print(bucket)


# Update a bucket
def update_bucket_by_name(name, planted_plant):
    
    bucket = session.query(Bucket).filter_by(name).first()
    bucket.name = name
    bucket.planted_plant = planted_plant
    
    session.commit()


# Delete a bucket
def delete_bucket_by_name(name):
    bucket = session.query(Bucket).filter_by(name).first()
    session.delete(bucket)
    session.commit()
