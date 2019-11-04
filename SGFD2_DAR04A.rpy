label SGFD2_DAR04A:
    window hide


    $ loadBG(0,"BG01A")
    show expression Solid("000") as black :
        alpha 0.5








    play se "SGSE200L" loop



    $ date="8/16"
    $ day="MON"
    hide screen phonebtn
    hide screen phoneSD1

    $ stopvoc("DAR")
    play DAR "DAR04A_DAR0000"
    $ current_voice = "voice/DAR04A_DAR0000.ogg"
    "至" "「…………」"
    $ stopvoc("DAR")
    play DAR "DAR04A_DAR0001"
    $ current_voice = "voice/DAR04A_DAR0001.ogg"
    "至" "「……………………」"
    window hide
    play se "SGSE056"
    hide black 
    with Dissolve(0.2)








    $ stopvoc("DAR")
    play DAR "DAR04A_DAR0002"
    $ current_voice = "voice/DAR04A_DAR0002.ogg"
    "至" "「哈！？」"
    $ stopvoc("DAR")
    play DAR "DAR04A_DAR0003"
    $ current_voice = "voice/DAR04A_DAR0003.ogg"
    "至" "「诶、等下、现在是几点了！？　那个……」"
    show screen phonebtn
    show screen phoneSD1
    $ stopvoc("DAR")
    play DAR "DAR04A_DAR0004"
    $ current_voice = "voice/DAR04A_DAR0004.ogg"
    "至" "「已经过五点了！？　咕哦哦哦哦哦、我竟然会睡过头！　这点看来是赶不上头班车了！」"
    $ stopvoc("DAR")
    play DAR "DAR04A_DAR0005"
    $ current_voice = "voice/DAR04A_DAR0005.ogg"
    "至" "「可恶、别开玩笑啊。我真是太没用了」"
    $ stopvoc("DAR")
    play DAR "DAR04A_DAR0006"
    $ current_voice = "voice/DAR04A_DAR0006.ogg"
    "至" "「哈、是因为太在意筷女氏的事情所以才会睡不着的啊……」"
    $ stopvoc("DAR")
    play DAR "DAR04A_DAR0007"
    $ current_voice = "voice/DAR04A_DAR0007.ogg"
    "至" "「总之如果不快点准备一下的话」"
    $ stopvoc("DAR")
    play DAR "DAR04A_DAR0008"
    $ current_voice = "voice/DAR04A_DAR0008.ogg"
    "至" "「就算是这么说、好像也就是背个包而已」"
    "像新的毛巾啊，换洗的T恤衫已经放在包里了。"
    "接着再去冰箱里拿出三瓶冰好的矿泉水。"
    $ stopvoc("DAR")
    play DAR "DAR04A_DAR0009"
    $ current_voice = "voice/DAR04A_DAR0009.ogg"
    "至" "「啊、话说回来昨天真由氏说要我好好的洗个澡……」"
    "闻了闻自己的身体。"
    $ stopvoc("DAR")
    play DAR "DAR04A_DAR0010"
    $ current_voice = "voice/DAR04A_DAR0010.ogg"
    "至" "「这点程度的话没问题的」"
    "把水放进包里后背了起来。"
    "这重量硬生生地把肩膀压下去一节。"
    "就在这时，我突然注意到了电脑。"
    window hide


    $ loadBG(2,"BG02A1")



    "迅速地解锁了电脑，刷新了从昨天开始就一直开着的帖子。"
    "在我睡着之后，也有些看帖子的人回复了些什么。"
    "但是筷女氏没有回一句话。"
    $ stopvoc("DAR")
    play DAR "DAR04A_DAR0011"
    $ current_voice = "voice/DAR04A_DAR0011.ogg"
    "至" "「…………」"
    "虽然很在意，但是现在天都快亮了，不赶快的话就赶不上头班车了。"

    hide screen phoneSD1
    window hide

    stop se
    $ loadBG(0,"BG_BLACK",trans=Fade(1,1,1))
    window hide
    hide screen phoneSD1






    return
