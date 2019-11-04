label SGFD2_NAE01A:
    show expression Solid("000") as background 
    with fade
    $ loadBG(0,"TIT011")
    $ renpy.pause(delay=3,hard=True)
    show expression Solid("000") as background 
    with fade



    $ date="7/5"
    $ day = "FRI"







    $ loadBG(0,"BG_BLACK")

    play bgm "FD2BGM04"

    hide screen phonebtn
    hide screen phoneSD1

    window hide

    $ stopvoc("NAE")
    play NAE "NAE01A_NAE0000"
    $ current_voice = "voice/NAE01A_NAE0000.ogg"
    "绹" "两年前的那个夏天──"
    $ stopvoc("NAE")
    play NAE "NAE01A_NAE0001"
    $ current_voice = "voice/NAE01A_NAE0001.ogg"
    "绹" "我、没有能够成为当事者。"
    window hide



    $ loadBG(0,"IBGX033")

    "无论那时也好、现在也好，我都还只是个小孩罢了。"
    "外界我所认识的人们遭遇的事情，也不曾丝毫察觉。"
    "我仅仅只是独自一人、在自己的圈子里平凡度日。"
    "注意到的时候，已经谁也不在了。"
    "父亲、已经不在了。留下我一个人、死去了。"
    "经常在父亲的大楼２层里出入的大学生叔叔们和高中生姐姐们，从那个夏天起，也一次没有再见到了。"
    "突然之间，我身边的人们全部一起消失了。"
    "发生了什么——我仅仅知道这些。"
    "终究发生了什么，我却没能知晓。"
    window hide


    $ loadBG(2,"BG79E5",at=[Transform(yalign=1.0)])







    show screen phonebtn
    show screen phoneSD1
    $ stopvoc("NAE")
    play NAE "NAE01A_NAE0002"
    $ current_voice = "voice/NAE01A_NAE0002.ogg"
    "绹" "「还是……走到了这里么」"
    "父亲这栋大楼的时间，从两年前开始就停止了。"
    "拉下来的卷帘门也一直紧闭着。"
    "想必店里已经沾满尘埃了吧。过去里面本来就很昏暗，满是灰尘罢了，如今的话应该已布满蜘蛛网了吧。"
    "想象着蜘蛛的模样，浑身起了鸡皮疙瘩。"
    "比起蟑螂，我还是比较难以应付蜘蛛。毛虫就更吓人了。"




    show screen phonebtn
    $ stopvoc("NAE")
    play NAE "NAE01A_NAE0003"
    $ current_voice = "voice/NAE01A_NAE0003.ogg"
    "绹" "「…………」"
    "到这里来，并不是想做些什么。"
    "并不打算进去，也并不是等待着谁。"
    "不过，我却会隔月一次地、放学回家不自觉走到这里。"
    window hide
    $ loadBG(0,"BG79E5")













    "我向四周张望。"
    "尽管秋叶原中央通路两旁的店家一直频繁地进出更替。"
    "到了这里我却觉得，无论是两年前还是现在，这一带的样子都不曾改变。"
    "只有些许的行人来往。"
    "大多数都是混杂着住房和各种店家的大楼。"
    hide screen phoneSD1
    window hide
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_NAE001A"]]["Check"]=True


    $ loadBG(2,"EV_NAE001A")



    hide screen phonebtn
    "……有什么在那。"
    "意识到时，视线在那儿停下了。"
    "斜对面大楼的屋顶。"
    "在那里，有一名全身穿着黑色的男人，很悠闲地抽着烟。"
    "“黑衣人”，是我擅自决定的称呼。"
    "父亲死了。"
    "那些叫做Ｌａｂｍｅｍ的人们也看不到了。"
    "从那一段时间之后，“黑衣人”像是从这座大楼周围冒出来的一样。"
    "——也并不是一直是同一个人。"
    "大概，每次都是不同的人。"
    "所以，最开始没有在意。"
    "不过，每当我偶然来到这儿，一定——是的，一定能在视野的某处看到“全身穿着黑色的人”的身影，不意间就注意到了。"
    "父亲的大楼，也许被监视着也说不定。"
    "明明现在是谁也不会出入的大楼。"
    "那些“黑衣人”们。"
    "是在等着谁呢——"
    "那些人们，会知道吗。"
    "父亲骤然结束自己生命的理由。"
    "“Ｌａｂｍｅｍ”的人们，消失的理由"
    "要不要试着搭话呢、我时常这么想。"
    "可是，也只是停留在想法罢了。心跳个不停，害怕起来。"
    "果然今天也还是，像逃跑一样地离开了。"
    window hide


    $ loadBG(2,"IBGX033")



    hide screen phonebtn
    show screen phoneSD1
    "这么说来，想起了两年前的那个夏天在父亲店里打工的姐姐，说过不可思议的话。"
    "——时间机器。"
    "能穿行于过去与未来的、梦之机器。"
    "那是绝对无法实现的、“米老师”——我就读的中学的数学老师的外号——这么说过。"
    "但如果真的有那样的机器的话，我。"
    "想回到那个夏天。"
    "…………。"
    "回到那个、夏天……？"
    "我想要成为、当事者吗？"
    "仅仅是为了不被抛下吗？"
    $ stopvoc("NAE")
    play NAE "NAE01A_NAE0004"
    $ current_voice = "voice/NAE01A_NAE0004.ogg"
    "绹" "「……我不懂啊」"

    hide screen phoneSD1
    window hide

    stop bgm 





    hide screen phonebtn
    scene expression Solid("000000")  with fade
    return
