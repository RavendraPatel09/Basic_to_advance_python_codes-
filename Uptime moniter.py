import requests
import time

def monitor_websites(websites, check_interval_seconds=60):
    print("Starting website monitor... Press Ctrl+C to stop.")
    
    while True:
        for url in websites:
            try:
                # Send a GET request to the website
                response = requests.get(url, timeout=5)
                
                # 200 means "OK" in HTTP status codes
                if response.status_code == 200:
                    print(f"[UP] {url} is running fine.")
                else:
                    print(f"[WARNING] {url} returned status code: {response.status_code}")
                    
            except requests.exceptions.RequestException as e:
                # This catches connection errors, timeouts, etc.
                print(f"[DOWN] Alert! {url} is unreachable. Error: {e}")
                
        print("-" * 30)
        # Wait before checking again
        time.sleep(check_interval_seconds)

# List the websites you want to keep an eye on
my_sites = [
    'https://www.google.com',
    'https://this-site-probably-does-not-exist-999.com'
]

# Run the monitor (checks every 10 seconds for this example)
# monitor_websites(my_sites, 10)