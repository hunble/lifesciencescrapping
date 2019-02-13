from xmljson import yahoo as bf
from xml.etree import ElementTree
import requests
import json

import Result



def ncbiGBSeSearch(key):
	url = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi/'

	params = dict(db='gds',term=key)

	resp = requests.get(url=url, params=params)

	tree = ElementTree.fromstring(resp.content)

	data = bf.data(tree)

	result = []

	try:
		if len(data['eSearchResult']['IdList']['Id']) <= 5:
			for d in data['eSearchResult']['IdList']['Id']:
				result.append(getSummary(d))
		else:
			for d in data['eSearchResult']['IdList']['Id'][0:5]:
				result.append(getSummary(d))

	except:
		print("No result found at ncbi")

	print(len(result)," results found")


	return result


def getSummary(key):

    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi/"

    params = dict(db='gds',id=key)

    resp = requests.get(url=url, params=params)
    
    tree = ElementTree.fromstring(resp.content)
    
    data = bf.data(tree)

    return Result.toJSON(data['eSummaryResult']['DocSum']['Item'][2].get('content'),
                  data['eSummaryResult']['DocSum']['Item'][3].get('content'),
                  data['eSummaryResult']['DocSum']['Item'][25].get('content'),
                  "https://www.ncbi.nlm.nih.gov/sites/GDSbrowser?acc=GDS"+key,
				  "NCBI",
				  "https://bouldermindcare.com/wp-content/uploads/2017/01/ncbi-logo1.png")



def search(key):

	url = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi/'

	params = dict(db='gds',term=key)

	resp = requests.get(url=url, params=params)

	tree = ElementTree.fromstring(resp.content)

	data = bf.data(tree)

	result = []

	try:
		for d in data['eSearchResult']['IdList']['Id']:
			print d
			r = [d , Result.NCBI]
			result.append(r)

	except:
		print("No result found at ncbi")
		return []

	return result


# data = search("cancer", 10)

# for x,r in data:
# 	print("\nFor UUID: ", x)
# 	getSummary(x)


