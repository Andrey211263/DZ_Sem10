#Прикрутить бота сложения многочлена к телекграмм

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *


app = ApplicationBuilder().token(
    "token telegram").build()

app.add_handler(CommandHandler('polin1', pl1_command))
app.add_handler(CommandHandler('polin2', pl2_command))
app.add_handler(CommandHandler('help', hl_command))



print('server start')
app.run_polling()
