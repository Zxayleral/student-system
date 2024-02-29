import csv
import os 


class Parser:
	def __init__(self, filename, header):
		self.filename = filename
		self.header = header
		self.initialize()

	# Initializes the file
	def initialize(self):
		# check if the file exists
		if os.path.exists(self.filename):
			# read all the contents
			existing_data = []
			with open(self.filename, 'r') as file:
				reader = csv.DictReader(file)
				existing_data = [row for row in reader]
			# if there are no existing datas, it will initiate and create a provided header
			if not existing_data:
				with open(self.filename, 'w', newline='') as file:
					writer = csv.DictWriter(file, fieldnames = self.header)
					writer.writeheader()
			return True

		if not os.path.exists(self.filename):
			# creates a file and adds a header if the file does not exist.
			with open(self.filename, "w", newline='') as file:
				writer = csv.DictWriter(file, fieldnames=self.header)
				writer.writeheader()

	# edits the data of a given index, and the document to be pushed
	def edit_data(self, index, document):
		self.initialize() # intialize the file

		collections = self.read_all() # gets all the collection data
		with open(self.filename, "w") as file: # resets the file and writes all the contents
			writer = csv.DictWriter(file, fieldnames=self.header)
			writer.writeheader()
			for idx, collection in enumerate(collections):
				if idx == index: # if the index is the same as the given index, the current document will be rewritten
					writer.writerow(document)
				else: # else, it will write the row as given by the former data.
					writer.writerow(collection)


	#[derive(dead_code)] This is a dead code. But it may be probably used for future purposes
	def count(self): # it just counts all the documents and returns the number
		self.initalize()
		with open(self.filename, "r") as file:
			reader = csv.DictReader(file)
			return len(list(x for x in reader))

	# adds another data
	def insert_one(self, document: dict) -> None:
		self.initialize()
		with open(self.filename, "a", newline='') as file:
			writer = csv.DictWriter(file, fieldnames=self.header)
			writer.writerow(document)

	# checks if the document is already in the collection, based on the ID
	def check(self, document) -> bool:
		self.initialize()
		collections = self.read_all()
		for collection in collections:
			if collection["id"] == document["id"]:
				return True
		return False

	# most used function in this class.
	# it reads all the data in the csv file and parses it into an array of dictionaries
	def read_all(self) -> list:
		self.initialize()
		with open(self.filename, "r") as file:
			reader = csv.DictReader(file)
			return list(x for x in reader)

	# deletes a data from the csv file with the given document
	def delete_one(self, document) -> None:
		self.initialize()
		if not self.check(document): #checks if the document exists
			return False
		collections = self.read_all() # reads all the data
		with open(self.filename, "w") as file:
			writer = csv.DictWriter(file, fieldnames=self.header)
			writer.writeheader()
			for collection in collections:
				if collection["id"] == document["id"]: # if the id is the same as with the document, it will continue the loop
					continue
				else:
					writer.writerow(collection)

	# fetches a data given by a provided index
	def fetch_one(self, index):
		self.initialize()
		collections = self.read_all()
		return collections[index]

# Parser for student csv file.
student = Parser(
	filename="./src/app/config/data/csv/students.csv", 
	header=["id", "name", "gender", "course"]
)

# Parser for course csv file.
course = Parser(
	filename="./src/app/config/data/csv/courses.csv",
	header=["id", "name"]
)