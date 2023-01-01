# ssl-expiration-date-checker
This Python script retrieves the expiration date of the SSL certificate for a given URL

This Python script retrieves the expiration date of the SSL certificate for a given URL. 
It does this by creating a socket and connecting to the URL using the create_connection method from the socket module. 
It then wraps the socket in an SSL context using the wrap_socket method from the ssl module and retrieves the SSL certificate using the getpeercert method.
Finally, it extracts the expiration date of the certificate from the notAfter field and prints it to the console.
