import re

pattern = re.compile(r"^[\.-]+(\|\|[\.-]+)*(\|\|\|\|[\.-]+(\|\|[\.-]+)*)*$")

alpha = {
    ".-": "a",
    "-...": "b",
    "-.-.": "c",
    "-..": "d",
    ".": "e",
    "..-.": "f",
    "--.": "g",
    "....": "h",
    "..": "i",
    ".---": "j",
    "-.-": "k",
    ".-..": "l",
    "--": "m",
    "-.": "n",
    "---": "o",
    ".--.": "p",
    "--.-": "q",
    ".-.": "r",
    "...": "s",
    "-": "t",
    "..-": "u",
    "...-": "v",
    ".--": "w",
    "-..-": "x",
    "-.--": "y",
    "--..": "z",
    "||": "",
    "": " ",
}


def translate(code: str):
    if not bool(pattern.match(code)):
        raise Exception("Invalid Morse Code!")

    return "".join(alpha.get(x, f" UNK {x} ") for x in code.split("||"))
