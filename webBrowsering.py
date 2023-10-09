#from selenium import webdriver

# Initialize the Firefox WebDriver with the path to Geckodriver (if not in PATH)
# driver = webdriver.Firefox(executable_path='/path/to/geckodriver')

# If Geckodriver is in PATH, you can simply use:
#driver = webdriver.Firefox()

# Open a website
#driver.get("https://www.example.com")

# Perform interactions with the web page here

# Close the browser when you're done
#driver.quit()
#from selenium import webdriver
#from selenium. webdriver. chrome. service import Service
#from selenium. webdriver. chrome. options import Options
#from webdriver_manager. chrome import ChromeDriverManager 
  

#options = Options()
#options.add_experimental_option("detach", True)


#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


#driver.get("chrome://newtab/")
#driver.maximize_window()
# from selenium import webdriver
# from selenium. webdriver.chrome. service import Service
# from selenium. webdriver. chrome.options import Options
# from webdriver_manager. chrome import ChromeDriverManager

# option = Options()
# option.add_experimental_option("detach", True)

# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)
# driver.get("https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwjnodiN6cyBAxUp2DgGHcWwCGMQFnoECBYQAQ&url=https%3A%2F%2Fedition.cnn.com%2F&usg=AOvVaw38zNMfLTk2LQOqQ0E5F1-r&opi=89978449")
# #driver.maximize_window()

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import requests
from urllib.parse import quote

# Setup Chrome options
option = Options()
option.add_argument("--headless")  # Run Chrome in the background

# Setup WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)

# Define the URL to scrape
url = "https://kuenselonline.com"

# Navigate to the URL
driver.get(url)

# Find the headline
# You should specify a more specific selector for the headline element
headline = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/h3/a").text

# Send the headline to Telegram
def send_message(message):
    token = '6508367929:AAFWGUfCFA9_rnz5v_CIbSU_6Rt9xC5z9u4'
    chat_id = '-1001939796437'
    message = quote(message)
    url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
    print(requests.get(url).json())

send_message(headline)

# Close the WebDriver
driver.quit()
