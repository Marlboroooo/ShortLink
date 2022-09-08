import os

API_KEY = os.getenv('API_KEY')
if not API_KEY:
    exit("Error: no API-key provided")


API_URL = ('http://cutt.ly/api/api.php?key=' + API_KEY + '&short={url}')
