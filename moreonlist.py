statelist = list (("abuja","kano","kaduna","jos","uyo","calabar","warri","asaba"))
anotherstaelist = (("enugu","lagos","abuja","kano","kaduna","jos","uyo","calabar","warri","asaba"))

newlist = []
for x in statelist:
    if x in anotherstaelist:
        newlist.append(x)

        print(newlist)

newlist.sort(key=str.upper)
print(newlist)
age = list((2,470,75,80,9,9,88,9,4,25,76))
s