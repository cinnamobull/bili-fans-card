from PIL import Image, ImageFont, ImageDraw
import time

class CardGenerator:
    font_number = ImageFont.truetype("font/FFF_Planeta.ttf", 75)
    font_DATE = ImageFont.truetype("font/agentdb-normal.ttf", 44)
    font_date = ImageFont.truetype("font/HarmonyOSHans-400.ttf", 42)
    font_uname = ImageFont.truetype("font/HarmonyOSHans-400.ttf", 45)

    @classmethod
    def getCard(cls: 'CardGenerator', background: Image, avatar: Image, date: time.struct_time, fans_no: int, uname: str):
        if background.mode != "RGBA":
            background = background.convert("RGBA")
        if background.size != (1256, 514):
            background = background.resize((1256, 514))

        if avatar.mode != "RGBA":
            avatar = avatar.convert("RGBA")
        if avatar.size != (80, 80):
            avatar = avatar.resize((80, 80))

        # write
        write = Image.new("RGBA", background.size, (255, 255, 255, 0))
        draw = ImageDraw.Draw(write)

        # write "FANS NO." "DATE"
        draw.text((45, 199), "FANS NO.", fill="#ffffff7f", font=cls.font_DATE)
        draw.text((45, 392), "DATE", fill="#ffffff7f", font=cls.font_DATE)

        # wrtie date
        draw.text((45, 450), time.strftime("%Y/%m/%d", date), fill="#ffffffff", font=cls.font_date)

        # write fans number
        num_remain = fans_no
        for i in range(6):
            num = int(num_remain % 10)
            draw.text((49 + (5 - i) * 50, 253), str(num), fill="#ffffffff", font=cls.font_number)
            num_remain = (num_remain - num) / 10

        # write uname
        draw.text((160, 65), uname, fill="#ffffffff", font=cls.font_uname)

        # write avatar
        avatar_back = Image.new("RGBA", (90*4, 90*4), (255, 255, 255, 0))
        draw = ImageDraw.Draw(avatar_back)
        draw.chord((0, 0, 90*4, 90*4), 0, 360, fill="#ffffffff")
        avatar_back = avatar_back.resize((90, 90))
        avatar_mask = Image.new("RGBA", avatar.size, (255, 255, 255, 0))
        draw = ImageDraw.Draw(avatar_mask)
        draw.chord((0, 0, 80, 80), 0, 360, fill="#ffffffff")
        write.paste(avatar_back, (45-5, 35-5), avatar_back)
        write.paste(avatar, (45, 35), avatar_mask)
        writed = Image.alpha_composite(background, write)
        return (write, writed)
