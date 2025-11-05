import reflex as rx
from app.state import AppState


def footer() -> rx.Component:
    return rx.el.footer(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.icon("paint_roller", class_name="h-6 w-6 text-emerald-500"),
                    rx.el.span("PaintCo", class_name="text-xl font-bold text-gray-800"),
                    class_name="flex items-center gap-2",
                ),
                rx.el.p(
                    "Servicios de pintura de calidad para hogares y oficinas.",
                    class_name="text-gray-500 mt-2",
                ),
            ),
            rx.el.div(
                rx.el.p(
                    "© 2024 PaintCo. Todos los derechos reservados.",
                    class_name="text-sm text-gray-500",
                ),
                rx.el.div(
                    rx.foreach(
                        AppState.social_links,
                        lambda link: rx.el.a(
                            rx.icon(link["icon"], class_name="h-5 w-5"),
                            href=link["href"],
                            class_name="text-gray-400 hover:text-emerald-500 transition-colors",
                        ),
                    ),
                    class_name="flex items-center gap-4 mt-4 md:mt-0",
                ),
                class_name="flex flex-col md:flex-row items-center justify-between mt-8 pt-8 border-t border-gray-100",
            ),
            class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12",
        ),
        class_name="w-full bg-white",
    )