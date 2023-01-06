from sqlalchemy.orm import declarative_base, relationship
from sqlamchemy import Column, Integer, String, Boolean, DateTime, Text, ForeingKey

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(120), nullable=False)
    active = Column(Boolean(), default=True)
    #roles_id = Column(Integer, ForeingKey("roles.id"), nullable=False)

    profile = relationship("Profile", uselist=False) # [<Profile 10>] => <Profile 10>

    roles = relationship("Role", secondary="roles_users") # []
    todos = relationship("Todo", backref="user") # []

"""
CREATE TABLE users (
    id integer not null,
    email varchar(120),
    password varchar(120),
    active boolean default true,
    primary key (id),
    unique key (email)
);
"""

class Role(Base):
    __tablename__ = "roles"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)

"""
CREATE TABLE roles (
    id integer not null,
    name varchar(120),
    primary key (id),
    unique key (name)
);
"""

class RoleUser():
    __tablename__ = "roles_users"
    roles_id = Column(Integer, ForeingKey("roles.id"), primary_key=True, nullable=False)
    users_id = Column(Integer, ForeingKey("users.id"), primary_key=True, nullable=False)



class Todo(Base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True)
    task = Column(String(100), unique=True, nullable=False)
    users_id = Column(Integer, ForeingKey("users.id"), nullable=False)
    # user = relationship("User", backref="todos")


class Profile(Base):
    __tablename__ = "profiles"
    id = Column(Integer, primary_key=True)
    biography = Column(String(100), unique=True, nullable=False)
    users_id = Column(Integer, ForeingKey("users.id"), nullable=False)





""" from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer)
    email = db.Column(db.String(120))
    password = db.Column(db.String(120))
    active = db.Column(db.Boolean())

"""