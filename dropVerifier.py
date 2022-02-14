from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
import requests
import os


####################poe teus cookie agui do jeito q ta organizado
own_session_cookies = [

	{
		'name': "at-main",
		'value': "Atza|IwEBIItHD15BtP9u-4eT5GcFu7FrproZstGRUf64AyjOywhU3qj2RRvY1sCKEWfgPgRcZh2fEJ5cFw0uTT1qsm36dHA-T-OXk4W4b-oXJV381BmzH0nL_pxbg4ghGNlowA0vhwyFjwoz85c4D-SkN5JOkBfoCJNx8NfrVj8A2p99bH12UKXQh4rVuGZ9vogiKCr9sDI2Vu2FOrpcw3Aa9S9Q2F3CNCwFeqAxbaUhZ6awMYnTOv9z9zk9G9xEaTgD-ApUTuA",
	},

	{
		'name': "aws-target-visitor-id", 
		'value': "1644785385687-174230"
	},

    {
	    'name': "sess-at-main",
	    'value': "\"oliYQVINONqaTyI4q1KQn1Sd4+C2E97tYfXZ6FhaNMQ=\""
    },

    {
	    'name': "session-id", 
	    'value': "146-9671765-0428218"
    },

    {
	    'name': "session-id-time", 
	    'value': "2082787201l"
    },

    {
	    'name': "session-token", 
	    'value': "3DbAoEebS/X/X7ceY6DnQYSZZhWAojAtzEZKHXxZyyv7R1eGiKWuA9qy3tqAB6Hs6EWU9IIZQOS6yNkbB/wdjjG0uW3bOivtoomuvwodGfzcWWOH1dslO70H+89Ebed89wSkPgVx0CvHVO20gMb+Avp1nAY8z8uZ/YdxHpeFr2ABltBvF5hc/dZZjIpJjQcCl1gizC1M+2nTSaANqC0iqQ=="
	},

	{
		'name': "sst-main", 
		'value': "Sst1|PQFu8eGtN4efGhAhyuuQ9y2aCaRkc67RcfjWPA640lIiQm75rwgusvFmYIOMfj15rn4Xh6OHEgIbSGACa1xIXY6c09uytvGOUDzUqw7zEMA-Z98-zoJHgzQSp41zAd6g1LV09ze17Tis48pa5TAEaH6i4lNdplKmHWX202qS29FwJEVKFHMz0Gxo_QPvRaCoMGu3burlBEidzfFJpEN8UPyuRRhqelYMAfbUIOhcJ_CHepWW_0fNqEbI1CgaVbpHU1Wo-3lubQRCMUbD96bSTzVmyx5FPPkLTedeRS61nf6eUcw"
	}, 	

	{
		'name': "ubid-main", 
		'value': "130-4236462-2965160"
	},

    {
	    'name': "x-main", 
	    'value': '\"DNQYcU0YC8a7V9WQI0kVhMDg990E?g7psBuql2qDdWjO1YtGkMbNt5k2NpueB@NM\"'
    },

	{
		'name': "unique_id", 
		'value': "f9c4124bfdc110fe"
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

	driver.get('https://gaming.amazon.com/')
	print('\nloading...\n')
	sleep(5)

	for i in range(-1, 9):
		driver.add_cookie(own_session_cookies[i])

	driver.get('https://gaming.amazon.com/home')
	sleep(5)

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
		return True 
	else:
		return False

print(f'o drop foi reclamado? {isClaimed()}')

