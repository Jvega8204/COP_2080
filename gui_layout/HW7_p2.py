from nicegui import ui
from random import shuffle

# TODO 1: Create list of 8 unique emojis, duplicate, and shuffle
EMOJIS = ['🍎', '🐶', '🚀', '🎵', '🔥', '🍩', '🧸', '🌟']
EMOJIS = EMOJIS * 2   # 2 for the matching pair
shuffle(EMOJIS)

buttons = []
opened = []  
matched = [] 

# TODO 2: Write function to flip non-matching cards back
def reset_pair(i, j):
    buttons[i].text = '?'
    buttons[j].text = '?'
    opened.clear()

# TODO 3: Write click handler
def handle_click(idx):
    # check if already flipped or matched
    if idx in matched or idx in opened:
        return

    # flip chosen card
    buttons[idx].text = EMOJIS[idx]
    opened.append(idx)

    # check if match
    if len(opened) == 2:
        i, j = opened

        if EMOJIS[i] == EMOJIS[j]:
            matched.append(i)
            matched.append(j)
            opened.clear()

            # check if win
            if len(matched) == 16:
                ui.notify('You Win! 🎉', color='green')
        else:
            # if not a match, flip back after delay
            ui.timer(0.5, lambda: reset_pair(i, j), once=True)

# Build 4x4 grid
with ui.grid(columns=4):
    for i in range(16):
        b = ui.button('?', on_click=lambda _, idx=i: handle_click(idx))
        b.classes('w-16 h-16 text-3xl')   # ← FIXED: moved classes() here
        buttons.append(b)

ui.run(title='Memory Game')
