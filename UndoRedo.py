undo_stack = []
redo_stack = []
def make_change():
    text = input("Enter a string: ")
    undo_stack.append(text)
    redo_stack.clear()

def undo_action():
    if undo_stack:
        x = undo_stack.pop()
        redo_stack.append(x)
    else:
        print("Nothing to Undo\n")

def redo_action():
    if redo_stack: 
        x = redo_stack.pop()
        undo_stack.append(x)
    else:
        print("Nothing to Redo\n")

def display():
    print("Current State: ", end="")
    for i in undo_stack:
        print(i, end="")
    print()

while True:
    print("\n1. Enter Text")
    print("2. Undo")
    print("3. Redo")
    print("4. Current State")
    print("5. Exit")

    choice = int(input("Enter your choice: "))
    print()
    if choice == 1:
        make_change()
        display()
    elif choice == 2:
        undo_action()
        display()
    elif choice == 3:
        redo_action()
        display()
    elif choice == 4:
        display()
    elif choice == 5:
        break
    else:
        print("Invalid Input")