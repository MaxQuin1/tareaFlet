import flet as ft

def main(page:ft.page):
    page.window_width = 650
    page.window_height = 650
    page.scroll_to = True

    def clear(e):
        checkboxes = [control for control in peopleView.controls if isinstance(control, ft.Checkbox)]
        for checkbox in checkboxes:
            peopleView.controls.remove(checkbox)
        view.update()

    def calcular(e):
        imc = float()

        weight = float(inputWeight.value)
        height = float(inputHeight.value)

        imc = float(weight) / float(height)**2

        if imc:
            if imc < 18.5:
                recomendacion = 'Estas bajo de peso come mas'
            elif (imc >= 18.5) and (imc <= 24.9):
                recomendacion = 'Tienes buen peso mantente asi'
            elif (imc >= 20) and (imc <= 29.9):
                recomendacion = 'Tienes sobrepeso tienes que hacer mas ejercicio'
            elif imc >= 30:
                recomendacion = 'Tienes obecidad urge que vayas a ver a un doctor'

        output_text = f"{inputName.value} tu edad es {inputYear.value}, tu peso de {inputWeight.value}, tu altura es {inputHeight.value} y tu imc seria: {imc}"
        infoPeople = f'{output_text}\n{recomendacion}'
        peopleView.controls.append(ft.Checkbox(label=infoPeople))

        inputName.value = ''
        inputYear.value = ''
        inputWeight.value = ''
        inputHeight.value = ''

        view.update()

    clear_btn = ft.ElevatedButton(text='Limpiar historial', on_click=clear)

    getName = ft.Text('Introduce tu nombre completo')
    inputName = ft.TextField(
            label="Nombre : ",
            width=550)
    
    inputYear = ft.TextField(
            label="Introduce tu edad : ",
            width=200)
    
    inputWeight = ft.TextField(
            label="Introduce tu peso en kg : ",
            width=200)
    
    inputHeight = ft.TextField(
            label="Introduce tu altura en metros: ",
            width=200)
    
    rowInput = ft.Row(
        controls=[inputYear,inputWeight,inputHeight]
    )
    
    submit_btn = ft.ElevatedButton(text="Calcular IMC", on_click=calcular)

    rowBtn = ft.Row(
        controls=[submit_btn,clear_btn]
    )

    recomendacion = ft.Text()
    output_text = ft.Text()
    peopleView = ft.Column()

    view=ft.Column(
        width=600,
        controls=[
            ft.Column(
                controls=[
                    getName,
                    inputName,
                    rowInput,
                    rowBtn,
                ],
            ),
            peopleView
        ],
    )

    
    page.add(view)

ft.app(target=main)

# ft.app(target=main, view=ft.AppView.WEB_BROWSER)