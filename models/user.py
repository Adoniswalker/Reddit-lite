"""
#app/models/user.py
This is the user model
"""
import psycopg2
from database.connect import conn, cursor as cur
from werkzeug.security import generate_password_hash, \
    check_password_hash


class UserModel:
    """this handles user registration and authentication"""

    def get_all_users():
        """retrieve all users from the database"""
        user_list = []
        conn
        que = cur.execute("SELECT * FROM auth_users")

        try:
            que
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            conn
            cur

        result = cur.fetchall()

        for i in result:
            user_list.append(result)

        return result

    def register(username, email, password):
        """save new user data"""

        data = dict(username=username, email=email, password=generate_password_hash(password))

        submit = cur.execute("""INSERT INTO users (username, email, password) VALUES 
                    (%(username)s, %(email)s, %(password)s)""", data)

        conn.commit()

    def check_if_exists(username):
        """checks if user exists in system"""
        fetch_question = "SELECT * FROM auth_users WHERE username = %s;"
        fetched_question = cur.execute(fetch_question, [username])
        result = cur.fetchall()

        return result

    def find_by_username(username, password):
        """check user dedtails on login"""
        user_list = []

        conn
        que = cur.execute("SELECT * FROM auth_users")

        try:
            que
        except (Exception, psycopg2.DatabaseError) as error:
            conn
            cur
            que

        result = cur.fetchall()

        for i in result:

            if i[3] == username and check_password_hash(i[5], password):
                u_id = i[0]
                return u_id
