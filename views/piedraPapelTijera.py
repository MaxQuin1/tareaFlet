import flet as ft
import random

def main(page:ft.Page):
    page.window_width = 650
    page.window_height = 650
    page.scroll_to = True

    def batalla(e):

        armMachine = ft.Text()
        armMachine.value = random.choice(armas)
        result = ft.Text('Resultado')

        if armChoice.value == "Piedra":
            if armMachine.value == "Piedra":
                result.value = "Empataste"
            if armMachine.value == "Tijera":
                result.value = "Ganaste"
            if armMachine.value == "Papel":
                result.value = "Perdiste"
        elif armChoice.value == "Papel":
            if armMachine.value == "Papel":
                result.value = "Empataste"
            if armMachine.value == "Tijera":
                result.value = "Perdiste"
            if armMachine.value == "Piedra":
                result.value = "Ganaste"
        elif armChoice.value == "Tijera":
            if armMachine.value == "Tijera":
                result.value = "Empataste"
            if armMachine.value == "Piedra":
                result.value = "Perdiste"
            if armMachine.value == "Papel":
                result.value = "Ganaste"

        output_text.value = f"{inputName.value} tu {result.value} con la maquina que uso {armMachine.value} y tu {armChoice.value}"
        page.update()

    piedra = ft.Text()
    papel = ft.Text()
    tijera = ft.Text()

    getName1 = ft.Text('Introduce tu nombre')

    inputName = ft.TextField(
            label="Nombre : ",
            width=600)
    
    armas = ['Piedra','Papel','Tijera']

    output_text = ft.Text()
    submit_btn = ft.ElevatedButton(text="Enviar", on_click=batalla)
    armChoice = ft.Dropdown(
        width=100,
        options=[
            ft.dropdown.Option("Piedra"),
            ft.dropdown.Option("Papel"),
            ft.dropdown.Option("Tijera"),
        ],)
    
    view=ft.Column(
        width=600,
        controls=[
            getName1,
            inputName,
            armChoice,
            submit_btn,
            output_text,
        ],
    )

    page.add(view)

ft.app(target=main)