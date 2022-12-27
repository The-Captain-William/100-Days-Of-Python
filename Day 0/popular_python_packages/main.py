import requests
import config  # import other .py file; api_key becomes a method of config

url = "https://api.yelp.com/v3/businesses/search"  # search through this page
headers = {
    "Authorization": "Bearer " + config.api_key  # is dictionary with Key:base pair + my key; "The bearer is_____"
}
params = {   # search parameters; contained in dictionary object
    "term": "Barber",
    "location": "NYC"
}
response = requests.get(url, headers=headers, params=params)  # get url, get auth, get key; search for barbers in NYC
businesses = response.json()["businesses"]  # capture response in json file; named businesses
names = [business["name"]
         for business in businesses if business["rating"] > 4.5]  # implicit definition of business, collecting and filtering
print(names)


  # what is the utility of all of this?
  # how can we save information?
