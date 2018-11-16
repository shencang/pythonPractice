# 列表的创建和添加
bicycles = ['trek','cannondale','redline','specialized','happy']
print(bicycles)

print(bicycles[2].title())
print(bicycles[-1].title())

print("= = ceshi:"+bicycles[-1].title()+".")

# 用-1直接指向末尾元素
bicycles[-1]="love"
print("= = ceshi:"+bicycles[-1].title()+".")

bicycles.append('ductai')
print("= = ceshi:"+bicycles[-1].title()+".")

# append向列表添加元素
app= []
app.append('dd')
app.append('cv')
app.append('bb')
app.append('ca')


# 向指定位置插入元素
app.insert(1,'hello')
app.insert(3,'float')
print(app)


# 列表的删除操作。

# 直接删除指定位置的元素
del app[1]
print(app)


# 移除指定位置的元素，放入临时变量
poped_app = app.pop()
print(poped_app)
print(app)

motorcycles =['honda','yamaha','suzuki']
last_owned = motorcycles.pop()
print(motorcycles)
print('The last motocycle I owned was a ' +last_owned.title()+'.')

# pop的指定位置的使用方法
last_owned = motorcycles.pop(1)
print(motorcycles)
print('The last motocycle I owned was a ' +last_owned.title()+'.')


# 移除指定内容的remove
motorcycles =['honda','yamaha','suzuki','fdd']
print(motorcycles)
motorcycles.remove('fdd')
print(motorcycles)


# 用变量承载的方法，remove只能去除同样内容的第一个
motorcycles =['fdd','honda','yamaha','suzuki','fdd']
mds = 'fdd'
print(motorcycles)
motorcycles.remove(mds)
print(motorcycles)
print('\nA '+mds+' was died')


