from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

URL = 'https://www.mtgstocks.com/interests'
CHROMEDRIVER_PATH = './chromedriver'

class Card:
	def __init__(self, list_from_site):
		self.name = list_from_site[0]
		self.release_set = list_from_site[1]
		self.new_price = list_from_site[2]
		self.old_price = list_from_site[3]
		self.change = list_from_site[4]

def get_cards():
	options = Options()
	options.add_argument('--headless')
	with webdriver.Chrome(CHROMEDRIVER_PATH, options=options) as driver:
		driver.implicitly_wait(15)
		driver.get(URL)
		tables = driver.find_elements(By.TAG_NAME, "table")
		print(driver.title)
		# Find the rows in the body of the first table
		body = tables[0].find_element(By.TAG_NAME, "tbody")
		rows = body.find_elements(By.TAG_NAME, "tr")
		# Get a list of cards by parsing each row.
		cards = []
		for row in rows:
			cols = row.find_elements(By.TAG_NAME, "td")
			cards.append(Card([col.text for col in cols]))
	return cards

def look_for_favorite_cards(favorite_cards):
	rows = get_cards()
	for card in rows:
		if card.name in favorite_cards:
			if card.change[0] == "+":
				print(f"Woah! {card.name} from {card.release_set} went up by {card.change}")
			else:
				print(f"Woah! {card.name} from {card.release_set} went down by {card.change}")

look_for_favorite_cards(["Reverse Damage", "Ripjaw Raptor", "Ashnod\'s Altar", "Scrap Mastery"])
