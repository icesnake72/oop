

# map() 함수

li = [1,2,3,4,5]

add = lambda x : x * 10

#map(add, li)
#print(li)

# li2 = map(add, li)

li2 = list(map(add, li))
print(li2)


# filter() 함수
li = [1,2,3,4,5,6,7,8,9,10]

even = lambda x : x % 2 == 0

#filter(even, li)
#print(li)

# li2 = filter(even, li)

li2 = list(filter(even, li))
print(li2)


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    
  def __str__(self):
    return f"이름 : {self.name}/나이 : {self.age}"
  
  def __repr__(self):
    return f"이름 : {self.name}/나이 : {self.age}"
  
  # def __lt__(self, other):
  #   return self.age < other.age
  
  # def __eq__(self, other):
  #   return self.age == other.age
  
  # def __le__(self, other):
  #   return self.age <= other.age
  
  # def __gt__(self, other):
  #   return self.age > other.age
  
  # def __ge__(self, other):
  #   return self.age >= other.age
  
  # def __ne__(self, other):
  #   return self.age != other.age
  
  def __add__(self, other):
    return self.age + other.age
  
  def __sub__(self, other):
    return self.age - other.age
  
  
  
p1 = Person("홍길동", 30)
p2 = Person("이순신", 20)
p3 = Person("강감찬", 40)
p4 = Person("김유신", 70)
p5 = Person("유관순", 10)

li = [p1, p2, p3, p4, p5]
print(li)

li.sort()
print(li)