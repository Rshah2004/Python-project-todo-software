
import time
import PySimpleGUI as sg
import streamlit as st

print()
print()

now = time.strftime("%b %d, %Y %H:%M:%S")
print(now)

print("                         TODO LIST                   ")

print("To get started, please enter your todos")



def get_todos():
    with open("todos.txt", "r") as file:
        todos = file.readlines()
    return todos
def write_todos(r):
    with open("todos.txt", "w") as file:
        todos = file.writelines(r)
    return todos

def web():
    st.title("My Todo App")
    



def graphical():
    def create_layout(todos):
        label = sg.Text("Type in a to-do")
        input_box = sg.InputText(tooltip="Enter todo", key = "todo")
        add_button = sg.Button("Add")

        clock = sg.Text('', key = "clock")

        list_box = sg.Listbox(values = get_todos(), key = "todos", enable_events = True, size = [45, 10])

        edit_button = sg.Button("Edit")

        clear_button = sg.Button("Clear")

        complete_button = sg.Button("Complete")

        Exit_button = sg.Button("Exit")

        layout=[[clock],[label], [input_box, add_button], [list_box, edit_button], [clear_button],[complete_button],[Exit_button]]
        return layout

        

    window = sg.Window("To-do App", create_layout(get_todos()), font = ("Helvetica", 20))

    while True:
        event, values = window.read(timeout = 10)
        window["clock"].update(value = time.strftime("%b %d, %Y %H:%M:%S"))
        print(event)
        print(values)

        match event:
            case "Add":
                todos = get_todos()
                new_todos = values["todo"].strip() + "\n"
                todos.append(new_todos) 
                write_todos(todos)
                window.close()
                window = sg.Window("To-do App", create_layout(todos), font = ("Helvetica", 20))
                event, values = window.read()
                
            case "Edit":
                try:
                    todo_edit = values["todos"][0]
                    input_box_2 = sg.InputText(tooltip = "Enter edited todo", key = "todo")
                    add_button_2 = sg.Button("add Edit")
                    window_2 = sg.Window("Edit todo", layout = [[input_box_2],[add_button_2]], font = ("Helvetica", 10))
                    event_2, values_2 = window_2.read()
                    window_2.close()
                    todos = get_todos()
                    new_todo = values_2["todo"] + "\n"
                    index = todos.index(todo_edit)
                    todos[index] = new_todo
                    write_todos(todos)
                    window["todos"].update(values = todos)
                except IndexError:
                    sg.popup("Please select an item first", font = ("Helvetica", 20))

            case "Clear":
                todos = get_todos()
                new_todos = []
                write_todos(new_todos)
                window["todos"].update(values = todos)

            case "Complete":
                try:
                    todos = get_todos()
                    todos_complete = values["todos"][0]
                    index1 = todos.index(todos_complete)
                    todos.pop(index1)
                    window["todos"].update(values = todos)
                    write_todos(todos)
                except:
                    sg.popup("Please select an item first", font = ("Helvetica", 20))
                    
            case "Exit":
                break
                
                
            case sg.WIN_CLOSED:
                break

            
                
    window.close()



def commandline(): 
    while True :
        user_action = input("show, add, edit, complete, clean or exit:? ")
        user_action = user_action.strip()
        if 'add' in user_action:
            check = user_action[4:]
            if check != "":
                x = user_action[4: ] + "\n"
                r = get_todos()
                r.append(x.title())
                write_todos(r)
                
            else:
                k = int(input("input the number of todos "))
                for i in range(0, k, 1):
                    x = input("Input your todo for tomorrow ") + "\n"
                    r = get_todos()
                    r.append(x.title())
                    write_todos(r)
                
        elif 'edit' in user_action:
            if user_action[5:] != "" :
                 check = int(user_action[5:])
                 check-= 1
                 r = get_todos()
                 print("Existing todos =")
                 for index,item in enumerate(r):
                     print(f"{index+1} - {item}".strip('\n'))
                 print()
                        
                 c = input("input the new todo ")
                 r[check] = c + '\n'           
                 write_todos(r)
            
            else:
                k = int(input("input the todo number u want to edit "))
                k-= 1
                r = get_todos()
                print("Existing todos =", end = " ")
                for x in r:
                    print(x.strip('\n'), end = " ")
                print()
                        
                c = input("input the new todo ")
                r[k] = c + '\n'

                print("New todos=", end = " ")
                for x in r:
                    print(x.strip('\n'), end = " ")

                write_todos(r)
                print()

            
        elif "show" in user_action or "display" in user_action:
            r = open('todos.txt','r')
            todos = r.readlines()
            new_todos = []
            for x in todos:
                new_todos.append(x.strip('\n'))
            r.close()
            for index, item in enumerate(new_todos):
                row = f"{index + 1}-{item} "
                print(row)
                
        elif "complete" in user_action:
            if user_action[9:] != "":
                check = int(user_action[9:])
                r = get_todos()
                todo_to_remove = r[check-1].strip('\n')
                r.pop(check - 1)
                write_todos(r)
                message = f"Todo {todo_to_remove} was removed"
                print(message)
                
            else:          
                number = int(input("Number of the todo to complete: "))
                r = get_todos()
                todo_to_remove = r[number-1].strip('\n')
                r.pop(number - 1)
                write_todos(r)
                message = f"Todo {todo_to_remove} was removed"
                print(message)
            

        elif "clean" in user_action:
            r = open("todos.txt","w")
            r.truncate()

            
        elif "exit" in user_action:
            break

        else:
            print("Invalid input")

while True:
    print("1. to use graphical interface")
    print("2. to use command line interface")
    case = int(input("input case"))
    if case == 1:
        graphical()
        
    elif case == 2:
        commandline()

    elif case == 3:
        web()
    else:
        print("invalid input")
        
