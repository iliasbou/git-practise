class emptyfile(Exception):
    pass

try:
    filename = (input("Type files name :"))
except :
    print("Invalid input of username")
    filename = (input("Type your filename :"))
try:
  with open(filename,"r") as f:
      lines = f.readlines()
      linescount = len(lines)

      if linescount == 0:
          
          raise file emptyfile 
        
except: 
    print("")
