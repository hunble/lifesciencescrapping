import requests_cache

GOOGLE = "GOOGLE"
NCBI = "NCBI"
DATA_GOV = "DATA_GOV"

requests_cache.install_cache('demo_cache')

def toJSON(title,summary,dataLink,siteLink,source = "Unknown", sourceImage = "https://cdn.onlinewebfonts.com/svg/img_503553.png" ):
	data = {}
	data['title'] = title
	data['summary'] = summary
	data['dataLink'] = dataLink
	data['siteLink'] = siteLink
	data['source'] = source
	data['sourceImage'] = sourceImage
	#print(data)
	return data






