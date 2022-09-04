import telebot
import pandas as pd
from datetime import date

def find_birth():
    df = pd.read_csv("Devers 2022.csv")
    df = df[['NOME', 'ANIVERSARIO2022','EMAIL']]

    dia_hoje = date.today()
    dia_hoje = dia_hoje.strftime("%d/%m/%Y") #.replace('X0','X').replace('X','')

    aniversarios_hoje = df[df["ANIVERSARIO2022"] == dia_hoje]

    print("\n",aniversarios_hoje,"\n")

    aniversariantes = ''
    if len(aniversarios_hoje)>0:
        aniversariantes = "Aniversariantes do dia: "+ date.today().strftime("%d/%m/%Y")+"\n"
        for i in aniversarios_hoje["NOME"]:
            aniversariantes += "- "+ i + "\n"
    return aniversariantes

niver_hoje = find_birth()
print(niver_hoje)

if len(niver_hoje)== 0:
    niver_hoje = "Ninguém faz niver no dia: "+date.today().strftime("%d/%m/%Y")

token = ' '     # Token do bot
user_id = []   	# ID da(s)/do(s) pessoa(s)/grupo(s) no Telegram

bot = telebot.TeleBot(token)

msg_bot = niver_hoje

[bot.send_message(id, msg_bot) for id in user_id]
print("Bot enviou a mensagem")

