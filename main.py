from card_generator import CardGenerator
from PIL import Image
import time

# settings
background_path = "img/background.png"
fans_no = 1
date = time.localtime()
avatar_path = "img/a.png"
uname = "啵啵小堂"

if __name__ == "__main__":
    # read background image
    background = Image.open(background_path)

    # read avatar image
    avatar = Image.open(avatar_path)

    write, writed = CardGenerator.getCard(background, avatar, date, fans_no, uname)

    write.save("write.png")
    writed.save("output.png")
