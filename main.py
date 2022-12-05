#Прикрутить бота сложения многочлена к телекграмм

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *


app = ApplicationBuilder().token(
    "5523430859:AAHuelCE7_4qoAgn3t-YfHuxij5Qhc6KzAs").build()

app.add_handler(CommandHandler('polin1', pl1_command))
app.add_handler(CommandHandler('polin2', pl2_command))
app.add_handler(CommandHandler('help', hl_command))



print('server start')
app.run_polling()
