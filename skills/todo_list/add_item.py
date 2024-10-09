from output import output


def add_item_todo_list(text):
    text = input("What would you like to add to your todo list? (cancel to cancel): ")
    if text == "cancel":
       print("Cancelled")
    else:
        text = text.lower()
        text = text.split("add ", 1)[1]
        text = text.split()
        text.reverse()
        text = " ".join(text)
        text = text.split("to ", 1)[1]
        text = " ".join(text.split(" ")[::-1]) 
    with open("todo.md", "a") as todo_list:
        todo_list.seek(0)
        todo_list.write("\n")
        todo_list.write(f"- [ ] {text}")

    output(f"Successfully added '{text}' to your todo list sir!");
