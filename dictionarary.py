mydict = {
    "name": "John",
    "age": "36",
    "country": "norway",
    "sex": "male"
}
print(mydict)

print(type(mydict))
print(mydict["name"])


theage = mydict["age"]
thename = mydict.get("name")

print(theage)
print(thename)


myname = "victory"

if myname in mydict.values():
    print("yes,'victory'is one of the keys in the thisdict dictionary")
else:
    print("no,'victory'is one of the keys in the thisdict dictionary")
    newdidt = {
        "listofnamws": ["emeka","chioma","victory"],
        "listofscores":[90,80,70,60],
        "lstofcities":["lagos","abuja","portharcourt","calabar"],
        "country":"nigeria"
    }