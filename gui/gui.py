from nicegui import ui

ui.label("Welcome NiceGUI!").style("color: green; font-size: 40px")

#create a greeting

def greet():
    name = input_field.value.strip()
    msg = f"Hello, {name or "Stranger"}"
    ui.notify(msg)  #creates a popup

input_field = ui.input("Enter your name")
ui.button("Greet me!", color = "green", on_click = greet)

#create a counter
class State:
    count = 0 

count_label = ui.label("Count: 0 ")
def add_one():
    State.count += 1
    count_label.text = f"Count: {State.count}"

ui.button("Add one", color = "red", on_click= add_one)

#create a reset button

ui.run(title = "Intro to NiceGUI",)