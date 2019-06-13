from flask import Flask
from flask import jsonify
from flask import request
import re
import pymongo

app = Flask(__name__)

connection = pymongo.MongoClient(
            "mongodb+srv://user1:password12345@cluster0-82tvq.mongodb.net/"
            "test?retryWrites=true&w=majority")

"""
    Name: get_request
    Parameters: None
    Usage: This function handles get requests at the end point request
"""
@app.route('/request', methods=['GET'])
def get_request():
    global connection
    args = request.args
    if len(args) == 0:
        return("No filtering parameters passed<br><br>Usage: One can search "
               "by 4 fields, namely Title, Author, Body and Url<br>"
               "Example:"
               "(a)request?Title=\"against 'book-up' credit\"<br>"
               "(b)request?Title=\"could be wiped out by fungal infection\""
               "&Author=\"Charles Anderson\"<br>"
               "(c)request?Url='smoking'\"<br>")
    else:
        query_str = []
        try:
            if any(key not in ("Url", "Title", "Body", "Author") for key in args.keys()):
                return ("Not a valid key to filter on<br><br>Usage: One can search "
                "by 4 fields, namely Title, Author, Body and Url<br>"
                "Example:"
                "(a)request?Title=\"against 'book-up' credit<br>"
                "(b)request?Title=\"could be wiped out by fungal infection\""
                "&Author=\"Charles Anderson<br>"
                "(c)request?Url='smoking'<br>")
            for key, val in args.items():
                regx = re.compile(val.strip("\"'"), re.IGNORECASE)
                query_str.append({key.strip(): regx})
                output = []
                db = connection['theguardian']
                collection = db['data']
                for s in collection.find({'$and': query_str}):
               	    output.append({'Title': s['Title'], 'Url': s['Url'],
                                   'Author': s['Author']})
                return jsonify({'result': output})
        except (pymongo.errors.OperationFailure,
            pymongo.errors.ServerSelectionTimeoutError) as e:
            return(str(e))


if __name__ == '__main__':
    app.run()
