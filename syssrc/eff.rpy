image EVOKA001A_BG1:
    "bg/EV_OKA001A1~ipad.jpg"
    xalign 0.0
    linear 0.07 xalign 1.0
    repeat

image EVOKA001A_BG2:
    "bg/EV_OKA001B1~ipad.jpg"
    xalign 1.0
    linear 0.07 xalign 0.0
    repeat

image EVOKA001A_BG3:
    "bg/EV_OKA001C1~ipad.jpg"
    yalign 1.0
    linear 0.07 yalign 0.0
    repeat

image EVOKA001A_BG4:
    "bg/EV_OKA001D1~ipad.jpg"
    yalign 0.0
    linear 0.07 yalign 1.0
    repeat

image EVOKA001A_FACE_R = "system/EV_OKA001A2~ipad.png"
image EVOKA001A_FACE_L = "system/EV_OKA001B2~ipad.png"
image EVOKA001A_FACE_C = "system/EV_OKA001C2~ipad.png"
image EVOKA001A_FACE_H = "system/EV_OKA001D2~ipad.png"
image EVOKA001A_FACE:
    "system/EV_OKA001E2~ipad.png"
    ypos -1.0
    alpha 0.0
    parallel:
        linear 0.2 ypos 2.3
    parallel:
        linear 0.2 alpha 1.0
    ypos -1.0
    alpha 0.0
    parallel:
        linear 0.2 ypos 2.3
    parallel:
        linear 0.2 alpha 1.0
    ypos -1.0
    alpha 0.0
    parallel:
        linear 0.2 ypos 2.3
    parallel:
        linear 0.2 alpha 1.0
    ypos -1.0
    alpha 0.0
    parallel:
        linear 0.6 ypos 2.3
    parallel:
        linear 0.6 alpha 1.0


image EVOKA001A_HAND:
    "system/EV_OKA001E3~ipad.png"
    alpha 0.0
    2.8
    linear 0.2 alpha 1.0
    linear 0.2 alpha 0.0
image EVOKA001E:
    "bg/EV_OKA001E0~ipad.jpg"
    yalign 0.5
    linear 0.5 yalign 0.0

image EVOKA001E2:
    "bg/EV_OKA001E0~ipad.jpg"
    yalign 0.5
    linear 0.5 yalign 0.3

image EVOKA001E3:
    "bg/EV_OKA001E0~ipad.jpg"
    yalign 0.3
    linear 0.5 yalign 0.0

image sprinkler:
    "system/imv050_0~ipad.png"
    pause 0.1
    "system/imv050_1~ipad.png"
    pause 0.1
    "system/imv050_2~ipad.png"
    pause 0.1
    "system/imv050_3~ipad.png"
    pause 0.1
    "system/imv050_4~ipad.png"
    pause 0.1
    "system/imv050_5~ipad.png"
    pause 0.1
    "system/imv050_6~ipad.png"
    pause 0.1
    repeat
