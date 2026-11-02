# question1
name=input("enter your name")
age=int(input("enter your age"))
height=int(input("enter your height"))
print(f"your name is {name} you are {age} year's old and your height is {height}")

# question2
number1=int(input("enter a number"))
number2=int(input("enter another number"))
sum=number1+number2
print(sum)

# question3
number=int(input("enter a number"))
if number%2==0:
    print(f"{number} even")
else:
    print(f"{number} odd")

# question4
user_name="admin"
password="1234"
while True:
    user_name1=input("enter your username")
    user_password=(input("enter the password"))
    if user_name1==user_name and user_password==password:
        print("your credentials are valid you have sucessfully logged in")
        break
    else:
        print("your credentials are invalid try again")

# question5
for i in range(10,0,-1):
    print(i)
    if i==5:
        continue

# question6
foods=["pizza","burger","pizza","sushi"]
unique_food=[]
for food in foods:
    if food not in unique_food:
        unique_food.append(food)
print(unique_food)

#question7
numbers=[1,2,3,4,5]
squared_number=[]
for n in numbers:
    squared_number.append(n**2)
print(squared_number)

#question8
students={"name":"alex","age":20,"grade":"A"}
students.update({"grade":"A+"})
students.update({"city":"newyork"})
print(students)

#question9
capitals={"india":"delhi","USA":"washington","japan":"tokyo"}
user_country=input("enter a country name ")
if user_country in capitals:
    print(capitals.get(user_name))
else:
    print("not found")

#question10
animals={"wild animal":"tiger","pet animal":"cat","venomous animal":"inland taipan"}
print(animals.keys())
print(animals.values())
print(animals.items())

#question11
sentence=input("enter any sentence you like")
s=sentence.split()
sd={}
for word in s:
    if word not in sd:
        sd[word]=1
    else:
        sd[word]=sd[word]+1
print(sd)



        
