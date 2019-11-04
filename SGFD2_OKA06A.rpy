label SGFD2_OKA06A:


    window hide


    $ loadBG(0,"BG05A1")
    play se "SGSE200L" loop



    $ date="8/11"
    python:
        cml = {}
        while len(rml)>0 and rml[0]["MetaData"]["Time"] > 740 and rml[0]["MetaData"]["Date"] == 811:
            UnreadMail(rml[0]["MailNumber"])
            notLate(rml[0]["MailNumber"])
            del rml[0]
        while len(sml)>0 and sml[0]["MetaData"]["Time"] > 740 and sml[0]["MetaData"]["Date"] == 811:
            del sml[0]
        while len(lml)>0 and gc["MailData"][lml[0]]["MetaData"]["Time"] > 740 and gc["MailData"][lml[0]]["MetaData"]["Date"] == 811:
            notLate(lml[0])
            del lml[0]
    show screen phonebtn
    show screen phoneSD1

    $ stopvoc("OKA")
    play OKA "OKA06A_OKA0000"
    $ current_voice = "voice/OKA06A_OKA0000.ogg"
    "伦太郎" "「…………」"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='NAE')",DynamicDisplayable(mouthanime,"NAE_ASA01"),"True","lh/NAE_ASA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("NAE")
    play NAE "OKA06A_NAE0000"
    $ current_voice = "voice/OKA06A_NAE0000.ogg"
    "绹" "「啊……冈伦叔叔，早上好……」"
    $ stopvoc("OKA")
    play OKA "OKA06A_OKA0001"
    $ current_voice = "voice/OKA06A_OKA0001.ogg"
    "伦太郎" "「走吧」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='TEN')",DynamicDisplayable(mouthanime,"TEN_BSA02"),"True","lh/TEN_BSA02a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("TEN")
    play TEN "OKA06A_TEN0000"
    $ current_voice = "voice/OKA06A_TEN0000.ogg"
    "天王寺" "「冈部，你听好了。你要是把绹弄哭的话，我绝不会轻饶你的。」"
    hide screen phoneSD1
    window hide

    stop se



    $ loadBG(0,"BG22B0",trans=fade)

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='NAE')",DynamicDisplayable(mouthanime,"NAE_ASA03"),"True","lh/NAE_ASA03a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    play bgm "FD2BGM05"

    show screen phoneSD1
    $ stopvoc("NAE")
    play NAE "OKA06A_NAE0001"
    $ current_voice = "voice/OKA06A_NAE0001.ogg"
    "绹" "「真的，能买到吗？」"
    $ stopvoc("OKA")
    play OKA "OKA06A_OKA0002"
    $ current_voice = "voice/OKA06A_OKA0002.ogg"
    "伦太郎" "「我们能买到的」"

    $ targetmailid = gc["ScriptMacros"]["RM_OKA_RECV_SUZ01_01"]

    $ LR_RM_CHANCE=3
    call CHECK_RM_RECEIVE
    $ stopvoc("NAE")
    play NAE "OKA06A_NAE0002"
    $ current_voice = "voice/OKA06A_NAE0002.ogg"
    "绹" "「但是，好多人啊」"
    call CHECK_RM_RECEIVE
    $ stopvoc("OKA")
    play OKA "OKA06A_OKA0003"
    $ current_voice = "voice/OKA06A_OKA0003.ogg"
    "伦太郎" "「没事的」"
    call CHECK_RM_RECEIVE
    $ stopvoc("OKA")
    play OKA "OKA06A_OKA0004"
    $ current_voice = "voice/OKA06A_OKA0004.ogg"
    "伦太郎" "「到那里为止都是能买到的」"


    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    "早起的我们，站在４℃他们的前面。"
    $ stopvoc("SDO")
    play SDO "OKA06A_SDO0000"
    $ current_voice = "voice/OKA06A_SDO0000.ogg"
    "４℃" "「我给你们带来的礼物，让你们感动得五脏六腑都温暖了吧！」"
    $ stopvoc("Y06")
    play voc "OKA06A_Y060000"
    $ current_voice = "voice/OKA06A_Y060000.ogg"
    "５℃" "「真不愧是４℃……真是一份振奋人心的礼物」"
    $ stopvoc("Y07")
    play voc "OKA06A_Y070000"
    $ current_voice = "voice/OKA06A_Y070000.ogg"
    "６℃" "「是很适合处于饥饿状态下的我们的食物……」"
    "其后的孩子们会买不到游戏……"
    "只能睁只眼闭只眼了。"
    "也只能这样了。"

    $ lml.append(gc["ScriptMacros"]["RM_OKA_RECV_SUZ01_01"])
    $ gd["RCVmailData"][gc["ScriptMacros"]["RM_OKA_RECV_SUZ01_01"]]["late"]=True

    hide screen phoneSD1
    window hide

    stop se

    stop bgm 




    $ targetmailid = cml.setdefault("RM_OKA_SEND_SUZ01","")

    $ LR_RM_CHANCE=1
    if phonemailring!= "":
        play se phonemailring
    if persistent.skipmail==False:
        $ renpy.choice_for_skipping()
    if targetmailid != "":
        $ RcvMail(targetmailid)
        $ targetmailid=""
    call CHECK_RM_RECEIVE



    $ gd["RCVmailData"][gc["ScriptMacros"]["RM_OKA_RECV_SUZ02_01"]]["late"]=True
    $ lml.append(gc["ScriptMacros"]["RM_OKA_RECV_SUZ02_01"])






    $ loadBG(0,"BG05A2",trans=fade)

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='NAE')",DynamicDisplayable(mouthanime,"NAE_ASA02"),"True","lh/NAE_ASA02a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    show screen phoneSD1
    $ stopvoc("NAE")
    play NAE "OKA06A_NAE0003"
    $ current_voice = "voice/OKA06A_NAE0003.ogg"
    "绹" "「我回来了！」"
    window hide
    play se "SGSE017"

    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='NAE')",DynamicDisplayable(mouthanime,"NAE_ASA02"),"True","lh/NAE_ASA02a~ipad.png") at left as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='TEN')",DynamicDisplayable(mouthanime,"TEN_BSA01"),"True","lh/TEN_BSA01a~ipad.png") at right as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("TEN")
    play TEN "OKA06A_TEN0001"
    $ current_voice = "voice/OKA06A_TEN0001.ogg"
    "天王寺" "「哦哦，终于回来了！」"
    $ stopvoc("TEN")
    play TEN "OKA06A_TEN0002"
    $ current_voice = "voice/OKA06A_TEN0002.ogg"
    "天王寺" "「游戏，买到了吗？」"
    $ stopvoc("NAE")
    play NAE "OKA06A_NAE0004"
    $ current_voice = "voice/OKA06A_NAE0004.ogg"
    "绹" "「嗯、买到了！」"
    $ stopvoc("TEN")
    play TEN "OKA06A_TEN0003"
    $ current_voice = "voice/OKA06A_TEN0003.ogg"
    "天王寺" "「真是太好了」"
    $ stopvoc("NAE")
    play NAE "OKA06A_NAE0005"
    $ current_voice = "voice/OKA06A_NAE0005.ogg"
    "绹" "「谢谢，冈伦叔叔！」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='TEN')",DynamicDisplayable(mouthanime,"TEN_BMA01"),"True","lh/TEN_BMA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("TEN")
    play TEN "OKA06A_TEN0004"
    $ current_voice = "voice/OKA06A_TEN0004.ogg"
    "天王寺" "「冈部，给——」"
    $ stopvoc("OKA")
    play OKA "OKA06A_OKA0005"
    $ current_voice = "voice/OKA06A_OKA0005.ogg"
    "伦太郎" "「不用」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='TEN')",DynamicDisplayable(mouthanime,"TEN_BMA03"),"True","lh/TEN_BMA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("TEN")
    play TEN "OKA06A_TEN0005"
    $ current_voice = "voice/OKA06A_TEN0005.ogg"
    "天王寺" "「啊？奖金哦，奖金」"
    $ stopvoc("OKA")
    play OKA "OKA06A_OKA0006"
    $ current_voice = "voice/OKA06A_OKA0006.ogg"
    "伦太郎" "「不是说不用了！」"
    $ stopvoc("TEN")
    play TEN "OKA06A_TEN0006"
    $ current_voice = "voice/OKA06A_TEN0006.ogg"
    "天王寺" "「哦……哦，这样啊」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    "我想早点去见真由理。"
    "稍微牺牲一点少年们的不幸，对我来说也许是最好的选择。"
    "我没有做错。"
    "现在依然是正义的伙伴。"
    "希望能够这么说。"
    window hide



    $ loadBG(0,"BG02A1",trans=fade)
    play se "SGSE024"


    $ stopvoc("OKA")
    play OKA "OKA06A_OKA0007"
    $ current_voice = "voice/OKA06A_OKA0007.ogg"
    "伦太郎" "「真由理！」"
    "打开门呼唤着她的名字。"
    "桶子坐在电脑桌前，就像往常一样。"
    $ stopvoc("OKA")
    play OKA "OKA06A_OKA0008"
    $ current_voice = "voice/OKA06A_OKA0008.ogg"
    "伦太郎" "「真由理，真由理！」"
    window hide


    $ loadBG(2,"BG03A4")



    $ stopvoc("OKA")
    play OKA "OKA06A_OKA0009"
    $ current_voice = "voice/OKA06A_OKA0009.ogg"
    "伦太郎" "「桶子。有没有看见真由理？」"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASB03"),"True","lh/DAR_ASB03a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "OKA06A_DAR0000"
    $ current_voice = "voice/OKA06A_DAR0000.ogg"
    "至" "「冈伦……」"
    $ stopvoc("OKA")
    play OKA "OKA06A_OKA0010"
    $ current_voice = "voice/OKA06A_OKA0010.ogg"
    "伦太郎" "「嗯？桶子怎么了？你知道真由理在哪吗？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA09"),"True","lh/DAR_ASA09a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "OKA06A_DAR0001"
    $ current_voice = "voice/OKA06A_DAR0001.ogg"
    "至" "「这个……抱歉，我不知道」"
    $ stopvoc("OKA")
    play OKA "OKA06A_OKA0011"
    $ current_voice = "voice/OKA06A_OKA0011.ogg"
    "伦太郎" "「嗯，这样啊。这样啊……」"
    $ stopvoc("DAR")
    play DAR "OKA06A_DAR0002"
    $ current_voice = "voice/OKA06A_DAR0002.ogg"
    "至" "「…………」"
    $ stopvoc("OKA")
    play OKA "OKA06A_OKA0012"
    $ current_voice = "voice/OKA06A_OKA0012.ogg"
    "伦太郎" "「怎么了，桶子？」"
    $ stopvoc("DAR")
    play DAR "OKA06A_DAR0003"
    $ current_voice = "voice/OKA06A_DAR0003.ogg"
    "至" "「没事，没什么。我今天还有事，现在要走了」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    "就像是逃开我一样，桶子迅速地做起了回去的准备。"
    "如果我的记忆是对的话，今天桶子应该没有重要的事情吧……"
    window hide



    $ loadBG(0,"BG01A",trans=fade)

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA09"),"True","lh/DAR_ASA09a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    $ stopvoc("DAR")
    play DAR "OKA06A_DAR0004"
    $ current_voice = "voice/OKA06A_DAR0004.ogg"
    "至" "「明天也有事情，再见面应该是后天了」"
    $ stopvoc("OKA")
    play OKA "OKA06A_OKA0013"
    $ current_voice = "voice/OKA06A_OKA0013.ogg"
    "伦太郎" "「嗯，这样啊……」"
    $ stopvoc("DAR")
    play DAR "OKA06A_DAR0005"
    $ current_voice = "voice/OKA06A_DAR0005.ogg"
    "至" "「那就再见啦」"
    $ stopvoc("OKA")
    play OKA "OKA06A_OKA0014"
    $ current_voice = "voice/OKA06A_OKA0014.ogg"
    "伦太郎" "「再见。看到真由理的话就联系我啊！」"
    $ stopvoc("DAR")
    play DAR "OKA06A_DAR0006"
    $ current_voice = "voice/OKA06A_DAR0006.ogg"
    "至" "「………」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    play se "SGSE024"
    "桶子无言地走了出去。"
    window hide


    $ loadBG(2,"BG02A1")



    "Ｌａｂ里没有人了。"
    "我想见到的真由理，却怎样都觅之不得。"
    "没办法了，只能向羊驼司令报告。"
    "我从口袋中取出羊驼面具，戴在头上——"
    hide screen phoneSD1
    window hide
    $ loadBG(3,"IBG019A",png=True,hold=True)
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA01"),"True","lh/MAY_CSA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with dissolve
    hide background-png 
    with Dissolve(1)




    show screen phoneSD1
    play bgm "FD2BGM11"

    $ stopvoc("MAY")
    play MAY "OKA06A_MAY0000"
    $ current_voice = "voice/OKA06A_MAY0000.ogg"
    "真由理" "「嘟噜噜」"
    $ stopvoc("OKA")
    play OKA "OKA06A_OKA0015a"
    $ current_voice = "voice/OKA06A_OKA0015a.ogg"
    "伦太郎" "「啊……！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSB03"),"True","lh/MAY_CSB03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "OKA06A_MAY0001"
    $ current_voice = "voice/OKA06A_MAY0001.ogg"
    "真由理" "「咦？桶子君呢？」"
    $ stopvoc("OKA")
    play OKA "OKA06A_OKA0015b"
    $ current_voice = "voice/OKA06A_OKA0015b.ogg"
    "伦太郎" "「刚刚回去了」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA04"),"True","lh/MAY_CSA04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "OKA06A_MAY0002"
    $ current_voice = "voice/OKA06A_MAY0002.ogg"
    "真由理" "「嗯，还想让大家尝尝酱汁满满的炸鸡块Ｎｏ．１呢！」"
    $ stopvoc("OKA")
    play OKA "OKA06A_OKA0016"
    $ current_voice = "voice/OKA06A_OKA0016.ogg"
    "伦太郎" "「哈哈哈……」"
    "听到真由理的声音让我放下心来。"
    "之前积累的感情就像没有存在过一样。"
    "我该在的地方，从很早以前开始，就只有这里。"
    "是救了人质真由理的正义的伙伴，羊驼人。"
    "我会一直、一直打败恶人的……"
    "一直、一直……"

    hide screen phoneSD1
    window hide



    stop bgm 




    return
