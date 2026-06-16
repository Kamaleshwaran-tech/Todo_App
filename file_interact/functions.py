def get_todo():
    """ This function is used to read the file and
        enter the new task in it .
    """
    with open('data.txt','r') as file_local:
        todo_local = file_local.readlines()
    return todo_local
def put_todo(to_do):
    with open('data.txt','w') as file:
        file.writelines(to_do)


