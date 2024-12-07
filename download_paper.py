import requests
import random
import time
import argparse

# Define the list of URLs to fetch
urls = [
    "https://example.com/file.pdf",
    "https://another-example.com/file.pdf"
]

# Load user-agent strings from a file (ua.txt)
# Each line in the file represents a different User-Agent string
with open("ua.txt", "r") as f:
    user_agents = [line.strip() for line in f if line.strip()]

# Proxy IP and port setup
proxy_ip = "192.168.0.254:9050"  # Replace with your proxy server's IP and port
proxies = {
    "http": f"socks5h://{proxy_ip}",
    "https": f"socks5h://{proxy_ip}",
}


def fetch_url(url, headers=None, use_proxy=False):
    """
    Fetch a URL with optional headers and proxy support.
    
    Parameters:
        url (str): The URL to fetch.
        headers (dict): Optional HTTP headers (e.g., User-Agent).
        use_proxy (bool): Whether to route the request through the proxy.
    
    Returns:
        Response object if the request succeeds.
        Error message (str) if the request fails.
    """
    try:
        # Use proxies if specified
        if use_proxy:
            response = requests.get(url, headers=headers, proxies=proxies, timeout=10)
        else:
            response = requests.get(url, headers=headers, timeout=10)
        return response
    except requests.exceptions.RequestException as e:
        # Return an error message if the request fails
        return f"Error fetching URL {url}: {e}"


def download_partial_pdf(url, headers=None, use_proxy=False):
    """
    Download the first few bytes of a PDF file.
    
    Parameters:
        url (str): The PDF URL to fetch.
        headers (dict): Optional HTTP headers (e.g., User-Agent, Range).
        use_proxy (bool): Whether to route the request through the proxy.
    
    Returns:
        Message indicating success or failure.
    """
    try:
        if headers is None:
            headers = {}
        headers["Range"] = "bytes=0-3"  # Request only the first few bytes

        # Fetch the partial content
        response = fetch_url(url, headers=headers, use_proxy=use_proxy)
        if isinstance(response, str):  # Check if an error message was returned
            return response
        elif response.status_code == 206:  # Partial content status code
            # Save the partial content to a file
            file_name = url.split("/")[-1]
            with open(file_name, "wb") as f:
                f.write(response.content)
            return f"Successfully downloaded partial content to {file_name}"
        else:
            return f"Failed to download content from {url}. Status Code: {response.status_code}"
    except Exception as e:
        return f"Error downloading partial PDF: {e}"


# Set up command-line argument parser
parser = argparse.ArgumentParser(description="Fetch URLs with or without a proxy.")
parser.add_argument("--use-proxy", action="store_true", help="Use proxy for requests")
args = parser.parse_args()  # Parse arguments from the command line

# Infinite loop to repeatedly cycle through the URLs
while True:
    for url in urls:
        # Select a random User-Agent string for each request
        user_agent = random.choice(user_agents)
        headers = {"User-Agent": user_agent}
        print(f"User-Agent: {user_agent}")

        # Fetch the current IP address (to verify proxy usage)
        ip_response = fetch_url("https://icanhazip.com/", use_proxy=args.use_proxy)
        if isinstance(ip_response, str):  # Check if an error message was returned
            print(ip_response)
        else:
            print(f"Current IP: {ip_response.text.strip()}")  # Print the fetched IP

        # Download the partial PDF content
        result = download_partial_pdf(url, headers=headers, use_proxy=args.use_proxy)
        print(result)

        # Sleep for a random interval between 60 and 120 seconds
        sleep_time = random.randint(60, 120)
        print(f"Sleeping for {sleep_time} seconds...")
        time.sleep(sleep_time)
