from nicegui import ui 

def twist_hash(text: str) -> int:
    h = 0x9E3779B1

    for c in text:
        h = h ^ ord(c)
        h = h * 0x517CC1C7
        h = h & 0xFFFFFFFF

    h = h ^ len(text)
    return h

hashbrowns_value = twist_hash("hashbrowns")
message = f'hashbrowns = {hashbrowns_value}'

with ui.card().classes('p-6'):
    with ui.row().classes('w-full'):
        ui.label('Hashing').classes('text-2xl font-bold text-red-600')
        ui.label(message).classes('text-md bold mb-4')

    input_box = ui.input(label='Enter text to hash:')
    output_label = ui.label('Hash value: ').classes('text-lg mt-4')

    def compute_hash():
        text = input_box.value
        result = twist_hash(text)
        output_label.text = f'Hash value: {result}'

    def clear_fields():
        input_box.value = ''
        output_label.text = 'Hash value: '

    with ui.row().classes('mt-4'):
        ui.button('GET HASH', on_click=compute_hash)
        ui.button('CLEAR', on_click=clear_fields, color='red')

ui.run()
