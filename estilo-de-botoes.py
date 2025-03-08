import flet as ft
import time

COR = {"cinza":"#1a1a1a", "branco":"#dedede", "roxo":"#791a78"}
FONTE = "JetBrains Mono"
NEGRITO = ft.FontWeight.BOLD

def main(page: ft.Page):
    
    page.title = "Siga a DungeonByte™ nas redes sociais e deixe seu like!"
    page.window.width = 1280
    page.window.height = 720
    page.window.maximizable = False
    page.window.minimizable = False
    page.padding = 0
    page.bgcolor = COR["cinza"]
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window.center()
    
    # Botão de número 1 |-----> |-----> |-----> |-----> |-----> |-----> |-----> |-----> |-----> |-----> |-----> |----->
    # Link: 
    def animacao1_botao1(e):
        fundo1.opacity = 1
        fundo1.update()
        while True:
            if e.data == "true":
                pass
            else:
                fundo1.opacity = 0
                fundo1.update()
                break

    def animacao2_botao1(e):
        fundo1.scale = 0
        fundo1.opacity = 0
        texto1.content.opacity = 0
        page.update()
        time.sleep(1)
        fundo1.scale = 1
        fundo1.opacity = 1
        texto1.content.opacity = 1
        page.update()

    texto1 = ft.Container(
        content=ft.Text(
            value="Botão", text_align=ft.TextAlign.CENTER, font_family=FONTE, size=30, weight=NEGRITO,
            color=COR["branco"]
        ), opacity=1, animate_opacity=100
    )

    fundo1 = ft.Container(
        alignment=ft.alignment.center, border=ft.border.all(width=2, color=COR["branco"]), border_radius=15, width=150,
        height=50, scale=1, animate_scale=100, opacity=0, animate_opacity=100
    )

    botao1 = ft.Container(
        ft.Stack(
            [
                fundo1, texto1
            ],alignment=ft.alignment.center
        ),alignment=ft.alignment.center, on_click=animacao2_botao1, on_hover=animacao1_botao1
    )


    coluna1 = ft.Column(
        [
            botao1
        ],alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    coluna2 = ft.Column(
        [

        ],alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    coluna3 = ft.Column(
        [

        ],alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    coluna4 = ft.Column(
        [

        ],alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    geral = ft.Row(
        [
            coluna1, coluna2, coluna3, coluna4
        ],alignment=ft.MainAxisAlignment.CENTER, vertical_alignment=ft.CrossAxisAlignment.CENTER
    )

    page.add(geral)

ft.app(target=main)