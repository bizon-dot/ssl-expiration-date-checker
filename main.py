import socket
import ssl
import urllib.request

urls = [
    "https://www.example.com",
]

for url in urls:
    url = urllib.request.urlparse(url).hostname

    print(f"Checking {url}...")
    
    sock = socket.create_connection((url, 443))

    context = ssl.create_default_context()
    conn = context.wrap_socket(sock, server_hostname=url)

    cert = conn.getpeercert()

    expiration_date = cert["notAfter"]

    print(f"{url} expires on {expiration_date}")
