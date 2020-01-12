from serpapi.google_search_results import GoogleSearchResults
import requests
import pickle
import json
import keyword

class Keyword():
	def __init__(self, word, definitions, questions, links):
		self.word = word
		self.definitions = definitions
		self.questions = questions
		self.links = links

def pickleData(data):
	pickle_out = open("data.pickle", "wb")
	pickle.dump(data, pickle_out)
	pickle_out.close()

def getPickleData():
	pickleFile = open("data.pickle", "rb")
	data = pickle.load(pickleFile)
	pickleFile.close()

	return data

def createJSONs(keywords):
	definitions = []

	for word in keywords:
		headers = {
			'apikey': '530c1f60-f844-11e9-a7fe-112a850a28b1',
		}

		params = (
			('q', word),
			('location', 'United States'),
			('search_engine', 'google.com'),
			('gl', 'US'),
			('hl', 'en')
		)

		response = requests.get('https://app.zenserp.com/api/v2/search', headers=headers, params=params)

		definitions.append(response.json())

	# pickleData(definitions)
	return definitions

def deserialize(search_results):
	definitions, questions, links = [], [], []
	keywords = []


	for result in search_results:
		query = result["query"]["q"]
		json_data = result["organic"][:7:]

		definition = [x["description"] for x in json_data if "description" in x]
		try:
			questions = [x["question"] for x in [x["questions"] for x in json_data if "questions" in x][0]]
		except:
			continue
		links = [x["url"] for x in json_data if "url" in x]

		keywords.append(Keyword(query, definition, questions, links))

	return keywords

def extract(file_name):
	#file_name = "keywords.txt"
	with open(file_name) as keyword_file:
		keywords = [x.rstrip() for x in keyword_file.readlines()]

	search_results = createJSONs(keywords)
	# search_results = getPickleData()

	keywords = deserialize(search_results)

	#pickleData(keywords)
	#keywords = getPickleData()

	return keywords