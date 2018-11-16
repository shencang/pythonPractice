bicycles = ['trek','cannondale','redline','specialized','happy']
print(bicycles)

print(bicycles[2].title())
print(bicycles[-1].title())

print("= = ceshi:"+bicycles[-1].title()+".")

bicycles[-1]="love"
print("= = ceshi:"+bicycles[-1].title()+".")

bicycles.append('ductai')
print("= = ceshi:"+bicycles[-1].title()+".")

app= []
app.append('dd')
app.append('cv')
app.append('bb')
app.append('ca')

app.insert(1,'hello')
app.insert(3,'float')
print(app)

del app[1]
print(app)


poped_app = app.pop()
print(poped_app)
print(app)

motorcycles =['honda','yamaha','suzuki']
last_owned = motorcycles.pop()
print(motorcycles)
print('The last motocycle I owned was a ' +last_owned.title()+'.')


last_owned = motorcycles.pop(1)
print(motorcycles)
print('The last motocycle I owned was a ' +last_owned.title()+'.')

motorcycles =['honda','yamaha','suzuki','fdd']
print(motorcycles)
motorcycles.remove('fdd')
print(motorcycles)


