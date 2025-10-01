mydictionary =  dict()
mydictionary ['humans']=2
mydictionary ['mouse']=4
mydictionary ['spider']=8


for animal in mydictionary:
    data=mydictionary[animal]
    print('the %s has %d'%(animal,data)) 


    #LOOPS
    counter=0
    while counter<10:
        print(counter)
       #counter=counter+1
        counter+=1
         #name=imput ('Enter your name:\n')
         #print(f'Hello,{name}')

mylist=list()
for i in range (10):
    if i %2==0:
       mylist.append(i)
print (mylist)

print('*********')
mylist= [i for i in range (10) if i %2==0]
print(mylist)
print('ok..!!')


print('*********')
mylist= [i*i for i in range (100)]
print(mylist)
print('ok..!!')

def greetings():
  return f'hello my friend.....'

tmp=greetings()
print(tmp)

def greetings2(name='friend'):
    print(f'Hello,{name}')
    return

    #greeting 
greetings2()
while True:

    num1 = int(input("Ingresa el primer número: "))
    num2 = int(input("Ingresa el segundo número: "))

    operation=imput('pon numeros del 1 a 4. \n 1 suma \n  2 multiplicacion \n  3 division')
    if operation==1:
        result=num1+num2
    elif operation==2:
        print(f"Resultado: {num1 * num2}")
    elif operation ==3:
        if num2 != 0:
            print(f"Resultado: {num1 / num2}")
        else:
            print("Error: No se puede dividir entre 0.")
    else:
        print("Opción inválida, intenta de nuevo.")


   