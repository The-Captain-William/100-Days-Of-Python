import requests
from bs4 import BeautifulSoup

response = requests.get("https://stackoverflow.com/questions")  # response contained in requests.get("webpage")
soup = BeautifulSoup(response.text, "html.parser")  #apply bs4 to response text; incoming info from html

questions = soup.select(".question-summary")  #css selector ->find element html doc
print(questions)  # css selector is wrong, generating empty list