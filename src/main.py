import flet as ft
import prototype as pt
import pageHandler as ph


def main(page: ft.Page):
    
    stackContent = ft.Stack(
        expand = True,
        controls=[],
    )
    
    page.add(
        ft.SafeArea(
            expand=True,
            content=ft.Container(
                alignment=ft.Alignment.CENTER,
                bgcolor = ft.Colors.BLACK,
                content = stackContent,
            ),
        ),
    )

    stackContent.controls.append(ph.make_redbox(0,0))
    stackContent.update()

    def increment_click(e: ft.Event[ft.FloatingActionButton]):
        stackContent.controls.append(ph.make_redbox(60,60))
        stackContent.update()

    page.floating_action_button = ft.FloatingActionButton(
            icon=ft.Icons.ADD, key="increment", on_click=increment_click
    )



if __name__ == "__main__":
    ft.run(main)
