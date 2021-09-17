import http.server
import socketserver
import os

PORT = 8000

webdir = os.path.join(os.path.dirname(__file__), '..', '..', 'web')
webdir = os.path.abspath(webdir)

webdir = webdir.replace("\\", "/")
os.chdir(webdir)

Handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(("", PORT), Handler)
print("serving at port", PORT)
httpd.serve_forever()

# check out http://127.0.0.1:8000/example00.html
