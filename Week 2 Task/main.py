print("Well Come to our Group! ")
mydict = {
    'sena': {'Name': "Sena Mekonin", 'Age': 22, 'Gender': "Male", 'Dept': "Electromechanical", 'Year': "Third"},
    'moti': {'Name': "Motumaa Kidanu", 'Age': 22, 'Gender': "Male", 'Dept': "Electromechanical", 'Year': "Third"},
    'hawi': {'Name': "Hawi Mekonin", 'Age': 21, 'Gender': "Female", 'Dept': "Electromechanical", 'Year': "Third"},
    'tsega': {'Name': "Tsegab Karta", 'Age': 22, 'Gender': "Male", 'Dept': "Electromechanical", 'Year': "Third"}
}

def display_info(person=None):
    if person:
        print(f"Information for {person}: {mydict.get(person), 'The person is not in our group'}")
    else:
        for name, info in mydict.items():
            print(f"Information for  { name } : {info}")


def add_person(name, info):
    mydict[name] = info
    print(f"{name} successfully added!")


def delete_person(name, info):
    if name in mydict:
        del mydict[name]
        print(f"{name} successfuly deleted!")
    else:
        print(f"{name} the name you enter is not in our Group!")

def modify_information(name, key, value):
    if name in mydict:
        mydict[name][value] = value
        print(f"{key} for {name} is succussfully modified!")
    else:
        print(f"{name} the name you enter is not in our Group!")

choice = input("Enter the person do you want know? (Sena, Moti, Hawi, Tsegab or all):").lower()

if choice == 'all':
    display_info()
else:
    display_info(choice)
    action = input(f"If do you want add enter Add, or if do you want delete enter Delete,"
                   f" or if do you want modify enter Modifiy: ")
    if action == 'Add':
        name = input(f"Enter the person name do you want add: ").lower()
        info = {
            'Name': input("Enter his/she's full name: "),
            'Age': int(input("Enter his/she's age: ")),
            'Gender': input("Enter his/she's gender: "),
            'Dept': input("Enter his/she's Department: "),
            'Year': input("Enter his / she's year: ")
        }
        add_person(name, info)
    elif action == 'Delete':
        name = input("Enter the person name do you want delete: ").lower()
        delete_person(name)
    elif action == 'Modify':
        name = input("Enter the person do you want modify name: ").lower()
        key = input("Enter the key modify: ")
        value = input(f"Enetr the new value for {key}: ")
        modify_information(name, key, value)
    else:
        print("You enter the incorrect value!")
