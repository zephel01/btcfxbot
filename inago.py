## -*- coding: utf-8 -*-
from selenium import webdriver
options = webdriver.ChromeOptions()
options.binary_location = '/Applications/Google Chrome Canary.app/Contents/MacOS/Google Chrome Canary'
options.add_argument('headless')
driver = webdriver.Chrome(chrome_options=options)

url = "https://inagoflyer.appspot.com/btcmac"

def main():

	driver.get(url)
	print("Connection successful.")
	
	#fetch and print BuyVol
	for buyvol in driver.find_elements_by_id("buyVolumePerMeasurementTime"):
		print("BuyVolume:"+buyvol.text)
	
	#fetch and print SellVol
	for sellvol in driver.find_elements_by_id("sellVolumePerMeasurementTime"):
		print("SellVolume:"+sellvol.text)
	
	driver.quit()

if __name__ == '__main__':
	main()
