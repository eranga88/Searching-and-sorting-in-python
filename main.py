def get_age(i):
    while True:
        try:
            age = int(input("Please Enter Age of Person : " + str(i) + " : "))
            if age < 0:
                raise ValueError
            if age == 0:
                raise ValueError
            break

        except ValueError :
            print("Please Enter Valid Age !!!")
            continue
    return age

def input_validator():
    while True:
        try:
            selection = int(input("Enter 0 to Exit  or 1 to Continue Search : "))

            if selection < 0:
                raise ValueError
            if selection > 1:
                raise ValueError
            break

        except ValueError :
            print("Please Enter Valid Number !!!")
            continue
    return selection

def check_name(list,i):
    while True:
        name = input("Please Enter Name of Person " + str(i) + " : ")

        if name in list:
            print(name + " exists in the system !!")
            continue
        if name == "":
            print("Please Enter Valid name !!!")
            continue
        break
    return name

def search(list,name):
    if name in list:
        print("Name : "+name)
        print("Age : "+str(list[name]))
    else:
        print("Person not found !!!")

def sort_by_key(list):
    list = list.items()
    print("Sorted by key: ", sorted(list, key=lambda x: x[0]))

def sort_by_value(list):
    list = list.items()
    print("Sorted by value: ", sorted(list, key=lambda x: x[1]))

i = 1
person = {}
while True:
    name= check_name(person,i)
    age = get_age(i)
    person[name] = age

    i = i+1
    if i==11:
        break

print("Original Dictionary : "+ str(person))
sort_by_key(person)
sort_by_value(person)

n = 1

while n:
    print()
    name = input("Enter Name of the Person to Search : ")
    search(person, name)
    print()

    if input_validator() == 0:
        break
    else:
        continue
