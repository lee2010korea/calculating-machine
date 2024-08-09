import sys
print ("숫자");
x = float(input("--->"));
print ("기호");
z = (input("--->"));
print ("숫자");
y = float(input("--->"));
if z == "+":
        print (x+y)
        x = float(x+y)
else:
        if z == "-":
            print (x-y)
            x = float(x-y)
        else:
            if z == "*":
                print (x*y)
                x = (x*y)
            else:
                if z == "/":
                    print (x/y)
                    x = float(x/y)                                                    
while True:      
    print (x)
    print ("기호");
    z = (input("--->"));
    if z == "end":
            break
    else:
        if z == "+":
                print ("숫자")
                y = float(input("--->"))
                print (x+y)
                x = float(x+y)
        else:
            if z == "-":
                      print ("숫자")
                      y = float(input("--->"))
                      print (x-y)
                      x = float(x-y)
            else:
                if z == "*":
                           print ("숫자")
                           y = float(input("--->"))
                           print (x*y)
                           x = float(x*y)
                else:
                           if z == "/":
                                print ("숫자")
                                y = float(input("--->"))
                                print (x/y)
                                x = float(x/y)
                           else:
                                 if z == "re":
                                       print ("숫자")
                                       x = float(input("--->"))
                                 else:
                                       if z == "RE":
                                             print ("숫자")
                                             x = float(input("--->"))
                                       else:
                                             if z == "END":
                                                   break

                                       

                      