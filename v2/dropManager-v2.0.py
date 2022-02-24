from playwright.sync_api import sync_playwright
import json



isClaimed = bool()
# page and session (context) initiation 
print('Initializing...', end='    ')
playwright = sync_playwright().start() 
browser = playwright.webkit.launch()
context = browser.new_context()
page = context.new_page()

# cookie adding management
page.goto("https://gaming.amazon.com/")
context.add_cookies(json.load(open('cookies.json', 'r')))
page.goto("https://gaming.amazon.com/home")
print('Done.\n')

##
##
## is it claimed?
##
print('Searching for drop...', end='    ')
locator = page.locator(

	"a[aria-label='League of Legends: Prime Gaming Capsule'] >> nth=1"
	).locator(
		
		"p[class='redeem__claimed-text tw-font-size-6']"
	).text_content()

if locator == 'Claimed':
	isClaimed = True
	print('Drop already claimed.')
else:
	isClaimed = False

##
##
## drop reclaim
##
if not isClaimed:
    
    print('Claiming...')
    page.goto('https://gaming.amazon.com/loot/lol10')#https://gaming.amazon.com/loot/wildrift
    
    page.click(
        'button[class="tw-interactive tw-border-radius-none tw-button tw-button--full-height tw-button--full-width tw-button--prime"][data-test-selector="AvailableButton"][data-a-target="AvailableButton"]'
    )

    print(' Reclaim successfully done.')
#print(f'it is {isClaimed}')


# html = BeautifulSoup(page.content(), 'html.parser').prettify()
# open('home.html', 'w').write(html)

browser.close()
playwright.stop()