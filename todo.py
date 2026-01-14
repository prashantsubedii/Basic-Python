tasks = []

while True:
    print("1.Add 2.View 3.Delete 4.Exit")
    ch = int(input("Choose: "))

    if ch == 1:
        task = input("Enter task: ")
        tasks.append(task)
    elif ch == 2:
        print(tasks)
    elif ch == 3:
        tasks.pop()
    elif ch == 4:
        break
