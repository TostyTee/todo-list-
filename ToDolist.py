import streamlit as st

# Initialize the ToDo list
if 'todo_list' not in st.session_state:
    st.session_state.todo_list = []

# Display the current ToDo list
st.header("Your ToDo List")
if not st.session_state.todo_list:
    st.write("Your ToDo list is empty")
else:
    for index, task in enumerate(st.session_state.todo_list, start=1):
        st.write(f"{index}. {task}")

# Options for adding or removing tasks
st.header("Options")
if st.button("Add Task"):
    new_task = st.text_input("Enter task to be added:", key='new_task')
    if new_task:
        st.session_state.todo_list.append(new_task)
        st.success(f"Task '{new_task}' added to the ToDo list")
        st.experimental_rerun()

if st.button("Remove Last Task"):
    if st.session_state.todo_list:
        removed_task = st.session_state.todo_list.pop()
        st.success(f"Removed task: {removed_task}")
        st.experimental_rerun()
    else:
        st.warning("Your ToDo list is empty")

if st.button("Quit"):
    st.write("Goodbye!")
