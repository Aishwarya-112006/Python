dict={"key":"name",
      "name":"sid",
      "rollno":"3",
      "list":[1,4,9]}
print(dict,type(dict))
print(dict["key"])
#DICTIONARY FUNCTIONS
print(dict.items())#items fun
print(dict.keys())#keys fun
print(dict.update({"name":"adi"}))#update fun
print(dict.update({"state":"Up"}))
print(dict.get("name"))#get fun
print(dict.get("state"))