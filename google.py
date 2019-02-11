import requests 
import requests_cache
import Result

from bs4 import BeautifulSoup

requests_cache.install_cache('GOOGLEDataSets')

def googleDataSets(query, noOfResults=5):

	

	payload = {'query': 'boston education data'}

	r = requests.get('https://toolbox.google.com/datasetsearch/search', params=payload)


	print("loaded...")

	soup = BeautifulSoup(r.text, features="html.parser")

	list = soup.find_all("li", {"class": "UnWQ5"})
	
	print(len(list)," results found")
	
	result = []

			
	
	for x in list[:noOfResults]:
	
		docid = x.find('div')['data-docid']
		
		payload = {'query': 'boston education data', 'docid': docid}
		
		#print(payload)
		
		r = requests.get('https://toolbox.google.com/datasetsearch/search', params=payload)
		soup = BeautifulSoup(r.text, features="html.parser")
		
		print("\n"+r.url+"\n")

		y = soup.find("div", {"class": "hTmcCe"})
		title = y.find("h1", {"class": "SAyv5"}).get_text()
		
		
		
		summary = y.find("div", {"class": "iH9v7b"}).get_text()

		dataLink = y.find("a", {"class": "gVd0We"})['href']
		
		siteLink = r.url

		source = y.find("a", {"class": "gVd0We"}).find("div",{'class':'eLDzIf'}).get_text()
		sourceImage = "https://media.wired.com/photos/5a0201b14834c514857a7ed7/master/w_582,c_limit/1217-WI-APHIST-01.jpg"
		
		try:
			sourceImage = soup.find("img", {"class": "EApCid"})['src']		
		except:
			print("Image not found")
		
		
#		print(source)
		
#		print(docid+"\n")
#		print(y.find("h1", {"class": "SAyv5"}).get_text())
#		print(y.find("div", {"class": "iH9v7b"}).get_text())
#		print("\n"+y.find("a", {"class": "gVd0We"})['href'])
		
		result.append(Result.toJSON(title,summary,dataLink,siteLink,source,sourceImage))
			
	return result
	
googleDataSets("cancer")