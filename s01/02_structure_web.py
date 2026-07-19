import flet as ft
# flet es 0.86.1
def main(page: ft.Page):
    page.title = 'Flet en la web'
    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'

    # Asignar un color de fondo (puedes usar el nombre en inglés o un código HEX)
    page.bgcolor = ft.Colors.AMBER_200
    page.add(ft.Text("¡Fondo de página cambiado!"))

    lbl_texto = ft.Text(value='¡Hola... Universo!', color='blue')
    page.controls.append(lbl_texto)
    page.update()

# La sintaxis moderna para la versión actual:
ft.app(target=main, view=ft.AppView.WEB_BROWSER, port=6173)