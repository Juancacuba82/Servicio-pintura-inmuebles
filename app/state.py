import reflex as rx
from typing import TypedDict


class NavItem(TypedDict):
    name: str
    href: str


class Service(TypedDict):
    icon: str
    title: str
    description: str


class SocialLink(TypedDict):
    icon: str
    href: str


class GalleryImage(TypedDict):
    src: str
    tag: str
    tag_display: str
    title: str


class Testimonial(TypedDict):
    quote: str
    author: str
    title: str
    avatar_seed: str


class AppState(rx.State):
    nav_items: list[NavItem] = [
        {"name": "Servicios", "href": "#services"},
        {"name": "Galería", "href": "#gallery"},
        {"name": "Cotización", "href": "#quote"},
        {"name": "Contacto", "href": "#"},
    ]
    services: list[Service] = [
        {
            "icon": "home",
            "title": "Pintura Residencial",
            "description": "Transforme su hogar con nuestros expertos servicios de pintura interior y exterior. Tratamos cada hogar como si fuera el nuestro.",
        },
        {
            "icon": "building",
            "title": "Pintura Comercial",
            "description": "Pintura profesional, confiable y eficiente para oficinas, locales comerciales y propiedades de todo tamaño.",
        },
        {
            "icon": "brush",
            "title": "Restauración de Gabinetes",
            "description": "Dé a su cocina o baño una renovación impresionante sin el costo de una remodelación completa. Un nuevo aspecto para sus gabinetes.",
        },
        {
            "icon": "droplet",
            "title": "Teñido de Terrazas y Cercas",
            "description": "Proteja y embellezca sus estructuras de madera exteriores con nuestros servicios de teñido y sellado de alta calidad.",
        },
    ]
    social_links: list[SocialLink] = [
        {"icon": "facebook", "href": "#"},
        {"icon": "instagram", "href": "#"},
        {"icon": "twitter", "href": "#"},
    ]
    gallery_images: list[GalleryImage] = [
        {
            "src": "/placeholder.svg",
            "tag": "Residential",
            "tag_display": "Residencial",
            "title": "Sala de Estar Moderna",
        },
        {
            "src": "/placeholder.svg",
            "tag": "Commercial",
            "tag_display": "Comercial",
            "title": "Oficina Corporativa",
        },
        {
            "src": "/placeholder.svg",
            "tag": "Interior",
            "tag_display": "Interior",
            "title": "Dormitorio Acogedor",
        },
        {
            "src": "/placeholder.svg",
            "tag": "Exterior",
            "tag_display": "Exterior",
            "title": "Exterior de Casa Suburbana",
        },
        {
            "src": "/placeholder.svg",
            "tag": "Residential",
            "tag_display": "Residencial",
            "title": "Cocina Renovada y Luminosa",
        },
        {
            "src": "/placeholder.svg",
            "tag": "Commercial",
            "tag_display": "Comercial",
            "title": "Frente de Tienda",
        },
        {
            "src": "/placeholder.svg",
            "tag": "Interior",
            "tag_display": "Interior",
            "title": "Comedor Elegante",
        },
        {
            "src": "/placeholder.svg",
            "tag": "Exterior",
            "tag_display": "Exterior",
            "title": "Teñido de Terraza y Patio",
        },
    ]
    testimonials: list[Testimonial] = [
        {
            "quote": "PaintCo hizo un trabajo increíble en nuestra sala de estar. La atención al detalle fue increíble y el equipo fue profesional y amable. ¡Muy recomendable!",
            "author": "Sara L.",
            "title": "Propietaria, Springfield",
            "avatar_seed": "Sarah",
        },
        {
            "quote": "El exterior de nuestro edificio de oficinas parece nuevo. El proyecto se completó a tiempo y dentro del presupuesto. No podríamos estar más contentos con los resultados.",
            "author": "David Chen",
            "title": "Gerente de Instalaciones, Innovate Inc.",
            "avatar_seed": "David",
        },
        {
            "quote": "Dudaba en restaurar los gabinetes de mi cocina, pero el equipo de PaintCo me guió en el proceso y el resultado es impresionante. ¡Es como una cocina nueva!",
            "author": "María García",
            "title": "Propietaria, Riverside",
            "avatar_seed": "Maria",
        },
    ]
    filter_tag: str = "All"

    @rx.var
    def filtered_gallery_images(self) -> list[GalleryImage]:
        if self.filter_tag == "All":
            return self.gallery_images
        return [img for img in self.gallery_images if img["tag"] == self.filter_tag]

    @rx.event
    def set_filter_tag(self, tag: str):
        self.filter_tag = tag

    customer_name: str = ""
    customer_email: str = ""
    customer_phone: str = ""
    service_type: str = "interior"
    square_footage: str = "1000"
    num_rooms: str = "1"
    include_ceiling: bool = False
    include_trim: bool = False
    include_cabinets: bool = False
    quote_submitted: bool = False

    @rx.event
    def toggle_include_ceiling(self, checked: bool):
        self.include_ceiling = checked

    @rx.event
    def toggle_include_trim(self, checked: bool):
        self.include_trim = checked

    @rx.event
    def toggle_include_cabinets(self, checked: bool):
        self.include_cabinets = checked

    @rx.var
    def is_form_valid(self) -> bool:
        return (
            bool(self.customer_name.strip())
            and bool(self.customer_email.strip())
            and str(self.square_footage).isdigit()
            and (int(self.square_footage) > 0)
            and str(self.num_rooms).isdigit()
            and (int(self.num_rooms) > 0)
        )

    @rx.var
    def estimated_cost(self) -> float:
        try:
            sq_ft = int(self.square_footage)
            rooms = int(self.num_rooms)
        except (ValueError, TypeError) as e:
            import logging

            logging.exception(f"Error: {e}")
            return 0.0
        base_rate_per_sq_ft = 2.5
        base_room_cost = 300
        cost = sq_ft * base_rate_per_sq_ft + rooms * base_room_cost
        if self.service_type == "commercial":
            cost *= 1.3
        elif self.service_type == "exterior":
            cost *= 1.2
        if self.include_ceiling:
            cost += 150 * rooms
        if self.include_trim:
            cost += 200 * rooms
        if self.include_cabinets:
            cost += 500
        return round(cost, 2)

    @rx.event
    def submit_quote_request(self, form_data: dict):
        print(f"Solicitud de cotización enviada: {form_data}")
        self.quote_submitted = True
        yield

    @rx.event
    def reset_quote_form(self):
        self.customer_name = ""
        self.customer_email = ""
        self.customer_phone = ""
        self.service_type = "interior"
        self.square_footage = "1000"
        self.num_rooms = "1"
        self.include_ceiling = False
        self.include_trim = False
        self.include_cabinets = False
        self.quote_submitted = False