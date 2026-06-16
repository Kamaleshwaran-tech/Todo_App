from functions import get_todo,put_todo
import time

now = time.strftime("%b %d ,%Y %H:%M:%S")
print("It is",now)

while True:
    user_input = input("Type add, show, complete, edit, or exit: ").strip()

    if user_input.startswith("add"):
        todo = user_input[4:]
        # file = open('data.txt','r')
        # to_do = file.read()
        # file.close()

        to_do = get_todo()

        to_do.append(todo + "\n")
        # file = open('data.txt','w')
        # file.writelines(to_do)
        # file.close()

        put_todo(to_do)
        print(help(get_todo))

    elif user_input.startswith("show"):
        # file = open('data.txt','r')
        # to_do = file.readlines()
        # file.close()
        to_do = get_todo()
        # new_todo = []
        # for i in to_do:
        #     new_item = i.strip("\n")
        #     new_todo.append(new_item)
        # new_todo = [i.strip("\n") for i in to_do]

        for index,todoo in enumerate(to_do):
            todoo = todoo.strip("\n")
            print(f"{index+1}-{todoo}")

    elif user_input.startswith("edit"):
        try:
            index = int(user_input[5:])
            index = index - 1
            to_do = get_todo()
            print(to_do[index])
            to_do[index] = input("Enter the new task : ")+"\n"
            put_todo(to_do)
        except ValueError:
            print("Invalid input")
            continue

    elif user_input.startswith("complete"):
        try:
            index = int(user_input[9:])
            to_do = get_todo()
            remove_tode = to_do[index-1].strip("\n")
            to_do.pop(index-1)
            put_todo(to_do)
            print(f"Todo {remove_tode} has been completed!")
        except IndexError:
            print("Input value is out of range")
            continue

    elif user_input.startswith("exit"):
        break

    else:
        print("Invalid input")


print("Hope! you will finish those task , visit again!..")
