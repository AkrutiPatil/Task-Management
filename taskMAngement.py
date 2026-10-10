def task():
    tasks =[] #empty list
    print("------Welcome  to the TASK mangement App-----------")

    total_task = int(input("Enter how many task you want to add = "))
    for i in range(1,total_task+1):
        task_name=input(f"Enter task{i} = ")#enter task 3
        tasks.append(task_name)


    print(f"today's tasks are\n{tasks}")

    while True:
        operation = int(input("Enter 1-add\n2-update\n3-delete\n4-view\n5-exit/stop/"))
        if operation ==1:
            add = input("enter the task you want to add =")
            task.append(add)
            print("task {add} hs been successfully added...")

        elif operation ==2:
            update_val=input("Enter the task name you want ot upadate = ")
            if update_val in tasks:
                up=input("enter new task ")
                ind= tasks.index(update_val)
                tasks[ind]=up
                print(f"updateed task{up}")

task()