image houden:
    "system/imv004_0~ipad.png"
    pause 0.1
    "system/imv004_1~ipad.png"
    pause 0.1
    "system/imv004_2~ipad.png"
    pause 0.1
    "system/imv004_3~ipad.png"
    pause 0.1
    "system/imv004_4~ipad.png"
    pause 0.1
    "system/imv004_5~ipad.png"
    pause 0.1
    "system/imv004_6~ipad.png"
    pause 0.1
    "system/imv004_7~ipad.png"
    pause 0.1
    "system/imv004_8~ipad.png"
    pause 0.1
    "system/imv004_9~ipad.png"
    pause 0.1
    "system/imv004_10~ipad.png"
    pause 0.1
    "system/imv004_11~ipad.png"
    pause 0.1
    "system/imv004_12~ipad.png"
    pause 0.1
    "system/imv004_13~ipad.png"
    pause 0.1
    "system/imv004_14~ipad.png"
    pause 0.1
    "system/imv004_15~ipad.png"
    pause 0.1
    "system/imv004_16~ipad.png"
    pause 0.1
    "system/imv004_17~ipad.png"
    pause 0.1
    "system/imv004_18~ipad.png"
    pause 0.1
    "system/imv004_19~ipad.png"
    pause 0.1
    "system/imv004_20~ipad.png"
    pause 0.1
    "system/imv004_21~ipad.png"
    pause 0.1
    "system/imv004_22~ipad.png"
    pause 0.1
    "system/imv004_23~ipad.png"
    pause 0.1
    "system/imv004_24~ipad.png"
    pause 0.1
    "system/imv004_25~ipad.png"
    pause 0.1
    "system/imv004_26~ipad.png"
    pause 0.1
    "system/imv004_27~ipad.png"
    pause 0.1
    "system/imv004_28~ipad.png"
    pause 0.1
    "system/imv004_29~ipad.png"
    pause 0.1
    "system/imv004_30~ipad.png"
    pause 0.1
    "system/imv004_31~ipad.png"
    pause 0.1
    "system/imv004_32~ipad.png"
    pause 0.1
    "system/imv004_33~ipad.png"
    pause 0.1
    "system/imv004_34~ipad.png"
    pause 0.1
    "system/imv004_35~ipad.png"
    pause 0.1
    "system/imv004_36~ipad.png"
    pause 0.1
    "system/imv004_37~ipad.png"
    pause 0.1
    "system/imv004_38~ipad.png"
    pause 0.1
    "system/imv004_39~ipad.png"
    pause 0.1
    "system/imv004_40~ipad.png"
    pause 0.1
    repeat
image timeleap_bg = Movie(channel="timeleap",play="video/timeleap.avi")
image timeleap_no = Movie(channel="timeleap",play="video/imv15.avi")

init python:
    def show_time(st,at,current,target,day):
        if st < 2:
            return Null(),0.5
        if not ( current[0] == target[0] and current[1] == target[1] and current[2] == target[2] and current[3] == target[3]):
            current[3] -= 1
            if current[3] < 0:
                current[3] = 59
                current[2] -= 1
                if current[2] < 0:
                    current[2] = 23
                    current[1] -= 1
                    day[0] -= 1
                    if day[0] == -1:
                        day[0] = 6
        else:
            time_leap_done = True
        return LiveComposite((1024,576),(0,0),"system/EFF_TIMELEAP~ipad.png",(75,240),LiveCrop((84*current[0],0,84,119),"system/eff_timeleap_digit~ipad.png"),(200,240),LiveCrop((84*(current[1]/10),0,84,119),"system/eff_timeleap_digit~ipad.png"),(200+84,240),LiveCrop((84*(current[1]%10),0,84,119),"system/eff_timeleap_digit~ipad.png"),(400,240),LiveCrop((114*day[0],0,114,118),"system/eff_timeleap_date~ipad.png"),(520,240),LiveCrop((84*(current[2]/10),0,84,119),"system/eff_timeleap_digit~ipad.png"),(520+84,240),LiveCrop((84*(current[2]%10),0,84,119),"system/eff_timeleap_digit~ipad.png"),(735,240),LiveCrop((84*(current[3]/10),0,84,119),"system/eff_timeleap_digit~ipad.png"),(735+84,240),LiveCrop((84*(current[3]%10),0,84,119),"system/eff_timeleap_digit~ipad.png")),1/120.0


label timeleap(fromtime=None, totime=None, fromday=None):
    $ time_leap_done = False
    show timeleap_bg
    show expression DynamicDisplayable(show_time, fromtime, totime, fromday) as timeanime:
        align (0.5,0.5)
        alpha 0.0
        zoom 3.0
        2
        parallel:
            linear 1.0 zoom 1.0
        parallel:
            linear 1.0 alpha 1.0
        fromtime[2] - totime[2] +(fromtime[1]-totime[1])*24+ 1
        parallel:
            linear 1.0 zoom 0.0001
        parallel:
            linear 1.0 alpha 0.0
    with Fade(0.5,1,0.5)
    $ renpy.pause(fromtime[2] - totime[2]+(fromtime[1]-totime[1])*24 + 3,hard=True)
    hide timeleap_bg
    hide timeanime
    $ loadBG(0,"BG_BLACK",trans=Fade(0.5,0,0))
    pause fromtime[2] - totime[2] + 3
    return


