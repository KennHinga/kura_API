import datetime
import psycopg2
from .db import DbConnection as db_conn
from passlib.hash import pbkdf2_sha256

TIME_NOW = datetime.datetime.utcnow()

class UserModel(db_conn):
    """class for User"""

    def __init__(self, user={}):
        self.db=db_conn()
        self.user= user

    def create_new_user(self, firstName, lastName, otherName, email, phoneNumber, passportUrl, isAdmin, isCandidate, password):
        """ Adds a new user to the users table"""
        user={
            "firstName": firstName,
            "lastName": lastName,
            "otherName": otherName,
            "email": email,
            "phoneNumber": phoneNumber,
            "passportUrl": passportUrl,
            "isAdmin": isAdmin,
            "isCandidate": isCandidate,
            # "password": user.generate_hash(password)
        }

        query = """ INSERT INTO users( firstName, lastName, otherName, email, phoneNumber, passportUrl, isAdmin, isCandidate, password)
                VALUES(%(firstName)s, %(lastName)s, %(otherName)s, %(email)s, %(phoneNumber)s, %(passprtUrl)s, %(isAdmin)s, %(isCandidate)s, %(password)s)"""    
        # cursor= self.db.cursor()
        # cursor.execute(query, user)
        # self.db.commit()
        return user

    @staticmethod
    def generate_hash(password):
        return sha256.hash(password)
    
    @staticmethod
    def hash_verify(password, hash):
        return sha256.verify(password, hash)
