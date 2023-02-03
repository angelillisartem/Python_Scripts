from urllib.parse import urlparse #Install library "urllib" with [pip install urllib]

def valida_url(url):
    try:
        rs = urlparse(url)
        return all([rs.scheme, rs.netloc])
    except ValueError:
        return False

url = str(input("Inserisci url da validare!"))

if valida_url(url):
    print("URL valido.")
else:
    print("URL non valido.")