import telebot

from main import *

bot = telebot. TeleBot(TOKEN)

@bot.message_handler(content_types=['text'])

def text(message):
     if message.text == "Королева слез":
         bot.send_message(message.from_user.id, "Жанр : романтика, год выпуска : 2024, кол.серий : 16")
     elif message.text == "Потомки солнца ":
         bot.send_message(message.from_user.id, " Жанры:  Романтика, драма, комедия"
                                                " Главные герои:  Чон Чжихён, Ким Хёнжу"
                                                "Год выпуска:  2015"
                                                "Количество серий:  16"
                                                "Рейтинг:  8.3/10 (MyDramaList)")
     elif message.text == "Истинная красота":
         bot.send_message(message.from_user.id, "Жанры	Роман,Комедия,Драма,Ломтик жизни:"
                                                "В главных ролях	Мун Га Ён,Чха Ын У,Хван Ин Ёп,Пак Ю На:"
                                                "Число серий	16:"
                                                "Страна	 Республика Корея,Язык	корейский")

     elif message.text == "Мое имя":
         bot.send_message(message.from_user.id, "Жанры: Боевик, Драма, Приключения, Триллер, Детективный фильм, криминальный жанр:"
                                                "Количество серий: 8:"
                                                " В ролях: Хан Соки , Пан Хикон:"
                                                "Страна	 Республика Корея")
     elif message.text == "Силочка До Бон Сун":
         bot.send_message(message.from_user.id, "Жанры	Роман,Комедия,Драма,:"
                                                "Количество серий:  16;"
                                                " В ролях: Ким Син Ю , Ли МИн Хо;"
                                                "Рейтинг:  8.3/10 (MyDramaList)")


bot.infinity_polling()