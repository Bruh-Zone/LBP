init -5 python:
    def loadplist():
        global gc,gd
        import plistlib
        from re import *
        f = renpy.loader.load("plist/Game-Constant.plist")
        gc = plistlib.readPlist(f)
        f = renpy.loader.load("plist/Game-Database.plist")
        gd = plistlib.readPlist(f)
        if persistent.gc == None:
            persistent.gc = gc
        if persistent.gd == None:
            persistent.gd = gd

    loadplist()
    sm = gc["ScriptMacros"]
    class Add(Action):
        def __init__(self,displayable,transform,i=1):
            self.displayable = displayable
            self.transform = transform
            self.i = i
        def __call__(self):
            renpy.hide("temp1")
            renpy.hide("temp2")
            renpy.hide("temp3")
            renpy.show("temp"+str(self.i),what=self.displayable,at_list=[self.transform],layer="screens",zorder=100)

screen phoneSD1(date=date, day=day, dar=False):
    add "system/bgPhoneSD1~ipad.png" pos (15,20)
    if CheckMail():

        add "system/markPhoneSDMail~ipad.png" xanchor 1.0 xpos 150 ypos 35
    if current_route=="dar":
        if bad_denpa:
            add "system/markPhoneSDAntenna2_dar~ipad.png" xanchor 1.0 xpos 150+28+26 ypos 35
        else:
            add "system/markPhoneSDAntenna1_dar~ipad.png" xanchor 1.0 xpos 150+28+26 ypos 35
    else:
        if bad_denpa:
            add "system/markPhoneSDAntenna2~ipad.png" xanchor 1.0 xpos 150+28+26 ypos 35
        else:
            add "system/markPhoneSDAntenna1~ipad.png" xanchor 1.0 xpos 150+28+26 ypos 35
    add "system/markPhoneSDBattery~ipad.png" xanchor 1.0 xpos 150+28 ypos 35
    text date xanchor 0.0 pos (35,45) size 36 font "lcd.ttf"
    text ("("+day+")") xanchor 0.5 xpos 165 ypos 52 size 24
transform phone_open:
    xalign 1.0
    "system/phone01_"+ current_route +".png"
    pause 0.05
    "system/phone02_"+ current_route +".png"
    pause 0.05
    "system/phone03_"+ current_route +".png"
    pause 0.05
    "system/phone04_"+ current_route +".png"
    pause 0.05
    "system/phone05_"+ current_route +".png"
    pause 0.05
    "system/phone06_"+ current_route +".png"
    pause 0.05
    "system/phone07_"+ current_route +".png"
    pause 0.05
    "system/phone08_"+ current_route +".png"
    pause 0.05
    "system/phone09_"+ current_route +".png"
    pause 0.05
    "system/phone10_"+ current_route +".png"
    pause 0.05
    Null()

transform phone_close:
    xalign 1.0
    "system/phone10_"+ current_route +".png"
    pause 0.05
    "system/phone09_"+ current_route +".png"
    pause 0.05
    "system/phone08_"+ current_route +".png"
    pause 0.05
    "system/phone07_"+ current_route +".png"
    pause 0.05
    "system/phone06_"+ current_route +".png"
    pause 0.05
    "system/phone05_"+ current_route +".png"
    pause 0.05
    "system/phone04_"+ current_route +".png"
    pause 0.05
    "system/phone03_"+ current_route +".png"
    pause 0.05
    "system/phone02_"+ current_route +".png"
    pause 0.05
    "system/phone01_"+ current_route +".png"
    pause 0.05
    Null()

transform phone_bg:
    alpha 0.0
    pause 0.5
    alpha 1.0

screen phonebtn(interact=True, transit=True) tag phonebtn:

    imagebutton idle "system/phone_icon.png" hover "system/phone_icon.png" selected_idle "system/phone_icon.png" selected_hover "system/phone_icon.png" action [Show("phonebtn2"),Show("phone")] align (1.0,0)

screen phonebtn2 tag phonebtn:


    imagebutton idle "system/phone_icon.png" hover "system/phone_icon.png" selected_idle "system/phone_icon.png" selected_hover "system/phone_icon.png" action [Show("phoneblank"),Hide("phonemenu"),Hide("phone2"),Show("phonebtn")] align (1.0,0)

