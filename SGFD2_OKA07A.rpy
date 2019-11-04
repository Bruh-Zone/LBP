label SGFD2_OKA07A:


    window hide


    $ loadBG(0,"BG_BLACK")
    pause 2
    $ RcvMail(3)
    $ RcvMail(4)
    $ RcvMail(5)
    $ RcvMail(6)
    $ RcvMail(7)

    play se "SGSE200L" loop



    $ date="8/13"
    $ day = "FRI"
    hide screen phonebtn
    hide screen phoneSD1

    $ stopvoc("MAY")
    play MAY "OKA07A_MAY0000"
    $ current_voice = "voice/OKA07A_MAY0000.ogg"
    "真由理" "「早上好。喂，冈伦！已经到起床的时间了哦」"
    $ stopvoc("MAY")
    play MAY "OKA07A_MAY0001"
    $ current_voice = "voice/OKA07A_MAY0001.ogg"
    "真由理" "「真是的，快起来！冈伦，快起来！」"
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0000"
    $ current_voice = "voice/OKA07A_OKA0000.ogg"
    "伦太郎" "「呼……嗯……嗯嗯……」"
    window hide


    $ loadBG(0,"BG02AS1")

    play se "SGSE056"



    show screen phonebtn
    show screen phoneSD1
    "在真由理的叫醒声中，我迷迷糊糊地醒来。"
    "那件事后之后整整两天，我都缩在Lab中发呆。"
    "正好桶子也没来，只有我与真由理，可以悠哉地度过。"
    "啊啊，什么都不做也很好啊……"
    "就这样一直，半梦半醒地待在梦与现实的狭缝间……"
    $ stopvoc("MAY")
    play MAY "OKA07A_MAY0002"
    $ current_voice = "voice/OKA07A_MAY0002.ogg"
    "真由理" "「冈伦冈伦！我说冈伦」"
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0001"
    $ current_voice = "voice/OKA07A_OKA0001.ogg"
    "伦太郎" "「呼……嗯，真由理啊」"
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0002"
    $ current_voice = "voice/OKA07A_OKA0002.ogg"
    "伦太郎" "「我已经累了，让我稍微睡一下……」"
    $ stopvoc("MAY")
    play MAY "OKA07A_MAY0003"
    $ current_voice = "voice/OKA07A_MAY0003.ogg"
    "真由理" "「但是，不早点起来的话——！」"
    hide screen phoneSD1
    window hide

    stop se
    play se "SGSE024"
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_OKA003A"]]["Check"]=True
    $ loadBG(0,"EV_OKA003A",trans=Fade(0.5,1,1,color="fff"))
    stop se


    hide screen phonebtn
    $ stopvoc("CRS")
    play CRS "OKA07A_CRS0000"
    $ current_voice = "voice/OKA07A_CRS0000.ogg"
    "红莉栖？" "「——————」"
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0003"
    $ current_voice = "voice/OKA07A_OKA0003.ogg"
    "伦太郎" "「嗯……？」"
    "耀眼的晨光从外面照了进来。"
    "入口的门被谁打开了，当我看到那个剪影的时候，我不禁怀疑起了自己的眼睛。"
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0004"
    $ current_voice = "voice/OKA07A_OKA0004.ogg"
    "伦太郎" "「唔，你——」"
    window hide
    play bgm "FD2BGM08" fadein 1.2

    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0005"
    $ current_voice = "voice/OKA07A_OKA0005.ogg"
    "伦太郎" "「红莉栖——？这不是牧濑红莉栖吗！」"
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0006"
    $ current_voice = "voice/OKA07A_OKA0006.ogg"
    "伦太郎" "「好久不见！你怎么来了？或者说，怎么突然来了！梦……这是梦吗？」"
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0007"
    $ current_voice = "voice/OKA07A_OKA0007.ogg"
    "伦太郎" "「好痛啊啊！唔，果然是现实！我就知道！我怎么可能这么简单被骗——」"
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0008"
    $ current_voice = "voice/OKA07A_OKA0008.ogg"
    "伦太郎" "「……红莉栖？喂，怎么了？给点反应好不好？」 "
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0009"
    $ current_voice = "voice/OKA07A_OKA0009.ogg"
    "伦太郎" "「哈哈，难道是被久违地再见感动的说不出话来了吗。我明白，我明白你的心情」"
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0010"
    $ current_voice = "voice/OKA07A_OKA0010.ogg"
    "伦太郎" "「无论你怎么否认，你都是Ｌａｂｍｅｍ００４！隔这么久再度回到重要的地方，就连话都说不出了吧？」 "
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0011"
    $ current_voice = "voice/OKA07A_OKA0011.ogg"
    "伦太郎" "「不对……真的是好久不见啊。你现在是在欧洲的研究机关工作吧？」"
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0012"
    $ current_voice = "voice/OKA07A_OKA0012.ogg"
    "伦太郎" "「但是，为什么特意从那么远的地方回来？而且还是以这种打扮——？」"
    window hide



    $ loadBG(2,"BG01A")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_HSA03"),"True","lh/CRS_HSA03a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    show screen phonebtn
    show screen phoneSD1
    "红莉栖的衣服是能吸收夏日阳光的黑色。"
    "她那周身的黑衣，就像是丧服——"
    "不对……是真的丧服吧……？"
    "这怎么可能……"
    "我进行时间跳跃后，应该救了Ｍｒ．布朗的命。"
    "完美地修复了过去的错误。"
    "在这条世界线上，应该没有任何人死去——"
    $ stopvoc("CRS")
    play CRS "OKA07A_CRS0001"
    $ current_voice = "voice/OKA07A_CRS0001.ogg"
    "红莉栖" "「这是为了真由理」"
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0013"
    $ current_voice = "voice/OKA07A_OKA0013.ogg"
    "伦太郎" "「真由理？可是——」"
    window hide


    $ loadBG(2,"BG02A1")



    "我瞄了一眼身边。"
    window hide



    $ loadBG(2,"BG02AS1")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CMA02"),"True","lh/MAY_CMA02a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    $ stopvoc("MAY")
    play MAY "OKA07A_MAY0004"
    $ current_voice = "voice/OKA07A_MAY0004.ogg"
    "真由理" "「嘟嘟噜—……」"
    "身边站着真由理。"
    "她的确出现在我的视线中。"
    "在……还在。"
    "你在吧，真由理？"
    "你一直是，我的人质吧？"
    "一直，待在这个Ｌａｂ的吧？"
    $ stopvoc("CRS")
    play CRS "OKA07A_CRS0002"
    $ current_voice = "voice/OKA07A_CRS0002.ogg"
    "红莉栖" "「——！！」"
    window hide



    $ loadBG(2,"BG01A")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_HLB04"),"True","lh/CRS_HLB04a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    "不知何时，红莉栖走到了我的面前。"
    "就这样将我的脸皮——不对。"
    hide screen phoneSD1
    window hide
    $ loadBG(0,"IBG019A",png=True,hide=False)

    hide screen phonebtn
    "抓住我戴着睡觉的羊驼面具。"

    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0014"
    $ current_voice = "voice/OKA07A_OKA0014.ogg"
    "伦太郎" "「呐……喂、喂！住手！这样做的话——」"
    $ stopvoc("MAY")
    play MAY "OKA07A_MAY0005"
    $ current_voice = "voice/OKA07A_MAY0005.ogg"
    "真由理" "「克里斯酱……求你了，乱来的话——」"
    "真由理的声音就像是没传到红莉栖耳中一样。"
    $ stopvoc("CRS")
    play CRS "OKA07A_CRS0003"
    $ current_voice = "voice/OKA07A_CRS0003.ogg"
    "红莉栖" "「你要带着这面具，带到什么时候——」"
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0015"
    $ current_voice = "voice/OKA07A_OKA0015.ogg"
    "伦太郎" "「喂！住手——住手！！」"
    $ stopvoc("CRS")
    play CRS "OKA07A_CRS0004"
    $ current_voice = "voice/OKA07A_CRS0004.ogg"
    "红莉栖" "「快点醒过来——！！」"
    window hide
    play se "SGSE056"


    hide background-png  with moveouttop
    show screen phonebtn
    show screen phoneSD1
    "红莉栖将羊驼面具从我的头上取下。"
    "随后。"
    window hide



    $ loadBG(2,"BG02AS1")



    "真由理的身影从Ｌａｂ中消失了。"
    window hide


    $ loadBG(2,"BG02A1")



    "完全，消失了。"
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0016"
    $ current_voice = "voice/OKA07A_OKA0016.ogg"
    "伦太郎" "「啊、啊……啊……」"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_HMA04"),"True","lh/CRS_HMA04a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "OKA07A_CRS0005"
    $ current_voice = "voice/OKA07A_CRS0005.ogg"
    "红莉栖" "「邮件没有回复，事情的经过我已经从桥田那里了解了」"
    $ stopvoc("CRS")
    play CRS "OKA07A_CRS0006"
    $ current_voice = "voice/OKA07A_CRS0006.ogg"
    "红莉栖" "「你自从那件事之后，就一直很奇怪」"
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0017"
    $ current_voice = "voice/OKA07A_OKA0017.ogg"
    "伦太郎" "「我……很奇怪……？」"
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0018"
    $ current_voice = "voice/OKA07A_OKA0018.ogg"
    "伦太郎" "「你究竟在说什么……」"
    $ stopvoc("CRS")
    play CRS "OKA07A_CRS0007"
    $ current_voice = "voice/OKA07A_CRS0007.ogg"
    "红莉栖" "「不要逃避。你其实全都记得吧？」"
    $ stopvoc("CRS")
    play CRS "OKA07A_CRS0008"
    $ current_voice = "voice/OKA07A_CRS0008.ogg"
    "红莉栖" "「就在距今天，1年前——」"
    $ stopvoc("CRS")
    play CRS "OKA07A_CRS0009"
    $ current_voice = "voice/OKA07A_CRS0009.ogg"
    "红莉栖" "「在这个Ｌａｂ中——就在Ｒｏｕｎｄｅｒ被袭击那天的事情」"
    stop bgm 
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0019"
    $ current_voice = "voice/OKA07A_OKA0019.ogg"
    "伦太郎" "「————！！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_HMC04"),"True","lh/CRS_HMC04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    "我从红莉栖手中夺回羊驼面具——"
    window hide


    $ loadBG(2,"BG01A")



    $ stopvoc("CRS")
    play CRS "OKA07A_CRS0010"
    $ current_voice = "voice/OKA07A_CRS0010.ogg"
    "红莉栖" "「等等，冈部！」"
    "就这样跑出了Ｌａｂ。"
    hide screen phonebtn
    hide screen phoneSD1
    window hide
    play se "SGSE316"
    $ loadBG(0,"BG_Black",hold=True)
    with Fade(0.5,1,0.5)
    show mayushi_flashback 
    $ renpy.pause(1,hard=True)
    hide mayushi_flashback 







    $ loadBG(0,"BG05A2",trans=Fade(0,2,1))

    show screen phoneSD1
    play bgm "FD2BGM06"
    "怎么可能——"
    "不可能、不可能、不可能不可能不可能——！！"
    "怎么可能！"
    "这种事情，绝对不可能！"
    "我是正常的！"
    "绝对是，正常的——！"
    $ stopvoc("SUZ")
    play SUZ "OKA07A_SUZ0000"
    $ current_voice = "voice/OKA07A_SUZ0000.ogg"
    "铃羽" "「冈部伦太郎——！」"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_ASB02"),"True","lh/SUZ_ASB02a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    "显像管工房那边传来了铃羽的声音。"
    "比往常更严肃的表情。"
    $ stopvoc("SUZ")
    play SUZ "OKA07A_SUZ0001"
    $ current_voice = "voice/OKA07A_SUZ0001.ogg"
    "铃羽" "「没事吧？牧濑红莉栖对你做什么了吗！？」"
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0020"
    $ current_voice = "voice/OKA07A_OKA0020.ogg"
    "伦太郎" "「没有，没事……」"
    "怎么这么说？"
    "为什么铃羽会问我这个问题？"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_ASB04"),"True","lh/SUZ_ASB04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "OKA07A_SUZ0002"
    $ current_voice = "voice/OKA07A_SUZ0002.ogg"
    "铃羽" "「太好了」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_ASB02"),"True","lh/SUZ_ASB02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "OKA07A_SUZ0003"
    $ current_voice = "voice/OKA07A_SUZ0003.ogg"
    "铃羽" "「如果她要是做了什么，我立刻就去打倒她——不过现在算了」"
    $ stopvoc("SUZ")
    play SUZ "OKA07A_SUZ0004"
    $ current_voice = "voice/OKA07A_SUZ0004.ogg"
    "铃羽" "「虽说她是我的仇人」"
    hide screen phonebtn

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_ASA06"),"True","lh/SUZ_ASA06a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "OKA07A_SUZ0005"
    $ current_voice = "voice/OKA07A_SUZ0005.ogg"
    "铃羽" "「今天，椎名真由理的性命——」"
    hide screen phoneSD1
    window hide
    stop bgm
    hide screen phonebtn
    hide screen phoneSD1
    window hide
    play se "SGSE316"
    show expression Solid("000") as black zorder 100 
    with Fade(0.5,1,0.5)
    show mayushi_flashback zorder 101 
    $ renpy.pause(1,hard=True)
    hide mayushi_flashback 
    hide black 
    hide lh5 








    show screen phonebtn
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0021"
    $ current_voice = "voice/OKA07A_OKA0021.ogg"
    "伦太郎" "「————！！」"
    play bgm "BGM25"


    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_ASA03"),"True","lh/SUZ_ASA03a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "OKA07A_SUZ0006"
    $ current_voice = "voice/OKA07A_SUZ0006.ogg"
    "铃羽" "「冈部伦太郎！？」"
    play se "SGSE182"

    hide screen phoneSD1
    window hide



    $ loadBG(0,"BG18A2",trans=fade)
    $ targetmailid = gc["ScriptMacros"]["FM_OKA07A_RECV_SUZ01"]
    if phonemailring!= "":
        play se phonemailring
    if persistent.skipmail==False:
        $ renpy.choice_for_skipping()
    if targetmailid != "":
        $ RcvMail(targetmailid)
        $ targetmailid=""

    show screen phoneSD1
    "骗人、骗人！"
    "这种话，我才不会相信！"
    "因为真由理一直在我身边！"
    "比如，没错——就像我以前阻止巴士劫案时！"
    hide screen phoneSD1
    window hide



    $ loadBG(0,"BG26A",trans=fade)
    stop se

    show screen phoneSD1
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0022"
    $ current_voice = "voice/OKA07A_OKA0022.ogg"
    "伦太郎" "「菲利斯！」"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_DSA02"),"True","lh/FEI_DSA02a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FEI")
    play FEI "OKA07A_FEI0000"
    $ current_voice = "voice/OKA07A_FEI0000.ogg"
    "菲利斯" "「凶真，你终于来了喵。但是，这么着急来我家拜访是为什么喵？」"
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0023"
    $ current_voice = "voice/OKA07A_OKA0023.ogg"
    "伦太郎" "「我说，之前你在雷Ｎｅｔ宣传巴士上的时候——」"
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0024"
    $ current_voice = "voice/OKA07A_OKA0024.ogg"
    "伦太郎" "「真由理跟你一起，被劫为人质吧！？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_DSA03"),"True","lh/FEI_DSA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FEI")
    play FEI "OKA07A_FEI0001"
    $ current_voice = "voice/OKA07A_FEI0001.ogg"
    "菲利斯" "「诶……」"
    "菲利斯的笑容，瞬间蒙上了阴影。"
    $ stopvoc("FEI")
    play FEI "OKA07A_FEI0002"
    $ current_voice = "voice/OKA07A_FEI0002.ogg"
    "菲利斯" "「在那里的，只有菲利斯一个人喵」"
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0025"
    $ current_voice = "voice/OKA07A_OKA0025.ogg"
    "伦太郎" "「啊……哈哈……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_DSC03"),"True","lh/FEI_DSC03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FEI")
    play FEI "OKA07A_FEI0003"
    $ current_voice = "voice/OKA07A_FEI0003.ogg"
    "菲利斯" "「而且……凶真，我希望你能认真听——」"
    hide screen phonebtn
    $ stopvoc("FEI")
    play FEI "OKA07A_FEI0004"
    $ current_voice = "voice/OKA07A_FEI0004.ogg"
    "菲利斯" "「真由喜在1年前已经——」"
    hide screen phoneSD1
    window hide
    stop bgm
    hide screen phonebtn
    hide screen phoneSD1
    window hide
    play se "SGSE316"
    show expression Solid("000") as black zorder 100 
    with Fade(0.5,1,0.5)
    show mayushi_flashback zorder 101 
    $ renpy.pause(1,hard=True)
    hide mayushi_flashback 
    hide black 
    hide lh5 







    show screen phonebtn
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0026"
    $ current_voice = "voice/OKA07A_OKA0026.ogg"
    "伦太郎" "「————！！」"
    play bgm "BGM24"


    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_DSC05"),"True","lh/FEI_DSC05a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FEI")
    play FEI "OKA07A_FEI0005"
    $ current_voice = "voice/OKA07A_FEI0005.ogg"
    "菲利斯" "「凶真！！」"
    hide screen phoneSD1
    window hide



    $ loadBG(0,"BG18A2",trans=fade)

    show screen phoneSD1
    "１年前？"
    "她说１年前怎么了？"
    "我已经——什么都不记得了——"
    "不想——回忆起来——"
    "况且，还有其他真由理跟我在一起的记录！"
    "例如——例如，我该，怎样证明——"

    $ targetmailid = gc["ScriptMacros"]["FM_OKA07A_RECV_MOE01"]
    if phonemailring!= "":
        play se phonemailring
    if persistent.skipmail==False:
        $ renpy.choice_for_skipping()
    if targetmailid != "":
        $ RcvMail(targetmailid)
        $ targetmailid=""

    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0028"
    $ current_voice = "voice/OKA07A_OKA0028.ogg"
    "伦太郎" "「对了，邮件！」"
    window hide
    hide screen phonebtn
    hide screen phonebtn2
    show screen phone(interact=False)
    "邮件就是证明真由理是真实存在的证据。"
    window hide


    hide screen phonemenu
    hide screen phonebtn
    call hide_phone

    $ loadBG(0,"BG_BLACK")

    hide screen phonebtn
    "我马上开始在过去的邮件文件夹中寻找。"
    "以真由理的名字为关键词，按日期查找——"
    "按——日期——"
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0029"
    $ current_voice = "voice/OKA07A_OKA0029.ogg"
    "伦太郎" "「怎么……可能……」"
    "椎名真由理发给我的邮件。"
    "去年８月１３日后就再也没有过了。"
    window hide


    $ loadBG(0,"BG18A2")

    show screen phonebtn
    show screen phoneSD1
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0030"
    $ current_voice = "voice/OKA07A_OKA0030.ogg"
    "伦太郎" "「啊……啊啊……啊……」"
    "为什么？"
    "为什么真由理从那天之后就不再给我发邮件了？"
    "我们明明，偶尔会在Ｌａｂ中见面的！"
    "为什么，会没有继续发邮件了？"
    "难道，真由理，真的——"
    window hide


    $ loadBG(2,"IBGX048")



    hide screen phonebtn
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0031"
    $ current_voice = "voice/OKA07A_OKA0031.ogg"
    "伦太郎" "「这怎么可能啊啊啊啊啊啊！！」"
    "没错，不可能！"
    "这肯定是恶之秘密组织的阴谋！"
    "是对正义的伙伴羊驼人设下的精妙陷阱！"
    window hide


    $ loadBG(2,"BG18A2")



    show screen phonebtn

    $ targetmailid = 356

    $ LR_RM_CHANCE=3
    call CHECK_RM_RECEIVE
    "一定是社会性地屏蔽了人质真由理的存在，为了让我精神错乱！"
    call CHECK_RM_RECEIVE
    "别开玩笑了！"
    call CHECK_RM_RECEIVE
    "竟然用这么卑鄙的手法，休想让我屈服！"




    hide screen phoneSD1
    window hide



    $ loadBG(0,"BG15A",trans=fade)

    show screen phoneSD1
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0032"
    $ current_voice = "voice/OKA07A_OKA0032.ogg"
    "伦太郎" "「琉华子——！」"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='RUK')",DynamicDisplayable(mouthanime,"RUK_BSA01"),"True","lh/RUK_BSA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("RUK")
    play RUK "OKA07A_RUK0000"
    $ current_voice = "voice/OKA07A_RUK0000.ogg"
    "琉华" "「啊、冈部师傅」"
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0033"
    $ current_voice = "voice/OKA07A_OKA0033.ogg"
    "伦太郎" "「拜托你告诉我！」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='RUK')",DynamicDisplayable(mouthanime,"RUK_BLA03"),"True","lh/RUK_BLA03a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("RUK")
    play RUK "OKA07A_RUK0001"
    $ current_voice = "voice/OKA07A_RUK0001.ogg"
    "琉华" "「呀！」"
    hide screen phonebtn
    "抓住琉华子的肩膀质问。"
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0034"
    $ current_voice = "voice/OKA07A_OKA0034.ogg"
    "伦太郎" "「真由理她……真由理她……」"
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0035"
    $ current_voice = "voice/OKA07A_OKA0035.ogg"
    "伦太郎" "「在什么，地方……！？」"
    $ stopvoc("RUK")
    play RUK "OKA07A_RUK0002"
    $ current_voice = "voice/OKA07A_RUK0002.ogg"
    "琉华" "「诶……真由理吗……？」"
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0036"
    $ current_voice = "voice/OKA07A_OKA0036.ogg"
    "伦太郎" "「我明白！你们也被坏人逼迫了吧？」"
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0037"
    $ current_voice = "voice/OKA07A_OKA0037.ogg"
    "伦太郎" "「所以悄悄说也没关系！悄悄地只跟我一个人说」"
    hide screen phoneSD1
    window hide


    $ loadBG(2,"BG_BLACK")





    hide screen phonebtn
    play se "SGSE359"
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0038"
    $ current_voice = "voice/OKA07A_OKA0038.ogg"
    "伦太郎" "「告诉我……真由理在的地方……！」"
    $ stopvoc("RUK")
    play RUK "OKA07A_RUK0003"
    $ current_voice = "voice/OKA07A_RUK0003.ogg"
    "琉华" "「冈部师傅……」"

    stop bgm 
    "什么东西，啪嗒一声从我及膝的白大褂上掉下来。"
    $ stopvoc("RUK")
    play RUK "OKA07A_RUK0004"
    $ current_voice = "voice/OKA07A_RUK0004.ogg"
    "琉华" "「啊……」"
    window hide
    stop se
    stop se


    $ loadBG(0,"BG15A")

    show expression ConditionSwitch("renpy.music.get_playing(channel='RUK')",DynamicDisplayable(mouthanime,"RUK_BLA03"),"True","lh/RUK_BLA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    $ loadBG(0,"IBG017A",png=True,hold=True,hide=False)
    with Dissolve(.5)






    hide screen phonebtn
    show screen phoneSD1
    "是从红莉栖那里抢回来的，羊驼面具——"
    "是我成为正义的伙伴所必需的东西。"
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0039"
    $ current_voice = "voice/OKA07A_OKA0039.ogg"
    "伦太郎" "「啊……原、原来如此。原来是这么回事！」"
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0040"
    $ current_voice = "voice/OKA07A_OKA0040.ogg"
    "伦太郎" "「证据！这不就是证据嘛！！」"
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0041"
    $ current_voice = "voice/OKA07A_OKA0041.ogg"
    "伦太郎" "「羊驼人的变身物品一套！能制作这个的除了真由理以外没有别人了！」"
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0042"
    $ current_voice = "voice/OKA07A_OKA0042.ogg"
    "伦太郎" "「如果不是真由理的话，这究竟是谁做的——」"
    $ stopvoc("RUK")
    play RUK "OKA07A_RUK0005"
    $ current_voice = "voice/OKA07A_RUK0005.ogg"
    "琉华" "「是，冈部师傅」"
    window hide
    play bgm "FD2BGM05"
    hide background-png 
    with moveoutbottom



    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0043"
    $ current_voice = "voice/OKA07A_OKA0043.ogg"
    "伦太郎" "「诶……」"
    $ stopvoc("RUK")
    play RUK "OKA07A_RUK0006"
    $ current_voice = "voice/OKA07A_RUK0006.ogg"
    "琉华" "「我……看见了」"
    $ stopvoc("RUK")
    play RUK "OKA07A_RUK0007"
    $ current_voice = "voice/OKA07A_RUK0007.ogg"
    "琉华" "「大约是那个事件发生后的３个月。冈部师傅走进了，真由理酱经常去的出售Ｃｏｓｐｌａｙ服装材料的店。」"
    $ stopvoc("RUK")
    play RUK "OKA07A_RUK0008"
    $ current_voice = "voice/OKA07A_RUK0008.ogg"
    "琉华" "「刚开始……我还以为是看错了……」"
    $ stopvoc("RUK")
    play RUK "OKA07A_RUK0009"
    $ current_voice = "voice/OKA07A_RUK0009.ogg"
    "琉华" "「羊驼人活跃在秋叶原，就在看见了那件事之后」"
    $ stopvoc("RUK")
    play RUK "OKA07A_RUK0010"
    $ current_voice = "voice/OKA07A_RUK0010.ogg"
    "琉华" "「后来也偶尔在那家店中看见……终于，之前……」"
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0044"
    $ current_voice = "voice/OKA07A_OKA0044.ogg"
    "伦太郎" "「可、可是、是吧！也有可能是我代替真由理去买东西！」"
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0045"
    $ current_voice = "voice/OKA07A_OKA0045.ogg"
    "伦太郎" "「况且我，根本就不会针线活！」"
    $ stopvoc("RUK")
    play RUK "OKA07A_RUK0011"
    $ current_voice = "voice/OKA07A_RUK0011.ogg"
    "琉华" "「试试看如何？」"
    $ stopvoc("RUK")
    play RUK "OKA07A_RUK0012"
    $ current_voice = "voice/OKA07A_RUK0012.ogg"
    "琉华" "「我有针线」"
    "平时就带在身上吧，琉华子拿出小小的裁缝工具。"
    $ stopvoc("RUK")
    play RUK "OKA07A_RUK0013"
    $ current_voice = "voice/OKA07A_RUK0013.ogg"
    "琉华" "「试试看，不是就知道了」"
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0046"
    $ current_voice = "voice/OKA07A_OKA0046.ogg"
    "伦太郎" "「怎么……会有，这种事……」"
    "我没有接过工具。"
    "我害怕接下。"
    "如果使用时间机器，能随时回到过去。"
    "就算完全不会用裁缝工具的我，如果不停地累积记忆，应该也会缝纫。"
    "如果我只是为了逃避这段过去——"
    $ stopvoc("RUK")
    play RUK "OKA07A_RUK0014"
    $ current_voice = "voice/OKA07A_RUK0014.ogg"
    "琉华" "「冈部师傅。我……知道你很喜欢真由理。但是——」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='RUK')",DynamicDisplayable(mouthanime,"RUK_BLA02"),"True","lh/RUK_BLA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("RUK")
    play RUK "OKA07A_RUK0015"
    $ current_voice = "voice/OKA07A_RUK0015.ogg"
    "琉华" "「已经不行了吧」"
    $ stopvoc("RUK")
    play RUK "OKA07A_RUK0016"
    $ current_voice = "voice/OKA07A_RUK0016.ogg"
    "琉华" "「自己缝纫……自己制作出像真由理能做出的衣服……」"
    $ stopvoc("RUK")
    play RUK "OKA07A_RUK0017"
    $ current_voice = "voice/OKA07A_RUK0017.ogg"
    "琉华" "「这样，又回陷入现在还跟以前一样的幻觉中……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='RUK')",DynamicDisplayable(mouthanime,"RUK_BLA04"),"True","lh/RUK_BLA04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("RUK")
    play RUK "OKA07A_RUK0018"
    $ current_voice = "voice/OKA07A_RUK0018.ogg"
    "琉华" "「这样，就太悲剧了……！」"
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0047"
    $ current_voice = "voice/OKA07A_OKA0047.ogg"
    "伦太郎" "「————！！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='RUK')",DynamicDisplayable(mouthanime,"RUK_BLA02"),"True","lh/RUK_BLA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("RUK")
    play RUK "OKA07A_RUK0019"
    $ current_voice = "voice/OKA07A_RUK0019.ogg"
    "琉华" "「冈部师傅！！」"
    hide screen phoneSD1
    window hide

    stop bgm 



    $ loadBG(0,"IBGX048")

    $ targetmailid = 357

    if phonemailring!= "":
        play se phonemailring
    if persistent.skipmail==False:
        $ renpy.choice_for_skipping()
    if targetmailid != "":
        $ RcvMail(targetmailid)
        $ targetmailid=""





    hide screen phonebtn
    show screen phoneSD1
    "不对！不对不对！"
    "那套羊驼服，是真由理为我制作的！"
    "因为是真由理做给我的，所以我才能成为正义的伙伴！"
    "为了救被当成人质的真由理，成为了正义的伙伴！"
    "是因为真由理……也是为了真由理……"
    "正义的伙伴羊驼人，冈部伦太郎是存在的……！"
    hide screen phoneSD1
    window hide



    $ loadBG(0,"BG64A",trans=fade)



    show screen phonebtn
    show screen phoneSD1
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0048"
    $ current_voice = "voice/OKA07A_OKA0048.ogg"
    "伦太郎" "「是吧……对吧？」"
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0049"
    $ current_voice = "voice/OKA07A_OKA0049.ogg"
    "伦太郎" "「真由理……真由理……」"
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0050"
    $ current_voice = "voice/OKA07A_OKA0050.ogg"
    "伦太郎" "「就算是谎话……也继续说下去啊……说啊……」"
    $ stopvoc("CRS")
    play CRS "OKA07A_CRS0011"
    $ current_voice = "voice/OKA07A_CRS0011.ogg"
    "红莉栖" "「冈部……」"
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0051"
    $ current_voice = "voice/OKA07A_OKA0051.ogg"
    "伦太郎" "「…………」"
    "我无力地转过身。"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_HSA04"),"True","lh/CRS_HSA04a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    "那里站着身着丧服的红莉栖。"
    "但是，真由理却不在。"
    "不在。"
    "就算找遍全世界。"
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0052"
    $ current_voice = "voice/OKA07A_OKA0052.ogg"
    "伦太郎" "「啊哈……啊哈哈哈哈哈……」"
    window hide
    $ loadBG(0,"IBG017A",png=True,hold=True,hide=False)
    with moveinbottom



    hide screen phonebtn
    "也许，现在戴上面具，还能，见到她吗？"
    "大概，肯定，会吧。"
    "因为，真由理是存在于想象中的。"
    window hide
    hide background-png 
    $ loadBG(0,"BG64A")











    "眼前的石头，已经，刻上了真由理的名字。"
    $ stopvoc("CRS")
    play CRS "OKA07A_CRS0012"
    $ current_voice = "voice/OKA07A_CRS0012.ogg"
    "红莉栖" "「接下来，是从我见到的你的行为中推导出来的，合理推测」"
    $ stopvoc("CRS")
    play CRS "OKA07A_CRS0013"
    $ current_voice = "voice/OKA07A_CRS0013.ogg"
    "红莉栖" "「你，进行了时空跳跃，对吧？」"
    $ stopvoc("CRS")
    play CRS "OKA07A_CRS0014"
    $ current_voice = "voice/OKA07A_CRS0014.ogg"
    "红莉栖" "「为了阻止真由理的死」"
    $ stopvoc("CRS")
    play CRS "OKA07A_CRS0015"
    $ current_voice = "voice/OKA07A_CRS0015.ogg"
    "红莉栖" "「没有与我们商量，一直一个人，在战斗着吧？」"
    $ stopvoc("CRS")
    play CRS "OKA07A_CRS0016"
    $ current_voice = "voice/OKA07A_CRS0016.ogg"
    "红莉栖" "「一次又一次，想要救真由理对吧？」"
    $ stopvoc("CRS")
    play CRS "OKA07A_CRS0017"
    $ current_voice = "voice/OKA07A_CRS0017.ogg"
    "红莉栖" "「但是——救不了」"
    $ stopvoc("CRS")
    play CRS "OKA07A_CRS0018"
    $ current_voice = "voice/OKA07A_CRS0018.ogg"
    "红莉栖" "「你，救不了，真由理」"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_AT_FIELD"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_AT_FIELD"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_AT_FIELD"])
    $ stopvoc("CRS")
    play CRS "OKA07A_CRS0019"
    $ current_voice = "voice/OKA07A_CRS0019.ogg"
    "红莉栖" "「因为被名为{color=#f00}Ａｔｒａｃｔ　Ｆｉｅｌｄ{/color}之壁所阻挡着」"
    $ stopvoc("CRS")
    play CRS "OKA07A_CRS0020"
    $ current_voice = "voice/OKA07A_CRS0020.ogg"
    "红莉栖" "「真由理，还是，死了」"
    hide screen phoneSD1
    window hide


    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_OKA004A"]]["Check"]=True


    $ loadBG(2,"EV_OKA004A")



    hide screen phonebtn
    play se "SGSE359"
    "没错。"
    "死了。"
    "真由理，死了。"
    "死去了。"
    "一次、又一次——"
    "一次又一次一次又一次一次又一次一次又一次一次又一次一次又一次一次又一次一次又一次一次又一次一次又一次一次又一次一次又一次一次又一次一次又一次——！！"
    "我没办法救她。"
    "没办法救被当成人质的真由理。"
    "不停重复的痛苦。"
    "不停重复的死亡。"
    "已经无法继续忍受了。"
    "连脑袋都变得奇怪了。"
    "所以停止了战斗。"
    "接受了命运。"
    "全部，放弃了。"
    $ stopvoc("CRS")
    play CRS "OKA07A_CRS0021"
    $ current_voice = "voice/OKA07A_CRS0021.ogg"
    "红莉栖" "「但是，你身边有时间机器」"
    $ stopvoc("CRS")
    play CRS "OKA07A_CRS0022"
    $ current_voice = "voice/OKA07A_CRS0022.ogg"
    "红莉栖" "「是有着能够改变命运，拯救真由理的机器」"
    $ stopvoc("CRS")
    play CRS "OKA07A_CRS0023"
    $ current_voice = "voice/OKA07A_CRS0023.ogg"
    "红莉栖" "「是告知无法拯救真由理命运的冷酷机器」"
    $ stopvoc("CRS")
    play CRS "OKA07A_CRS0024"
    $ current_voice = "voice/OKA07A_CRS0024.ogg"
    "红莉栖" "「你被痛苦地夹在这两者的矛盾之中，为此诞生了羊驼人」"
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0053"
    $ current_voice = "voice/OKA07A_OKA0053.ogg"
    "伦太郎" "「我……创造了羊驼人？」"
    $ stopvoc("CRS")
    play CRS "OKA07A_CRS0025"
    $ current_voice = "voice/OKA07A_CRS0025.ogg"
    "红莉栖" "「没错。使用时间机器，更正错误过去的正义的伙伴」"
    $ stopvoc("CRS")
    play CRS "OKA07A_CRS0026"
    $ current_voice = "voice/OKA07A_CRS0026.ogg"
    "红莉栖" "「从恶之秘密组织手中救出作为人质的真由理的秋叶原英雄」"
    $ stopvoc("CRS")
    play CRS "OKA07A_CRS0027"
    $ current_voice = "voice/OKA07A_CRS0027.ogg"
    "红莉栖" "「只要羊驼人还在行动，只要这个世上还有罪恶，真由理就继续活着」"
    $ stopvoc("CRS")
    play CRS "OKA07A_CRS0028"
    $ current_voice = "voice/OKA07A_CRS0028.ogg"
    "红莉栖" "「你让你自己这样相信着」"
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0054"
    $ current_voice = "voice/OKA07A_OKA0054.ogg"
    "伦太郎" "「…………」"
    "哑口无言，说的就是现在这种情况。"
    "正如她所说。"
    "我没有接受现实。"
    "所以，逃入了羊驼人这种虚构的英雄所创造的正义中。"
    "但是——"
    window hide



    $ loadBG(2,"BG64A")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_HSA04"),"True","lh/CRS_HSA04a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    show screen phonebtn
    show screen phoneSD1
    $ stopvoc("CRS")
    play CRS "OKA07A_CRS0029"
    $ current_voice = "voice/OKA07A_CRS0029.ogg"
    "红莉栖" "「差不多你该明白了吧？」"
    $ stopvoc("CRS")
    play CRS "OKA07A_CRS0030"
    $ current_voice = "voice/OKA07A_CRS0030.ogg"
    "红莉栖" "「这个世界，不存在绝对的正义」"
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0055"
    $ current_voice = "voice/OKA07A_OKA0055.ogg"
    "伦太郎" "「绝对的……正义……」"
    $ stopvoc("CRS")
    play CRS "OKA07A_CRS0031"
    $ current_voice = "voice/OKA07A_CRS0031.ogg"
    "红莉栖" "「正义的另一边，还有另一种正义——选择穿越时空回到过去，只不过是，去选择哪边是正义而已」"
    $ stopvoc("CRS")
    play CRS "OKA07A_CRS0032"
    $ current_voice = "voice/OKA07A_CRS0032.ogg"
    "红莉栖" "「你，能肯定你就是正义？」"
    $ stopvoc("CRS")
    play CRS "OKA07A_CRS0033"
    $ current_voice = "voice/OKA07A_CRS0033.ogg"
    "红莉栖" "「只用一只手来承受命运太沉重了」"
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0056"
    $ current_voice = "voice/OKA07A_OKA0056.ogg"
    "伦太郎" "「我，只是……」"
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0057"
    $ current_voice = "voice/OKA07A_OKA0057.ogg"
    "伦太郎" "「想要救真由理」"
    $ stopvoc("CRS")
    play CRS "OKA07A_CRS0034"
    $ current_voice = "voice/OKA07A_CRS0034.ogg"
    "红莉栖" "「那个真由理是借口」"
    $ stopvoc("CRS")
    play CRS "OKA07A_CRS0035"
    $ current_voice = "voice/OKA07A_CRS0035.ogg"
    "红莉栖" "「是你为了让你自己的行为正当化的幻觉」"
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0058"
    $ current_voice = "voice/OKA07A_OKA0058.ogg"
    "伦太郎" "「你的天才头脑……真的让人很讨厌」"
    "……是啊，没错。"
    "我没办法接受自己的命运，而选择了逃了出来。"
    "逃出来之后，创造了理想中的真由理。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_HSC06"),"True","lh/CRS_HSC06a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "OKA07A_CRS0036"
    $ current_voice = "voice/OKA07A_CRS0036.ogg"
    "红莉栖" "「我说……」"
    $ stopvoc("CRS")
    play CRS "OKA07A_CRS0037"
    $ current_voice = "voice/OKA07A_CRS0037.ogg"
    "红莉栖" "「如果你能帮忙我们的研究，能够拯救将来会饿死的几亿人」"
    $ stopvoc("CRS")
    play CRS "OKA07A_CRS0038"
    $ current_voice = "voice/OKA07A_CRS0038.ogg"
    "红莉栖" "「数不清的罪恶，能够从源头上被切断」"
    $ stopvoc("CRS")
    play CRS "OKA07A_CRS0039"
    $ current_voice = "voice/OKA07A_CRS0039.ogg"
    "红莉栖" "「追求大部分人的最大幸福。这才是，改变未来的人应尽的义务」"
    "红莉栖的话，正确到只要听着就会胸口隐隐发疼。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_HSA01"),"True","lh/CRS_HSA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "OKA07A_CRS0040"
    $ current_voice = "voice/OKA07A_CRS0040.ogg"
    "红莉栖" "「冈部，求你了」"
    $ stopvoc("CRS")
    play CRS "OKA07A_CRS0041"
    $ current_voice = "voice/OKA07A_CRS0041.ogg"
    "红莉栖" "「将世界的命运放在我们的手上」"
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0059"
    $ current_voice = "voice/OKA07A_OKA0059.ogg"
    "伦太郎" "「………」"
    "我，完全无法忍受这种话。"
    "没办法听这些话。"
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0060"
    $ current_voice = "voice/OKA07A_OKA0060.ogg"
    "伦太郎" "「红莉栖」"
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0061"
    $ current_voice = "voice/OKA07A_OKA0061.ogg"
    "伦太郎" "「你变了」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_HSC04"),"True","lh/CRS_HSC04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "OKA07A_CRS0042"
    $ current_voice = "voice/OKA07A_CRS0042.ogg"
    "红莉栖" "「我……变了？」"
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0062"
    $ current_voice = "voice/OKA07A_OKA0062.ogg"
    "伦太郎" "「如果是1年前，刚进Ｌａｂ那时的你，肯定——」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_HSC06"),"True","lh/CRS_HSC06a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "OKA07A_CRS0043"
    $ current_voice = "voice/OKA07A_CRS0043.ogg"
    "红莉栖" "「那时候的我，和现在不一样」"
    $ stopvoc("CRS")
    play CRS "OKA07A_CRS0044"
    $ current_voice = "voice/OKA07A_CRS0044.ogg"
    "红莉栖" "「最开始，我没想过我会帮助ＳＥＲＮ」"
    $ stopvoc("CRS")
    play CRS "OKA07A_CRS0045"
    $ current_voice = "voice/OKA07A_CRS0045.ogg"
    "红莉栖" "「但是爸爸——」"
    "红莉栖的话卡在了喉咙中。"
    $ stopvoc("CRS")
    play CRS "OKA07A_CRS0046"
    $ current_voice = "voice/OKA07A_CRS0046.ogg"
    "红莉栖" "「因为爸爸能被接纳入ＳＥＲＮ。爸爸的研究能被认可」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_HSA01"),"True","lh/CRS_HSA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "OKA07A_CRS0047"
    $ current_voice = "voice/OKA07A_CRS0047.ogg"
    "红莉栖" "「所以我也——这样也很好吧」"
    "在说ＳＥＲＮ。"
    "将红莉栖的家人当成人质，是很简单的事情吧。"
    "她也不是自愿去协助的。"
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0063"
    $ current_voice = "voice/OKA07A_OKA0063.ogg"
    "伦太郎" "「……你妥协了」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_HSB07"),"True","lh/CRS_HSB07a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "OKA07A_CRS0048"
    $ current_voice = "voice/OKA07A_CRS0048.ogg"
    "红莉栖" "「我没想过要救全世界」"
    $ stopvoc("CRS")
    play CRS "OKA07A_CRS0049"
    $ current_voice = "voice/OKA07A_CRS0049.ogg"
    "红莉栖" "「这种想法，绝对不行。但是——冈部」"
    $ stopvoc("CRS")
    play CRS "OKA07A_CRS0050"
    $ current_voice = "voice/OKA07A_CRS0050.ogg"
    "红莉栖" "「就像你想救真由理一样，我也想救你」"
    $ stopvoc("CRS")
    play CRS "OKA07A_CRS0051"
    $ current_voice = "voice/OKA07A_CRS0051.ogg"
    "红莉栖" "「因为，现在的你，实在是太痛苦了……」"
    "她的话，温柔地沁入，我心中的伤口……"
    $ stopvoc("CRS")
    play CRS "OKA07A_CRS0052"
    $ current_voice = "voice/OKA07A_CRS0052.ogg"
    "红莉栖" "「所以，求你了」"
    $ stopvoc("CRS")
    play CRS "OKA07A_CRS0053"
    $ current_voice = "voice/OKA07A_CRS0053.ogg"
    "红莉栖" "「别当羊驼人了——来协助我们的研究」"
    $ stopvoc("CRS")
    play CRS "OKA07A_CRS0054"
    $ current_voice = "voice/OKA07A_CRS0054.ogg"
    "红莉栖" "「不要再……一个人，痛苦了……好吗？」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_HMB07"),"True","lh/CRS_HMB07a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    "红莉栖静静伸过来的手——"
    "我，并没有抓住。"
    "不想抓住。"
    "但是——"
    "连推开她的手都懒得推。"
    hide screen phoneSD1
    window hide

    stop se

    stop se

    stop bgm 



    $ loadBG(0,"BG11N4",trans=fade)

    play se "SGSE084"


    show screen phonebtn
    show screen phoneSD1
    "周围没有任何人，就算用火也不会暴露——"
    "那种地方，我只能想到这里。"
    "人工卫星消失的屋顶。"
    "右手拿着羊驼七道具(Ｓｅｖｅｎ　Ｇｅａｒ ) 「Ｓａｌｓａ・Ｆｉｒｅ　Ｇｕｎ」。"
    "使用气化的莎莎酱做成的火焰发射器。"
    "然后左手拿着——羊驼服、羊驼面具。"
    hide screen phoneSD1
    window hide


    $ loadBG(0,"BG64A",trans=Fade(0.5,1.0,0.5,color="fff"))

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_HMA05"),"True","lh/CRS_HMA05a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    hide screen phonebtn
    "红莉栖的话从理论上来说没有任何问题。"
    "所以，我应该做的事情，只有一个。"
    "不再当羊驼人，而去帮助她。"
    "我是这么想的。"
    window hide


    $ loadBG(0,"IBGX072",trans=Fade(0.5,1.0,0.5,color="fff"))

    hide screen phonebtn
    show screen phoneSD1
    "——这样，真的好吗？"
    "——我，想要这样的结局吗？"
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0064"
    $ current_voice = "voice/OKA07A_OKA0064.ogg"
    "伦太郎" "「别开玩笑了」"
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0065"
    $ current_voice = "voice/OKA07A_OKA0065.ogg"
    "伦太郎" "「谁也不会想要这种结局」"
    window hide


    $ loadBG(2,"BG11N4")



    show screen phonebtn
    show screen phoneSD1
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0066"
    $ current_voice = "voice/OKA07A_OKA0066.ogg"
    "伦太郎" "「但是，也找不到……其他的办法」"
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0067"
    $ current_voice = "voice/OKA07A_OKA0067.ogg"
    "伦太郎" "「所以……」"
    window hide
    play se "SGSE347"
    $ loadBG(0,"IBG018A",trans=moveinbottom, png=True)



    hide screen phonebtn
    "我扔出羊驼服。"
    "这是为了让自己认为真由理还活着，而拼命做出来的Ｃｏｓｐｌａｙ服装。"
    "穿越越多次时空就越好用的，正义之衣。"
    "然后用Ｓａｌｓａ・Ｆｉｒｅ　Ｇｕｎ罐点火。"
    window hide
    play se "SGSE317"

    play se "SGSE357L" loop

    "烧了起来。"
    "正义的印记，燃烧着。"
    window hide
    hide background-png 
    with ImageDissolve(im.Scale("mask/mask04.png",1024,576),2,reverse=True)

    show screen phonebtn
    "然后就在我要将羊驼面具——"
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0068"
    $ current_voice = "voice/OKA07A_OKA0068.ogg"
    "伦太郎" "「…………」"
    "投入火中之前。"
    window hide
    $ loadBG(0,"IBG017A",trans=moveinbottom, png=True)


    hide screen phonebtn
    "只是在最后，好想，再看一眼。"
    "静静地戴上面具。"
    hide screen phoneSD1
    window hide
    $ loadBG(0,"IBG019A",png=True,trans=dissolve)
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_ASA01"),"True","lh/MAY_ASA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    hide background-png 
    with dissolve





    show screen phoneSD1
    $ stopvoc("MAY")
    play MAY "OKA07A_MAY0006"
    $ current_voice = "voice/OKA07A_MAY0006.ogg"
    "真由理" "「晚上好，冈伦」"
    $ stopvoc("MAY")
    play MAY "OKA07A_MAY0007"
    $ current_voice = "voice/OKA07A_MAY0007.ogg"
    "真由理" "「本体，暴露了」"
    "只有戴上羊驼面具时才能看见的，幻像。"
    "在我为正义奋斗时，总是被结为人质的同伴。"
    "我隐藏的愿望暴露。"
    "就是，她——"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_ASB01"),"True","lh/MAY_ASB01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "OKA07A_MAY0008"
    $ current_voice = "voice/OKA07A_MAY0008.ogg"
    "真由理" "「噗—！只对了一半，其他错了」"
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0069"
    $ current_voice = "voice/OKA07A_OKA0069.ogg"
    "伦太郎" "「错了？」"
    $ stopvoc("MAY")
    play MAY "OKA07A_MAY0009"
    $ current_voice = "voice/OKA07A_MAY0009.ogg"
    "真由理" "「真由喜就是真由喜。是冈伦的愿望，与真由喜的思恋，结成的结晶」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_ASA02"),"True","lh/MAY_ASA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "OKA07A_MAY0010"
    $ current_voice = "voice/OKA07A_MAY0010.ogg"
    "真由理" "「所以，真由喜的话有一半，是真由喜的心情哦」"
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0070"
    $ current_voice = "voice/OKA07A_OKA0070.ogg"
    "伦太郎" "「……这样啊」"
    "的确是这样的。"
    "真由理就是真由理。"
    "以我贫乏的想象力，创造出完整的她这点，连想都不敢想。"
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0071"
    $ current_voice = "voice/OKA07A_OKA0071.ogg"
    "伦太郎" "「我说，真由理」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_ASA01"),"True","lh/MAY_ASA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "OKA07A_MAY0011"
    $ current_voice = "voice/OKA07A_MAY0011.ogg"
    "真由理" "「什么事，冈伦？」"
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0072"
    $ current_voice = "voice/OKA07A_OKA0072.ogg"
    "伦太郎" "「我做的事情……是正确的吗？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_ASB03"),"True","lh/MAY_ASB03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "OKA07A_MAY0012"
    $ current_voice = "voice/OKA07A_MAY0012.ogg"
    "真由理" "「嗯」"
    $ stopvoc("MAY")
    play MAY "OKA07A_MAY0013"
    $ current_voice = "voice/OKA07A_MAY0013.ogg"
    "真由理" "「这个嘛—」"
    $ stopvoc("MAY")
    play MAY "OKA07A_MAY0014"
    $ current_voice = "voice/OKA07A_MAY0014.ogg"
    "真由理" "「是呢……」"
    "真由理有些困惑的用食指戳着脸颊。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_ASA03"),"True","lh/MAY_ASA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "OKA07A_MAY0015"
    $ current_voice = "voice/OKA07A_MAY0015.ogg"
    "真由理" "「真由喜，不太明白这些复杂的事情」"
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0073"
    $ current_voice = "voice/OKA07A_OKA0073.ogg"
    "伦太郎" "「呼」"
    "因为听到过于像真由理的回答，让我不由自主地呼了一口气。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_ASC03"),"True","lh/MAY_ASC03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "OKA07A_MAY0016"
    $ current_voice = "voice/OKA07A_MAY0016.ogg"
    "真由理" "「真是的，为什么要笑？」"
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0074"
    $ current_voice = "voice/OKA07A_OKA0074.ogg"
    "伦太郎" "「嗯嗯，抱歉抱歉」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_ASA01"),"True","lh/MAY_ASA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "OKA07A_MAY0017"
    $ current_voice = "voice/OKA07A_MAY0017.ogg"
    "真由理" "「但是呢，冈伦」"
    $ stopvoc("MAY")
    play MAY "OKA07A_MAY0018"
    $ current_voice = "voice/OKA07A_MAY0018.ogg"
    "真由理" "「拼了命的，思考，烦恼，如果决定要做了，就完全不用在意其他人的眼光，就奋不顾身地去做——」"
    $ stopvoc("MAY")
    play MAY "OKA07A_MAY0019"
    $ current_voice = "voice/OKA07A_MAY0019.ogg"
    "真由理" "「真由喜，最喜欢这样的冈伦了」"
    $ stopvoc("MAY")
    play MAY "OKA07A_MAY0020"
    $ current_voice = "voice/OKA07A_MAY0020.ogg"
    "真由理" "「所以，真由喜」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_ASA02"),"True","lh/MAY_ASA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "OKA07A_MAY0021"
    $ current_voice = "voice/OKA07A_MAY0021.ogg"
    "真由理" "「希望冈伦能笑着走完，冈伦选择的路」"
    "真由理微笑着，对着我微笑——"
    hide screen phoneSD1
    window hide
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_OKA005A"]]["Check"]=True
    hide lh5 
    show expression "bg/EV_OKA005A~ipad.jpg" as background :
        yalign 1.0
    with dissolve












    hide screen phonebtn
    "将手伸向星空。"
    "与星屑握手( Ｓｔａｒｄｕｓｔ・Ｓｈａｋｅｈａｎｄ )"
    show expression "bg/EV_OKA005A~ipad.jpg" as background :
        yalign 1.0
        linear 10yalign 0.0



    "我也，像被什么吸引着看向天空。"
    "然后……不知为何。"
    "不知为何，眼泪，渐渐流了出来。"
    "我拼命地将自己的手向前伸。"
    "想用手抓住宇宙彼岸传来的光芒。"
    "但是那只是残光。"
    "穿越宇宙，穿越日月而来。"
    "现在那颗星已经不存在了。"
    "这前头的，星星，已经——"
    "星星——"
    window hide


    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_OKA005B"]]["Check"]=True







    $ loadBG(0,"EV_OKA005B")
    $ stopvoc("MAY")
    play MAY "OKA07A_MAY0022"
    $ current_voice = "voice/OKA07A_MAY0022.ogg"
    "真由理" "「嘟噜噜……♪」"
    window hide
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_OKA005C"]]["Check"]=True
    $ loadBG(0,"EV_OKA005C")



    "就在我脱下羊驼面具的同时。"
    "真由理的身影与闪耀的星星一同消失了。"
    window hide


    $ loadBG(2,"BG11N4")



    show screen phonebtn
    show screen phoneSD1
    "她，原本，就不存在于此。"
    "这是呼唤遥远的记忆的，残光——"
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0075"
    $ current_voice = "voice/OKA07A_OKA0075.ogg"
    "伦太郎" "「呵——呵——」"
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0076"
    $ current_voice = "voice/OKA07A_OKA0076.ogg"
    "伦太郎" "「呵呵——呵呵呵——！」"
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0077"
    $ current_voice = "voice/OKA07A_OKA0077.ogg"
    "伦太郎" "「哈—————哈哈哈哈！」"
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0078"
    $ current_voice = "voice/OKA07A_OKA0078.ogg"
    "伦太郎" "「哈哈哈！哈哈哈哈哈——！！」"
    window hide
    $ loadBG(0,"IBG017A",png=True)


    "我将羊驼面具扔入火中。"
    window hide
    play se "SGSE317"
    hide background-png 
    with ImageDissolve(im.Scale("mask/mask04.png",1024,576),2,reverse=True)


    "火焰瞬间扩大，羊驼的脸消失得无影无踪。"
    "永别了，羊驼人。"
    "涌上我心头的，是无以取代的解放感。"
    "没错，我——"
    "为什么在这种地方，现在不是该止步不前的时候。"
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0079"
    $ current_voice = "voice/OKA07A_OKA0079.ogg"
    "伦太郎" "「真由理——等着我！！」"
    window hide
    stop se



    $ loadBG(0,"BG40N",trans=fade)

    play se "SGSE182"


    hide screen phonebtn
    show screen phoneSD1
    "我，奔跑着。"
    "在夜间的秋叶原，奋力奔跑。"
    "脚步轻盈。"
    "已经没有了任何迷茫。"
    "我现在该做的——"
    "从现在起我该选择的命运，那就是——"
    window hide



    $ loadBG(0,"BG_BLACK")

    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0080"
    $ current_voice = "voice/OKA07A_OKA0080.ogg"
    "伦太郎" "「呼！！」"
    window hide


    $ loadBG(0,"BG02N2")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_HSC04"),"True","lh/CRS_HSC04a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    play se "SGSE316"


    show screen phonebtn
    $ stopvoc("CRS")
    play CRS "OKA07A_CRS0055"
    $ current_voice = "voice/OKA07A_CRS0055.ogg"
    "红莉栖" "「冈部？为什么突然——」"
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0081"
    $ current_voice = "voice/OKA07A_OKA0081.ogg"
    "伦太郎" "「动起来！」"
    $ stopvoc("CRS")
    play CRS "OKA07A_CRS0056"
    $ current_voice = "voice/OKA07A_CRS0056.ogg"
    "红莉栖" "「诶？动起来什么——」"
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0082"
    $ current_voice = "voice/OKA07A_OKA0082.ogg"
    "伦太郎" "「什么都别问快点准备，助手！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_HSB05"),"True","lh/CRS_HSB05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "OKA07A_CRS0057"
    $ current_voice = "voice/OKA07A_CRS0057.ogg"
    "红莉栖" "「啊——！都说了，我不是你的助手！」"
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0083"
    $ current_voice = "voice/OKA07A_OKA0083.ogg"
    "伦太郎" "「唔……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_HSB09"),"True","lh/CRS_HSB09a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "OKA07A_CRS0058"
    $ current_voice = "voice/OKA07A_CRS0058.ogg"
    "红莉栖" "「嗯……」"
    "过于怀念的动作，让身体僵硬了。"
    "是该说不舒服呢，还是说痒痒的呢……"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_HSB04"),"True","lh/CRS_HSB04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "OKA07A_CRS0059"
    $ current_voice = "voice/OKA07A_CRS0059.ogg"
    "红莉栖" "「总、总之！我完全不知道你说的准备究竟是要准备什么」"
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0084"
    $ current_voice = "voice/OKA07A_OKA0084.ogg"
    "伦太郎" "「呼，闻名天下的天才少女，也没什么了不起的」"
    $ stopvoc("CRS")
    play CRS "OKA07A_CRS0060"
    $ current_voice = "voice/OKA07A_CRS0060.ogg"
    "红莉栖" "「啊？你究竟在干什么。久违的再遇，是想让我觉得你变得更奇怪——」"
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0085"
    $ current_voice = "voice/OKA07A_OKA0085.ogg"
    "伦太郎" "「别说了快点准备，助手！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_HSA07"),"True","lh/CRS_HSA07a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "OKA07A_CRS0061"
    $ current_voice = "voice/OKA07A_CRS0061.ogg"
    "红莉栖" "「我说，我在问你究竟打算做什么！」"
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0086"
    $ current_voice = "voice/OKA07A_OKA0086.ogg"
    "伦太郎" "「回到那一天」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_HSC06"),"True","lh/CRS_HSC06a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "OKA07A_CRS0062"
    $ current_voice = "voice/OKA07A_CRS0062.ogg"
    "红莉栖" "「那一天……？」"
    $ stopvoc("CRS")
    play CRS "OKA07A_CRS0063"
    $ current_voice = "voice/OKA07A_CRS0063.ogg"
    "红莉栖" "「难道——」"
    "我微笑着看着红莉栖惊讶得说不出话来。"
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0087"
    $ current_voice = "voice/OKA07A_OKA0087.ogg"
    "伦太郎" "「嗯嗯。距今１年前——」"
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0088"
    $ current_voice = "voice/OKA07A_OKA0088.ogg"
    "伦太郎" "「我要回到，真由理被杀的那一天！！」"
    window hide
    play se "SGSE110"



    $ loadBG(2,"BG03A5")



    play bgm "FD2BGM11"
    "星星已经消失了。"
    "但如果它的残光还在迷惑人心的话。"
    "那我回到过去就好。"
    "超越光速，去改变，让星星消逝的那一瞬间的命运即可——！"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_HSA04"),"True","lh/CRS_HSA04a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "OKA07A_CRS0064"
    $ current_voice = "voice/OKA07A_CRS0064.ogg"
    "红莉栖" "「住手吧」"
    "牧濑红莉栖干脆地回答。"
    $ stopvoc("CRS")
    play CRS "OKA07A_CRS0065"
    $ current_voice = "voice/OKA07A_CRS0065.ogg"
    "红莉栖" "「我以时间机器开发者的身份给你忠告」"
    $ stopvoc("CRS")
    play CRS "OKA07A_CRS0066"
    $ current_voice = "voice/OKA07A_CRS0066.ogg"
    "红莉栖" "「这个技术，有根本性的缺陷。时间机器使用ＶＲ技术将大脑的状态转换成电波提取，然后拷贝到别的大脑中」"
    $ stopvoc("CRS")
    play CRS "OKA07A_CRS0067"
    $ current_voice = "voice/OKA07A_CRS0067.ogg"
    "红莉栖" "「但是，就算是同一个人，物理上完全相同的脑也是不存在的」"
    $ stopvoc("CRS")
    play CRS "OKA07A_CRS0068"
    $ current_voice = "voice/OKA07A_CRS0068.ogg"
    "红莉栖" "「仅仅是身体在48小时中发生的差异，也可能会跟拷贝后的意识发生冲突。你在穿越时空后，肯定也感受到过异样感吧？」"
    "的确如此。"
    "穿越时空后涌向身体的那种奇妙感觉。"
    "那应该是４８小时的时间差所导致的，肉体与精神的差异。"
    $ stopvoc("CRS")
    play CRS "OKA07A_CRS0069"
    $ current_voice = "voice/OKA07A_CRS0069.ogg"
    "红莉栖" "「就算如此，时间很短也并没有产生什么恶劣影响。」"
    $ stopvoc("CRS")
    play CRS "OKA07A_CRS0070"
    $ current_voice = "voice/OKA07A_CRS0070.ogg"
    "红莉栖" "「但如果连续的穿越时空呢？精神与肉体的差异，会越来越大。你的大脑也被损害的越来越大」 "
    $ stopvoc("CRS")
    play CRS "OKA07A_CRS0071"
    $ current_voice = "voice/OKA07A_CRS0071.ogg"
    "红莉栖" "「如果要我说的话，进行超过１年的时空穿越，就是自杀」"
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0089"
    $ current_voice = "voice/OKA07A_OKA0089.ogg"
    "伦太郎" "「原来如此……啊」"
    "所以红莉栖才阻止我回到过去啊……"
    $ stopvoc("CRS")
    play CRS "OKA07A_CRS0072"
    $ current_voice = "voice/OKA07A_CRS0072.ogg"
    "红莉栖" "「已经伤的很厉害了吧？」"
    $ stopvoc("CRS")
    play CRS "OKA07A_CRS0073"
    $ current_voice = "voice/OKA07A_CRS0073.ogg"
    "红莉栖" "「你不是正义的同伴吗。没有必要再痛苦下去了。全凭自己一个人的力量去拯救——会被当成正义的疯子的」"
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0090"
    $ current_voice = "voice/OKA07A_OKA0090.ogg"
    "伦太郎" "「啊，没错。你挺清楚的啊！」"
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0091"
    $ current_voice = "voice/OKA07A_OKA0091.ogg"
    "伦太郎" "「我不是正义的同伴，甚至连正义是什么都不知道！」"
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0092"
    $ current_voice = "voice/OKA07A_OKA0092.ogg"
    "伦太郎" "「我是——我是——！」 "
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0093"
    $ current_voice = "voice/OKA07A_OKA0093.ogg"
    "伦太郎" "「发狂的疯狂科学家，凤凰院凶真！！哇哈哈哈哈哈！！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_HSC05"),"True","lh/CRS_HSC05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "OKA07A_CRS0074"
    $ current_voice = "voice/OKA07A_CRS0074.ogg"
    "红莉栖" "「发狂的……疯狂，科学家？」"
    "红莉栖似乎在想着什么似的小声说到——"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_HSC03"),"True","lh/CRS_HSC03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "OKA07A_CRS0075"
    $ current_voice = "voice/OKA07A_CRS0075.ogg"
    "红莉栖" "「呵呵！」"
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0094"
    $ current_voice = "voice/OKA07A_OKA0094.ogg"
    "伦太郎" "「呼，想笑就笑吧！我和你不一样，是不会按常理出牌的！」"
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0095"
    $ current_voice = "voice/OKA07A_OKA0095.ogg"
    "伦太郎" "「正因为你认为不正常，所以才是我该走的路！我凤凰院凶真要走的路，谁都别想打扰！哇哈哈哈哈哈！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_HSA01"),"True","lh/CRS_HSA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "OKA07A_CRS0076"
    $ current_voice = "voice/OKA07A_CRS0076.ogg"
    "红莉栖" "「……什么啊，厨二病啊。没心情陪你玩这些」"
    "红莉栖一副惊讶的语气，但是，总觉得有些温柔。"
    $ stopvoc("CRS")
    play CRS "OKA07A_CRS0077"
    $ current_voice = "voice/OKA07A_CRS0077.ogg"
    "红莉栖" "「像你这种自作多情的家伙，需要回到过去改变你自己的人生！」"
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0096"
    $ current_voice = "voice/OKA07A_OKA0096.ogg"
    "伦太郎" "「可惜，我生下来就是这样的人！」"
    $ stopvoc("CRS")
    play CRS "OKA07A_CRS0078"
    $ current_voice = "voice/OKA07A_CRS0078.ogg"
    "红莉栖" "「出生前就这样了吧，肯定」"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_FD"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_FD"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_FD"])
    "虽然有些惊讶，但是她将{color=#f00} Ｆｌｏｐｐｙ　Ｄｉｃｋ {/color}插进了Ｘ６８０００。"
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0097"
    $ current_voice = "voice/OKA07A_OKA0097.ogg"
    "伦太郎" "「这是……？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_HSB01"),"True","lh/CRS_HSB01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "OKA07A_CRS0079"
    $ current_voice = "voice/OKA07A_CRS0079.ogg"
    "红莉栖" "「我还在想也可能会有这种事，所以程序的版本都帮你升级了」"
    $ stopvoc("CRS")
    play CRS "OKA07A_CRS0080"
    $ current_voice = "voice/OKA07A_CRS0080.ogg"
    "红莉栖" "「这样对大脑的损伤，多少会减轻一些」"
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0098"
    $ current_voice = "voice/OKA07A_OKA0098.ogg"
    "伦太郎" "「是知道我会选择回到过去吗……？」"
    $ stopvoc("CRS")
    play CRS "OKA07A_CRS0081"
    $ current_voice = "voice/OKA07A_CRS0081.ogg"
    "红莉栖" "「从理论上说，回到过去连一丝丝的益处都不会有。但是——」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_HSB02"),"True","lh/CRS_HSB02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "OKA07A_CRS0082"
    $ current_voice = "voice/OKA07A_CRS0082.ogg"
    "红莉栖" "「你是超越理论的，发狂的疯狂科学家——凤凰院凶真吧？」"
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0099"
    $ current_voice = "voice/OKA07A_OKA0099.ogg"
    "伦太郎" "「呼哈哈哈！能注意到这一点，真不愧是我的助手！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_HSA07"),"True","lh/CRS_HSA07a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "OKA07A_CRS0083"
    $ current_voice = "voice/OKA07A_CRS0083.ogg"
    "红莉栖" "「都说了，我不是你的助手！」 "
    "跟刚刚一样的对话，就像是与对方确认两人之间的信赖的对话。"
    "唔……真奇怪？这种无法言喻的安心感……！"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_HSA08"),"True","lh/CRS_HSA08a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "OKA07A_CRS0084"
    $ current_voice = "voice/OKA07A_CRS0084.ogg"
    "红莉栖" "「好歹还是听我说一句」"
    $ stopvoc("CRS")
    play CRS "OKA07A_CRS0085"
    $ current_voice = "voice/OKA07A_CRS0085.ogg"
    "红莉栖" "「虽然多少会减轻一些问题，但是没有从根本上解决」"
    $ stopvoc("CRS")
    play CRS "OKA07A_CRS0086"
    $ current_voice = "voice/OKA07A_CRS0086.ogg"
    "红莉栖" "「我没办法避免你在穿越时空时，记忆散失等，一些副作用的产生」 "

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_HSA01"),"True","lh/CRS_HSA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "OKA07A_CRS0087"
    $ current_voice = "voice/OKA07A_CRS0087.ogg"
    "红莉栖" "「即便如此——你也要穿越吧」"
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0100"
    $ current_voice = "voice/OKA07A_OKA0100.ogg"
    "伦太郎" "「嗯。不能让真由理成为命运的人质」"
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0101"
    $ current_voice = "voice/OKA07A_OKA0101.ogg"
    "伦太郎" "「因为，她是我的人质」"
    $ stopvoc("CRS")
    play CRS "OKA07A_CRS0088"
    $ current_voice = "voice/OKA07A_CRS0088.ogg"
    "红莉栖" "「……嗯」"
    "红莉栖像是在考虑着什么似的点了点头。"
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0102"
    $ current_voice = "voice/OKA07A_OKA0102.ogg"
    "伦太郎" "「那我出发了！助手，做准备——」"
    $ stopvoc("CRS")
    play CRS "OKA07A_CRS0089"
    $ current_voice = "voice/OKA07A_CRS0089.ogg"
    "红莉栖" "「冈部，我就再说一句，可以吗？」"
    $ stopvoc("CRS")
    play CRS "OKA07A_CRS0090"
    $ current_voice = "voice/OKA07A_CRS0090.ogg"
    "红莉栖" "「我就只能这样了，现在不能再去冒险，只单这样就已经尽全力了」"
    $ stopvoc("CRS")
    play CRS "OKA07A_CRS0091"
    $ current_voice = "voice/OKA07A_CRS0091.ogg"
    "红莉栖" "「但是，那边的我，会更加顽固，但也肯定会帮你的，所以——」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_HSA06"),"True","lh/CRS_HSA06a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "OKA07A_CRS0092"
    $ current_voice = "voice/OKA07A_CRS0092.ogg"
    "红莉栖" "「要跟她好好相处哦」"
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0103"
    $ current_voice = "voice/OKA07A_OKA0103.ogg"
    "伦太郎" "「哼，别担心。你已经是一个了不起的Ｌａｂｍｅｍ了」"
    "我深呼吸了一口—— "
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0104"
    $ current_voice = "voice/OKA07A_OKA0104.ogg"
    "伦太郎" "「我是发狂的疯狂科学家——过去是、现在是、未来也，绝对还是继续当下去！」"
    "下意识地指着红莉栖，这样宣布。"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_NORNIR"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_NORNIR"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_NORNIR"])
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0105"
    $ current_voice = "voice/OKA07A_OKA0105.ogg"
    "伦太郎" "「现在执行{color=#f00}『命运的女神们』作战(Ｏｐｅｒａｔｉｏｎ　Ｎｉｒｎｏｒ){/color}」"
    hide screen phoneSD1
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    show houden 

    play se "SGSE035L" loop

    hide screen phonebtn
    "时间机器发出了蜂鸣声。"
    "接下来我会踏上一段长途时间旅行。"
    "将４８小时的穿越延长成１年。"
    "无论程序被改良了多少，我的大脑，最终能忍受这些吗——？"
    "不对，肯定，没事的。"
    "就算丧失记忆，我也要救真由理。"
    "就像是一个有妄想症的英雄继续去救她。"
    "拯救真由理这一行为，已经深深地印在了我的本能之中。"
    $ stopvoc("CRS")
    play CRS "OKA07A_CRS0093"
    $ current_voice = "voice/OKA07A_CRS0093.ogg"
    "红莉栖" "「冈部！」"
    $ stopvoc("CRS")
    play CRS "OKA07A_CRS0094"
    $ current_voice = "voice/OKA07A_CRS0094.ogg"
    "红莉栖" "「——拜托了，救救真由理！」"
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0106"
    $ current_voice = "voice/OKA07A_OKA0106.ogg"
    "伦太郎" "「嗯！！」"
    "听到红莉栖的声援。"
    "我踏上了前往命运之日的旅途。"
    window hide




    stop se
    stop se
    stop bgm 


    hide houden 
    $ loadBG(0,"BG_BLACK")

    play se "SGSE377L" loop

    hide screen phonebtn
    hide screen phoneSD1
    "一遍又一遍——一遍又一遍——"
    "去穿越时空——"
    "这次，大脑似乎像有被车轮压过的痛苦——"
    "渐渐地散失了时间感——"
    "连现在是什么季节都不知道了——"
    "我最初究竟是为了什么要进行这次时空穿越——"
    "为什么，为什么——？"
    "渐渐的能够断断续续地听见声音。"
    "从遥远的后方传来红莉栖的声援。"
    "远处传来真由理的叫声。"
    "只靠这两个。"
    "我从昨天与明天的狭缝中，从梦与现实的狭缝中，逃出——"
    window hide





    show timeleap_no 
    with dissolve
    "嗯？"
    "这里是哪里……？"
    window hide
    $ loadBG(0,"IBG021A",png=True)



    $ stopvoc("Y05")
    play voc "OKA07A_Y050000"
    $ current_voice = "voice/OKA07A_Y050000.ogg"
    "羊驼司令" "「现实与游戏的狭缝」"
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0107"
    $ current_voice = "voice/OKA07A_OKA0107.ogg"
    "伦太郎" "「羊驼司令……？」"
    "发出声音后，意识终于回来了。"
    "画面中是熟悉的身影。"
    "在没有真由理的世界中，让我勉勉强强撑住的，就是——他。"
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0108"
    $ current_voice = "voice/OKA07A_OKA0108.ogg"
    "伦太郎" "「给您添麻烦了」"
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0109"
    $ current_voice = "voice/OKA07A_OKA0109.ogg"
    "伦太郎" "「但是，我已经从羊驼人中毕业了」"
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0110"
    $ current_voice = "voice/OKA07A_OKA0110.ogg"
    "伦太郎" "「就此永别了」"
    $ stopvoc("Y05")
    play voc "OKA07A_Y050001"
    $ current_voice = "voice/OKA07A_Y050001.ogg"
    "羊驼司令" "「真的是这样吗？」"
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0111"
    $ current_voice = "voice/OKA07A_OKA0111.ogg"
    "伦太郎" "「恩……？」"
    "司令的唇奇妙地弯曲了一下。"
    $ stopvoc("Y05")
    play voc "OKA07A_Y050002"
    $ current_voice = "voice/OKA07A_Y050002.ogg"
    "羊驼司令" "「我通过监视器看着你的一举一动。只有我能够完全理解你」"
    $ stopvoc("Y05")
    play voc "OKA07A_Y050003"
    $ current_voice = "voice/OKA07A_Y050003.ogg"
    "羊驼司令" "「就像是杰基尔博士与海德先生一样，你没办法离开我」"
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0112"
    $ current_voice = "voice/OKA07A_OKA0112.ogg"
    "伦太郎" "「………………呵」"
    "说这些恶心话。"
    "话说，别看我。"
    "渐渐有些不舒服了。"
    "虽然他原本就一副让人不舒服的脸。"
    $ stopvoc("Y05")
    play voc "OKA07A_Y050004"
    $ current_voice = "voice/OKA07A_Y050004.ogg"
    "羊驼司令" "「你知道，为什么羊驼人是正义的同伴？」"
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0113"
    $ current_voice = "voice/OKA07A_OKA0113.ogg"
    "伦太郎" "「……不知道」"
    $ stopvoc("Y05")
    play voc "OKA07A_Y050005"
    $ current_voice = "voice/OKA07A_Y050005.ogg"
    "羊驼司令" "「是因为，我们想做正确的事情」"
    "司令的话，还是跟以前一样让人摸不著头脑。"
    "无论使用怎样的算法。"
    "无论是这些还是那些，全都是我脑中产生的幻影……？"
    $ stopvoc("Y05")
    play voc "OKA07A_Y050006"
    $ current_voice = "voice/OKA07A_Y050006.ogg"
    "羊驼司令" "「在现实中，正义的行为不一定会有回报。但是，潜入监视器中事情就会发生改变」"
    $ stopvoc("Y05")
    play voc "OKA07A_Y050007"
    $ current_voice = "voice/OKA07A_Y050007.ogg"
    "羊驼司令" "「无论处于多么绝望的情况下，正义在心中，隐隐地，隐隐地，只要隐隐地感到就行」"
    $ stopvoc("Y05")
    play voc "OKA07A_Y050008"
    $ current_voice = "voice/OKA07A_Y050008.ogg"
    "羊驼司令" "「永不妥协，不顾常理，只求得到完美结局」"
    $ stopvoc("Y05")
    play voc "OKA07A_Y050009"
    $ current_voice = "voice/OKA07A_Y050009.ogg"
    "羊驼司令" "「只要不失去能够拯救所有人的希望就行」"
    $ stopvoc("Y05")
    play voc "OKA07A_Y050010"
    $ current_voice = "voice/OKA07A_Y050010.ogg"
    "羊驼司令" "「就像孩子一般，继续将手伸向星空就行」"
    $ stopvoc("Y05")
    play voc "OKA07A_Y050011"
    $ current_voice = "voice/OKA07A_Y050011.ogg"
    "羊驼司令" "「这样，肯定——」"
    $ stopvoc("Y05")
    play voc "OKA07A_Y050012"
    $ current_voice = "voice/OKA07A_Y050012.ogg"
    "羊驼司令" "「会迎来Ｔｒｕｅ　Ｅｎｄ」"
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0114"
    $ current_voice = "voice/OKA07A_OKA0114.ogg"
    "伦太郎" "「可笑」"
    "司令的话让我不由自主地笑了出来。"
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0115"
    $ current_voice = "voice/OKA07A_OKA0115.ogg"
    "伦太郎" "「你说的好像我是游戏中的登场人物一样」"
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0116"
    $ current_voice = "voice/OKA07A_OKA0116.ogg"
    "伦太郎" "「游戏的登场人物是你吧」"
    $ stopvoc("Y05")
    play voc "OKA07A_Y050013"
    $ current_voice = "voice/OKA07A_Y050013.ogg"
    "羊驼司令" "「谁知道呢」"
    "羊驼司令让人很生气。"
    "举手投足之间，都让人觉得碍眼。"
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0117"
    $ current_voice = "voice/OKA07A_OKA0117.ogg"
    "伦太郎" "「算了，怎样都行」"
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0118"
    $ current_voice = "voice/OKA07A_OKA0118.ogg"
    "伦太郎" "「总之，承蒙您照顾了」"
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0119"
    $ current_voice = "voice/OKA07A_OKA0119.ogg"
    "伦太郎" "「也许还会在什么地方再见」"
    $ stopvoc("Y05")
    play voc "OKA07A_Y050014"
    $ current_voice = "voice/OKA07A_Y050014.ogg"
    "羊驼司令" "「不要再迷失方向了」"
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0120"
    $ current_voice = "voice/OKA07A_OKA0120.ogg"
    "伦太郎" "「我知道」"
    $ stopvoc("Y05")
    play voc "OKA07A_Y050015"
    $ current_voice = "voice/OKA07A_Y050015.ogg"
    "羊驼司令" "「好了，快点走吧。我会为你的幸运祈祷」"
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0121"
    $ current_voice = "voice/OKA07A_OKA0121.ogg"
    "伦太郎" "「真是个说什么话都让人不爽的家伙……」"
    "苦涩地小声说到。"
    "为了回到之前的世界线。"
    "目标是正确的结局(ＴＯ　ＴＲＵＥ)"
    "我向他道了别。"
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0122"
    $ current_voice = "voice/OKA07A_OKA0122.ogg"
    "伦太郎" "「永别了羊驼人」"
    $ stopvoc("OKA")
    play OKA "OKA07A_OKA0123"
    $ current_voice = "voice/OKA07A_OKA0123.ogg"
    "伦太郎" "「ＥＬ　ＰＳＹ　ＣＯＮＧＲＯＯ」"

    hide screen phoneSD1
    window hide



    stop se
    hide timeleap_no 
    hide background-png 
    $ loadBG(0,"BG_BLACK")
    show screen invisible
    $ renpy.movie_cutscene("video/imv04.avi")
    hide screen invisible
    $ renpy.movie_cutscene("video/op.avi")
    "「扫描线上的化身博士·完成」"







    return
