import requests

def check_website(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"{url} is ONLINE ✅")
        else:
            print(f"{url} returned status code: {response.status_code} ⚠️")
    except requests.exceptions.RequestException as e:
        print(f"{url} is OFFLINE ❌")
        print(f"Reason: {e}")

# Example usage
website = input("Enter website URL (e.g., https://example.com): ")
check_website(website)