screen phone(interact=True, transit=True) tag phone:

    zorder -100
    if transit:
        add Null() xalign 1.0 at phone_open
        add "system/phone00_"+current_route+"@2x.png" xalign 1.0 at phone_bg
        add "system/"+phonecg+".png" pos (690,86) at phone_bg
        if bad_denpa:
            add "system/status_bar2_"+current_route+".png" pos (690,86) at phone_bg
        else:
            add "system/status_bar1_"+current_route+".png" pos (690,86) at phone_bg
        if CheckMail():
            add "system/mark_mail_"+current_route+".png" pos (925-50,88) at phone_bg
    else:
        add "system/phone00_"+current_route+"@2x.png" xalign 1.0
        add "system/"+phonecg+".png" pos (690,86)
        add "system/status_bar1_"+current_route+".png" pos (690,86)
        if CheckMail():
            add "system/mark_mail_"+current_route+".png" pos (925-50,88)
    on "replaced" action [Add(Null(),phone_close)]
    if interact:
        on "show" action [Show("phonebtn2")]
    if interact:
        button:
            background None
            xfill True
            area (0,0,1024-335,576)
            action NullAction()
        button:
            background None
            xfill True
            area (730-40,0,1024-730 + 40,86)
            action NullAction()
        button:
            background None
            xfill True
            area (730-40,407,1024-730 + 40,576-407)
            action NullAction()
        button:
            background None
            xfill True
            area (730-40+256,86,1024-730 + 40-256,320)
            action NullAction()
        button:
            background None
            area (730-40,86,256,320)
            action Show("phonemenu",id=id)
    key 'skip' action NullAction()

screen phoneblank tag phone:

    timer 0.01 action [Hide("phone"),Hide("phoneblank")]




screen phonemenu(id=1) tag phonemenu:

    zorder -1
    add LiveCrop((0,0,256,320-26-25),"system/phone_menu_" + current_route+ ".png") pos (730-40,86+26+25)
    add "system/header_menu_"  + current_route+  ".png" pos (730-40,86+26)
    if bad_denpa:
        add "system/status_bar2_"+current_route+".png" pos (690,86) at phone_bg
    else:
        add "system/status_bar1_"+current_route+".png" pos (690,86) at phone_bg
    if CheckMail():
        add "system/mark_mail_"+ current_route+ ".png" pos (925-50,88)
    imagebutton idle "system/cancel.png" hover "system/cancel.png" selected_idle "system/cancel.png" selected_hover "system/cancel.png" action Hide("phonemenu") pos (730-40,86+26)
    text "菜单" pos (810-40,86+25) size 20
    imagebutton idle "system/mail_off_" + current_route+ ".png" hover "system/mail_on_" + current_route+ ".png" selected_idle "system/mail_on_" + current_route+ ".png" selected_hover "system/mail_on_" + current_route+ ".png" action Show("phonemenu_mail",id=id) pos (730+40-40,185)
    imagebutton idle "system/address_off_"+ current_route+ ".png" hover "system/address_on_" + current_route+ ".png" selected_idle "system/address_on_" + current_route+ ".png" selected_hover "system/address_on_" + current_route+ ".png" action Show("phonemenu_address") pos (730+150-40,185)
    imagebutton idle "system/imode_off_" + current_route+ ".png" hover "system/imode_on_" + current_route+ ".png" selected_idle "system/imode_on_" + current_route+".png" selected_hover "system/imode_on_" + current_route+".png" action Hide("phonemenu_imode") pos (730+40-40,185+110)
    imagebutton idle "system/setting_off_" + current_route+ ".png" hover "system/setting_on_" + current_route+ ".png" selected_idle "system/setting_on_" + current_route+ ".png" selected_hover "system/setting_on_" + current_route+ ".png" action NullAction() pos (730+150-40,185+110)
style nothing:
    color "000000"
