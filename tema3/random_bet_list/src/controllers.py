from src.templates import render_template
from src.models.data import GAMEDAYS
import random


def home(environ: dict) -> str:
    return render_template("src/views/index.html")


def gamedays(environ: dict) -> str:
    list_show: str = "<ul>"

    for game in GAMEDAYS:
        list_show += f"<li> <a href='gamedays/?n={str(game['gameday'])}'>Jornada {str(game['gameday'])}</li>"

    list_show += "</ul>"

    context: dict[str, str] = {
        "gamedays_list": list_show
    }
    return render_template("src/views/gamedays.html", context)


def randombetlist(environ: dict) -> str:
    pronostico_elem: list[int, str] = [1, "X", 2]
    team1: str = ""
    team2: str = ""

    table: str = "<td>"

    game1: str = team1 + team2

    table += game1

    table += "</td>"

    context: dict[str, str] = {
        "gameday_number": 18,
        "game1": "<td>" + GAMEDAYS[-1]["games"][0]["team1"] + "</td>" + "<td>"
        + GAMEDAYS[-1]["games"][0]["team2"] + "</td>" + "<td>" +
        str(pronostico_elem[random.randint(0, 2)]) + "</td>",

        "game2": "<td>" + GAMEDAYS[-1]["games"][1]["team1"] + "</td>" + "<td>"
        + GAMEDAYS[-1]["games"][1]["team2"] + "</td>" + "<td>" +
        str(pronostico_elem[random.randint(0, 2)]) + "</td>",

        "game3": "<td>" + GAMEDAYS[-1]["games"][2]["team1"] + "</td>" + "<td>"
        + GAMEDAYS[-1]["games"][2]["team2"] + "</td>" + "<td>" +
        str(pronostico_elem[random.randint(0, 2)]) + "</td>",

        "game4": "<td>" + GAMEDAYS[-1]["games"][3]["team1"] + "</td>" + "<td>"
        + GAMEDAYS[-1]["games"][3]["team2"] + "</td>" + "<td>" +
        str(pronostico_elem[random.randint(0, 2)]) + "</td>",

        "game5": "<td>" + GAMEDAYS[-1]["games"][4]["team1"] + "</td>" + "<td>"
        + GAMEDAYS[-1]["games"][4]["team2"] + "</td>" + "<td>" +
        str(pronostico_elem[random.randint(0, 2)]) + "</td>"
    }

    return render_template("src/views/randombetlist.html", context)
