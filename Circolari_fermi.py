# stampa di debug con orario
import datetime
# tempo usato nel loop
import time
# utilizzati per ricevere codice
import requests
from bs4 import BeautifulSoup
# cose di telegram
from telegram import update
from telegram.ext import Updater, CommandHandler
from telegram import ParseMode
import bs4
import emoji

newspaper = emoji.emojize(':newspaper:')
label = emoji.emojize(':label:')
clipboard = emoji.emojize(':clipboard:')
linkemoji = emoji.emojize(':link:')

# tokenbot
TOKEN = 'replacewithtoken'
chatid = '@replacewithchatid'
url = "https://www.itisfermi.edu.it/comunicazioni"

def start(update, context):
    while True:
        response = requests.get(url)
        response.raise_for_status()
        soup = bs4.BeautifulSoup(response.text, 'html.parser')
        contenuto = soup.find('div', class_="main-content page-content")
        A = contenuto.find_all('a')
        f = open('circolarifermi.txt', 'a')
        old_circolari = [riga.rstrip('\n') for riga in open('circolarifermi.txt')]
        verifica=0
    #prendo i link e li metto in href
        for link in A:
            links = (link.get('href'))
            if links  not in old_circolari:
                f.write('%s\n' % links)
                titolo = (link.get('title'))
                context.bot.send_message(chat_id=chatid, disable_web_page_preview=True,
                                         parse_mode=ParseMode.HTML,
                                         text= newspaper+ " "+ titolo + '\n' + linkemoji + " " + '<a href="' + links + '">' 'Link della circolare</a>')
                verifica=1
                time.sleep(2)


        if verifica == 0:
            print("nessuna nuova circolare al momento...")


        f.close()
        time.sleep(60)

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))

    # Start bot
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()










