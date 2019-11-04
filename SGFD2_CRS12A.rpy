label SGFD2_CRS12A:
    window hide


    $ loadBG(0,"BG26A")

    play bgm "BGM26"

    $ date="8/14"
    $ day = "SAT"
    show screen phonebtn
    show screen phoneSD1

    "第二天一早，充分休息后醒来，我简单地整理了一下，来到了客厅。"
    "客厅里的幸高叔叔似乎是整晚在不停地打电话，显得有些憔悴，在旁边辅佐的黑木先生也在。"
    "大概是为了也从别的渠道获取情报，巨大的液晶电视正在播放着新闻节目。"

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='FPP')",DynamicDisplayable(mouthanime,"FPP_ASA03"),"True","lh/FPP_ASA03a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FPP")
    play FPP "CRS12A_FPP0000"
    $ current_voice = "voice/CRS12A_FPP0000.ogg"
    "菲利斯父亲" "「啊，红莉栖酱。早。」"
    $ stopvoc("CRS")
    play CRS "CRS12A_CRS0000"
    $ current_voice = "voice/CRS12A_CRS0000.ogg"
    "红莉栖" "「叔叔早安。那个……情况怎么样了？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='FPP')",DynamicDisplayable(mouthanime,"FPP_ASA02"),"True","lh/FPP_ASA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FPP")
    play FPP "CRS12A_FPP0001"
    $ current_voice = "voice/CRS12A_FPP0001.ogg"
    "菲利斯父亲" "「……不是，特别好呢。」"
    "幸高叔叔经过整晚的交涉和调兵遣将，对Ｒｏｕｎｄｅｒ的组织结构有了相当程度的切入。"
    "似乎已经对一定数量的低层成员和其负责中枢之间联络的特务有了掌握。"
    "虽然对其中的部分成员成功实施了抓捕，但最重要的名为ＦＢ的人物，及真由理和桥田的情报都没有获得。"
    $ stopvoc("FPP")
    play FPP "CRS12A_FPP0002"
    $ current_voice = "voice/CRS12A_FPP0002.ogg"
    "菲利斯父亲" "「看来，这回的行动对他们而言有着超乎想像的重要价值。从情报的隐蔽和行动的迅速就能看出来。」"
    "幸高叔叔的面前摊放着好多页文件和地图，上面有好几个地方做了红色的记号。"
    "描了一眼地图，从日本到远东·东南亚，美国，欧洲都有，不仅图域广阔，还有不少详细的信息。"
    "看来他已经对图中的几个地方进行了预测，甚至已经进行了实际调查。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='FPP')",DynamicDisplayable(mouthanime,"FPP_ASA01"),"True","lh/FPP_ASA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FPP")
    play FPP "CRS12A_FPP0003"
    $ current_voice = "voice/CRS12A_FPP0003.ogg"
    "菲利斯父亲" "「一般来说做到这种地步时，对方要么进行反击，要么该提出交涉了。」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    "据叔叔的预测，这回的行动，恐怕是他们计划之中优先度极高的项目。"
    "所谓组织，有时会为了优先目的，把其它的损害全部视为必要的经费支出而舍弃掉。"
    "面对幸高叔叔对Ｒｏｕｎｄｅｒ采取的行动，对方的回应就如上所述。"
    "确实，对于Ｒｏｕｎｄｅｒ的上级组织ＳＥＲＮ和支配他们的３００人委员会而言，没有什么比独占时间机器更重要的了。"
    "如果可以支配时间，操纵过去，可以把计划重新来过，那这个世界上将没有不可能。"
    "正如之前所说过的，这是等同于非人之神的力量。"
    "为什么要把这力量给自己之外的人呢？"
    "如果他们把自己定义为世界的支配者，会是这副姿态也是理所当然的了。"
    "问题在于，这对现在的我们来说是相当不利的状况。"
    "幸高叔叔看起来也是快有心无力了。"

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='FPP')",DynamicDisplayable(mouthanime,"FPP_ASA01"),"True","lh/FPP_ASA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "CRS12A_CRS0001"
    $ current_voice = "voice/CRS12A_CRS0001.ogg"
    "红莉栖" "「……叔叔。」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='FPP')",DynamicDisplayable(mouthanime,"FPP_ASA02"),"True","lh/FPP_ASA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FPP")
    play FPP "CRS12A_FPP0004"
    $ current_voice = "voice/CRS12A_FPP0004.ogg"
    "菲利斯父亲" "「虽然一直顶着压力继续调查，却没什么进展。就这么与３００人委员会正面对抗实在不是明智之举啊……」"
    "话虽这么说，但从幸高叔叔的表情看，这一点也已在他的预料之内。"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='FPP')",DynamicDisplayable(mouthanime,"FPP_ASA02"),"True","lh/FPP_ASA02a~ipad.png") at left as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_CSC04"),"True","lh/FEI_CSC04a~ipad.png") at right as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FEI")
    play FEI "CRS12A_FEI0000"
    $ current_voice = "voice/CRS12A_FEI0000.ogg"
    "菲利斯" "「爸爸……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='FPP')",DynamicDisplayable(mouthanime,"FPP_ASA03"),"True","lh/FPP_ASA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FPP")
    play FPP "CRS12A_FPP0005"
    $ current_voice = "voice/CRS12A_FPP0005.ogg"
    "菲利斯父亲" "「啊，留未穗。早。」"
    "菲利斯进了客厅，似乎她从幸高叔叔的神情中就已经把握了大体的情况。"
    "她坐到叔叔的旁边，贴在身旁挽住他的手臂。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='FPP')",DynamicDisplayable(mouthanime,"FPP_ASA01"),"True","lh/FPP_ASA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FPP")
    play FPP "CRS12A_FPP0006"
    $ current_voice = "voice/CRS12A_FPP0006.ogg"
    "菲利斯父亲" "「……让你操心了。不过，爸爸没问题的。」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_CSA03"),"True","lh/FEI_CSA03a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FEI")
    play FEI "CRS12A_FEI0001"
    $ current_voice = "voice/CRS12A_FEI0001.ogg"
    "菲利斯" "「嗯……」"
    "菲利斯复杂的感情浮在了脸上。"
    "她对真由理、桥田和冈部都担心得不得了。另一方面，又为勉强自己的幸高叔叔担心……"
    "幸高叔叔大概是那类会不顾一切硬干下去的人吧。为了女儿的朋友，为了心爱的秋叶原，有着不能退让的部分。"
    "所以菲利斯在担心幸高叔叔会勉强自己。"
    "可同时，如果幸高叔叔不这样做，大概就真的没办法救真由理和桥田了。"
    "就这样考虑着，菲利斯陷入了两难境地。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_CSC03"),"True","lh/FEI_CSC03a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FEI")
    play FEI "CRS12A_FEI0002"
    $ current_voice = "voice/CRS12A_FEI0002.ogg"
    "菲利斯" "「…………」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='FPP')",DynamicDisplayable(mouthanime,"FPP_ASA03"),"True","lh/FPP_ASA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FPP")
    play FPP "CRS12A_FPP0007"
    $ current_voice = "voice/CRS12A_FPP0007.ogg"
    "菲利斯父亲" "「……谢谢你，留未穗。」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='FPP')",DynamicDisplayable(mouthanime,"FPP_ASA01"),"True","lh/FPP_ASA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    "幸高叔叔一边说一边摸摸菲利斯的头，然后准备继续给下一个交涉对象打电话。就在这时──"
    "液晶电视里，播出一条新闻。"
    hide screen phoneSD1
    window hide


    $ loadBG(2,"IBG048A")



    hide screen phonebtn
    $ stopvoc("X01")
    play KUR "CRS12A_X010000"
    $ current_voice = "voice/CRS12A_X010000.ogg"
    "新闻主播" "「下条新闻。本日黎明，在葛西临海公园附近的海边……」"
    $ stopvoc("X01")
    play KUR "CRS12A_X010001"
    $ current_voice = "voice/CRS12A_X010001.ogg"
    "新闻主播" "「前来钓鱼的公司职员发现一辆小型面包车沉于海中。」"
    "画面中出现了东京湾的影像。"
    "接下来，一辆白色箱型车被吊车吊起。"
    "慢慢从水中吊起的面包车，被运到了被蓝色警戒带围住的港口路上。"

    stop bgm 
    "不知怎么地，这幅景象让我感到一股难以言喻的不安。"
    "——讨厌。是神经过敏了吧。 不快的联想，涌上心头。"
    "不愿想下去，却控制不住。"
    window hide


    $ loadBG(2,"IBG048B")



    $ stopvoc("X01")
    play KUR "CRS12A_X010002"
    $ current_voice = "voice/CRS12A_X010002.ogg"
    "新闻主播" "「车内发现一具约十几岁女性的遗体，警察当局正在紧急确认身份。」"
    "电视机里传达着机械般无感情的播报声。然后画面中出现了车内的遗留品。"
    $ stopvoc("CRS")
    play CRS "CRS12A_CRS0002"
    $ current_voice = "voice/CRS12A_CRS0002.ogg"
    "红莉栖" "「……！」"
    $ stopvoc("FEI")
    play FEI "CRS12A_FEI0003"
    $ current_voice = "voice/CRS12A_FEI0003.ogg"
    "菲利斯" "「……！」"
    "我和菲利斯无声地站了起来。"
    "看到这难以置信的东西，我眼睛瞪得滚圆。"
    "心跳声大得在耳边作响。"
    $ stopvoc("CRS")
    play CRS "CRS12A_CRS0003"
    $ current_voice = "voice/CRS12A_CRS0003.ogg"
    "红莉栖" "「怎么会……怎么会……」"
    "液晶电视画面中所显示的，是我认识的帽子和绿色的手机……无论哪个都应该是我们所熟知的“某人”持有的东西。"
    $ stopvoc("FEI")
    play FEI "CRS12A_FEI0004"
    $ current_voice = "voice/CRS12A_FEI0004.ogg"
    "菲利斯" "「骗，骗人的……骗人的吧……」"
    "菲利斯像小孩子一样摇着头。"
    "不想承认……不可能承认的……"
    "我本应做好了觉悟的。在听过冈部的话之后，就应该预料到事情会是如此。"
    "但是，我们没法接受。"
    "这种事，怎么可能接受啊。"
    "无论是我还是菲利斯，就这么僵硬地盯着画面。——所以，没有注意到。"
    $ stopvoc("OKA")
    play OKA "CRS12A_OKA0000"
    $ current_voice = "voice/CRS12A_OKA0000.ogg"
    "伦太郎？" "「真由理？」"
    window hide



    $ loadBG(2,"BG26A")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA07"),"True","lh/OKA_ASA07a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    show screen phoneSD1
    show screen phonebtn
    "“他”是什么时候起来的……什么时候，来到了客厅……！"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA06"),"True","lh/OKA_ASA06a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "CRS12A_OKA0001"
    $ current_voice = "voice/CRS12A_OKA0001.ogg"
    "伦太郎" "「真由理！！！！！！！！」"
    play bgm "BGM24"
    $ stopvoc("CRS")
    play CRS "CRS12A_CRS0004"
    $ current_voice = "voice/CRS12A_CRS0004.ogg"
    "红莉栖" "「冈部！」"
    "我听到背后的叫声后赶紧回头一看。"
    "站在那里的是，脸色比纸还苍白的冈部。"
    $ stopvoc("OKA")
    play OKA "CRS12A_OKA0002"
    $ current_voice = "voice/CRS12A_OKA0002.ogg"
    "伦太郎" "「真，真由里……真由理！ 真由理！ 真由理！！ 我，我……又！」"
    $ stopvoc("OKA")
    play OKA "CRS12A_OKA0003"
    $ current_voice = "voice/CRS12A_OKA0003.ogg"
    "伦太郎" "「啊啊啊，啊啊啊啊啊啊，哇啊啊啊啊啊啊─────────────！」"
    "双手抱着头，像忏悔般地跪在地上嚎哭起来的冈部。"
    "那如同灵魂被千刀万剐的悲鸣，让我第一次知道，原来人的惨叫声可以如此痛彻心扉。"
    "但同时这已是无可动摇的事实——无论再怎么不愿承认，我们重要的朋友已经死了。"
    "冈部的恸哭，正是真由理死亡的证明。"
    "直到刚才，或许我还能用“遗留品和车内的遗体全都是伪装的”来欺骗自己。"
    "仿佛只要不是亲眼所见，就可以拒绝承认真由理的死亡。"
    "可到头来这只不过是愚蠢的自欺欺人罢了。作为本应追求真实的研究者，这完全是开倒车的行为啊。"
    hide screen phoneSD1
    window hide


    $ loadBG(2,"IBG048B")



    hide screen phonebtn
    "是呢。在电视中看到帽子和手机的那一刻，我就已经明白了。"
    "重要的伙伴，朋友……她已经不在这个世界上了，已经再也不能见面了。"
    "但是，我不想承认啊。只是如此而已。"
    window hide


    $ loadBG(2,"BG_BLACK",trans=ImageDissolve(im.Scale("mask/mask15.png",1024,576),1,reverse=True))





    "所以对自己说谎……想欺骗自己……不愿看清事实。"
    "但是——那只是再肤浅不过的愚蠢行为。"
    window hide


    $ loadBG(2,"BG26A")



    show screen phoneSD1
    show screen phonebtn
    "现实就在眼前。真相就在这里。"
    "清醒吧。理解吧。承认吧。"
    "已经不在了……真由理已经不在了啊……！"
    $ stopvoc("OKA")
    play OKA "CRS12A_OKA0004"
    $ current_voice = "voice/CRS12A_OKA0004.ogg"
    "伦太郎" "「哦哦哦，哦哦……啊啊啊──我，我……为什么！ 为什么！ 为什么救不了她！」"
    "但是这种时候，我已经不能再任由自己沉浸在失去朋友的悲伤中了。"
    "因为无论何时，我都要作为一名有修养的研究者，来应对眼前的情况……而且此时，我的眼前有一个远比我更悲痛的身影。"
    $ stopvoc("CRS")
    play CRS "CRS12A_CRS0005"
    $ current_voice = "voice/CRS12A_CRS0005.ogg"
    "红莉栖" "「冈部！」"
    window hide



    $ loadBG(2,"BG26AS1")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ALD01"),"True","lh/OKA_ALD01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    "那就是正握拳敲打自己的头，流着泪，不断发出悲鸣的冈部……"
    "我抓住他的手，至少想制止住他伤害自己的行为，但冈部挣脱开了。"
    $ stopvoc("OKA")
    play OKA "CRS12A_OKA0005"
    $ current_voice = "voice/CRS12A_OKA0005.ogg"
    "伦太郎" "「为什么！ 为什么，是真由理？ 做出时间机器的是我！ 让我受天谴就行了！ 杀我不就行了吗！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ALD02"),"True","lh/OKA_ALD02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "CRS12A_OKA0006"
    $ current_voice = "voice/CRS12A_OKA0006.ogg"
    "伦太郎" "「为什么！ 为什么？ 为什么是真由理？」"
    "冈部面对着虚空，向不在场的Ｒｏｕｎｄｅｒ和ＳＥＲＮ不断地投去痛苦的质问。"
    "那饱含悲怆的叫喊，光是听着就仿佛已经要撕裂我的灵魂……"
    "当然，喊出这声音的人，比听者还要痛苦百倍。"
    $ stopvoc("CRS")
    play CRS "CRS12A_CRS0006"
    $ current_voice = "voice/CRS12A_CRS0006.ogg"
    "红莉栖" "「别这样，冈部！ 这样下去……再这样下去，冈部！ 你自己会坏掉的啊！」"
    "不要啊。"
    "不想看到喜欢的人这副样子。"
    "不想让喜欢的人如此痛苦。"
    "无论什么都行。我能帮他做什么吗？"
    "冈部是那么地痛苦，我怎么就救不了他呢？"
    "无力感和绝望感缠住了心。"
    "——这不仅是我的心情。冈部正在饱尝的苦痛也是如此吧。"
    "光是声音已经足以让人无法释怀的、极度苦闷的悲叫。"
    "我──还有菲利斯──能做的就只有抱住冈部。"
    "这已经是，无能为力的我们，唯一能做到的事了。"
    $ stopvoc("Y13")
    play KUR "CRS12A_Y130000"
    $ current_voice = "voice/CRS12A_Y130000.ogg"
    "黒木" "「失礼了……」"
    "黑木先生无声地伸出手。"
    play se "SGSE080"

    "顿时，冈部像昨天一样全身脱力倒了下去。"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve




    $ loadBG(2,"BG26A")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='KUR')",DynamicDisplayable(mouthanime,"KUR_ASA01"),"True","lh/KUR_ASA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    $ stopvoc("Y13")
    play KUR "CRS12A_Y130001"
    $ current_voice = "voice/CRS12A_Y130001.ogg"
    "黒木" "「让他这样连续睡着不是好事……但这样下去更加危险。」"
    $ stopvoc("CRS")
    play CRS "CRS12A_CRS0007"
    $ current_voice = "voice/CRS12A_CRS0007.ogg"
    "红莉栖" "「…………」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_CSC04"),"True","lh/FEI_CSC04a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FEI")
    play FEI "CRS12A_FEI0005"
    $ current_voice = "voice/CRS12A_FEI0005.ogg"
    "菲利斯" "「…………」"
    "我们只是无声地抱着冈部，连连摇头。"
    "这样的表情有些对不住黑木先生，但现在的我们连让冈部睡下的本事都没有。也根本没有提出异议的权利吧。"
    "我们就是这么无力。那一点微不足道的经验，还有被称为天才的才气──"
    "对现状来说没有任何用处。"
    "就像冈部救不了真由理，我救不了冈部。"
    "甚至没法帮他分担一点点负担。"
    "至少，如果有冈部的Ｒｅａｄｉｎｇ；ｓｔｅｉｎｅｒ，说不定我就能代替他使用时间跳跃机。"
    "但那也只是不可能办得到的任性吧。"
    $ stopvoc("CRS")
    play CRS "CRS12A_CRS0008"
    $ current_voice = "voice/CRS12A_CRS0008.ogg"
    "红莉栖" "「冈部……，冈部……冈部……」"
    "从刚才起，我就像冈部不停地念着真由理名字那样，不由自主地搂着冈部轻轻叫他的名字。"
    "我知道幸高叔叔和黑木先生正担心地看着我，可是我现在又还能做些什么呢。"


    stop bgm 




    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    "这时，手机忽然响了起来。"



    window hide
    hide screen phonebtn
    hide screen phonebtn2
    show screen phone(interact=False)

    "我习惯性地打开了手机。"
    "然后按下接听键。"





    $ stopvoc("CRS")
    play CRS "CRS12A_CRS0009"
    $ current_voice = "voice/CRS12A_CRS0009.ogg"
    "红莉栖" "「…………」"
    $ stopvoc("CRS")
    play CRS "CRS12A_CRS0010"
    $ current_voice = "voice/CRS12A_CRS0010.ogg"
    "红莉栖" "「……爸，爸爸」"

    $ stopvoc("NAK")
    play NAK "CRS12A_NAK0000"
    $ current_voice = "voice/CRS12A_NAK0000.ogg"
    "中钵" "「你又……」"

    hide screen phoneSD1
    window hide
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_CRS003A"]]["Check"]=True


    call hide_phone
    $ loadBG(2,"EV_CRS003A")



    hide screen phonebtn
    $ stopvoc("CRS")
    play CRS "CRS12A_CRS0011"
    $ current_voice = "voice/CRS12A_CRS0011.ogg"
    "红莉栖" "「拜托了！ 爸爸，救冈部！ 救救冈部！ 冈部……冈！ ……爸爸」"
    $ stopvoc("NAK")
    play NAK "CRS12A_NAK0001"
    $ current_voice = "voice/CRS12A_NAK0001.ogg"
    "中钵" "「什……？ 说，什么……」"
    $ stopvoc("CRS")
    play CRS "CRS12A_CRS0012"
    $ current_voice = "voice/CRS12A_CRS0012.ogg"
    "红莉栖" "「救救我！ 拜托了……我已经，已经……我，救不了冈部……救不了喜欢的人！」"
    "眼泪和哭声决堤而出。已经万念俱灰、被绝望包围的我，在听到爸爸声音的瞬间，最后一条防线也土崩瓦解。"
    "顾不上面对爸爸时的精神创伤和胆怯……在听到儿时爱着我、帮助我的爸爸的声音时，我再也忍不住了。"
    "爸爸被我的哭声惊呆了，似乎也没有了平时面对我时的责骂和愤怒……"
    "──不过这一点，我也是在很长一段时间后才注意到。"

    hide screen phoneSD1
    window hide
    scene expression Solid("000000")  with fade





    return
