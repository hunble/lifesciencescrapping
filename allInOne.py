import requests 
import Result

from bs4 import BeautifulSoup


def searchDataGov(query): 

	payload = {'q': query}

	r = requests.get('https://catalog.data.gov/dataset', params=payload)
	
	soup = BeautifulSoup(r.text, features="html.parser")

	result = soup.find("div",{"class":"new-results"}).getText()
	
	
	
	return Result.toJSONALLINONE("Data Gov", result, r.url, Result.DATA_GOV, "http://gsa.github.io/datagov-presentations/CKANcon/images/logo-with-flag.svg")


def searchNCBI(query): 

	payload = {'term': query}

	r = requests.get('https://www.ncbi.nlm.nih.gov/gds', params=payload)
	
	soup = BeautifulSoup(r.text, features="html.parser")

	result = soup.find("h3",{"class":"result_count left"}).getText().rstrip()
	
	result.rStrip()
	
	return Result.toJSONALLINONE("NCBI",result,r.url,Result.NCBI,"http://www.lib.berkeley.edu/BIOS/images/NCBI-Logo_sm.jpg")

def searchGoogle(query): 

	payload = {'query': query}

	r = requests.get('https://toolbox.google.com/datasetsearch/search', params=payload)
	
	soup = BeautifulSoup(r.text, features="html.parser")

	result = soup.find("div",{"class":"UvPsAb"}).getText()
	
	return Result.toJSONALLINONE("Google data Sets",result,r.url,Result.GOOGLE,"https://www.gstatic.com/images/branding/googlelogo/svg/googlelogo_clr_74x24px.svg")


def searchHealthDataGov(query): 

	payload = {'query': query}

	r = requests.get('https://healthdata.gov/search/type/dataset', params=payload)
	
	soup = BeautifulSoup(r.text, features="html.parser")

	result = soup.find("div",{"class":"view-header"}).getText()
	
	return Result.toJSONALLINONE("Health Data Gov",result,r.url,Result.HEALTHDATA_GOV,"https://i2.wp.com/www.healthdata.gov/sites/default/files/logo.png?w=980&ssl=1")


def searchDataGovIn(query): 

	payload = {'query': query}

	r = requests.get('https://data.gov.in/search/site', params=payload)
	
	soup = BeautifulSoup(r.text, features="html.parser")

	result = soup.find("div",{"class":"view-header"})
	
	return Result.toJSONALLINONE("Data Gov India","Unknown",r.url,Result.DATA_GOV_IN,"https://data.gov.in/sites/all/themes/ogplv3light/logo.png")


def searchKaggle(query): 

	payload = {"sortBy":"relevance",
				"group":"public",
				"search":query,
				"size":"all",
				"filetype":"all",
				"license":"all"}


	r = requests.get('https://www.kaggle.com/datasets', params=payload)

	print(r.url)
	
	soup = BeautifulSoup(r.text, features="html.parser")

	
	result = soup.find("div",{"class":"content-box"})
	
	
	return Result.toJSONALLINONE("Kaggle","Unknown",r.url,Result.KAGGLE,"https://www.kaggle.com/static/images/site-logo.png")


def allInOne(query):
	Result = []
	
	try:
		print("\n")
		Result.append(searchDataGov(query))
	except:
		print("Exception Occured")
		
		
	try:
		print("\n")
		Result.append(searchNCBI(query))
	except:
		print("Exception Occured")


	try:
		print("\n")
		Result.append(searchGoogle(query))
	except:
		print("Exception Occured")
		

	try:
		print("\n")
		Result.append(searchHealthDataGov(query))
	except:
		print("Exception Occured")

		
	try:
		print("\n")
		Result.append(searchKaggle(query))
	except:
		print("Exception Occured")
		
		
	try:
		print("\n")
		Result.append(searchDataGovIn(query))
	except:
		print("Exception Occured")


	return Result
	
	
	
print(allInOne("cancer"))