from infi.systray import SysTrayIcon
import requests
import sys


def update(systray):
	global old,currency
	headers = {
		'Content-Type' : 'application/json',
	}
	r = requests.get("https://api.coinbase.com/v2/prices/spot?currency="+currency)
	new = float(r.json()['data']['amount'])
	upDown = ""
	if old!=0:
		if old<new:
			upDown = "UP"
		elif old>new:
			upDown = "DOWN"
	old = new
	text = r.json()['data']['amount']
	if currency == 'EUR':
		text = text[:len(text)-4]
	systray.update(hover_text = r.json()['data']['amount']+' '+currency + '|'+upDown)


if len(sys.argv)<2:
	currency = 'EUR'
else:
	currency = sys.argv[1]
old = 0 
menu_options = (("Update value", None, update),)
systray = SysTrayIcon("icon.ico", "Bitcoin Tracker", menu_options)
systray.start()