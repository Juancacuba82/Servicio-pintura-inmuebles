import reflex as rx
from app.state import AppState


def testimonial_card(testimonial: rx.Var[dict]) -> rx.Component:
    return rx.el.div(
        rx.el.blockquote(
            f'''"{testimonial["quote"]}"''',
            class_name="text-gray-700 italic mb-6 leading-relaxed",
        ),
        rx.el.div(
            rx.el.image(
                src=f"https://api.dicebear.com/9.x/notionists/svg?seed={testimonial['avatar_seed']}",
                class_name="h-12 w-12 rounded-full object-cover",
            ),
            rx.el.div(
                rx.el.p(testimonial["author"], class_name="font-bold text-gray-800"),
                rx.el.p(testimonial["title"], class_name="text-sm text-gray-500"),
            ),
            class_name="flex items-center gap-4 mt-auto pt-4 border-t border-gray-100",
        ),
        class_name="bg-white p-8 rounded-2xl border border-gray-100 shadow-sm flex flex-col h-full hover:shadow-lg hover:-translate-y-1 transition-all duration-300",
    )


def testimonials_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.h2(
                "Lo que Dicen Nuestros Clientes",
                class_name="text-3xl md:text-4xl font-bold text-gray-800 tracking-tight text-center",
            ),
            rx.el.p(
                "Historias reales de clientes satisfechos.",
                class_name="mt-4 text-lg text-gray-600 max-w-3xl mx-auto text-center",
            ),
            rx.el.div(
                rx.foreach(AppState.testimonials, testimonial_card),
                class_name="mt-16 grid grid-cols-1 lg:grid-cols-3 gap-8",
            ),
            class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-20 md:py-28",
        ),
        class_name="bg-white",
    )