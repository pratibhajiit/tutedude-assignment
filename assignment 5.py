dict={'ram':25,'mohan':78,'Alice':85}


a=input("enter the student name : ")
if a=="ram":
    print("ram marks is=",(dict.get('ram')))


elif a == "mohan":
    print("mohan marks is",(dict.get('mohan')))
elif a=="Alice":
    print("Alice marks is=",(dict.get('Alice')))

else:
    print(dict.get('moh',"student not found"))
