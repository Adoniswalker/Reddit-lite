import psycopg2

import jwt
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime, timedelta
import uuid
from config.config import conn, Config

try:
    cur = conn.cursor()
    cur.execute("ROLLBACK")
    conn.commit()
except Exception as ex:
    print('connection exception ', ex)
    cur = conn.cursor()
    cur.execute("ROLLBACK")


def auth_encode(uid):
    """Generate auth token"""
    try:
        payload = {
            'exp': datetime.now() + timedelta(hours=1),
            'iat': datetime.now(),
            'sub': uid
        }
        return jwt.encode(
            payload,
            Config.SECRET
        )
    except Exception as ex:
        raise ex


def auth_decode(token):
    """Decode auth token"""
    try:
        payload = jwt.decode(token, Config.SECRET)
        return payload['sub']
    except Exception as e:
        print('auth_token error', e)
        return None


def signin(username, password):
    """
    login an existing user
    """
    user = User(username, "", "")

    try:
        user = user.exists()
        if check_password_hash(user.password_hash, password):
            """token if password is correct"""
            token = auth_encode(user.uid)
            if token:
                file = open('token.txt', 'w')
                file.write(token.__str__())
                file.close()
                return "success"
            else:
                return "invalid"
    except (psycopg2.DatabaseError, psycopg2.IntegrityError, Exception) as e:
        return "failed"


class User(object):
    def __init__(self, username, password_hash, role):
        self.uid = ''
        self.username = username
        self.role = role
        self.password_hash = password_hash
        self.time_created = datetime.now()

    def create_user(self, password):
        """Create user in db DONE"""
        try:
            password_hash = generate_password_hash(password)
            uid = uuid.uuid4()
            query = "INSERT INTO " \
                    "users (id, username,password_hash,role, time_created)" \
                    "VALUES('%s','%s', '%s', '%s', '%s')" % (
                        uid, self.username, password_hash, self.role, self.time_created)
            cur.execute(query)
            conn.commit()
            return "success"
        except psycopg2.IntegrityError as ex:
            return "failed"

    def get_user(self, uid):
        """get user using uid"""
        cur.execute("SELECT * FROM users WHERE id = %s;" % uid)
        user = cur.fetchone()
        user_dict = {'id': user[0], 'username': user[1], 'password_hash': user[2],  'role': user[3],
                     'time_created': user[4]}
        return user_dict

    def exists(self):
        """check if user exists using"""
        cur.execute("SELECT * FROM users WHERE username = '%s';" % self.username)
        user = cur.fetchone()
        if user is None:
            return None
        else:
            self.uid = user[0]
            self.password_hash = user[2]
            self.role = user
            self.time_created = user[4]
            return self
