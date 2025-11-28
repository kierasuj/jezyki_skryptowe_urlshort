from flask import Blueprint
from controllers.shortener_controller import (
    get_url,
    save_url,
)

shortener_router = Blueprint("url", __name__)

@shortener_router.get("/url/<path:id>")
def get_shortened_url(id: str):
    url = get_url(id)
    return {"shortened_url": f"http://short.url/{url}"}, 200


@shortener_router.post("/url")
def create_shortened_url():
    save_url
    return {"shortened_url": "http://short.url/abc123"}, 201

@shortener_router.delete("/url/<path:url>")
def delete_shortened_url(url: str):
    
    return {"message": f"Shortened URL for {url} deleted"}, 200

@shortener_router.post("/url/<path:url>/custom")
def create_custom_shortened_url(url: str):
    
    return {"shortened_url": f"http://short.url/{url}"}, 201