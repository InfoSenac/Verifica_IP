import flet as ft
import ipaddress

def main(page: ft.Page):
    page.title = "Verificador de IP e Rede"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor = ft.Colors.BLUE_GREY_50

    # Campos de entrada
    ip_field = ft.TextField(label="Endereço IP", width=350, autofocus=True)
    rede_field = ft.TextField(label="Rede (CIDR)", width=350)
    resultado = ft.Text(value="", color=ft.Colors.BLUE, size=16, text_align=ft.TextAlign.CENTER)

    # Função de verificação
    def verificar_ip(e):
        ip_text = ip_field.value.strip()
        rede_text = rede_field.value.strip()

        try:
            ip = ipaddress.ip_address(ip_text)
            rede = ipaddress.ip_network(rede_text, strict=False)

            if ip in rede:
                resultado.value = f"✅ O IP {ip} pertence à rede {rede}."
                resultado.color = ft.Colors.GREEN_600
            else:
                resultado.value = f"❌ O IP {ip} NÃO pertence à rede {rede}."
                resultado.color = ft.Colors.RED_600

        except ValueError as err:
            resultado.value = f"⚠️ Erro: {err}"
            resultado.color = ft.Colors.ORANGE_700

        page.update()

    # Botão
    btn_verificar = ft.ElevatedButton(
        text="Verificar",
        icon=ft.Icons.SEARCH,
        bgcolor=ft.Colors.BLUE_600,
        color=ft.Colors.WHITE,
        on_click=verificar_ip,
        width=200,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=12))
    )

    # Card central
    card = ft.Container(
        content=ft.Column(
            [
                ft.Text("Verificador de IP e Rede", size=22, weight=ft.FontWeight.BOLD),
                ft.Divider(),
                ip_field,
                rede_field,
                btn_verificar,
                ft.Divider(),
                resultado
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=15,
        ),
        padding=30,
        width=400,
        bgcolor=ft.Colors.WHITE,
        border_radius=16,
        shadow=ft.BoxShadow(
            spread_radius=1,
            blur_radius=10,
            color=ft.Colors.with_opacity(0.3, ft.Colors.BLACK),
            offset=ft.Offset(0, 3),
        ),
        alignment=ft.alignment.center,
    )

    # Adiciona o card à página
    page.add(card)

ft.app(target=main)
