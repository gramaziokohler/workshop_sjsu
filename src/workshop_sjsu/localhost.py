import http.server
import socketserver
import os

PORT = 8000

webdir = os.path.join(os.path.dirname(__file__), 'web')
webdir = webdir.replace("\\","/")
os.chdir(webdir)

Handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(("", PORT), Handler)
print("serving at port", PORT)
httpd.serve_forever()
