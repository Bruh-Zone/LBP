label SGFD2_RUK03A:
    hide screen phonebtn
    scene expression Solid("000000")  with fade

    window hide


    $ loadBG(0,"IBGX048")
    play se "SGSE200L" loop



    $ date="8/15"
    $ day = "SUN"
    hide screen phonebtn
    hide screen phoneSD1

    "从不管经历几次都难以习惯的激烈的痛苦中解放出来的时候，我发现我正在被窝里。"
    "大概是睡得迷糊的时候起床接了电话，只有上半身钻出了被窝的状态。"
    hide screen phonebtn
    show screen phoneSD1
    "确认了一下手机，果然是１５日的早上。时间是早上５点半。"
    "１５日的早上——"
    "确实这个时候，真由理酱——还活着。"
    $ stopvoc("RUK")
    play RUK "RUK03A_RUK0000"
    $ current_voice = "voice/RUK03A_RUK0000.ogg"
    "琉华" "「……」"
    "是因为刚才还在睡觉的关系吗，总感觉头还有些重，晕乎乎的。"
    "夏Ｃｏｍｉ的日子会在早上和桥田在研究所汇合后一起过去，真由理这么说过。"
    "虽然没有问具体是什么时候汇合，但是她说比平时去学校的时间还要早，所以要是运气不好的话已经碰头了也说不定。"
    "我赶紧慌张地洗漱了下，从房间里跑了出来。"
    window hide
    stop se



    $ loadBG(0,"BG15A")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='UPP')",DynamicDisplayable(mouthanime,"URP_ASA01"),"True","lh/URP_ASA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    show screen phonebtn
    show screen phoneSD1
    play bgm "BGM14"

    $ stopvoc("UPP")
    play UPP "RUK03A_UPP0000"
    $ current_voice = "voice/RUK03A_UPP0000.ogg"
    "漆原父" "「哦？」"
    "在神社里，父亲已经在扫地了。"
    $ stopvoc("RUK")
    play RUK "RUK03A_RUK0001"
    $ current_voice = "voice/RUK03A_RUK0001.ogg"
    "琉华" "「啊，爸爸，早上好」"
    $ stopvoc("UPP")
    play UPP "RUK03A_UPP0001"
    $ current_voice = "voice/RUK03A_UPP0001.ogg"
    "漆原父" "「早上好。怎么了吗？这么早是要去哪里啊？」"
    $ stopvoc("RUK")
    play RUK "RUK03A_RUK0002"
    $ current_voice = "voice/RUK03A_RUK0002.ogg"
    "琉华" "「啊，是的。那个……是叫做夏Ｃｏｍｉ的地方」"
    $ stopvoc("UPP")
    play UPP "RUK03A_UPP0002"
    $ current_voice = "voice/RUK03A_UPP0002.ogg"
    "漆原父" "「什么，夏Ｃｏｍｉ？」"
    $ stopvoc("RUK")
    play RUK "RUK03A_RUK0003"
    $ current_voice = "voice/RUK03A_RUK0003.ogg"
    "琉华" "「恩」"
    $ stopvoc("UPP")
    play UPP "RUK03A_UPP0003"
    $ current_voice = "voice/RUK03A_UPP0003.ogg"
    "漆原父" "「哼，夏Ｃｏｍｉ吗。要小心啊，那里可是战场呢。」"
    $ stopvoc("RUK")
    play RUK "RUK03A_RUK0004"
    $ current_voice = "voice/RUK03A_RUK0004.ogg"
    "琉华" "「诶？」"
    $ stopvoc("RUK")
    play RUK "RUK03A_RUK0005"
    $ current_voice = "voice/RUK03A_RUK0005.ogg"
    "琉华" "「爸爸……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='UPP')",DynamicDisplayable(mouthanime,"URP_ASA02"),"True","lh/URP_ASA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("UPP")
    play UPP "RUK03A_UPP0004"
    $ current_voice = "voice/RUK03A_UPP0004.ogg"
    "漆原父" "「恩？　怎么了吗？」"
    "难道说……"

    show expression ConditionSwitch("renpy.music.get_playing(channel='UPP')",DynamicDisplayable(mouthanime,"URP_ASA01"),"True","lh/URP_ASA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("UPP")
    play UPP "RUK03A_UPP0005"
    $ current_voice = "voice/RUK03A_UPP0005.ogg"
    "漆原父" "「比起那些，没关系吗？时间，难道不紧张吗？」"
    $ stopvoc("RUK")
    play RUK "RUK03A_RUK0006"
    $ current_voice = "voice/RUK03A_RUK0006.ogg"
    "琉华" "「啊，是这样哦！那么，我出发了！」"
    $ stopvoc("UPP")
    play UPP "RUK03A_UPP0006"
    $ current_voice = "voice/RUK03A_UPP0006.ogg"
    "漆原父" "「一路顺风。要做好防中暑的准备哦」"
    window hide


    $ loadBG(2,"IBGX048")



    hide screen phonebtn
    "……爸爸，好像对于夏Ｃｏｍｉ很了解的样子。"
    "难道说，有去过么？"
    window hide

    stop bgm 



    $ loadBG(0,"BG05A1")




    $ loadBG(2,"BG_BLACK")



    hide screen phonebtn
    "我登上这几个小时之间已经不知道登过几次的楼梯，站在了研究所的门前。"
    "我感到里面有人的样子。"
    $ stopvoc("RUK")
    play RUK "RUK03A_RUK0007"
    $ current_voice = "voice/RUK03A_RUK0007.ogg"
    "琉华" "「…………」"
    "我听见了声音。"
    "是女孩子的声音。"
    "温暖，温柔。"
    "像悦耳的铃音。"
    "女孩子的。"
    "声音。"
    "这声音是。"
    "这个。"
    "声音是。"
    window hide


    $ loadBG(0,"BG01A")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA02"),"True","lh/MAY_CSA02a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    play se "SGSE024"


    show screen phonebtn
    $ stopvoc("MAY")
    play MAY "RUK03A_MAY0000"
    $ current_voice = "voice/RUK03A_MAY0000.ogg"
    "真由理" "「咦？　是琉华酱啊！」"
    play bgm "FD2BGM09"
    "那的确是。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA02"),"True","lh/MAY_CSA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "RUK03A_MAY0001"
    $ current_voice = "voice/RUK03A_MAY0001.ogg"
    "真由理" "「琉华酱，嘟嘟噜！」"
    $ stopvoc("RUK")
    play RUK "RUK03A_RUK0008"
    $ current_voice = "voice/RUK03A_RUK0008.ogg"
    "琉华" "「真由理……酱……」"
    "果然"
    $ stopvoc("RUK")
    play RUK "RUK03A_RUK0009"
    $ current_voice = "voice/RUK03A_RUK0009.ogg"
    "琉华" "「是，真由理酱啊」"
    $ stopvoc("MAY")
    play MAY "RUK03A_MAY0002"
    $ current_voice = "voice/RUK03A_MAY0002.ogg"
    "真由理" "「是呢。真由喜呢。诶嘿嘿，今天是夏Ｃｏｍｉ，所以我起得很早啊」"
    "真由理酱。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA01"),"True","lh/MAY_CSA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "RUK03A_MAY0003"
    $ current_voice = "voice/RUK03A_MAY0003.ogg"
    "真由理" "「琉华酱你呢，为什么，会这么早起来？」"
    "真由理酱，真由理酱，真由理酱，真由理酱，真由理酱！"
    "是真实的真由理酱啊。"
    "好好地活动着，好好地说着话，好好地笑着。"
    "没有错。"
    "是活着的真由理酱！"
    $ stopvoc("RUK")
    play RUK "RUK03A_RUK0010"
    $ current_voice = "voice/RUK03A_RUK0010.ogg"
    "琉华" "「真由理酱！」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CLA04"),"True","lh/MAY_CLA04a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide screen phonebtn
    $ stopvoc("MAY")
    play MAY "RUK03A_MAY0004"
    $ current_voice = "voice/RUK03A_MAY0004.ogg"
    "真由理" "「哇哇！」"
    "我没有多想就抱住了真由理酱。"
    "就好像不那么做的话，她就会消失一样。"
    "但是。"
    $ stopvoc("MAY")
    play MAY "RUK03A_MAY0005"
    $ current_voice = "voice/RUK03A_MAY0005.ogg"
    "真由理" "「琉华酱！？」"
    $ stopvoc("RUK")
    play RUK "RUK03A_RUK0011"
    $ current_voice = "voice/RUK03A_RUK0011.ogg"
    "琉华" "「真由理……酱……」"
    "真由理酱确实无疑地在这里。"
    "温暖地。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CLA03"),"True","lh/MAY_CLA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "RUK03A_MAY0006"
    $ current_voice = "voice/RUK03A_MAY0006.ogg"
    "真由理" "「怎么了吗，琉华酱？　为什么在哭？」"
    $ stopvoc("RUK")
    play RUK "RUK03A_RUK0012"
    $ current_voice = "voice/RUK03A_RUK0012.ogg"
    "琉华" "「……」"
    $ stopvoc("MAY")
    play MAY "RUK03A_MAY0007"
    $ current_voice = "voice/RUK03A_MAY0007.ogg"
    "真由理" "「难道说又被冈伦说了很过分的话？」"
    $ stopvoc("RUK")
    play RUK "RUK03A_RUK0013"
    $ current_voice = "voice/RUK03A_RUK0013.ogg"
    "琉华" "「呜……呜呜……」"
    $ stopvoc("MAY")
    play MAY "RUK03A_MAY0008"
    $ current_voice = "voice/RUK03A_MAY0008.ogg"
    "真由理" "「那样的话没关系的哦？　真由理会狠狠地教训他的」"
    $ stopvoc("RUK")
    play RUK "RUK03A_RUK0014"
    $ current_voice = "voice/RUK03A_RUK0014.ogg"
    "琉华" "「不对……并不是……那样……」"
    $ stopvoc("MAY")
    play MAY "RUK03A_MAY0009"
    $ current_voice = "voice/RUK03A_MAY0009.ogg"
    "真由理" "「不是吗？那么会什么会哭呢？」"
    $ stopvoc("RUK")
    play RUK "RUK03A_RUK0015"
    $ current_voice = "voice/RUK03A_RUK0015.ogg"
    "琉华" "「那是因为……」"
    window hide
    stop bgm 
    play se "SGSE024"

    $ stopvoc("DAR")
    play DAR "RUK03A_DAR0000"
    $ current_voice = "voice/RUK03A_DAR0000.ogg"
    "至" "「哼，便利店的冷藏饮料居然已经快要卖完了。真是的，夏Ｃｏｍｉ时间就该多进点货嘛常考……」"
    $ stopvoc("DAR")
    play DAR "RUK03A_DAR0001"
    $ current_voice = "voice/RUK03A_DAR0001.ogg"
    "至" "「唔哦哦哦哦！　早上就来百合展开啊ｋｒｋｔ！！」"
    $ stopvoc("OKA")
    play OKA "RUK03A_OKA0000"
    $ current_voice = "voice/RUK03A_OKA0000.ogg"
    "伦太郎" "「好啦桶子，就别打扰她们了，给我赶快进去……」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA04"),"True","lh/OKA_ASA04a~ipad.png") at left as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASB04"),"True","lh/DAR_ASB04a~ipad.png") at right as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("RUK")
    play RUK "RUK03A_RUK0016"
    $ current_voice = "voice/RUK03A_RUK0016.ogg"
    "琉华" "「啊…………」"
    $ stopvoc("OKA")
    play OKA "RUK03A_OKA0001"
    $ current_voice = "voice/RUK03A_OKA0001.ogg"
    "伦太郎" "「琉华……子……」"
    $ stopvoc("RUK")
    play RUK "RUK03A_RUK0017"
    $ current_voice = "voice/RUK03A_RUK0017.ogg"
    "琉华" "「冈部师傅……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA01"),"True","lh/DAR_ASA01a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "RUK03A_DAR0002"
    $ current_voice = "voice/RUK03A_DAR0002.ogg"
    "至" "「啊，两位不要在意我们，快请继续吧」"
    $ stopvoc("OKA")
    play OKA "RUK03A_OKA0002"
    $ current_voice = "voice/RUK03A_OKA0002.ogg"
    "伦太郎" "「…………」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA06"),"True","lh/DAR_ASA06a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "RUK03A_DAR0003"
    $ current_voice = "voice/RUK03A_DAR0003.ogg"
    "至" "「咦，咦？　怎么了啊，大家？　难道说，我搞错了？」"
    hide screen phoneSD1
    window hide



    $ loadBG(0,"BG02A2")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA03"),"True","lh/MAY_CSA03a~ipad.png") at left as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA01"),"True","lh/OKA_ASA01a~ipad.png") at right as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    play bgm "BGM18"

    show screen phonebtn
    show screen phoneSD1
    $ stopvoc("MAY")
    play MAY "RUK03A_MAY0010"
    $ current_voice = "voice/RUK03A_MAY0010.ogg"
    "真由理" "「那也就是说，没有被冈伦说很过分的事情咯？」"
    $ stopvoc("OKA")
    play OKA "RUK03A_OKA0003"
    $ current_voice = "voice/RUK03A_OKA0003.ogg"
    "伦太郎" "「所以说不是说了不是那样的么」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSC03"),"True","lh/MAY_CSC03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "RUK03A_MAY0011"
    $ current_voice = "voice/RUK03A_MAY0011.ogg"
    "真由理" "「琉华酱，真的吗？」"
    $ stopvoc("RUK")
    play RUK "RUK03A_RUK0018"
    $ current_voice = "voice/RUK03A_RUK0018.ogg"
    "琉华" "「恩，恩……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA03"),"True","lh/MAY_CSA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "RUK03A_MAY0012"
    $ current_voice = "voice/RUK03A_MAY0012.ogg"
    "真由理" "「这样啊。那样的话就好……」"
    "好像冈部师傅和桥田君刚刚两个人为了夏Ｃｏｍｉ去买了东西的样子。"
    "回来的时候在Ｌａｂ里看到我吓了一跳的样子。"
    "但多亏了两位的出现，我内心激动万分的心情稍微有些平静下来了。"
    $ stopvoc("OKA")
    play OKA "RUK03A_OKA0004"
    $ current_voice = "voice/RUK03A_OKA0004.ogg"
    "伦太郎" "「…………」"
    "冈部师傅和平时相比没什么精神的样子。"
    "我觉得那也是没有办法的事。"
    "因为，冈部师傅肯定现在也很迷茫。"
    "自己的判断到底是不是正确的呢，这么烦躁着不断地重复这段时间。"
    hide screen phonebtn
    $ stopvoc("RUK")
    play RUK "RUK03A_RUK0019"
    $ current_voice = "voice/RUK03A_RUK0019.ogg"
    "琉华" "「那个，冈部师──」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA01"),"True","lh/MAY_CSA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    show screen phonebtn
    $ stopvoc("MAY")
    play MAY "RUK03A_MAY0013"
    $ current_voice = "voice/RUK03A_MAY0013.ogg"
    "真由理" "「呐呐，但是但是，这样的话为什么琉华酱会在这个时间来到这里呢？」"
    $ stopvoc("RUK")
    play RUK "RUK03A_RUK0020"
    $ current_voice = "voice/RUK03A_RUK0020.ogg"
    "琉华" "「诶？」"
    $ stopvoc("MAY")
    play MAY "RUK03A_MAY0014"
    $ current_voice = "voice/RUK03A_MAY0014.ogg"
    "真由理" "「不是因为和冈伦吵架了想来和我谈心才过来的吧？那样的话到底是为了什么才会这么早来到这里的呢？」"
    "是啊。"
    "我现在比起担心冈部师傅，还有更加重要的事情要做。"
    $ stopvoc("RUK")
    play RUK "RUK03A_RUK0021"
    $ current_voice = "voice/RUK03A_RUK0021.ogg"
    "琉华" "「那件事情呢，其实是……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA02"),"True","lh/MAY_CSA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "RUK03A_MAY0015"
    $ current_voice = "voice/RUK03A_MAY0015.ogg"
    "真由理" "「啊，我知道了。难道说，要和我们一起去夏Ｃｏｍｉ吗，是吗？」"
    $ stopvoc("RUK")
    play RUK "RUK03A_RUK0022"
    $ current_voice = "voice/RUK03A_RUK0022.ogg"
    "琉华" "「啊……」"
    $ stopvoc("MAY")
    play MAY "RUK03A_MAY0016"
    $ current_voice = "voice/RUK03A_MAY0016.ogg"
    "真由理" "「是这样的话。是这样的话，果然真由喜还是希望琉华酱能够去Ｃｏｓｐｌａｙ呢，什么的」"
    $ stopvoc("OKA")
    play OKA "RUK03A_OKA0005"
    $ current_voice = "voice/RUK03A_OKA0005.ogg"
    "伦太郎" "「真由理。我和你说过不要这么勉强她了吧」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSC02"),"True","lh/MAY_CSC02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "RUK03A_MAY0017"
    $ current_voice = "voice/RUK03A_MAY0017.ogg"
    "真由理" "「恩，虽然我觉得超级适合的呢。呐，琉华酱，不行吗？」"
    $ stopvoc("RUK")
    play RUK "RUK03A_RUK0023"
    $ current_voice = "voice/RUK03A_RUK0023.ogg"
    "琉华" "「那个，关于那个呢，果然我还是，要不试试看吧……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSB03"),"True","lh/MAY_CSB03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "RUK03A_MAY0018"
    $ current_voice = "voice/RUK03A_MAY0018.ogg"
    "真由理" "「是呢。抱歉呢，明明你都说过那么多次不喜欢了」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA04"),"True","lh/OKA_ASA04a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "RUK03A_OKA0006"
    $ current_voice = "voice/RUK03A_OKA0006.ogg"
    "伦太郎" "「嘛，本来这种事也是不能强求的」"
    $ stopvoc("RUK")
    play RUK "RUK03A_RUK0024"
    $ current_voice = "voice/RUK03A_RUK0024.ogg"
    "琉华" "「诶？那个，不是那样其实我，还是要不试试看吧……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSC03"),"True","lh/MAY_CSC03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "RUK03A_MAY0019"
    $ current_voice = "voice/RUK03A_MAY0019.ogg"
    "真由理" "「但是，真由理，还没有放弃哦。琉华酱说不定什么时候就回心转意了呢……」"
    $ stopvoc("OKA")
    play OKA "RUK03A_OKA0007"
    $ current_voice = "voice/RUK03A_OKA0007.ogg"
    "伦太郎" "「嗯？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSB03"),"True","lh/MAY_CSB03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "RUK03A_MAY0020"
    $ current_voice = "voice/RUK03A_MAY0020.ogg"
    "真由理" "「咦？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA01"),"True","lh/OKA_ASA01a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "RUK03A_OKA0008"
    $ current_voice = "voice/RUK03A_OKA0008.ogg"
    "伦太郎" "「喂，喂，琉华子，你刚才，说了什么……？」"
    $ stopvoc("RUK")
    play RUK "RUK03A_RUK0025"
    $ current_voice = "voice/RUK03A_RUK0025.ogg"
    "琉华" "「所以说，我在想，要不试试去Ｃｏｓｐｌａｙ吧……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSC02"),"True","lh/MAY_CSC02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "RUK03A_MAY0021"
    $ current_voice = "voice/RUK03A_MAY0021.ogg"
    "真由理" "「诶诶！？　真的是真的吗？」"
    $ stopvoc("RUK")
    play RUK "RUK03A_RUK0026"
    $ current_voice = "voice/RUK03A_RUK0026.ogg"
    "琉华" "「恩，恩……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA02"),"True","lh/MAY_CSA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "RUK03A_MAY0022"
    $ current_voice = "voice/RUK03A_MAY0022.ogg"
    "真由理" "「太好了！　琉华酱同意Ｃｏｓｐｌａｙ了！　琉华酱的Ｃｏｓｐｌａｙ～♪」"
    $ stopvoc("OKA")
    play OKA "RUK03A_OKA0009"
    $ current_voice = "voice/RUK03A_OKA0009.ogg"
    "伦太郎" "「这，这样好吗，琉华子？你不是一直说不是很擅长那种事的么……」"
    $ stopvoc("RUK")
    play RUK "RUK03A_RUK0027"
    $ current_voice = "voice/RUK03A_RUK0027.ogg"
    "琉华" "「没关系。我想试试看」"
    "为了真由理酱……"
    $ stopvoc("MAY")
    play MAY "RUK03A_MAY0023"
    $ current_voice = "voice/RUK03A_MAY0023.ogg"
    "真由理" "「太好了太好了」"
    "真由理酱……"
    $ stopvoc("OKA")
    play OKA "RUK03A_OKA0010"
    $ current_voice = "voice/RUK03A_OKA0010.ogg"
    "伦太郎" "「这，这样啊……」"
    $ stopvoc("DAR")
    play DAR "RUK03A_DAR0004"
    $ current_voice = "voice/RUK03A_DAR0004.ogg"
    "至" "「唔哦哦哦哦！琉华氏都要出Ｃｏｓｐｌａｙ了啊，我ｗ整ｗ个ｗ人ｗ都ｗ要ｗ上ｗ天ｗ了ｗｗｗ！」"
    $ stopvoc("OKA")
    play OKA "RUK03A_OKA0011"
    $ current_voice = "voice/RUK03A_OKA0011.ogg"
    "伦太郎" "「但是啊真由理。有给琉华子用的服装么？」"
    $ stopvoc("MAY")
    play MAY "RUK03A_MAY0024"
    $ current_voice = "voice/RUK03A_MAY0024.ogg"
    "真由理" "「哼哼哼，为了这种场合，真由喜早就做好准备了」"
    $ stopvoc("DAR")
    play DAR "RUK03A_DAR0005"
    $ current_voice = "voice/RUK03A_DAR0005.ogg"
    "至" "「不愧是真由氏。ＧＪ点赞！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA01"),"True","lh/MAY_CSA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "RUK03A_MAY0025"
    $ current_voice = "voice/RUK03A_MAY0025.ogg"
    "真由理" "「是因为想着琉华酱可能什么时候就想要Ｃｏｓｐｌａｙ了呢才准备的哦」"
    $ stopvoc("RUK")
    play RUK "RUK03A_RUK0028"
    $ current_voice = "voice/RUK03A_RUK0028.ogg"
    "琉华" "「真由理酱……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA02"),"True","lh/MAY_CSA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "RUK03A_MAY0026"
    $ current_voice = "voice/RUK03A_MAY0026.ogg"
    "真由理" "「诶嘿嘿。这样真由喜的一个梦想就实现了呢」"
    "这么说着，真由理酱看起来十分高兴的样子。"
    "如果是这么回事的话，要是我早点同意就好了。"
    "我的那些害羞的心情和真由理的这样的笑容比起来什么都不算啊。"
    $ stopvoc("RUK")
    play RUK "RUK03A_RUK0029"
    $ current_voice = "voice/RUK03A_RUK0029.ogg"
    "琉华" "「……」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    "我感觉自己就要哭了，拼了命地忍住了。"

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA04"),"True","lh/OKA_ASA04a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "RUK03A_OKA0012"
    $ current_voice = "voice/RUK03A_OKA0012.ogg"
    "伦太郎" "「琉华子……」"
    $ stopvoc("RUK")
    play RUK "RUK03A_RUK0030"
    $ current_voice = "voice/RUK03A_RUK0030.ogg"
    "琉华" "「是的？」"
    $ stopvoc("OKA")
    play OKA "RUK03A_OKA0013"
    $ current_voice = "voice/RUK03A_OKA0013.ogg"
    "伦太郎" "「昨天真是抱歉了」"
    "昨天——"
    "说了什么还记得我是男的什么的，是因为那件事吧。"
    $ stopvoc("RUK")
    play RUK "RUK03A_RUK0031"
    $ current_voice = "voice/RUK03A_RUK0031.ogg"
    "琉华" "「不会。其实是我……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA01"),"True","lh/OKA_ASA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "RUK03A_OKA0014"
    $ current_voice = "voice/RUK03A_OKA0014.ogg"
    "伦太郎" "「……真的……没关系吗？」"
    "稍微想了想，是在说现在的Ｃｏｓｐｌａｙ的事情吧。"
    $ stopvoc("RUK")
    play RUK "RUK03A_RUK0032"
    $ current_voice = "voice/RUK03A_RUK0032.ogg"
    "琉华" "「是的，是我自己想要去试试」"
    $ stopvoc("OKA")
    play OKA "RUK03A_OKA0015"
    $ current_voice = "voice/RUK03A_OKA0015.ogg"
    "伦太郎" "「是吗……。谢谢了」"
    $ stopvoc("RUK")
    play RUK "RUK03A_RUK0033"
    $ current_voice = "voice/RUK03A_RUK0033.ogg"
    "琉华" "「冈部师傅……」"
    "冈部师傅……他很明白。"
    "今天，真由理就会死去这件事。"
    "已经发生过无数次的事实。"
    "无法回避的事实。"
    "到底现在，冈部师傅是怎样的一种心情呢。"
    hide screen phoneSD1
    window hide

    stop bgm 



    $ loadBG(0,"BG38A")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_ASB02"),"True","lh/MAY_ASB02a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    $ targetmailid = gc["ScriptMacros"]["RM_RUK_RECV_UPP03_01"]

    $ LR_RM_CHANCE=1
    if phonemailring!= "":
        play se phonemailring
    if persistent.skipmail==False:
        $ renpy.choice_for_skipping()
    if targetmailid != "":
        $ RcvMail(targetmailid)
        $ targetmailid=""

    call CHECK_RM_RECEIVE

    play bgm "FDBGM02"

    show screen phonebtn
    show screen phoneSD1
    $ stopvoc("MAY")
    play MAY "RUK03A_MAY0027"
    $ current_voice = "voice/RUK03A_MAY0027.ogg"
    "真由理" "「唔哇，今年人也超多的啊ー」"
    "国际会场周围的人数超过了想象。"
    $ stopvoc("RUK")
    play RUK "RUK03A_RUK0034"
    $ current_voice = "voice/RUK03A_RUK0034.ogg"
    "琉华" "「好，好厉害的场面……」"
    "没想到有这么多人，我都有点畏缩了。"
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA01"),"True","lh/DAR_ASA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "RUK03A_DAR0006"
    $ current_voice = "voice/RUK03A_DAR0006.ogg"
    "至" "「嗯？　琉华氏，怎么了吗？」"
    $ stopvoc("RUK")
    play RUK "RUK03A_RUK0035"
    $ current_voice = "voice/RUK03A_RUK0035.ogg"
    "琉华" "「诶？啊……那个，这么说起来，我因为是第一次有点紧张啦……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASB07"),"True","lh/DAR_ASB07a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "RUK03A_DAR0007"
    $ current_voice = "voice/RUK03A_DAR0007.ogg"
    "至" "「硫，琉华氏，刚才的发言，再来一波！可以的话请用那种小鸟依人的眼神来说，哈，哈」"
    $ stopvoc("RUK")
    play RUK "RUK03A_RUK0036"
    $ current_voice = "voice/RUK03A_RUK0036.ogg"
    "琉华" "「诶，诶诶？」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASB03"),"True","lh/OKA_ASB03a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "RUK03A_OKA0016"
    $ current_voice = "voice/RUK03A_OKA0016.ogg"
    "伦太郎" "「省省吧变态！」"
    "这次的夏Ｃｏｍｉ，冈部师傅也一起来了。"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_ASA01"),"True","lh/MAY_ASA01a~ipad.png") at left as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA01"),"True","lh/DAR_ASA01a~ipad.png") at right as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "RUK03A_MAY0028"
    $ current_voice = "voice/RUK03A_MAY0028.ogg"
    "真由理" "「桶子君不一起去吗？Ｃｏｓｐｌａｙ广场」"
    $ stopvoc("DAR")
    play DAR "RUK03A_DAR0008"
    $ current_voice = "voice/RUK03A_DAR0008.ogg"
    "至" "「第一天一般都是攻击企业Ｂｏｏｔｈ吧常考」"
    $ stopvoc("DAR")
    play DAR "RUK03A_DAR0009"
    $ current_voice = "voice/RUK03A_DAR0009.ogg"
    "至" "「所以我觉得Ｃｏｓｐｌａｙ广场是要在午后再去的」"
    $ stopvoc("MAY")
    play MAY "RUK03A_MAY0029"
    $ current_voice = "voice/RUK03A_MAY0029.ogg"
    "真由理" "「冈伦呢？」"

    $ gd["RCVmailData"][gc["ScriptMacros"]["RM_RUK_RECV_UPP02_01"]]["late"]=True
    $ lml.append(gc["ScriptMacros"]["RM_RUK_RECV_UPP02_01"])

    window hide
    hide lh6  with dissolve

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA01"),"True","lh/OKA_ASA01a~ipad.png") at right as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "RUK03A_OKA0017"
    $ current_voice = "voice/RUK03A_OKA0017.ogg"
    "伦太郎" "「我没有什么特别的目的啦。就和你们一起行动了」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_ASA02"),"True","lh/MAY_ASA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "RUK03A_MAY0030"
    $ current_voice = "voice/RUK03A_MAY0030.ogg"
    "真由理" "「虽然嘴上这么说，实际上是想看琉华酱的Ｃｏｓｐｌａｙ吧？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA03"),"True","lh/OKA_ASA03a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "RUK03A_OKA0018"
    $ current_voice = "voice/RUK03A_OKA0018.ogg"
    "伦太郎" "「才，才不是这样呢」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_ASB01"),"True","lh/MAY_ASB01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "RUK03A_MAY0031"
    $ current_voice = "voice/RUK03A_MAY0031.ogg"
    "真由理" "「嘿嘿嘿，看起来很亲热呢」"
    "才不是这样。"
    "冈部师傅肯定只是想和真由理多呆在一起一会儿。"
    "因为——这是最后的机会了。"
    "但是——"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_ASA01"),"True","lh/MAY_ASA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "RUK03A_MAY0032"
    $ current_voice = "voice/RUK03A_MAY0032.ogg"
    "真由理" "「太好了呢，琉华酱」"
    $ stopvoc("RUK")
    play RUK "RUK03A_RUK0037"
    $ current_voice = "voice/RUK03A_RUK0037.ogg"
    "琉华" "「恩，恩……」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_ASA01"),"True","lh/MAY_ASA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "RUK03A_MAY0033"
    $ current_voice = "voice/RUK03A_MAY0033.ogg"
    "真由理" "「那么大家和真由喜在和吹雪酱和枫酱汇合以后一起向Ｃｏｓｐｌａｙ广场出发吧！」"
    $ stopvoc("RUK")
    play RUK "RUK03A_RUK0038"
    $ current_voice = "voice/RUK03A_RUK0038.ogg"
    "琉华" "「啊……」"
    $ stopvoc("MAY")
    play MAY "RUK03A_MAY0034"
    $ current_voice = "voice/RUK03A_MAY0034.ogg"
    "真由理" "「好啦，快走吧，琉华酱！」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    $ stopvoc("RUK")
    play RUK "RUK03A_RUK0039"
    $ current_voice = "voice/RUK03A_RUK0039.ogg"
    "琉华" "「等等，真由理酱！」"
    "——但是，真的是那样吗。"
    window hide



    $ loadBG(0,"BG56A")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_ASA01"),"True","lh/MAY_ASA01a~ipad.png") at left as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA01"),"True","lh/OKA_ASA01a~ipad.png") at right as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    $ stopvoc("MAY")
    play MAY "RUK03A_MAY0035"
    $ current_voice = "voice/RUK03A_MAY0035.ogg"
    "真由理" "「啊，冈伦！有好好地在约好的地方等我呢」"
    $ stopvoc("OKA")
    play OKA "RUK03A_OKA0019"
    $ current_voice = "voice/RUK03A_OKA0019.ogg"
    "伦太郎" "「啊啊。我也没法跟你进更衣室啊。说起来……」"

    $ targetmailid = cml.setdefault("RM_RUK_SEND_UPP03","")

    $ LR_RM_CHANCE=2

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_ASA02"),"True","lh/MAY_ASA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    call CHECK_RM_RECEIVE
    $ stopvoc("MAY")
    play MAY "RUK03A_MAY0036"
    $ current_voice = "voice/RUK03A_MAY0036.ogg"
    "真由理" "「诶嘿嘿，琉华酱的样子，很在意吧？很在意吧？」"
    call CHECK_RM_RECEIVE
    $ stopvoc("OKA")
    play OKA "RUK03A_OKA0020"
    $ current_voice = "voice/RUK03A_OKA0020.ogg"
    "伦太郎" "「嘛，我才没有在意Ｃｏｓｐｌａｙ时的琉华子会变成什么样子呢」"

    call CHECK_RM_RECEIVE

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_ASA03"),"True","lh/MAY_ASA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "RUK03A_MAY0037"
    $ current_voice = "voice/RUK03A_MAY0037.ogg"
    "真由理" "「真是的，小冈伦还是一如既往的不坦率呢」"

    $ gd["RCVmailData"][gc["ScriptMacros"]["RM_RUK_RECV_UPP03_01"]]["late"]=True
    $ lml.append(gc["ScriptMacros"]["RM_RUK_RECV_UPP03_01"])

    $ stopvoc("RUK")
    play RUK "RUK03A_RUK0040"
    $ current_voice = "voice/RUK03A_RUK0040.ogg"
    "琉华" "「那，那个，真由理酱……」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_AMA01"),"True","lh/MAY_AMA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "RUK03A_MAY0038"
    $ current_voice = "voice/RUK03A_MAY0038.ogg"
    "真由理" "「好啦好啦，琉华酱也不要害羞了，这边这边。让冈伦看看也没关系的哦」"
    $ stopvoc("RUK")
    play RUK "RUK03A_RUK0041"
    $ current_voice = "voice/RUK03A_RUK0041.ogg"
    "琉华" "「恩，恩……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_AMA02"),"True","lh/MAY_AMA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "RUK03A_MAY0039"
    $ current_voice = "voice/RUK03A_MAY0039.ogg"
    "真由理" "「让你久等了。琉华酱隆重登场。锵锵！」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA01"),"True","lh/OKA_ASA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("RUK")
    play RUK "RUK03A_RUK0042"
    $ current_voice = "voice/RUK03A_RUK0042.ogg"
    "琉华" "「……」"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_COSTUME"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_COSTUME"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_COSTUME"])
    $ stopvoc("MAY")
    play MAY "RUK03A_MAY0040"
    $ current_voice = "voice/RUK03A_MAY0040.ogg"
    "真由理" "「看啊看啊冈伦。琉华酱出了凯拉玲酱的Ｃｏｓ哦！超可爱的吧！」"
    $ stopvoc("RUK")
    play RUK "RUK03A_RUK0043"
    $ current_voice = "voice/RUK03A_RUK0043.ogg"
    "琉华" "「那，那个……」"
    $ stopvoc("OKA")
    play OKA "RUK03A_OKA0021"
    $ current_voice = "voice/RUK03A_OKA0021.ogg"
    "伦太郎" "「…………」"
    $ stopvoc("MAY")
    play MAY "RUK03A_MAY0041"
    $ current_voice = "voice/RUK03A_MAY0041.ogg"
    "真由理" "「呐，呐？和真由理想的一样，琉华酱超适合凯拉玲酱的Ｃｏｓ的吧？」"
    $ stopvoc("OKA")
    play OKA "RUK03A_OKA0022"
    $ current_voice = "voice/RUK03A_OKA0022.ogg"
    "伦太郎" "「…………」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_ASA01"),"True","lh/MAY_ASA01a~ipad.png") at left as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA01"),"True","lh/OKA_ASA01a~ipad.png") at right as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "RUK03A_MAY0042"
    $ current_voice = "voice/RUK03A_MAY0042.ogg"
    "真由理" "「呼呼，琉华酱。你看冈伦看到了以后话都说不出来了哦？」"
    $ stopvoc("RUK")
    play RUK "RUK03A_RUK0044"
    $ current_voice = "voice/RUK03A_RUK0044.ogg"
    "琉华" "「那种事情……」"

    "感觉这么下去的话，真由理酱会死掉什么的就是骗人的。"
    "难道说是因为我回到了过去，来到了夏Ｃｏｍｉ，导致世界发生变化了？"
    "世界线？什么的变化了以后，就变成了真由理酱不会死掉的未来也说不定。"
    "不对，肯定是那样。"
    "因为，真由理酱看起来那么有精神。"
    "这么充满活力地说着笑着。"
    "所以说，未来肯定发生了变化！"
    "不会有错！"

    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    $ stopvoc("Y24")
    play KUR "RUK03A_Y240000"
    $ current_voice = "voice/RUK03A_Y240000.ogg"
    "拍客Ａ" "「那个……」"
    $ stopvoc("RUK")
    play RUK "RUK03A_RUK0045"
    $ current_voice = "voice/RUK03A_RUK0045.ogg"
    "琉华" "「诶！？」"
    $ stopvoc("Y24")
    play KUR "RUK03A_Y240001"
    $ current_voice = "voice/RUK03A_Y240001.ogg"
    "拍客Ａ" "「我想拍张照片，可以吗？」"
    "突然，我被不认识的人搭话了。"
    $ stopvoc("RUK")
    play RUK "RUK03A_RUK0046"
    $ current_voice = "voice/RUK03A_RUK0046.ogg"
    "琉华" "「照片……是在说我吗？」"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_ASA01"),"True","lh/MAY_ASA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "RUK03A_MAY0043"
    $ current_voice = "voice/RUK03A_MAY0043.ogg"
    "真由理" "「当然啦。琉华酱的Ｃｏｓ很可爱，所以大家都想拍你的照片啊」"
    $ stopvoc("RUK")
    play RUK "RUK03A_RUK0047"
    $ current_voice = "voice/RUK03A_RUK0047.ogg"
    "琉华" "「哪个，但是我……」"
    $ stopvoc("Y24")
    play KUR "RUK03A_Y240002"
    $ current_voice = "voice/RUK03A_Y240002.ogg"
    "拍客Ａ" "「那，拜托摆一个Ｐｏｓｅ！」"
    $ stopvoc("RUK")
    play RUK "RUK03A_RUK0048"
    $ current_voice = "voice/RUK03A_RUK0048.ogg"
    "琉华" "「Ｐｏｓｅ？」"
    $ stopvoc("MAY")
    play MAY "RUK03A_MAY0044"
    $ current_voice = "voice/RUK03A_MAY0044.ogg"
    "真由理" "「怎么来都行哦。只要可爱就可以了」"
    $ stopvoc("RUK")
    play RUK "RUK03A_RUK0049"
    $ current_voice = "voice/RUK03A_RUK0049.ogg"
    "琉华" "「但，但是……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_ASA02"),"True","lh/MAY_ASA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "RUK03A_MAY0045"
    $ current_voice = "voice/RUK03A_MAY0045.ogg"
    "真由理" "「没关系！真由喜也会陪着你的」"
    $ stopvoc("RUK")
    play RUK "RUK03A_RUK0050"
    $ current_voice = "voice/RUK03A_RUK0050.ogg"
    "琉华" "「真由理酱……」"
    $ stopvoc("MAY")
    play MAY "RUK03A_MAY0046"
    $ current_voice = "voice/RUK03A_MAY0046.ogg"
    "真由理" "「呐？拿出点自信来！」"
    "平时的话，突然被不认识的人搭话的话，我一定会很困扰地逃开吧。"
    "但是现在的我，对于未来说不定已经改变了怀着少许的期待。"
    "而且，真由理酱能在我身边这一点比什么都要令人安心。"
    "真由理酱鼓励着我。"
    "真由理酱正……"
    "所以我要。"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    hide screen phonebtn
    $ stopvoc("RUK")
    play RUK "RUK03A_RUK0051"
    $ current_voice = "voice/RUK03A_RUK0051.ogg"
    "琉华" "「这，这种感觉……怎么样？」"
    "我比平时多了一些勇气。"
    window hide
    play se "SGSE223"

    $ stopvoc("MAY")
    play MAY "RUK03A_MAY0047"
    $ current_voice = "voice/RUK03A_MAY0047.ogg"
    "真由理" "「恩恩，这感觉很不错哦，琉华酱」"
    $ stopvoc("RUK")
    play RUK "RUK03A_RUK0052"
    $ current_voice = "voice/RUK03A_RUK0052.ogg"
    "琉华" "「……是嘛？」"
    $ stopvoc("MAY")
    play MAY "RUK03A_MAY0048"
    $ current_voice = "voice/RUK03A_MAY0048.ogg"
    "真由理" "「没关系，真由喜保证ＯＫ的」"
    "但是——"
    window hide
    stop bgm 



    $ loadBG(2,"IBGX048")


    hide screen phonebtn
    "——只有一开始的时候我是这么想的。"
    window hide


    $ loadBG(2,"BG56A")



    hide screen phonebtn
    play se "SGSE007L" loop

    $ stopvoc("Y25")
    play KUR "RUK03A_Y250000"
    $ current_voice = "voice/RUK03A_Y250000.ogg"
    "拍客Ｂ" "「不好意思，请看我这边一下！」"
    $ stopvoc("RUK")
    play RUK "RUK03A_RUK0053"
    $ current_voice = "voice/RUK03A_RUK0053.ogg"
    "琉华" "「啊……好的！」"
    $ stopvoc("Y26")
    play KUR "RUK03A_Y260000"
    $ current_voice = "voice/RUK03A_Y260000.ogg"
    "拍客Ｃ" "「啊，接下来，希望你能看这边！」"
    $ stopvoc("RUK")
    play RUK "RUK03A_RUK0054"
    $ current_voice = "voice/RUK03A_RUK0054.ogg"
    "琉华" "「那个……」"
    "因为已经快到中午了，来到Ｃｏｓｐｌａｙ广场的人变多了，于是相应的想要拍照的人也不断增多。"
    $ stopvoc("Y27")
    play KUR "RUK03A_Y270000"
    $ current_voice = "voice/RUK03A_Y270000.ogg"
    "拍客Ｄ" "「不好意思，拜托了！！」"
    $ stopvoc("RUK")
    play RUK "RUK03A_RUK0055"
    $ current_voice = "voice/RUK03A_RUK0055.ogg"
    "琉华" "「…………」"
    "由于周围人数增加导致的恐惧感……"
    "刷的一下，就想起来和冈部师傅最初相遇时的事情。"
    "在秋叶原的街道上，被大量拿着照相机的男人包围的事。"
    hide screen phoneSD1
    window hide

    stop se


    $ loadBG(0,"EVX_R06A")

    hide screen phonebtn
    play bgm "FD2BGM04"


    "……不，不对。"
    "我和冈部师傅相遇的时候，是通过真由理酱介绍的。"
    "所以，这是——这份记忆是。"
    "以前的记忆。"
    "我还是——男生的“世界”的记忆。"

    window hide



    $ loadBG(0,"IBGX048")

    hide screen phonebtn
    show screen phoneSD1
    "所以，现在我所拥有的恐惧感，对于现在是女生的我来说有些奇怪。"
    "这么一想的话，心情变得十分复杂。"
    window hide



    $ loadBG(2,"BG56A")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_ASA01"),"True","lh/MAY_ASA01a~ipad.png") at left as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA01"),"True","lh/OKA_ASA01a~ipad.png") at right as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    show screen phonebtn
    show screen phoneSD1
    $ stopvoc("MAY")
    play MAY "RUK03A_MAY0049"
    $ current_voice = "voice/RUK03A_MAY0049.ogg"
    "真由理" "「琉华酱，好厉害啊。我知道你会很有人气的，但没想到会到这个程度啊。」"
    $ stopvoc("OKA")
    play OKA "RUK03A_OKA0023"
    $ current_voice = "voice/RUK03A_OKA0023.ogg"
    "伦太郎" "「是这样……的呢」"
    "说真的，这种情况下我真的很想马上逃走……"
    "但是真由理酱看到我被人们包围着的样子很开心。"
    "还有就是，守护着真由理酱的笑容的冈部师傅的身影。"
    "看着这样的两个人的样子，那种懦弱的话我说不出来。"
    hide screen phoneSD1
    window hide

    stop bgm 



    $ loadBG(0,"IBGX033")



    "在那之后，有很多人来拍我。"
    "在其中还有人给我名片，以及给我展示他们的杂志的名字和主页什么的，但是我不是很懂。"
    "只是，真由理酱看着这样的我，一直到最后还是开心地笑着。"


    window hide


    $ loadBG(0,"BG38N")

    play bgm "FD2BGM08"
    show screen phonebtn
    show screen phoneSD1
    "于是从国际展览馆出来的时候，太阳已经完全下手了，夜空中群星闪耀。"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_ASA01"),"True","lh/MAY_ASA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "RUK03A_MAY0050"
    $ current_voice = "voice/RUK03A_MAY0050.ogg"
    "真由理" "「搞到这么晚了啊」"
    $ stopvoc("RUK")
    play RUK "RUK03A_RUK0056"
    $ current_voice = "voice/RUK03A_RUK0056.ogg"
    "琉华" "「恩，是呢」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_ASA03"),"True","lh/MAY_ASA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "RUK03A_MAY0051"
    $ current_voice = "voice/RUK03A_MAY0051.ogg"
    "真由理" "「琉华酱，没问题？累坏了吧？」"
    $ stopvoc("RUK")
    play RUK "RUK03A_RUK0057"
    $ current_voice = "voice/RUK03A_RUK0057.ogg"
    "琉华" "「恩，稍微有点……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_ASB03"),"True","lh/MAY_ASB03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "RUK03A_MAY0052"
    $ current_voice = "voice/RUK03A_MAY0052.ogg"
    "真由理" "「但是这也是理所当然的嘛。被不认识的人这样拍照什么的」"
    $ stopvoc("OKA")
    play OKA "RUK03A_OKA0024"
    $ current_voice = "voice/RUK03A_OKA0024.ogg"
    "伦太郎" "「…………」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_ASA03"),"True","lh/MAY_ASA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "RUK03A_MAY0053"
    $ current_voice = "voice/RUK03A_MAY0053.ogg"
    "真由理" "「抱歉啊。要是累了的话在哪里休息一下就好了……」"
    $ stopvoc("RUK")
    play RUK "RUK03A_RUK0058"
    $ current_voice = "voice/RUK03A_RUK0058.ogg"
    "琉华" "「没事，没关系的。是我自己说要试一下的」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_ASA01"),"True","lh/MAY_ASA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "RUK03A_MAY0054"
    $ current_voice = "voice/RUK03A_MAY0054.ogg"
    "真由理" "「但是，虽然我知道人气会很高，但没想到竟然会有这么多人聚集起来，真由喜都吓了一跳呢」"
    $ stopvoc("MAY")
    play MAY "RUK03A_MAY0055"
    $ current_voice = "voice/RUK03A_MAY0055.ogg"
    "真由理" "「Ｃｏｓｐｌａｙ界的超新星出现了呢。呐，冈伦你说是吧」"
    $ stopvoc("OKA")
    play OKA "RUK03A_OKA0025"
    $ current_voice = "voice/RUK03A_OKA0025.ogg"
    "伦太郎" "「恩？　啊，啊啊。是这样吧……」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_ASA01"),"True","lh/MAY_ASA01a~ipad.png") at left as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA04"),"True","lh/OKA_ASA04a~ipad.png") at right as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    "随着时间过去，冈部师傅脸上的表情越来越沉重。"
    $ stopvoc("RUK")
    play RUK "RUK03A_RUK0059"
    $ current_voice = "voice/RUK03A_RUK0059.ogg"
    "琉华" "「…………」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_ASA02"),"True","lh/MAY_ASA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "RUK03A_MAY0056"
    $ current_voice = "voice/RUK03A_MAY0056.ogg"
    "真由理" "「冈伦的话，刚才看到琉华酱人气这么高冈伦都有点嫉妒了呢」"
    "虽然真由理这么说，但是我知道冈部师傅那样的表现的原因并不是因为我。"
    "逐渐迫近的期限。"
    "冈部师傅一定拼命地在抗拒着那份沉重的压力吧。"
    "但是——"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_ASA02"),"True","lh/MAY_ASA02a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "RUK03A_MAY0057"
    $ current_voice = "voice/RUK03A_MAY0057.ogg"
    "真由理" "「第一次Ｃｏｓｐｌａｙ，琉华酱觉得如何？开心吗」"
    $ stopvoc("RUK")
    play RUK "RUK03A_RUK0060"
    $ current_voice = "voice/RUK03A_RUK0060.ogg"
    "琉华" "「那个……比想象中的要好一些吧？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_ASA01"),"True","lh/MAY_ASA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "RUK03A_MAY0058"
    $ current_voice = "voice/RUK03A_MAY0058.ogg"
    "真由理" "「这样啊。但是我觉得你肯定能习惯那种感觉然后乐于其中的」"
    $ stopvoc("MAY")
    play MAY "RUK03A_MAY0059"
    $ current_voice = "voice/RUK03A_MAY0059.ogg"
    "真由理" "「能够从中获取乐趣之后，就可以比现在更加积极地向世界各地的人们展示琉华酱的可爱之处哦」"
    $ stopvoc("RUK")
    play RUK "RUK03A_RUK0061"
    $ current_voice = "voice/RUK03A_RUK0061.ogg"
    "琉华" "「那种事……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_ASA02"),"True","lh/MAY_ASA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "RUK03A_MAY0060"
    $ current_voice = "voice/RUK03A_MAY0060.ogg"
    "真由理" "「琉华酱，谢谢你了。真由喜对于琉华酱能鼓起勇气来参加Ｃｏｓｐｌａｙ这一点感到非常高兴」"
    $ stopvoc("RUK")
    play RUK "RUK03A_RUK0062"
    $ current_voice = "voice/RUK03A_RUK0062.ogg"
    "琉华" "「我也是。真由理酱能高兴的话真是太好了……」"
    "虽然说，也许——"
    $ stopvoc("MAY")
    play MAY "RUK03A_MAY0061"
    $ current_voice = "voice/RUK03A_MAY0061.ogg"
    "真由理" "「是吗。这样的话，真由喜就更加更加开心了哦」"
    $ stopvoc("RUK")
    play RUK "RUK03A_RUK0063"
    $ current_voice = "voice/RUK03A_RUK0063.ogg"
    "琉华" "「诶……」"
    $ stopvoc("MAY")
    play MAY "RUK03A_MAY0062"
    $ current_voice = "voice/RUK03A_MAY0062.ogg"
    "真由理" "「真由喜如果能看到琉华酱还有小冈伦和大家露出笑脸的话，就会感到很幸福哦」"
    $ stopvoc("RUK")
    play RUK "RUK03A_RUK0064"
    $ current_voice = "voice/RUK03A_RUK0064.ogg"
    "琉华" "「真由理酱……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_ASA01"),"True","lh/MAY_ASA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "RUK03A_MAY0063"
    $ current_voice = "voice/RUK03A_MAY0063.ogg"
    "真由理" "「啊！　是桶子君啊！」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    "也许，未来会——"

    $ targetmailid = 428

    $ LR_RM_CHANCE=2
    call CHECK_RM_RECEIVE
    $ stopvoc("MAY")
    play MAY "RUK03A_MAY0063a"
    $ current_voice = "voice/RUK03A_MAY0063a.ogg"
    "真由理" "「桶子君，这边这边ー！」"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_ASA01"),"True","lh/MAY_ASA01a~ipad.png") at left as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASB06"),"True","lh/DAR_ASB06a~ipad.png") at right as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    call CHECK_RM_RECEIVE
    $ stopvoc("DAR")
    play DAR "RUK03A_DAR0010"
    $ current_voice = "voice/RUK03A_DAR0010.ogg"
    "至" "「哈，呼，抱歉抱歉。那个确认战利品花了些时间啦」"

    call CHECK_RM_RECEIVE

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_ASA03"),"True","lh/MAY_ASA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "RUK03A_MAY0064"
    $ current_voice = "voice/RUK03A_MAY0064.ogg"
    "真由理" "「说起来桶子君，最后没来看Ｃｏｓｐｌａｙ呢」"


    $ stopvoc("DAR")
    play DAR "RUK03A_DAR0011"
    $ current_voice = "voice/RUK03A_DAR0011.ogg"
    "至" "「那是因为哈，排队的队伍比想象中要长啊」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_ASC02"),"True","lh/MAY_ASC02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "RUK03A_MAY0065"
    $ current_voice = "voice/RUK03A_MAY0065.ogg"
    "真由理" "「琉华酱，超厉害的哦。超级可爱，被大家团团围住了呢」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASB04"),"True","lh/DAR_ASB04a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "RUK03A_DAR0012"
    $ current_voice = "voice/RUK03A_DAR0012.ogg"
    "至" "「真的么？这么厉害？」"
    "是啊，未来已经改变了——"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_ASB03"),"True","lh/MAY_ASB03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "RUK03A_MAY0066"
    $ current_voice = "voice/RUK03A_MAY0066.ogg"
    "真由理" "「感觉如果没有看到那时候的她的话，感觉我的人生都要缺少一半了呢」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASB01"),"True","lh/DAR_ASB01a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "RUK03A_DAR0013"
    $ current_voice = "voice/RUK03A_DAR0013.ogg"
    "至" "「等等，一半也太多了吧」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_ASA01"),"True","lh/MAY_ASA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "RUK03A_MAY0067"
    $ current_voice = "voice/RUK03A_MAY0067.ogg"
    "真由理" "「啊，但是但是，如果琉华酱明天也来夏Ｃｏｍｉ的话，也还有机会再看到吧」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASB01"),"True","lh/DAR_ASB01a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "RUK03A_DAR0014"
    $ current_voice = "voice/RUK03A_DAR0014.ogg"
    "至" "「哦？琉华氏，明天也会来吗？」"
    $ stopvoc("RUK")
    play RUK "RUK03A_RUK0066"
    $ current_voice = "voice/RUK03A_RUK0066.ogg"
    "琉华" "「诶？　我的话……」"
    "到此为止一切正常——"
    $ stopvoc("OKA")
    play OKA "RUK03A_OKA0026"
    $ current_voice = "voice/RUK03A_OKA0026.ogg"
    "伦太郎" "「…………」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_ASA01"),"True","lh/MAY_ASA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide screen phonebtn
    $ stopvoc("MAY")
    play MAY "RUK03A_MAY0068"
    $ current_voice = "voice/RUK03A_MAY0068.ogg"
    "真由理" "「呐呐，琉华酱，明天也──」"
    stop bgm 

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_ASA04"),"True","lh/MAY_ASA04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    show screen phonebtn
    "明天，虽然这么说着，但是真由理酱的笑容凝固在了脸上。"
    play se "SGSE072"

    "拿着的手提箱，啪嗒一声直直地摔在地上。"
    $ stopvoc("MAY")
    play MAY "RUK03A_MAY0069"
    $ current_voice = "voice/RUK03A_MAY0069.ogg"
    "真由理" "「啊，咕，呃……」"
    play bgm "FD2BGM05"
    "明天——"
    "未来——"
    $ stopvoc("RUK")
    play RUK "RUK03A_RUK0067"
    $ current_voice = "voice/RUK03A_RUK0067.ogg"
    "琉华" "「真由理……酱……？」"
    "我缓缓捧起真由理酱的手。"
    hide screen phoneSD1
    window hide
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_RUK004A"]]["Check"]=True


    $ loadBG(2,"EV_RUK004A")



    hide screen phonebtn
    "就像抓住了整个宇宙一样。"
    "刚才脸上的笑容消失了，取而代之的是扭曲的痛苦神色。"
    "缓缓地。"
    window hide
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_RUK004B"]]["Check"]=True


    $ loadBG(2,"EV_RUK004B")



    "就仿佛时间的流逝变缓了一样。"
    "真由理酱就在那里。"
    window hide
    play se "SGSE014"

    stop bgm 


    $ loadBG(2,"BG_BLACK")



    "倒下了。"
    window hide


    $ loadBG(2,"BG38N")



    show screen phonebtn
    show screen phoneSD1
    $ stopvoc("RUK")
    play RUK "RUK03A_RUK0068"
    $ current_voice = "voice/RUK03A_RUK0068.ogg"
    "琉华" "「…………」"
    $ stopvoc("OKA")
    play OKA "RUK03A_OKA0027"
    $ current_voice = "voice/RUK03A_OKA0027.ogg"
    "伦太郎" "「…………」"
    $ stopvoc("DAR")
    play DAR "RUK03A_DAR0015"
    $ current_voice = "voice/RUK03A_DAR0015.ogg"
    "至" "「…………」"
    "那实在是太过突然。"
    "我们也只好束手无策地看着她倒下。"
    $ stopvoc("DAR")
    play DAR "RUK03A_DAR0016"
    $ current_voice = "voice/RUK03A_DAR0016.ogg"
    "至" "「真由氏……？」"
    "桥田君的声音远远地传了过来。"
    "路过的人冷眼相待，投来了不解的目光。"
    $ stopvoc("RUK")
    play RUK "RUK03A_RUK0069"
    $ current_voice = "voice/RUK03A_RUK0069.ogg"
    "琉华" "「啊……啊啊……」"
    play bgm "BGM24"
    "心跳加速。"
    "血流的声音大到仿佛要冲破鼓膜。"
    "真由理酱——一动不动。"
    "一点点动静都没有。"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASB04"),"True","lh/DAR_ASB04a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "RUK03A_DAR0017"
    $ current_voice = "voice/RUK03A_DAR0017.ogg"
    "至" "「真由氏！怎么了啊！」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    "桥田冲了过来。"
    "冈部师傅则——"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA01"),"True","lh/OKA_ASA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "RUK03A_OKA0028"
    $ current_voice = "voice/RUK03A_OKA0028.ogg"
    "伦太郎" "「…………」"
    "表情丝毫不变地看着那个场景。"
    $ stopvoc("DAR")
    play DAR "RUK03A_DAR0018"
    $ current_voice = "voice/RUK03A_DAR0018.ogg"
    "至" "「真由氏！　喂，真由氏！　真由氏啊！」"
    "桥田君跑到真由理酱身边将她抱了起来。"
    "拍着她的脸，一直叫着她的名字。"
    "但是，真由理酱还是没有反应。"
    $ stopvoc("DAR")
    play DAR "RUK03A_DAR0019"
    $ current_voice = "voice/RUK03A_DAR0019.ogg"
    "至" "「连呼吸……都没有了……」"
    $ stopvoc("DAR")
    play DAR "RUK03A_DAR0020"
    $ current_voice = "voice/RUK03A_DAR0020.ogg"
    "至" "「诶？　这算啥……这到底算什么哦……」"
    $ stopvoc("DAR")
    play DAR "RUK03A_DAR0021"
    $ current_voice = "voice/RUK03A_DAR0021.ogg"
    "至" "「冈伦！　真由氏，真由氏状态很奇怪哦！」"
    $ stopvoc("OKA")
    play OKA "RUK03A_OKA0029"
    $ current_voice = "voice/RUK03A_OKA0029.ogg"
    "伦太郎" "「……她已经死了啊。」"
    "死因是——心脏病发作。"
    "我知道。"
    "是的。明明我也是知道的。"
    "未来并没有改变。"
    "就算我回到了过去，未来也并没有发生改变。"
    $ stopvoc("RUK")
    play RUK "RUK03A_RUK0070"
    $ current_voice = "voice/RUK03A_RUK0070.ogg"
    "琉华" "「真由理……酱……」"
    "已经安息的真由理酱的身影又出现在了我的脑海里。"
    hide screen phoneSD1
    window hide


    $ loadBG(0,"BG_BLACK")


    "她就这么一副安详的神态，躺在小小的棺材里。"
    "被花包围着的真由理酱。"
    "冰冷的肌肤。"
    "白色的棚子。"
    "笑容的照片。"
    "黑色的边框。"
    "香火的味道。"
    "哭泣的声音。"
    "驶去的灵车。"
    "升天的灰烟。"
    "小小的箱子。"

    window hide


    $ loadBG(0,"BG38N")

    show screen phonebtn
    show screen phoneSD1
    $ stopvoc("DAR")
    play DAR "RUK03A_DAR0022"
    $ current_voice = "voice/RUK03A_DAR0022.ogg"
    "至" "「死了什么的……骗人的吧！？刚刚不是还在好好地说着话嘛！」"
    $ stopvoc("DAR")
    play DAR "RUK03A_DAR0023"
    $ current_voice = "voice/RUK03A_DAR0023.ogg"
    "至" "「喂，真由氏！快起来啊！是吓了一跳吧！只是吓了一跳昏过去了吧！只是为了骗我一下的吧！」"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA01"),"True","lh/OKA_ASA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "RUK03A_OKA0030"
    $ current_voice = "voice/RUK03A_OKA0030.ogg"
    "伦太郎" "「桶子」"
    "是哦。"
    $ stopvoc("OKA")
    play OKA "RUK03A_OKA0031"
    $ current_voice = "voice/RUK03A_OKA0031.ogg"
    "伦太郎" "「真由理，已经死了」"
    "我是知道的。"
    "虽然我知道。"
    "但是那时我并不在此。"
    "所以当我看到这一切的时候，完全没有现实感。"
    $ stopvoc("OKA")
    play OKA "RUK03A_OKA0032"
    $ current_voice = "voice/RUK03A_OKA0032.ogg"
    "伦太郎" "「赶紧叫救护车吧」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA01"),"True","lh/OKA_ASA01a~ipad.png") at left as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASB05"),"True","lh/DAR_ASB05a~ipad.png") at right as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "RUK03A_DAR0024"
    $ current_voice = "voice/RUK03A_DAR0024.ogg"
    "至" "「说起来，你这家伙怎么还这么一副淡然的样子啊！」"
    $ stopvoc("DAR")
    play DAR "RUK03A_DAR0025"
    $ current_voice = "voice/RUK03A_DAR0025.ogg"
    "至" "「她可是死了哦！再也不会回来了哦！你明白吗，冈伦！」"
    $ stopvoc("OKA")
    play OKA "RUK03A_OKA0033"
    $ current_voice = "voice/RUK03A_OKA0033.ogg"
    "伦太郎" "「……我明白的」"
    "尽管如此，现实中能感受到的只有绝望。"
    "我什么也做不到，只能站在那里。"
    $ stopvoc("OKA")
    play OKA "RUK03A_OKA0034"
    $ current_voice = "voice/RUK03A_OKA0034.ogg"
    "伦太郎" "「见死不救了哦。我。对真由理。」"
    hide screen phoneSD1
    window hide


    $ loadBG(2,"IBGX072")




    stop bgm 

    "在那之后，救护车赶来了，试图进行急救。"
    "但结果——并没有用。"



    $ loadBG(2,"BG_BLACK")




    "真由理酱死了。"


    hide screen phoneSD1
    window hide





    hide screen phonebtn
    scene expression Solid("000000")  with fade
    return
