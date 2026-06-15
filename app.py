"""Minimal WSGI app that serves index.html, for use with gunicorn.

Run with:
    gunicorn app:app
"""

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INDEX_PATH = os.path.join(BASE_DIR, "index.html")


def app(environ, start_response):
    path = environ.get("PATH_INFO", "/")

    if path in ("/", "/index.html"):
        with open(INDEX_PATH, "rb") as f:
            body = f.read()
        start_response("200 OK", [
            ("Content-Type", "text/html; charset=utf-8"),
            ("Content-Length", str(len(body))),
        ])
        return [body]

    body = b"404 Not Found"
    start_response("404 Not Found", [
        ("Content-Type", "text/plain; charset=utf-8"),
        ("Content-Length", str(len(body))),
    ])
    return [body]
