import csv
import os 


class Parser:
	def __init__(self, filename, header):
		self.filename = filename
		self.header = header
		self.initialize()

	def initialize(self):
		if os.path.exists(self.filename):
			existing_data = []
			with open(self.filename, 'r') as file:
				reader = csv.DictReader(file)
				existing_data = [row for row in reader]
			if not existing_data:
				with open(self.filename, 'w', newline='') as file:
					writer = csv.DictWriter(file, fieldnames = self.header)
					writer.writeheader()
			return True

		if not os.path.exists(self.filename):
			with open(self.filename, "w", newline='') as file:
				writer = csv.DictWriter(file, fieldnames=self.header)
				writer.writeheader()

	def edit_data(self, index, document):
		self.initialize()
		collections = self.read_all()
		with open(self.filename, "w") as file:
			writer = csv.DictWriter(file, fieldnames=self.header)
			writer.writeheader()
			for idx, collection in enumerate(collections):
				if idx == index:
					writer.writerow(document)
				else:
					writer.writerow(collection)


	def count(self):
		self.initalize()
		with open(self.filename, "r") as file:
			reader = csv.DictReader(file)
			return len(list(x for x in reader))

	def insert_one(self, document: dict):
		self.initialize()
		with open(self.filename, "a", newline='') as file:
			writer = csv.DictWriter(file, fieldnames=self.header)
			writer.writerow(document)

	def check(self, document):
		self.initialize()
		collections = self.read_all()
		for collection in collections:
			if collection["id"] == document["id"]:
				return True
		return False

	def read_all(self):
		self.initialize()
		with open(self.filename, "r") as file:
			reader = csv.DictReader(file)
			return list(x for x in reader)

	def delete_one(self, document):
		self.initialize()
		if not self.check(document):
			return False
		collections = self.read_all()
		with open(self.filename, "w") as file:
			writer = csv.DictWriter(file, fieldnames=self.header)
			for collection in collections:
				if collection["id"] == document["id"]:
					continue
				else:
					writer.writerow(student)

	def fetch_one(self, index):
		self.initialize()
		collections = self.read_all()
		return collections[index]

student = Parser(
	filename="./src/app/config/data/csv/students.csv", 
	header=["id", "name", "gender", "course"]
)

course = Parser(
	filename="./src/app/config/data/csv/courses.csv",
	header=["id", "name"]
)