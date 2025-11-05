import reflex as rx
from app.state import AppState


def filter_button(text: str, tag: str, current_filter: rx.Var[str]) -> rx.Component:
    return rx.el.button(
        text,
        on_click=lambda: AppState.set_filter_tag(tag),
        class_name=rx.cond(
            current_filter == tag,
            "bg-emerald-500 text-white font-semibold",
            "bg-gray-100 text-gray-700 hover:bg-gray-200 font-medium",
        ),
        style={
            "padding": "0.5rem 1.25rem",
            "borderRadius": "9999px",
            "transition": "all 0.2s",
        },
    )


def gallery_card(image: rx.Var[dict]) -> rx.Component:
    return rx.el.div(
        rx.el.image(
            src=image["src"],
            class_name="w-full h-64 object-cover group-hover:scale-105 transition-transform duration-300",
        ),
        rx.el.div(
            class_name="absolute inset-0 bg-black/20 group-hover:bg-black/40 transition-all duration-300"
        ),
        rx.el.div(
            rx.el.p(image["title"], class_name="font-bold text-white tracking-wide"),
            rx.el.span(
                image["tag_display"],
                class_name="bg-emerald-500/80 text-white text-xs font-semibold px-2 py-1 rounded-full",
            ),
            class_name="absolute bottom-0 left-0 p-4 flex flex-col items-start gap-2",
        ),
        class_name="relative rounded-2xl overflow-hidden group shadow-sm border border-gray-100",
    )


def gallery_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.h2(
                "Galería de Proyectos",
                class_name="text-3xl md:text-4xl font-bold text-gray-800 tracking-tight text-center",
            ),
            rx.el.p(
                "Una muestra de nuestro compromiso con la calidad y la artesanía.",
                class_name="mt-4 text-lg text-gray-600 max-w-3xl mx-auto text-center",
            ),
            rx.el.div(
                filter_button("Todos", "All", AppState.filter_tag),
                filter_button("Residencial", "Residential", AppState.filter_tag),
                filter_button("Comercial", "Commercial", AppState.filter_tag),
                filter_button("Interior", "Interior", AppState.filter_tag),
                filter_button("Exterior", "Exterior", AppState.filter_tag),
                class_name="mt-12 flex flex-wrap items-center justify-center gap-4",
            ),
            rx.el.div(
                rx.foreach(AppState.filtered_gallery_images, gallery_card),
                class_name="mt-12 grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-8",
            ),
            class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-20 md:py-28",
        ),
        id="gallery",
        class_name="bg-gray-50",
    )