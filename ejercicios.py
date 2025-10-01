#while True:

#userDefault='admin'
#passwordDefault=1234

#user=input('enter the user of the account.\n')
#password=input('enter the password of the account \n')

#if user==userDefault and passwordDefault
#print ('You are allowed to come to the system')

#else:
    #print('you are not user of the system...') 


#repository=list()

#ramdonNumber=int(input('Enter a number please'))
#sum=0

#for i in range(ramdonNumber):
    #repository.append(i)

#for i in repository:
   #sum=sum+i

    #repository = repository+i

#rint(f'the total sun is {sum}')
# Cajero automático mejorado

balance = 1000  # saldo inicial

while True:
    print("\n" + "="*30)
    print("     💳 CAJERO AUTOMÁTICO 💳     ")
    print("="*30)
    print("1 > Depositar")
    print("2 > Retirar")
    print("3 > Consultar saldo")
    print("4 > Salir")
    print("-"*30)

    choice = input("👉 Elige una opción: ")

    if choice == "1":
        print("\n--- DEPÓSITO ---")
        money = int(input("Ingresa la cantidad a depositar: $"))
        if money > 0:
            balance += money
            print(f"✅ Depósito exitoso. Nuevo saldo: ${balance}")
        else:
            print("❌ Cantidad inválida.")

    elif choice == "2":
        print("\n--- RETIRO ---")
        money = int(input("Ingresa la cantidad a retirar: $"))
        if money > 0 and balance >= money:
            balance -= money
            print("💵 Retiro exitoso. Retira tu dinero, por favor.")
            print(f"Tu nuevo saldo es: ${balance}")
        else:
            print("❌ Fondos insuficientes o cantidad inválida.")

    elif choice == "3":
        print("\n--- CONSULTA DE SALDO ---")
        print(f"📌 Tu saldo actual es: ${balance}")

    elif choice == "4":
        print("\n👋 Gracias por usar el cajero. ¡Adiós!")
        print("="*30)
        break

    else:
        print("\n⚠️ Opción inválida, intenta de nuevo.")


#class Students():
#    def __init__(self,name,course='AI'):
#        print('the student has been registered.....')
#        self.name=name
#        self.course=course
#    def datastudent(self):
#        print(f'Name: {self.name} and Course {self.course}')
#        return


#student1=Students('Daniela')
#student2=Students('juana','Distributed system')


#student1.datastudent()
#student2.datastudent()



 
#class Students():
#    def __init__(self,name,course='AI'):
#        print('the student has been registered.....')
#        self.name=name
#        self.course=course

#    def datastudent(self,status='No active'):
#        print(f'Name: {self.name} and Course {self.course}')
#       return


#student1=Students('Daniela')
#student2=Students('juana','Distributed system')

#student1.datastudent()
#student2.datastudent()



