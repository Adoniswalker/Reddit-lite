"""

#app/models/comment.py
This is the comment model
"""
from datetime import datetime
from database.connect import conn, cur
from flask_jwt_extended import (create_access_token, create_refresh_token,
jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt,)
from flask_jwt_extended import JWTManager


class CommentModel():
    """handles operations for the answers"""
    def save_comment(body):
        """save new answer"""
        author_id = get_jwt_identity()

        submit = cur.execute("""INSERT INTO comments(author_id, message) VALUES 
                    (%s, %s)""", [author_id, message])

        conn.commit()

