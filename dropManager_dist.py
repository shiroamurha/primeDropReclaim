from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
#import requests
import os



####################poe teus cookie aqui do jeito q ta organizado
####################put your cookies like it is organized
own_session_cookies = [

	{
		'name': "at-main",
		'value': " - your cookie - ",
	},

	{
		'name': "aws-target-visitor-id", 
		'value': " - your cookie - "
	},

    {
	    'name': "sess-at-main",
	    'value': " - your cookie - "
    },

    {
	    'name': "session-id", 
	    'value': " - your cookie - "
    },

    {
	    'name': "session-id-time", 
	    'value': " - your cookie - "
    },

    {
	    'name': "session-token", 
	    'value': " - your cookie - "
	},

	{
		'name': "sst-main", 
		'value': " - your cookie - "
	}, 	

	{
		'name': "ubid-main", 
		'value': " - your cookie - "
	},

    {
	    'name': "x-main", 
	    'value': ' - your cookie - '
    },

	{
		'name': "unique_id", 
		'value': " - your cookie - "
	}
]


# verificador usando requests, nao da certo pq nao usa js no request
# def verifier():	
# 	website_request = requests.Session()

# 	website_home_html = website_request.request(

# 		'get',
# 		'https://gaming.amazon.com/home',
# 		cookies=own_session_cookies

# 	)

# 	return website_home_html.text



###############################
# verificador usando webdriver
def isClaimed():

	local_path = rf'{os.path.dirname(os.path.realpath(__file__))}\\chromedriver.exe'

	options = webdriver.ChromeOptions()
	options.add_argument('--headless')
	options.add_argument('--no-sandbox')
	options.add_argument('--disable-dev-shm-usage')
	options.add_argument("--log-level=3")

	driver_service = Service(local_path)
	driver = webdriver.Chrome(
		service=driver_service,
		options=options
	)
	print('\nloading...\n')
	
	driver.get('https://gaming.amazon.com/')
	sleep(5)

	for i in range(-1, 9):
		driver.add_cookie(own_session_cookies[i])

	driver.get('https://gaming.amazon.com/home')
	sleep(3)

	website_home_html = BeautifulSoup(driver.page_source, features="html.parser")

	try:
		claimValue = website_home_html.find(

			'a', 
			attrs={

				'aria-label':'League of Legends: Prime Gaming Capsule'
			}).find(

				'p', 
				class_="redeem__claimed-text tw-font-size-6"
			).contents
	except AttributeError:
		claimValue = None

	if claimValue is not None:
		print('Drop already claimed.')
		return True 
	else:
		print('Drop claimable.')
		return False

###############################

def dropReclaim():

	local_path = rf'{os.path.dirname(os.path.realpath(__file__))}\\chromedriver.exe'

	options = webdriver.ChromeOptions()
	options.add_argument('--headless')
	options.add_argument('--no-sandbox')
	options.add_argument('--disable-dev-shm-usage')
	options.add_argument("--log-level=3")

	driver_service = Service(local_path)
	driver = webdriver.Chrome(
		service=driver_service,
		options=options
	)
	print('\nloading...\n')
	
	driver.get('https://gaming.amazon.com/')
	sleep(3)

	for i in range(-1, 9):
		driver.add_cookie(own_session_cookies[i])

	driver.get('https://gaming.amazon.com/loot/lol10') ##https://gaming.amazon.com/loot/lol10

	try:

		WebDriverWait(driver, 20).until(EC.visibility_of_element_located((
			By.CSS_SELECTOR, 
			"button[data-test-selector='AvailableButton'][data-a-target='AvailableButton']"
		))).click()

	except:
		print('\n  ---> something went wrong!!\n\n')
		raise Exception

	print('Claim Successful.')

	


def reclaimTry():

	if not isClaimed():
		dropReclaim()
	else:
		return


#print(f'is the drop claimed? {isClaimed()}')

