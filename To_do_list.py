
print(" welcome to TO-DO-LIST program")
 
def load_tasks(filename):
    try:
        with open(filename, "r") as  file :
            tasks = [line.strip( ) for line in file]
    except FileNotFoundError:
        tasks = []
    return tasks
    
def save_tasks(filename, tasks):
    with open(filename, "w") as file:
        for task in tasks:
            file.write(task + "\n")
    
filename = "tasks.txt"
tasks = load_tasks(filename)

while True :
    print("\n1.view task \n 2.add task \n 3.remove task \n 4.exit task :")
    choice = input( "Enter your choice :")
    
    
    if choice == "1":
        if tasks:
            print("\n your taks are ")
            for i , task in enumerate(tasks , start = 1):
                print(f"{i}.{task}")
        else:
            print("\n no task found")

    elif choice == "2":
        task = input("Enter your task :")
        tasks.append(task)
        save_tasks(filename , tasks)
        print("Task added successfully!")
    
    elif choice =="3":
        if tasks:
            task_no = int(input("Enter the task number to remove :"))
            if 1 <= task_no <= len(tasks):
                remove = tasks.pop(task_no - 1)
                save_tasks(filename , tasks)
                print(f" task {remove} removed successfully :")
            else:
                print("invaild task number :")
        else: 
            print("NO tasks found to remove :")
            
    elif choice == "4":
        print("Thank you for using to do list program . Goodbye! ")
        break
    else :
        print("Invaild choice please try again")
