# #Pagination

import requests
from bs4 import BeautifulSoup

# all_jobs = []



# def scrape_page(url):
#   print(f"Scrapping {url}...")
#   response = requests.get(url)
#   soup = BeautifulSoup(response.content, "html.parser",)

#   jobs = soup.find("section", class_="jobs").find_all("li")[1:-1]

#   for job in jobs:
#     title = job.find("span", class_="title").text

#     company, position, region = job.find_all("span", class_="company")
#     company = company.text
#     position = position.text
#     region = region.text
#     url = job.find("div", class_="tooltip--flag-logo").next_sibling["href"]
#     job_data = {
#      "title":title,
#      "company": company,
#      "position" : position,
#      "region" : region,
#      "url" : f"https://weworkremotely.com{url}"
#     }
#     all_jobs.append(job_data)
  
# def get_pages(url):
#   response = requests.get("https://weworkremotely.com/remote-full-time-jobs")

#   soup = BeautifulSoup(response.content,"html.parser")

#   return len(soup.find("div",class_="pagination").find_all("span",class_="page"))


# total_pages = get_pages("https://weworkremotely.com/remote-full-time-jobs?page=1")


# for x in range(total_pages):
#   url = f"https://weworkremotely.com/remote-full-time-jobs?page={x+1}"
#   scrape_page(url)

# print(len(all_jobs))


# 6.6 code challenge 부터 --> 시작 

jobs = ["flutter","ios","python"]

headers = {
  "User-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
}


def scrape_page(url,headers):
  all_jobs = []
  print(f"scraping from {url}...")
  response = requests.get(url,headers=headers)
  soup = BeautifulSoup(response.content, "html.parser")
  jobs = soup.find("table",id="jobsboard").find_all("td",class_="company position company_and_position")[1:-1]

  for job in jobs:
    title = job.find("h2",itemprop="title").text[2:-2]
    company = job.find("span",itemprop="hiringOrganization").find("h3", itemprop="name").text[2:-2]
    location = job.find("div",class_="location").text
    salary = job.find("div",class_="location").next_sibling.text
    
    all_jobs.append(title)
    all_jobs.append(company)
    all_jobs.append(location)
    all_jobs.append(salary)

  return all_jobs

# 각 직업에 대한 request 요청
for job in jobs:
  url = f"https://remoteok.com/remote-{job}-jobs"
  print(f"jobs about {job}...")
  print(scrape_page(url,headers))
  
  