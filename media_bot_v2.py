import telebot
import sqlite3
import config
from MediaCore.FileListing import FileListing, filesDict
from MediaCore.Parser import Parser, outDict
import MediaCore.Pdf as fileOut



bot = telebot.TeleBot(config.API)


@bot.message_handler(content_types=["text"])
def menu(message):

    parser = Parser()
    filelist = FileListing()
    numMessage = message.text
    bot.send_message(message.chat.id, "Выберите файл: " + '\n' + filelist.buildMessage())



    bot.send_message(message.chat.id, "Сканирую файл: " + message.text)


    parser.scan_file(int(message.text))


    # for key in outDict:
    #     messageOut = messageOut + key + ' - ' + outDict[key] + '\n'

    finalInfo = ''
    for key in outDict:
        finalInfo = (finalInfo + key + ': ' + outDict[key] + '\n')
    fileOut.generator(numMessage)
    bot.send_message(message.chat.id, finalInfo)
    fileName = filesDict[int(numMessage)]+'.pdf'
    fileOp = open(fileName, 'rb')
    bot.send_document(message.chat.id, fileOp)

    # finally:
    #     menu(message)


if __name__ == '__main__':
    bot.polling(none_stop=True)