screen phonemenu_setting tag phonemenu:

    zorder -1
    add LiveCrop((0,0,256,320-26),"system/setting_menu.png") pos (730-40,86+26)
    add "system/header_setting.png" pos (730-40,86+26)
    if bad_denpa:
        add "system/status_bar2_"+current_route+".png" pos (690,86) at phone_bg
    else:
        add "system/status_bar1_"+current_route+".png" pos (690,86) at phone_bg
    if CheckMail():
        add "system/mark_mail_"+current_route+".png" pos (925-50,88)
    imagebutton idle "system/cancel.png" hover "system/cancel.png" selected_idle "system/cancel.png" selected_hover "system/cancel.png" action [Hide("phonemenu_setting"),Show("phonemenu")] pos (730-40,86+26)
    text "设定" pos (840,86+28) size 24
    textbutton "壁纸变更" action Show("phone_changecg") pos (750,210) text_style "nothing" background None
    textbutton "电话铃声变更" action Show("phone_changering") pos (750,210+50) text_style "nothing" background None
    textbutton "短信铃声变更" action Show("phone_changemailring") pos (750,210+100) text_style "nothing" background None

screen phone_changecg tag phonemenu:

    zorder -1
    $ list = GetPhoneCgList()
    add LiveCrop((0,0,256,320-26),"system/setting_menu.png") pos (730-40,86+26)
    add "system/header_setting.png" pos (730-40,86+26)
    if bad_denpa:
        add "system/status_bar2_"+current_route+".png" pos (690,86) at phone_bg
    else:
        add "system/status_bar1_"+current_route+".png" pos (690,86) at phone_bg
    if CheckMail():
        add "system/mark_mail.png" pos (925-50,88)
    imagebutton idle "system/cancel.png" hover "system/cancel.png" selected_idle "system/cancel.png" selected_hover "system/cancel.png" action [Hide("phonemenu"),Show("phonemenu_setting")] pos (730-40,86+26)
    text "壁纸变更" pos (820,86+28) size 24
    window:
        area (730-40,86+26+27,256,320-26-27)
        xpadding 0
        ypadding 0
        add Solid("FFFFFF")
        viewport:
            child_size (256,45)
            mousewheel True
            draggable True
            scrollbars "vertical"
            has grid 1 len(list)
            for i in list:
                button:
                    ypadding 0
                    xpadding 0
                    background None
                    add im.Scale("system/"+gc["PhoneWallPaperData"][i]["image"]+".png",36,45)
                    text gc["PhoneWallPaperData"][i]["name"] pos (40,7) style "nothing"
                    action [SetDict(persistent.gd['AchievementData'][33],'Check',1),Show("phonecomfirm",t="壁纸已设定完成"),SetVariable("phonecg",gc["PhoneWallPaperData"][i]["image"])]






screen phone_changering tag phonemenu:
    $ persistent.gd['AchievementData'][34]['Check']=1

    zorder -1
    $ list = GetPhoneRingList()
    add LiveCrop((0,0,256,320-26),"system/setting_menu.png") pos (730-40,86+26)
    add "system/header_setting.png" pos (730-40,86+26)
    if bad_denpa:
        add "system/status_bar2_"+current_route+".png" pos (690,86) at phone_bg
    else:
        add "system/status_bar1_"+current_route+".png" pos (690,86) at phone_bg
    if CheckMail():
        add "system/mark_mail.png" pos (925-50,88)
    imagebutton idle "system/cancel.png" hover "system/cancel.png" selected_idle "system/cancel.png" selected_hover "system/cancel.png" action [Hide("phonemenu"),Show("phonemenu_setting")] pos (730-40,86+26)
    text "通话铃声变更" pos (820,86+28) size 24
    window:
        area (730-40,86+26+27,256,320-26-27)
        xpadding 0
        ypadding 0
        add Solid("FFFFFF")
        viewport:

            mousewheel True
            draggable True
            scrollbars "vertical"
            has grid 1 len(list)
            for i in list:
                button:
                    ypadding 2
                    xpadding 5
                    background None
                    text gc["PhoneRingData"][i]["name"] pos (7,0) style "nothing"
                    action [Show("phonecomfirm",t="通话铃声已设定完成"),SetVariable("phonering",gc["PhoneRingData"][i]["MailRing"])]


