from database import cursor, db

# Add User

def add_user(name,password):
    sql = (f"INSERT INTO users(name,password) VALUES({name},{password})")
    cursor.execute(sql)
    db.commit()
    log_id = cursor.lastrowid
    print("User have been created you can now log in".format(log_id))

# Show List of Users

def get_users():
    sql = ("SELECT * FROM users ORDER BY created DESC")
    cursor.execute(sql)
    result = cursor.fetchall()

    for row in result:
        print(row)

# Get single specyfic user
def get_user(id):
    sql = (f"SELECT * FROM logs WHERE id = {id}")
    cursor.execute(sql)
    result = cursor.fetchone()

    for row in result:
        print(row)

# Update User

def update_user(id,name,password):
    sql = ("UPDATE users SET name=%s, password=%s WHERE id = %s")
    cursor.execute(sql,(name,password,id,))
    db.commit()
    print("User upadted")

# Delete User

def delete_user(id):
    sql = ("DELETE FROM users WHERE id = %s")
    cursor.execute(sql(id,))
    db.commit()
    print("User Deleted")

    