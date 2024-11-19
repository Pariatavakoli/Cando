from gooey import Gooey,GooeyParser
from random import randint
@Gooey(program_name="متن هدر اصلی")
def main():
   
    parser= GooeyParser(description="متن هدر")
    parser.add_argument("number",help="enter a number: ")
    args=parser.parse_args()
    print(args.number)
    var2=randint(1,3) 
    if number == var2:
        print("ok")
    else:
        print("not good")
  
main()




