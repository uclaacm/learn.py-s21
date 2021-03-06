from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By

URL = 'https://www.mtgstocks.com/interests'
CHROMEDRIVER_PATH = '/usr/local/bin/chromeDriver'

class Card:
	def __init__(self, list_from_site):
		self.name = list_from_site[0]
		self.release_set = list_from_site[1]
		self.new_price = list_from_site[2]
		self.old_price = list_from_site[3]
		self.change = list_from_site[4]

def get_cache():
	cards = []
	current_time = time.time()
	try:
		with open("cards.csv", "r") as f:
			first_line = f.readline()
			if first_line == "":
				return []
			update_time = float(first_line)
			if current_time - update_time > 24 * 60 * 60:
				print("The cache is over a day old! We better check again!")
				return []
			print("Reading cards from Cache!")
			for line in f:
				line = line.rstrip()
				cards.append(Card(line.split(",")))
		return cards
	except IOError:
		return []

def fill_cache():
	options = Options()
	options.add_argument('--headless')
	with webdriver.Chrome(CHROMEDRIVER_PATH, options=options) as driver:
		driver.implicitly_wait(15)
		driver.get(URL)
		tables = driver.find_elements(By.TAG_NAME, "table")
		print(driver.title)
		body = tables[0].find_element(By.TAG_NAME, "tbody")
		rows = body.find_elements(By.TAG_NAME, "tr")
		cards = []
		for row in rows:
			cols = row.find_elements(By.TAG_NAME, "td")
			cards.append([col.text for col in cols])
		with open("cards.csv", "w") as f:
			f.write(str(time.time()) + "\n")
			for card in cards:
				f.write(",".join(card) + "\n")
	return [Card(card) for card in cards]

def look_for_favorite_cards(favoriteCards):
	rows = get_cache()
	if len(rows) == 0:
		rows = fill_cache()
	for card in rows:
		if card.name in favoriteCards:
			if card.change[0] == "+":
				print(f"Woah! {card.name} from {card.release_set} went up by {card.change}")
			else:
				print(f"Woah! {card.name} from {card.release_set} went down by {card.change}")

look_for_favorite_cards(["Reverse Damage", "Ripjaw Raptor", "Ashnod's Altar", "Scrap Mastery"])