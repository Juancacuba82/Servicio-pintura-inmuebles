import reflex as rx
from app.state import AppState


def form_field(
    label: str,
    placeholder: str,
    input_type: str,
    name: str,
    value: rx.Var,
    on_change: rx.event.EventHandler,
) -> rx.Component:
    return rx.el.div(
        rx.el.label(label, class_name="block text-sm font-medium text-gray-700 mb-1"),
        rx.el.input(
            placeholder=placeholder,
            type=input_type,
            name=name,
            default_value=value,
            on_change=on_change,
            class_name="w-full px-4 py-2 rounded-lg border border-gray-300 focus:ring-emerald-500 focus:border-emerald-500 transition-shadow",
            required=True,
        ),
        class_name="w-full",
    )


def checkbox_field(
    label: str, name: str, is_checked: rx.Var, on_change: rx.event.EventHandler
) -> rx.Component:
    return rx.el.label(
        rx.el.input(
            type="checkbox",
            name=name,
            checked=is_checked,
            on_change=on_change,
            class_name="h-4 w-4 text-emerald-600 border-gray-300 rounded focus:ring-emerald-500 mr-2",
        ),
        label,
        class_name="flex items-center text-sm font-medium text-gray-700",
    )


def quote_calculator_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.h2(
                    "Obtenga una Cotización al Instante",
                    class_name="text-3xl md:text-4xl font-bold text-gray-800 tracking-tight",
                ),
                rx.el.p(
                    "Complete el formulario a continuación para obtener una estimación en tiempo real para su proyecto de pintura.",
                    class_name="mt-4 text-lg text-gray-600",
                ),
                rx.cond(
                    AppState.quote_submitted,
                    rx.el.div(
                        rx.icon(
                            "check_check", class_name="h-12 w-12 text-green-500 mx-auto"
                        ),
                        rx.el.h3(
                            "¡Gracias!",
                            class_name="mt-4 text-2xl font-semibold text-center text-gray-800",
                        ),
                        rx.el.p(
                            "Su solicitud de cotización ha sido enviada. Nos pondremos en contacto en breve.",
                            class_name="mt-2 text-center text-gray-600",
                        ),
                        rx.el.button(
                            "Iniciar una Nueva Cotización",
                            on_click=AppState.reset_quote_form,
                            class_name="mt-6 w-full bg-emerald-500 text-white px-6 py-3 rounded-lg font-semibold hover:bg-emerald-600 transition-all",
                        ),
                        class_name="w-full p-8 text-center",
                    ),
                    rx.el.form(
                        rx.el.div(
                            form_field(
                                "Nombre Completo",
                                "John Doe",
                                "text",
                                "customer_name",
                                AppState.customer_name,
                                AppState.set_customer_name,
                            ),
                            form_field(
                                "Dirección de Correo Electrónico",
                                "usted@ejemplo.com",
                                "email",
                                "customer_email",
                                AppState.customer_email,
                                AppState.set_customer_email,
                            ),
                            form_field(
                                "Número de Teléfono (Opcional)",
                                "(555) 123-4567",
                                "tel",
                                "customer_phone",
                                AppState.customer_phone,
                                AppState.set_customer_phone,
                            ),
                            rx.el.div(
                                rx.el.label(
                                    "Tipo de Servicio",
                                    class_name="block text-sm font-medium text-gray-700 mb-1",
                                ),
                                rx.el.select(
                                    rx.el.option("Pintura Interior", value="interior"),
                                    rx.el.option("Pintura Exterior", value="exterior"),
                                    rx.el.option(
                                        "Pintura Comercial", value="commercial"
                                    ),
                                    default_value=AppState.service_type,
                                    on_change=AppState.set_service_type,
                                    name="service_type",
                                    class_name="w-full px-4 py-2 rounded-lg border border-gray-300 focus:ring-emerald-500 focus:border-emerald-500",
                                ),
                            ),
                            form_field(
                                "Metros Cuadrados Totales",
                                "ej., 150",
                                "number",
                                "square_footage",
                                AppState.square_footage,
                                AppState.set_square_footage,
                            ),
                            form_field(
                                "Número de Habitaciones",
                                "ej., 3",
                                "number",
                                "num_rooms",
                                AppState.num_rooms,
                                AppState.set_num_rooms,
                            ),
                            rx.el.div(
                                rx.el.label(
                                    "Servicios Adicionales",
                                    class_name="block text-sm font-medium text-gray-700 mb-2",
                                ),
                                rx.el.div(
                                    checkbox_field(
                                        "Pintura de Techos",
                                        "include_ceiling",
                                        AppState.include_ceiling,
                                        AppState.toggle_include_ceiling,
                                    ),
                                    checkbox_field(
                                        "Pintura de Molduras y Zócalos",
                                        "include_trim",
                                        AppState.include_trim,
                                        AppState.toggle_include_trim,
                                    ),
                                    checkbox_field(
                                        "Restauración de Gabinetes",
                                        "include_cabinets",
                                        AppState.include_cabinets,
                                        AppState.toggle_include_cabinets,
                                    ),
                                    class_name="space-y-2",
                                ),
                                class_name="col-span-1 md:col-span-2",
                            ),
                            class_name="grid grid-cols-1 md:grid-cols-2 gap-6",
                        ),
                        rx.el.button(
                            "Enviar Solicitud",
                            type="submit",
                            class_name="mt-8 w-full bg-emerald-500 text-white px-6 py-3 rounded-lg font-semibold hover:bg-emerald-600 transition-all disabled:bg-gray-400 disabled:cursor-not-allowed",
                            disabled=~AppState.is_form_valid,
                        ),
                        on_submit=AppState.submit_quote_request,
                        reset_on_submit=False,
                        class_name="mt-8 space-y-6",
                    ),
                ),
                class_name="w-full lg:w-1/2",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.h3(
                        "Costo Estimado",
                        class_name="text-xl font-semibold text-gray-800",
                    ),
                    rx.el.p(
                        "Su estimación de proyecto en tiempo real:",
                        class_name="text-gray-500",
                    ),
                    rx.el.p(
                        rx.el.span("$"),
                        AppState.estimated_cost.to_string(),
                        class_name="text-5xl font-extrabold text-emerald-600 mt-4",
                    ),
                    rx.el.p(
                        "Esta es una estimación. Se proporcionará una cotización final después de una consulta.",
                        class_name="text-xs text-gray-500 mt-2",
                    ),
                    class_name="bg-white p-8 rounded-2xl shadow-lg border border-gray-100 text-center",
                ),
                class_name="w-full lg:w-2/5 mt-12 lg:mt-0",
            ),
            class_name="max-w-7xl mx-auto flex flex-col lg:flex-row items-start justify-between gap-16",
        ),
        id="quote",
        class_name="px-4 sm:px-6 lg:px-8 py-20 md:py-28 bg-white",
    )