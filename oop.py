#oop object oriented programming

#class 데이터 정의 및 inheritance 

class Dog:

  def __init__(self,name,breed,age):
    self.name = name
    self.breed = breed
    self.age = age

  def sleep(self):
    print("zzzzzzzzz")


class GuardDog(Dog):

  def __init__ (self, name, breed):
    super().__init__(name, breed, 5)
  
  def rrrrr(self):
    print("stay away!")
  


class Puppy(Dog):

  def __init__ (self, name, breed):
    #super란 부모 class를 참조함 (Dog class 참조)
    super().__init__(name, breed, 10)
  def __str__(self):
    return f"Puppy name is {self.name} and breed is {self.breed}"

  def bark(self):
    print("Bark")
  

ruffus = Puppy(
  name = "Ruffus",
  breed = "Beagle"
)

guardDog = GuardDog(
  name = "GuardDog",
  breed = "Dalmatian"
)


ruffus.sleep()
guardDog.sleep()
