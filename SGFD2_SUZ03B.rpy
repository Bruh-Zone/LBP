label SGFD2_SUZ03B:
    window hide


    $ loadBG(0,"BG_BLACK")


    $ date="8/13"
    hide screen phonebtn
    hide screen phoneSD1

    $ stopvoc("X06")
    play voc "SUZ03A_X060000"
    $ current_voice = "voice/SUZ03A_X060000.ogg"
    "妈妈" "「铃羽～！差不多该起床了！」"
    "听见了母亲的声音。"
    "一如既往未曾改变的声音。"
    "想要化身为企图将我从温暖的被窝里拉出来的人了！"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0267"
    $ current_voice = "voice/SUZ03A_SUZ0267.ogg"
    "铃羽" "「好－」"
    "我为了阻止她那么做便装作自己已经起来了。"
    "只是装作。"
    "没错，到昨天为止我还会这样通过装醒来再睡五分钟。"
    window hide

    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0268"
    $ current_voice = "voice/SUZ03A_SUZ0268.ogg"
    "不能太给父亲和母亲添麻烦了呐。"
    window hide

    "但是，今天却并不想继续躺下去。"
    "在母亲叫我起来之前就从被子里出来了。"
    "然后走向了客厅。"
    window hide


    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_SUZ005A"]]["Check"]=True
    $ loadBG(0,"EV_SUZ005A")

    play bgm "FD2BGM09"
    hide screen phonebtn
    $ stopvoc("X06")
    play voc "SUZ03A_X060001"
    $ current_voice = "voice/SUZ03A_X060001.ogg"
    "妈妈" "「咦，怎么了吗？没想到真的起来了」"
    "母亲都显得略感惊讶。"
    "虽说平时这么做确实很恶劣，但真的让她惊讶的话我还是很生气的。"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0269"
    $ current_voice = "voice/SUZ03A_SUZ0269.ogg"
    "铃羽" "「不能起来吗？」"
    $ stopvoc("X06")
    play voc "SUZ03A_X060002"
    $ current_voice = "voice/SUZ03A_X060002.ogg"
    "妈妈" "「没有。平时也能这样就好了」"
    "母亲依旧很高兴。"
    "对我起来这件事感到这么高兴吗。"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0270"
    $ current_voice = "voice/SUZ03A_SUZ0270.ogg"
    "铃羽" "「……是吗」"
    window hide
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_SUZ005B"]]["Check"]=True


    $ loadBG(2,"EV_SUZ005B")



    "然后我走到了一如既往地放着早餐的餐桌边上。"
    "这也跟平时一样。"
    "早餐的过程也是跟平时一样。"
    window hide
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_SUZ005C"]]["Check"]=True


    $ loadBG(2,"EV_SUZ005C")



    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0271"
    $ current_voice = "voice/SUZ03A_SUZ0271.ogg"
    "铃羽" "「呐，母亲」"
    "但是我说这种话，肯定是第一次。"
    $ stopvoc("SUZ")
    play SUZ "SUZ03A_SUZ0272"
    $ current_voice = "voice/SUZ03A_SUZ0272.ogg"
    "铃羽" "「吃完后让我来洗碗行吗？」"
    "这话让母亲非常的惊讶，但是这次她的惊讶让我有种自豪感。"
    "真是不可思议。"

    hide screen phoneSD1
    window hide


    stop bgm 
    scene expression Solid("000000")  with Fade(3,3,1)
    show screen invisible
    $ renpy.movie_cutscene("video/imv09.avi")
    hide screen invisible
    "「幽灵障害的会合·完成」"






    return
