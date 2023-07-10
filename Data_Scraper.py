from bs4 import BeautifulSoup
import requests
from requests.exceptions import RequestException
import validators


def get_url():
    while True:
        url = input("Enter website link here: ")
        if validators.url(url):
            return url
        else:
            print("Invalid URL. Please enter a valid URL.")


def get_selector():
    selector = input("Enter the CSS selector for the target element: ")
    return selector


def make_request(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) "
                      "Version/16.4 Safari/605.1.15",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "sec-fetch-site": "none",
        "Accept-Encoding": "gzip, deflate",
        "upgrade-insecure-requests": "1",
        "sec-fetch-mode": "navigate",
    }

    try:
        with requests.get(url, headers=headers) as response:
            response.raise_for_status()
            return response.text
    except RequestException as e:
        print("An error occurred during the request:", e)
        return None


def parse_html(html_content):
    return BeautifulSoup(html_content, "html.parser")


def scrape_data(soup, selector):
    elements = soup.select(selector)
    if elements:
        return [element.text for element in elements]
    else:
        return []


def main():
    url = get_url()
    selector = get_selector()

    html_content = make_request(url)
    if html_content:
        soup = parse_html(html_content)
        scraped_data = scrape_data(soup, selector)

        if scraped_data:
            print("Scraped data:")
            for data in scraped_data:
                print(data)
        else:
            print("No data found for the specified selector.")


if __name__ == "__main__":
    main()
