import streamlit as st

todo_list = []

while True:
  if not todo_list:
    print("Your ToDo list is empty")
  else:
    index = 1
    for task in todo_list:
      print(f"{index}. {task}")
      index += 1

  print("Options:")
  print("1. Add Task")
  print("2. Remove Task")
  print("3. Quit")

  choice = input("Enter your choice (1, 2, or 3): ")
  
  if choice == "1":
    print("Adding task")
    new_task = input("Enter task to be added:")
    todo_list.append(new_task)
    print(f"Task '{new_task}' added to the ToDo list")
  elif choice == "2":
    if len(todo_list) == 0:
      print("Your ToDo list is empty")
    else:
        removed_task = todo_list.pop()
        print(f"Removed task: {removed_task}") 
  elif choice == "3":
    print("Quitting")
    break
