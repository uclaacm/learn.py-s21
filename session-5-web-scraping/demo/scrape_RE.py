import requests

def lookForFavoriteCards(favoriteCards):
	res = requests.get("https://api.mtgstocks.com/interests/average")
	json = None
	try:
		json = res.json()
	except:
		print("Not a json")
		return
	cards = json["average"]["normal"]
	cards = filter(lambda card: card["print"]["include_default"] and card["interest_type"] == "day", cards)
	for card in cards:
		if card["print"]["name"] in favoriteCards:
			if card["percentage"] > 0:
				print(f"Woah! {card['print']['name']} increased by {card['percentage']}%")
			else:
				print(f"Drat! {card['print']['name']} decreased by {abs(card['percentage'])}%")

lookForFavoriteCards(["Primal Amulet", "Ashnod's Altar", "Scrap Mastery"])