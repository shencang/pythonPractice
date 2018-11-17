cars = ['bmw','audi','toyota','subaru','dazhong','hongqi','qq','tosala','auto','sasx']

for car in cars:
    if car == 'qq':
        print(car.upper())
        print("=========")
    else:
        print(car.title())
        print("---------")

print(cars[1]=='audi')
print(cars[1]=='Audi')

print(cars[1]=='audi'and cars[0] =='bmw')
print(cars[1]=='audi'or  cars[0] =='bmsw')
print('qq'in cars)

# if elif else 结构
age = 12
if age<4:
    print("isvery lattle")
elif age<18:
    print("you can")
else:
    print("emmmmm")