screen phone_changemailring tag phonemenu:

    zorder -1
    $ list = GetPhoneRingList()
    add LiveCrop((0,0,256,320-26),"system/setting_menu.png") pos (730-40,86+26)
    add "system/header_setting.png" pos (730-40,86+26)
    if bad_denpa:
        add "system/status_bar2_"+current_route+".png" pos (690,86) at phone_bg
    else:
        add "system/status_bar1_"+current_route+".png" pos (690,86) at phone_bg
    if CheckMail():
        add "system/mark_mail.png" pos (925-50,88)
    imagebutton idle "system/cancel.png" hover "system/cancel.png" selected_idle "system/cancel.png" selected_hover "system/cancel.png" action [Hide("phonemenu"),Show("phonemenu_setting")] pos (730-40,86+26)
    text "短信铃声变更" pos (820,86+28) size 24
    window:
        area (730-40,86+26+27,256,320-26-27)
        xpadding 0
        ypadding 0
        add Solid("FFFFFF")
        viewport:

            mousewheel True
            draggable True
            scrollbars "vertical"
            has grid 1 len(list)
            for i in list:
                button:
                    ypadding 2
                    xpadding 5
                    background None
                    text gc["PhoneRingData"][i]["name"] pos (7,0) style "nothing"
                    action [Show("phonecomfirm",t="短信铃声已设定完成"),SetVariable("phonemailring",gc["PhoneRingData"][i]["MailRing"])]


screen phonemenu_address(dial=False, mail=False) tag phonemenu:

    zorder -1
    $ list = [9,2,1,0,7,4,3,8,11]
    add LiveCrop((0,0,256,320-26),"system/setting_menu_" + current_route+".png") pos (730-40,86+26)
    add "system/header_setting_" + current_route+".png" pos (730-40,86+26)
    if bad_denpa:
        add "system/status_bar2_"+current_route+".png" pos (690,86) at phone_bg
    else:
        add "system/status_bar1_"+current_route+".png" pos (690,86) at phone_bg
    if CheckMail():
        add "system/mark_mail_" + current_route+".png" pos (925-50,88)
    imagebutton idle "system/cancel.png" hover "system/cancel.png" selected_idle "system/cancel.png" selected_hover "system/cancel.png" action [Hide("phonemenu"),Show("phonemenu")] pos (730-40,86+26)
    #text "通讯录" pos (810-40,86+25) size 20
    text "Contacts" pos (810-40,86+25) size 20
    window:
        area (730-40,86+26+27,256,320-26-27)
        xpadding 0
        ypadding 0
        add Solid("FFFFFF")
        viewport:

            mousewheel True
            draggable True
            scrollbars "vertical"
            has grid 1 len(list)
            for i in list:
                if dial == False and mail == False:
                    button:
                        ypadding 2
                        xpadding 5
                        background None
                        text gc["AddressBookData"][i]["Name"] pos (7,0) style "nothing"

                        action [Show("phonecomfirm",t=gc["AddressBookData"][i]["Name"]+gc["AddressBookData"][i]["PhoneNumber"]),SetVariable("phonemailring",gc["PhoneRingData"][i]["MailRing"])]


screen phonemenu_mail(id=1) tag phonemenu:

    zorder -1
    add LiveCrop((0,0,256,320-26),"system/mail_menu_"+current_route+".png") pos (730-40,86+26)
    add "system/header_mail_"+current_route+".png" pos (730-40,86+26)
    if bad_denpa:
        add "system/status_bar2_"+current_route+".png" pos (690,86) at phone_bg
    else:
        add "system/status_bar1_"+current_route+".png" pos (690,86) at phone_bg
    if CheckMail():
        add "system/mark_mail_"+current_route+".png" pos (925-50,88)
    imagebutton idle "system/cancel.png" hover "system/cancel.png" selected_idle "system/cancel.png" selected_hover "system/cancel.png" action [Hide("phonemenu"),Show("phonemenu")] pos (730-40,86+26)
    text "邮件" pos (810-40,86+25) size 20
    #textbutton "收件箱" action Show("phone_inbox",id=id) pos (750-40,210) text_style None background None text_color "000000"
    textbutton "Inbox" action Show("phone_inbox",id=id) pos (750-40,210) text_style None background None text_color "000000"
    #textbutton "发件箱" action Show("phone_sent",id=id) pos (750-40,210+50) text_style None background None text_color "000000"
    textbutton "Sent" action Show("phone_sent",id=id) pos (750-40,210+50) text_style None background None text_color "000000"

