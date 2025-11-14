from nicegui import ui
from random import shuffle

EMOJIS = []
buttons = []
opened = []
matched = []

def restart_game():
    global EMOJIS, opened, matched

    opened.clear()
    matched.clear()

    EMOJIS = ['🍎', '🐶', '🚀', '🎵', '🔥', '🍩', '🧸', '🌟']
    EMOJIS = EMOJIS * 2
    shuffle(EMOJIS)

    # reset buttons
    for b in buttons:
        b.text = '?'


def reset_pair(i, j):
    buttons[i].text = '?'
    buttons[j].text = '?'
    opened.clear()


def handle_click(idx):
    """Logic for clicking a card."""
    # if its already flipped then wont reflip card
    if idx in matched or idx in opened:
        return

    # flip
    buttons[idx].text = EMOJIS[idx]
    opened.append(idx)

    # check if two cards get flipped
    if len(opened) == 2:
        i, j = opened

        if EMOJIS[i] == EMOJIS[j]:
            matched.append(i)
            matched.append(j)
            opened.clear()

            # check if the player won
            if len(matched) == 16:
                win_dialog.open()

        else:
            # if didnt match then flip over again
            ui.timer(0.5, lambda: reset_pair(i, j), once=True)


# popup when when player wins
win_dialog = ui.dialog()
with win_dialog:
    with ui.card():
        ui.label(' YOU WIN! ').classes('text-2xl font-bold text-green-600')
        ui.button('Close', on_click=win_dialog.close)


# restart button and title
with ui.row().classes('items-center mb-4'):
    ui.label('Memory Game').classes('text-2xl font-bold')
    ui.button('Restart', on_click=restart_game, color='red')


#Build 4×4 Grid of Buttons
with ui.grid(columns=4):
    for i in range(16):
        b = ui.button('?', on_click=lambda _, idx=i: handle_click(idx))
        b.classes('w-16 h-16 text-3xl')
        buttons.append(b)

# start game
restart_game()

ui.run(title='Memory Game')
