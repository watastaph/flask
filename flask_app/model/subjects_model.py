from flask_app.config.mysqlconnection import connectToMySQL

class Subjects:
    def __init__(self, data):
        self.id = data['id']
        self.course_code = data['course_code']
        self.description = data['description']
        self.semester_offered = data['semester_offered']
        self.student_id = data['student_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def add_subject(cls, data):
        query = "INSERT INTO subjects (course_code, description, semester_offered, student_id, created_at, updated_at) VALUES (%(course_code)s, %(description)s, %(semester_offered)s, %(student_id)s, NOW(), NOW());"
        return connectToMySQL('enrollment').query_db(query, data)

    @classmethod
    def get_subject(cls, data):
        query =  "SELECT * FROM subjects WHERE student_id = %(student_id)s"
        results = connectToMySQL('enrollment').query_db(query, data)
        subjects = []
        for subject in results:
            subjects.append(cls(subject))
        return subjects