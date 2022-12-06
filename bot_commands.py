from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from spy import *
import datetime
import f_la


f1 = []
f2 = []


async def hl_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'Находим сумму многочленов\nвводим 1-ую формулу без пробелов\n например:\n/polin1 4x^3+5x^2+6x=0\n затем после приглашения вторую\n например:\n/polin2 7x^4+8x^3+9x+10=0 ')


async def pl1_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global f1
    log(update, context)
    msg = update.message.text
    data = msg.split()
    f1 = f_la.splt(data[1])  # функция обработки сроки, Убрали +^
    await update.message.reply_text(f'Введите вторую формулу')


async def pl2_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    msg = update.message.text
    data = msg.split()
    f2 = f_la.splt(data[1])  # функция обработки сроки, Убрали +^

    # функция обработки сроки в int, 0-й элемент степень
    f11 = f_la.int_str(f1)
    f21 = f_la.int_str(f2)
    a1 = f11[0]
    a2 = f21[0]
    itof_str = []
    if a1 >= a2:
        itof_str = f_la.sum_str(f11, f21, a1, a2)
        count = a1
    else:
        itof_str = f_la.sum_str(f21, f11, a2, a1)
        count = a2
    res = f_la.formula(itof_str, count)

    print(res)
    await update.message.reply_text(f'Получите: {res}')
