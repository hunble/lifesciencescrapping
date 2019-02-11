def toJSON(title,summary,dataLink,siteLink,source = "Unknown", sourceImage = "https://media.wired.com/photos/5a0201b14834c514857a7ed7/master/w_582,c_limit/1217-WI-APHIST-01.jpg" ):
	data = {}
	data['title'] = title
	data['summary'] = summary
	data['dataLink'] = dataLink
	data['siteLink'] = siteLink
	data['source'] = source
	data['sourceImage'] = sourceImage
	#print(data)
	return data

