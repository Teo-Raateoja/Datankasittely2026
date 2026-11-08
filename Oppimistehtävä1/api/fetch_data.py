import requests

def fetch_data(api_url):
    try:
        response = requests.get(api_url)
        response.raise_for_status()  
        return response.json()
    except Exception as e:
        print(f"Error fetching data from {api_url}: {e}")
        return None