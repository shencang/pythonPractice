# 4.1 遍历整个列表

magicians = ['qq','aiai','cc','ee','adse','xxz','xcd']
for magician in magicians:
    print(magician)
    print("--------")
print("=======================")

# 4.1.2 在for循环中执行更多的操作

magicians = ['qq','aiai','cc','ee','adse','xxz','xcd']
for magician in magicians:
    print(magician.title()+", that was a great trick!")
    print("I can't wait to see your next trick ,"+magician.title()+'.\n')
    print("--------")
print("=======================")