import random
import time
from typing import Optional
from fastapi import FastAPI
from PIL import Image
import aiohttp
from card_generator import CardGenerator
import io
from fastapi.responses import Response

app = FastAPI()

@app.on_event("startup")
def startup_event():
    global bobo_bg
    global session
    headers = {
        "Referer": "https://www.bilibili.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/83.0.4103.116 Safari/537.36"
    }
    bobo_bg = Image.open("img/background.png")
    session = aiohttp.ClientSession(headers=headers)

@app.get("/getCard")
async def getCard(uid: Optional[int] = 33605910, fans_no: Optional[int] = 0):
    global bobo_bg
    global session

    if fans_no <= 0 or fans_no >= 999999:
        fans_no = random.randint(1, 999999)
    try:
        async with session.get(
            'https://api.bilibili.com/x/space/acc/info',
            params={'mid':uid}) as res:
            res_json = await res.json()
            uname = res_json['data']['name']
            face_url = res_json['data']['face']
            async with session.get(face_url) as face_res:
                data = await face_res.content.read()
                face_data = io.BytesIO(data)
                face_img = Image.open(face_data)
                write, writed = CardGenerator.getCard(bobo_bg, face_img, time.localtime(), fans_no, uname)
                out_stream = io.BytesIO()
                writed.save(out_stream, format='PNG')
                return Response(content=out_stream.getvalue())
    except Exception as e:
        return {'err': f'无法获取数据，原因：{str(e)}'}
