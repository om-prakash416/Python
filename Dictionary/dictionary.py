
thisdict= {
    "brand":"ford",
    "model":"mustang",
    "year":1957,
    # "year":1945 #overwrite value
    "colors":["red","white","blue"]
}
print(thisdict)
print(len(thisdict))
print(type(thisdict))
x = thisdict["model"]
print(x)
y = thisdict.get("model")
print(y)

z = thisdict.keys()
print(z)

a = thisdict.values()
print(a)

b = thisdict.items()
print(b)

thisdict["year"] = 2008
print(thisdict)

thisdict.update({"year":2020})
print(thisdict)

thisdict["fruit"] = "mango"
print(thisdict)
print("*********")
thisdict.pop("model")
print(thisdict)



print("*******")

myfamily = {
    "child1":{
        "name":"vikash",
        "age":16
    },
    "child2":{
        "name":"om",
        "age":50
    }
}

print(myfamily)