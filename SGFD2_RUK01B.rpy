label SGFD2_RUK01B:
    hide screen phonebtn
    scene expression Solid("000000")  with fade

    window hide


    $ loadBG(0,"BG13E1")








    $ date="8/18"
    $ day = "WED"
    hide screen phonebtn
    hide screen phoneSD1

    $ stopvoc("RUK")
    play RUK "RUK01B_RUK0000"
    $ current_voice = "voice/RUK01B_RUK0000.ogg"
    "琉华" "「啊啊啊啊啊啊啊！」"
    "这里是哪——？"
    "我是谁——？"
    "记忆，意识，视线都一片混乱。"
    "整个脑子仿佛要炸开了。"
    $ stopvoc("RUK")
    play RUK "RUK01B_RUK0001"
    $ current_voice = "voice/RUK01B_RUK0001.ogg"
    "琉华" "「呜、啊啊啊啊啊──」"
    "感觉像用锥子从眼睛向大脑的中心刺进去的痛感。"
    $ stopvoc("RUK")
    play RUK "RUK01B_RUK0002"
    $ current_voice = "voice/RUK01B_RUK0002.ogg"
    "琉华" "「……啊啊、呜、啊啊啊啊啊！」"
    "感觉像是有人在不断地翻搅着我的大脑。"
    "又痒又痛"
    "但是，不知为何感到很舒服、那样地——"
    $ stopvoc("RUK")
    play RUK "RUK01B_RUK0003"
    $ current_voice = "voice/RUK01B_RUK0003.ogg"
    "琉华" "「啊……啊啊……」"
    "我究竟怎么了？"
    $ stopvoc("RUK")
    play RUK "RUK01B_RUK0004"
    $ current_voice = "voice/RUK01B_RUK0004.ogg"
    "琉华" "「哈……啊……啊啊……」"
    "到底发生了什么？"
    window hide











    $ stopvoc("RUK")
    play RUK "RUK01B_RUK0005"
    $ current_voice = "voice/RUK01B_RUK0005.ogg"
    "琉华" "「啊啊……」"
    play se "SGSE007L" loop

    "突然，声音涌入了耳朵。"
    "散乱的声波回荡在大脑里。"
    $ stopvoc("RUK")
    play RUK "RUK01B_RUK0006"
    $ current_voice = "voice/RUK01B_RUK0006.ogg"
    "琉华" "「哈啊……哈……啊……」"
    "就像在那之前连呼吸都忘记了一样，我大口地喘着气。"
    "不知做了多少次深呼吸后。"
    $ stopvoc("RUK")
    play RUK "RUK01B_RUK0007"
    $ current_voice = "voice/RUK01B_RUK0007.ogg"
    "琉华" "「…………」"
    "——我终于缓缓取回了存在的实感。"
    "这里是秋叶原站的广场。"
    "一如既往的人山人海。"
    "像是为了确认自己的脸的样子，我用手抚摸着自己的脸颊。"
    "还好……"
    "我还是我。"
    "我还是漆原琉华。"
    "冈部师傅说过，记忆的破坏和混合确实会有一定危险性，但随着深呼吸头疼确实稍稍有些减弱了。"
    $ stopvoc("RUK")
    play RUK "RUK01B_RUK0008"
    $ current_voice = "voice/RUK01B_RUK0008.ogg"
    "琉华" "「啊……」"
    "终于有了观察环境的余裕的我，才发现有些人好像正注意着我。"
    "在这种地方表现出痛苦的样子的话，确实会被人注目吧。"
    $ stopvoc("RUK")
    play RUK "RUK01B_RUK0009"
    $ current_voice = "voice/RUK01B_RUK0009.ogg"
    "琉华" "「啊、恩……那个……」"
    window hide

    stop se


    $ loadBG(0,"BG_BLACK")

    hide screen phonebtn
    "虽说我觉得该说些什么，但最后什么也没能说出来，只得像逃跑一样奔出了车站。"

    hide screen phoneSD1
    window hide





    hide screen phonebtn
    scene expression Solid("000000")  with fade
    return
