from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def run_chrome():
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument('--start-maximized')  # Start browser maximized
    
    # Create a new Chrome driver instance
    driver = webdriver.Chrome(options=chrome_options)
    
    # Navigate to a website
    driver.get('https://www.google.com')
    
    # Keep the browser open until user input
    input('Press Enter to close the browser...')
    
    # Close the browser
    driver.quit()

if __name__ == "__main__":
    run_chrome()