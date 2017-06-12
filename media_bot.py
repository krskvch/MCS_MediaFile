import config
import telebot
from telebot import types
from MediaInfoDLL3 import *

bot = telebot.TeleBot(config.API)
MI = MediaInfo()
outDict = {}
filesDict = {}

@bot.message_handler(content_types=["text"])
def file_listing(message):
    messageStart = message.text
    messageOut = ''
    rootDir = '/Users/igorkriskevich/Movies/MAY/4x3'
    files = []
    for dirName, subdirList, fileList in os.walk(rootDir):
        for fname in fileList:
            if fname != '.DS_Store':
                files.append(fname)
    filesDict = dict(enumerate(files))
    markup = types.ReplyKeyboardMarkup()
    markup.row('START')

    if messageStart == 'START':
        for key in filesDict:
            messageOut = messageOut + str(key) + ': ' + filesDict[key] + '\n'
        bot.send_message(message.chat.id, "Выберите файл: " + '\n' + messageOut)

    else:
        messageOut = message.text
        bot.send_message(message.chat.id, "Сканирую файл: " + filesDict[int(messageOut)])
        MI.Open(rootDir + '/' + filesDict[int(messageOut)])

        class file:
            MI.Option_Static("Inform", "General;%FileName%.%FileExtension%")
            outDict['File name'] = MI.Inform()
            MI.Option_Static("Inform", "General;%FileSize/String2%")
            outDict['File size'] = MI.Inform()
            MI.Option_Static("Inform", "General;%Format%")
            outDict['File format'] = MI.Inform()
            MI.Option_Static("Inform", "General;%Duration/String4%")
            outDict['Duration'] = MI.Inform()

        class video:
            MI.Option_Static("Inform", "Video;%CodecID%")
            outDict['Codec'] = MI.Inform()
            MI.Option_Static("Inform", "Video;%BitRate_Mode/String%, %BitRate/String%")
            outDict['Bit rate'] = MI.Inform()
            MI.Option_Static("Inform", "Video;%FrameRate/String%")
            outDict['Frame rate'] = MI.Inform()
            MI.Option_Static("Inform", "Video;%ScanOrder/String%")
            outDict['Field order'] = MI.Inform()
            MI.Option_Static("Inform", "Video;%Width%x%Height%")
            outDict['Resolution'] = MI.Inform()
            MI.Option_Static("Inform", "Video;%PixelAspectRatio%")
            outDict['Aspect'] = MI.Inform()

        class audio:
            MI.Option_Static("Inform", "Audio;%Format%")
            outDict['Audio codec'] = MI.Inform()
            MI.Option_Static("Inform", "Audio;%BitRate/String%")
            outDict['Audio bit rate'] = MI.Inform()
            MI.Option_Static("Inform", "Audio;%SamplingRate/String%")
            outDict['Sample rate'] = MI.Inform()
            MI.Option_Static("Inform", "Audio;%BitDepth_Detected%")
            outDict['Sample size'] = MI.Inform()


            MI.Option_Static("Inform", "Audio;%Channel(s)/String%, %ChannelLayout%")
            outDict['Channels layout'] = MI.Inform()


        for key in outDict:
            messageOut = messageOut + key + '-' + outDict[key] + '\n'
        bot.send_message(message.chat.id, messageOut)



    # if message == 'Left':
    #     message = "Turn left?"
    # bot.send_message(message.chat.id, message.text)

    # markup = types.ReplyKeyboardMarkup()
    # markup.row('Left', 'Right')
    # markup.row('c', 'd', 'e')
    # bot.send_message(message.chat.id, "Choose your destination:", reply_markup=markup)

if __name__ == '__main__':
    bot.polling(none_stop=True)