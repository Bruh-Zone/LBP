label SGFD2_KYO08A:
    python:
        
        RcvMail(26)
        ReadMail(26)
        RcvMail(25)
        ReadMail(25)
        RcvMail(24)
        ReadMail(24)
    window hide


    $ loadBG(0,"BG03A4")




    hide screen phonebtn


    $ date="8/13"
    hide screen phonebtn
    hide screen phoneSD1

    "视线摇晃着……大脑摇晃着……"
    "就算感受着一如既往的眩晕，我也很快分辨出了我的所在之处。"
    "未来道具研究所——Ｌａｂ的开发室。"
    "在房间的一角是真由理的身影。"
    "抱着膝盖坐在那边，耳朵里塞着耳塞。"
    "好像是在听着随身听里的音乐的样子。"
    "真由理……真由理还在……"
    "对此感到十分安心的同时，我的头里开始考虑别的事情。"
    "真由理现在，正在用随身听听着音乐。"
    "也就是说……？"
    "恐怕这里是『第３世界线』吧。"
    "“Ｒｅａｄｉｎｇ・Ｓｔｅｉｎｅｒ”的发动和手机里的邮件都说明了这一点。"
    "『绝对外出禁止』"
    "『Ｌａｂ安全待机』"
    "『和黑万十战斗』"
    "所以我——"
    show screen phonebtn
    show screen phoneSD1
    play bgm "BGM12"
    "一边赶紧减轻自己的头晕，一边赶紧开始行动。"
    window hide


    $ loadBG(2,"BG01E")



    "我跑进了谈话室，首先确认了一下窗户的外面。"
    hide screen phoneSD1
    window hide
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_KYO002A"]]["Check"]=True


    $ loadBG(2,"EV_KYO002A")



    hide screen phonebtn
    "虽然黑色涂装的ＳＵＶ还停在那里，但是黑斗篷的身影已经不见了。"
    "当然了。那群家伙现在……"
    window hide


    $ loadBG(2,"BG01E")



    show screen phonebtn
    show screen phoneSD1
    play se "SGSE022"

    "正在玄关的另一侧吧……"
    "咕……我吞了口口水，走到了门前。"
    "为了确认情况，我颤颤巍巍地从猫眼里看了一下外面。"
    stop se
    hide screen phoneSD1
    window hide


    $ loadBG(2,"BG_BLACK")



    hide screen phonebtn
    "在那里果然是那群家伙的身影。"
    "猫眼的效果使得他们的样子令人不快地扭曲着。"
    "虽然就算没有猫眼也已经很诡异了，但是这样一来使得怪异程度更上一层。"
    window hide


    $ loadBG(2,"BG01E")



    show screen phonebtn
    show screen phoneSD1
    "没有多想，我后退了一步。"
    "将手放在胸口，调整呼吸。"
    window hide



    $ stopvoc("FEI")
    play FEI "KYO08A_FEI0000"
    $ current_voice = "voice/KYO08A_FEI0000.ogg"
    "菲利斯" "战斗吧，凶真！　当缩头乌龟是不行的喵！"
    window hide



    "突然，菲利斯的声音又回响在我的耳边。"
    "是啊，不战斗的话……！"
    "你到底在害怕什么呢，凤凰院凶真哦！"
    "这样下去的话，被敌人破门而入几乎是铁板钉钉的事了。"
    "那样的话只能这边先下手为强了！"
    $ stopvoc("OKA")
    play OKA "KYO08A_OKA0000"
    $ current_voice = "voice/KYO08A_OKA0000.ogg"
    "伦太郎" "「好的，要上了……！」"
    play se "SGSE111"

    "我下定了决心，打开了门锁。"
    "然后缓缓地握着门把手推了出去。"
    "在这个状态下——"
    $ stopvoc("OKA")
    play OKA "KYO08A_OKA0001"
    $ current_voice = "voice/KYO08A_OKA0001.ogg"
    "伦太郎" "「啊哒哒哒────！！！」"
    hide screen phoneSD1
    window hide
    play se "SGSE058"



    $ loadBG(2,"BG_BLACK")



    hide screen phonebtn
    "我一脚踹开了门。"
    $ stopvoc("Y20")
    play KUR "KYO08A_Y200000"
    $ current_voice = "voice/KYO08A_Y200000.ogg"
    "黑斗篷四号" "「咕哇！」"
    $ stopvoc("Y21")
    play KUR "KYO08A_Y210000"
    $ current_voice = "voice/KYO08A_Y210000.ogg"
    "黑斗篷五号" "「咕呃！」"
    "看了看脚尖。"
    "有两个穿着黑斗篷的男子，一个捧着肚子，一个捂着鼻子倒在地上。"
    "好奇怪啊……"
    "在我的脑内模拟中，刚才那一击应该可以将门口的５个黑斗篷全数击倒，让他们狼狈地从楼梯上滚下去才对。"
    "但是实际上只打倒了两人……"
    "剩下三个人无伤……"
    window hide


    $ loadBG(0,"BG01E")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='KUR')",DynamicDisplayable(mouthanime,"MAN_ASA01"),"True","lh/MAN_ASA01a~ipad.png") at left_t as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='KUR')",DynamicDisplayable(mouthanime,"MAN_ASA01"),"True","lh/MAN_ASA01a~ipad.png") at right_t as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    hide lh7 
    show expression ConditionSwitch("renpy.music.get_playing(channel='KUR')",DynamicDisplayable(mouthanime,"MAN_ASB01"),"True","lh/MAN_ASB01a~ipad.png") at center as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)





    hide screen phonebtn
    show screen phoneSD1
    "麻烦了……"
    "冷汗直流。"
    "为什么一片沉默……"
    "虽然剩下三人面无表情，无法判断到底是神额意思，但是好像因为受到我的奇袭而倍感狼狈。"
    "那样的话就立刻追击——！"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_SUBWOOFER"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_SUBWOOFER"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_SUBWOOFER"])
    "这么想着的时候，左边的黑斗篷发出了{color=#f00}低音炮{/color}那样的怒鸣。"
    $ stopvoc("Y22")
    play KUR "KYO08A_Y220000"
    $ current_voice = "voice/KYO08A_Y220000.ogg"
    "黑斗篷一号" "「啊哇哇哇哇哇————你都干了些什么呀，呆子——————！！！」"
    "诶……？　关西腔？　广岛腔？"
    "虽然不太清楚，但是这一声叫得让我毛骨悚然倒是真的。"
    "果然这群人是什么团体的一员吧。"
    "（在这后面，发出这声悲鸣的黑斗篷称为『一号』，在右边的黑斗篷称为『二号』，在『二号』右手边的称为『三号』）"
    "（顺便一提倒在地上的是『四号』和『五号』）"
    hide screen phoneSD1
    window hide
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_KYO006A"]]["Check"]=True


    $ loadBG(2,"EV_KYO006A")



    "虽然一瞬间有些迟疑，但这是这样的话，我还没有输。"
    "如果我是伞蜥的话我应该会张开脖子上的膜来威吓他们吧，但很不巧我不是伞蜥所以脖子也没有那种东西。"
    window hide
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_KYO006B"]]["Check"]=True


    $ loadBG(2,"EV_KYO006B")



    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_MANTIS"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_MANTIS"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_MANTIS"])
    "于是我摆出了螳螂拳第十八式。"
    "并大吼道。"
    $ stopvoc("OKA")
    play OKA "KYO08A_OKA0002"
    $ current_voice = "voice/KYO08A_OKA0002.ogg"
    "伦太郎" "「啊喝喝喝喝——————！！！」"
    $ stopvoc("Y22")
    play KUR "KYO08A_Y220001"
    $ current_voice = "voice/KYO08A_Y220001.ogg"
    "黑斗篷一号" "「…………」"
    $ stopvoc("Y23")
    play KUR "KYO08A_Y230000"
    $ current_voice = "voice/KYO08A_Y230000.ogg"
    "黑斗篷二号" "「…………」"
    $ stopvoc("Y15")
    play KUR "KYO08A_Y150000"
    $ current_voice = "voice/KYO08A_Y150000.ogg"
    "新一" "「…………」"
    $ stopvoc("OKA")
    play OKA "KYO08A_OKA0003"
    $ current_voice = "voice/KYO08A_OKA0003.ogg"
    "伦太郎" "「好，看来有效果看来有效果」"
    $ stopvoc("Y22")
    play KUR "KYO08A_Y220002"
    $ current_voice = "voice/KYO08A_Y220002.ogg"
    "黑斗篷一号" "「有毛线效果啊！」"
    window hide
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_KYO006C"]]["Check"]=True


    $ loadBG(2,"EV_KYO006C")



    "那样的话就用第十七式——“鹤翼”。"
    "姿势像那釧路自然公园里优雅展翅的丹顶鹤一样。"
    $ stopvoc("OKA")
    play OKA "KYO08A_OKA0004"
    $ current_voice = "voice/KYO08A_OKA0004.ogg"
    "伦太郎" "「咯！」"
    $ stopvoc("Y23")
    play KUR "KYO08A_Y230001"
    $ current_voice = "voice/KYO08A_Y230001.ogg"
    "黑斗篷二号" "「…………」"
    $ stopvoc("Y15")
    play KUR "KYO08A_Y150001"
    $ current_voice = "voice/KYO08A_Y150001.ogg"
    "新一" "「…………」"
    $ stopvoc("Y22")
    play KUR "KYO08A_Y220003"
    $ current_voice = "voice/KYO08A_Y220003.ogg"
    "黑斗篷一号" "「你这家伙，是在小看我们么……？」"
    "这么说着，一号将手伸进了斗篷。"
    "好像拔出了什么。"
    window hide
    play se "SGSE326"



    $ loadBG(0,"BG_BLACK")

    "那是一把长剑——Ｌｏｎｇｓｗｏｒｄ。"
    $ stopvoc("OKA")
    play OKA "KYO08A_OKA0005"
    $ current_voice = "voice/KYO08A_OKA0005.ogg"
    "伦太郎" "「喂，喂，这可是作弊行为！」"
    $ stopvoc("Y22")
    play KUR "KYO08A_Y220004"
    $ current_voice = "voice/KYO08A_Y220004.ogg"
    "黑斗篷一号" "「吵死了！」"
    "一边大吼着，一号操着剑占了过来。"
    "我为了躲闪这一击，朝着后边跳去。"
    window hide

    $ loadBG(0,"BG01E")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='KUR')",DynamicDisplayable(mouthanime,"MAN_AMB01"),"True","lh/MAN_AMB01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='KUR')",DynamicDisplayable(mouthanime,"MAN_ASA01"),"True","lh/MAN_ASA01a~ipad.png") at right_t as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    hide lh7 
    show expression ConditionSwitch("renpy.music.get_playing(channel='KUR')",DynamicDisplayable(mouthanime,"MAN_ASA01"),"True","lh/MAN_ASA01a~ipad.png") at left_t as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)





    hide screen phonebtn
    show screen phoneSD1
    "虽然之后也试着说『等等，别冲动！』但是好像对于这个男子没有效果。"
    "渐渐地朝着房间的中央移动了。"
    "而且二号和三号也跟着进入了室内……"
    hide screen phonebtn
    $ stopvoc("Y22")
    play KUR "KYO08A_Y220005"
    $ current_voice = "voice/KYO08A_Y220005.ogg"
    "黑斗篷一号" "「椎名在哪里……？」"
    "一号大叫着向我提问。"
    "我这么回答了。"
    $ stopvoc("OKA")
    play OKA "KYO08A_OKA0006"
    $ current_voice = "voice/KYO08A_OKA0006.ogg"
    "伦太郎" "「椎名？　那是谁啊？」"
    $ stopvoc("Y22")
    play KUR "KYO08A_Y220006"
    $ current_voice = "voice/KYO08A_Y220006.ogg"
    "黑斗篷一号" "「别装傻。椎名真由理啊」"
    $ stopvoc("OKA")
    play OKA "KYO08A_OKA0008"
    $ current_voice = "voice/KYO08A_OKA0008.ogg"
    "伦太郎" "「不知道啊……。真由理，那是谁啊？」"
    $ stopvoc("Y22")
    play KUR "KYO08A_Y220008"
    $ current_voice = "voice/KYO08A_Y220008.ogg"
    "黑斗篷一号" "「说了叫你不要装傻了」"
    "这个时候——"
    window hide


    $ loadBG(2,"BG02E2")



    "二号的视线投向了开发室的方向。"
    "麻烦了……"
    "是察觉到了我的内心吗，一号的面具里的眼睛眯了起来，慢慢地说道。"
    window hide



    $ stopvoc("Y22")
    play KUR "KYO08A_Y220009"
    $ current_voice = "voice/KYO08A_Y220009.ogg"
    "黑斗篷一号" "「是在那儿吧？」"
    "他向前踏出一步……"
    "该怎么办……！　该怎么办才好……！"
    "这样的话真由理就要被带走了！"
    window hide



    $ stopvoc("FEI")
    play FEI "KYO08A_FEI0001"
    $ current_voice = "voice/KYO08A_FEI0001.ogg"
    "菲利斯" "战斗吧，凶真！　当缩头乌龟是不行的喵！"
    window hide



    "再次响起的菲利斯的声音……"
    "但是究竟该怎么战斗！？　到底该怎么做才好！？"
    "对手还握着长剑呢……！"
    "如果要和剑战斗的话，我也必须用剑才行。"
    "但是在Ｌａｂ里像剑一样的东西……"
    window hide
    $ loadBG(0,"IBG027A",png=True)

    "…………"
    "有的。"
    window hide

    hide background-png  with dissolve
    "一号朝着开发室走去，已经近在咫尺了。"
    "就差要拉开关着的窗帘了。"
    "没有时间再让我仔细思考了。"
    window hide


    $ loadBG(2,"BG02E2")



    hide screen phonebtn
    show screen phoneSD1
    $ loadBG(0,"IBG027A",png=True)

    "我拔腿朝着纸板箱跑去，从那里面拔出插着的一把剑。"
    "将它举起，大叫道。"
    hide screen phoneSD1
    window hide
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_KYO007A"]]["Check"]=True

    $ loadBG(0,"EV_KYO007A")






    hide background-png  with dissolve

    hide screen phonebtn
    $ stopvoc("OKA")
    play OKA "KYO08A_OKA0009"
    $ current_voice = "voice/KYO08A_OKA0009.ogg"
    "伦太郎" "「唔哈哈哈！　让我拿起这把剑真是你的疏忽啊，一号！」"
    $ stopvoc("Y22")
    play KUR "KYO08A_Y220010"
    $ current_voice = "voice/KYO08A_Y220010.ogg"
    "黑斗篷一号" "「啊？　一号是谁啊……」"
    $ stopvoc("OKA")
    play OKA "KYO08A_OKA0010"
    $ current_voice = "voice/KYO08A_OKA0010.ogg"
    "伦太郎" "「就让你领教一下清心斩魔流剑法的极意！」"
    $ stopvoc("OKA")
    play OKA "KYO08A_OKA0011"
    $ current_voice = "voice/KYO08A_OKA0011.ogg"
    "伦太郎" "「上了哦，唔啊啊啊────！！！」"
    window hide








    $ loadBG(2,"BG01E")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='KUR')",DynamicDisplayable(mouthanime,"MAN_BSA01"),"True","lh/MAN_BSA01a~ipad.png") at left_t as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='KUR')",DynamicDisplayable(mouthanime,"MAN_ASA01"),"True","lh/MAN_ASA01a~ipad.png") at right_t as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh7 
    show expression ConditionSwitch("renpy.music.get_playing(channel='KUR')",DynamicDisplayable(mouthanime,"MAN_ASB01"),"True","lh/MAN_ASB01a~ipad.png") at center as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)






    show screen phoneSD1
    hide screen phonebtn
    $ stopvoc("OKA")
    play OKA "KYO08A_OKA0012"
    $ current_voice = "voice/KYO08A_OKA0012.ogg"
    "伦太郎" "「…………」"
    "说不出话来。结果没能让他领教到。"
    "虽然我确实挥着剑斩向了一号，但是被他举起的长剑挡了一下，于是就散架了。"
    "这也是理所当然的……要问为什么的话因为我拿着的是……"
    window hide
    $ loadBG(0,"IBG027A",png=True)

    "未来道具６号机『荧光棒·Ｓａｂｅｒ』。"
    "连自己也不觉得这也的东西能够来一发太刀打。"
    "肯定是一瞬间就崩了吧。"
    "我下意识地取出了这个道具。"
    window hide





    hide background-png  with dissolve
    "万事休矣……山穷水尽……"
    "已经没有反击的办法了……"
    "全身开始冒冷汗……"
    "另一方面，一号发现了手中的红色液体。"
    $ stopvoc("Y22")
    play KUR "KYO08A_Y220011"
    $ current_voice = "voice/KYO08A_Y220011.ogg"
    "黑斗篷一号" "「喂，喂这是什么啊？难道说我，哪里受伤了么？」"
    $ stopvoc("Y23")
    play KUR "KYO08A_Y230002"
    $ current_voice = "voice/KYO08A_Y230002.ogg"
    "黑斗篷二号" "「不对，看起来没事的样子啊……」"
    $ stopvoc("Y22")
    play KUR "KYO08A_Y220012"
    $ current_voice = "voice/KYO08A_Y220012.ogg"
    "黑斗篷一号" "「血迹……？」"
    $ stopvoc("Y22")
    play KUR "KYO08A_Y220013"
    $ current_voice = "voice/KYO08A_Y220013.ogg"
    "黑斗篷一号" "「喂，唔哇哇哇！这是什么啊！仔细一看斗篷上也不都是吗」"
    $ stopvoc("Y23")
    play KUR "KYO08A_Y230003"
    $ current_voice = "voice/KYO08A_Y230003.ogg"
    "黑斗篷二号" "「还有，长剑上也有啊……」"
    $ stopvoc("Y22")
    play KUR "KYO08A_Y220014"
    $ current_voice = "voice/KYO08A_Y220014.ogg"
    "黑斗篷一号" "「唔哇哇哇！　不可能啊！　这可是在『武器屋本铺』花了９万８千日元买的啊！」"
    "在『武器屋本铺』……？"
    "也就是说，这是把和给琉华子的『妖刀·五月雨』一样的，模型刀咯……"
    "仔细确认的话，确实在刀刃的部分是圆的。"
    "还有也明白了另一点。"
    "『荧光棒·Ｓａｂｅｒ』的攻击并不是无效的。"
    "这些家伙的手忙脚乱简直一目了然——"
    "好像这群家伙对于斗篷被弄脏了十分厌恶。"
    "我的直觉这样告诉我。"
    "那么现在就举起反攻的大旗吧！"
    window hide


    $ loadBG(2,"BG02E2")



    hide screen phonebtn
    show screen phoneSD1



    $ loadBG(2,"IBG027A",png=True)



    "我再次冲向纸板箱，从里面取出好多『荧光棒·Ｓａｂｅｒ』。"
    "剑的顶端有个小帽。"
    "我将那小帽取了下来，然后一把把扔了出去。"
    window hide



    $ loadBG(2,"BG01E")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='KUR')",DynamicDisplayable(mouthanime,"MAN_BSA01"),"True","lh/MAN_BSA01a~ipad.png") at left_t as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='KUR')",DynamicDisplayable(mouthanime,"MAN_ASA01"),"True","lh/MAN_ASA01a~ipad.png") at right_t as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh7 
    show expression ConditionSwitch("renpy.music.get_playing(channel='KUR')",DynamicDisplayable(mouthanime,"MAN_ASB01"),"True","lh/MAN_ASB01a~ipad.png") at center as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)






    show screen phoneSD1
    hide screen phonebtn

    show expression ConditionSwitch("renpy.music.get_playing(channel='KUR')",DynamicDisplayable(mouthanime,"MAN_BSB01"),"True","lh/MAN_BSB01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    $ stopvoc("Y22")
    play KUR "KYO08A_Y220015"
    $ current_voice = "voice/KYO08A_Y220015.ogg"
    "黑斗篷一号" "「喂，住手！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='KUR')",DynamicDisplayable(mouthanime,"MAN_BSA01"),"True","lh/MAN_BSA01a~ipad.png") as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    $ stopvoc("Y23")
    play KUR "KYO08A_Y230004"
    $ current_voice = "voice/KYO08A_Y230004.ogg"
    "黑斗篷二号" "「给我住手！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='KUR')",DynamicDisplayable(mouthanime,"MAN_BSA01"),"True","lh/MAN_BSA01a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    $ stopvoc("Y15")
    play KUR "KYO08A_Y150002"
    $ current_voice = "voice/KYO08A_Y150002.ogg"
    "新一" "「拜托住手啊！」"
    hide screen phoneSD1
    window hide
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_KYO007B"]]["Check"]=True


    $ loadBG(2,"EV_KYO007D")



    hide screen phonebtn

    "当然，才没有住手的理由。"

    "作为追击，我继续投掷着溅射武器。"

    $ stopvoc("Y22")
    play KUR "KYO08A_Y220016"
    $ current_voice = "voice/KYO08A_Y220016.ogg"
    "黑斗篷一号" "「不行！　这样下去就要全身浴血了！」"

    $ stopvoc("Y23")
    play KUR "KYO08A_Y230005"
    $ current_voice = "voice/KYO08A_Y230005.ogg"
    "黑斗篷二号" "「恩！　那样的话后天的夏Ｃｏｍｉ就不能去了！」"
    "恩……？　夏Ｃｏｍｉ？"
    "但是并没有在意为什么会听到这样的词语。"

    "我继续穷追猛打，将去掉盖子的『荧光棒·Ｓａｂｅｒ』一一发射出去。"

    $ stopvoc("Y22")
    play KUR "KYO08A_Y220017"
    $ current_voice = "voice/KYO08A_Y220017.ogg"
    "黑斗篷一号" "「好的，这里就先撤退吧！」"

    $ stopvoc("Y23")
    play KUR "KYO08A_Y230006"
    $ current_voice = "voice/KYO08A_Y230006.ogg"
    "黑斗篷二号" "「了解！」"

    $ stopvoc("Y15")
    play KUR "KYO08A_Y150003"
    $ current_voice = "voice/KYO08A_Y150003.ogg"
    "新一" "「但，但是──！」"

    $ stopvoc("Y22")
    play KUR "KYO08A_Y220018"
    $ current_voice = "voice/KYO08A_Y220018.ogg"
    "黑斗篷一号" "「好了别磨蹭了！　走了！」"
    window hide


    $ loadBG(2,"BG01E4")



    hide screen phonebtn
    show screen phoneSD1
    "就这样三个人朝着玄关外面——！"
    "但是敌人的真正身份依然不明。"
    "为了不让他们逃脱，我赶紧追了上去。"

    window hide


    $ loadBG(0,"BG05E1")

    hide screen phonebtn
    show screen phoneSD1
    "冲下了楼梯，来到了显像管工房前。"
    "黑色的ＳＵＶ已经开远了。"
    "只能看着那辆车渐行渐远。"
    "在Ｌａｂ前面的四号和五号也不见了，恐怕那两人早已上车准备随时脱离了吧。"
    "可恶……！"
    "虽然想要追上去，但是如果目标是车的话就没办法了。"
    "我只能在原地一个人生闷气。"
    "这时候……"
    $ stopvoc("Y15")
    play KUR "KYO08A_Y150004"
    $ current_voice = "voice/KYO08A_Y150004.ogg"
    "新一？" "「那，那个……」"
    "我身后传来了声音。"
    "回头看去在那里站着的是……"

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='KUR')",DynamicDisplayable(mouthanime,"MAN_BSB01"),"True","lh/MAN_BSB01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    "黑斗篷——！"
    $ stopvoc("OKA")
    play OKA "KYO08A_OKA0014"
    $ current_voice = "voice/KYO08A_OKA0014.ogg"
    "伦太郎" "「你，你这家伙——！」"
    "我大喝一声，狠狠地瞪着他。"
    $ stopvoc("Y15")
    play KUR "KYO08A_Y150005"
    $ current_voice = "voice/KYO08A_Y150005.ogg"
    "新一" "「请，请稍微等等！」"
    $ stopvoc("OKA")
    play OKA "KYO08A_OKA0015"
    $ current_voice = "voice/KYO08A_OKA0015.ogg"
    "伦太郎" "「烦死了！　问答无用！」"
    "我猛地冲向了他，将他扑倒在地。"
    hide screen phoneSD1
    window hide
    play se "SGSE328"





    $ loadBG(0,"BG_BLACK")

    hide screen phonebtn
    "就这么扭在一起滚在了地上。"
    "停下来的时候我的身体位于上方。"
    window hide

    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_KYO008A"]]["Check"]=True
    $ loadBG(0,"EV_KYO008A")

    hide screen phonebtn
    "立刻就制住了他，举起右手！"
    $ stopvoc("OKA")
    play OKA "KYO08A_OKA0016"
    $ current_voice = "voice/KYO08A_OKA0016.ogg"
    "伦太郎" "「哈，反省吧，黑斗篷！」"
    $ stopvoc("Y15")
    play KUR "KYO08A_Y150006"
    $ current_voice = "voice/KYO08A_Y150006.ogg"
    "新一" "「我反省！　所以说我反省了！」"
    $ stopvoc("OKA")
    play OKA "KYO08A_OKA0017"
    $ current_voice = "voice/KYO08A_OKA0017.ogg"
    "伦太郎" "「不对，你还没有反省。就算假装反省了，但是很抱歉也已经太迟了」"
    $ stopvoc("OKA")
    play OKA "KYO08A_OKA0018"
    $ current_voice = "voice/KYO08A_OKA0018.ogg"
    "伦太郎" "「因为我的右腕的封印，已经解开了啊……。就连我自己，也无法阻止它的暴走了啊……」"
    $ stopvoc("Y15")
    play KUR "KYO08A_Y150007"
    $ current_voice = "voice/KYO08A_Y150007.ogg"
    "新一" "「噫呀呀呀！　谁来救救我～～～！」"
    $ stopvoc("OKA")
    play OKA "KYO08A_OKA0019"
    $ current_voice = "voice/KYO08A_OKA0019.ogg"
    "伦太郎" "「那么上了哦！　震动吧，我的右腕！　服从我们的契约！　用着漆黑的地狱之火──！」"
    "这么说着的时候——"

    stop bgm 
    $ stopvoc("MAY")
    play MAY "KYO08A_MAY0000"
    $ current_voice = "voice/KYO08A_MAY0000.ogg"
    "真由理" "「冈伦！！！　不可以——————！！！」"
    "从头上传来了声音。"
    window hide


    $ loadBG(2,"IBGX033")



    hide screen phonebtn
    show screen phoneSD1
    "抬头看去，真由理从Ｌａｂ的窗户里探出身来大叫着。"
    $ stopvoc("MAY")
    play MAY "KYO08A_MAY0001"
    $ current_voice = "voice/KYO08A_MAY0001.ogg"
    "真由理" "「拜托了，冈伦，住手吧！」"
    $ stopvoc("MAY")
    play MAY "KYO08A_MAY0002"
    $ current_voice = "voice/KYO08A_MAY0002.ogg"
    "真由理" "「那个人是……」"
    $ stopvoc("MAY")
    play MAY "KYO08A_MAY0003"
    $ current_voice = "voice/KYO08A_MAY0003.ogg"
    "真由理" "「那个人是，真由理的，朋友啊ー！　大概……」"
    $ stopvoc("OKA")
    play OKA "KYO08A_OKA0020"
    $ current_voice = "voice/KYO08A_OKA0020.ogg"
    "伦太郎" "「大，大概……？」"
    hide screen phoneSD1
    window hide
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_KYO008A"]]["Check"]=True


    $ loadBG(2,"EV_KYO008A")



    hide screen phonebtn
    "我粗暴地扯下他的面具。"
    "在下面的是……"
    $ stopvoc("OKA")
    play OKA "KYO08A_OKA0021"
    $ current_voice = "voice/KYO08A_OKA0021.ogg"
    "伦太郎" "「你，你是──！」"
    window hide


    $ loadBG(0,"BG21N2")




    $ loadBG(0,"IBGX033")

    hide screen phonebtn
    show screen phoneSD1
    $ stopvoc("MAY")
    play MAY "KYO08A_MAY0005"
    $ current_voice = "voice/KYO08A_MAY0005.ogg"
    "真由理" "「啊啊，果然是啊！」"
    $ stopvoc("MAY")
    play MAY "KYO08A_MAY0006"
    $ current_voice = "voice/KYO08A_MAY0006.ogg"
    "真由理" "「那个人叫做『长濑新一』！」"
    $ stopvoc("MAY")
    play MAY "KYO08A_MAY0007"
    $ current_voice = "voice/KYO08A_MAY0007.ogg"
    "真由理" "「是吹雪酱的，哥哥哦！」"

    hide screen phoneSD1
    window hide




    hide screen phonebtn
    scene expression Solid("000000")  with fade
    return
