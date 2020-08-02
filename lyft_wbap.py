""" Basic JSON flask web-app """

from flask import Flask
from flask import request
import json

app = Flask(__name__)

""" If a POST request method comes in to the test directory
then run the function 'test' """
@app.route('/test', methods=['POST'])
def test():
    """ The raw json string POST'd to the server (request.data)
	Take this data and load it from JSON into a python Dictionary
	for parsing """
    pst_dict = json.loads(request.data)

    """ We can assume the dict key is always 'string_to_cut' """
    raw_third = pst_dict['string_to_cut']
    parse_third = ""

    """ Loop through, add every third letter
	to a new string (parse_third) """
    for letter in range(0, len(raw_third)):
        if (letter + 1) % 3 is 0:
            parse_third += raw_third[letter]

    """ Place the string into a dictionary """
    parse_dict = {}
    parse_dict['return_string'] = parse_third

    """ Convert the string into JSON and return the JSON string """
    return json.dumps(parse_dict)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
