from xmljson import yahoo as bf
from xml.etree import ElementTree
import requests
import json
import requests_cache
import Result


requests_cache.install_cache('demo_cache')

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
				print d
				result.append(getSummary(d))
		else:
			for d in data['eSearchResult']['IdList']['Id'][0:5]:
				print d
				result.append(getSummary(d))

	except:
		print("No result found at ncbi")
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

