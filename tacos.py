#This script finds the unique listing of the top rated taco joints
#in Austin, TX (according to Yelp.com)

import requests
from bs4 import BeautifulSoup

baseurl = "https://www.yelp.com/search?find_desc=tacos&find_loc="
location = 'Austin, TX'
start_results = 0

url = baseurl + location + "&start=" + str(start_results)
taco_request = requests.get(url)

if not taco_request.status_code == 200:
  print("Uh oh - we didn't get a 200 OK from the URL")

taco_soup = BeautifulSoup(taco_request.text, 'html.parser')

taco_list = []
address_list = []

try:
	for tag in taco_soup.find_all("h3"):
		for link in tag.find_all("a"):
			for each in link:
				taco_list.append(link.text)
except:
	print("Couldn't find a name for the taco joint")
	taco_list.append("Unknown")

try:	
	for div in taco_soup.find_all("div"):
		for div2 in div.find_all("div"):
			for addy in div2.find_all("address"):
				if addy.text not in address_list:
					address_list.append(addy.text)
except:
	print("Couldn't find address")
	address_list.append("Unknown")

taco_tuple = []
list_length = 0

if ( len(taco_list) != len(address_list) ):
	print("There is not a matching number of addresses and taco joints - this list will be truncated")
        if ( len(taco_list) < len(address_list) ):
		list_length = len(taco_list)
	if ( len(taco_list) > len(address_list) ):
		list_length = len(address_list)        

counter = 0
while counter < list_length:
        taco_tuple.append( (taco_list[counter], address_list[counter]) )
	counter += 1

for each in taco_tuple:
	page_line = "%s, %s" % each
	print(page_line)
