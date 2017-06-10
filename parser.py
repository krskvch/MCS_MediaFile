import config

MI = config.MediaInfo
#MI.Open(messageOut)

outDict = {}
# key


class file:
#     def getFileName(self):
    MI.Option_Static("Inform", "General;%FileName%.%FileExtension%")
    outDict['File name'] = MI.Inform()
    # def getFileSize(self):
    MI.Option_Static("Inform", "General;%FileSize/String2%")
    outDict['File size'] = MI.Inform()
    # def getFileFormat(self):
    MI.Option_Static("Inform", "General;%Format%")
    outDict['File format'] = MI.Inform()
    # def getDurTC(self):
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

    max_TP_level = ''
    loudness = ''

    MI.Option_Static("Inform", "Audio;%Channel(s)/String%, %ChannelLayout%")
    outDict['Channels layout'] = MI.Inform()

QC_notes = ''

def getfileName(self, path):
    return self.file_name

def getfileSize(self, size):
    return self.file_size

# file.getFileName(self)
# file.getFileFormat(self)
# file.getFileSize(self)
# file.getDurTC(self)
#
# print(file.file_name)
# print(file.file_size)
# print(file.file_format)
# print(file.durationTC)
# print(video.codec)
# print(video.bitrate)
# print(video.framerate)
# print(video.field_order)
# print(video.resolution)
# print(video.aspect)
# print(audio.codec)
# print(audio.bitrate)
# print(audio.sample_rate)
# print(audio.sample_size)
# print(audio.max_TP_level)
# print(audio.loudness)
# print(audio.channels)

for key in outDict:
    outMessage = key + '-' + outDict[key]