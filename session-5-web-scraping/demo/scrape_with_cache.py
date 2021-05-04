# Poll: How familiar are you with HTML
URL = 'https://www.mtgstocks.com/interests'
CHROMEDRIVER_PATH = '/usr/local/bin/chromeDriver'
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By

class Card:
	def __init__(self, list_from_site):
		self.name = list_from_site[0]
		self.release_set = list_from_site[1]
		self.new_price = list_from_site[2]
		self.old_price = list_from_site[3]
		self.change = list_from_site[4]

def getCache():
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

def fillCache():
	options = Options()
	options.add_argument('--headless')
	driver = webdriver.Chrome(CHROMEDRIVER_PATH, options=options)
	driver.implicitly_wait(15)
	driver.get(URL)
	tables = driver.find_elements(By.TAG_NAME, "table")
	print(driver.title)
	body = tables[0].find_element(By.TAG_NAME, "tbody")
	rows = body.find_elements(By.TAG_NAME, "tr")
	cards = [[col.text for col in row.find_elements(By.TAG_NAME, "td")] for row in rows]
	with open("cards.csv", "w") as f:
		f.write(str(time.time()) + "\n")
		for card in cards:
			f.write(",".join(card) + "\n")
	driver.quit()
	return [Card(card) for card in cards]

def lookForFavoriteCards(favoriteCards):
	rows = getCache()
	if len(rows) == 0:
		rows = fillCache()
	for card in rows:
		if card.name in favoriteCards:
			if card.change[0] == "+":
				print(f"Woah! {card.name} from {card.release_set} went up by {card.change}")
			else:
				print(f"Woah! {card.name} from {card.release_set} went down by {card.change}")

lookForFavoriteCards(["Reverse Damage", "Ripjaw Raptor", "Ashnod's Altar", "Scrap Mastery"])