from hashlib import sha256
from pathlib import Path

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from src.model.user import User
from src.ent.entities.base import Base


class DBContext:
    def __init__(self) -> None:
        path = Path(__file__).parent / "access_control.db"
        if not path.exists():
            self.engine = create_engine(f"sqlite:///{path}")
            self._initial_load()
        else:
            self.engine = create_engine(f"sqlite:///{path}")


    def _initial_load(self):
        Base.metadata.create_all(self.engine)
        session = sessionmaker(bind=self.engine)()
        password = sha256("0000".encode("UTF-8")).hexdigest()
        admin = User(first_name="Admin", last_name="Admin", password=password, active=True, system=True)
        session.add(admin)
        session.commit()


    def login(self, password):
        session = sessionmaker(bind=self.engine)()
        pwd = sha256(password.encode("UTF-8")).hexdigest()
        return session.query(User).filter_by(password=pwd).first()
    
    
    def add(self, first_name, last_name, password, active):
        pwd = sha256(password.encode("UTF-8")).hexdigest()
        session = sessionmaker(bind=self.engine)()
        usr = session.query(User).filter_by(password=pwd).first()
        
        if usr is None:
            usr = User(first_name=first_name, last_name=last_name, password=pwd, active=active, system=False)
            session.add(usr)
            session.commit()
            session.refresh(usr)
            session.close()
            return usr
        session.close()


    def update(self, id, first_name, last_name, password, active):
        session = sessionmaker(bind=self.engine)()
        pwd = sha256(password.encode("UTF-8")).hexdigest()
        usr = session.query(User).filter_by(id=id).first()
        usr.first_name = first_name
        usr.last_name = last_name 
        usr.password = pwd
        usr.active = active
        session.close()


    def delete(self, id):
        session = sessionmaker(bind=self.engine)()
        usr = session.query(User).filter_by(id=id).first()
        
        if usr:
            session.delete(usr)
            session.commit()
        session.close()


    def all(self):
        session = sessionmaker(bind=self.engine)()
        data = session.query(User).filter_by(system=False).all()
        session.close()
        
        return data
    
    
    def get_by_id(self, id):
        session = sessionmaker(bind=self.engine)()
        data = session.query(User).filter_by(id=id).first()
        session.close()
        
        return data
