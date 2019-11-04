init python:
    whiteflash = Fade(0.1,0.1,0.1,color="fff")
init:
    transform m(lh):
        pause 0.3
        "lh/"+lh+"b~ipad.png"
        pause 0.3
        "lh/"+lh+"c~ipad.png"
        pause 0.1
        "lh/"+lh+"a~ipad.png"
        repeat
    transform left:
        yanchor 1.0
        xanchor .5
        xpos .25
    transform right:
        yanchor 1.0
        xanchor .5
        xpos .75
    transform right_q2:
        yanchor 1.0
        xanchor .5
        xpos .95
    transform right_q1:
        yanchor 1.0
        xanchor .5
        xpos .65
    transform left_q1:
        yanchor 1.0
        xanchor .5
        xpos .35
    transform left_q2:
        yanchor 1.0
        xanchor .5
        xpos .05
    transform right_t:
        yanchor 1.0
        xanchor .5
        xpos .75
    transform left_t:
        yanchor 1.0
        xanchor .5
        xpos .25
    transform right0:
        yanchor 1.0
        xanchor .5
        xpos .6
    transform left0:
        yanchor 1.0
        xanchor .5
        xpos .4
    transform left_l:
        yanchor 1.0
        xanchor .5
        xpos .2
    transform right_l:
        yanchor 1.0
        xanchor .5
        xpos .8
    image cursor:
        LiveCrop((0,0,24,24),Image("system/icoMes~ipad.png"))
        pause .1
        LiveCrop((24*1,0,24,24),Image("system/icoMes~ipad.png"))
        pause .1
        LiveCrop((24*2,0,24,24),Image("system/icoMes~ipad.png"))
        pause .1
        LiveCrop((24*3,0,24,24),Image("system/icoMes~ipad.png"))
        pause .1
        LiveCrop((24*4,0,24,24),Image("system/icoMes~ipad.png"))
        pause .1
        LiveCrop((24*5,0,24,24),Image("system/icoMes~ipad.png"))
        pause .1
        LiveCrop((24*6,0,24,24),Image("system/icoMes~ipad.png"))
        pause .1
        LiveCrop((24*7,0,24,24),Image("system/icoMes~ipad.png"))
        pause .1
        LiveCrop((24*8,0,24,24),Image("system/icoMes~ipad.png"))
        pause .1
        LiveCrop((24*9,0,24,24),Image("system/icoMes~ipad.png"))
        pause .1
        LiveCrop((24*10,0,24,24),Image("system/icoMes~ipad.png"))
        pause .1
        LiveCrop((24*11,0,24,24),Image("system/icoMes~ipad.png"))
        pause .1
        LiveCrop((24*12,0,24,24),Image("system/icoMes~ipad.png"))
        pause .1
        LiveCrop((24*13,0,24,24),Image("system/icoMes~ipad.png"))
        pause .1
        LiveCrop((24*14,0,24,24),Image("system/icoMes~ipad.png"))
        pause .1
        LiveCrop((24*15,0,24,24),Image("system/icoMes~ipad.png"))
        repeat


    define persistent.imagelog = {}
    define persistent.skipmail = False
    define persistent.bgmdown = True
    define persistent.tips = True
    define persistent.mail = []
    define character.centered.ctc = "cursor"
    define character.centered.kind = nvl
