from os import path
from random import randint
from subprocess import run

import screeninfo
from PIL import Image

monitors = screeninfo.get_monitors()
WIDTH, HEIGHT = max([m.width for m in monitors]), max([m.height for m in monitors])

colour = "#" + str(hex(randint(0, 65535)))[2:]

background = Image.new(mode="RGB", size=(WIDTH, HEIGHT), color=colour)
background.save("background.jpg")

p = path.abspath("./background.jpg")

run(f"gsettings set org.gnome.desktop.background picture-uri file://{p}".split())
run(f"gsettings set org.gnome.desktop.background picture-uri-dark file://{p}".split())
