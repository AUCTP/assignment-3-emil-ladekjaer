'''
In this make task, you should write a simple note taking program. It should wait for user input and do the following depending on it: 
1. All saved notes are loaded to a list noteBooks from the file notebook.txt
2. The user can enter a short message that is appended to the list noteBooks.
3. Show all notes
4: The notebook is stored in a file called notebook.txt and the program is terminated
'''


#main program
notebook = []
load_notes = open("notebook.txt", "r")
for line in load_notes:
    notebook.append(line.strip())
load_notes.close()

while True:
    print("1. Add a note")
    print("2. Show all notes")
    print("3. Save and exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        note = input("Enter your note: ")
        notebook.append(note)
    elif choice == 2:
        print("Notes:")
        for i in range(len(notebook)):
            print(f"Note {i+1}: {notebook[i]}")
    elif choice == 3:
        save_file=open("notebook.txt", "w")
        for note in notebook:
            save_file.write(note + "\n")
        print("Notes saved. Exiting...")
        break
    else:
        print("Invalid choice, please try again.")