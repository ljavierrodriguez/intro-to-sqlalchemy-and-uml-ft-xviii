from models import User, Role, Todo, Profile

""" 
DML (Data Manipulation Language)

INSERT

UPDATE

DELETE

SELECT

"""


""" 
INSERT:

INSERT INTO users (email, password, active) VALUES ('john.doe@gmail.com', '123456', true);

"""

user = User()
user.email = "john.doe@gmail.com"
user.password = "123456"
user.active = True

db.session.add(user)
db.session.commit()


"""
UPDATE:

UPDATE users SET password='12345678' WHERE id=1;

"""

user = User.query.get(1) # SELECT * FROM users WHERE id=1;
user.password = '12345678' 
user.active = False
# UPDATE users SET password='12345678', active=false WHERE id=1;
db.session.commit()


"""
DELETE:

DELETE FROM users WHERE id=1;
"""

user = User.query.get(1)
db.session.delete(user)
db.session.commit()


""" 
SELECT:

SELECT * FROM users;
SELECT * FROM users WHERE id=1;
SELECT * FROM users WHERE active=true;

"""

""" 
SELECT * FROM users;
"""
users = User.query.all() # [<User 1>, <User 2>, <User 3>]

""" 
SELECT * FROM users WHERE id=1;
"""
user = User.query.get(1) # <User 1>

""" 
SELECT * FROM users WHERE active=true;
"""
users = User.query.filter_by(active=True) # [<User 2>, <User 9>, <User 13>]

user.roles[0].name # Admin
 
user.profile.biography
user.todos # [<Todo 1>, <Todo 3>, <Todo 9>]

for todo in user.todos:
    print(todo.task) # Primera Tarea
    print(todo.user.email)



user = User.query.get(1)
profile = Profile.query.filter_by(users_id=user.id) # [<Profile 10>]
profile = Profile.query.filter_by(users_id=user.id).first() # <Profile 10>