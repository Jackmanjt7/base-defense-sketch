import flet as ft
import prototype as pt


def handle_pan_update(e: ft.DragUpdateEvent[ft.GestureDetector]):
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
            on_pan_update=handle_pan_update,
        ),
    )