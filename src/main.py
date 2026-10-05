import flet as ft
import prototype as pt


def main(page: ft.Page):
    
    def handle_pan_update1(e: ft.DragUpdateEvent[ft.GestureDetector]):
        container = e.control.parent
        container.top = max(0.0, container.top + e.local_delta.y)
        container.left = max(0.0, container.left + e.local_delta.x)
        container.update()

    def make_redbox(x,y):
        return ft.Container(
            width=50,
            height=50,
            left=x,
            top=y,
            bgcolor=ft.Colors.RED,
            border_radius = 5,
            content=ft.GestureDetector(
                mouse_cursor = ft.MouseCursor.MOVE,
                drag_interval=10,
                on_pan_update=handle_pan_update1,
            ),
        )
    
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

    stackContent.controls.append(make_redbox(0,0))
    stackContent.update()

    def increment_click(e: ft.Event[ft.FloatingActionButton]):
        stackContent.controls.append(make_redbox(60,60))
        stackContent.update()

    page.floating_action_button = ft.FloatingActionButton(
            icon=ft.Icons.ADD, key="increment", on_click=increment_click
    )



if __name__ == "__main__":
    ft.run(main)
