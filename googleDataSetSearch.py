import requests 
import Result

from bs4 import BeautifulSoup


def search(query): 

	payload = {'query': query}

	r = requests.get('https://toolbox.google.com/datasetsearch/search', params=payload)


	print("loaded...")

	soup = BeautifulSoup(r.text, features="html.parser")

	list = soup.find_all("li", {"class": "UnWQ5"})
	
	print(len(list)," results found")

	results = []

	for x in list:
	

		try: 
			docid = x.find('div')['data-docid']
			r = [docid , Result.GOOGLE]
			results.append(r)
		except:
			print("some forign cell encountered")
			
	return results



def getSummary(identifier): 

	payload = {'docid': identifier}

	r = requests.get('https://toolbox.google.com/datasetsearch/search', params=payload)
	soup = BeautifulSoup(r.text, features="html.parser")
	
	print("\n"+r.url+"\n")

	y = soup.find("div", {"class": "hTmcCe"})
	title = y.find("h1", {"class": "SAyv5"}).get_text()
	
	
	
	summary = y.find("div", {"class": "iH9v7b"}).get_text()

	dataLink = y.find("a", {"class": "gVd0We"})['href']
	
	siteLink = r.url

	source = y.find("a", {"class": "gVd0We"}).find("div",{'class':'eLDzIf'}).get_text()
	sourceImage = "https://cdn.onlinewebfonts.com/svg/img_503553.png"
	
	try:
		sourceImage = soup.find("img", {"class": "EApCid"})['src']		
	except:
		print("Image not found")
	
	return Result.toJSON(title,summary,dataLink,siteLink,source,sourceImage)






def googleDataSets(query, noOfResults=5):

	

	payload = {'query': query}

	r = requests.get('https://toolbox.google.com/datasetsearch/search', params=payload)


	print("loaded...")

	soup = BeautifulSoup(r.text, features="html.parser")

	list = soup.find_all("li", {"class": "UnWQ5"})
	
	print(len(list)," results found")
	
	result = []

			
	
	for x in list[:noOfResults]:
	
		docid = x.find('div')['data-docid']
		
		payload = {'docid': docid}
		
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
		sourceImage = "https://cdn.onlinewebfonts.com/svg/img_503553.png"
		
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
			
		print result
	return result


# data = search("caner")

# for x,r in data:
# 	print("\nFor UUID: ", x)
# 	getSummary(x)

	
#googleDataSets("cancer")