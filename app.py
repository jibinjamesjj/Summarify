# Backend for the summary creating app

#load core pkg
from flask import Flask, redirect, render_template, request, url_for
import nltk     # pip install nltk
import heapq    ## built-in library


#To be run only once
#ltk.download('punkt')
#nltk.download('stopwords')
#nltk.download('punkt_tab')

#init app
app = Flask(__name__)


#route
@app.route('/')
def index():
	return 'Hello app'
#return render_template('index.html', messages=messages)

# Adding HTML
@app.route('/home')
def home():
	return render_template('home.html')

@app.route('/createsummary',methods=['GET','POST'])
def createsummary():
	if request.method == 'POST':
		text = request.form['texttobesummarized']

		## Initializing Stop words (so, but , in, on, and etc.)
		stopwords = nltk.corpus.stopwords.words('english')

		## spliting article into sentences
		sentence_list = nltk.sent_tokenize(text)

		## Making a dictonary of frequency scores to words {word : frequency}
		frequency_map = {}
		word_list = nltk.word_tokenize(text)  ## Spliting article into words

		for i in word_list:
			if i not in stopwords:
				if i not in frequency_map:
					frequency_map[i] = 1
				else:
					frequency_map[i] += 1

		max_frequency = max(frequency_map.values()) ## Checking for the maximum frequency

		for word in frequency_map:
			frequency_map[word] = frequency_map[word] / max_frequency ## reassigning the scores in proportion to max frequency

		sent_scores = {}

		## Setting sentence scores based on word scores
		for sent in sentence_list:
			for word in word_list:
				if word in frequency_map and len(sent.split(' ')) < 35:
					if sent not in sent_scores:
						sent_scores[sent] = frequency_map[word]
					else:
						sent_scores[sent] += frequency_map[word]

		## Finding top 10 sentences based on scores
		summary = heapq.nlargest( 10,sent_scores, key=sent_scores.get)

		#for a in summary: ## Final output           
		#		print(a) 

		#summarizedtext = summarizedtextdata.text

		#soup = BeautifulSoup(r.content)
		#findtextbox = soup.find('textarea',id='Text')
	return render_template('home.html', summary=summary)

if __name__ == '__main__':
	app.run(debug=True)

#print("App run successful!")