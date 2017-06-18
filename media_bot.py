import telebot
import sqlite3
import config
from MediaInfoDLL3 import *

bot = telebot.TeleBot(config.API)
MI = MediaInfo()
outDict = {}
filesDict = {}
fileName = 'File name'
fileSize = 'File size'
fileFormat = 'File format'
duration = 'Duration'
codec = 'Codec'
bitRate = 'Bit rate'
frameRate = 'Frame rate'
fieldOrder = 'Field order'
resolution = 'Resolution'
aspect = 'Aspect'
audioCodec = 'Audio codec'
audioBitRate = 'Audio bit rate'
sampleRate = 'Sample rate'
sampleSize = 'Sample size'
channelsLayout = 'Channels layout'
con = sqlite3.connect('parsedData.db')
c = con.cursor()

# c.execute('CREATE TABLE parsedData (id INTEGER PRIMARY KEY, fileName VARCHAR(100), fileSize VARCHAR(50),'
#             'fileFormat VARCHAR(50), duration VARCHAR(50), codec VARCHAR(50), bitRate VARCHAR(50),'
#             'frameRate VARCHAR(50), fieldOrder VARCHAR(50), resolution VARCHAR(50), aspect VARCHAR(50),'
#             'audioCodec VARCHAR(50), audioBitRate VARCHAR(50), sampleRate VARCHAR(50), sampleSize VARCHAR(50),'
#             'channelsLayout VARCHAR(50))')
# con.commit()



@bot.message_handler(content_types=["text"])
def menu(message):
    messageOut = ''
    rootDir = '/Users/igorkriskevich/Movies/MAY/4x3'
    files = []
    for dirName, subdirList, fileList in os.walk(rootDir):
        for fname in fileList:
            if fname != '.DS_Store':
                files.append(fname)
    filesDict = dict(enumerate(files))
    for key in filesDict:
        messageOut = messageOut + str(key) + ': ' + filesDict[key] + '\n'
    bot.send_message(message.chat.id, "Выберите файл: " + '\n' + messageOut)

    # while(message):
    try:
        # int(message.text)
        rootDir = '/Users/igorkriskevich/Movies/MAY/4x3'
        messageIn = message.text
        messageOut = str()
        bot.send_message(message.chat.id, "Сканирую файл: " + filesDict[int(messageIn)])
        MI.Open(rootDir + '/' + filesDict[int(messageIn)])

        MI.Option_Static("Inform", "General;%FileName%.%FileExtension%")
        outDict['File name'] = MI.Inform()
        MI.Option_Static("Inform", "General;%FileSize/String2%")
        outDict['File size'] = MI.Inform()
        MI.Option_Static("Inform", "General;%Format%")
        outDict['File format'] = MI.Inform()
        MI.Option_Static("Inform", "General;%Duration/String4%")
        outDict['Duration'] = MI.Inform()
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
            messageOut = messageOut + key + ' - ' + outDict[key] + '\n'
        bot.send_message(message.chat.id, messageOut)
        cursor.execute("SELECT parsedData FROM outDict ORDER BY parsedData")
        # c.execute("INSERT INTO parsedData VALUES (id, fileName, fileSize, fileFormat, duration, codec, bitRate,"
        #           "frameRate, fieldOrder, resolution, aspect, audioCodec, audioBitRate, sampleRate, sampleSize,"
        #           "channelsLayout)", [None, outDict[fileName], [outDict[fileSize], [outDict[fileFormat],
        #                              [outDict[duration], [outDict[codec], [outDict[bitRate], [outDict[frameRate],
        #                              [outDict[fieldOrder], [outDict[resolution], [outDict[aspect],
        #                              [outDict[audioCodec], [outDict[audioBitRate], [outDict[sampleRate],
        #                              [outDict[sampleSize], [outDict[channelsLayout]])
        con.commit()
        con.close()

    except:
        bot.send_message(message.chat.id, "Некорректный ввод. Повторите.")
    # finally:
    #     menu(message)


if __name__ == '__main__':
    bot.polling(none_stop=True)