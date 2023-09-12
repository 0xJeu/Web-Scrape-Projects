# Data Scraping Project (Data_Scraper.py)

This Python project allows users to perform data scraping by specifying a website link and a CSS selector for the target element they want to scrape. The code retrieves the HTML content of the provided link, parses it using BeautifulSoup library, and extracts data based on the specified CSS selector.

## Prerequisites

Make sure you have the following prerequisites installed:

- Python 3.x
- BeautifulSoup (`pip install beautifulsoup4`)
- Requests (`pip install requests`)
- Validators (`pip install validators`)

## Usage

1. Clone the repository or download the code files.

2. Install the required dependencies mentioned in the prerequisites section.

3. Run the script `scraping_project.py` in a Python environment.

4. Enter the website link when prompted. Make sure to provide a valid URL.

5. Enter the CSS selector for the target element. This selector specifies the HTML element(s) you want to scrape from the webpage. Refer to the CSS selector syntax and rules for correct usage.

6. The script will make an HTTP request to the provided URL, retrieve the HTML content, and extract the desired data based on the specified selector.

7. The scraped data will be displayed on the console.

Note: If no data is found for the specified selector, a message indicating the absence of data will be displayed.

## Examples

- Example 1:
  ```
  Enter website link here: https://www.example.com
  Enter the CSS selector for the target element: h1
  ```
  Output:
  ```
  Scraped data:
  Welcome to Example
  ```

- Example 2:
  ```
  Enter website link here: https://www.example.com
  Enter the CSS selector for the target element: .description
  ```
  Output:
  ```
  Scraped data:
  This is an example website.
  ```


# Google Search Automation (Search.py)

This Python code utilizes the Selenium library to automate a Google search. It opens a Chrome browser, navigates to Google's homepage, and performs a search based on user input.

## How It Works

- The code imports necessary modules from Selenium to interact with the browser.

- It prompts the user to enter a search query.

- Chrome options are set to enable the browser window to detach from the script after execution.

- The webdriver is configured to use the Chrome browser.

- The webdriver navigates to "https://www.google.com/".

- The user's search query is entered into the search input field on the Google homepage.

- The search is performed by sending the Enter key (\n) to the search input.

## How to Use

To use this code, follow these steps:

1. Make sure you have Python installed on your system.

2. Install the necessary dependencies by running the command: `pip install selenium webdriver_manager`.

3. Import the necessary modules (selenium, webdriver, ChromeDriverManager, Options, By, Keys).

4. Copy the provided code into a Python file (e.g., `google_search.py`).

5. Run the Python file.

6. Enter the search query when prompted by the script.

7. The script will open a Chrome browser, navigate to Google's homepage, perform the search, and display the search results.

8. After the search is completed, you can interact with the browser window as needed. The script will continue running in the background.

9. When finished, you can terminate the script or close the browser window.

## Acknowledgments

The code is built upon the BeautifulSoup and Requests libraries. Special thanks to the authors and contributors of these libraries for providing powerful tools for web scraping in Python.
