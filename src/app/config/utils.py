import csv
import os 


class Parser:
	def __init__(self):
		self.filename: str
		self.header: list

	def initialize(self):
		if not os.path.exists(self.filename):
			with open(self.filename, "w") as file:
				writer = csv.DictWriter(file, fieldnames=self.header)

	def count(self):
		with open(self.filename, "r") as file:
			reader = csv.DictReader(file)
			return len(list(x for x in reader))

	def check(self, document):
		collections = self.read_all()
		for collection in collections:
			if collection["id"] == document["id"]:
				return True
		return False

	def read_all(self):
		with open(self.filename, "r") as file:
			reader = csv.DictReader(file)
			return list(x for x in reader)

	def delete_one(self, document):
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
		
