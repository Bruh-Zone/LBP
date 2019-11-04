label SGFD2_FEI03A:
    hide screen phonebtn
    scene expression Solid("000000")  with fade

    window hide





    $ loadBG(0,"IBGX072")

    play bgm "FD2BGM09"

    $ date="8/9"
    $ day="MON"
    hide screen phonebtn
    hide screen phoneSD1


    "那一天，阿万音和我聊到很晚。"
    "是因为彼此都过着缺少父爱的日子吧。"
    "我因为１０年前的事故失去了爸爸。"
    "而阿万音从懂事起就是由母亲带大，没有见过父亲的脸。"
    "我和她比起来还算好吧。"
    "在仅有的时间里，还能留下与爸爸一起度过的美好回忆。"
    "当然，也有无法挽回的『罪』……"
    window hide

    $ stopvoc("SUZ")
    play SUZ "FEI03A_SUZ0000"
    $ current_voice = "voice/FEI03A_SUZ0000.ogg"
    "铃羽" "「难道不难受吗？」"
    $ stopvoc("FEI")
    play FEI "FEI03A_FEI0000"
    $ current_voice = "voice/FEI03A_FEI0000.ogg"
    "菲利斯" "「虽然很难受，但是大概没有大家想的那么难过……」"
    window hide
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_FEI002A"]]["Check"]=True


    $ loadBG(2,"EV_FEI002A")



    "换上睡衣，我钻到了床上。"
    "阿万音穿着我的睡衣躺在我身边。"
    "因为刚才她说她一般穿着Ｔ恤和紧身裤睡觉，所以就借给她了。"
    "但是尺寸完全不合身，手和脚的地方都很紧，臀部周围都快崩开了。"
    $ stopvoc("SUZ")
    play SUZ "FEI03A_SUZ0001"
    $ current_voice = "voice/FEI03A_SUZ0001.ogg"
    "铃羽" "「没有大家想的那么难过……是怎样的感觉？」"
    $ stopvoc("FEI")
    play FEI "FEI03A_FEI0001"
    $ current_voice = "voice/FEI03A_FEI0001.ogg"
    "菲利斯" "「心灵的创伤虽然被填上了，但是伤口上总会不时地隐隐作痛那种感觉……」"
    "我已经变回了秋叶留未穗。"
    "阿万音并不觉得不可思议，很自然地接受了。"
    "因为言语方面和黑猫时的我很像吧。"
    "但是我不敢继续问下去。"
    "不想因为问了多余的事情而被讨厌……"
    "虽然觉得自己有点神经质了，但是也有些想要避开风险的意思在里面。"
    "因此，我就这么带着心结装作若无其事的样子接着她的话题。"
    $ stopvoc("FEI")
    play FEI "FEI03A_FEI0002"
    $ current_voice = "voice/FEI03A_FEI0002.ogg"
    "菲利斯" "「当然了，１０年的时候我每天都过得很难受」"
    $ stopvoc("FEI")
    play FEI "FEI03A_FEI0003"
    $ current_voice = "voice/FEI03A_FEI0003.ogg"
    "菲利斯" "「那个时候，我应该还能做些什么。如果能用自己的双手改变命运的话，即使是现在我也想去做……我一直是这么认为的」"
    window hide
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_FEI002B"]]["Check"]=True


    $ loadBG(2,"EV_FEI002B")



    $ stopvoc("SUZ")
    play SUZ "FEI03A_SUZ0002"
    $ current_voice = "voice/FEI03A_SUZ0002.ogg"
    "铃羽" "「现在也是？」"
    $ stopvoc("FEI")
    play FEI "FEI03A_FEI0004"
    $ current_voice = "voice/FEI03A_FEI0004.ogg"
    "菲利斯" "「想要改变命运的心情到现在也是一样的。但是经过这１０年，我的心情已经整理妥当了。」"
    $ stopvoc("FEI")
    play FEI "FEI03A_FEI0005"
    $ current_voice = "voice/FEI03A_FEI0005.ogg"
    "菲利斯" "「只要不去触碰伤口就不会痛苦……。虽然伤口一直无法痊愈，但是我已经找到了应对方法……这样的感觉」"
    $ stopvoc("SUZ")
    play SUZ "FEI03A_SUZ0003"
    $ current_voice = "voice/FEI03A_SUZ0003.ogg"
    "铃羽" "「要是没有１０年前的事故的话，和爸爸的关系现在也许变得很紧张也说不定哦……没有这么想过吗？」"
    $ stopvoc("FEI")
    play FEI "FEI03A_FEI0006"
    $ current_voice = "voice/FEI03A_FEI0006.ogg"
    "菲利斯" "「阿万音对于和爸爸的相遇感到不安吗？」"
    $ stopvoc("SUZ")
    play SUZ "FEI03A_SUZ0004"
    $ current_voice = "voice/FEI03A_SUZ0004.ogg"
    "铃羽" "「因为不知道是怎样的人啊？」"
    $ stopvoc("FEI")
    play FEI "FEI03A_FEI0007"
    $ current_voice = "voice/FEI03A_FEI0007.ogg"
    "菲利斯" "「也就是说觉得说不定没见到也好？」"
    $ stopvoc("SUZ")
    play SUZ "FEI03A_SUZ0005"
    $ current_voice = "voice/FEI03A_SUZ0005.ogg"
    "铃羽" "「怎么说呢……」"
    $ stopvoc("SUZ")
    play SUZ "FEI03A_SUZ0006"
    $ current_voice = "voice/FEI03A_SUZ0006.ogg"
    "铃羽" "「既想见到又害怕见到，大概是这样的感觉吧……」"
    "阿万音对于连长相都不知道的对方感到不安。"
    "说不定在想着见不到也没关系这样的逃避的想法。"
    "但是我想见见她爸爸。"
    "不管做些什么……"
    "因为像这样在即将见到时又没能见到的难受，我很清楚。"
    "残留在我心中的根深蒂固的罪恶感的源头便是它。"
    $ stopvoc("FEI")
    play FEI "FEI03A_FEI0008"
    $ current_voice = "voice/FEI03A_FEI0008.ogg"
    "菲利斯" "「没关系。阿万音的爸爸，一定是一个温柔的好男人哦。」"
    $ stopvoc("SUZ")
    play SUZ "FEI03A_SUZ0007"
    $ current_voice = "voice/FEI03A_SUZ0007.ogg"
    "铃羽" "「是这样……吧」"
    $ stopvoc("FEI")
    play FEI "FEI03A_FEI0009"
    $ current_voice = "voice/FEI03A_FEI0009.ogg"
    "菲利斯" "「说不定是那种看了一眼就要犯花痴的男神哦♪」"
    $ stopvoc("SUZ")
    play SUZ "FEI03A_SUZ0008"
    $ current_voice = "voice/FEI03A_SUZ0008.ogg"
    "铃羽" "「啊哈哈，到底是不是呢」"
    $ stopvoc("FEI")
    play FEI "FEI03A_FEI0010"
    $ current_voice = "voice/FEI03A_FEI0010.ogg"
    "菲利斯" "「但是阿万音，我希望你不要忘记接下来我说的」"
    $ stopvoc("SUZ")
    play SUZ "FEI03A_SUZ0009"
    $ current_voice = "voice/FEI03A_SUZ0009.ogg"
    "铃羽" "「…………」"
    $ stopvoc("FEI")
    play FEI "FEI03A_FEI0011"
    $ current_voice = "voice/FEI03A_FEI0011.ogg"
    "菲利斯" "「不管你爸爸是怎样的人，我希望你一定要能够接受他。因为与家人不和，形同陌路的话，是非常不幸的」"
    $ stopvoc("SUZ")
    play SUZ "FEI03A_SUZ0010"
    $ current_voice = "voice/FEI03A_SUZ0010.ogg"
    "铃羽" "「与家人不和，形同陌路的话，是非常不幸的……」"
    window hide
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_FEI002A"]]["Check"]=True


    $ loadBG(2,"EV_FEI002A")



    $ stopvoc("SUZ")
    play SUZ "FEI03A_SUZ0011"
    $ current_voice = "voice/FEI03A_SUZ0011.ogg"
    "铃羽" "「……恩。Ｏｋａｙ－Ｄｏｋｅｙ，Ｂｏｓｓ」"
    $ stopvoc("FEI")
    play FEI "FEI03A_FEI0012"
    $ current_voice = "voice/FEI03A_FEI0012.ogg"
    "菲利斯" "「……留未穂」"
    $ stopvoc("SUZ")
    play SUZ "FEI03A_SUZ0012"
    $ current_voice = "voice/FEI03A_SUZ0012.ogg"
    "铃羽" "「……恩？」"
    $ stopvoc("FEI")
    play FEI "FEI03A_FEI0013"
    $ current_voice = "voice/FEI03A_FEI0013.ogg"
    "菲利斯" "「……秋叶留未穗。我的真名」"
    $ stopvoc("SUZ")
    play SUZ "FEI03A_SUZ0013"
    $ current_voice = "voice/FEI03A_SUZ0013.ogg"
    "铃羽" "「留未穂……吗。好可爱的名字啊」"
    $ stopvoc("FEI")
    play FEI "FEI03A_FEI0014"
    $ current_voice = "voice/FEI03A_FEI0014.ogg"
    "菲利斯" "「……害羞了喵♪」"
    $ stopvoc("SUZ")
    play SUZ "FEI03A_SUZ0014"
    $ current_voice = "voice/FEI03A_SUZ0014.ogg"
    "铃羽" "「那么，明天也请多指教了呢。……秋叶留未穗」"
    $ stopvoc("FEI")
    play FEI "FEI03A_FEI0015"
    $ current_voice = "voice/FEI03A_FEI0015.ogg"
    "菲利斯" "「恩，晚安了」"
    $ stopvoc("FEI")
    play FEI "FEI03A_FEI0016"
    $ current_voice = "voice/FEI03A_FEI0016.ogg"
    "菲利斯" "「……铃羽」"
    "对于一直和黑木住在一起的我来说，并不明白姐妹是怎样的感觉。但是，如果我真的有姐妹的话，应该是这样的感觉吧。"
    "总感觉这几天冈部有点鬼鬼祟祟的，黑木也有什么奇怪的地方。果然时间机器是ＵＦＯ，宇宙生物已经控制了秋叶原的人们了吗。"
    "这么想着，阿万音的存在就对我来说更加必要了。我心中想要和她一直在一起的愿望逐渐变强。"
    window hide
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_FEI002C"]]["Check"]=True


    $ loadBG(2,"EV_FEI002C")



    "——不想被她讨厌。"
    "——不想失去她。"
    "——想和她一直在一起。"
    "这么想着，我的意识陷入了沉睡之中……"
    window hide

    stop bgm 
    scene expression Solid("000000")  with fade


    $ loadBG(0,"BG26A")

    show screen phonebtn
    show screen phoneSD1
    $ stopvoc("SUZ")
    play SUZ "FEI03A_SUZ0015"
    $ current_voice = "voice/FEI03A_SUZ0015.ogg"
    "铃羽" "「……哈、……哈、……哈」"
    "醒来的时候，没在床上看到阿万音的身影，我正想着她是不是去了什么别的地方了。"
    "在客厅发现了她的身影。"
    $ stopvoc("FEI")
    play FEI "FEI03A_FEI0017"
    $ current_voice = "voice/FEI03A_FEI0017.ogg"
    "菲利斯" "「呜喵，你在干什么呀喵？」"
    $ stopvoc("SUZ")
    play SUZ "FEI03A_SUZ0016"
    $ current_voice = "voice/FEI03A_SUZ0016.ogg"
    "铃羽" "「……哈，看了还不知道吗？　……哈、这是俯卧撑哦……哈，俯卧撑」"
    "看了看时钟……８点３８分。"
    $ stopvoc("SUZ")
    play SUZ "FEI03A_SUZ0017"
    $ current_voice = "voice/FEI03A_SUZ0017.ogg"
    "铃羽" "「……好」"

    hide lh7 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_ESA01"),"True","lh/SUZ_ESA01a~ipad.png") at center as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    play bgm "BGM26"
    "接过毛巾的阿万音刷的一下站了起来。"
    "已经换上了服装。"
    $ stopvoc("SUZ")
    play SUZ "FEI03A_SUZ0018"
    $ current_voice = "voice/FEI03A_SUZ0018.ogg"
    "铃羽" "「你很喜欢睡懒觉呢。黑木先生已经准备好早饭了」"
    "我从被窝里慢慢地钻了出来。"
    $ stopvoc("FEI")
    play FEI "FEI03A_FEI0018"
    $ current_voice = "voice/FEI03A_FEI0018.ogg"
    "菲利斯" "「你平时都几点钟起床啊？」"
    $ stopvoc("SUZ")
    play SUZ "FEI03A_SUZ0019"
    $ current_voice = "voice/FEI03A_SUZ0019.ogg"
    "铃羽" "「６点吧。诶呀，来到这边之后都开始睡懒觉了」"
    "……６点起床都算睡懒觉吗。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_ESA02"),"True","lh/SUZ_ESA02a~ipad.png") as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "FEI03A_SUZ0020"
    $ current_voice = "voice/FEI03A_SUZ0020.ogg"
    "铃羽" "「就算那样昨天也挺不错的呢。早上起来的时候，有谁睡在旁边的感觉」"
    $ stopvoc("FEI")
    play FEI "FEI03A_FEI0019"
    $ current_voice = "voice/FEI03A_FEI0019.ogg"
    "菲利斯" "「菲利斯也想起了１０年前的时候」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_ESA06"),"True","lh/SUZ_ESA06a~ipad.png") as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "FEI03A_SUZ0021"
    $ current_voice = "voice/FEI03A_SUZ0021.ogg"
    "铃羽" "「像以前那样醒来的时候人已经不见了的事情，在现在这个世界上已经没有了呢。不用担心那种事情的感觉真是不错」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve


    hide screen phonebtn
    $ targetmailid = gc["ScriptMacros"]["FM_FEI03A_RECV_FEI01"]
    if phonemailring!= "":
        play se phonemailring
    if persistent.skipmail==False:
        $ renpy.choice_for_skipping()
    if targetmailid != "":
        $ RcvMail(targetmailid)
        $ targetmailid=""
    "从房间里拿出来的手机发出着有邮件的亮光。"

    "我拼命撑起眼皮，确认了一下内容。"

    window hide


    hide screen phonebtn
    hide screen phonebtn2
    pause 2
    call read_last_mail







    stop bgm 
    "打开邮件的瞬间，我的头里一片空白。"
    play bgm "BGM23"
    "是我发来的邮件？"
    "去帮助绹吧？"
    "绹是说显像管工房的店长的女儿吧。但是为什么是我给自己发的邮件？"
    $ stopvoc("SUZ")
    play SUZ "FEI03A_SUZ0022"
    $ current_voice = "voice/FEI03A_SUZ0022.ogg"
    "铃羽" "「怎么了嘛，Ｂｏｓｓ」"
    "是觉得我的样子有点奇怪吗，阿万音从我身后看着我的手里。"
    "听着她叹了口气，我也明白了她心中的无奈。"
    $ stopvoc("SUZ")
    play SUZ "FEI03A_SUZ0023"
    $ current_voice = "voice/FEI03A_SUZ0023.ogg"
    "铃羽" "「这是……啥？」"
    $ stopvoc("FEI")
    play FEI "FEI03A_FEI0020"
    $ current_voice = "voice/FEI03A_FEI0020.ogg"
    "菲利斯" "「菲利斯也想问喵」"
    $ stopvoc("SUZ")
    play SUZ "FEI03A_SUZ0024"
    $ current_voice = "voice/FEI03A_SUZ0024.ogg"
    "铃羽" "「绹……是那个绹吧」"
    $ stopvoc("FEI")
    play FEI "FEI03A_FEI0021"
    $ current_voice = "voice/FEI03A_FEI0021.ogg"
    "菲利斯" "「就算是……恶作剧吧，但为什么发件人是菲利斯喵？」"

    hide lh7 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_EMB04"),"True","lh/SUZ_EMB04a~ipad.png") at center as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "FEI03A_SUZ0025"
    $ current_voice = "voice/FEI03A_SUZ0025.ogg"
    "铃羽" "「总之我们去看看吧。就算什么也没发生也想要确认一下」"
    window hide
    call hide_phone

    $ stopvoc("FEI")
    play FEI "FEI03A_FEI0022"
    $ current_voice = "voice/FEI03A_FEI0022.ogg"
    "菲利斯" "「那么就赶紧去准备吧」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_EMA02"),"True","lh/SUZ_EMA02a~ipad.png") as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "FEI03A_SUZ0026"
    $ current_voice = "voice/FEI03A_SUZ0026.ogg"
    "铃羽" "「黑猫出动！」"
    window hide

    stop bgm 



    $ loadBG(0,"BG30A0")

    "那是在Ｌａｂ前面的小路里发生的事情。"
    "阿万音立刻就注意到了，指着古董零件店在我的耳边低语道。"
    $ stopvoc("SUZ")
    play SUZ "FEI03A_SUZ0027"
    $ current_voice = "voice/FEI03A_SUZ0027.ogg"
    "铃羽" "「Ｂｏｓｓ，那个」"

    hide lh7 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_BSA01"),"True","lh/OKA_BSA01a~ipad.png") at center as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    play bgm "BGM12"
    "我看到她的发现，虎躯一震。"
    "感觉身体里有火在熊熊燃烧着，那种血液都要沸腾起来逆向流动的快感遍布全身。"
    window hide



    $ loadBG(2,"BG30A0")





    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_BMA01"),"True","lh/OKA_BMA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    "那个就是……阿万音和我一直在追寻的东西。"
    "穿着高领风衣，满是走错了时代的着衣风格。"
    "全身遍布鳞片，露着滑溜溜的绿色肌肤。"
    "眼睛是血红色的，嘴巴一直到耳朵边上，里面满是尖牙利齿。"
    "那莫非不就是蜥蜴人吗？"
    "是打算偷偷观察古董零件店里的店主，伺机猎杀吗？"
    window hide



    $ loadBG(2,"BG30A0")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_FMB04"),"True","lh/SUZ_FMB04a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    "我和阿万音对视一眼，然后慢慢地从身后接近，最后看准时机一起冲了出去！"
    hide screen phoneSD1
    window hide
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_FEI003A"]]["Check"]=True


    $ loadBG(2,"EV_FEI003A")



    hide screen phonebtn
    $ stopvoc("SUZ")
    play SUZ "FEI03A_SUZ0028"
    $ current_voice = "voice/FEI03A_SUZ0028.ogg"
    "铃羽" "「……！」"
    $ stopvoc("FEI")
    play FEI "FEI03A_FEI0023"
    $ current_voice = "voice/FEI03A_FEI0023.ogg"
    "菲利斯" "「豁呀！」"
    "被吓了一跳的蜥蜴人。"
    "他反射性地将身子向后倾，奇迹般地躲开了从左右两侧飞扑过来的我们。"
    "失去了目标的我一瞬间停顿了一下，但是运动神经超群的阿万音并没有迟疑。"
    $ stopvoc("SUZ")
    play SUZ "FEI03A_SUZ0029"
    $ current_voice = "voice/FEI03A_SUZ0029.ogg"
    "铃羽" "「……！」"
    "飞快地跑进了似乎想逃的蜥蜴人前进方向，露出了杀气，威吓似地捏了捏手指。"
    $ stopvoc("FEI")
    play FEI "FEI03A_FEI0024"
    $ current_voice = "voice/FEI03A_FEI0024.ogg"
    "菲利斯" "「还有我这边喵！」"
    "我从背后攻了过去。从真由理酱做的小口袋里取出猫爪，我也朝着蜥蜴人飞扑过去。"
    $ stopvoc("OKA")
    play OKA "FEI03A_OKA0000"
    $ current_voice = "voice/FEI03A_OKA0000.ogg"
    "伦太郎" "「○×＃＄＠ＴＴ）！！！！！」"
    "蜥蜴人发出奇妙的声音之后身子一晃，堪堪躲过了猫爪攻击。"
    $ stopvoc("SUZ")
    play SUZ "FEI03A_SUZ0030"
    $ current_voice = "voice/FEI03A_SUZ0030.ogg"
    "铃羽" "「喂别想逃啊！」"
    "抓住了一瞬间的空隙，阿万音从后方抓住了蜥蜴人的背后。"
    "蜥蜴人为了逃跑拼命地挣扎着。"
    "我的视线，被那令人厌恶的红色眼前所吸引。"
    "那双眼睛，好像在哪里看到过……"
    window hide



    $ loadBG(2,"BG30A0")

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ISA01"),"True","lh/CRS_ISA01a~ipad.png") at center as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    show screen phonebtn
    show screen phoneSD1
    "就在那时，另一只蜥蜴人，从零件点里走了出来。"
    $ stopvoc("CRS")
    play CRS "FEI03A_CRS0000"
    $ current_voice = "voice/FEI03A_CRS0000.ogg"
    "红莉栖" "「△▼×□＄＆＞＜！？」"
    $ stopvoc("SUZ")
    play SUZ "FEI03A_SUZ0031"
    $ current_voice = "voice/FEI03A_SUZ0031.ogg"
    "铃羽" "「又来了一条！？　难道说……！！」"
    "总觉得另外一条蜥蜴人看起来也很眼熟。"
    "虽然眼睛是红色的，但是那眼睛里的一些微妙的动作感觉在哪里见过。"

    stop bgm 
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    "……原来如此。"
    "被阿万音抓住背后的蜥蜴人和另一条蜥蜴人。"
    "我取下了护目镜，看着两边的蜥蜴人宣告道。"
    $ stopvoc("FEI")
    play FEI "FEI03A_FEI0025"
    $ current_voice = "voice/FEI03A_FEI0025.ogg"
    "菲利斯" "「放开他也没关系，铃羽喵」"

    hide lh7 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_FSA03"),"True","lh/SUZ_FSA03a~ipad.png") at center as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "FEI03A_SUZ0032"
    $ current_voice = "voice/FEI03A_SUZ0032.ogg"
    "铃羽" "「诶？　明明好不容易才捉到的啊？」"
    $ stopvoc("FEI")
    play FEI "FEI03A_FEI0026"
    $ current_voice = "voice/FEI03A_FEI0026.ogg"
    "菲利斯" "「我明白他们的身份了。那么你们可要把真相一五一十地招出来啊，两位喵」"
    $ stopvoc("FEI")
    play FEI "FEI03A_FEI0027"
    $ current_voice = "voice/FEI03A_FEI0027.ogg"
    "菲利斯" "「做好觉悟了喵？　凶真，红喵」"
    window hide



    $ loadBG(0,"BG02A1")

    play bgm "BGM22"
    "Ｌａｂ的小房间被异样的空气所笼罩着。"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ISC01"),"True","lh/CRS_ISC01a~ipad.png") at left as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_BSA01"),"True","lh/OKA_BSA01a~ipad.png") at right as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    "冈部和牧濑正襟危坐在地板上。"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA03"),"True","lh/DAR_ASA03a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    "通宵的桶子，在一边冷冷旁观着。"
    "我和阿万音把手挽在胸前，俯视着冈部他们。"
    "其实是为了绹的事情来的，但是现在好像不是问她这个问题的时机。"
    hide screen phoneSD1
    window hide


    $ loadBG(0,"BG04A1")

    hide lh7 
    show expression ConditionSwitch("renpy.music.get_playing(channel='TEN')",DynamicDisplayable(mouthanime,"TEN_ASA01"),"True","lh/TEN_ASA01a~ipad.png") at center as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    hide lh8 
    show expression ConditionSwitch("renpy.music.get_playing(channel='NAE')",DynamicDisplayable(mouthanime,"NAE_ASA01"),"True","lh/NAE_ASA01a~ipad.png") at left_t as lh8 zorder (10-8) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    hide screen phonebtn
    "据朝显像管工房里望了一眼的阿万音说，天王寺绹忙着帮店里的忙，好像没空的样子。"
    window hide


    $ loadBG(0,"BG02A1")

    show screen phonebtn
    show screen phoneSD1
    "总之虽然确认没出啥事，但到明白邮件的意思之前可不能大意。"
    "所以在等着绹酱完成开店准备之前，我们决定先问清楚蜥蜴人的真相。"

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_ESA03"),"True","lh/SUZ_ESA03a~ipad.png") at left as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA03"),"True","lh/DAR_ASA03a~ipad.png") at right as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "FEI03A_SUZ0033"
    $ current_voice = "voice/FEI03A_SUZ0033.ogg"
    "铃羽" "「就算如此……」"
    $ stopvoc("FEI")
    play FEI "FEI03A_FEI0028"
    $ current_voice = "voice/FEI03A_FEI0028.ogg"
    "菲利斯" "「这个化妆好厉害喵。质感和使用方法都很不错，可以做出很多丰富的表情喵」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA01"),"True","lh/DAR_ASA01a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "FEI03A_DAR0000"
    $ current_voice = "voice/FEI03A_DAR0000.ogg"
    "至" "「眼睛是用美瞳的吧？　嘴巴上的裂缝仔细看看的话是画出来的嘛」"
    $ stopvoc("OKA")
    play OKA "FEI03A_OKA0001"
    $ current_voice = "voice/FEI03A_OKA0001.ogg"
    "伦太郎" "「呼呼呼……唔哈哈哈哈！」"
    $ stopvoc("OKA")
    play OKA "FEI03A_OKA0002"
    $ current_voice = "voice/FEI03A_OKA0002.ogg"
    "伦太郎" "「可不是吗可不是吗！这个化妆是在上电影学院的，古董零件店的老板的小鬼的朋友的弟弟的杰作哦。必须是完美的！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA02"),"True","lh/DAR_ASA02a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "FEI03A_DAR0001"
    $ current_voice = "voice/FEI03A_DAR0001.ogg"
    "至" "「冈伦反省的意思不够哦。再沉默一会不是更加酷么？」"
    $ stopvoc("OKA")
    play OKA "FEI03A_OKA0003"
    $ current_voice = "voice/FEI03A_OKA0003.ogg"
    "伦太郎" "「抱歉啊桶子。这个任务是只能由被选中的人来完成的，也就是所谓的Ｏｐｅｒａｔｉｏｎ・Ｇｒａｎｄｅ。如果不让我凤凰院凶真来做的话，换了别人谁都是做不到的！」"
    $ stopvoc("CRS")
    play CRS "FEI03A_CRS0001"
    $ current_voice = "voice/FEI03A_CRS0001.ogg"
    "红莉栖" "「说什么这么羞耻的样子可不能让真由理看到的还不是你吗」"
    $ stopvoc("OKA")
    play OKA "FEI03A_OKA0004"
    $ current_voice = "voice/FEI03A_OKA0004.ogg"
    "伦太郎" "「…………」"
    window hide



    $ loadBG(2,"BG01A")

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MOE')",DynamicDisplayable(mouthanime,"MOE_ASB02"),"True","lh/MOE_ASB02a~ipad.png") at center as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)
    play se "SGSE024"


    stop bgm 



    "突然门被打开了，我们大家一齐望向那里。"
    "呆立在玄关的是，握着门把手僵在那里的桐生。"

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MOE')",DynamicDisplayable(mouthanime,"MOE_ASB04"),"True","lh/MOE_ASB04a~ipad.png") at center as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MOE")
    play MOE "FEI03A_MOE0000"
    $ current_voice = "voice/FEI03A_MOE0000.ogg"
    "萌郁" "「…………」"
    "是有什么内疚的事情吗，眼神游离不定。"
    "飘忽不定的视线的另一端是，正坐在那里的冈部和牧濑。"
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    "她好像理解了目前的情况。于是一副若无其事的样子，又关上了门离开了这里。"
    play se "SGSE024"
    $ stopvoc("OKA")
    play OKA "FEI03A_OKA0005"
    $ current_voice = "voice/FEI03A_OKA0005.ogg"
    "伦太郎" "「别想逃萌郁！」"
    "从她本身的反应，以及和冈部的所谓“打工”的事实来看，她和这次的骚动也脱不了关系。"
    "所以我才在冈部说话的同时给阿万音下了指令。"
    $ stopvoc("FEI")
    play FEI "FEI03A_FEI0029"
    $ current_voice = "voice/FEI03A_FEI0029.ogg"
    "菲利斯" "「铃喵，拜托了喵！」"

    hide lh7 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_ESA02"),"True","lh/SUZ_ESA02a~ipad.png") at center as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "FEI03A_SUZ0034"
    $ current_voice = "voice/FEI03A_SUZ0034.ogg"
    "铃羽" "「Ｏｋａｙ－Ｄｏｋｅｙ♪」"
    window hide


    $ loadBG(3,"IBGX048",over=True)
    with vpunch
    with hpunch
    with vpunch
    hide background-over 
    with dissolve












    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA02"),"True","lh/DAR_ASA02a~ipad.png") at right_q2 as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ISC01"),"True","lh/CRS_ISC01a~ipad.png") at left_q2 as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15

    hide lh7 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_BSA01"),"True","lh/OKA_BSA01a~ipad.png") at left_q1 as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15

    hide lh8 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MOE')",DynamicDisplayable(mouthanime,"MOE_ASB03"),"True","lh/MOE_ASB03a~ipad.png") at right_q1 as lh8 zorder (10-8) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)





    play bgm "BGM26"
    $ stopvoc("DAR")
    play DAR "FEI03A_DAR0002"
    $ current_voice = "voice/FEI03A_DAR0002.ogg"
    "至" "「……所以，到底是怎么一回事说明Ｐｌｅａｓｅ」"
    "包括被抓回来的桐生在内，他们做出了一副做好了觉悟的样子抬起了头看着我们。"
    $ stopvoc("CRS")
    play CRS "FEI03A_CRS0002"
    $ current_voice = "voice/FEI03A_CRS0002.ogg"
    "红莉栖" "「其实呢……是作为给显像管工房的店长打工的一部分哦。你看，租金不是一直拖着吗。于是他就说你们就当回蜥蜴人去把那个都市传说再搞得大一些吧」"
    $ stopvoc("OKA")
    play OKA "FEI03A_OKA0006"
    $ current_voice = "voice/FEI03A_OKA0006.ogg"
    "伦太郎" "「不是什么蜥蜴人，是Ｔｈｅ☆Ｌｉｚａｒｄ！是从混沌的黑暗中诞生的孤高的魔神！你要我说几次才会记住啊！」"
    $ stopvoc("CRS")
    play CRS "FEI03A_CRS0003"
    $ current_voice = "voice/FEI03A_CRS0003.ogg"
    "红莉栖" "「是是，Ｌｉｚａｒｄ」"
    $ stopvoc("OKA")
    play OKA "FEI03A_OKA0007"
    $ current_voice = "voice/FEI03A_OKA0007.ogg"
    "伦太郎" "「是Ｔｈｅ☆Ｌｉｚａｒｄ！」"
    $ stopvoc("DAR")
    play DAR "FEI03A_DAR0003"
    $ current_voice = "voice/FEI03A_DAR0003.ogg"
    "至" "「不管哪种都好吧」"
    $ stopvoc("FEI")
    play FEI "FEI03A_FEI0030"
    $ current_voice = "voice/FEI03A_FEI0030.ogg"
    "菲利斯" "「也就是说三个都市传说中，有关蜥蜴人的是店长自演自导的喵？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ISA01"),"True","lh/CRS_ISA01a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "FEI03A_CRS0004"
    $ current_voice = "voice/FEI03A_CRS0004.ogg"
    "红莉栖" "「……不对，全部都是哦」"
    window hide
    hide lh5  with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_ESA03"),"True","lh/SUZ_ESA03a~ipad.png") at right_q2 as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "FEI03A_SUZ0035"
    $ current_voice = "voice/FEI03A_SUZ0035.ogg"
    "铃羽" "「全部？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ISB01"),"True","lh/CRS_ISB01a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "FEI03A_CRS0005"
    $ current_voice = "voice/FEI03A_CRS0005.ogg"
    "红莉栖" "「恩恩，蜥蜴人呀ＵＦＯ呀还有人间蒸发呀，全部是编出来的哦」"
    window hide
    play se "SGSE063"



    $ loadBG(2,"BG_BLACK",trans=ImageDissolve(im.Scale("mask/mask00.png",1024,576),1),at=[Transform(alpha=0.5)],over=True)









    "……又是，谎言。"
    window hide
    hide background-over  with dissolve

















    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_ESA01"),"True","lh/SUZ_ESA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "FEI03A_SUZ0036"
    $ current_voice = "voice/FEI03A_SUZ0036.ogg"
    "铃羽" "「桐生萌郁刚才为什么要逃跑呀？」"
    $ stopvoc("CRS")
    play CRS "FEI03A_CRS0006"
    $ current_voice = "voice/FEI03A_CRS0006.ogg"
    "红莉栖" "「她是摄影人员」"
    $ stopvoc("FEI")
    play FEI "FEI03A_FEI0031"
    $ current_voice = "voice/FEI03A_FEI0031.ogg"
    "菲利斯" "「……专门拍秋叶原怪奇地图的照片喵」"
    "这么说着桐生似乎是不好意思地低下了头。"
    window hide

    show expression ConditionSwitch("renpy.music.get_playing(channel='MOE')",DynamicDisplayable(mouthanime,"MOE_ASA01"),"True","lh/MOE_ASA01a~ipad.png") as lh8 zorder (10-8) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    $ targetmailid = gc["ScriptMacros"]["FM_FEI03A_RECV_MOE01"]
    if phonemailring!= "":
        play se phonemailring
    if persistent.skipmail==False:
        $ renpy.choice_for_skipping()
    if targetmailid != "":
        $ RcvMail(targetmailid)
        $ targetmailid=""


    show expression ConditionSwitch("renpy.music.get_playing(channel='MOE')",DynamicDisplayable(mouthanime,"MOE_ASB03"),"True","lh/MOE_ASB03a~ipad.png") as lh8 zorder (10-8) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    show screen phonebtn
    hide screen phonebtn
    hide screen phonebtn2
    call read_last_mail



    call hide_phone

    $ stopvoc("FEI")
    play FEI "FEI03A_FEI0032"
    $ current_voice = "voice/FEI03A_FEI0032.ogg"
    "菲利斯" "「也就是说店长喵在暗中操作，这是委员会搞出来的事情啊」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ISC01"),"True","lh/CRS_ISC01a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "FEI03A_CRS0007"
    $ current_voice = "voice/FEI03A_CRS0007.ogg"
    "红莉栖" "「确实。计划通过秋叶原的怪异事件来吸引更多的游客」"
    $ stopvoc("SUZ")
    play SUZ "FEI03A_SUZ0037"
    $ current_voice = "voice/FEI03A_SUZ0037.ogg"
    "铃羽" "「那样的话，告诉我们不就好了吗」"
    $ stopvoc("CRS")
    play CRS "FEI03A_CRS0008"
    $ current_voice = "voice/FEI03A_CRS0008.ogg"
    "红莉栖" "「但这超害羞的啊！？　真不想让大家看到我穿成这样……」"
    window hide
    hide lh5  with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA04"),"True","lh/DAR_ASA04a~ipad.png") at right_q2 as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "FEI03A_DAR0004"
    $ current_voice = "voice/FEI03A_DAR0004.ogg"
    "至" "「羞耻Ｐｌａｙ，哈哈」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ISB01"),"True","lh/CRS_ISB01a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "FEI03A_CRS0009"
    $ current_voice = "voice/FEI03A_CRS0009.ogg"
    "红莉栖" "「闭嘴ＨＥＮＴＡＩ」"
    $ stopvoc("OKA")
    play OKA "FEI03A_OKA0008"
    $ current_voice = "voice/FEI03A_OKA0008.ogg"
    "伦太郎" "「还有就是Ｍｒ布朗也让我们不要说出来……」"
    $ stopvoc("OKA")
    play OKA "FEI03A_OKA0009"
    $ current_voice = "voice/FEI03A_OKA0009.ogg"
    "伦太郎" "「他说敢说的话就要把房租涨到３倍！」"
    $ stopvoc("OKA")
    play OKA "FEI03A_OKA0010"
    $ current_voice = "voice/FEI03A_OKA0010.ogg"
    "伦太郎" "「那个光头，下次见到了可不能饶了他！」"
    window hide
    hide lh5  with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_ESA01"),"True","lh/SUZ_ESA01a~ipad.png") at right_q2 as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "FEI03A_SUZ0038"
    $ current_voice = "voice/FEI03A_SUZ0038.ogg"
    "铃羽" "「啊、店長！　早上好」"

    $ stopvoc("OKA")
    play OKA "FEI03A_OKA0011"
    $ current_voice = "voice/FEI03A_OKA0011.ogg"
    "伦太郎" "「咿！」"
    $ stopvoc("SUZ")
    play SUZ "FEI03A_SUZ0039"
    $ current_voice = "voice/FEI03A_SUZ0039.ogg"
    "铃羽" "「开玩笑的♪」"
    $ stopvoc("OKA")
    play OKA "FEI03A_OKA0012"
    $ current_voice = "voice/FEI03A_OKA0012.ogg"
    "伦太郎" "「唔咕……！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_ESA02"),"True","lh/SUZ_ESA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "FEI03A_SUZ0040"
    $ current_voice = "voice/FEI03A_SUZ0040.ogg"
    "铃羽" "「啊哈哈哈♪」"

    stop bgm 
    "屋内沉重的氛围一下子就变成了我所熟悉的欢乐的氛围。但是就算知道了都市传说的真相，我的心情依然没能放松下来。"
    "——还有那群大人。"
    "什么都是，谎言、谎言、谎言……"
    "开会的时候什么计划的事情都不和我说，却在背后搞这些东西。"
    "他们之所以不说，肯定是认为我会反对这样的计划，所以就索性来个先斩后奏。说起来这样的话，监视者应该也只是确认我和阿万音没有做什么多余的事情吧。"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_EMB04"),"True","lh/SUZ_EMB04a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "FEI03A_SUZ0041"
    $ current_voice = "voice/FEI03A_SUZ0041.ogg"
    "铃羽" "「呐，Ｂｏｓｓ」"
    "在我想着这些的时候，阿万音凑了过来，以只有我听得到的声音说道。"
    $ stopvoc("SUZ")
    play SUZ "FEI03A_SUZ0042"
    $ current_voice = "voice/FEI03A_SUZ0042.ogg"
    "铃羽" "「店长肯定认为我迟到了啊。你看都不是在让绹帮忙准备开店的事情了吗」"
    $ stopvoc("FEI")
    play FEI "FEI03A_FEI0033"
    $ current_voice = "voice/FEI03A_FEI0033.ogg"
    "菲利斯" "「她真的会一个人出来喵？」"
    $ stopvoc("SUZ")
    play SUZ "FEI03A_SUZ0043"
    $ current_voice = "voice/FEI03A_SUZ0043.ogg"
    "铃羽" "「我们来瞄一眼吧？」"
    $ stopvoc("FEI")
    play FEI "FEI03A_FEI0034"
    $ current_voice = "voice/FEI03A_FEI0034.ogg"
    "菲利斯" "「稍微等一下喵」"
    "我转过头去朝着冈部，以牧濑和桶子君也能听到的音量说道。"
    $ stopvoc("FEI")
    play FEI "FEI03A_FEI0035"
    $ current_voice = "voice/FEI03A_FEI0035.ogg"
    "菲利斯" "「凶真，有些事想问你可以吗？」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh7 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_BSA01"),"True","lh/OKA_BSA01a~ipad.png") at center as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "FEI03A_OKA0013"
    $ current_voice = "voice/FEI03A_OKA0013.ogg"
    "伦太郎" "「尽管问就是了！」"
    $ stopvoc("FEI")
    play FEI "FEI03A_FEI0036"
    $ current_voice = "voice/FEI03A_FEI0036.ogg"
    "菲利斯" "「今天早上，你有给菲利斯发过邮件喵？」"
    $ stopvoc("OKA")
    play OKA "FEI03A_OKA0014"
    $ current_voice = "voice/FEI03A_OKA0014.ogg"
    "伦太郎" "「……邮件？　没有，今天早上一直在化妆忙得很。到现在连看一眼收件箱的时间都没有」"
    "我环视了一下房间里的众人，桶子、牧濑、桐生，大家对于邮件看起来毫不知情的样子。"
    "抱着一丝侥幸问了一下，果然没有任何收获啊。"
    $ stopvoc("FEI")
    play FEI "FEI03A_FEI0037"
    $ current_voice = "voice/FEI03A_FEI0037.ogg"
    "菲利斯" "「那样的话就没事了喵」"
    $ stopvoc("SUZ")
    play SUZ "FEI03A_SUZ0044"
    $ current_voice = "voice/FEI03A_SUZ0044.ogg"
    "铃羽" "「那么，我们还有一点事就先告辞了"
    "这么说着，我们就离开了因为冈部和牧濑的特殊化妆而骚动的Ｌａｂ。"
    window hide


    $ loadBG(0,"BG05A1")

    play bgm "BGM18"

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='NAE')",DynamicDisplayable(mouthanime,"NAE_ASA01"),"True","lh/NAE_ASA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    "从大楼２楼下来，沿着楼梯走到楼下之后，我们就看到了绹酱在显像管工房门前扫着地。"
    "和作战计划一样。阿万音和我交换了一个眼神。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='NAE')",DynamicDisplayable(mouthanime,"NAE_ASA02"),"True","lh/NAE_ASA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("NAE")
    play NAE "FEI03A_NAE0000"
    $ current_voice = "voice/FEI03A_NAE0000.ogg"
    "绹" "「啊，打工姐姐和猫姐姐，早上好☆」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_FSA01"),"True","lh/SUZ_FSA01a~ipad.png") at left as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='NAE')",DynamicDisplayable(mouthanime,"NAE_ASA02"),"True","lh/NAE_ASA02a~ipad.png") at right as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "FEI03A_SUZ0045"
    $ current_voice = "voice/FEI03A_SUZ0045.ogg"
    "铃羽" "「早上好」"
    $ stopvoc("FEI")
    play FEI "FEI03A_FEI0038"
    $ current_voice = "voice/FEI03A_FEI0038.ogg"
    "菲利斯" "「早上好……诶，猫姐姐？　咦？　我……」"
    "我还在想为什么会暴露的时候才注意到……没有带护目镜啊。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_FSB04"),"True","lh/SUZ_FSB04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "FEI03A_SUZ0046"
    $ current_voice = "voice/FEI03A_SUZ0046.ogg"
    "铃羽" "「疏忽是最大的敌人啊」"
    $ stopvoc("FEI")
    play FEI "FEI03A_FEI0039"
    $ current_voice = "voice/FEI03A_FEI0039.ogg"
    "菲利斯" "「……会注意的」"
    "我干净利落地掏出护目镜带上。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='NAE')",DynamicDisplayable(mouthanime,"NAE_ASA04"),"True","lh/NAE_ASA04a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("NAE")
    play NAE "FEI03A_NAE0001"
    $ current_voice = "voice/FEI03A_NAE0001.ogg"
    "绹" "「打工姐姐，爸爸很生气哦。迟到是不行的哦」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_FSA01"),"True","lh/SUZ_FSA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "FEI03A_SUZ0047"
    $ current_voice = "voice/FEI03A_SUZ0047.ogg"
    "铃羽" "「抱歉抱歉。啊，我来打扫吧」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='NAE')",DynamicDisplayable(mouthanime,"NAE_ASA02"),"True","lh/NAE_ASA02a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    "绹酱把扫把递给阿万音，然后像是等不及了似的眼睛里闪着光看着我们。"
    $ stopvoc("NAE")
    play NAE "FEI03A_NAE0002"
    $ current_voice = "voice/FEI03A_NAE0002.ogg"
    "绹" "「呐呐，这件衣服，是昨天在车站前面发传单的时候穿的那件吧！」"
    "是因为能够近距离看的关系兴奋起来了吗，她看着我和阿万音的服装，一脸激动的样子。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='NAE')",DynamicDisplayable(mouthanime,"NAE_ASA01"),"True","lh/NAE_ASA01a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("NAE")
    play NAE "FEI03A_NAE0003"
    $ current_voice = "voice/FEI03A_NAE0003.ogg"
    "绹" "「这难道，莫非就是叫做Ｃｏｓｐｌａｙ的？」"
    $ stopvoc("FEI")
    play FEI "FEI03A_FEI0040"
    $ current_voice = "voice/FEI03A_FEI0040.ogg"
    "菲利斯" "「恩，和Ｃｏｓｐｌａｙ有点不一样♥我是秋叶原的守护战士黑猫，她是我的伙伴希艾拉。请多指教呢」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='NAE')",DynamicDisplayable(mouthanime,"NAE_ASA02"),"True","lh/NAE_ASA02a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("NAE")
    play NAE "FEI03A_NAE0004"
    $ current_voice = "voice/FEI03A_NAE0004.ogg"
    "绹" "「真厉害啊ー♪　呐呐，可以摸摸看吗？」"
    $ stopvoc("FEI")
    play FEI "FEI03A_FEI0041"
    $ current_voice = "voice/FEI03A_FEI0041.ogg"
    "菲利斯" "「当然了！　请不要顾忌随便摸吧♪」"
    "她看起来很稀罕地摸着紧身衣，画着圆圈那样感受着衣服的质感。"
    "看准了时机，我摆出了弯下身去的姿势。"
    $ stopvoc("FEI")
    play FEI "FEI03A_FEI0042"
    $ current_voice = "voice/FEI03A_FEI0042.ogg"
    "菲利斯" "「说起来有一些想问你的事情，可以吗」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='NAE')",DynamicDisplayable(mouthanime,"NAE_ASA01"),"True","lh/NAE_ASA01a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("NAE")
    play NAE "FEI03A_NAE0005"
    $ current_voice = "voice/FEI03A_NAE0005.ogg"
    "绹" "「什么？」"
    $ stopvoc("FEI")
    play FEI "FEI03A_FEI0043"
    $ current_voice = "voice/FEI03A_FEI0043.ogg"
    "菲利斯" "「最近，有什么困扰或者令你害怕的事情吗？」"
    $ stopvoc("NAE")
    play NAE "FEI03A_NAE0006"
    $ current_voice = "voice/FEI03A_NAE0006.ogg"
    "绹" "「可怕的事情？」"
    $ stopvoc("FEI")
    play FEI "FEI03A_FEI0044"
    $ current_voice = "voice/FEI03A_FEI0044.ogg"
    "菲利斯" "「被谁看着的啦，或者跟在后面之类的」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='NAE')",DynamicDisplayable(mouthanime,"NAE_ASA05"),"True","lh/NAE_ASA05a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("NAE")
    play NAE "FEI03A_NAE0007"
    $ current_voice = "voice/FEI03A_NAE0007.ogg"
    "绹" "「啊！　那样的话，一直有哦」"
    $ stopvoc("FEI")
    play FEI "FEI03A_FEI0045"
    $ current_voice = "voice/FEI03A_FEI0045.ogg"
    "菲利斯" "「知道是谁吗？」"
    $ stopvoc("NAE")
    play NAE "FEI03A_NAE0008"
    $ current_voice = "voice/FEI03A_NAE0008.ogg"
    "绹" "「恩」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_FSB04"),"True","lh/SUZ_FSB04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "FEI03A_SUZ0048"
    $ current_voice = "voice/FEI03A_SUZ0048.ogg"
    "铃羽" "「谁！？」"
    $ stopvoc("NAE")
    play NAE "FEI03A_NAE0009"
    $ current_voice = "voice/FEI03A_NAE0009.ogg"
    "绹" "「爸爸！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_FSA03"),"True","lh/SUZ_FSA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FEI")
    play FEI "FEI03A_FEI0046"
    $ current_voice = "voice/FEI03A_FEI0046.ogg"
    "菲利斯" "「……诶？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='NAE')",DynamicDisplayable(mouthanime,"NAE_ASA01"),"True","lh/NAE_ASA01a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("NAE")
    play NAE "FEI03A_NAE0010"
    $ current_voice = "voice/FEI03A_NAE0010.ogg"
    "绹" "「２楼的人变多了不是吗？　所以他担心会不会有人教我奇怪的东西」"
    "２楼？是在说我们吗。"
    $ stopvoc("SUZ")
    play SUZ "FEI03A_SUZ0049"
    $ current_voice = "voice/FEI03A_SUZ0049.ogg"
    "铃羽" "「店长保护过度啦」"
    $ stopvoc("FEI")
    play FEI "FEI03A_FEI0047"
    $ current_voice = "voice/FEI03A_FEI0047.ogg"
    "菲利斯" "「还有呢？」"
    $ stopvoc("NAE")
    play NAE "FEI03A_NAE0011"
    $ current_voice = "voice/FEI03A_NAE0011.ogg"
    "绹" "「恩……。没有哦？」"
    "怎么看都不像在说谎的样子。也没有能继续问下去的感觉，果然那封邮件是别的含义吗。"
    $ stopvoc("TEN")
    play TEN "FEI03A_TEN0000"
    $ current_voice = "voice/FEI03A_TEN0000.ogg"
    "天王寺" "「喂喂，可不要给我的女儿灌输奇怪的东西啊」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='TEN')",DynamicDisplayable(mouthanime,"TEN_ASA01"),"True","lh/TEN_ASA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    "看了一眼那个光头……不对，绹酱的爸爸正好走出来了。"
    "他也是委员会的一员，恐怕这次的怪谈计划也有他的一份。"
    "他看见我的脸，露出了惊讶的表情。但是很快他就恢复了正常的样子，不动声色地站到了我和阿万音面前。"
    $ stopvoc("TEN")
    play TEN "FEI03A_TEN0001"
    $ current_voice = "voice/FEI03A_TEN0001.ogg"
    "天王寺" "「因为你打工迟到了，还以为出了什么事呢」"

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='TEN')",DynamicDisplayable(mouthanime,"TEN_ASA03"),"True","lh/TEN_ASA03a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("TEN")
    play TEN "FEI03A_TEN0002"
    $ current_voice = "voice/FEI03A_TEN0002.ogg"
    "天王寺" "「这么看又是……穿了奇怪的服装啊，小姑娘们」"
    "他上下打量着阿万音和我的服装。眼中只有吃惊的感情。"

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='TEN')",DynamicDisplayable(mouthanime,"TEN_ASA01"),"True","lh/TEN_ASA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("TEN")
    play TEN "FEI03A_TEN0003"
    $ current_voice = "voice/FEI03A_TEN0003.ogg"
    "天王寺" "「可别把我家女儿带坏了啊」"

    stop bgm 
    $ stopvoc("FEI")
    play FEI "FEI03A_FEI0048"
    $ current_voice = "voice/FEI03A_FEI0048.ogg"
    "菲利斯" "「这说的，就好像第一次看到一样呢」"
    $ stopvoc("TEN")
    play TEN "FEI03A_TEN0004"
    $ current_voice = "voice/FEI03A_TEN0004.ogg"
    "天王寺" "「恩？」"
    $ stopvoc("FEI")
    play FEI "FEI03A_FEI0049"
    $ current_voice = "voice/FEI03A_FEI0049.ogg"
    "菲利斯" "「以为我们不知道吗。尾行的事情，还有怪谈计划的事情」"
    "这么说着，他开始用他的手敲起了他亮得晃眼的光头。"

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='TEN')",DynamicDisplayable(mouthanime,"TEN_ASA03"),"True","lh/TEN_ASA03a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("TEN")
    play TEN "FEI03A_TEN0005"
    $ current_voice = "voice/FEI03A_TEN0005.ogg"
    "天王寺" "「暴露了吗。……嘛，编造传言什么的，是做过头了点啊。但是如果结果是好的话，你不能帮忙配合一下吗」"
    $ stopvoc("FEI")
    play FEI "FEI03A_FEI0050"
    $ current_voice = "voice/FEI03A_FEI0050.ogg"
    "菲利斯" "「那是应该在会议上说的话吧」"

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='TEN')",DynamicDisplayable(mouthanime,"TEN_ASA01"),"True","lh/TEN_ASA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("TEN")
    play TEN "FEI03A_TEN0006"
    $ current_voice = "voice/FEI03A_TEN0006.ogg"
    "天王寺" "「……是这样呢」"
    "天王寺先生露出了困扰的表情，摸着看着事态发展的绹酱的头。就好像在说不要担心我们会吵起来一样。"
    "他就那么望了我一眼。"
    "是在寻找说服我的话呢，还是在和平时一样通过转变话题来蒙混过去呢。"
    "——答案是后者。"
    $ stopvoc("TEN")
    play TEN "FEI03A_TEN0007"
    $ current_voice = "voice/FEI03A_TEN0007.ogg"
    "天王寺" "「说起来……喂打工的」"
    "将矛头指向了阿万音。"
    $ stopvoc("TEN")
    play TEN "FEI03A_TEN0008"
    $ current_voice = "voice/FEI03A_TEN0008.ogg"
    "天王寺" "「你真的今天就要不干了啊？」"
    "……诶？"
    $ stopvoc("TEN")
    play TEN "FEI03A_TEN0009"
    $ current_voice = "voice/FEI03A_TEN0009.ogg"
    "天王寺" "「最开始说好的日子就是今天倒是……看在绹的份上，再干几天怎么样啊？」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh7 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_ESA03"),"True","lh/SUZ_ESA03a~ipad.png") at left as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='TEN')",DynamicDisplayable(mouthanime,"TEN_ASA01"),"True","lh/TEN_ASA01a~ipad.png") at right as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    play bgm "BGM20"
    $ stopvoc("SUZ")
    play SUZ "FEI03A_SUZ0050"
    $ current_voice = "voice/FEI03A_SUZ0050.ogg"
    "铃羽" "「等，等等店长！」"
    $ stopvoc("TEN")
    play TEN "FEI03A_TEN0010"
    $ current_voice = "voice/FEI03A_TEN0010.ogg"
    "天王寺" "「虽然不知道你要离开秋叶原去什么地方，但是不那么赶也没关系吧？」"
    window hide



    $ loadBG(2,"BG05A1")





    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_EMA03"),"True","lh/SUZ_EMA03a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    "我下意识地看向阿万音。"
    "但是她慌张地移开视线。"
    "难道说，又是……谎言！？"
    window hide
    play se "SGSE063"




    $ loadBG(2,"BG05A1")

    hide lh7 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_ESA03"),"True","lh/SUZ_ESA03a~ipad.png") at left as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='TEN')",DynamicDisplayable(mouthanime,"TEN_ASA03"),"True","lh/TEN_ASA03a~ipad.png") at right as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    $ stopvoc("TEN")
    play TEN "FEI03A_TEN0011"
    $ current_voice = "voice/FEI03A_TEN0011.ogg"
    "天王寺" "「至少暑假这段时间……不对，再多做一周就好啦」"
    "阿万音只是看着地面。"
    "她避开我的视线，不让我察觉到她的真实心情。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_ESB04"),"True","lh/SUZ_ESB04a~ipad.png") as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "FEI03A_SUZ0051"
    $ current_voice = "voice/FEI03A_SUZ0051.ogg"
    "铃羽" "「……不行的哦，店长」"
    $ stopvoc("TEN")
    play TEN "FEI03A_TEN0012"
    $ current_voice = "voice/FEI03A_TEN0012.ogg"
    "天王寺" "「为什么呀」"
    $ stopvoc("SUZ")
    play SUZ "FEI03A_SUZ0052"
    $ current_voice = "voice/FEI03A_SUZ0052.ogg"
    "铃羽" "「我今天不走不行的。……就算再怎么迟，最多到明天凌晨」"
    $ stopvoc("TEN")
    play TEN "FEI03A_TEN0013"
    $ current_voice = "voice/FEI03A_TEN0013.ogg"
    "天王寺" "「真是没法理解啊」"
    $ stopvoc("SUZ")
    play SUZ "FEI03A_SUZ0053"
    $ current_voice = "voice/FEI03A_SUZ0053.ogg"
    "铃羽" "「真的……不行啊」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='TEN')",DynamicDisplayable(mouthanime,"TEN_ASA01"),"True","lh/TEN_ASA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("TEN")
    play TEN "FEI03A_TEN0014"
    $ current_voice = "voice/FEI03A_TEN0014.ogg"
    "天王寺" "「这样啊……真遗憾」"
    $ stopvoc("FEI")
    play FEI "FEI03A_FEI0051"
    $ current_voice = "voice/FEI03A_FEI0051.ogg"
    "菲利斯" "「为什么……」"
    $ stopvoc("FEI")
    play FEI "FEI03A_FEI0052"
    $ current_voice = "voice/FEI03A_FEI0052.ogg"
    "菲利斯" "「为什么不告诉我」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_ESA03"),"True","lh/SUZ_ESA03a~ipad.png") as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "FEI03A_SUZ0054"
    $ current_voice = "voice/FEI03A_SUZ0054.ogg"
    "铃羽" "「…………」"
    $ stopvoc("FEI")
    play FEI "FEI03A_FEI0053"
    $ current_voice = "voice/FEI03A_FEI0053.ogg"
    "菲利斯" "「不是一直在我身边的吗」"
    $ stopvoc("TEN")
    play TEN "FEI03A_TEN0015"
    $ current_voice = "voice/FEI03A_TEN0015.ogg"
    "天王寺" "「呐，小猫娘……」"
    $ stopvoc("FEI")
    play FEI "FEI03A_FEI0054"
    $ current_voice = "voice/FEI03A_FEI0054.ogg"
    "菲利斯" "「你也请先安静一下！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='TEN')",DynamicDisplayable(mouthanime,"TEN_ASA03"),"True","lh/TEN_ASA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("TEN")
    play TEN "FEI03A_TEN0016"
    $ current_voice = "voice/FEI03A_TEN0016.ogg"
    "天王寺" "「哦……哦唔……」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh7 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_EMA03"),"True","lh/SUZ_EMA03a~ipad.png") at center as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FEI")
    play FEI "FEI03A_FEI0055"
    $ current_voice = "voice/FEI03A_FEI0055.ogg"
    "菲利斯" "「为什么……」"
    $ stopvoc("FEI")
    play FEI "FEI03A_FEI0056"
    $ current_voice = "voice/FEI03A_FEI0056.ogg"
    "菲利斯" "「明明告诉我就好了……」"
    $ stopvoc("SUZ")
    play SUZ "FEI03A_SUZ0055"
    $ current_voice = "voice/FEI03A_SUZ0055.ogg"
    "铃羽" "「……我说不出口」"
    $ stopvoc("SUZ")
    play SUZ "FEI03A_SUZ0056"
    $ current_voice = "voice/FEI03A_SUZ0056.ogg"
    "铃羽" "「是我的任务啊……。不是今天的话就赶不上回收的日子了」"
    $ stopvoc("FEI")
    play FEI "FEI03A_FEI0057"
    $ current_voice = "voice/FEI03A_FEI0057.ogg"
    "菲利斯" "「任务？　那是什么……我们明明在说认真的」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_EMB01"),"True","lh/SUZ_EMB01a~ipad.png") as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "FEI03A_SUZ0057"
    $ current_voice = "voice/FEI03A_SUZ0057.ogg"
    "铃羽" "「……诶？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_EMB04"),"True","lh/SUZ_EMB04a~ipad.png") as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "FEI03A_SUZ0058"
    $ current_voice = "voice/FEI03A_SUZ0058.ogg"
    "铃羽" "「……等等，也就是说你也不相信我说的吗！？」"
    $ stopvoc("FEI")
    play FEI "FEI03A_FEI0058"
    $ current_voice = "voice/FEI03A_FEI0058.ogg"
    "菲利斯" "「那，那个和这个是不同的……」"
    $ stopvoc("SUZ")
    play SUZ "FEI03A_SUZ0059"
    $ current_voice = "voice/FEI03A_SUZ0059.ogg"
    "铃羽" "「有什么不同的，Ｂｏｓｓ也……留未穗最后也还是没有相信我说的话啊」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_EMB02"),"True","lh/SUZ_EMB02a~ipad.png") as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "FEI03A_SUZ0060"
    $ current_voice = "voice/FEI03A_SUZ0060.ogg"
    "铃羽" "「……好悲伤啊」"
    $ stopvoc("FEI")
    play FEI "FEI03A_FEI0059"
    $ current_voice = "voice/FEI03A_FEI0059.ogg"
    "菲利斯" "「那我相信不就好了吗？」"
    $ stopvoc("SUZ")
    play SUZ "FEI03A_SUZ0061"
    $ current_voice = "voice/FEI03A_SUZ0061.ogg"
    "铃羽" "「不是那个问题」"
    $ stopvoc("FEI")
    play FEI "FEI03A_FEI0060"
    $ current_voice = "voice/FEI03A_FEI0060.ogg"
    "菲利斯" "「那我要怎么做才能让你留下来啊」"
    $ stopvoc("SUZ")
    play SUZ "FEI03A_SUZ0062"
    $ current_voice = "voice/FEI03A_SUZ0062.ogg"
    "铃羽" "「那是不现实的」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_EMB04"),"True","lh/SUZ_EMB04a~ipad.png") as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "FEI03A_SUZ0063"
    $ current_voice = "voice/FEI03A_SUZ0063.ogg"
    "铃羽" "「好奇怪啊，今天的Ｂｏｓｓ。又是因为服装的关系？」"
    $ stopvoc("FEI")
    play FEI "FEI03A_FEI0061"
    $ current_voice = "voice/FEI03A_FEI0061.ogg"
    "菲利斯" "「……！」"
    "我下意识地看了一下制服。"
    "……不能理解。但是……"
    $ stopvoc("FEI")
    play FEI "FEI03A_FEI0062"
    $ current_voice = "voice/FEI03A_FEI0062.ogg"
    "菲利斯" "「好像组合穿错了呢」"
    "并没有，穿错……"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_EMA06"),"True","lh/SUZ_EMA06a~ipad.png") as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "FEI03A_SUZ0064"
    $ current_voice = "voice/FEI03A_SUZ0064.ogg"
    "铃羽" "「呐留未穂……」"
    $ stopvoc("FEI")
    play FEI "FEI03A_FEI0063"
    $ current_voice = "voice/FEI03A_FEI0063.ogg"
    "菲利斯" "「请不要叫我那个名字」"
    window hide

    stop bgm 
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    "我大声吼道。"
    "脑海中一片混乱。什么话都脱口而出，无法压制住。"
    window hide
    play se "SGSE181"
    hide screen phoneSD1



    $ loadBG(0,"BG_BLACK")

    hide screen phonebtn
    "我不知所措地从那里跑开了——"
    window hide



    $ loadBG(0,"BG72A")
    $ RcvMail(279)
    $ RcvMail(280)

    play bgm "FD2BGM05"

    hide screen phonebtn
    hide screen phoneSD1
    "然后我就立刻回到家里，把自己关了起来。"
    "为什么事情会变成这个样子啊……"
    "要怎么才能和阿万音和好啊……"
    "脱下了黑猫的制服之后，我就那么躺在床上，一直一直思考着这个问题。"
    play se "SGSE335"

    $ stopvoc("Y13")
    play KUR "FEI03A_Y130000"
    $ current_voice = "voice/FEI03A_Y130000.ogg"
    "黑木" "「大小姐，您醒着吗大小姐」"
    "管家黑木在门口叫我。"
    "从我把自己关在房间里开始，不时来观察一下我的样子。"
    $ stopvoc("Y13")
    play KUR "FEI03A_Y130001"
    $ current_voice = "voice/FEI03A_Y130001.ogg"
    "黑木" "「虽然您的怒火尚未平息，但请也不要搞坏了身体，来吃点东西吧。」"
    "声音中掺杂着对主人的抱歉心情。"
    "为什么黑木也会感到抱歉啊……"
    "那是因为黑木也参加了怪谈计划吧。"
    "天王寺先生说为了让我吃一惊所以让他对我保密。"
    "他毫不怀疑地对我撒了谎。"
    "我知道他没有恶意。但是我很难原谅他。"
    "我又一次将自己关起来，坠入了没有出口的蚁蛉地狱。（注：蚁蛉幼虫会在沙地上制造出漏斗状的陷阱（蚁蛉地狱），好让蚂蚁之类的动物掉落下来并吃掉。）"
    $ stopvoc("Y13")
    play KUR "FEI03A_Y130002"
    $ current_voice = "voice/FEI03A_Y130002.ogg"
    "黑木" "「我在房间外面准备简单的食物。不用担心我的问题，请您多加保重……」"
    "如果在这个点不出去的话，也许就再也没法和好了……这么想着，我握住了门把手。但是……"
    window hide
    play se "SGSE374"


    stop se
    $ stopvoc("Y13")
    play KUR "FEI03A_Y130003"
    $ current_voice = "voice/FEI03A_Y130003.ogg"
    "黑木" "「……您好，这里是秋叶家。啊啊天王寺先生……」"
    "天王寺……先生？"
    $ stopvoc("Y13")
    play KUR "FEI03A_Y130004"
    $ current_voice = "voice/FEI03A_Y130004.ogg"
    "黑木" "「……不，不在我们这边、……好的、好的……」"
    "……果然黑木也是「大人(那边)」的人。"
    "抱歉的心情，因为再次的背叛变成了失望。"
    "讨厌……我在变成自己所厌恶的人类……"
    "束手无策的绝望感。为什么会变成这样啊……"
    "吸引住我的视线的是，我脱下来的紧身衣。"
    $ stopvoc("FEI")
    play FEI "FEI03A_FEI0064"
    $ current_voice = "voice/FEI03A_FEI0064.ogg"
    "菲利斯" "「黑猫……」"
    "是啊。让我改变的是，这件紧身衣。"
    window hide
    $ loadBG(0,"IBG005A",png=True)



    "带着护目镜的时候心情高涨，感觉什么都做得到一样。"
    "能够按照自己的本心行事。"
    "就好像脱下了留未穗和菲利斯的面具一样清爽。"
    "我究竟是什么时候开始带上名为“我自己”的面具的呢……"
    window hide
    hide background-png 
    with dissolve


    "但是注意到这一点的代价就是。"
    "我失去了对自己来说最重要的存在。"
    "这次又是，我用自己的双手……"
    $ targetmailid = gc["ScriptMacros"]["FM_FEI03A_RECV_FEI02"]
    if phonemailring!= "":
        play se phonemailring
    if persistent.skipmail==False:
        $ renpy.choice_for_skipping()
    if targetmailid != "":
        $ RcvMail(targetmailid)
        $ targetmailid=""
    "望着窗外的夜景，突然手机的电话铃声引起了我的注意。"
    "但是现在没有那样的心情。"
    $ targetmailid = gc["ScriptMacros"]["FM_FEI03A_RECV_FEI03"]
    if phonemailring!= "":
        play se phonemailring
    if persistent.skipmail==False:
        $ renpy.choice_for_skipping()
    if targetmailid != "":
        $ RcvMail(targetmailid)
        $ targetmailid=""
    "像是要告诉我什么的样子，手机又响了起来，我只好无奈地取出手机。"
    window hide

    stop bgm 
    show screen phonebtn
    hide screen phonebtn
    hide screen phonebtn2



    $ targetmailid = gc["ScriptMacros"]["FM_FEI03A_RECV_FEI02"]
    $ RcvMail(targetmailid)






    $ targetmailid = gc["ScriptMacros"]["FM_FEI03A_RECV_FEI03"]
    $ RcvMail(targetmailid)
    call read_last_mail (1)
    call hide_phone
    call read_last_mail (0)




    call hide_phone

    "说起来……刚才的电话，天王寺先生打来的啊……"
    window hide

    $ stopvoc("Y13")
    play KUR "FEI03A_Y130005"
    $ current_voice = "voice/FEI03A_Y130005.ogg"
    "……不，不在我们这边。"
    window hide

    play bgm "BGM23"
    $ stopvoc("FEI")
    play FEI "FEI03A_FEI0065"
    $ current_voice = "voice/FEI03A_FEI0065.ogg"
    "菲利斯" "「…………」"
    "有不好的预感。"
    window hide


    $ loadBG(2,"IBG005A",png=True)






    "我从床上站起来，把手伸向了黑猫的制服。"
    window hide




    hide background-png 
    $ loadBG(3,"BG_WHITE")

    hide lh3 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_ALA02"),"True","lh/SUZ_ALA02a~ipad.png") at center as lh3 zorder (10-3) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)
    hide lh3 

















    hide lh3 
    $ loadBG(0,"BG72A")
    "那时，阿万音的笑容在脑海中不经意间掠过。"
    $ stopvoc("FEI")
    play FEI "FEI03A_FEI0066"
    $ current_voice = "voice/FEI03A_FEI0066.ogg"
    "菲利斯" "「…………」"
    window hide
    with dissolve




















    "所以我把制服放在身后，走向衣柜，拿了一套平时的服装。"

    hide screen phoneSD1
    window hide



    hide screen phonebtn
    scene expression Solid("000000")  with fade
    return
