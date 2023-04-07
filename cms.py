import random
import sqlite3
conn = sqlite3.connect("tovary.db")
cur = conn.cursor()
lines = []
inp = open('index.html',"w")
inp.write("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style.css">
    <title>Барахолка</title>
</head>
<body>
    <div class="menu"><a class="menuA" href="index.html">Главная</a><a class="menuA" href="shopping.html">Корзина</a><a class="menuA"href="about.html">О нас</a></div>
    <div>
        <table>
            <tr>
                <td>
""")
for row in cur.execute("SELECT * from Tovary"):
    lines.append(row)
for line in lines:
    res = f"""<table class="table{random.randint(1,4)}">
    <tr>
        <td rowspan="3">
            <h3><a class ="tovary" href = "#">{line[0]}</a></h3>
            <img src="{line[1]}" width = 300>
        </td>
        <td>
            <p style="font-size: 40px;color:rgb(164, 0, 0);">{line[2]} р.</p>
            <button>В корзину</button>
        </td>
    </tr>
</table>
"""
    inp.write(res)
footh = """</td>
<td>
<h1 style="margin-left: 300px;">Категории</h1>
<div class = "filter" style="margin-left: 300px;">
<div>
<a href="">Мышки</a><br><a href="">Чехлы</a><br><a href="">Пульты</a><br><a href="">Arduino</a><br><a href="">Компьтеры</a><br><a href="">Телефоны</a><br><a href="">Кнопочные телефоны</a><br><a href="">Акамуляторы</a><br><a href="">Часы</a><br><a href="">Сломанное</a><br><a href="">Другое</a>
</div>
</div>
</td>
</tr>
</table>
</div>
</body>
</html>
"""
inp.write(footh)