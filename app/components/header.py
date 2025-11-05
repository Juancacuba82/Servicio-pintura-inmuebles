import reflex as rx
from app.state import AppState


def header() -> rx.Component:
    return rx.el.header(
        rx.el.div(
            rx.el.div(
                rx.icon("paint_roller", class_name="h-8 w-8 text-emerald-500"),
                rx.el.span(
                    "PaintCo",
                    class_name="text-2xl font-bold text-gray-800 tracking-tighter",
                ),
                class_name="flex items-center gap-2",
            ),
            rx.el.nav(
                rx.foreach(
                    AppState.nav_items,
                    lambda item: rx.el.a(
                        item["name"],
                        href=item["href"],
                        class_name="text-gray-600 hover:text-emerald-600 transition-colors font-medium",
                    ),
                ),
                class_name="hidden md:flex items-center gap-8",
            ),
            rx.el.div(
                rx.el.a(
                    "Obtener Cotización",
                    href="#quote",
                    class_name="hidden md:flex bg-emerald-500 text-white px-5 py-2 rounded-lg font-semibold hover:bg-emerald-600 transition-all duration-300 shadow-sm hover:shadow-md",
                ),
                rx.el.button(
                    rx.icon("menu", class_name="h-6 w-6"),
                    class_name="flex md:hidden bg-gray-100 p-2 rounded-md hover:bg-gray-200",
                ),
                class_name="flex items-center gap-4",
            ),
            class_name="flex items-center justify-between w-full max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4",
        ),
        class_name="w-full bg-white/80 backdrop-blur-md sticky top-0 z-50 border-b border-gray-100",
    )