screen phone_inbox(id=1) tag phonemenu:
    $ persistent.gd['AchievementData'][30]['Check']=1

    zorder -1
    $ list = rml
    add LiveCrop((0,0,256,320-26),"system/mail_menu_" + current_route+".png") pos (730-40,86+26)
    add "system/header_mail_" + current_route+".png" pos (730-40,86+26)
    if bad_denpa:
        add "system/status_bar2_"+current_route+".png" pos (690,86) at phone_bg
    else:
        add "system/status_bar1_"+current_route+".png" pos (690,86) at phone_bg
    if CheckMail():
        add "system/mark_mail_" + current_route+".png" pos (925-50,88)
    imagebutton idle "system/cancel.png" hover "system/cancel.png" selected_idle "system/cancel.png" selected_hover "system/cancel.png" action [Hide("phonemenu"),Show("phonemenu_mail")] pos (730-40,86+26)
    #text "收件箱" pos (810-40,86+25) size 20
    text "Inbox" pos (810-40,86+25) size 20
    $ reply = False
    window:
        area (730-40,86+26+27,256,320-26-27)
        xpadding 0
        ypadding 0
        add Solid("FFFFFF")
        if (len(list)!=0):
            viewport:
                child_size (256,25)
                mousewheel True
                draggable True
                scrollbars "vertical"
                has grid 1 len(list)
                for i in list:
                    button:
                        ypadding 2
                        xpadding 5
                        background None
                        if gd["RCVmailData"][i["MailNumber"]]["check"] == 0:
                            add "system/mail_icon.png"
                        elif gd["RCVmailData"][i["MailNumber"]]["check"] == 1:
                            add "system/mail_icon1.png"
                        else:
                            add "system/mail_icon2.png"
                        if i["MetaData"]["Reply0"] != "NO_REPLY" and gd["RCVmailData"][i["MailNumber"]]["check"] != 2:
                            $ reply = True
                        else:
                            $ reply = False
                        if i["MetaData"]["AttachID"] != "NO_ATTACH":
                            add LiveCrop((104,0,26,26),"system/mail_content_" + current_route+".png") pos (30,0)
                            text str(i["MetaData"]["Date"])[0]+"/"+("%d"%int((str(i["MetaData"]["Date"])[1:])))+" "+i["FromTo"] pos (54,0) style "nothing"
                        else:
                            text str(i["MetaData"]["Date"])[0]+"/"+("%d"%int((str(i["MetaData"]["Date"])[1:])))+" "+i["FromTo"] pos (37,0) style "nothing"

                        action [Function(ReadMail,i["MailNumber"]),Show("phone_readmail",None,i)]



screen phone_sent(id=1) tag phonemenu:
    $ persistent.gd['AchievementData'][29]['Check']=1

    zorder -1
    $ list = [i for i in sml]
    add LiveCrop((0,0,256,320-26),"system/mail_menu_" + current_route+".png") pos (730-40,86+26)
    add "system/header_mail_" + current_route+".png" pos (730-40,86+26)
    if bad_denpa:
        add "system/status_bar2_"+current_route+".png" pos (690,86) at phone_bg
    else:
        add "system/status_bar1_"+current_route+".png" pos (690,86) at phone_bg
    if CheckMail():
        add "system/mark_mail_"+current_route+".png" pos (925-50,88)
    imagebutton idle "system/cancel.png" hover "system/cancel.png" selected_idle "system/cancel.png" selected_hover "system/cancel.png" action [Hide("phonecomfirm"),Show("phonemenu_mail")] pos (730-40,86+26)
    text "发件箱" pos (810-40,86+25) size 20
    window:
        area (730-40,86+26+27,256,320-26-27)
        xpadding 0
        ypadding 0
        add Solid("FFFFFF")
        if (len(list)!=0):
            viewport:
                child_size (256,25)
                mousewheel True
                draggable True
                scrollbars "vertical"
                has grid 1 len(list)
                for i in list:
                    button:
                        ypadding 2
                        xpadding 5
                        background None
                        add "system/mail_icon.png"
                        text str(i["MetaData"]["Date"])[0]+"/"+("%d"%int((str(i["MetaData"]["Date"])[1:])))+" "+i["FromTo"] pos (37,0) style "nothing"

                        action Show("phone_readmail", None,i,ml=list)


