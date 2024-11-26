def main():
  var_list=[]
  var_dict={}
  var_tuple=[]
  var_input=(int(input("enter number 1/5: ")))
  if var_input == 1:
      for i in range(5):
          var_input=(int(input("Enter number ")))
          var_list.append(var_input)

      print(var_list)
  if var_input == 2:
      for i in range(5):
          var_input=(int(input("Enter number ")))
          var_dict[i]=var_input
      print(var_dict)
  
  if var_input == 3:
      for i in range(5):
          var_input=(int(input("Enter number ")))
          var_tuple.append(var_input)
      print(tuple(var_tuple))
      
  if var_input == 4:
      for i in range(5):
          var_input=(int(input("Enter number ")))
          var_tuple.append(var_input)
      print(set(var_tuple))
  
  
  
          

            
main()