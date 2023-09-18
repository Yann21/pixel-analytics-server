import http.server
import socketserver
import csv
from urllib.parse import urlparse, parse_qs

PORT = 8888
CSV_FILE = "requests.csv"

class RequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Parse the URL and extract the query parameters
        parsed_url = urlparse(self.path)
        query_params = parse_qs(parsed_url.query)

        # Write the query parameters to a CSV file
        with open(CSV_FILE, mode="a", newline="") as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(query_params.keys())

        # Serve the pixel GIF image
        self.send_response(200)
        self.send_header("Content-type", "image/gif")
        self.end_headers()

        # Load and serve the pixel.gif image
        with open("images/pixel.gif", "rb") as image_file:
            self.wfile.write(image_file.read())

with socketserver.TCPServer(("", PORT), RequestHandler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()

