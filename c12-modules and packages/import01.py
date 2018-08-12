import bs4
import requests

webpage = requests.get("http://www.iastate.edu/")
soup = bs4.BeautifulSoup(webpage.text, "html.parser")
print(soup.title.string)
