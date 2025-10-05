import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re

def scrape_js_libraries(url, js_path=""):
    js_libraries = []
    ignored_files = ['index', 'main', 'api','Unknown','front-page','cdn','wp-']
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        for script in soup.find_all('script', src=True):
            script_url = urljoin(url, script['src'])
            lib_name, version = extract_name_and_version(script_url)

            if not any(ignored in lib_name for ignored in ignored_files):
                js_libraries.append({
                    'library_name': lib_name,
                    'current_version': version
                })
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")

    return js_libraries

def extract_name_and_version(script_url):
    # Cette regex est une approche basique et peut ne pas fonctionner pour toutes les structures d'URL
    name_match = re.search(r'/([a-zA-Z0-9\-_]+)(\.min)?\.js', script_url)
    # Extraire la version après le paramètre `?ver=`
    version_match = re.search(r'\?ver=([0-9a-zA-Z\.\-_]+)', script_url)

    lib_name = name_match.group(1) if name_match else "Unknown"
    version = version_match.group(1) if version_match else "Unknown"

    return lib_name, version
