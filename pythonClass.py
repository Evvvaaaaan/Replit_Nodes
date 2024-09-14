# Class의 정의 
from collections import namedtuple


class ClassName:
  names = 'evan'
  

  def __init__(self, name):
    self.name = "python"
    self.tricks = []

  def add_trick(self, trick):
    self.tricks.append(trick)

d = ClassName('evvvaaaaan')
e = ClassName('Junsun')
print(d.names) # evan ,, shared  by all ClassName
print(d.name) # python,, shared by unique to d


#상속 

class Country: 
  """super class"""

  name = "Korea"
  population = 51000000
  capital = "Seoul"

  def show(self):
   print("method class")


class Korea(Country):
  """sub class"""
  def __init__(self,name):
    self.name = name
  def show_name(self):
    print("country name : ", self.name)


a = Korea("Japan")
a.show()
a.show_name()