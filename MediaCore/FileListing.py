import os
import config


files = []
for dirName, subdirList, fileList in os.walk(config.rootDir):
    for fname in fileList:
        if fname != '.DS_Store':
            files.append(fname)

    filesDict = dict(enumerate(files))
class FileListing:

    def buildMessage(self):
        messageOut = ''
        for key in filesDict:
            messageOut = messageOut + str(key) + ': ' + filesDict[key] + '\n'
        return messageOut

def get_filesDict(num):
    # print(filesDict)
    return filesDict[num]