from http.server import HTTPServer, BaseHTTPRequestHandler

content = '''
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body bgcolor="cyan">
    <table border="1" align="center" bgcolor="pink" cellpadding="10"
    <caption><h1 align="center">List of protocol</h1></caption>
    <tr>
        <th>S.NO</th>
        <th>Name of Layers</th>
        <th>Name of protocols</th>
    </tr>
    <tr>
        <td>1</td>
        <td>Application Layer</td>
        <td>HTTP,FTP</td>
    </tr>
    <tr>
        <td>2</td>
        <td>Transport Layer</td>
        <td>TCP & UDP</td>
    </tr>
    <tr>
        <td>3</td>
        <td>Internet Layer</td>
        <td>ICMP & ARP</td>
    </tr>
    <tr>
        <td>4</td>
        <td>Network Access Layer</td>
        <td>Ethernet & Frame Relay</td>
    </tr>
    </table>
</body>
</html>
'''

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200) 
        self.send_header("content-type", "text/html")       
        self.end_headers()
        self.wfile.write(content.encode())

print("This is my webserver") 
server_address =('',8000)
httpd = HTTPServer(server_address,MyServer)
httpd.serve_forever()
