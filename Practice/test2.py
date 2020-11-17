def getInfo():
    var1 = input("please provide the first numeric value: ")
    var2 = input("please provide the second numeric value: ")
    return var1,var2
    
def compute():
    go = True
    while go:
        var1,var2 = getInfo()
        try:
            var3 = int(var1) + int(var2)
            go = False
        except ValueError:
            print("You didn't provide a numeric value")
        except:
            print("Opps something happened....program will close now")
    print("{}+{}={}".format(var1,var2,var3))

if __name__ == "__main__":
    compute()
