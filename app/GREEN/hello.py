from wsgiref.simple_server import make_server
#print('Hello, world!')
GREETING = b'Hello, GREEN TEAM!\n (version 3)'
#
def hello(environ, start_response):
        start_response('200 OK', [('Content-Type', 'text/plain')])
        return [GREETING]

make_server('0.0.0.0', 9000, hello).serve_forever()
