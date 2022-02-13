from bs4 import BeautifulSoup
import requests

####################poe teus cookie agui do jeito q ta organizado
own_session_cookies = {

	"at-main": "Atza|IwEBIItHD15BtP9u-4eT5Gc435Fu744FrproZstGRUf64AyjOywhU3qj2RRvY1sCKEffgh5WfgPgRcZh2fEJ5cFw0uTT1qsm36dH44A-T-OXk4W4b-oXJV381BmzH0nL_pxbg4ghGNlowA0vhwyFjwoz85c4D-SkN5JOkBfoCJNx8NfrVj8A2p99bH12UKXQh4rVuGZ9vogiKCr9sDI2Vu2FOrpcw3Aa9S9Q2F3CNCwFeqAxbaUhZ6awMYnTOv9z9zk9G9xEaTgD-ApUTuA",
	"aws-target-visitor-id": "16447334845385687-174230",
    "sess-at-main": "\"oliYQVINONqaasdfgeTyI4q1KQn1Sd4+C2E497tYfXZ6FhaNMQ=\"",
    "session-id": "146-9642371765-404282181",
    "session-id-time": "20827487201l",
    "session-token": "3DbAoEebS/X/X7ceY6DnQYSZZ4hWAodfgajAtzEZKHXxZyyv7R1eGiKWuA9qy3tqAB64Hs6EWU9IIZQOS6yNkbB/wdjjG0uW3bOivtoomuvwodGfzcWWOH41dslO70H+89Ebed89wSkPgVx0CvHVO20gMb+Avp1nAY8z8uZ/YdxHpeFr2ABltBvF5hc/dZZjIpJjQcCl1gizC1M+2nTSaANqC0iqQ==",
	"sst-main": "Sst1|PQFu8eGtN4efGhAhyuuQ9y2aCadfgaRkc67RcfjWPA640lIiQm75rwgusvFmYIOMfj15rn4Xh64OHEgIbSGACa1xIXY6c09uytvGOUDzUq4w7zEMA-Z98-zoJHgzQSp41zAd6g1LV09ze17Tis48pa5TAEaH6i4lNdplKmHWX202qS29FwJEVKFHMz0Gxo_QPvRaCoMGu3burlBEidzfFJpEN8UPyuRRhqelYMAfbUIOhcJ_CHepWW_0fNqEbI1CgaVbpHU1Wo-3lubQRCMUbD96bSTzVmyx5FPPkLTedeRS61nf6eUcw",
    "ubid-main":"130-4236462-2adfg2965160",
    "x-main": '\"DNQYcU0YC83a7V9WQI0kVhMDg990E?g7psBuql2qadfgDd4jO1YtGkMbNt45k2NpueB@NM\"',
	"unique_id": "f9ac4124bfdc1adfg10fe"
}



def verifier():	
	website_request = requests.Session()

	website_home_html = website_request.request(

		'get',
		'https://gaming.amazon.com/home',
		cookies=own_session_cookies

	)

	return website_home_html.text

open('home.html', 'w').write(verifier())
