a=10

b=3.5

name="zambrano"

is_active=True


print(a,b,name)

print(type(a))

print(type(name))
print(type(is_active))


device="router"
id=101


print(f'Device:{device}and ID;(id)')

#ARIMETIC OPERATIONS

numbera=2
numberb=3

#result=numbera=numberb
#print()

print("The result is: ",numbera+numberb)
print("The result is:", numbera-numberb)
print("The result of power to any number is:", numbera**numberb)
print("The result is: ",numbera/numberb)
print("The result is: ",numbera//numberb)

# STRING
print("#STRING")
name="karen zambrano"
print(name.upper())
print(name.capitalize())
name2=name.upper()
print(name2.lower())

#lenguaj
language='PYTHON'
print(language[0])
print(language[-1])
print(len(language))

#list
print("#LIST")
devices=['router','swith','cable', 45, True, False]
print(len(devices))

print(device[0])
print(device[-1])

devices.append('Server')
print(devices)


names=list()
names.append('camil')
names.append('nicol')
names.append('juana')
names.append('Daniel')
print(names)
names[1]='sebastian'
print(names)
print(names.pop())
print(names)

numbers=list(range(10))
print(numbers)
selectdnumbers=numbers[2:4]
print(selectdnumbers)
print(numbers[:-1])
print(numbers[:3])

numbers[2:3]=[100,100]
print(numbers)


#TUPLES
print('#TUPLES')


containertuple=(10,20)


print(containertuple[0])
containerlist=list(containertuple)
print(type[containerlist])



#DICTIONARY
print('#tuples')


animals={'dog':'nice','cat':'pretty','monkey':'black'}
print(animals['cat'])

animals['cat']='ugly'
print(animals)

print('horse'in animals)



del animals['monkey']
print(animals)


animals['monkey']='ugly'
animals['mouse']='tiny'
animals['donkey']='big'

for item in animals:
    feature=animals[item]
    print("%item has %feature"%(item,feature))




print('ok!!!')