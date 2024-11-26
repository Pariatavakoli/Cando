from random import randint
from  colorama import init,Fore,Back,Style
def main():
 var_user=(input(" pleas Enter user: "))
 var_password=(input(" pleas Enter password: "))
 var_user2=(input(" pleas Enter user: "))
 var_password2=(input(" pleas Enter password: "))

 if var_password.isdigit() and var_password2.isdigit():
    print("ok")
    user1_conter=0
    user2_conter=0
    for i in range (5):
         var_random=randint(1,10)
         print(var_random)
         var_input1=int(input("enter number for user 1: "))
         var_input2=int(input("enter number for user 2: "))
         if var_input1==var_random and var_input2==var_random:
            user1_conter+=1
            user2_conter+=1
            
         elif var_input1==var_random and var_input2!=var_random:
            user1_conter+=1
            
         elif var_input1==var_random and var_input2!=var_random:
            user1_conter+=1   
         else:
             continue             
             
    print(user1_conter) 
    print(user2_conter)    
    if user1_conter > user2_conter:
        print(Fore.BLUE +"user1  winner")
    elif user1_conter < user2_conter:
        print(Fore.RED +"user2  winner")
    else:
        print("equal")
    
 else:
    print("Eror")
    exit()
    
main()

