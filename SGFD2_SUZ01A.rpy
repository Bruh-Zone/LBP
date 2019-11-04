label SGFD2_SUZ01A:
    show expression Solid("000") as background 
    with fade
    $ loadBG(0,"TIT005")
    $ renpy.pause(delay=3,hard=True)
    show expression Solid("000") as background 
    with fade
    $ date="8/10"
    $ day="TUE"
    $ RcvMail(284)







    $ loadBG(0,"BG_BLACK")

    play se "SGSE200L" loop

    hide screen phonebtn
    hide screen phoneSD1

    "这不是梦。"
    "虽然头脑还有些不清醒，但是我能确定这不是梦。"
    "昨晚前半部分还是很有趣的。"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_OFFKAI"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_OFFKAI"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_OFFKAI"])
    "在时间机器{color=#f00}线下会{/color}上虽然没有找到父亲，但是冈部伦太郎说我是他们的朋友。"
    "但是台风来了。下了暴雨。"
    "虽然昨晚很快乐，但是有种不好的预感让我半夜逃了出来。"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_RADIKAN"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_RADIKAN"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_RADIKAN"])
    "{color=#f00}广播馆{/color}的屋顶。镶嵌在地面里的时间机器，坏掉了。"
    "我，做了多余的事情。"
    "来２０１０年并顺便寻找父亲的时候弄坏了时间机器，已经没办法回到过去了。"
    "失败了。"
    "失败了。"
    "失败了。"
    "只能这样认为。"
    "我没办法修好时间机器。"
    "只知道使用方法。"
    "所以，回家路上出现的“那东西”是我受打击太大而产生的幻觉。"
    "也许我已经睡着了，也许这只是我的一个梦。我是这样认为的。"
    "无论怎样，我醒来时都会消失吧。"
    "我是这样认为的。"
    "也希望是这样的。"
    "“那东西”已经不可能再出现在我眼前。"
    "我是这样认为的。"
    "也希望是这样。"
    "所以，今天早上。"
    "在我擅自搭建在北之丸公园某处草坪的帐篷中。"
    "我从浅睡中醒来，安静地将头伸出帐篷外。"
    window hide

    stop se


    $ loadBG(3,"BG_WHITE")






    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_SUZ001A"]]["Check"]=True
    $ loadBG(0,"EV_SUZ001A")



    $ stopvoc("SUZ")
    play SUZ "SUZ01A_SUZ0000"
    $ current_voice = "voice/SUZ01A_SUZ0000.ogg"
    "铃羽β２" "「早上好，我准备好早饭了」"
    $ stopvoc("SUZ")
    play SUZ "SUZ01A_SUZ0001"
    $ current_voice = "voice/SUZ01A_SUZ0001.ogg"
    "铃羽ω２" "「主人，早上了哦，骗你的」"
    play bgm "FD2BGM10"
    "但是“那东西”还是出现在我的眼前。"
    "“那东西”指的是“是另一个的我们”。"
    "之所以说是“我们”，是因为她们是两个和我长得一样的人。"
    window hide


    $ loadBG(2,"EV_SUZ001A1")






    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ2')",DynamicDisplayable(mouthanime,"SUZ_BMB04"),"True","lh/SUZ_BMB04a~ipad.png") at right as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)






































    "第一个是“穿军装的我”。"
    "精神饱满看起来很严肃。"
    "肯定是真正的军人。从姿态上就能看出。"
    window hide





















    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ3')",DynamicDisplayable(mouthanime,"SUZ_DMA02"),"True","lh/SUZ_DMA02a~ipad.png") at left as lh1 zorder (10-1) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)






























    "第二个是“穿女仆服的我”。"
    "庸庸散散看起来很不严肃。"
    "肯定只是个普通人。姿态上就能看出。"
    window hide





























    "昨天在发现时间机器坏了后的回家路上，这两个人不知从何时开始走在了我的身边。"
    "不知道为什么。"
    "总之等我发现时已经在那里了，现在也在。……大概。如果不是幻觉的话。"
    window hide





    $ loadBG(0,"BG76A")

    hide lh1 
    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ3')",DynamicDisplayable(mouthanime,"SUZ_DMA01"),"True","lh/SUZ_DMA01a~ipad.png") at left as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ2')",DynamicDisplayable(mouthanime,"SUZ_BMB04"),"True","lh/SUZ_BMB04a~ipad.png") at right as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)




    show screen phonebtn
    show screen phoneSD1
    $ stopvoc("SUZ2")
    play SUZ "SUZ01A_SUZ0002"
    $ current_voice = "voice/SUZ01A_SUZ0002.ogg"
    "军装的我" "「怎么了？　不舒服吗？」"
    $ stopvoc("SUZ")
    play SUZ "SUZ01A_SUZ0003"
    $ current_voice = "voice/SUZ01A_SUZ0003.ogg"
    "铃羽" "「看起来也不像不舒服……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ2')",DynamicDisplayable(mouthanime,"SUZ_BMB03"),"True","lh/SUZ_BMB03a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ2")
    play SUZ2 "SUZ01A_SUZ0004"
    $ current_voice = "voice/SUZ01A_SUZ0004.ogg"
    "军装的我" "「那就好。昨天淋了很多雨，是不是感冒了？」"
    $ stopvoc("SUZ")
    play SUZ "SUZ01A_SUZ0005"
    $ current_voice = "voice/SUZ01A_SUZ0005.ogg"
    "铃羽" "「大概……没关系、谢谢」"
    "被有着相同面容的人关心真是种奇怪的感觉。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ2')",DynamicDisplayable(mouthanime,"SUZ_BMB04"),"True","lh/SUZ_BMB04a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ2")
    play SUZ2 "SUZ01A_SUZ0006"
    $ current_voice="voice/SUZ01A_SUZ0006.ogg"
    "军装的我" "「如果还没有完全醒的话，先洗洗脸如何？」"
    $ stopvoc("SUZ")
    play SUZ "SUZ01A_SUZ0007"
    $ current_voice = "voice/SUZ01A_SUZ0007.ogg"
    "铃羽" "「没关系。我已经醒了」"
    "头有些晕。"
    "只是有点搞不清楚状况而已。"
    "鼻子也很灵敏。"
    "能闻到穿军服的我所做出的美味味增汤的香味。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ3')",DynamicDisplayable(mouthanime,"SUZ_DMA03"),"True","lh/SUZ_DMA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ3")
    play SUZ3 "SUZ01A_SUZ0008"
    $ current_voice = "voice/SUZ01A_SUZ0008.ogg"
    "便服的我" "「话说，早饭，只有这点吗？」"
    $ stopvoc("SUZ2")
    play SUZ2 "SUZ01A_SUZ0009"
    $ current_voice = "voice/SUZ01A_SUZ0009.ogg"
    "军装的我" "「白饭加汤。已经足够了」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ3')",DynamicDisplayable(mouthanime,"SUZ_DMA05"),"True","lh/SUZ_DMA05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ3")
    play SUZ3 "SUZ01A_SUZ0010"
    $ current_voice = "voice/SUZ01A_SUZ0010.ogg"
    "便服的我" "「你在说什么啊。根本一点都不够」"
    "头有些晕。"
    "但是感觉自己不该回答他们两人的对话。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ2')",DynamicDisplayable(mouthanime,"SUZ_BMB01"),"True","lh/SUZ_BMB01a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ2")
    play SUZ2 "SUZ01A_SUZ0011"
    $ current_voice = "voice/SUZ01A_SUZ0011.ogg"
    "军装的我" "「铃羽，你跟她的意见一样？」"
    "穿军服的我，将我称为“铃羽”。"
    "虽然很想问一句，我是铃羽的话那你是谁，但还是忍住了。"
    $ stopvoc("SUZ")
    play SUZ "SUZ01A_SUZ0012"
    $ current_voice = "voice/SUZ01A_SUZ0012.ogg"
    "铃羽" "「我觉得已经足够了」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ3')",DynamicDisplayable(mouthanime,"SUZ_DMA03"),"True","lh/SUZ_DMA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ3")
    play SUZ3 "SUZ01A_SUZ0013"
    $ current_voice = "voice/SUZ01A_SUZ0013.ogg"
    "便服的我" "「哪里够了？真没法理解你们」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ2')",DynamicDisplayable(mouthanime,"SUZ_BMB02"),"True","lh/SUZ_BMB02a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ2")
    play SUZ2 "SUZ01A_SUZ0014"
    $ current_voice = "voice/SUZ01A_SUZ0014.ogg"
    "军装的我" "「不满意的话就别吃」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ3')",DynamicDisplayable(mouthanime,"SUZ_DMC01"),"True","lh/SUZ_DMC01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ3")
    play SUZ3 "SUZ01A_SUZ0015"
    $ current_voice = "voice/SUZ01A_SUZ0015.ogg"
    "便服的我" "「……随便抱怨一下就让我别吃，真是无法理喻」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ2')",DynamicDisplayable(mouthanime,"SUZ_BMB03"),"True","lh/SUZ_BMB03a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ2")
    play SUZ2 "SUZ01A_SUZ0016"
    $ current_voice = "voice/SUZ01A_SUZ0016.ogg"
    "军装的我" "「你，真是奢侈啊」"
    $ stopvoc("SUZ")
    play SUZ "SUZ01A_SUZ0017"
    $ current_voice = "voice/SUZ01A_SUZ0017.ogg"
    "铃羽" "「我没有怨言，可以让我吃吗？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ2')",DynamicDisplayable(mouthanime,"SUZ_BMB04"),"True","lh/SUZ_BMB04a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ2")
    play SUZ2 "SUZ01A_SUZ0018"
    $ current_voice = "voice/SUZ01A_SUZ0018.ogg"
    "军装的我" "「当然可以啊」"
    $ stopvoc("SUZ")
    play SUZ "SUZ01A_SUZ0019"
    $ current_voice = "voice/SUZ01A_SUZ0019.ogg"
    "铃羽" "「谢谢」"
    "穿军服的我，非常熟练地将味增汤递了过来。"
    "还有些烫嘴。"
    "小口小口地啜着。"
    $ stopvoc("SUZ")
    play SUZ "SUZ01A_SUZ0020"
    $ current_voice = "voice/SUZ01A_SUZ0020.ogg"
    "铃羽" "「啊……真是美味」"
    "只喝了一口就明白了。"
    "虽然看起来很朴素，但是配料的量非常精准。"
    "冈部伦太郎他们带我去过牛肉饭餐馆，比在那里喝过的还要美味。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ2')",DynamicDisplayable(mouthanime,"SUZ_BMA01"),"True","lh/SUZ_BMA01a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ2")
    play SUZ2 "SUZ01A_SUZ0021"
    $ current_voice = "voice/SUZ01A_SUZ0021.ogg"
    "军装的我" "「合你的口味真是太好了。原本我觉得，大概按照我的口味就可以了，但是也不能肯定就跟自己的一样」"
    $ stopvoc("SUZ")
    play SUZ "SUZ01A_SUZ0022"
    $ current_voice = "voice/SUZ01A_SUZ0022.ogg"
    "铃羽" "「喜好……是一样的吗」"
    "虽然外表一样，但味觉却不一定一样。"
    "因为会根据从小吃什么长大的而改变。"
    "但是我们三人在味觉这点上似乎并没有差异。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ3')",DynamicDisplayable(mouthanime,"SUZ_DMA06"),"True","lh/SUZ_DMA06a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ3")
    play SUZ3 "SUZ01A_SUZ0023"
    $ current_voice = "voice/SUZ01A_SUZ0023.ogg"
    "便服的我" "「的确，味道是很美味」"
    "女仆装的我，也扭扭捏捏地喝了味增汤，轻声表示赞同。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ2')",DynamicDisplayable(mouthanime,"SUZ_BMB03"),"True","lh/SUZ_BMB03a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ2")
    play SUZ2 "SUZ01A_SUZ0024"
    $ current_voice = "voice/SUZ01A_SUZ0024.ogg"
    "军装的我" "「我说过有怨言就不要吃」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ3')",DynamicDisplayable(mouthanime,"SUZ_DMA05"),"True","lh/SUZ_DMA05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ3")
    play SUZ3 "SUZ01A_SUZ0025"
    $ current_voice = "voice/SUZ01A_SUZ0025.ogg"
    "便服的我" "「这个，根本就不算怨言」"
    "味增汤的确存在，像现在这样一起吃饭。"
    "至少在我看来，那两人并不是幻觉。"
    "当然也有可能是连味增汤都是幻想出来的。"
    "总之，先假设那两人的存在。接着，就有必要开始稍微整理一下这个诡异的状况了。"
    $ stopvoc("SUZ")
    play SUZ "SUZ01A_SUZ0026"
    $ current_voice = "voice/SUZ01A_SUZ0026.ogg"
    "铃羽" "「那个，我该怎么称呼你们两人好呢？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ3')",DynamicDisplayable(mouthanime,"SUZ_DMA01"),"True","lh/SUZ_DMA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ3")
    play SUZ3 "SUZ01A_SUZ0027"
    $ current_voice = "voice/SUZ01A_SUZ0027.ogg"
    "便服的我" "「你在问我的名字吗？我是阿万音铃羽哦。叫我铃羽就可以了」"
    "穿女仆装的我，似乎没有理解问题的意思。"
    "这是在我们三人都叫铃羽的前提下问出的问题。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ2')",DynamicDisplayable(mouthanime,"SUZ_BMB04"),"True","lh/SUZ_BMB04a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ2")
    play SUZ2 "SUZ01A_SUZ0028"
    $ current_voice = "voice/SUZ01A_SUZ0028.ogg"
    "军装的我" "「我也是阿万音铃羽。而且她也是」"
    "穿军服的我，看着我这样回答。"
    $ stopvoc("SUZ3")
    play SUZ3 "SUZ01A_SUZ0029"
    $ current_voice = "voice/SUZ01A_SUZ0029.ogg"
    "便服的我" "「那，大家都叫铃羽吧」"
    $ stopvoc("SUZ")
    play SUZ "SUZ01A_SUZ0030"
    $ current_voice = "voice/SUZ01A_SUZ0030.ogg"
    "铃羽" "「这样的话，就分不清究竟是谁在跟谁讲话了」"
    $ stopvoc("SUZ3")
    play SUZ3 "SUZ01A_SUZ0031"
    $ current_voice = "voice/SUZ01A_SUZ0031.ogg"
    "便服的我" "「说起来到是如此」"
    $ stopvoc("SUZ2")
    play SUZ2 "SUZ01A_SUZ0032"
    $ current_voice = "voice/SUZ01A_SUZ0032.ogg"
    "军装的我" "「不，我还以为你有自明了」"
    $ stopvoc("SUZ3")
    play SUZ3 "SUZ01A_SUZ0033"
    $ current_voice = "voice/SUZ01A_SUZ0033.ogg"
    "便服的我" "「自明是什么？」"
    $ stopvoc("SUZ2")
    play SUZ2 "SUZ01A_SUZ0034"
    $ current_voice = "voice/SUZ01A_SUZ0034.ogg"
    "军装的我" "「就是不用说也会明白的意思」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ3')",DynamicDisplayable(mouthanime,"SUZ_DMA07"),"True","lh/SUZ_DMA07a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ3")
    play SUZ3 "SUZ01A_SUZ0035"
    $ current_voice = "voice/SUZ01A_SUZ0035.ogg"
    "便服的我" "「……我可不明白哦？」"
    $ stopvoc("SUZ2")
    play SUZ2 "SUZ01A_SUZ0036"
    $ current_voice = "voice/SUZ01A_SUZ0036.ogg"
    "军装的我" "「是呢」"
    $ stopvoc("SUZ")
    play SUZ "SUZ01A_SUZ0037"
    $ current_voice = "voice/SUZ01A_SUZ0037.ogg"
    "铃羽" "「你们两人，有没有什么好建议？ 能够帮助理清这个状况的建议」"
    $ stopvoc("SUZ2")
    play SUZ2 "SUZ01A_SUZ0038"
    $ current_voice="voice/SUZ01A_SUZ0038.ogg"
    "军装的我" "「我觉得，你应该被称为铃羽」"
    $ stopvoc("SUZ")
    play SUZ "SUZ01A_SUZ0039"
    $ current_voice = "voice/SUZ01A_SUZ0039.ogg"
    "铃羽" "「我吗？ 为什么？」"
    $ stopvoc("SUZ2")
    play SUZ2 "SUZ01A_SUZ0040"
    $ current_voice="voice/SUZ01A_SUZ0040.ogg"
    "军装的我" "「因为这个世界原本的阿万音铃羽就是你」"
    $ stopvoc("SUZ")
    play SUZ "SUZ01A_SUZ0041"
    $ current_voice = "voice/SUZ01A_SUZ0041.ogg"
    "铃羽" "「原来如此，简单明了」"
    "原本就不清楚我究竟是不是这个世界线里的阿万音铃羽。或者说，没有办法证明。"
    "而且，昨天记忆已经串成了线，是我的可能性最高。"
    "为了测试，将帐篷中的世界线变动率检测仪拿了出来。"
    window hide


    $ loadBG(2,"IBG049A",png=True,hide=False)



    "世界线变动率是……０．３３７３３７％。"
    "昨天以前，都是这个数值吧。"
    "感觉像是这个数值，但是没有能够确性的证据。"
    "有人告诉我，带着这个也没有用。"
    "能够察觉到变动率的数值变化的，只有做出了这台仪器的冈部伦太郎而已。"
    window hide
    hide background-png 
    with dissolve






    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ3')",DynamicDisplayable(mouthanime,"SUZ_DMA03"),"True","lh/SUZ_DMA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ3")
    play SUZ3 "SUZ01A_SUZ0042"
    $ current_voice="voice/SUZ01A_SUZ0042.ogg"
    "便服的我" "「那我就不是铃羽了吗？ 可我明明就是铃羽哦？ 怎么会这样？」"
    "在我查看检测仪的时候，另一个我将话题继续了下去。"
    $ stopvoc("SUZ2")
    play SUZ2 "SUZ01A_SUZ0043"
    $ current_voice="voice/SUZ01A_SUZ0043.ogg"
    "军装的我" "「因为我跟你在这里都是外乡人(Ｓｔｒａｎｇｅｒ)」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ3')",DynamicDisplayable(mouthanime,"SUZ_DMA05"),"True","lh/SUZ_DMA05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ3")
    play SUZ3 "SUZ01A_SUZ0044"
    $ current_voice="voice/SUZ01A_SUZ0044.ogg"
    "便服的我" "「但是我就是我。铃羽就是铃羽哦！」"
    $ stopvoc("SUZ2")
    play SUZ2 "SUZ01A_SUZ0045"
    $ current_voice="voice/SUZ01A_SUZ0045.ogg"
    "军装的我" "「无疑，你在任何世界线中都是阿万音铃羽君。但是现在我们谈的是该怎么互相称呼的问题」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ3')",DynamicDisplayable(mouthanime,"SUZ_DMA01"),"True","lh/SUZ_DMA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ3")
    play SUZ3 "SUZ01A_SUZ0046"
    $ current_voice="voice/SUZ01A_SUZ0046.ogg"
    "便服的我" "「称呼是？」"
    $ stopvoc("SUZ2")
    play SUZ2 "SUZ01A_SUZ0047"
    $ current_voice="voice/SUZ01A_SUZ0047.ogg"
    "军装的我" "「就是用什么名字来叫」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ3')",DynamicDisplayable(mouthanime,"SUZ_DMB03"),"True","lh/SUZ_DMB03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ3")
    play SUZ3 "SUZ01A_SUZ0048"
    $ current_voice="voice/SUZ01A_SUZ0048.ogg"
    "便服的我" "「嗯，虽然不是很清楚，我们之间相互称呼铃羽的话，就叫铃羽１，铃羽２，铃羽３如何？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ2')",DynamicDisplayable(mouthanime,"SUZ_BMA06"),"True","lh/SUZ_BMA06a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ2")
    play SUZ2 "SUZ01A_SUZ0049"
    $ current_voice="voice/SUZ01A_SUZ0049.ogg"
    "军装的我" "「我完全不明白你举的例子」"
    $ stopvoc("SUZ3")
    play SUZ3 "SUZ01A_SUZ0050"
    $ current_voice="voice/SUZ01A_SUZ0050.ogg"
    "便服的我" "「我是不明白你的说话方式」"
    $ stopvoc("SUZ")
    play SUZ "SUZ01A_SUZ0051"
    $ current_voice = "voice/SUZ01A_SUZ0051.ogg"
    "铃羽" "「好啦好啦」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ2')",DynamicDisplayable(mouthanime,"SUZ_BMB04"),"True","lh/SUZ_BMB04a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ2")
    play SUZ2 "SUZ01A_SUZ0052"
    $ current_voice="voice/SUZ01A_SUZ0052.ogg"
    "军装的我" "「铃羽。我想知道这个世界线的世界变动率」"
    "军服的我一边说一边看着我。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ3')",DynamicDisplayable(mouthanime,"SUZ_DMA02"),"True","lh/SUZ_DMA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ3")
    play SUZ3 "SUZ01A_SUZ0053"
    $ current_voice="voice/SUZ01A_SUZ0053.ogg"
    "便服的我" "「哇，这是什么」"
    $ stopvoc("SUZ")
    play SUZ "SUZ01A_SUZ0054"
    $ current_voice = "voice/SUZ01A_SUZ0054.ogg"
    "铃羽" "「是表示实际世界线变动率的测量仪」"
    "女仆装的我似乎没见过。"
    "军服的我，似乎知道。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ2')",DynamicDisplayable(mouthanime,"SUZ_BMB01"),"True","lh/SUZ_BMB01a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ2")
    play SUZ2 "SUZ01A_SUZ0055"
    $ current_voice="voice/SUZ01A_SUZ0055.ogg"
    "军装的我" "「０％台吗……。我所在的世界线……是怎样的呢」"
    $ stopvoc("SUZ")
    play SUZ "SUZ01A_SUZ0056"
    $ current_voice = "voice/SUZ01A_SUZ0056.ogg"
    "铃羽" "「就算数值变动了，我们也没办法知道。你不知道吗？」"
    $ stopvoc("SUZ2")
    play SUZ2 "SUZ01A_SUZ0057"
    $ current_voice="voice/SUZ01A_SUZ0057.ogg"
    "军装的我" "「…………」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ2')",DynamicDisplayable(mouthanime,"SUZ_BMB04"),"True","lh/SUZ_BMB04a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ2")
    play SUZ2 "SUZ01A_SUZ0058"
    $ current_voice="voice/SUZ01A_SUZ0058.ogg"
    "军装的我" "「那么，假如将这个世界线称为α世界线。也就是说，你是α世界线中的阿万音铃羽」"
    "军服的我指着我。"
    $ stopvoc("SUZ2")
    play SUZ2 "SUZ01A_SUZ0059"
    $ current_voice="voice/SUZ01A_SUZ0059.ogg"
    "军装的我" "「然后，同理我的是β。那边的她被称为γ」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ3')",DynamicDisplayable(mouthanime,"SUZ_DMA01"),"True","lh/SUZ_DMA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ3")
    play SUZ3 "SUZ01A_SUZ0060"
    $ current_voice="voice/SUZ01A_SUZ0060.ogg"
    "便服的我" "「同理，是什么意思？」"
    $ stopvoc("SUZ2")
    play SUZ2 "SUZ01A_SUZ0061"
    $ current_voice="voice/SUZ01A_SUZ0061.ogg"
    "军装的我" "「是同样道理的意思」"

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ3')",DynamicDisplayable(mouthanime,"SUZ_DMA05"),"True","lh/SUZ_DMA05a~ipad.png") at left as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)










    $ stopvoc("SUZ3")
    play SUZ3 "SUZ01A_SUZ0062"
    $ current_voice="voice/SUZ01A_SUZ0062.ogg"
    "便服的我" "「这个女孩子是α，你是β然后我是γ？　总觉得，将我放在最后面会不会很奇怪？」"


    $ stopvoc("SUZ2")
    play SUZ2 "SUZ01A_SUZ0063"
    $ current_voice="voice/SUZ01A_SUZ0063.ogg"
    "铃羽β" "「只是编号而已。没有顺序的意思」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ3')",DynamicDisplayable(mouthanime,"SUZ_DMA03"),"True","lh/SUZ_DMA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "SUZ01A_SUZ0064"
    $ current_voice = "voice/SUZ01A_SUZ0064.ogg"
    "铃羽ω４" "「没有特别意思的话那我可以改吗？」"
    $ stopvoc("SUZ2")
    play SUZ2 "SUZ01A_SUZ0065"
    $ current_voice="voice/SUZ01A_SUZ0065.ogg"
    "铃羽β" "「可以」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ3')",DynamicDisplayable(mouthanime,"SUZ_DMA01"),"True","lh/SUZ_DMA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "SUZ01A_SUZ0066"
    $ current_voice = "voice/SUZ01A_SUZ0066.ogg"
    "铃羽ω４" "「那么我就叫铃羽。后面什么都不要加」"
    $ stopvoc("SUZ2")
    play SUZ2 "SUZ01A_SUZ0067"
    $ current_voice="voice/SUZ01A_SUZ0067.ogg"
    "铃羽β" "「这可不行」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ3')",DynamicDisplayable(mouthanime,"SUZ_DMA05"),"True","lh/SUZ_DMA05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "SUZ01A_SUZ0068"
    $ current_voice = "voice/SUZ01A_SUZ0068.ogg"
    "铃羽ω４" "「为什么！？」"
    $ stopvoc("SUZ2")
    play SUZ2 "SUZ01A_SUZ0069"
    $ current_voice="voice/SUZ01A_SUZ0069.ogg"
    "铃羽β" "「阿万音铃羽，是她的名字」"
    "似乎指的就是我。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ3')",DynamicDisplayable(mouthanime,"SUZ_DMC01"),"True","lh/SUZ_DMC01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "SUZ01A_SUZ0070"
    $ current_voice = "voice/SUZ01A_SUZ0070.ogg"
    "铃羽ω４" "「这样没办法明白，还是我叫铃羽比较好」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ2')",DynamicDisplayable(mouthanime,"SUZ_BMA03"),"True","lh/SUZ_BMA03a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    "这样下去好像永远结束不了了。"
    "我还是提出个折中方案比较好。"
    $ stopvoc("SUZ")
    play SUZ "SUZ01A_SUZ0071"
    $ current_voice = "voice/SUZ01A_SUZ0071.ogg"
    "铃羽" "「那我叫α也没关系哦」"
    $ stopvoc("SUZ")
    play SUZ "SUZ01A_SUZ0072"
    $ current_voice = "voice/SUZ01A_SUZ0072.ogg"
    "铃羽" "「我是α。军装的是β。然后女仆装的叫铃羽。这样，我们就知道在称呼谁了」"
    $ stopvoc("SUZ2")
    play SUZ2 "SUZ01A_SUZ0073"
    $ current_voice="voice/SUZ01A_SUZ0073.ogg"
    "铃羽β" "「不行，你不是阿万音就不行」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ3')",DynamicDisplayable(mouthanime,"SUZ_DMA05"),"True","lh/SUZ_DMA05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "SUZ01A_SUZ0074"
    $ current_voice = "voice/SUZ01A_SUZ0074.ogg"
    "铃羽ω４" "「但是我想当铃羽！」"
    $ stopvoc("SUZ")
    play SUZ "SUZ01A_SUZ0075"
    $ current_voice = "voice/SUZ01A_SUZ0075.ogg"
    "铃羽" "「所以说我是α就行」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ2')",DynamicDisplayable(mouthanime,"SUZ_BMB04"),"True","lh/SUZ_BMB04a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ2")
    play SUZ2 "SUZ01A_SUZ0076"
    $ current_voice="voice/SUZ01A_SUZ0076.ogg"
    "铃羽β" "「这不行」"
    $ stopvoc("SUZ")
    play SUZ "SUZ01A_SUZ0077"
    $ current_voice = "voice/SUZ01A_SUZ0077.ogg"
    "铃羽" "「嗯」"
    "军服的我似乎也很坚持己见。"
    "就这样造成了我们持续瞪着对方。"
    $ stopvoc("SUZ2")
    play SUZ2 "SUZ01A_SUZ0078"
    $ current_voice="voice/SUZ01A_SUZ0078.ogg"
    "铃羽β" "「不喜欢γ的话，叫ω如何？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ3')",DynamicDisplayable(mouthanime,"SUZ_DMA01"),"True","lh/SUZ_DMA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "SUZ01A_SUZ0079"
    $ current_voice = "voice/SUZ01A_SUZ0079.ogg"
    "铃羽ω４" "「Ｏｍｅｇａ？」"
    $ stopvoc("SUZ2")
    play SUZ2 "SUZ01A_SUZ0080"
    $ current_voice="voice/SUZ01A_SUZ0080.ogg"
    "铃羽β" "「α是第一个字母，ω是最后一个字母」"

    hide lh8 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ3')",DynamicDisplayable(mouthanime,"SUZ_DMA05"),"True","lh/SUZ_DMA05a~ipad.png") at left as lh8 zorder (10-8) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)








    $ stopvoc("SUZ3")
    play SUZ3 "SUZ01A_SUZ0081"
    $ current_voice="voice/SUZ01A_SUZ0081.ogg"
    "铃羽ω" "「Ｏｍｅｇａ……虽然叫法听起来挺帅气的，但还是铃羽好！」"


    window hide


    $ loadBG(2,"IBGX048")



    "就这样他们两个“另一个我”继续将讨论进行下去。"
    "老实说，我叫什么都没关系。"
    $ stopvoc("SUZ")
    play SUZ "SUZ01A_SUZ0082"
    $ current_voice = "voice/SUZ01A_SUZ0082.ogg"
    "铃羽" "「哈哈哈哈哈……」"
    "我觉得，那位铃羽和这位铃羽，都很厉害呢。"
    "但是β一定要坚持称她为ω，她也一定坚持要称自己为铃羽。"
    "但是，综合来说，军服的我还是比任性的女仆装的我要稍微成熟一些。"
    window hide

    $ loadBG(0,"BG76A")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ3')",DynamicDisplayable(mouthanime,"SUZ_DMA05"),"True","lh/SUZ_DMA05a~ipad.png") at left as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ2')",DynamicDisplayable(mouthanime,"SUZ_BMB04"),"True","lh/SUZ_BMB04a~ipad.png") at right as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)





    $ stopvoc("SUZ2")
    play SUZ2 "SUZ01A_SUZ0083"
    $ current_voice="voice/SUZ01A_SUZ0083.ogg"
    "铃羽β" "「那这样吧」"
    $ stopvoc("SUZ2")
    play SUZ2 "SUZ01A_SUZ0084"
    $ current_voice="voice/SUZ01A_SUZ0084.ogg"
    "铃羽β" "「你是α」"
    "看着我，被称为β的我这样说。"
    $ stopvoc("SUZ2")
    play SUZ2 "SUZ01A_SUZ0085"
    $ current_voice="voice/SUZ01A_SUZ0085.ogg"
    "铃羽β" "「我是β」"
    "然后β转身看着女仆装的我。"
    $ stopvoc("SUZ2")
    play SUZ2 "SUZ01A_SUZ0086"
    $ current_voice="voice/SUZ01A_SUZ0086.ogg"
    "铃羽β" "「然后你是铃羽。但是，我却将你当成ω来看待」"
    $ stopvoc("SUZ2")
    play SUZ2 "SUZ01A_SUZ0087"
    $ current_voice="voice/SUZ01A_SUZ0087.ogg"
    "铃羽β" "「这样可以了吗？」"
    $ stopvoc("SUZ")
    play SUZ "SUZ01A_SUZ0088"
    $ current_voice = "voice/SUZ01A_SUZ0088.ogg"
    "铃羽" "「没有异议」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ3')",DynamicDisplayable(mouthanime,"SUZ_DMA01"),"True","lh/SUZ_DMA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ3")
    play SUZ3 "SUZ01A_SUZ0089"
    $ current_voice="voice/SUZ01A_SUZ0089.ogg"
    "铃羽ω" "「虽然不太明白意思，但是这样也好」"
    "终于，漫长的会话结束了。"
    "决定我们的称呼也是很辛苦的。"
    "跟自己说话，也很累。"
    "虽然两人看起来都像我，但是内心却有很大的不同。"
    "感觉单是弄明白这一件事这个早上就算有意义了。"
    hide screen phoneSD1
    window hide

    stop bgm 



    $ loadBG(0,"BG04A1")
    play se "SGSE017"


    play bgm "BGM05"

    show screen phonebtn
    show screen phoneSD1
    "对我们来说幸运的是这两个“另一个我”，其他人是看不到的。"
    "多亏了这样，将两人带到打工的地方也没有被店长骂。"
    "再加上就算没有顾客来，也毫不无聊地度过了，这算是意外的惊喜。"

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ3')",DynamicDisplayable(mouthanime,"SUZ_DMA01"),"True","lh/SUZ_DMA01a~ipad.png") at left as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ3")
    play SUZ3 "SUZ01A_SUZ0090"
    $ current_voice="voice/SUZ01A_SUZ0090.ogg"
    "铃羽ω" "「这家店，是卖什么的？」"
    "因为女仆装的我——在我的心中也被称为ω——不停地东张西望，让我看着都有些疲惫了。"

    hide lh7 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ2')",DynamicDisplayable(mouthanime,"SUZ_BMB04"),"True","lh/SUZ_BMB04a~ipad.png") at right as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ2")
    play SUZ2 "SUZ01A_SUZ0091"
    $ current_voice="voice/SUZ01A_SUZ0091.ogg"
    "铃羽β" "「这里卖旧型电视机」"
    "另一边，军服的我笔直地站在那里一动不动。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ3')",DynamicDisplayable(mouthanime,"SUZ_DMA05"),"True","lh/SUZ_DMA05a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ3")
    play SUZ3 "SUZ01A_SUZ0092"
    $ current_voice="voice/SUZ01A_SUZ0092.ogg"
    "铃羽ω" "「电视机？ 这是电视机啊？ 这个时代的电视机是这么厚重的东西啊」"
    $ stopvoc("SUZ2")
    play SUZ2 "SUZ01A_SUZ0093"
    $ current_voice="voice/SUZ01A_SUZ0093.ogg"
    "铃羽β" "「这里卖在这个时代也算是旧货的东西吧」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ3')",DynamicDisplayable(mouthanime,"SUZ_DMA01"),"True","lh/SUZ_DMA01a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ3")
    play SUZ3 "SUZ01A_SUZ0094"
    $ current_voice="voice/SUZ01A_SUZ0094.ogg"
    "铃羽ω" "「为什么？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ2')",DynamicDisplayable(mouthanime,"SUZ_BMB03"),"True","lh/SUZ_BMB03a~ipad.png") as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ2")
    play SUZ2 "SUZ01A_SUZ0095"
    $ current_voice="voice/SUZ01A_SUZ0095.ogg"
    "铃羽β" "「因为怀旧主义和复古情怀。像是铃羽穿的运动服」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ3')",DynamicDisplayable(mouthanime,"SUZ_DMA03"),"True","lh/SUZ_DMA03a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ3")
    play SUZ3 "SUZ01A_SUZ0096"
    $ current_voice="voice/SUZ01A_SUZ0096.ogg"
    "铃羽ω" "「我？　我可不穿运动服哦？」"

    $ targetmailid = gc["ScriptMacros"]["RM_SUZ_RECV_RUK01_01"]

    $ LR_RM_CHANCE=4

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ2')",DynamicDisplayable(mouthanime,"SUZ_BMB02"),"True","lh/SUZ_BMB02a~ipad.png") as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    call CHECK_RM_RECEIVE
    $ stopvoc("SUZ2")
    play SUZ2 "SUZ01A_SUZ0097"
    $ current_voice="voice/SUZ01A_SUZ0097.ogg"
    "铃羽β" "「我指的是α铃羽」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ3')",DynamicDisplayable(mouthanime,"SUZ_DMA02"),"True","lh/SUZ_DMA02a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    call CHECK_RM_RECEIVE
    $ stopvoc("SUZ3")
    play SUZ3 "SUZ01A_SUZ0098"
    $ current_voice="voice/SUZ01A_SUZ0098.ogg"
    "铃羽ω" "「啊啊，那个铃羽啊」"
    call CHECK_RM_RECEIVE
    $ stopvoc("SUZ")
    play SUZ "SUZ01A_SUZ0099"
    $ current_voice = "voice/SUZ01A_SUZ0099.ogg"
    "铃羽" "「哈哈哈……」"
    call CHECK_RM_RECEIVE
    "果然变成这样了。"

    call CHECK_RM_RECEIVE


    hide lh5 
    hide lh6 
    hide lh7 
    show expression ConditionSwitch("renpy.music.get_playing(channel='TEN')",DynamicDisplayable(mouthanime,"TEN_BMA02"),"True","lh/TEN_BMA02a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("TEN")
    play TEN "SUZ01A_TEN0000"
    $ current_voice = "voice/SUZ01A_TEN0000.ogg"
    "天王寺" "「怎么了，打工的。打起精神来，打起精神来」"
    $ stopvoc("SUZ")
    play SUZ "SUZ01A_SUZ0100"
    $ current_voice = "voice/SUZ01A_SUZ0100.ogg"
    "铃羽" "「抱歉，店长」"
    $ stopvoc("TEN")
    play TEN "SUZ01A_TEN0001"
    $ current_voice = "voice/SUZ01A_TEN0001.ogg"
    "天王寺" "「你昨天也去二楼冈部他们那里疯闹了吗？」"
    $ stopvoc("SUZ")
    play SUZ "SUZ01A_SUZ0101"
    $ current_voice = "voice/SUZ01A_SUZ0101.ogg"
    "铃羽" "「半途就走了」"
    "然后，我走到了电台馆那边去，发现了时间机器已经坏掉的事实。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='TEN')",DynamicDisplayable(mouthanime,"TEN_BMA01"),"True","lh/TEN_BMA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("TEN")
    play TEN "SUZ01A_TEN0002"
    $ current_voice = "voice/SUZ01A_TEN0002.ogg"
    "天王寺" "「那就不是睡眠不足啦？」"
    $ stopvoc("SUZ")
    play SUZ "SUZ01A_SUZ0102"
    $ current_voice = "voice/SUZ01A_SUZ0102.ogg"
    "铃羽" "「有比睡眠不足更严重的问题……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='TEN')",DynamicDisplayable(mouthanime,"TEN_BMA03"),"True","lh/TEN_BMA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("TEN")
    play TEN "SUZ01A_TEN0003"
    $ current_voice = "voice/SUZ01A_TEN0003.ogg"
    "天王寺" "「更严重的问题？ 不要说的这么夸张」"
    $ stopvoc("SUZ")
    play SUZ "SUZ01A_SUZ0103"
    $ current_voice = "voice/SUZ01A_SUZ0103.ogg"
    "铃羽" "「店长没有经历过吗？ 见到另一个自己。还见到了两个」"
    $ stopvoc("TEN")
    play TEN "SUZ01A_TEN0004"
    $ current_voice = "voice/SUZ01A_TEN0004.ogg"
    "天王寺" "「这是什么。新出的都市传说？」"
    $ stopvoc("SUZ")
    play SUZ "SUZ01A_SUZ0104"
    $ current_voice = "voice/SUZ01A_SUZ0104.ogg"
    "铃羽" "「我就知道你不会相信，刚刚，你看见了吧」"
    "原以为他会生气地说你在说什么啊，结果店长却在很认真地思考着。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='TEN')",DynamicDisplayable(mouthanime,"TEN_BMA02"),"True","lh/TEN_BMA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("TEN")
    play TEN "SUZ01A_TEN0005"
    $ current_voice = "voice/SUZ01A_TEN0005.ogg"
    "天王寺" "「两个“另一个”自己……就像是重影一样吗」"
    $ stopvoc("SUZ")
    play SUZ "SUZ01A_SUZ0105"
    $ current_voice = "voice/SUZ01A_SUZ0105.ogg"
    "铃羽" "「重影？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='TEN')",DynamicDisplayable(mouthanime,"TEN_BMA01"),"True","lh/TEN_BMA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("TEN")
    play TEN "SUZ01A_TEN0006"
    $ current_voice = "voice/SUZ01A_TEN0006.ogg"
    "天王寺" "「现在的电视很精致所以不太能见到了。以前的电视机中经常会出现哦」"
    $ stopvoc("SUZ")
    play SUZ "SUZ01A_SUZ0106"
    $ current_voice = "voice/SUZ01A_SUZ0106.ogg"
    "铃羽" "「诶？　你说的是电视机？」"
    $ stopvoc("TEN")
    play TEN "SUZ01A_TEN0007"
    $ current_voice = "voice/SUZ01A_TEN0007.ogg"
    "天王寺" "「只要是我说出的话，都肯定是跟电视相关的吧」"
    $ stopvoc("SUZ")
    play SUZ "SUZ01A_SUZ0107"
    $ current_voice = "voice/SUZ01A_SUZ0107.ogg"
    "铃羽" "「这个，嗯，说的也是」"
    "我一边看着店内一边小声说，也只能接受这个说法。"
    $ stopvoc("SUZ")
    play SUZ "SUZ01A_SUZ0108"
    $ current_voice = "voice/SUZ01A_SUZ0108.ogg"
    "铃羽" "「那，重影是怎样产生的？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='TEN')",DynamicDisplayable(mouthanime,"TEN_BMA02"),"True","lh/TEN_BMA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("TEN")
    play TEN "SUZ01A_TEN0008"
    $ current_voice = "voice/SUZ01A_TEN0008.ogg"
    "天王寺" "「嗯，比如说本该一条直线发送过来的电波，与在山和大楼的反射下生成的电波，一起被天线接收了。这两者时间肯定会有时间差吧」"
    $ stopvoc("TEN")
    play TEN "SUZ01A_TEN0009"
    $ current_voice = "voice/SUZ01A_TEN0009.ogg"
    "天王寺" "「于是，原本有影像的地方，左右都有影像」"
    $ stopvoc("TEN")
    play TEN "SUZ01A_TEN0010"
    $ current_voice = "voice/SUZ01A_TEN0010.ogg"
    "天王寺" "「这就是重影的原理。年轻人没有见过吧」"
    $ stopvoc("SUZ")
    play SUZ "SUZ01A_SUZ0109"
    $ current_voice = "voice/SUZ01A_SUZ0109.ogg"
    "铃羽" "「嗯。一时根本想像不出来」"
    $ stopvoc("TEN")
    play TEN "SUZ01A_TEN0011"
    $ current_voice = "voice/SUZ01A_TEN0011.ogg"
    "天王寺" "「从技术上来说不是左右而是时间的前后。左边出现的是先到达的重影，右边出现的是后到达的重影」"
    $ stopvoc("SUZ")
    play SUZ "SUZ01A_SUZ0110"
    $ current_voice = "voice/SUZ01A_SUZ0110.ogg"
    "铃羽" "「可能是重影吧」"
    "这样说起来，我目前的状况的确与重影现象很相似。"
    "感觉现实中发生的事情，是不能与电视机所产生的现象相提并论，但是这种细节现在不需要太在意。"
    $ stopvoc("SUZ")
    play SUZ "SUZ01A_SUZ0111"
    $ current_voice = "voice/SUZ01A_SUZ0111.ogg"
    "铃羽" "「也就是说，无论是β还是ω或者我都有可能是别的世界线的？ 这是复数世界线中的我，重合在一起的状态？？」"
    "于是出现了前后并存的重影现象。"
    "如果真是这样，被称为α的我对ω和β来说，也许并不是什么坏名字。"
    "被称为ω的女仆装的我是前面的重影。"
    "被称为β的军装的我是后面的重影。"
    "就这样，我明白了，原本无法解决的问题，在命名后竟然意外的符合道理。"

    $ gd["RCVmailData"][gc["ScriptMacros"]["RM_SUZ_RECV_RUK01_01"]]["late"]=True
    $ lml.append(gc["ScriptMacros"]["RM_SUZ_RECV_RUK01_01"])

    hide screen phoneSD1
    window hide

    stop bgm 



    $ loadBG(0,"BG05A2")

    $ targetmailid = cml.setdefault("RM_SUZ_SEND_RUK01","")

    $ LR_RM_CHANCE=1
    if phonemailring!= "":
        play se phonemailring
    if persistent.skipmail==False:
        $ renpy.choice_for_skipping()
    if targetmailid != "":
        $ RcvMail(targetmailid)
        $ targetmailid=""


    call CHECK_RM_RECEIVE

    $ gd["RCVmailData"][gc["ScriptMacros"]["RM_SUZ_RECV_RUK02_01"]]["late"]=True
    $ lml.append(gc["ScriptMacros"]["RM_SUZ_RECV_RUK02_01"])


    play bgm "BGM26"
    show screen phonebtn
    show screen phoneSD1
    "午后。"

    hide lh8 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA01"),"True","lh/OKA_ASA01a~ipad.png") at center as lh8 zorder (10-8) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    "冈部伦太郎突然出现。"
    $ stopvoc("OKA")
    play OKA "SUZ01A_OKA0000"
    $ current_voice = "voice/SUZ01A_OKA0000.ogg"
    "伦太郎" "「……早上好，打工战士」"
    "冈部伦太郎打算装冷静，但是我觉得他看起来有些奇怪。"
    $ stopvoc("SUZ")
    play SUZ "SUZ01A_SUZ0112"
    $ current_voice = "voice/SUZ01A_SUZ0112.ogg"
    "铃羽" "「早啊」"
    "但是他一直这样和我打招呼。"
    $ stopvoc("OKA")
    play OKA "SUZ01A_OKA0001"
    $ current_voice = "voice/SUZ01A_OKA0001.ogg"
    "伦太郎" "「偷懒中吗？」"
    $ stopvoc("SUZ")
    play SUZ "SUZ01A_SUZ0113"
    $ current_voice = "voice/SUZ01A_SUZ0113.ogg"
    "铃羽" "「现在，又没有顾客」"
    window hide





    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ3')",DynamicDisplayable(mouthanime,"SUZ_DMA01"),"True","lh/SUZ_DMA01a~ipad.png") at left_t as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh7 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ2')",DynamicDisplayable(mouthanime,"SUZ_BMB04"),"True","lh/SUZ_BMB04a~ipad.png") at right_t as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    "虽然没有顾客，但是还有两个我在这里。"
    $ stopvoc("SUZ3")
    play SUZ3 "SUZ01A_SUZ0114"
    $ current_voice="voice/SUZ01A_SUZ0114.ogg"
    "铃羽ω" "「这个穿白衣的人，难道是冈伦大叔？」"
    $ stopvoc("SUZ2")
    play SUZ2 "SUZ01A_SUZ0115"
    $ current_voice="voice/SUZ01A_SUZ0115.ogg"
    "铃羽β" "「大概，是这么回事吧」"
    "说起来她们好像认识冈部伦太郎的样子。"
    window hide
    hide lh6 
    hide lh7 




    "但是冈部伦太郎没有办法看见他们两人，于是我装出往常的样子。"
    $ stopvoc("SUZ")
    play SUZ "SUZ01A_SUZ0116"
    $ current_voice = "voice/SUZ01A_SUZ0116.ogg"
    "铃羽" "「而且，昨夜一直闹到半夜」"
    $ stopvoc("SUZ")
    play SUZ "SUZ01A_SUZ0117"
    $ current_voice = "voice/SUZ01A_SUZ0117.ogg"
    "铃羽" "「你很困吧」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA04"),"True","lh/OKA_ASA04a~ipad.png") as lh8 zorder (10-8) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "SUZ01A_OKA0002"
    $ current_voice = "voice/SUZ01A_OKA0002.ogg"
    "伦太郎" "「闹到半夜……？　谁啊？」"

    stop bgm 
    "但是冈部伦太郎不是普通的人。"
    "感觉似乎前言不接后语。"
    play bgm "BGM23"
    $ stopvoc("SUZ")
    play SUZ "SUZ01A_SUZ0118"
    $ current_voice = "voice/SUZ01A_SUZ0118.ogg"
    "铃羽" "「冈部伦太郎你，昨天喝酒了吗？」"
    $ stopvoc("SUZ")
    play SUZ "SUZ01A_SUZ0119"
    $ current_voice = "voice/SUZ01A_SUZ0119.ogg"
    "铃羽" "「喝醉了吧。身为未成年人这样可不行哦」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA01"),"True","lh/OKA_ASA01a~ipad.png") as lh8 zorder (10-8) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "SUZ01A_OKA0003"
    $ current_voice = "voice/SUZ01A_OKA0003.ogg"
    "伦太郎" "「我们昨天晚上，因为你没能见到父亲，所以打算将你作为实验对象，举行了“最后的晚餐”。是这样吧？」"
    $ stopvoc("SUZ")
    play SUZ "SUZ01A_SUZ0120"
    $ current_voice = "voice/SUZ01A_SUZ0120.ogg"
    "铃羽" "「哈哈哈。没错没错。你昨天也是这么说的」"
    $ stopvoc("SUZ")
    play SUZ "SUZ01A_SUZ0121"
    $ current_voice = "voice/SUZ01A_SUZ0121.ogg"
    "铃羽" "「谢谢你们昨天为了我特意这么做」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA04"),"True","lh/OKA_ASA04a~ipad.png") as lh8 zorder (10-8) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "SUZ01A_OKA0004"
    $ current_voice = "voice/SUZ01A_OKA0004.ogg"
    "伦太郎" "「……虽然已经记不得细节了，我究竟是怎样将你拉进来的？」"
    $ stopvoc("SUZ")
    play SUZ "SUZ01A_SUZ0122"
    $ current_voice = "voice/SUZ01A_SUZ0122.ogg"
    "铃羽" "「难道，你昨天真的喝酒了？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA01"),"True","lh/OKA_ASA01a~ipad.png") as lh8 zorder (10-8) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "SUZ01A_OKA0005"
    $ current_voice = "voice/SUZ01A_OKA0005.ogg"
    "伦太郎" "「别问了，快点告诉我」"
    $ stopvoc("SUZ")
    play SUZ "SUZ01A_SUZ0123"
    $ current_voice = "voice/SUZ01A_SUZ0123.ogg"
    "铃羽" "「那个，我从时间机器线下会会场回来后——」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA04"),"True","lh/OKA_ASA04a~ipad.png") as lh8 zorder (10-8) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "SUZ01A_OKA0006"
    $ current_voice = "voice/SUZ01A_OKA0006.ogg"
    "伦太郎" "「等，等等。时间机器线下！？」"
    $ stopvoc("SUZ")
    play SUZ "SUZ01A_SUZ0124"
    $ current_voice = "voice/SUZ01A_SUZ0124.ogg"
    "铃羽" "「嗯」"
    $ stopvoc("OKA")
    play OKA "SUZ01A_OKA0007"
    $ current_voice = "voice/SUZ01A_OKA0007.ogg"
    "伦太郎" "「那里是你父亲有可能会出现的场所吗」"
    $ stopvoc("SUZ")
    play SUZ "SUZ01A_SUZ0125"
    $ current_voice = "voice/SUZ01A_SUZ0125.ogg"
    "铃羽" "「这件事，昨天说过了么」"
    "的确，是说过了。"
    "应该说过了。"
    "果然今天的冈部伦太郎有什么地方不对劲。"
    $ stopvoc("OKA")
    play OKA "SUZ01A_OKA0008"
    $ current_voice = "voice/SUZ01A_OKA0008.ogg"
    "伦太郎" "「然后，回来后怎样了？」"
    $ stopvoc("SUZ")
    play SUZ "SUZ01A_SUZ0126"
    $ current_voice = "voice/SUZ01A_SUZ0126.ogg"
    "铃羽" "「你，桥田至，还有椎名真由理突然出现──」"
    $ stopvoc("SUZ")
    play SUZ "SUZ01A_SUZ0127"
    $ current_voice = "voice/SUZ01A_SUZ0127.ogg"
    "铃羽" "「将我带到研究所。祝贺祝贺」"
    "我后来半夜是离开了，接下来的事情就是秘密了。"
    "虽然离开是有理由的，但是这话不能对冈部伦太郎说。"

    stop bgm 
    $ stopvoc("SUZ")
    play SUZ "SUZ01A_SUZ0128"
    $ current_voice = "voice/SUZ01A_SUZ0128.ogg"
    "铃羽" "「昨天真是愉快啊」"
    $ stopvoc("SUZ")
    play SUZ "SUZ01A_SUZ0129"
    $ current_voice = "voice/SUZ01A_SUZ0129.ogg"
    "铃羽" "「如果没有牧濑红莉栖的话，会更愉快。她做出来的苹果派，简直是杀人凶器」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA01"),"True","lh/OKA_ASA01a~ipad.png") as lh8 zorder (10-8) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "SUZ01A_OKA0009"
    $ current_voice = "voice/SUZ01A_OKA0009.ogg"
    "伦太郎" "「…………」"
    play bgm "BGM13"
    $ stopvoc("SUZ")
    play SUZ "SUZ01A_SUZ0130"
    $ current_voice = "voice/SUZ01A_SUZ0130.ogg"
    "铃羽" "「但是，漆原琉华做的咖喱简直是极品」"
    $ stopvoc("SUZ")
    play SUZ "SUZ01A_SUZ0131"
    $ current_voice = "voice/SUZ01A_SUZ0131.ogg"
    "铃羽" "「你们的实验室，那个，是不是像活动部一样的地方？那种地方，感觉很不错啊」"
    $ stopvoc("SUZ")
    play SUZ "SUZ01A_SUZ0132"
    $ current_voice = "voice/SUZ01A_SUZ0132.ogg"
    "铃羽" "「大家感情很好，总是很开心……」"
    $ stopvoc("SUZ")
    play SUZ "SUZ01A_SUZ0133"
    $ current_voice = "voice/SUZ01A_SUZ0133.ogg"
    "铃羽" "「那样愉快的时光，是我自出生以来第一次体验到」"
    "这真的是我真正的感受。"
    "在我出生的时代，这是无法想像的事情。"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_RESISTANCE"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_RESISTANCE"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_RESISTANCE"])
    "也不是没有被称为同伴的人，但是他们是{color=#f00}反抗军{/color}的同志。"
    "是一起战斗的同伴。是战友。"
    $ stopvoc("OKA")
    play OKA "SUZ01A_OKA0010"
    $ current_voice = "voice/SUZ01A_OKA0010.ogg"
    "伦太郎" "「打工战士啊。我按照约定，将你变成实验对象了哦」"
    $ stopvoc("SUZ")
    play SUZ "SUZ01A_SUZ0134"
    $ current_voice = "voice/SUZ01A_SUZ0134.ogg"
    "铃羽" "「……但是，我之前也说过，我不知道我父亲的邮箱地址」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA05"),"True","lh/OKA_ASA05a~ipad.png") as lh8 zorder (10-8) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "SUZ01A_OKA0011"
    $ current_voice = "voice/SUZ01A_OKA0011.ogg"
    "伦太郎" "「那么实验就延期到你知道的时候吧」"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_DENWA_RANGE"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_DENWA_RANGE"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_DENWA_RANGE"])
    $ stopvoc("OKA")
    play OKA "SUZ01A_OKA0012"
    $ current_voice = "voice/SUZ01A_OKA0012.ogg"
    "伦太郎" "「顺带说一下，实验用的{color=#f00}电话微波炉（暂）{/color}是我们实验室最高的机密事项，为了不对外泄露情报，就让你也成为Ｌａｂｍｅｍ吧」"
    $ stopvoc("SUZ")
    play SUZ "SUZ01A_SUZ0135"
    $ current_voice = "voice/SUZ01A_SUZ0135.ogg"
    "铃羽" "「Ｌａｂｍｅｍ？」"
    $ stopvoc("OKA")
    play OKA "SUZ01A_OKA0013"
    $ current_voice = "voice/SUZ01A_OKA0013.ogg"
    "伦太郎" "「是Ｌａｂｏｒａｔｏｒｙ　ｍｅｍｂｅｒ的简称。被赋予研究所成员的身份人，也就是研究所的同伴」"
    $ stopvoc("SUZ")
    play SUZ "SUZ01A_SUZ0136"
    $ current_voice = "voice/SUZ01A_SUZ0136.ogg"
    "铃羽" "「……这样好吗？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASB05"),"True","lh/OKA_ASB05a~ipad.png") as lh8 zorder (10-8) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "SUZ01A_OKA0014"
    $ current_voice = "voice/SUZ01A_OKA0014.ogg"
    "伦太郎" "「不愿意也要当。你从今天开始，就是Ｌａｂｍｅｍ　００８！」"
    "听到冈部伦太郎的话，我脚一软蹲了下去。"
    "因为太高兴了，而变得无力。"
    "因为快要哭泣而导致鼻子有些不舒服。"
    "所以我皱皱脸吸了吸鼻子。"
    "连自己都察觉到自己在笑。"
    $ stopvoc("SUZ")
    play SUZ "SUZ01A_SUZ0137"
    $ current_voice = "voice/SUZ01A_SUZ0137.ogg"
    "铃羽" "「那就没办法了，让我成为你们的实验品吧」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA04"),"True","lh/OKA_ASA04a~ipad.png") as lh8 zorder (10-8) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "SUZ01A_OKA0015"
    $ current_voice = "voice/SUZ01A_OKA0015.ogg"
    "伦太郎" "「……你，还不急着回去吧？」"
    $ stopvoc("SUZ")
    play SUZ "SUZ01A_SUZ0138"
    $ current_voice = "voice/SUZ01A_SUZ0138.ogg"
    "铃羽" "「嗯。我还想再努力寻找父亲一下」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA05"),"True","lh/OKA_ASA05a~ipad.png") as lh8 zorder (10-8) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "SUZ01A_OKA0016"
    $ current_voice = "voice/SUZ01A_OKA0016.ogg"
    "伦太郎" "「你从今天开始就是实验员了。有什么事情的话，我们也会帮忙的」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA01"),"True","lh/OKA_ASA01a~ipad.png") as lh8 zorder (10-8) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "SUZ01A_OKA0017"
    $ current_voice = "voice/SUZ01A_OKA0017.ogg"
    "伦太郎" "「顺带问一下，关于你父亲，你有没有什么线索？」"
    "有些踌躇。"
    "接着，我站了起来，面向冈部伦太郎。"
    $ stopvoc("SUZ")
    play SUZ "SUZ01A_SUZ0139"
    $ current_voice = "voice/SUZ01A_SUZ0139.ogg"
    "铃羽" "「我的父亲，自称为“提托”」"
    "这是让冈部伦太郎知道我真实身份的危险发言。"
    "之所以敢说出来，是因为冈部伦太郎说我是同伴。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASB04"),"True","lh/OKA_ASB04a~ipad.png") as lh8 zorder (10-8) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "SUZ01A_OKA0018"
    $ current_voice = "voice/SUZ01A_OKA0018.ogg"
    "伦太郎" "「等，提托，是那个提托吗！？」"
    "冈部伦太郎的反应正是我想像中的。"
    $ stopvoc("SUZ")
    play SUZ "SUZ01A_SUZ0140"
    $ current_voice = "voice/SUZ01A_SUZ0140.ogg"
    "铃羽" "「你知道？　可是现在，他应该在使用其他的代号……」"
    "接着冈部伦太郎取出手机查找起了什么。"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_JOHN"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_JOHN"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_JOHN"])
    $ stopvoc("OKA")
    play OKA "SUZ01A_OKA0019"
    $ current_voice = "voice/SUZ01A_OKA0019.ogg"
    "伦太郎" "「你看！是　{color=#f00}约翰·提托{/color}这个人写的吧！？」"
    "我死死地盯着屏幕。"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_ATTCHANNEL"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_ATTCHANNEL"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_ATTCHANNEL"])

    $ stopvoc("SUZ")
    play SUZ "SUZ01A_SUZ0141"
    $ current_voice = "voice/SUZ01A_SUZ0141.ogg"
    "铃羽" "「啊啊，这个，是真的呢……」"
    "但是那里没有我想要的父亲的情报。"
    "看一眼就能明白没有任何新的情报。"
    "那里有的只是我见过的文章而已。"
    $ stopvoc("OKA")
    play OKA "SUZ01A_OKA0021"
    $ current_voice = "voice/SUZ01A_OKA0021.ogg"
    "伦太郎" "「……那么，喂。你这淡定的表情是怎么回事」"
    $ stopvoc("SUZ")
    play SUZ "SUZ01A_SUZ0142"
    $ current_voice = "voice/SUZ01A_SUZ0142.ogg"
    "铃羽" "「没有……。不是这个人」"
    $ stopvoc("OKA")
    play OKA "SUZ01A_OKA0022"
    $ current_voice = "voice/SUZ01A_OKA0022.ogg"
    "伦太郎" "「你怎么知道？　你不是刚刚才说你的父亲自称为提托！？」"
    $ stopvoc("SUZ")
    play SUZ "SUZ01A_SUZ0143"
    $ current_voice = "voice/SUZ01A_SUZ0143.ogg"
    "铃羽" "「我就是知道。总之，这个提托不是我父亲」"
    "虽然冈部伦太郎说不是，但是我知道。"
    "因为，这里写着的约翰·提托是不存在的人。"
    $ stopvoc("SUZ")
    play SUZ "SUZ01A_SUZ0144"
    $ current_voice = "voice/SUZ01A_SUZ0144.ogg"
    "铃羽" "「不是约翰。我父亲使用的名字是——」"
    "没有办法说出口的我，将别的证据摆在了冈部伦太郎的面前。"
    $ stopvoc("SUZ")
    play SUZ "SUZ01A_SUZ0145"
    $ current_voice = "voice/SUZ01A_SUZ0145.ogg"
    "铃羽" "「是巴雷尔·提托」"
    hide screen phoneSD1
    window hide

    stop bgm 



    $ loadBG(0,"BG04A1")

    play bgm "BGM26"
    show screen phonebtn
    show screen phoneSD1
    "冈部伦太郎正在兴头上的时候突然被浇了一盆冷水，低落地回２楼上去了。"

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ3')",DynamicDisplayable(mouthanime,"SUZ_DMA03"),"True","lh/SUZ_DMA03a~ipad.png") at left as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh7 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ2')",DynamicDisplayable(mouthanime,"SUZ_BMB04"),"True","lh/SUZ_BMB04a~ipad.png") at right as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ2")
    play SUZ2 "SUZ01A_SUZ0146"
    $ current_voice="voice/SUZ01A_SUZ0146.ogg"
    "铃羽β" "「如果跟冈伦叔叔说出来就好了」"
    $ stopvoc("SUZ")
    play SUZ "SUZ01A_SUZ0147"
    $ current_voice = "voice/SUZ01A_SUZ0147.ogg"
    "铃羽" "「怎么β跟ω，都称冈部伦太郎为冈伦叔叔呢？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ3')",DynamicDisplayable(mouthanime,"SUZ_DMA05"),"True","lh/SUZ_DMA05a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ3")
    play SUZ3 "SUZ01A_SUZ0148"
    $ current_voice="voice/SUZ01A_SUZ0148.ogg"
    "铃羽ω" "「不是ω，我是铃羽」"
    "ω似乎怎样都不愿意让步。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ2')",DynamicDisplayable(mouthanime,"SUZ_BMA01"),"True","lh/SUZ_BMA01a~ipad.png") as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ2")
    play SUZ2 "SUZ01A_SUZ0149"
    $ current_voice="voice/SUZ01A_SUZ0149.ogg"
    "铃羽β" "「冈伦叔叔就是冈伦叔叔」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ3')",DynamicDisplayable(mouthanime,"SUZ_DMA02"),"True","lh/SUZ_DMA02a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ3")
    play SUZ3 "SUZ01A_SUZ0150"
    $ current_voice="voice/SUZ01A_SUZ0150.ogg"
    "铃羽ω" "「冈伦叔叔就是冈伦叔叔哦」"
    $ stopvoc("SUZ")
    play SUZ "SUZ01A_SUZ0151"
    $ current_voice = "voice/SUZ01A_SUZ0151.ogg"
    "铃羽" "「可是他叫冈部伦太郎啊」"
    "大概是因为成长的环境不同吧。"
    "也许在他们两人的世界线中，冈部伦太郎没有在２０２５年死去，而是一直活着。"
    $ stopvoc("SUZ")
    play SUZ "SUZ01A_SUZ0152"
    $ current_voice = "voice/SUZ01A_SUZ0152.ogg"
    "铃羽" "「那，如果我跟冈部伦太郎说了又会怎样？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ3')",DynamicDisplayable(mouthanime,"SUZ_DMA01"),"True","lh/SUZ_DMA01a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ2')",DynamicDisplayable(mouthanime,"SUZ_BMB04"),"True","lh/SUZ_BMB04a~ipad.png") as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ2")
    play SUZ2 "SUZ01A_SUZ0153"
    $ current_voice="voice/SUZ01A_SUZ0153.ogg"
    "铃羽β" "「这个我无法做出判断。但是——」"
    $ stopvoc("SUZ2")
    play SUZ2 "SUZ01A_SUZ0154"
    $ current_voice="voice/SUZ01A_SUZ0154.ogg"
    "铃羽β" "「你把他当成了同伴。还是我猜错了？」"
    $ stopvoc("SUZ")
    play SUZ "SUZ01A_SUZ0155"
    $ current_voice = "voice/SUZ01A_SUZ0155.ogg"
    "铃羽" "「……你猜的没有错」"
    "但是就算被当成同伴也有没办法说出口的事情。"
    "我以约翰·提托的名义向冈部伦太郎发了很多次短信。"
    "还参加了＠ｃｈ的讨论。"
    "但是我一直向冈部伦太郎隐瞒我是约翰·提托的事实。"
    "刚刚也没有说出口。"
    "干涉过去太多并不好。"
    "因为我来到了２０１０年，可能会导致世界线的变动。"
    "而且──"
    "除此之外还有──"
    "我很害怕冈部伦太郎他们看我的目光会发生改变──"

    hide screen phoneSD1
    window hide

    stop bgm
    scene expression Solid("000000")  with fade





    return







    return







    return
