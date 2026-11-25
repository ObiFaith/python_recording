def add_task(tasks: list[dict], title: str):
    if not title:
        return tasks

    tasks.append({"title": title, "done": False})

def mark_done(tasks: list[dict], index: int):
    tasks[index]["done"] = True

def remove_task(tasks, index):
    del tasks[index]

def count_remaining(tasks: list[dict]):
    count = 0

    for task in tasks:
        if task['done'] == False:
            count += 1

    return count


COMMANDS = ("add", "mark_done")

def get_valid_input(prompt: str="Enter command: "):
    while True:
        user_input = input(prompt).strip().lower()

        if user_input.startswith(COMMANDS):
            return user_input

def main():
    tasks = []

    while True:
        user_input = get_valid_input()

        if user_input.startswith(COMMANDS[0]):
            title = user_input.split('"')[1]
            add_task(tasks, title)
        elif user_input.startswith(COMMANDS[1]):
            index = user_input.split('index')[1]
            try:
                mark_done(tasks, int(index))
                count = count_remaining(tasks)
                print("count_remaining =", count)
            except:
                print("Enter a valid index")

if __name__ == "__main__":
    main()
