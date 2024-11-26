from colorama import init,Fore, Back, Style
def main():
    var_list=[]
    var_number1=int(input("plz enter number 6/10 "))
    var_number2=int(input("plz enter number 6/10 "))
    if  6 < var_number1 <10 and  6 < var_number1 <10:
        for i in range(1,var_number1+1):
            if i == 2:
                continue
            for j in range(1,var_number2+1):
                if j == 2:
                    continue
                if  j==4:
                    print(Fore.RED + str(i*j)  ,  end=" " +Style.RESET_ALL)
    
                print(Fore.YELLOW +str(i*j ), end=" ")
                var_list.append(i*j)
            print()      
        print(var_list)
        return var_list    

var_main=main()
def main2(var_list2):
   var_listg=[]
   for g in range(len(var_main)):
       if g % 2 ==0:
           var_listg.append(g)
   print(var_listg)
           
  
        
main2(var_main)
        



