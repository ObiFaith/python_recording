tasks = []

while True:
    user_input = input("What do you want to do?: ").strip()
    if user_input.startswith('add'):
        tasks.append(user_input[5:-1])
        print("Task added successfully!")
    elif user_input.startswith('remove'):
        index = int(user_input[-1]) - 1
        if len(tasks) <= index:
            print(f"Either no task or no task at {index}")
        else:
            tasks.pop()
            print("Task removed successfully!")
    elif user_input.startswith('quit'):
        break
    elif user_input.startswith('view'):
        if not tasks:
            print("No task to view")
        else:
            for index in range(len(tasks)):
                print(f"{index+1}: {tasks[index]}")