init -5 python:
    Preference("skip", "all")()














    phonecg = "WALLOKA"
    phonering = "sgse700"
    phonemailring = "sgse701"


    movief = ".mp4"
    video = True

    def Savename(scn):
        for t in gc["TitleList"]:
            try:
                t["Script"].index(scn)
                return t["Title"]
            except:
                pass
    def RcvMail(i):
        try:
            rml.index(gc["MailData"][i])
        except:
            rml.append(gc["MailData"][i])
            rml.sort(mailsort)
    def SndMail(i):
        try:
            sml.index(gc["MailData"][i])
        except:
            sml.append(gc["MailData"][i])
            sml.sort(mailsort)
    def ReadMail(i):
        if gd["RCVmailData"][i]["check"] == 0:
            gd["RCVmailData"][i]["check"] = 1
    def ReplyMail(i):
        gd["RCVmailData"][i]["check"] = 2
    def UnreadMail(i):
        gd["RCVmailData"][i]["check"] = 0
    def GetMail(i,may=False):
        mailID=""
        parentmailID=gd["RCVmailData"][i]["mailID"]
        print parentmailID
        for t in gc["MailTreeData"][parentmailID[3:6]]:
            if t["parentMailID"] == parentmailID:
                mailID = t["mailID"]
        if len(mailID)!=0:
            mailIDnum = gc["ScriptMacros"][mailID]
            if not may:
                cml[parentmailID[:-6]]=mailIDnum
            else:
                cml[parentmailID]=mailIDnum

    def mailsort(m1,m2):
        if m1["MetaData"]["Date"]>m2["MetaData"]["Date"]:
            return -1
        elif m1["MetaData"]["Date"]<m2["MetaData"]["Date"]:
            return 1
        else:
            if m1["MetaData"]["Time"]>=m2["MetaData"]["Time"]:
                return -1
            else:
                return 1



    def InitMail(route):
        loadplist()
        
        sm = gc["ScriptMacros"]
        if route == "oka":
            pass


    persistent.video = False
    persistent.mouth = False
    persistent.phone = False
    style.default.font = "default.ttf"

    renpy.music.register_channel("bgm", mixer="music", loop=True, stop_on_mute=True, tight=True, file_prefix='bgm/', file_suffix='.ogg', buffer_queue=True)
    renpy.music.register_channel("MAY", mixer="voice", loop=False, stop_on_mute=True, tight=True, file_prefix='voice/', file_suffix='.ogg', buffer_queue=True)
    renpy.music.register_channel("OKA", mixer="voice", loop=False, stop_on_mute=True, tight=True, file_prefix='voice/', file_suffix='.ogg', buffer_queue=True)
    renpy.music.register_channel("DAR", mixer="voice", loop=False, stop_on_mute=True, tight=True, file_prefix='voice/', file_suffix='.ogg', buffer_queue=True)
    renpy.music.register_channel("CRS", mixer="voice", loop=False, stop_on_mute=True, tight=True, file_prefix='voice/', file_suffix='.ogg', buffer_queue=True)
    renpy.music.register_channel("FEI", mixer="voice", loop=False, stop_on_mute=True, tight=True, file_prefix='voice/', file_suffix='.ogg', buffer_queue=True)
    renpy.music.register_channel("GOS", mixer="voice", loop=False, stop_on_mute=True, tight=True, file_prefix='voice/', file_suffix='.ogg', buffer_queue=True)
    renpy.music.register_channel("MAR", mixer="voice", loop=False, stop_on_mute=True, tight=True, file_prefix='voice/', file_suffix='.ogg', buffer_queue=True)
    renpy.music.register_channel("MOE", mixer="voice", loop=False, stop_on_mute=True, tight=True, file_prefix='voice/', file_suffix='.ogg', buffer_queue=True)
    renpy.music.register_channel("OKF", mixer="voice", loop=False, stop_on_mute=True, tight=True, file_prefix='voice/', file_suffix='.ogg', buffer_queue=True)
    renpy.music.register_channel("RUK", mixer="voice", loop=False, stop_on_mute=True, tight=True, file_prefix='voice/', file_suffix='.ogg', buffer_queue=True)
    renpy.music.register_channel("SDO", mixer="voice", loop=False, stop_on_mute=True, tight=True, file_prefix='voice/', file_suffix='.ogg', buffer_queue=True)
    renpy.music.register_channel("SUZ", mixer="voice", loop=False, stop_on_mute=True, tight=True, file_prefix='voice/', file_suffix='.ogg', buffer_queue=True)
    renpy.music.register_channel("SUZ2", mixer="voice", loop=False, stop_on_mute=True, tight=True, file_prefix='voice/', file_suffix='.ogg', buffer_queue=True)
    renpy.music.register_channel("SUZ3", mixer="voice", loop=False, stop_on_mute=True, tight=True, file_prefix='voice/', file_suffix='.ogg', buffer_queue=True)
    renpy.music.register_channel("TEN", mixer="voice", loop=False, stop_on_mute=True, tight=True, file_prefix='voice/', file_suffix='.ogg', buffer_queue=True)
    renpy.music.register_channel("TMA", mixer="voice", loop=False, stop_on_mute=True, tight=True, file_prefix='voice/', file_suffix='.ogg', buffer_queue=True)
    renpy.music.register_channel("TMB", mixer="voice", loop=False, stop_on_mute=True, tight=True, file_prefix='voice/', file_suffix='.ogg', buffer_queue=True)
    renpy.music.register_channel("TNS", mixer="voice", loop=False, stop_on_mute=True, tight=True, file_prefix='voice/', file_suffix='.ogg', buffer_queue=True)
    renpy.music.register_channel("URP", mixer="voice", loop=False, stop_on_mute=True, tight=True, file_prefix='voice/', file_suffix='.ogg', buffer_queue=True)
    renpy.music.register_channel("YUK", mixer="voice", loop=False, stop_on_mute=True, tight=True, file_prefix='voice/', file_suffix='.ogg', buffer_queue=True)
    renpy.music.register_channel("AN", mixer="voice", loop=False, stop_on_mute=True, tight=True, file_prefix='voice/', file_suffix='.ogg', buffer_queue=True)
    renpy.music.register_channel("CMA", mixer="voice", loop=False, stop_on_mute=True, tight=True, file_prefix='voice/', file_suffix='.ogg', buffer_queue=True)
    renpy.music.register_channel("CMB", mixer="voice", loop=False, stop_on_mute=True, tight=True, file_prefix='voice/', file_suffix='.ogg', buffer_queue=True)
    renpy.music.register_channel("CMC", mixer="voice", loop=False, stop_on_mute=True, tight=True, file_prefix='voice/', file_suffix='.ogg', buffer_queue=True)
    renpy.music.register_channel("DIR", mixer="voice", loop=False, stop_on_mute=True, tight=True, file_prefix='voice/', file_suffix='.ogg', buffer_queue=True)
    renpy.music.register_channel("FAA", mixer="voice", loop=False, stop_on_mute=True, tight=True, file_prefix='voice/', file_suffix='.ogg', buffer_queue=True)
    renpy.music.register_channel("FAB", mixer="voice", loop=False, stop_on_mute=True, tight=True, file_prefix='voice/', file_suffix='.ogg', buffer_queue=True)
    renpy.music.register_channel("NAE", mixer="voice", loop=False, stop_on_mute=True, tight=True, file_prefix='voice/', file_suffix='.ogg', buffer_queue=True)
    renpy.music.register_channel("KUR", mixer="voice", loop=False, stop_on_mute=True, tight=True, file_prefix='voice/', file_suffix='.ogg', buffer_queue=True)
    renpy.music.register_channel("UPP", mixer="voice", loop=False, stop_on_mute=True, tight=True, file_prefix='voice/', file_suffix='.ogg', buffer_queue=True)
    renpy.music.register_channel("FPP", mixer="voice", loop=False, stop_on_mute=True, tight=True, file_prefix='voice/', file_suffix='.ogg', buffer_queue=True)
    renpy.music.register_channel("NAK", mixer="voice", loop=False, stop_on_mute=True, tight=True, file_prefix='voice/', file_suffix='.ogg', buffer_queue=True)
    renpy.music.register_channel("voc", mixer="voice", loop=False, stop_on_mute=True, tight=True, file_prefix='voice/', file_suffix='.ogg', buffer_queue=True)
    renpy.music.register_channel("se", mixer="sfx", loop=False, stop_on_mute=True, tight=True, file_prefix='se/', file_suffix='.ogg', buffer_queue=True)
    renpy.music.register_channel("rain", mixer="se",loop=True,tight=True)
    style.default.size = 20
    style.default.color = "#FFFFFF" 
    config.has_autosave = True
    config.image_cache_size = 16
    config.default_text_cps = 30
    _game_menu_screen = "rmenu"
    def stopallvoc(event,interact=True,**kwargs):
        if not interact:
            return
        if event == "begin":
            stopvoc("")
    def CheckMail():
        flag = False
        for m in rml:
            if gd["RCVmailData"][m["MailNumber"]]["check"] == 0:
                flag = True
        if flag==False:
            persistent.gd['AchievementData'][18]['Check']=1
        return flag
    def loadBG(id,name,png=False,trans=dissolve,hide=True,hold=False,at=[Transform()],over=False):
        if not over:
            if hide:
                renpy.hide("lh5")
                renpy.hide("lh6")
                renpy.hide("lh7")
                renpy.hide("lh8")
                renpy.hide("background-over")
                renpy.hide("background-png")
            
            if not png:
                renpy.show("background",what=Image("bg/"+name+"~ipad.jpg"),at_list=at)
            else:
                renpy.show("background-png",what=Image("system/"+name+"~ipad.png"),zorder = 100,at_list=at)
        else:
            renpy.show("background-over",what=Image("bg/"+name+"~ipad.jpg"),at_list=at,zorder=100)
        if not hold:
            renpy.with_statement(trans)
        persistent.imagelog[name] = True
    def mouthanime(st,at,lh):
        return At(Null(),m(lh)),None
    def stopvoc(name=""):
        if name != "MAY":
            renpy.music.stop(channel="MAY")
        if name != "OKA":
            renpy.music.stop(channel="OKA")
        if name != "DAR":
            renpy.music.stop(channel="DAR")
        if name != "CRS":
            renpy.music.stop(channel="CRS")
        if name != "FEI":
            renpy.music.stop(channel="FEI")
        if name != "GOS":
            renpy.music.stop(channel="GOS")
        if name != "MAR":
            renpy.music.stop(channel="MAR")
        if name != "MOE":
            renpy.music.stop(channel="MOE")
        if name != "OKF":
            renpy.music.stop(channel="OKF")
        if name != "RUK":
            renpy.music.stop(channel="RUK")
        if name != "SDO":
            renpy.music.stop(channel="SDO")
        if name != "SUZ":
            renpy.music.stop(channel="SUZ")
        if name != "SUZ2":
            renpy.music.stop(channel="SUZ2")
        if name != "SUZ3":
            renpy.music.stop(channel="SUZ3")
        if name != "TEN":
            renpy.music.stop(channel="TEN")
        if name != "TMA":
            renpy.music.stop(channel="TMA")
        if name != "TMB":
            renpy.music.stop(channel="TMB")
        if name != "TNS":
            renpy.music.stop(channel="TNS")
        if name != "URP":
            renpy.music.stop(channel="URP")
        if name != "YUK":
            renpy.music.stop(channel="YUK")
        if name != "AN":
            renpy.music.stop(channel="AN")
        if name != "CMA":
            renpy.music.stop(channel="CMA")
        if name != "CMB":
            renpy.music.stop(channel="CMB")
        if name != "NAE":
            renpy.music.stop(channel="NAE")
        if name != "CMC":
            renpy.music.stop(channel="CMC")
        if name != "DIR":
            renpy.music.stop(channel="DIR")
        if name != "FAA":
            renpy.music.stop(channel="FAA")
        if name != "FAB":
            renpy.music.stop(channel="FAB")
        if name != "FAB":
            renpy.music.stop(channel="FAB")
        if name != "FPP":
            renpy.music.stop(channel="FPP")
        if name != "NAK":
            renpy.music.stop(channel="NAK")
        if name != "KUR":
            renpy.music.stop(channel="KUR")
        if name != "UPP":
            renpy.music.stop(channel="UPP")
        renpy.music.stop(channel="voc")
    def GetPhoneCgList():
        l = []
        for index,i in enumerate(persistent.gc["PhoneWallPaperData"]):
            if i["flag"] == "0":
                l.append(index)
        return l
    def GetPhoneRingList():
        l=[]
        for index,i in enumerate(persistent.gc["PhoneRingData"]):
            if i["flag"]=="0":
                l.append(index)
        return l
    def notLate(mailID):
        gd["RCVmailData"][mailID]["late"]=False
    def isread(mailID):
        return gd["RCVmailData"][gc["ScriptMacros"][mailID]]["check"]
    def isreplied(mailID):
        return gd["RCVmailData"][gc["ScriptMacros"][mailID]]["check"]==2
    def isrcved(mailID):
        if gc["MailData"][gc["ScriptMacros"][mailID]] in rml:
            return True
        else:
            return False
