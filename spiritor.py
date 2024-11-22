print("This program makes a spiritual name")
print("tomato  potato  spinach")
inp = input("Type one:")
storage = ""

if inp=="tomato":
    storage = storage + "j"
elif inp=="potato":
    storage = storage + "e"
elif inp=="spinach":
    storage = storage + "a"

print("apple  banana  mango")
inp = input("Type one:")
if inp == "apple":
    storage = storage + "b"
elif inp =="banana":
    storage = storage + "m"
elif inp =="mango":
    storage = storage + "u"

print("pen  pencil  eraser")
inp = input("type one:")
if inp =="pen":
    storage = storage + "g"
elif inp =="pencil":
    storage = storage + "h"
elif inp =="eraser":
    storage = storage+ "p"

print("logitech zebronics hewlett packard")    
inp = input("type one:")
if inp == ("logitech"):
    storage = storage+ "x"
elif inp == ("zebronics"):
    storage = storage + "f"
elif inp == ("hewlett packard"):
    storage = storage + "q"
print(storage   +""+ "this is your spiritual name")