label read_last_mail(id=0, p=False):
    if not p:
        hide screen phonebtn
        hide screen phonebtn2
        pause 1
        show screen phone(interact=False)
        pause 1
    show screen phonemenu
    pause 1
    show screen phonemenu_mail
    pause 1
    show screen phone_inbox
    pause 1
    $ ReadMail(rml[id]["MailNumber"])
    show screen phone_readmail(rml[id])
    pause
    return
label show_mail(id):

    show screen phone_readmail(gc["MailData"][id],ml=sml,interact=False)
    $ renpy.pause(1,hard=True)
    return

label send_mail(id=[], send=True):
    show screen phonemenu
    $ renpy.pause(1,hard=True)
    show screen phonemenu_mail
    $ renpy.pause(1,hard=True)
    while len(id)!=0:
        call show_mail (id[0])
        if len(id) == 1 and send:
            $ SndMail(id[0])
        $ del id[0]

    $ renpy.pause(1,hard=True)


label hide_phone:

    show screen phoneblank
    hide screen phonemenu
    hide screen phone2
    show screen phonebtn
    return


image smoke = Movie(channel="smoke",play="video/imv02.avi",mask="video/imv02_m.avi")
image fire = Movie(channel="fire",play="video/imv01.avi",mask="video/imv01_m.avi")
image mayushi_flashback = Movie(channel="flashback",play="video/imv14.avi")

screen invisible:
    button:
        background None
        action NullAction()
init python:
    def printer(st,at,current,target,light,static=False):
        if len(current)<len(target):
            current.append(target[(len(current))])
        elif not static:
            if len(current) == len(target):
                current.append("&")
            else:
                del current[-1]
        charlist = []
        i = 0
        
        for c in current:
            fn = ""
            if c == "<":
                fn = light+"_"
            elif c==".":
                fn = light+"-0"
            elif c==",":
                fn = light+"-1"
            elif c=="!":
                fn = light+"-2"
            elif c== ";":
                fn = light+"-3"
            elif c== "/":
                fn = light+"-4"
            elif c== "|":
                fn = light+"-5"
            elif c== "?":
                fn = light+"-6"
            elif c== r"%":
                fn = light+"-7"
            elif c== ">":
                fn = light+"-9"
            elif c== "(":
                fn = light+"-10"
            elif c== ")":
                fn = light+"-11"
            elif c== "-":
                fn = light+"-12"
            elif c== "@":
                fn = light+"-13"
            elif c== "&":
                fn = light+"-14"
            elif c== " ":
                fn = "blank"
            else:
                fn = light+c
            if fn!="blank":
                charlist.append((20*i,0))
                charlist.append("system/"+fn+".png")
            
            i+=1
        if not static:
            return LiveComposite((len(current)*20,34),*charlist),0.15
        else:
            return LiveComposite((len(current)*20,34),*charlist),0


init python:
    def printer_str(s):
        return DynamicDisplayable(printer,list(s),list(s),"s",static=True)

