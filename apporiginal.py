# Backend for the summary creating app

#load core pkg
from flask import Flask, render_template, request
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
#from webdriver_manager.firefox import GeckoDriverManager
#from webdriver_manager.microsoft import EdgeChromiumDriverManager



#driver = webdriver.Edge(EdgeChromiumDriverManager().install())


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
		websiteurl = request.form['websiteurl']
		#driver = webdriver.Edge(EdgeChromiumDriverManager().install())
		#options = webdriver.EdgeOptions()
		#driver = webdriver.Edge(options=options)
		driver = webdriver.Firefox()
		


		#driver.get("https://en.wikipedia.org/wiki/Bird#:~:text=Birds%20are%20a%20group%20of%20warm-blooded%20vertebrates%20constituting%20the%20class#:~:text=Birds%20are%20a%20group%20of%20warm-blooded%20vertebrates%20constituting%20the%20class")
		#wikimsg = driver.find_element(By.CLASS_NAME, "noprint")
		#if wikimsg:
		#	foundmsg = "Found the element"
			#Found
		

		driver.get("https://www.tldrthis.com/#uploadFileSection")
		driver.find_element(By.XPATH, '//*[@id="uploadFileSection"]/div/div[1]/div/div/div/div[1]/div/div/button[2]').click()
		#driver.find_element(By.CLASS_NAME, "chat__textarea").send_keys(websiteurl)
		foundtextbox = driver.find_element(By.XPATH, '//*[@id="uploadFileSection"]/div/div[1]/div/div/div/div[2]/div/div/input')
		foundtextbox.send_keys(websiteurl)
		driver.find_element(By.XPATH, '//*[@id="uploadFileSection"]/div/div[2]/button').click()

		driver.implicitly_wait(30)
		#delay = 100 # seconds
		#try:
		#	myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/main/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]/div/div[2]/div/div[1]')))
		#	pageresultmsg = "Page is ready!"
		#except TimeoutException:
		#	pageresultmsg = "Loading took too much time!"
		summarizedtextdata = driver.find_element(By.XPATH, '/html/body/main/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]/div/div[2]/div/div[1]/text()')
		summarizedtext = summarizedtextdata.text

		#wikimsgtext = wikimsg.text
		#driver.quit()
		#driver.get("https://talkai.info/chat/")
		#driver.find_element(By.CLASS_NAME, "chat__textarea").send_keys(websiteurl)


		#driver.find_element_by_tag_name("textarea").send_keys("This is the input text which is inputed.")
		#soup = BeautifulSoup(r.content)
		#findtextbox = soup.find('textarea',id='Text')
	return render_template('home.html',websiteurl=websiteurl,summarizedtext=summarizedtext)


if __name__ == '__main__':
	app.run(debug=True)

#print("App run successful!")