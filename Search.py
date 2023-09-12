from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

try:
    user_input = input("Please enter Google Search:")

    # Specify the path to the ChromeDriver executable
    chrome_driver_path = '/Users/stephanejeudy/Downloads/chromedriver-mac-arm64/chromedriver'

    # Set up ChromeOptions if needed (e.g., to run headless)
    chrome_options = Options()
    # Add options as needed, for example:
    # chrome_options.add_argument('--headless')

    # Create a Service object with the specified ChromeDriver path
    chrome_service = Service(executable_path=chrome_driver_path)

    # Create a WebDriver instance using the Service object and ChromeOptions
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

    driver.get("https://www.google.com/")

    search = driver.find_element(By.NAME, "q")
    search.send_keys(f"{user_input}\n")

    # Add a pause here if needed to observe the browser window
    input("Press Enter to continue...")

except Exception as e:
    print(f"An error occurred: {str(e)}")

finally:
    # Close the browser window
    driver.quit()
