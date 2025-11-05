from nicegui import ui

ui.label("Welcome NiceGUI!").style("color: green; font-size: 40px")

#create a greeting

#-----------------Greeting------------

def greet():
    name = input_field.value.strip()
    msg = f"Hello, {name or "Stranger"}"
    ui.notify(msg)  #creates a popup

#-----------------Greeting------------

#-----------------Counter------------

#create a counter
class State:
    count = 0 


def add_one():
    State.count += slider.value
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
    with ui.column().classes("flex-1"):
        with ui.card().classes("h-65 w-full"): 
            count_label = ui.label("Count: 0 ").classes("text-lg")
            with ui.row():
                ui.button("Add one", color= "blue", on_click = add_one)
                ui.button("Reset", color = "red", on_click= reset )
            label_slider = ui.label("step: 5").classes("text-lg")
            slider = ui.slider(min=1, max = 10, value = 5)
            slider.on("update:model-value", lambda: label_slider.set_text(f"Step: {slider.value}"))

    with ui.row():
        n1 = ui.number("Number 1",value = 0).classes("w-24")
        ui.label("+").classes("text-lg")
        n2 = ui.number("Number 2",value = 0).classes("w-24")
        ui.label("=").classes("text-lg")
        ui.label(f"{n1}+{n2}")



ui.switch ("Darkmode", 
        on_change=lambda e: ui.dark_mode().enable() if e.value else ui.dark_mode().disable())

ui.run(title = "Intro to NiceGUI",)