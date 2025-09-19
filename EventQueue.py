Event_Queue=[]

def Add_event(event):
    Event_Queue.append(event)
    print("the event",event,"added to the queue.")

def Process_event():
    if Event_Queue:
        m=Event_Queue.pop(0)
        print("the event",m,"has been processed.")
    else:
        print("No event available for processing.")

def Display_pending_events():
    if Event_Queue:
        for event in Event_Queue: 
            print(event)
    else:
        print("No pending Events.")

def Cancel_event(n):
     if Event_Queue: 
        if n in Event_Queue:
            Event_Queue.remove(n)
            print("the event",n,"is cancelled successfully.")
     else:
        print("The event is not available or has been processed.")

while True:
    print("\n--- MENU ---")
    print("1. Add an event")
    print("2. Process an event")
    print("3. Display pending events")
    print("4. Cancel an event")
    print("5. Exit")

    choice=int(input("Enter a choice:"))

    match(choice):
        case 1 :
            event= input("Enter the event to be added in the event Queue.")
            Add_event(event)
        case 2:
            if not Event_Queue:
                print("Event queue is empty.Please add events first.")
            else:
                Process_event()
        case 3:
            Display_pending_events()
        case 4:
            n=input("enter the event to be canceled:")
            Cancel_event(n)
        case 5:
            print("Exiting the program\nThankyou")
            break
        case _:
            print("Invalid choice,please try again")