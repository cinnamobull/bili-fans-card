from PIL import Image, ImageFont, ImageDraw
import requests

# settings
background_path = "background.png"
avatar_path = "avatar.png"
uname = ""


def get_avatar(uid: int):
    url = "https://api.bilibili.com/x/space/acc/info"
    params = {"mid": uid}
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"}
    resp = requests.get(url, params=params, headers=headers)
    # print(resp.text)
    # print(resp.status_code)
    data = resp.json()
    global uname
    global avatar_path
    uname = data["data"]["name"]
    avatar_url = data["data"]["face"]
    with open(avatar_path, "wb") as f:
        f.write(requests.get(avatar_url).content)
    print(f"你的名字是：{uname}")


if __name__ == "__main__":
    while True:
        try:
            uid = int(input("uid: "))
            get_avatar(uid)
            break
        except Exception as e:
            print(e)
            print("出错了🥺")

    while True:
        try:
            fans_no = input("fans_no: ")
            break
        except Exception as e:
            print(e)
            print("出错了🥺")

    while True:
        try:
            date = input("date: ")
            break
        except Exception as e:
            print(e)
            print("出错了🥺")

    font_number = ImageFont.truetype("font/FFF_Planeta.ttf", 75)
    font_DATE = ImageFont.truetype("font/agentdb-normal.ttf", 44)
    font_date = ImageFont.truetype("font/HarmonyOSHans-400.ttf", 42)
    font_uname = ImageFont.truetype("font/HarmonyOSHans-400.ttf", 45)

    # read background image
    background = Image.open(background_path)
    if background.mode != "RGBA":
        background = background.convert("RGBA")
    if background.size != (1256, 514):
        background = background.resize((1256, 514))

    # read avatar image
    avatar = Image.open(avatar_path)
    if avatar.mode != "RGBA":
        avatar = avatar.convert("RGBA")
    if avatar.size != (80, 80):
        avatar = avatar.resize((80, 80))

    # write
    write = Image.new("RGBA", background.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(write)

    # write "FANS NO." "DATE"
    draw.text((45, 199), "FANS NO.", fill="#ffffff7f", font=font_DATE)
    draw.text((45, 392), "DATE", fill="#ffffff7f", font=font_DATE)

    # wrtie date
    draw.text((45, 450), date, fill="#ffffffff", font=font_date)

    # write fans number
    for i, n in enumerate(fans_no):
        draw.text((49 + i * 50, 253), n, fill="#ffffffff", font=font_number)

    # write uname
    draw.text((160, 65), uname, fill="#ffffffff", font=font_uname)

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

    # save
    # composite
    writed = Image.alpha_composite(background, write)
    write.save("write.png")
    writed.save("output.png")