image flux1:
    DynamicDisplayable(printer,list("Q           P"),list("Q           P"),"s",static=True)
    pause 0.07
    DynamicDisplayable(printer,list("MK         DV"),list("MK         DV"),"s",static=True)
    pause 0.07
    DynamicDisplayable(printer,list("OVA       7M&"),list("OVA       7M&"),"s",static=True)
    pause 0.07
    DynamicDisplayable(printer,list("5DFY     I/VB"),list("5DFY     I#VB"),"s",static=True)
    pause 0.07
    DynamicDisplayable(printer,list("GTZXK   54Y0J"),list("GTZXK   54Y0J"),"s",static=True)
    pause 0.07
    DynamicDisplayable(printer,list("MTVXKL YSGZ;?"),list("MTVXKL YSGZ;?"),"s",static=True)
    pause 0.07
    DynamicDisplayable(printer,list("H(UA|&QO>RML)"),list("H(UA|&QO>RML)"),"s",static=True)
    pause 0.07
    DynamicDisplayable(printer,list("BAKERYHUNDAND"),list("BAKERYHUNDAND"),"s",static=True)
    pause 0.07
    DynamicDisplayable(printer,list("ELIONPRODUCE!"),list("ELIONPRODUCE!"),"s",static=True)
    pause 0.07
    DynamicDisplayable(printer,list("ZUZHANGKUAIDI"),list("ZUZHANGKUAIDI"),"s",static=True)
    pause 0.07
    DynamicDisplayable(printer,list("ANQUNVZHUANG&"),list("ANQUNVZHUANG&"),"s",static=True)
    pause 0.07
    DynamicDisplayable(printer,list("BAKERYHUNDAND"),list("BAKERYHUNDAND"),"s",static=True)
    pause 0.07
    DynamicDisplayable(printer,list("ELIONPRODUCE!"),list("ELIONPRODUCE!"),"s",static=True)
    pause 0.07
    DynamicDisplayable(printer,list("ZUZHANGKUAIDI"),list("ZUZHANGKUAIDI"),"s",static=True)
    pause 0.07
    DynamicDisplayable(printer,list("ANQUNVZHUANG&"),list("ANQUNVZHUANG&"),"s",static=True)
    pause 0.07
    DynamicDisplayable(printer,list("(JJGFA LQPZML"),list("(JJGFA LQPZML"),"s",static=True)
    pause 0.07
    DynamicDisplayable(printer,list("GTZXK   54Y0J"),list("GTZXK   54Y0J"),"s",static=True)
    pause 0.07
    DynamicDisplayable(printer,list("5DFY     I/VB"),list("5DFY     I#VB"),"s",static=True)
    pause 0.07
    DynamicDisplayable(printer,list("OVA       7M&"),list("OVA       7M&"),"s",static=True)
    pause 0.07
    DynamicDisplayable(printer,list("MK         DV"),list("MK         DV"),"s",static=True)
    pause 0.07
    DynamicDisplayable(printer,list("Q           P"),list("Q           P"),"s",static=True)
    Null()

image flux2:
    0.21
    DynamicDisplayable(printer,list("1           Y"),list("1           Y"),"s",static=True)
    pause 0.07
    DynamicDisplayable(printer,list("EB         QJ"),list("EB         QJ"),"s",static=True)
    pause 0.07
    DynamicDisplayable(printer,list("ZPF       DQN"),list("ZPF       DQN"),"s",static=True)
    pause 0.07
    DynamicDisplayable(printer,list("52EZ     FKGJ"),list("52EZ     FKGJ"),"s",static=True)
    pause 0.07
    DynamicDisplayable(printer,list("WCLNN   FK987"),list("WCLNN   FK987"),"s",static=True)
    pause 0.07
    DynamicDisplayable(printer,list("2W@|(S QZ;?LM"),list("2W@|(S QZ;?LM"),"s",static=True)
    pause 0.07
    DynamicDisplayable(printer,list("12NNVBSA7TYZF"),list("12NNVBSA7TYZF"),"s",static=True)
    pause 0.07
    DynamicDisplayable(printer,list("QIUASGVXHDKL2"),list("QIUASGVXHDKL2"),"s",static=True)
    pause 0.07
    DynamicDisplayable(printer,list("8DG18SYF6XL1;"),list("8DG18SYF6XL1;"),"s",static=True)
    pause 0.07
    DynamicDisplayable(printer,list("M87ZXF(&&)1ST"),list("M87ZXF(&&)1ST"),"s",static=True)
    pause 0.07
    DynamicDisplayable(printer,list("2W@|(S QZ;?LM"),list("2W@|(S QZ;?LM"),"s",static=True)
    pause 0.07
    DynamicDisplayable(printer,list("12NNVBSA7TYZF"),list("12NNVBSA7TYZF"),"s",static=True)
    pause 0.07
    DynamicDisplayable(printer,list("QIUASGVXHDKL2"),list("QIUASGVXHDKL2"),"s",static=True)
    pause 0.07
    DynamicDisplayable(printer,list("8DG18SYF6XL1;"),list("8DG18SYF6XL1;"),"s",static=True)
    pause 0.07
    DynamicDisplayable(printer,list("VNPAOW1FSKT31"),list("VNPAOW1FSKT31"),"s",static=True)
    pause 0.07
    DynamicDisplayable(printer,list("(JJGFA LQPZML"),list("(JJGFA LQPZML"),"s",static=True)
    pause 0.07
    DynamicDisplayable(printer,list("QQWRF   ZVXSG"),list("QQWRF   ZVXSG"),"s",static=True)
    pause 0.07
    DynamicDisplayable(printer,list("SGFD     MNUI"),list("SGFD     MNUI"),"s",static=True)
    pause 0.07
    DynamicDisplayable(printer,list("1SA       NBA"),list("1SA       NBA"),"s",static=True)
    pause 0.07
    DynamicDisplayable(printer,list("WT         IM"),list("WT         IM"),"s",static=True)
    pause 0.07
    DynamicDisplayable(printer,list("2           F"),list("2           F"),"s",static=True)
    Null()


