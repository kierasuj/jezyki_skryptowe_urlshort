from .health import health_router
from .shortener import shortener_router

all_blueprints = [
    health_router,
    shortener_router
]