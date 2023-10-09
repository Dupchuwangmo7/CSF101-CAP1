from selenium import webdriver 
# selenium automates web related task
from selenium. webdriver.chrome. service import Service
#manage the ChromeDriver service when working with Google Chrome through Selenium.
from selenium. webdriver. chrome.options import Options
#customize and configure how the Chrome browser behaves when controlled by Selenium.
from webdriver_manager. chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import requests
from urllib.parse import quote 


option = Options()
#This allows you to run Chrome in the background without displaying a graphical user interface.
option.add_experimental_option("detach", True)#used to configure options for the Chrome WebDriver in Selenium.
#setting "detach" to True will keep the browser window open for you to do so.

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)
#used to automate interactions with the Google Chrome browser according to your desired settings and preferences.


# driver.get("https://www.bbc.com/news/science_and_environment")
driver.get("https://kuenselonline.com")
#driver.maximize_window()

headline = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/h3/a").text

#print(headline)



def send_message(message):
    token = '6508367929:AAFWGUfCFA9_rnz5v_CIbSU_6Rt9xC5z9u4'
    chat_id = '-1001939796437'
    message = quote(message)
    url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
    print(requests.get(url).json())
    
send_message(headline)
