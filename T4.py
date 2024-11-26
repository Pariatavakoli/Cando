from random import randint
def main():
    var_random=randint(0,10)
    print(var_random)
    while True:
         var_input=(int(input("please Enter a nmber 1/10: ")))
         if var_random == var_input:
            print("thats geat")
            break
            
    
main()
    

