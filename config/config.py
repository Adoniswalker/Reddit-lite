import os
import psycopg2

base_dir = os.path.abspath(os.path.dirname(__file__))

try:
    conn = psycopg2.connect("dbname=reddit host=localhost user=abadojack password=''")
except Exception as e:
    print("connect to database failed ", e)


def create_tables():
    cur = conn.cursor()
    try:
        # delete tables if they exist
        cur.execute("DROP TABLE IF EXISTS users;")
        cur.execute("DROP TABLE IF EXISTS comments;")
        cur.execute("DROP TABLE IF EXISTS tokens;")

        # create table users
        users = "CREATE TABLE users(id VARCHAR(256) PRIMARY KEY, username VARCHAR(64) UNIQUE , password_hash VARCHAR(256) UNIQUE," \
                "role VARCHAR(256),time_created TIMESTAMP );"

        comments = "CREATE TABLE comments(id VARCHAR(256) PRIMARY KEY, uid VARCHAR(256) )"

        cur.execute(users)

        conn.commit()
    except Exception as ex:
        print('error in migration', ex)


def delete_tables():
    cur = conn.cursor()
    cur.execute("DELETE from users;")
    conn.commit()


# Base configuration
class Config(object):
    DEBUG = True
    CSRF_ENABLED = True
    SECRET = os.getenv('STACKOVERFLOW_SECRET', 'KeepYourSecretsToYourself')
