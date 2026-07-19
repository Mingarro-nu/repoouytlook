## Limpiar l terminal al ejecutar
import sys
if sys.platform == "win32":
    import asyncio
    from asyncio.proactor_events import _ProactorBasePipeTransport
    _original_close = _ProactorBasePipeTransport.close
    def _patched_close(self, *args, **kwargs):
        try:
            return _original_close(self, *args, **kwargs)
        except RuntimeError as e:
            if "Event loop is closed" in str(e):
                pass
            else:
                raise
    _ProactorBasePipeTransport.close = _patched_close
# ====================================================

import flet
from flet import ElevatedButton, Page, Text, TextField, Row


def main(page: Page):
    txt_nombre = TextField(label='Digite su nombre')

    lbl_saludo = Text()

    def saludar(event):
        lbl_saludo.value = f'¡Hola... {txt_nombre.value}!'
        page.update()

    row = Row(controls=[
        txt_nombre,
        ElevatedButton(text='Saludar', on_click=saludar),
        lbl_saludo
    ])

    page.add(row)


# Ejecución en el escritorio:
flet.app(target=main)
