from typing import Callable, Iterator
from src.controllers import home, gamedays, randombetlist
from src.templates import render_template


def app(environ: dict, start_response: Callable) -> Iterator:
    
    path: str = environ.get("PATH_INFO")

    if path.endswith("/"):
        path = path[:-1]

    if path == "" or path == "/index":
        data: str = home(environ)
    elif path == "/gamedays":
        data: str = gamedays(environ)
    elif path == "/randombetlist":
        data: str = randombetlist(environ)
    else:
        data: str = render_template("src/views/404.html")

    data_in_bytes: bytes = data.encode("utf-8")

    start_response(
        "200 OK",
        [
            ("Content-Type", "text/html"),
            ("Content-Length", str(len(data_in_bytes)))
        ]
    )

    return iter([data_in_bytes])
