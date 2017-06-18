from MediaInfoDLL3 import MediaInfo
import config
from MediaCore.FileListing import filesDict, get_filesDict

outDict = {}

class Parser:
    
    
    def __init__(self):
        self.MI = MediaInfo()


    def scan_file(self, file_num):
        # print(get_filesDict(file_num))
        self.MI.Open(config.rootDir + '/' + filesDict[int(file_num)])
        self.get_info()

        # return filesDict[int(file_num)]

    def get_info(self):
        finalInfo = ''
        self.MI.Option_Static("Inform", "General;%FileName%.%FileExtension%")
        outDict['File name'] = self.MI.Inform()
        self.MI.Option_Static("Inform", "General;%FileSize/String2%")
        outDict['File size'] = self.MI.Inform()
        self.MI.Option_Static("Inform", "General;%Format%")
        outDict['File format'] = self.MI.Inform()
        self.MI.Option_Static("Inform", "General;%Duration/String4%")
        outDict['Duration'] = self.MI.Inform()
        self.MI.Option_Static("Inform", "Video;%CodecID%")
        outDict['Codec'] = self.MI.Inform()
        self.MI.Option_Static("Inform", "Video;%BitRate_Mode/String%, %BitRate/String%")
        outDict['Bit rate'] = self.MI.Inform()
        self.MI.Option_Static("Inform", "Video;%FrameRate/String%")
        outDict['Frame rate'] = self.MI.Inform()
        self.MI.Option_Static("Inform", "Video;%ScanOrder/String%")
        outDict['Field order'] = self.MI.Inform()
        self.MI.Option_Static("Inform", "Video;%Width%x%Height%")
        outDict['Resolution'] = self.MI.Inform()
        self.MI.Option_Static("Inform", "Video;%PixelAspectRatio%")
        outDict['Aspect'] = self.MI.Inform()
        self.MI.Option_Static("Inform", "Audio;%Format%")
        outDict['Audio codec'] = self.MI.Inform()
        self.MI.Option_Static("Inform", "Audio;%BitRate/String%")
        outDict['Audio bit rate'] = self.MI.Inform()
        self.MI.Option_Static("Inform", "Audio;%SamplingRate/String%")
        outDict['Sample rate'] = self.MI.Inform()
        self.MI.Option_Static("Inform", "Audio;%BitDepth_Detected%")
        outDict['Sample size'] = self.MI.Inform()
        self.MI.Option_Static("Inform", "Audio;%Channel(s)/String%, %ChannelLayout%")
        outDict['Channels layout'] = self.MI.Inform()
        return outDict

    # def getFInfo(self):
    #     finalInfo = ''
    #     for key in outDict:
    #         finalInfo = (key + ': ' + outDict[key] + '\n')
    #     return finalInfo