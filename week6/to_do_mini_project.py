def to_do_mini_project():
    todos: list[dict] = []
    print("Menu: add | view | remove | done | quit")
    while True:
        user_input = input("> ").strip()

        if user_input.startswith("add "):
            todos.append({"id": len(todos) + 1, "todo": user_input[4:], "completed": False})
            print("Task added.\n")
        elif user_input.lower() == "view":
            for todo in todos:
                id, task, completed = todo.values()
                print(f"{id}. [{"x" if completed else " "}] {task}")
            print("\n")
        elif user_input.startswith("done "):
            try:
                idx = int(user_input[5:])
                todos[idx - 1]["completed"] = True
                print(f"Task {idx} marked as done.\n")
            except:
                print("Enter a valid todo number\n")
        elif user_input.startswith("remove "):
                try:
                    idx = int(user_input[7:])
                    del todos[idx - 1]
                    print(f"Task removed.\n")
                except:
                    print("Enter a valid todo number\n")
        elif user_input.lower() == "quit":
            print("Goodbye!")
            break

to_do_mini_project()
