import http.server
import socketserver

# Define the port to listen on
PORT = 8080

# Create a request handler
Handler = http.server.SimpleHTTPRequestHandler

# Create a TCP server object that listens on the specified port
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving on port {PORT}")
    
    # Serve until interrupted
    httpd.serve_forever()
