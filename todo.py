tasks = [] #list to store tasks

while True:
    print("1.Add 2.View 3.Delete 4.Exit")
    ch = int(input("Choose: ")) #user choice

    if ch == 1:
        task = input("Enter task: ")
        tasks.append(task) #add task to the list
    elif ch == 2:
        print(tasks)
    elif ch == 3:
        tasks.pop() #remove last task from the list
    elif ch == 4:
        break #exit the loop
