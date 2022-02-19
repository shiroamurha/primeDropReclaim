from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

own_session_cookies = [

	{
		'name': "at-main",
		'value': "Atza|IwEBIItHD15BtP9u-4eT5GcFu7FrproZstGRUf64AyjOywhU3qj2RRvY1sCKEWfgPgRcZh2fEJ5cFw0uTT1qsm36dHA-T-OXk4W4b-oXJV381BmzH0nL_pxbg4ghGNlowA0vhwyFjwoz85c4D-SkN5JOkBfoCJNx8NfrVj8A2p99bH12UKXQh4rVuGZ9vogiKCr9sDI2Vu2FOrpcw3Aa9S9Q2F3CNCwFeqAxbaUhZ6awMYnTOv9z9zk9G9xEaTgD-ApUTuA", 	
		'url': 'https://gaming.amazon.com/'
	},

	{
		'name': "aws-target-visitor-id", 
		'value': "1644785385687-174230", 	
		'url': 'https://gaming.amazon.com/'
	},

    {
	    'name': "sess-at-main",
	    'value': "\"oliYQVINONqaTyI4q1KQn1Sd4+C2E97tYfXZ6FhaNMQ=\"", 	
		'url': 'https://gaming.amazon.com/'
    },

    {
	    'name': "session-id", 
	    'value': "146-9671765-0428218", 	
		'url': 'https://gaming.amazon.com/'
    },

    {
	    'name': "session-id-time", 
	    'value': "2082787201l", 	
		'url': 'https://gaming.amazon.com/'
    },

    {
	    'name': "session-token", 
	    'value': "3DbAoEebS/X/X7ceY6DnQYSZZhWAojAtzEZKHXxZyyv7R1eGiKWuA9qy3tqAB6Hs6EWU9IIZQOS6yNkbB/wdjjG0uW3bOivtoomuvwodGfzcWWOH1dslO70H+89Ebed89wSkPgVx0CvHVO20gMb+Avp1nAY8z8uZ/YdxHpeFr2ABltBvF5hc/dZZjIpJjQcCl1gizC1M+2nTSaANqC0iqQ==", 	
		'url': 'https://gaming.amazon.com/'
	},

	{
		'name': "sst-main", 
		'value': "Sst1|PQFu8eGtN4efGhAhyuuQ9y2aCaRkc67RcfjWPA640lIiQm75rwgusvFmYIOMfj15rn4Xh6OHEgIbSGACa1xIXY6c09uytvGOUDzUqw7zEMA-Z98-zoJHgzQSp41zAd6g1LV09ze17Tis48pa5TAEaH6i4lNdplKmHWX202qS29FwJEVKFHMz0Gxo_QPvRaCoMGu3burlBEidzfFJpEN8UPyuRRhqelYMAfbUIOhcJ_CHepWW_0fNqEbI1CgaVbpHU1Wo-3lubQRCMUbD96bSTzVmyx5FPPkLTedeRS61nf6eUcw", 	
		'url': 'https://gaming.amazon.com/'
	},
	
	{
		'name': "ubid-main", 
		'value': "130-4236462-2965160",
		'url': 'https://gaming.amazon.com/'
	},

    {
	    'name': "x-main", 
	    'value': '\"DNQYcU0YC8a7V9WQI0kVhMDg990E?g7psBuql2qDdWjO1YtGkMbNt5k2NpueB@NM\"',
		'url': 'https://gaming.amazon.com/'
    },

	{
		'name': "unique_id", 
		'value': "f9c4124bfdc110fe",
		'url': 'https://gaming.amazon.com/'
	}
]



with sync_playwright() as driver:
    browser = driver.webkit.launch()
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://gaming.amazon.com/")
    
    context.add_cookies(own_session_cookies)
    
    html = BeautifulSoup(page.content(), 'html.parser').prettify()
    open('home.html', 'w').write(html)
    
    browser.close()