import requests
from bs4 import BeautifulSoup

url = "https://weworkremotely.com/categories/remote-full-stack-programming-jobs"

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser",)

jobs = soup.find("section", class_="jobs").find_all("li")[1:-1]

for job in jobs:
  title = job.find("span", class_="title").text
 
  company, position, region = job.find_all("span", class_="company")
  company = company.text
  position = position.text
  region = region.text
  print(title, company,position, region)
'''
letters = ["a","b","c"]
a,b,c = letters -> 각 변수에 a b c 들어감
'''



#Pagination

