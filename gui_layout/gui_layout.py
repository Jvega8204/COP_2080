from nicegui import ui

ui.label("Welcome NiceGUI!").style("color: green; font-size: 40px")

#create a greeting

#-----------------Greeting------------

def greet():
    name = input_field.value.strip()
    msg = f"Hello, {name or "Stranger"}"
    ui.notify(msg)  #creates a popup

input_field = ui.input("Enter your name")
ui.button("Greet me!", color = "green", on_click = greet)

#-----------------Greeting------------

#-----------------Counter------------

#create a counter
class State:
    count = 0 

count_label = ui.label("Count: 0 ")

def add_one():
    State.count += 1
    count_label.text = f"Count: {State.count}"
#create a reset button
def reset(): 
    State.count = 0
    count_label.text = f"Count: {State.count}"
#-----------------Counter------------

#-----------------Layout------------

with ui.row():
    with ui.column().classes("flex-1"):
        #creates a card
        with ui.card().classes("h-65 w-full"):
            input_field = ui.input("Enter your name")
            ui.button("Greet me!", color = "green", on_click = greet)

        with ui.card().classes("h-65 w-full"): 
            count_label = ui.label("Count: 0 ")
            with ui.row():
                ui.button("Add one", color= "blue", on_click = add_one)
                ui.button("Reset", color = "red", on_click= reset )

#create a row 


ui.run(title = "Intro to NiceGUI",)