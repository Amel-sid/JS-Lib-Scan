# version_checker.py
import requests

def get_latest_version(library_name):
    url = f"https://registry.npmjs.org/{library_name}"
    try:
        response = requests.get(url)
        data = response.json()
        latest_version = data['dist-tags']['latest']
        return latest_version
    except requests.RequestException as e:
        print(f"Error fetching latest version for {library_name}: {e}")
        return None
    except KeyError:
        print(f"Could not find latest version for {library_name}. It may not exist on npm.")
        return None

