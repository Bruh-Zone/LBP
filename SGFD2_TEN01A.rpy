label SGFD2_TEN01A:
    $ date="8/10"
    $ day = "TUE"
    show expression Solid("000") as background 
    with fade
    $ loadBG(0,"TIT009")
    $ renpy.pause(delay=3,hard=True)
    show expression Solid("000") as background 
    with fade








    $ loadBG(0,"BG37A")

    show screen phonebtn
    show screen phoneSD1

    "今天也去佛坛上香了。"
    $ stopvoc("TEN")
    play TEN "TEN01A_TEN0000"
    $ current_voice = "voice/TEN01A_TEN0000.ogg"
    "天王寺" "「你那边怎么样？过得还好吗？」"
    $ stopvoc("TEN")
    play TEN "TEN01A_TEN0001"
    $ current_voice = "voice/TEN01A_TEN0001.ogg"
    "天王寺" "「这边……怎么说呢」"
    play bgm "FD2BGM05"
    "要计算你已经不在了的年数，简单得很。"
    "只要想想绹的年龄就知道了。"
    "你啊……生下绹以后，就一个人先离我而去了。"
    "绹今年十一岁。"
    "读小学六年级了。"
    "很快，明年就是中学生了。"
    "身体很好，不用担心健康问题。"
    $ stopvoc("TEN")
    play TEN "TEN01A_TEN0002"
    $ current_voice = "voice/TEN01A_TEN0002.ogg"
    "天王寺" "「但是呢……有时候会想啊。」"
    "我到底有没有给绹创建一个“美满家庭”呢？"
    "而且我本来对于这个概念也不是很清楚。"
    "如果你活着的话，肯定是没问题的吧，但偏偏就那么走了。"
    window hide

    hide screen phonebtn
    "啊啊，当然工作还是在继续着的。"
    "大桧山大楼的店还是和以前一样。"
    "不工作的话就养活不了绹了呢。"
    window hide




    "也有从上层的租客那里收到的房租，所以生活是没有问题了……"
    window hide

    show screen phonebtn
    $ stopvoc("TEN")
    play TEN "TEN01A_TEN0003"
    $ current_voice = "voice/TEN01A_TEN0003.ogg"
    "天王寺" "「但是，总感觉少了些什么啊」"
    "这个家……"
    window hide

    hide screen phonebtn
    "还有大桧山的家。"
    "对于绹来说，是能够安心下来的两个地方。"
    "我能挺起胸膛来说这样就是理想的家庭吗？"
    window hide

    show screen phonebtn
    "你的早逝造成的空洞还没有填上。"
    "但是，如果用什么办法可以弥补的话……"
    window hide


    $ loadBG(2,"IBGX048")



    hide screen phonebtn
    $ stopvoc("TEN")
    play TEN "TEN01A_TEN0004"
    $ current_voice = "voice/TEN01A_TEN0004.ogg"
    "天王寺" "「如果可能的话，真希望这里能成为对于绹来说，最好的家庭啊……」"

    hide screen phoneSD1
    window hide
    window hide
    hide screen phonebtn
    scene expression Solid("000000")  with fade

    stop bgm 






    return
