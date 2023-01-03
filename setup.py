import env
import mysql.connector
from mysql.connector import errorcode
from database import cursor

DB_NAME = 'Logging_System_DB'

TABLES = {}

# TABLE WITH USERES
TABLES['users'] = (
    "CREATE TABLE `users`("
    "`id` int(11) NOT NULL AUTO_INCREMENT,"
    "`user` varchar(15) NOT NULL,"
    "`password` varchar(15) NOT NULL,"
    "`isLogged` BOOLEAN NOT NULL DEFAULT FALSE,"
    "`created` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,"
    "PRIMARY KEY(`id`)"
    ") ENGINE=InnoDB"
)
# TABLE WITH CONTENT
TABLES['content'] = (
    "CREATE TABLE `content`("
    "`id` int(11) NOT NULL AUTO_INCREMENT,"
    "`title` varchar(25) NOT NULL,"
    "`content` varchar(250) NOT NULL,"
    "`created` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,"
    "PRIMARY KEY(`id`)"
    ") ENGINE=InnoDB"
)

def create_database():
    cursor.execute("CREATE DATABASE IF NOT EXISTS {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    print("Database {} created!".format(DB_NAME))

def create_tables():
    cursor.execute("USE {}".format(DB_NAME))
    for table_name in TABLES:
        table_description = TABLES[table_name]
        try:
            print('Creating table ({})'.format(table_name), end="")
            cursor.execute(table_description)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("Already exist")
            else:
                print(err.msg)

create_database()
create_tables()