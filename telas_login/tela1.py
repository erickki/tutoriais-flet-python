import flet as ft
import time

COR = {"cinza":"#1a1a1a", "branco":"#dedede", "roxo":"#791a78", "transparente":ft.colors.TRANSPARENT}
FONTE = "JetBrains Mono"
NEGRITO = ft.FontWeight.BOLD
IMAGEM = {"fundo":"assets/fundo_tela1.jpg"}

ESTILO_TEXT = ft.TextStyle(size=18, font_family=FONTE, color=COR["branco"])
ESTILO_LABEL = ft.TextStyle(size=20, font_family=FONTE, color=COR["branco"], weight=NEGRITO)

def tela_login(page: ft.Page):
    
    page.title = "Faça seu login."
    page.window.width = 1280
    page.window.height = 720
    page.window.maximizable = False
    page.window.minimizable = False
    page.padding = 0
    page.bgcolor = COR["cinza"]
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window.center()

    def mudar_visibilidade_senha(e):
        if entrada_senha.password == True:
            icone_visibilidade.scale = 0
            page.update()
            entrada_senha.password = False
            icone_visibilidade.content.name = ft.icons.VISIBILITY_OFF
            time.sleep(0.3)
            icone_visibilidade.scale = 1
        else:
            icone_visibilidade.scale = 0
            page.update()
            entrada_senha.password = True
            icone_visibilidade.content.name = ft.icons.VISIBILITY
            time.sleep(0.3)
            icone_visibilidade.scale = 1
        page.update()

    def logar_no_sistema(e):
        None

    def esqueci_minha_senha(e):
        None

    def clique_aqui(e):
        None


    texto_login = ft.Text(
        value="Faça seu login.", text_align=ft.TextAlign.CENTER, font_family=FONTE, size=24, weight=NEGRITO,
        color=COR["branco"]
    )

    barra_horizontal = ft.Divider(
        height=0, thickness=1.5, color=COR["branco"], leading_indent=25, trailing_indent=25
    )

    entrada_login = ft.TextField(
        text_align=ft.TextAlign.START, cursor_color=COR["branco"], cursor_width=1.5, cursor_height=30, cursor_radius=15,
        selection_color=COR["roxo"], text_size=18, text_style=ESTILO_TEXT, label="Login", label_style=ESTILO_LABEL,
        border_color=COR["transparente"], border_radius=15, border_width=1.5, width=250, height=50
    )

    entrada_senha = ft.TextField(
        text_align=ft.TextAlign.START, cursor_color=COR["branco"], cursor_width=1.5, cursor_height=30, cursor_radius=15,
        selection_color=COR["roxo"], text_size=18, text_style=ESTILO_TEXT, label="Senha", label_style=ESTILO_LABEL,
        border_color=COR["transparente"], border_radius=15, border_width=1.5, width=200, height=50, password=True
    )

    icone_visibilidade = ft.Container(
        content=ft.Icon(
            name=ft.icons.VISIBILITY, color=COR["branco"], size=30
        ),alignment=ft.alignment.center, width=50, height=50, on_click=mudar_visibilidade_senha, animate_scale=300,
        scale=1
    )

    linha_senha = ft.Container(
        content=ft.Row(
            [
                entrada_senha, icone_visibilidade
            ],alignment=ft.MainAxisAlignment.CENTER, vertical_alignment=ft.CrossAxisAlignment.CENTER
        ),alignment=ft.alignment.center, width=250, height=50
    )

    botao_login = ft.Container(
        content=ft.Text(
            value="Login", text_align=ft.TextAlign.CENTER, font_family=FONTE, size=24, weight=NEGRITO,
            color=COR["branco"]
        ),alignment=ft.alignment.center, width=200, height=50, border_radius=15, on_click=logar_no_sistema,
        border=ft.border.all(width=1.5, color=COR["branco"])
    )

    botao_esqueci_minha_senha = ft.Container(
        content=ft.Text(
            value="esqueci minha senha", text_align=ft.TextAlign.CENTER, font_family=FONTE, size=18, weight=NEGRITO,
            color=COR["branco"], italic=True, style=ft.TextStyle(decoration=ft.TextDecoration.UNDERLINE,
            decoration_color=COR["branco"])
        ),alignment=ft.alignment.center, width=250, height=50, on_click=esqueci_minha_senha
    )

    texto_nova_conta = ft.Text(
        value="Ainda não possui um cadastro?", text_align=ft.TextAlign.CENTER, font_family=FONTE, size=14, weight=NEGRITO,
        color=COR["branco"]
    )

    botao_clique_aqui = ft.Container(
        content=ft.Text(
            value="Clique Aqui!", text_align=ft.TextAlign.CENTER, font_family=FONTE, size=14, weight=NEGRITO,
            color=COR["branco"], italic=True, style=ft.TextStyle(decoration=ft.TextDecoration.UNDERLINE,
            decoration_color=COR["branco"])
        ),alignment=ft.alignment.center, on_click=clique_aqui
    )

    linha_cadastro = ft.Container(
        content=ft.Row(
            [
                texto_nova_conta, botao_clique_aqui
            ],alignment=ft.MainAxisAlignment.CENTER, vertical_alignment=ft.CrossAxisAlignment.CENTER, expand=True
        ),alignment=ft.alignment.center, height=50
    )

    fundo_itens = ft.Container(
        content=ft.Column(
            [
                texto_login, barra_horizontal, entrada_login, linha_senha, botao_login, botao_esqueci_minha_senha,
                linha_cadastro
            ],alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=20
        ),alignment=ft.alignment.center, width=500, height=500, border=ft.border.all(width=1.5, color=COR["branco"]),
        border_radius=15, blur=15.0
    )

    fundo_geral = ft.Container(
        content=ft.Column(
            [
                fundo_itens
            ],alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ),alignment=ft.alignment.center, width=1280, height=720, image=ft.DecorationImage(src=IMAGEM["fundo"],
        fit=ft.ImageFit.FILL)
    )

    page.add(fundo_geral)

ft.app(target=tela_login)