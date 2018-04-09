import socket

HOST, PORT = '', 8888

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(3)
print ('Serving HTTP on port %s ..' % PORT)
while True:
    print("waiting for connection...")
    client_connection, client_address = listen_socket.accept()
    request = client_connection.recv(1024)
    print (request)
    html_content="""<!DOCTYPE html>
    <html>
    <head>
        <title>
            Sample page
        </title>
        <style>
            body
            {
                font-family: arial,verdana,sans-serif,Georgia, "Times New Roman", Times, serif;
                text-align:center;
                background:#cceeff;
            }
            h1
            {
                text-shadow: 5px 5px 5px #aaaaaa;
            }
        </style>

        <meta name="keywords" content="HTML, sample page">
        <meta name="description" content="This is a sample page to illustrate how to write HTML code for a web page.">

        <script type="text/javascript">
            function message()
            {
                alert("This is a Javascript alert box.")
            }
        </script>
    </head>
    <body>
        <h1>Hello World!</h1>
        <p>This is the page content.</p>
        <button onclick="message()">Click me!</button>
    </body>
</html>

"""
                 
    print("Length of the content is:")
    print(len(html_content))
    length=len(html_content)
    file_content = "Hello wolrd"
    http_response = """
\HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: %d

%s
"""%(length, html_content)
        
        #file_content = f.readlines()
    print (http_response)
    client_connection.sendall(http_response.encode())
    client_connection.close()