screen phone_readmail(m, ml=rml, id=1, reply=False, attach=False, rindex=0, interact=True, may=False) tag phonemenu:
    on "show" action Stop("se")

    zorder -1
    add LiveCrop((0,0,256,320-26),"system/mail_menu_" + current_route+".png") pos (730-40,86+26)
    add "system/header_mail_" + current_route+".png" pos (730-40,86+26)
    if bad_denpa:
        add "system/status_bar2_"+current_route+".png" pos (690,86) at phone_bg
    else:
        add "system/status_bar1_"+current_route+".png" pos (690,86) at phone_bg
    if CheckMail():
        add "system/mark_mail_" + current_route+".png" pos (925-50,88)
    if ml == rml:
        #text "收件箱" pos (820-40,86+24) size 24
        text "Received Messages" pos (820-40,86+24) size 24
        imagebutton idle "system/cancel.png" hover "system/cancel.png" selected_idle "system/cancel.png" selected_hover "system/cancel.png" action [Hide("phone2"),Show("phone_inbox")] pos (730-40,86+26)
    else:
        #text "发件箱" pos (820-40,86+24) size 24
        text "Sent Messages" pos (820-40,86+24) size 24
        imagebutton idle "system/cancel.png" hover "system/cancel.png" selected_idle "system/cancel.png" selected_hover "system/cancel.png" action [Hide("phone2"),Show("phone_sent")] pos (730-40,86+26)
    if reply == False and interact:
        imagebutton idle LiveCrop((0,0,35,23),"system/next.png") hover LiveCrop((0,0,35,23),"system/next.png") selected_idle LiveCrop((0,0,35,23),"system/next.png") selected_hover LiveCrop((0,0,35,23),"system/next.png") action Show("phone_readmail",None,ml[max(ml.index(m)-1,0)],ml=ml) pos (910-40,86+28)
        imagebutton idle LiveCrop((36,0,35,23),"system/next.png") hover LiveCrop((36,0,35,23),"system/next.png") selected_idle LiveCrop((36,0,35,23),"system/next.png") selected_hover LiveCrop((36,0,35,23),"system/next.png") action Show("phone_readmail",None,ml[min(ml.index(m)+1,len(ml)-1)],ml=ml) pos (945-40,86+28)
    window:
        area (730-40,86+26+27,256,320-26-27)
        xpadding 0
        ypadding 0
        add Solid("FFFFFF")
        frame:
            background None
            add LiveCrop((0,0,26,26),"system/mail_content_" + current_route+".png")
            if m["MetaData"]["Time"]>=1000:
                text " "+str(m["MetaData"]["Date"])[0]+"/"+("%d"%int((str(m["MetaData"]["Date"])[1:])))+" "+str(m["MetaData"]["Time"])[0:2]+":"+str(m["MetaData"]["Time"])[2:] pos (30,0) size 18 style "nothing"
            elif m["MetaData"]["Time"] >= 100:
                text " "+str(m["MetaData"]["Date"])[0]+"/"+("%d"%int((str(m["MetaData"]["Date"])[1:])))+" "+str(m["MetaData"]["Time"])[0:1]+":"+str(m["MetaData"]["Time"])[1:] pos (30,0) size 18 style "nothing"
            elif m["MetaData"]["Time"] >= 10:
                text "00:"+str(m["MetaData"]["Time"])[0:] pos (30,0) size 18 style "nothing"
            else:
                text "00:0"+str(m["MetaData"]["Time"])[0:] pos (30,0) size 18 style "nothing"

            if m["MetaData"]["AttachID"]!= "NO_ATTACH":
                imagebutton idle LiveCrop((104,0,26,26),"system/mail_content_" + current_route+".png") hover LiveCrop((104,0,26,26),"system/mail_content_" + current_route+".png") selected_idle LiveCrop((104,0,26,26),"system/mail_content_" + current_route+".png") selected_hover LiveCrop((104,0,26,26),"system/mail_content_" + current_route+".png") action Show("phone_attach",None,m["MetaData"]["AttachID"]) pos (0.9,0)

            if m["MetaData"]["MailType"]%2 == 0:

                add LiveCrop((26,0,26,26),"system/mail_content_" + current_route+".png") pos (0,26)
            else:
                add LiveCrop((52,0,26,26),"system/mail_content_" + current_route+".png") pos (0,26)
            text m["FromTo"] pos (30,26) size 18 style "nothing"
            add LiveCrop((78,0,26,26),"system/mail_content_" + current_route+".png") pos (0,52)
            text m["Subject"] pos (30,52) size 18 style "nothing"
        viewport:
            area (0,10,256,320-26-27-78-10)
            mousewheel True
            draggable True
            scrollbars "vertical"
            side_pos (0,78)
            python:
                replystr = []
                if search(r"\\rs",m["Content"]):
                    if ( gd["RCVmailData"][m["MailNumber"]]["check"]==2 or gd["RCVmailData"][m["MailNumber"]].setdefault("late",False)==True):
                        content = sub(r"\\rs(.*?)\\re",r"{color=#000}\1{/color}",m["Content"])
                    else:
                        content = sub(r"\\rs(.*?)\\re",r"{color=#00f}\1{/color}",m["Content"])
                    content = sub(r"\\n",r"",content)
                    for r in findall(r"\\rs.*?\\re",m["Content"]):
                        r = search(r"\\rs(.*?)\\re",r).group(1)
                        replystr.append(r)
                else:
                    content = sub(r"\\n",r"",m["Content"])
            if (len(replystr)== 0 and reply==False )or gd["RCVmailData"][m["MailNumber"]]["check"]==2 or gd["RCVmailData"][m["MailNumber"]].setdefault("late",False)==True:
                text content size 22 style "nothing"
            elif reply == False:
                textbutton content:
                    xpadding 0
                    xmargin 0
                    ypadding 0
                    ymargin 0
                    background None
                    text_size 22
                    text_style "nothing"
                    action Show("phone_mailreply",None,replystr,m,may=may)
            else:

                textbutton content:
                    background None
                    text_size 22
                    text_style "nothing"
                    action [Function(GetMail,m["MailNumber"]),Function(SndMail,m["MailNumber"]),Function(sml.sort,mailsort),SetDict(gd["RCVmailData"][rindex],"check",2),Show("phonecomfirm",None,"信息已发送",m=m,may=may),Hide("phonemenu")]

