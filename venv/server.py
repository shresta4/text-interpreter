from flask import Flask, render_template, request
app = Flask(__name__) 

@app.route('/') 
def home(): 
	return render_template("home.html")

@app.route('/about') 
def about(): 
	return render_template("about.html")

@app.route('/text_interpreter')
def text_interpreter(): 
	return render_template("text_interpreter.html");

@app.route('/file_interpreter') 
def file_interpreter(): 
	return render_template("file_interpreter.html"); 

import text_interpreter_main
import DefinitionExtraction

filename = "userinput.txt"
filename2 = "keywords.txt"

@app.route('/process', methods=['GET','POST'])
def process(): 
	# if request.method == 'POST':
	text_input = request.form.get('input_text')
	
	#write words into a file
	write_input_text_to_file(text_input); 

	#get keywords 
	keywords = text_interpreter_main.interpret_for_plain_text(filename)
	text_interpreter_main.write_keywords_to_file(keywords, filename2)

	#get definitions 
	definitions = DefinitionExtraction.extract(filename2)

	keyword_results = "\n\n\n"; 
	for keyword in definitions: 
		keyword_results += keyword.word + ": \n"; 
		for defn in keyword.definitions: 
			keyword_results += defn + "; "; 
		keyword_results += "\n"
		for q in keyword.questions: 
			keyword_results += q + " "; 
		keyword_results += "\n"
		for link in keyword.links: 
			keyword_results += link + "; "
		keyword_results += "\n\n"
    
	#third send the data as a result
	return render_template('results.html', keyword_results = keyword_results)

import urllib.request
import io 
from PIL import Image 
import ocr_on_text
@app.route('/process2', methods=['GET','POST'])
def process2(): 
	# if request.method == 'POST':
	# text_input = request.form.get('input_text') 
	URL = request.form.get('urltext'); 
	with urllib.request.urlopen(URL) as url: 
		f = io.BytesIO(url.read())
	text = ocr_on_text.get_text(f)

	write_input_text_to_file(text)

	#get keywords 
	keywords = text_interpreter_main.interpret_for_plain_text(filename)
	text_interpreter_main.write_keywords_to_file(keywords, filename2)
	keyword_results = ""; 
	for word in keywords: 
		keyword_results += word + ", "

	keyword_results += "\n\n\n\n" + text; 
    
	#third send the data as a result
	return render_template('results2.html', keyword_results = keyword_results)

def write_input_text_to_file(input_text): 
	f = open(filename, "w")
	input_text = input_text.replace("\n", " ")
	f.write(input_text)
	f.close()
	
if __name__ == '__main__': 
	app.run() 