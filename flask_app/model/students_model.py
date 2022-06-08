from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class Students:
    def __init__(self, data):
        self.id = data['id']
        self.fullname = data['fullname']
        self.course = data['course']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @staticmethod
    def validate_registration(student):
        is_valid = True
        if len(student['fullname']) > 20:
            flash("the fullname is more than 20 characters long!")
            is_valid = False
        if not EMAIL_REGEX.match(student['email']):
            flash("Invalid E-Mail Address!")
            is_valid = False
        if student['password'] != student['cpassword']:
            flash("Password not match!")
            is_valid = False
        return is_valid

    @staticmethod
    def validate_login(student):
        is_valid = True
        if not EMAIL_REGEX.match(student['email']):
            flash("Invalid E-Mail Address!")
            is_valid = False
        return is_valid
    
    @classmethod
    def register_student(cls, data):
        query = "INSERT INTO students (fullname, course, email, password, created_at, updated_at) VALUES (%(fullname)s, %(course)s, %(email)s, %(password)s, NOW(), NOW());"
        return connectToMySQL('enrollment').query_db(query, data)

    @classmethod
    def verify_student(cls, data):
        query = "SELECT * FROM students WHERE email = %(email)s"
        results = connectToMySQL('enrollment').query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    