print("this is task1")

tasks=[]
while True:
    print("\n---------TO DO LIST---------")
    print("1.add task")
    print("2.view task")
    print("3.exit")
    
    choice=input("enter your choice (1/2/3):")
    if choice=='1':
        task = input("enter the task you want to do :")
        tasks.append(task)
        print("task inserted successfully!" )
        
        
    elif choice=='2':
        if len(tasks)==0:
            print("there are no tasks in list")
            
        else:
            print(" your tasks:")
            for i in range(len(tasks)):
                print(i+1,".",tasks[i])
                
    elif choice =='3':
        print("Exiting TO-DO LIST thank you !")
        break
        
    else:
        print("invalid choice !")