screen phone_mailreply(replystr, m, may=False) tag phone2:

    $ items = []
    for r in replystr:
        $ items.append((r,[Show("phone_readmail",None,gc["MailData"][sm[m["MetaData"]["Reply"+str(replystr.index(r))]]],reply=True,rindex = m["MailNumber"],may=may),Hide("phone_mailreply")]))
    window:
        area (750-40,200,214,160)
        background "system/phone_submenu_"+current_route+".png"

        has vbox:
            style "menu"
            spacing 2

        for caption, action in items:

            if action:

                button:
                    action action
                    background None
                    text '回复"[caption]"' style "nothing"

            else:
                text caption


screen phone_attach(a):
    python:
        try:
            persistent.gc["PhoneWallPaperData"][int(gc["AttachData"][int(a)]["data"][0]["wall"])]["flag"]="0"
        except:
            pass
    window:
        xpadding 0
        ypadding 0
        background "system/phone_movie_moe~ipad.png"
        add "system/PACG032~ipad.png" pos (283,35)
        button:
            background None
            xfill True
            yfill True
            action Hide("phone_attach")
    use phoneSD1
screen phonecomfirm(t="", m=None, may=False) tag phone2:


    button:
        area (750-40,200,214,160)
        background "system/phone_submenu_"+current_route+".png"
        text t size 24 area (20,20,150,80) color "#000"
        action Hide("phonecomfirm")
