from database import cursor, db

# Add Article


def add_article(title, content):
    sql = (f"INSERT INTO content(name,password) VALUES({title},{content})")
    cursor.execute(sql)
    db.commit()
    log_id = cursor.lastrowid
    print("User have been created you can now log in".format(log_id))

# Show List of Articles


def get_articles():
    sql = ("SELECT * FROM content ORDER BY created DESC")
    cursor.execute(sql)
    result = cursor.fetchall()

    for row in result:
        print(row)

# Get single specyfic article


def get_article(id):
    sql = (f"SELECT * FROM content WHERE id = {id}")
    cursor.execute(sql)
    result = cursor.fetchone()

    for row in result:
        print(row)

# Update Article


def update_article(id, title, content):
    sql = ("UPDATE content SET title=%s, content=%s WHERE id = %s")
    cursor.execute(sql, (title, content, id,))
    db.commit()
    print("Article updated")

# Delete User


def delete_article(id):
    sql = ("DELETE FROM content WHERE id = %s")
    cursor.execute(sql(id,))
    db.commit()
    print("Article Deleted")