image flux3:
    0.42
    DynamicDisplayable(printer,list("1           Y"),list("1           Y"),"s",static=True)
    pause 0.07
    DynamicDisplayable(printer,list("EB         QJ"),list("EB         QJ"),"s",static=True)
    pause 0.07
    DynamicDisplayable(printer,list("ZPF       DQN"),list("ZPF       DQN"),"s",static=True)
    pause 0.07
    DynamicDisplayable(printer,list("52EZ     FKGJ"),list("52EZ     FKGJ"),"s",static=True)
    pause 0.07
    DynamicDisplayable(printer,list("WCLNN   FK987"),list("WCLNN   FK987"),"s",static=True)
    pause 0.07
    DynamicDisplayable(printer,list("2W@|(S QZ;?LM"),list("2W@|(S QZ;?LM"),"s",static=True)
    pause 0.07
    DynamicDisplayable(printer,list("12NNVBSA7TYZF"),list("12NNVBSA7TYZF"),"s",static=True)
    pause 0.07
    DynamicDisplayable(printer,list("QIUASGVXHDKL2"),list("QIUASGVXHDKL2"),"s",static=True)
    pause 0.07
    DynamicDisplayable(printer,list("8DG18SYF6XL1;"),list("8DG18SYF6XL1;"),"s",static=True)
    pause 0.07
    DynamicDisplayable(printer,list("M87ZXF(&&)1ST"),list("M87ZXF(&&)1ST"),"s",static=True)
    pause 0.07
    DynamicDisplayable(printer,list("VNPAOW1FSKT31"),list("VNPAOW1FSKT31"),"s",static=True)
    pause 0.07
    DynamicDisplayable(printer,list("(JJGFA LQPZML"),list("(JJGFA LQPZML"),"s",static=True)
    pause 0.07
    DynamicDisplayable(printer,list("8DG18SYF6XL1;"),list("8DG18SYF6XL1;"),"s",static=True)
    pause 0.07
    DynamicDisplayable(printer,list("M87ZXF(&&)1ST"),list("M87ZXF(&&)1ST"),"s",static=True)
    pause 0.07
    DynamicDisplayable(printer,list("VNPAOW1FSKT31"),list("VNPAOW1FSKT31"),"s",static=True)
    pause 0.07
    DynamicDisplayable(printer,list("(JJGFA LQPZML"),list("(JJGFA LQPZML"),"s",static=True)
    pause 0.07
    DynamicDisplayable(printer,list("QQWRF   ZVXSG"),list("QQWRF   ZVXSG"),"s",static=True)
    pause 0.07
    DynamicDisplayable(printer,list("SGFD     MNUI"),list("SGFD     MNUI"),"s",static=True)
    pause 0.07
    DynamicDisplayable(printer,list("1SA       NBA"),list("1SA       NBA"),"s",static=True)
    pause 0.07
    DynamicDisplayable(printer,list("WT         IM"),list("WT         IM"),"s",static=True)
    pause 0.07
    DynamicDisplayable(printer,list("2           F"),list("2           F"),"s",static=True)
    Null()
    