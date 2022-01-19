from django.http import HttpResponse


def index(request):
    return HttpResponse('''
    <html>
    <head>
         <title>ОБЪЯВЛЕНИЕ</title>
    </head>
    <body>
    <p align=center><b>ПРОПАЛ КОТ</b></p>
    <br>
    <p align=center>
    <img src="https://avatars.mds.yandex.net/i?id=94901e2511a39b823d0f92546e761871-5482341-images-thumbs&n=13&exp=1"></p>
    <br>
    <p align=center>Зовут Фрэнк. Пропал вчера вечером в районе ул. Николая Ершова (ЖК Арт-сити). Большая просьба, 
    если вы видели кота или смогли его поймать, позвоните по номеру +7(987)-222-00-00. </p>
    <p align=center>Очень надеемся на возвращение любимца домой!</p>
    <br>
    <p align=center><b>ВОЗНАГРАЖДЕНИЕ</b></p>
    </body>
    </html>    
    ''')
