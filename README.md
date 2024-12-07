# URL Fetcher Script with Proxy Support

This script automates the process of fetching content from a list of URLs, optionally using a proxy server. It rotates User-Agent strings to mimic real browser requests and includes error handling for failed requests. The script supports flexible configurations via command-line arguments.

## Features

- **URL Fetching**: Fetches content from a predefined list of URLs.
- **Proxy Support**: Optionally routes requests through a SOCKS5 proxy.
- **User-Agent Rotation**: Randomly selects a User-Agent string for each request.
- **Dynamic Sleep Intervals**: Pauses for a random time between requests to prevent detection.
- **Error Handling**: Handles and logs errors for failed requests.

## Requirements

- Python 3.7+
- `requests` library

## Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/sjhilt/fetch-blogs
   cd fetch-blogs
   ```

2. **Install Dependencies**:
   Install the `requests` library if not already installed:
   ```bash
   pip install requests
   ```

3. **Prepare User-Agent File**:
   Create a file named `ua.txt` in the script directory, and populate it with User-Agent strings (one per line).

4. **Configure Proxy**:
   Update the `proxy_ip` variable in the script to your proxy server's IP and port:
   ```python
   proxy_ip = "192.168.0.254:9050"  # Replace with your proxy server details
   ```

## Usage

### URL Fetcher Script
- To fetch URLs without a proxy:
  ```bash
  python url_fetcher.py
  ```
- To fetch URLs with a proxy:
  ```bash
  python url_fetcher.py --use-proxy
  ```

### PDF Papers Downloader Script
- To download partial PDFs without a proxy:
  ```bash
  python partial_pdf_downloader.py
  ```
- To download partial PDFs with a proxy:
  ```bash
  python partial_pdf_downloader.py --use-proxy
  ```

### Arguments
- `--use-proxy`: Routes requests through the configured proxy.

## File Structure
```
.
├── fetch_blogs.py          # The main Python script
├── download_papers.py # Script for partial PDF downloading
├── ua.txt             # User-Agent strings (one per line)
└── README.md          # This README file
```

## Script Workflow

1. **URL List**: The script iterates through a predefined list of URLs.
2. **User-Agent Selection**: A random User-Agent string is chosen for each request.
3. **IP Verification**: The script fetches the current IP (via `https://icanhazip.com/`) to verify whether the proxy is used.
4. **Content Fetching**: Each URL is fetched with or without the proxy, based on the `--use-proxy` argument.
5. **Error Handling**: Logs errors for failed requests.
6. **Dynamic Sleep**: Pauses for a random interval (60-120 seconds) between iterations.

## Example Output

```
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)
Current IP: 203.0.113.42
Successfully fetched: https://example.com
Sleeping for 87 seconds...
```

## Customization

### Adding URLs
To add URLs for fetching, modify the `urls` list in the script:
```python
urls = [
    "https://example.com",
    "https://another-example.com"
]
```

### Updating the Proxy
Change the `proxy_ip` variable to use a different proxy server:
```python
proxy_ip = "192.0.2.1:9050"  # Replace with your proxy details
```

### Adjusting Sleep Time
Modify the random sleep interval in the script:
```python
sleep_time = random.randint(60, 120)  # Adjust time range as needed
```

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contribution

Feel free to fork this repository and submit pull requests for enhancements or bug fixes. For major changes, please open an issue first to discuss your ideas.

## Author

Stepehn Hilt

