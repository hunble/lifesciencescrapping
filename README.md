# Life Science Search Engine

This is a deplyable website plus API for searching NCBI Geo Data sets data store and scraping google data sets to find the most relivant results to your life science query.

## Getting Started

The web site includes a Flask based API to extend the project and build client based solutions over the searhing api. Build up on Flast and Flask API to support API interface. 

### Prerequisites

Pythin 2.7, pip (compatible with Pythion 2.7)

### Deployment

The website can be depleyed using the following single linear command

```
cd ~/PATH_TO_REPO
cd lifesciencescrapping
```
and
```
python api_server.py
```
and visit in your browser
```
http://localhost:8000
```

## API

The api can be quried using the folling curl

### Example for searching cancer

```
curl "http://hunle.pythonanywhere.com/api/cancer" -H "DNT: 1" -H "Accept-Encoding: gzip, deflate" -H "Accept-Language: en-US,en;q=0.9" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36" -H "Accept: */*" -H "Referer: http://hunle.pythonanywhere.com/" -H "Cookie: sessionid=nv8118jaf9w69xt154d50yl099ybmx5l; _ga=GA1.2.1176568897.1549879661; _gid=GA1.2.834200829.1549879661" -H "Connection: keep-alive" --compressed
```

## Demo

For demo please visit : [Here]("http://hunle.pythonanywhere.com/")

## Authors

* **Muhammad Hunble Dhillon** [PurpleBooth](https://www.linkedin.com/in/muhammad-hunble-dhillon-b64b84a0/)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

* This is open source project, please fork extend add more arsers and feel free to get in touch with me.

## Acknowledgments

* [Bilal Wajid](https://pk.linkedin.com/in/dr-bilal-wajid-98949276)
* [NCBI API](https://www.ncbi.nlm.nih.gov/home/develop/api/)
* [Google Datasets Search Beta](https://toolbox.google.com/datasetsearch)
* [NCBI API](http://semver.org/)
* [Requests](http://docs.python-requests.org/en/master/)
* [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
* [xmljson](https://pydigger.com/pypi/xmljson)
* [Python Anywhere]("https://www.pythonanywhere.com")