

mySentence = "loves the color"

color_list = ["blue","red","green","black","violet"]

def color_function(name) :
    lst = []
    for i in color_list:
        msg = "{} {} {}.".format(name, mySentence, i)
        lst.append(msg)
    return lst

#lst = color_function("Forest")
#for i in lst:
#    print(i)

def get_name():
    go = True
    while go:
        name = input("What is your name? ")
        if name == "":
            print("Please provide your name:")
        else:
            go = False
    lst = color_function(name)
    for i in lst:
        print(i)

get_name()
        
mth = lambda num: num + num

print(mth(5))
