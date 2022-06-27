# 哔哩哔哩装扮粉丝牌生成

## TODO

头图还没整，就是对着样例一点一点调参数，今天没时间。

## 注意

`psd/` 下的文件来自 [火花狐狸](https://space.bilibili.com/236165593) 佬。

`agentdb-normal.ttf` 和 `FFF_Planeta.ttf` 不能商用。
## 使用方法

修改 `main.py` 里的设置：

```py
# 背景图片路径，要求分辨率 1256x514 （是哔哩哔哩生成卡片的大小）
# 分辨率不符合的会被拉伸
background_path = "img/background.png"
# 粉丝编号
fans_no = "000001"
# 日期
date = "2022/06/27"
# 头像路径，要求分辨率 80x80
# 分辨率不符合的会被拉伸
avatar_path = "img/a.png"
# 用户名
uname = "啵啵小堂"
```

然后 `python main.py` 就好了，需要安装 `pillow` 库。

## 生成结果

两张图片，一张包含透明通道的，只有文字的图片，可以随便加背景；另一张是和背景混合的图片，可以直接用。

**这张图字是白的，可能看不见**

![](img/example1.png)

![](img/example2.png)

## 在线版

- 安装 `FastAPI` 和 `uvicorn` 服务，参见[这里](https://cloud.tencent.com/developer/article/1601020)
- 在根目录下执行 `uvicorn.exe server:app`
- 浏览器打开地址`http://127.0.0.1:8000/getCard?uid=<卡片申请人UID>&fans_no=<粉丝编号>`即可看到生成的图片
