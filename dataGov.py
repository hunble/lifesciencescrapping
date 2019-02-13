import requests 
import Result

from bs4 import BeautifulSoup


def search(query): 

	payload = {'q': query}

	r = requests.get('https://catalog.data.gov/dataset', params=payload)


	print("loaded...")

	soup = BeautifulSoup(r.text, features="html.parser")

	list = soup.find_all("h3", {"class": "dataset-heading"})
	
	print(len(list)," results found")

	results = []

	for x in list:
	
		docid = x.find('a')['href']

		r = [docid , Result.DATA_GOV]

		results.append(r)

	return results



def getSummary(identifier): 

	r = requests.get("https://catalog.data.gov/"+identifier)
	soup = BeautifulSoup(r.text, features="html.parser")
	
	print("\n"+r.url+"\n")

	title = soup.find("h1", {"itemprop": "name"}).get_text()
	summary = soup.find("div", {"itemprop": "description"}).find("p").get_text()


	dataLink = r.url
	try:
		dataLink = "https://catalog.data.gov"+soup.find("a", {"itemprop": "contentUrl"})['href']
	except:
		print("Data set doesnot seem to public")

	siteLink = r.url

	source = "data.gov"
	sourceImage = "https://www.data.gov/app/themes/roots-nextdatagov/assets/img/logo.svg"

	
	return Result.toJSON(title,summary,dataLink,siteLink,source,sourceImage)







# data = search("cancer")

# for x,r in data:
# 	print("\nFor UUID: ", x)
# 	getSummary(x)

	
#googleDataSets("cancer")
