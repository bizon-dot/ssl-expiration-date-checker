import socket
import ssl
import urllib.request
from datetime import datetime
from rich.console import Console
from rich.table import Table
console = Console()
urls = [
   ## Sites 
]
table = Table(title="Scadenza certificati SSL", show_header=True)
table.add_column("URL", style="bold")
table.add_column("Scadenza", style="dim")
table.add_column("Giorni restanti")
for url in urls:
    url = urllib.request.urlparse(url).hostname
    sock = socket.create_connection((url, 443))
    context = ssl.create_default_context()
    conn = context.wrap_socket(sock, server_hostname=url)
    cert = conn.getpeercert()
    expiration_date = cert["notAfter"]
    expiration_date_dt = datetime.strptime(expiration_date, "%b %d %H:%M:%S %Y %Z")
    remaining_days = (expiration_date_dt - datetime.utcnow()).days
    row_style = "green"
    if remaining_days <= 30:
        row_style = "yellow"
    if remaining_days <= 7:
        row_style = "red"
    table.add_row(url, expiration_date, str(remaining_days), style=row_style)
console.print(table)
