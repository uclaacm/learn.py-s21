# Poll: How familiar are you with HTML

URL = 'https://www.mtgstocks.com/interests'
CHROMEDRIVER_PATH = '/usr/local/bin/chromeDriver'
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class Card:
	def __init__(self, list_from_site):
		self.name = list_from_site[0]
		self.release_set = list_from_site[1]
		self.new_price = list_from_site[2]
		self.old_price = list_from_site[3]
		self.change = list_from_site[4]

def getCards():
	options = Options()
	options.add_argument('--headless')
	driver = webdriver.Chrome(CHROMEDRIVER_PATH, options=options)
	driver.implicitly_wait(15)
	driver.get(URL)
	tables = driver.find_elements_by_tag_name("table")
	print(driver.title)
	# Find the rows in the body of the first table
	rows = tables[0].find_element_by_tag_name("tbody").find_elements_by_tag_name("tr")
	# Get a list of cards by parsing each row.
	cards = [Card([col.text for col in row.find_elements_by_tag_name("td")]) for row in rows]
	driver.quit()
	return cards

def lookForFavoriteCards(favoriteCards):
	rows = getCards()
	for card in rows:
		if card.name in favoriteCards:
			if card.change[0] == "+":
				print(f"Woah! {card.name} from {card.release_set} went up by {card.change}")
			else:
				print(f"Woah! {card.name} from {card.release_set} went down by {card.change}")

lookForFavoriteCards(["Reverse Damage", "Ripjaw Raptor", "Ashnod's Altar", "Scrap Mastery"])