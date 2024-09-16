from requests import get 

'''
data structure 

list, tuple, dictionary

:데이터를 구조화하기 위해 사용 
'''

#list 

days_of_week = ["Mon","Tue","Wed","Thur","Fri"]

# print(days_of_week)
# print(days_of_week[-1])

name = "Evan"

# name이라는 variable은 다양한 함수를 갖고 있다. 

print(name.upper())
print(name.startswith("e"))
print(name.endswith("n"))

#모든 string에 대해 사용할 수 있음

print("hello world".upper())

# days_of_week.clear()

# days_of_week.reverse()

# print(days_of_week.count("Wed"))


# tuple

days = ("Mon","Tue","Wed")

# tuple과 list 차이,, tuple은 변경할 수 없음 

'''
dictionary 

key : value

dictionary는 많은 속성을 갖고있는 데이터를 만들 때 사용 됨. 
'''

player = {
  'name' : 'evan',
  'age' : 21,
  'alive' : True,
  'fav_food' : ["🍕","🍔"],
}

# print(player)
print(player.get('fav_food'))

# add new key 

player['xp'] = 1500

player['fav_food'].append("🍜")

print(player)

# delete key

player.pop('age')


# for loop 

# pypi.org 에서 다양한 프로젝트 확인하기 

websites = (
  "google.com",
  "airbnb.com",
  "https://x.com",
  "facebook.com",
  "https://tiktok.com"
)
results = {}

for website in websites:
  if not website.startswith("https://"):
    website = f"https://{website}" 

  response = get(website)
  if response.status_code == 200:
    results[website] = "OK"
  else:
    results[website] = "FAILED"

print(results)