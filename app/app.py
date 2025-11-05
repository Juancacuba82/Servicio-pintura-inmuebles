import reflex as rx
from app.state import AppState
from app.components.header import header
from app.components.footer import footer
from app.components.gallery import gallery_section
from app.components.testimonials import testimonials_section
from app.components.quote_calculator import quote_calculator_section


def hero_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.h1(
                    "Pintura Profesional,",
                    rx.el.span(
                        " Resultados Impecables.", class_name="text-emerald-500"
                    ),
                    class_name="text-4xl md:text-6xl font-extrabold text-gray-800 tracking-tighter leading-tight",
                ),
                rx.el.p(
                    "Dale nueva vida a tu espacio con nuestros servicios de pintura expertos. Ofrecemos calidad que puedes ver y un acabado que dura.",
                    class_name="mt-6 text-lg text-gray-600 max-w-2xl",
                ),
                rx.el.div(
                    rx.el.a(
                        "Solicita una Cotización Gratis",
                        rx.icon("arrow-right", class_name="ml-2"),
                        href="#quote",
                        class_name="flex items-center bg-emerald-500 text-white px-8 py-4 rounded-xl font-bold text-lg hover:bg-emerald-600 transition-all duration-300 transform hover:scale-105 shadow-lg",
                    ),
                    class_name="mt-10 flex gap-4",
                ),
            ),
            rx.el.div(
                rx.el.image(
                    src="/placeholder.svg",
                    class_name="rounded-2xl shadow-2xl object-cover w-full h-full",
                ),
                class_name="hidden lg:block w-full max-w-lg",
            ),
            class_name="flex flex-col lg:flex-row items-center justify-between gap-12 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-20 md:py-32",
        ),
        class_name="bg-gray-50",
    )


def service_card(service: rx.Var[dict]) -> rx.Component:
    return rx.el.div(
        rx.icon(service["icon"], class_name="h-10 w-10 text-emerald-500 mb-4"),
        rx.el.h3(service["title"], class_name="text-xl font-bold text-gray-800 mb-2"),
        rx.el.p(service["description"], class_name="text-gray-600"),
        class_name="bg-white p-8 rounded-2xl border border-gray-100 shadow-sm hover:shadow-lg hover:-translate-y-1 transition-all duration-300",
    )


def services_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.h2(
                "Nuestros Servicios",
                class_name="text-3xl md:text-4xl font-bold text-gray-800 tracking-tight text-center",
            ),
            rx.el.p(
                "Desde una sola habitación hasta un edificio comercial completo, lo tenemos cubierto.",
                class_name="mt-4 text-lg text-gray-600 max-w-3xl mx-auto text-center",
            ),
            rx.el.div(
                rx.foreach(AppState.services, service_card),
                class_name="mt-16 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8",
            ),
            class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-20 md:py-28",
        ),
        id="services",
        class_name="bg-white",
    )


def index() -> rx.Component:
    return rx.el.main(
        header(),
        hero_section(),
        services_section(),
        gallery_section(),
        testimonials_section(),
        quote_calculator_section(),
        footer(),
        class_name="font-['Lora'] bg-white",
    )


app = rx.App(
    theme=rx.theme(appearance="light"),
    head_components=[
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(rel="preconnect", href="https://fonts.gstatic.com", cross_origin=""),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Lora:wght@400;500;600;700&display=swap",
            rel="stylesheet",
        ),
    ],
)
app.add_page(index)