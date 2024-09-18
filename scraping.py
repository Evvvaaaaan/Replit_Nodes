import requests
from bs4 import BeautifulSoup

# 사이트의 html을 가져오기 위해 url을 입력함 
url = "https://weworkremotely.com/categories/remote-full-stack-programming-jobs"

# request 패키지를 사용하여 url에 get요청을 보냄
response = requests.get(url)

#html.parser를 사용해서 soup에 넣음
soup = BeautifulSoup(response.content, "html.parser",)

#section, class="jobs" 모든 li들을 찾아서 jobs에 저장
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

