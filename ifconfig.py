from flask import Flask, request, Response
app = Flask(__name__)

from pprint import pformat

@app.route('/')
def hello():
    nl = '\r\n'

    lines = [
        'Request from ' + str(request.environ.get('REMOTE_ADDR', 'UNDEFINED'))
                  + ':' + str(request.environ.get('REMOTE_PORT', 'UNDEFINED')),
            '',
            ]

    lines += map(': '.join, request.headers.items())
    return Response(nl.join(lines), mimetype="text/plain")
