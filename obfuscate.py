import socket
import ssl

# Assume host and port have been provided as parameters
host = 'www.example.com'
port = 443

# Create a socket and wrap it with an SSL/TLS layer
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ssl_sock = ssl.wrap_socket(s, cert_reqs=ssl.CERT_NONE)
ssl_sock.connect((host, port))

# Send an HTTP request to the host
request = b"GET / HTTP/1.1\r\nHost: www.example.com\r\n\r\n"
ssl_sock.send(request)

# Read the response from the server
response = ssl_sock.recv(4096)

# Obfuscate the response by replacing the SSL/TLS headers with regular HTTP headers
obfuscated_response = response.replace(b"HTTP/1.1 200 Connection Established\r\n\r\n", b"HTTP/1.1 200 OK\r\n\r\n")

# Send the obfuscated response back to the client
client_socket.send(obfuscated_response)

# Close the connection
ssl_sock.close()
