from gooey import Gooey, GooeyParser 
@Gooey(program_name="Even/odd")

def main():
    
    parser=GooeyParser(description="practice1")
    parser.add_argument("name" , help="plz enter your name")
    parser.add_argument("family" , help="plz enter your family")
    parser.add_argument("number1", help="plz enter number 1")
    parser.add_argument("number2", help="plz enter number 2")
    parser.add_argument("operation", choices= ["add","sub","div","mull"] , help="plz enter oprations")
    
    args=parser.parse_args()
    var_name="paria"
    var_family="tavakoli"
    if var_name == args.name and var_family == args.family and 10 < (int(args.number1)) < 99 and 10 < (int(args.number1)) < 99:
        
        if args.operation == "add":
            var_add=(int(args.number1) + int(args.number2))
            print(var_add)
            
        if args.operation == "sub":
            var_sub=(int(args.number1) - int(args.number2))
            print(var_sub)
            
        if args.operation == "div":
            var_div=(int(args.number1) / int(args.number2))
            print(var_div)
            
        if args.operation == "mull":
            var_mull=(int(args.number1) * int(args.number2))
            print(var_mull)
    else:
        print("eroerr")
main()


