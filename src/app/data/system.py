import csv
import os

class StudentAlreadyExists(Exception):
	def __init__(self, message = "Student already exists."):
		self.message = message
		super().__init__(message)

class CourseAlreadyExists(Exception):
	def __init__(self, message = "Course already exists."):
		self.message = message

class Courses:
	def __init__(self):
		self.filename = "./courses.csv"
		self.header = ["id", "name", "description", "teacher"]
		self.initialize()

	def initialize(self):
		if not os.path.exists(self.filename):
			with open(self.filename, "w") as file:
				writer = csv.DictWriter(file, fieldnames = self.header)
				writer.writeheader
	def read_all(self):
		with open(self.filename, newline='') as file:
			reader = csv.DictReader(file)
			return [row for row in reader]

	def get(self, _id: str):
		data = self.read_all()
		for row in data:
			if row["id"] == _id:
				return row 
		return None

	def write_one(self, course: dict):
		if not self.check_course(course):
			return False
		with open(self.filename, 'a') as file:
			writer = csv.DictWriter(file, fieldnames = self.header)
			writer.writerow(course)

	# deletes a single course data from the csv file.
	def delete_one(self, _id: str):
		if not self.check_student({"id": _id}):
			return False 

		courses = self.read_all()

		with open(self.filename, "w") as file:
			writer = csv.DictWriter(file, fieldnames=self.header)
			writer.writeheader()
			for course in courses:
				if course["id"] == _id:
					continue
				course.writerow(student)

	def check_course(self, course: dict):
		courses = self.read_all()
		for std in courses:
			if std["id"] == course["id"]:
				return False
		return True




# main class of student, includes the reading and writing function for the csv
class Students:
	def __init__(self):
		self.filename = "./students.csv"
		self.header = ["id", "name", "gender", "course"]
		self.initialize()

	def initialize(self):
		if not os.path.exists(self.filename):

			with open(self.filename, "w") as file:
				writer = csv.DictWriter(file, fieldnames = self.header)
				writer.writeheader()

	def read_all(self):
		with open(self.filename, newline='') as file:
			reader = csv.DictReader(file)
			return [row for row in reader]

	def get(self, _id: str):
		data = self.read_all()
		for row in data:
			if row["id"] == _id:
				return row 
		return None

	def write_one(self, student: dict):
		if self.check_student(student):
			return False
		with open(self.filename, 'a') as file:
			writer = csv.DictWriter(file, fieldnames = self.header)
			writer.writerow(student)

	# deletes a single student data from the csv file.
	def delete_one(self, _id: str):
		if not self.check_student({"id": _id}):
			return False 

		students = self.read_all()
		with open(self.filename, "w") as file:
			writer = csv.DictWriter(file, fieldnames=self.header)
			writer.writeheader()
			for student in students:
				if student["id"] == _id:
					continue
				writer.writerow(student)

	def check_student(self, student: dict):
		students = self.read_all()
		for std in students:
			if std["id"] == student["id"]:
				return True
		return False
