import telegram

chat_token = "5943714466:AAEr3JxRxzrEJRsgoJFi_ybzPZpFXM8TWjI"
# chat_token = "HTTP API"
bot = telegram.Bot(token = chat_token)
text = '안녕하세요'
bot.sendMessage(chat_id = "5834271658", text=text)