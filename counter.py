import flet 
from flet import IconButton, Page, Row, TextField, icons

# Poner flet as ft, simplifica en las lineas que tengamos flet a ft

def main(page: Page):
    page.title = 'Flet Counter'
    page.vertical_alignment = 'center'

    # Asignar un color de fondo (puedes usar el nombre en inglés o un código HEX)
    page.bgcolor = flet.Colors.AMBER_100
    page.add(flet.Text("¡Fondo de página cambiado!"))
    txt_number = TextField(value='0', text_align='right', width=100)

    def minus_click(event):
        txt_number.value = int(txt_number.value) - 1
        page.update()
        
    def plus_click(event):
        txt_number.value = int(txt_number.value) + 1
        page.update()
    
    page.add(
        Row(
            [
                IconButton(icons.Icons.REMOVE, on_click=minus_click),
                txt_number,
                IconButton(icons.Icons.ADD, on_click=plus_click)
            ],
            alignment='center'
        )
    )

# En icons.Remove NO funciona es icons.Icons.REMOVE y en ADD
# Modo Desktop:
# flet.app(target=main)

# La sintaxis moderna para la versión actual
# Modo web:
flet.app(target=main, view=flet.AppView.WEB_BROWSER, port=6173)