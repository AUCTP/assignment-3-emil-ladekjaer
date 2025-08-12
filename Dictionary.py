'''
In this make task we will write our own phonebook. First, your should create an empty dictionary called phoneBook. 
Subsequently, you should ask the user to press: 
1. to add an entry to the phonebook (name, phone number, email) and store it in the dictionary (you might want to nest multiple dictionaries). 
If the users presses 2, the program should show all available contacts. 
If the user presses 3, the program should ask the user for a contact name and show all the information for this contact. 
If the user presses 4, the program should be terminated
'''
phoneBook = {}
while True:
    print("1. Add a contact")
    print("2. Show all contacts")
    print("3. Show contact details")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        phoneBook[name] = {'phone': phone, 'email': email}
        print(f"Contact {name} added.")
        
    elif choice == '2':
            print("Contacts:")
            for contact in phoneBook:
                print(contact)
                
    elif choice == '3':
        name = input("Enter the name of the contact: ")
        if name in phoneBook:
            contact_info = phoneBook[name]
            print(f"Name: {name}, Phone: {contact_info['phone']}, Email: {contact_info['email']}")
        else:
            print(f"No contact found with the name {name}.")
            
    elif choice == '4':
        print("Exiting the program.")
        break
        
    else:
        print("Invalid choice, please try again.")