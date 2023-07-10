from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.ent.database import DBContext

def update_user(db: "DBContext",id, first_name, last_name, password, active):
    db.update(id, first_name, last_name, password, active)

def insert_user(db: "DBContext", first_name, last_name, password, active):
    return db.add(first_name, last_name, password, active)

def delete_user(db: "DBContext",id):
    db.delete(int(id))

def get_items(db: "DBContext"):
    return db.all()

def get_by_id(db: "DBContext", id):
    return db.get_by_id(int(id))