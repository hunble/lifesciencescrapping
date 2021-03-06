import os.path
from flask import Flask, request, Response
from flask_restful import Resource, Api
import json
from flask import jsonify
#from flask.ext.jsonpify import jsonify
import googleDataSetSearch as gds
import ncbi as ncbi
import dataGov as gov
import Result
import math
import allInOne

app = Flask(__name__)
api = Api(app)

def root_dir():  # pragma: no cover
    return os.path.abspath(os.path.dirname(__file__))

def get_file(filename):  # pragma: no cover
    try:
        src = os.path.join(root_dir(), filename)
        # Figure out how flask returns static files
        # Tried:
        # - render_template
        # - send_file
        # This should not be so non-obvious
        return open(src).read()
    except IOError as exc:
        return str(exc)


@app.route('/', methods=['GET'])
def metrics():  # pragma: no cover
    content = get_file('index.html')
    return Response(content, mimetype="text/html")

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def get_resource(path):  # pragma: no cover
    mimetypes = {
        ".css": "text/css",
        ".html": "text/html",
        ".js": "application/javascript",
    }
    complete_path = os.path.join(root_dir(), path)
    ext = os.path.splitext(path)[1]
    mimetype = mimetypes.get(ext, "text/html")
    content = get_file(complete_path)
    return Response(content, mimetype=mimetype)

class AllInOne(Resource):
    def get(self):
		args = request.args
		print (args) # For debugging
		query = args['query']
		print("A search made for: ", query)

		result = allInOne.allInOne(query)

		return jsonify(result)

	
class Search(Resource):
    def get(self):
        args = request.args
        print (args) # For debugging
        query = args['query']
        pageNumber = int(args['pageNumber'])
        pageSize = int(args['pageSize'])


        print("A search made for: ", query, pageNumber, pageSize, gds)

        data = ncbi.search(query)
        googleResult = gds.search(query)
        govResult = gov.search(query)

        data.extend(govResult)
        data.extend(googleResult)


          #  1,2,3,4, 5,6,7, 8,9

        results = []



        # here goes the paginantion logic

        pages = math.ceil(float(len(data))/float(pageSize))

        if pages >= pageNumber:

            s = pageNumber * pageSize
            e = (pageNumber * pageSize)  + pageSize 

            for d in data[s:e]:
                if d[1] == Result.GOOGLE :
                    results.append(gds.getSummary(d[0]))
                elif d[1] == Result.NCBI :
                    results.append(ncbi.getSummary(d[0]))
                elif d[1] == Result.DATA_GOV :
                    results.append(gov.getSummary(d[0]))

        result = {}

        result["query"] = query
        result["pages"] =  pages
        result["records"] =  results


        return jsonify(result)


class Pages(Resource):
    def get(self):
        args = request.args
        print (args) # For debugging
        query = args['query']
        pageSize = int(args['pageSize'])

        print("A search made for: ", query, pageSize, gds)

        data = ncbi.search(query)
        googleResult = gds.search(query)   
        govResult = gov.search(query)

        data.extend(googleResult)
        data.extend(govResult)


        pages = math.ceil(float(len(data))/float(pageSize))

        result = {}

        result["query"] = query
        result["total_reocrds"] = len(data)
        result["pages"] = pages

        return jsonify(result)

api.add_resource(Search, '/api/search', endpoint='search') # Route_1
api.add_resource(Pages, '/api/pages', endpoint='pages') # Route_2
api.add_resource(AllInOne, '/api/allInOne', endpoint='allInOne') # Route_3


if __name__ == '__main__':
     app.run(port='8000')
