label SGFD2_KYO01A:
    show expression Solid("000") as background 
    with fade
    $ loadBG(0,"TIT010")
    $ renpy.pause(delay=3,hard=True)
    show expression Solid("000") as background 
    with fade



    $ date="8/13"
    $ day = "FRI"
    call timeleap (fromtime=[8,13,19,56], totime=[8,13,15,56], fromday=[5])











    window hide


    $ loadBG(0,"BG01A")










    play se "SGSE054"



    play bgm "BGM25"
    hide screen phonebtn
    hide screen phoneSD1

    "一如既往的违和感。"
    "一如既往地，被不愉快的感觉所覆盖着。"
    $ stopvoc("OKA")
    play OKA "KYO01A_OKA0000"
    $ current_voice = "voice/KYO01A_OKA0000.ogg"
    "伦太郎" "「唔……唔唔唔……」"
    "下意识地发出了声音。"
    "我将右手中的手机放回口袋，用左手按住太阳穴。"
    $ stopvoc("OKA")
    play OKA "KYO01A_OKA0001"
    $ current_voice = "voice/KYO01A_OKA0001.ogg"
    "伦太郎" "「这里是……哪里？」"
    "我一边嚅嗫道，一边环顾四周。"
    window hide


    $ loadBG(2,"BG02A1")




    "…………"
    window hide


    $ loadBG(2,"BG03A4")




    "…………"
    show screen phonebtn
    show screen phoneSD1
    $ stopvoc("OKA")
    play OKA "KYO01A_OKA0002"
    $ current_voice = "voice/KYO01A_OKA0002.ogg"
    "伦太郎" "「研究所……。是研究所，啊……」"
    "一如既往的室内设置。"
    "一如既往的……一如既往的……"
    "但是……为什么我会觉得是一如既往的Ｌａｂ呢？"
    "为什么我会知道这一点呢？"
    "记忆十分混乱，无法判断。"
    "意识也时断时续的，无从依靠。"
    "开发室的桌子上，还是一如既往地陈设着被称为Ｘ６８０００(×六八)的古董ＣＲＴ显示器。"
    "显示器没有通电。"
    "我缓缓地走到了它之前，朝着黑黝黝的屏幕的内侧窥去。"
    $ stopvoc("OKA")
    play OKA "KYO01A_OKA0003"
    $ current_voice = "voice/KYO01A_OKA0003.ogg"
    "伦太郎" "「你是谁……？」"
    "我朝着显示器里倒映着的自己发问了。"
    $ stopvoc("OKA")
    play OKA "KYO01A_OKA0004"
    $ current_voice = "voice/KYO01A_OKA0004.ogg"
    "伦太郎" "「我是……冈部伦太郎。」"
    "谁那么说了。"
    "这么说的明显是我自己啊。"
    "但是无法消除心中微妙的违和感。"
    "感觉在那里的自己的脸庞，似乎有一种不是自己的感觉。"
    "明明就是自己的脸啊……"
    "明明脑袋里是很清楚这一点的……为何……"
    $ stopvoc("OKA")
    play OKA "KYO01A_OKA0005"
    $ current_voice = "voice/KYO01A_OKA0005.ogg"
    "伦太郎" "「你到底是谁……？」"
    "似乎是为了确认一般，我又问了一遍。"
    "得到的答案是这样的。"
    $ stopvoc("OKA")
    play OKA "KYO01A_OKA0006"
    $ current_voice = "voice/KYO01A_OKA0006.ogg"
    "伦太郎" "「不对。我不是冈部伦太郎。」"
    "声音自然地从嘴唇中漏出。"
    "就好像被谁操纵着一样……"
    $ stopvoc("OKA")
    play OKA "KYO01A_OKA0007"
    $ current_voice = "voice/KYO01A_OKA0007.ogg"
    "伦太郎" "「我是……吾之真名为……」"
    $ stopvoc("OKA")
    play OKA "KYO01A_OKA0008"
    $ current_voice = "voice/KYO01A_OKA0008.ogg"
    "伦太郎" "「凤凰院凶真！　唔哈哈哈哈哈！」"
    window hide






    "在发出这阵笑声的同时，我胸口里的那阵烦闷荡然无存了。"
    "一如既往威严满满的狂笑(Ｖｅｌｖｅｔ　Ｖｏｉｃｅ)回荡在耳边。"
    "是啊，一如既往的……什么都没有变。"
    "这里是未来道具研究所，通称“Ｌａｂ”的地方，而我就是“凤凰院凶真”冈部伦太郎。"
    "理所当然的现实。无须证明的定理。"
    window hide
    hide screen phonebtn
    hide screen phonebtn2
    show screen phone(interact=False)
    "我从口袋里取出手机，放在右耳边。"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_KIKAN"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_KIKAN"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_KIKAN"])
    $ stopvoc("OKA")
    play OKA "KYO01A_OKA0009"
    $ current_voice = "voice/KYO01A_OKA0009.ogg"
    "伦太郎" "「是我。受到了来自“{color=#f00}机关{/color}”的强烈电磁波攻击，但没事，我使用某种方法反射回去了」"
    $ stopvoc("OKA")
    play OKA "KYO01A_OKA0010"
    $ current_voice = "voice/KYO01A_OKA0010.ogg"
    "伦太郎" "「什——么，这不算什么大事了。和格鲁吉亚之启示(Ａｐｏｃａｌｙｐｓｅ　ｏｆ　Ｇｕｒｉａｎ)那种洗脑兵器比起来算不了什么。」"
    $ stopvoc("OKA")
    play OKA "KYO01A_OKA0011"
    $ current_voice = "voice/KYO01A_OKA0011.ogg"
    "伦太郎" "「无需担心，没有任何问题。……啊啊，明白了。Ｅｌ　Ｐｓｙ　Ｃｏｎｇｒｏｏ」"
    "真的吗……？"
    "真的没有任何问题，吗？"
    window hide
    call hide_phone

    "我又一次审视了四周。"
    window hide


    $ loadBG(2,"BG01A")



    "…………"
    window hide


    $ loadBG(2,"BG02A1")



    "…………"
    window hide


    $ loadBG(2,"BG03A4")



    "…………"
    window hide


    $ loadBG(2,"BG01A")



    "好微妙啊……为什么谁也不在？"
    window hide
    hide screen phonebtn
    hide screen phonebtn2
    show screen phone(interact=False)
    "又一次取出手机来确认日期。"
    "８月１３日星期五。时间是刚到１６点。"
    window hide
    call hide_phone

    "确实在这个时候桶子和红莉栖应该在Ｌａｂ啊……"
    "真由理呢……？真由理怎么样了？"
    "试着回溯了一下记忆，又捕捉到了那种奇妙的感觉。"
    hide screen phoneSD1
    window hide


    hide screen phonebtn
    "恩？为什么我会不知道今天是８月１３日？"
    "反而知道“在这个时间点红莉栖和桶子应该在这里”这一点？"
    "知道不该知道的事，而应该知道的事情却不知道……"
    "这种矛盾。违和感。一阵恶心的感觉。"
    "头脑中依然一片混沌，记忆十分模糊。"
    window hide




    show screen phonebtn
    show screen phoneSD1
    $ stopvoc("OKA")
    play OKA "KYO01A_OKA0012"
    $ current_voice = "voice/KYO01A_OKA0012.ogg"
    "伦太郎" "「没关系，没关系的。没有任何问题」"
    "就好像是在说给自己听一样，我走到了冰箱前面。"
    window hide


    $ loadBG(2,"BG02A1")



    "这种时候喝些智慧饮料最好不过了。"
    "那样的话，我灰色的脑细胞就会恢复活性，这一切很快就会水落石出吧。"
    play se "SGSE206"

    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_DOCPE"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_DOCPE"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_DOCPE"])
    "打开冰箱的门，我从里面取出了一罐{color=#f00}Ｄｒ．Ｐｅｐｐｅｒ{/color}。铁罐在我手里丁丁作响。"
    window hide
    play se "SGSE207"

    $ stopvoc("OKA")
    play OKA "KYO01A_OKA0013"
    $ current_voice = "voice/KYO01A_OKA0013.ogg"
    "伦太郎" "「咕……咕……咕……呼哈！」"

    stop bgm 
    "在吐气的同时，一股清爽的味道充满了我的鼻腔。"
    "Ｄｒ．Ｐｅｐｐｅｒ不会背叛我。"
    "然后我也没有做过背叛Ｄｒ．Ｐｅｐｐｅｒ的事。"
    "作为彼此的Ｄｏｃｔｏｒ的我与他之间，既是彼此的对手但又互相认同了对方的功绩因而萌发了真挚的友情！"
    "什么的，比起考虑这种怎样都好的事情，我走到边上的沙发旁坐了下去。"
    "在那个时刻，我的视线中出现了某样东西。"
    "它放在沙发前的桌子上。"
    window hide


    $ loadBG(2,"IBG023A")



    hide screen phonebtn
    $ stopvoc("OKA")
    play OKA "KYO01A_OKA0014"
    $ current_voice = "voice/KYO01A_OKA0014.ogg"
    "伦太郎" "「什么呀，这是……」"
    "封面写着『素描簿』。"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_RAINET"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_RAINET"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_RAINET"])
    "在上面画着似乎的是『{color=#f00}雷Ｎｅｔ翔{/color}』动画里面的角色，不知为何我发现了这一点。"
    "问题是“为什么它会在这里”。"
    "随便翻了翻，里面还有几十页其他的插图。"
    "应该是不一样的插图吧，每一张的角色和其他的都不一样。"
    $ stopvoc("OKA")
    play OKA "KYO01A_OKA0015"
    $ current_voice = "voice/KYO01A_OKA0015.ogg"
    "伦太郎" "「这里有这种东西吗……？」"
    "头的一角隐隐作痛。"
    "就像是为了冲走那痛苦一般，我又喝了一口胡椒博士。"
    "下一个瞬间，手机就响了起来。"


    $ targetmailid = gc["ScriptMacros"]["FM_KYO01A_RECV_ICH01"]
    if phonemailring!= "":
        play se phonemailring
    if persistent.skipmail==False:
        $ renpy.choice_for_skipping()
    if targetmailid != "":
        $ RcvMail(targetmailid)
        $ targetmailid=""
    $ targetmailid = gc["ScriptMacros"]["FM_KYO01A_RECV_ICH02"]
    if phonemailring!= "":
        play se phonemailring
    if persistent.skipmail==False:
        $ renpy.choice_for_skipping()
    if targetmailid != "":
        $ RcvMail(targetmailid)
        $ targetmailid=""
    $ targetmailid = gc["ScriptMacros"]["FM_KYO01A_RECV_ICH03"]
    if phonemailring!= "":
        play se phonemailring
    if persistent.skipmail==False:
        $ renpy.choice_for_skipping()
    if targetmailid != "":
        $ RcvMail(targetmailid)
        $ targetmailid=""
    window hide


    $ loadBG(2,"BG02A1")



    show screen phonebtn
    "左手拿着罐子，右手在口袋里翻找着电话。"

    window hide


    hide screen phonebtn
    hide screen phonebtn2
    show screen phone(interact=False)



    "打开手机后，发现了三封新邮件。"
    window hide
    $ targetmailid = gc["ScriptMacros"]["FM_KYO01A_RECV_ICH03"]


    "发送人全部是『ｉ_ｃｈａｉｎ_ｈｉｓ_ｓｎａｋｅ＠ｅｇｗｅｂ．ｎｅ．ｊｐ』。"
    "没见过的地址……"
    "显然在地址簿里没有登陆过。"
    "总有一种讨厌的感觉。"
    "发现了内心的躁动、"
    "掌心开始冒汗。"
    "我深深地呼吸了几次，用颤动的指尖按下了……打开按钮。"
    window hide
    call read_last_mail (id=0, p=True)
    call read_last_mail (id=2, p=True)
    call read_last_mail (id=1, p=True)




    $ targetmailid = gc["ScriptMacros"]["FM_KYO01A_RECV_ICH02"]






    $ targetmailid = gc["ScriptMacros"]["FM_KYO01A_RECV_ICH01"]







    window hide










    play se "SGSE208"
    $ stopvoc("OKA")
    play OKA "KYO01A_OKA0016"
    $ current_voice = "voice/KYO01A_OKA0016.ogg"
    "伦太郎" "「什么啊……。什么啊、这是……」"
    play bgm "BGM23"
    "不对，并不是不能理解。"
    "这明显是……"
    $ stopvoc("OKA")
    play OKA "KYO01A_OKA0017"
    $ current_voice = "voice/KYO01A_OKA0017.ogg"
    "伦太郎" "「恐吓信……」"
    $ stopvoc("OKA")
    play OKA "KYO01A_OKA0018"
    $ current_voice = "voice/KYO01A_OKA0018.ogg"
    "伦太郎" "「真由理被带走了……」"
    $ stopvoc("OKA")
    play OKA "KYO01A_OKA0019"
    $ current_voice = "voice/KYO01A_OKA0019.ogg"
    "伦太郎" "「被诱拐了！」"
    "这么说的时候——"
    window hide

    call hide_phone

    $ loadBG(0,"BG_BLACK")
    play se "SGSE024"


    hide screen phonebtn
    "玄关的门开了，"
    "虽然一瞬间我以为是敌人来袭所以转过了身子，但是并不是那样。"
    "看见了一张张悠闲的脸……"
    window hide


    $ loadBG(0,"BG01A")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASA01"),"True","lh/CRS_ASA01a~ipad.png") at left as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASB01"),"True","lh/DAR_ASB01a~ipad.png") at right as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    show screen phonebtn
    $ stopvoc("CRS")
    play CRS "KYO01A_CRS0000"
    $ current_voice = "voice/KYO01A_CRS0000.ogg"
    "红莉栖" "「我回来了——」"
    $ stopvoc("DAR")
    play DAR "KYO01A_DAR0000"
    $ current_voice = "voice/KYO01A_DAR0000.ogg"
    "至" "「呼，累死我了」"
    $ stopvoc("OKA")
    play OKA "KYO01A_OKA0020"
    $ current_voice = "voice/KYO01A_OKA0020.ogg"
    "伦太郎" "「你们到哪里去了啊！」"
    $ stopvoc("CRS")
    play CRS "KYO01A_CRS0001"
    $ current_voice = "voice/KYO01A_CRS0001.ogg"
    "红莉栖" "「到哪里去了……」"
    $ stopvoc("DAR")
    play DAR "KYO01A_DAR0001"
    $ current_voice = "voice/KYO01A_DAR0001.ogg"
    "至" "「出去买东西啊」"
    $ stopvoc("OKA")
    play OKA "KYO01A_OKA0021"
    $ current_voice = "voice/KYO01A_OKA0021.ogg"
    "伦太郎" "「买东西？」"
    $ stopvoc("CRS")
    play CRS "KYO01A_CRS0002"
    $ current_voice = "voice/KYO01A_CRS0002.ogg"
    "红莉栖" "「要进行开发评议会……叫这个名字的宴会，不是吗？」"
    $ stopvoc("DAR")
    play DAR "KYO01A_DAR0002"
    $ current_voice = "voice/KYO01A_DAR0002.ogg"
    "至" "「所以我就和牧濑氏去买了零食──」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASB04"),"True","lh/DAR_ASB04a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "KYO01A_DAR0003"
    $ current_voice = "voice/KYO01A_DAR0003.ogg"
    "至" "「喂，啊啊啊啊啊————————啊！！！」"
    "突然桶子咆哮起来。"
    "桶子将手上提着的袋子随手一扔，面无血色地向前冲去。"
    window hide


    $ loadBG(2,"BG02A1")



    "用两手捧住素描簿，肩膀不住地震动着。"
    $ stopvoc("DAR")
    play DAR "KYO01A_DAR0004"
    $ current_voice = "voice/KYO01A_DAR0004.ogg"
    "至" "「小、小、小、小、小冈伦……」"
    $ stopvoc("DAR")
    play DAR "KYO01A_DAR0005"
    $ current_voice = "voice/KYO01A_DAR0005.ogg"
    "至" "「这、这、这、这、这个……这个到底……」"
    "桶子将素描簿朝这边打开。"
    window hide


    $ loadBG(2,"IBG023B")



    hide screen phonebtn
    "映入眼帘的是，那被放佛要滴落下来的黑色液体浸满的纸张。"
    "纸张吸收了液体之后，变得皱巴巴的。"
    "怎么看都好像是刚才看到邮件的时候，不小心弄翻了胡椒博士的罐子。"
    "结果便是，那里的液体朝着素描簿……"
    $ stopvoc("DAR")
    play DAR "KYO01A_DAR0006"
    $ current_voice = "voice/KYO01A_DAR0006.ogg"
    "至" "「啊啊，啊啊，我重要的Ｓｋｅｂｏ……」"
    $ stopvoc("OKA")
    play OKA "KYO01A_OKA0022"
    $ current_voice = "voice/KYO01A_OKA0022.ogg"
    "伦太郎" "「Ｓｋｅｂｏ？」"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_JOKO"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_JOKO"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_JOKO"])
    $ stopvoc("DAR")
    play DAR "KYO01A_DAR0007"
    $ current_voice = "voice/KYO01A_DAR0007.ogg"
    "至" "「当然就是在说这个素描簿咯{color=#f00}常考{/color}！」"
    window hide



    $ loadBG(2,"BG02A1")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASB06"),"True","lh/DAR_ASB06a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    show screen phonebtn
    $ stopvoc("DAR")
    play DAR "KYO01A_DAR0008"
    $ current_voice = "voice/KYO01A_DAR0008.ogg"
    "至" "「啊啊，完蛋了……。彻底完蛋了」"
    $ stopvoc("DAR")
    play DAR "KYO01A_DAR0009"
    $ current_voice = "voice/KYO01A_DAR0009.ogg"
    "至" "「未来道具研究所，关闭通知」"
    $ stopvoc("OKA")
    play OKA "KYO01A_OKA0023"
    $ current_voice = "voice/KYO01A_OKA0023.ogg"
    "伦太郎" "「那是，什么意思……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA05"),"True","lh/DAR_ASA05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "KYO01A_DAR0010"
    $ current_voice = "voice/KYO01A_DAR0010.ogg"
    "至" "「就不需要详细说明了吧。小冈伦明明是明白的」"
    "虽然更加想问怎么回事了……但只是想想。"
    "那种事怎么都好了。"
    "啊啊，是啊，真的怎样都好了！"
    "现在比起那个——！"
    $ stopvoc("OKA")
    play OKA "KYO01A_OKA0024"
    $ current_voice = "voice/KYO01A_OKA0024.ogg"
    "伦太郎" "「呐，桶子，素描簿的事情非常抱歉。在那之前先听我说」"
    $ stopvoc("OKA")
    play OKA "KYO01A_OKA0025"
    $ current_voice = "voice/KYO01A_OKA0025.ogg"
    "伦太郎" "「不对，直接给你们看更快吧。克里斯提娜也看下……」"
    hide screen phoneSD1
    window hide
    call hide_phone

    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    hide screen phonebtn
    "我将手机的收件箱打开，然后把手机递了过去。"
    "桶子和红莉栖两人肩并肩看着手机的屏幕。"
    "脸色逐渐变得苍白，这也是难免的。"
    "两个人目瞪口呆地说道。"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASC04"),"True","lh/CRS_ASC04a~ipad.png") at left as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASB04"),"True","lh/DAR_ASB04a~ipad.png") at right as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "KYO01A_DAR0011"
    $ current_voice = "voice/KYO01A_DAR0011.ogg"
    "至" "「这是说……」"
    $ stopvoc("CRS")
    play CRS "KYO01A_CRS0003"
    $ current_voice = "voice/KYO01A_CRS0003.ogg"
    "红莉栖" "「真由理被诱拐了吗！？」"
    $ stopvoc("OKA")
    play OKA "KYO01A_OKA0026"
    $ current_voice = "voice/KYO01A_OKA0026.ogg"
    "伦太郎" "「啊啊，恐怕是的……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA02"),"True","lh/DAR_ASA02a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_BUILDE"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_BUILDE"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_BUILDE"])
    $ stopvoc("DAR")
    play DAR "KYO01A_DAR0012"
    $ current_voice = "voice/KYO01A_DAR0012.ogg"
    "至" "「『大楼前面的Ｌｏｃｋｅｒ』是说『{color=#f00}大楼{/color}前的投币式保险柜』吧？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASB06"),"True","lh/CRS_ASB06a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "KYO01A_CRS0004"
    $ current_voice = "voice/KYO01A_CRS0004.ogg"
    "红莉栖" "「『向那里投入“惯例物品”，这么做的话就把真由理还给你。』这么写着诶」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA03"),"True","lh/DAR_ASA03a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "KYO01A_DAR0013"
    $ current_voice = "voice/KYO01A_DAR0013.ogg"
    "至" "「但是“惯例物品”是啥啊？」"
    $ stopvoc("OKA")
    play OKA "KYO01A_OKA0027"
    $ current_voice = "voice/KYO01A_OKA0027.ogg"
    "伦太郎" "「不知道……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASB02"),"True","lh/DAR_ASB02a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "KYO01A_DAR0014"
    $ current_voice = "voice/KYO01A_DAR0014.ogg"
    "至" "「不知道的话……不知道的话真由氏就──！」"
    $ stopvoc("OKA")
    play OKA "KYO01A_OKA0028"
    $ current_voice = "voice/KYO01A_OKA0028.ogg"
    "伦太郎" "「吵死了！所以现在正在想啊！」"
    $ stopvoc("CRS")
    play CRS "KYO01A_CRS0005"
    $ current_voice = "voice/KYO01A_CRS0005.ogg"
    "红莉栖" "「想到谁是犯人了吗？」"
    hide screen phoneSD1
    window hide


    hide screen phonebtn
    "有线索。只会是……Ｒｏｕｎｄｅｒ。"
    "那么想的话，“惯例物品”也许就是能推测出来了。"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_IBN5100"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_IBN5100"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_IBN5100"])
    "恐怕就是『{color=#f00}ＩＢＮ５１００{/color}』吧。"
    "不对，等等……"
    "为什么我会知道这种事情？"
    "因为再次袭来的头痛，我皱起了眉头。"
    window hide










    show screen phonebtn
    show screen phoneSD1
    $ stopvoc("CRS")
    play CRS "KYO01A_CRS0006"
    $ current_voice = "voice/KYO01A_CRS0006.ogg"
    "红莉栖" "「冈部，难道说你知道了？」"
    $ stopvoc("OKA")
    play OKA "KYO01A_OKA0029"
    $ current_voice = "voice/KYO01A_OKA0029.ogg"
    "伦太郎" "「不是，还没有想法……」"
    "觉得不应该现在说出来。"
    "没有证据，记忆也很混乱的前提下，并不认为自己能做出很好的说明。"
    $ stopvoc("OKA")
    play OKA "KYO01A_OKA0030"
    $ current_voice = "voice/KYO01A_OKA0030.ogg"
    "伦太郎" "「你们呢？」"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_ACCOUNT"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_ACCOUNT"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_ACCOUNT"])
    $ stopvoc("OKA")
    play OKA "KYO01A_OKA0031"
    $ current_voice = "voice/KYO01A_OKA0031.ogg"
    "伦太郎" "「发送人的地址有『Ｉ ｃｈａｉｎ ｈｉｓ ｓｎａｋｅ』{color=#f00}账户名{/color}……对于这串英文有什么想法吗？」"
    "红莉栖和桶子沉思片刻，最终无力地摇了摇头。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASC06"),"True","lh/CRS_ASC06a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA03"),"True","lh/DAR_ASA03a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "KYO01A_CRS0007"
    $ current_voice = "voice/KYO01A_CRS0007.ogg"
    "红莉栖" "「虽说意思就是“我抓住了他的蛇”，但……」"
    $ stopvoc("DAR")
    play DAR "KYO01A_DAR0015"
    $ current_voice = "voice/KYO01A_DAR0015.ogg"
    "至" "「只凭那个的话，什么都搞不懂啊……」"
    $ stopvoc("CRS")
    play CRS "KYO01A_CRS0008"
    $ current_voice = "voice/KYO01A_CRS0008.ogg"
    "红莉栖" "「硬要说的话，只有一点，就是这邮件看起来像Ｄｍａｉｌ一样啊」"
    $ stopvoc("OKA")
    play OKA "KYO01A_OKA0032"
    $ current_voice = "voice/KYO01A_OKA0032.ogg"
    "伦太郎" "「……诶？」"
    $ stopvoc("CRS")
    play CRS "KYO01A_CRS0009"
    $ current_voice = "voice/KYO01A_CRS0009.ogg"
    "红莉栖" "「所以说看啊，３６Ｂｙｔｅ的文字，分成了３封发过来吧？」"
    "我从红莉栖那里接过手机，再次确认了收件箱里的邮件。"
    show screen phonebtn
    show screen phoneSD1
    window hide
    hide screen phonebtn
    hide screen phonebtn2
    show screen phone(interact=False)

    call read_last_mail (id=0, p=True)
    call read_last_mail (id=2, p=True)
    call read_last_mail (id=1, p=True)

    $ targetmailid = gc["ScriptMacros"]["FM_KYO01A_RECV_ICH03"]




    $ targetmailid = gc["ScriptMacros"]["FM_KYO01A_RECV_ICH02"]






    $ targetmailid = gc["ScriptMacros"]["FM_KYO01A_RECV_ICH01"]




    call hide_phone



    $ stopvoc("CRS")
    play CRS "KYO01A_CRS0010"
    $ current_voice = "voice/KYO01A_CRS0010.ogg"
    "红莉栖" "「难道说没有注意到吗？」"
    $ stopvoc("OKA")
    play OKA "KYO01A_OKA0033"
    $ current_voice = "voice/KYO01A_OKA0033.ogg"
    "伦太郎" "「在，在说什么蠢话！当然注意到了哦！呼哈哈哈哈！」"
    $ stopvoc("CRS")
    play CRS "KYO01A_CRS0011"
    $ current_voice = "voice/KYO01A_CRS0011.ogg"
    "红莉栖" "「这种紧急情况下，你居然还笑得出来啊」"
    "因为是紧急情况所以才要笑一下镇定下来……"
    window hide


    $ loadBG(2,"BG_BLACK")



    hide screen phonebtn
    "为了平息指尖的震动一般，我握紧了拳头。"
    window hide



    $ loadBG(0,"BG01A")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASB07"),"True","lh/CRS_ASB07a~ipad.png") at left as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA02"),"True","lh/DAR_ASA02a~ipad.png") at right as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    show screen phonebtn
    show screen phoneSD1
    $ stopvoc("DAR")
    play DAR "KYO01A_DAR0016"
    $ current_voice = "voice/KYO01A_DAR0016.ogg"
    "至" "「也就是说这封恐吓信是从未来发送过来的？」"
    $ stopvoc("OKA")
    play OKA "KYO01A_OKA0034"
    $ current_voice = "voice/KYO01A_OKA0034.ogg"
    "伦太郎" "「看起来是呢」"
    $ stopvoc("DAR")
    play DAR "KYO01A_DAR0017"
    $ current_voice = "voice/KYO01A_DAR0017.ogg"
    "至" "「为什么？怎么做到的？也就是说犯人在未来使用了在这个Ｌａｂ里的电话微波炉？？」"
    $ stopvoc("OKA")
    play OKA "KYO01A_OKA0035"
    $ current_voice = "voice/KYO01A_OKA0035.ogg"
    "伦太郎" "「鬼知道！」"
    $ stopvoc("CRS")
    play CRS "KYO01A_CRS0012"
    $ current_voice = "voice/KYO01A_CRS0012.ogg"
    "红莉栖" "「呐，也就是说那是在真由理被绑架之后的事吧？」"
    $ stopvoc("CRS")
    play CRS "KYO01A_CRS0013"
    $ current_voice = "voice/KYO01A_CRS0013.ogg"
    "红莉栖" "「对于未来来说的过去，是对于现在来说的未来也说不定吧？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA03"),"True","lh/DAR_ASA03a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "KYO01A_DAR0018"
    $ current_voice = "voice/KYO01A_DAR0018.ogg"
    "至" "「用日语就ＯＫ」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASB05"),"True","lh/CRS_ASB05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "KYO01A_CRS0014"
    $ current_voice = "voice/KYO01A_CRS0014.ogg"
    "红莉栖" "「所以说！　因为恐吓信是用Ｄｍａｉｌ发送的，所以真由理现在可能还没有被诱拐！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA02"),"True","lh/DAR_ASA02a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "KYO01A_OKA0036"
    $ current_voice = "voice/KYO01A_OKA0036.ogg"
    "伦太郎" "「原来如此……。也就是说……」"
    $ stopvoc("DAR")
    play DAR "KYO01A_DAR0019"
    $ current_voice = "voice/KYO01A_DAR0019.ogg"
    "至" "「有给真由氏打过电话吗？」"
    $ stopvoc("OKA")
    play OKA "KYO01A_OKA0037"
    $ current_voice = "voice/KYO01A_OKA0037.ogg"
    "伦太郎" "「…………」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASA07"),"True","lh/CRS_ASA07a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "KYO01A_CRS0015"
    $ current_voice = "voice/KYO01A_CRS0015.ogg"
    "红莉栖" "「难道说，还没有打过！？」"
    $ stopvoc("OKA")
    play OKA "KYO01A_OKA0038"
    $ current_voice = "voice/KYO01A_OKA0038.ogg"
    "伦太郎" "「没办法啊！　收到邮件的时间点，就是刚好在你们回来之前啊！」"



    $ stopvoc("CRS")
    play CRS "KYO01A_CRS0016"
    $ current_voice = "voice/KYO01A_CRS0016.ogg"
    "红莉栖" "「所以，现在快点去打啊！　好了，快啊！」"



    window hide
    hide screen phonebtn
    hide screen phonebtn2
    show screen phone(interact=False)
    "我一个激灵地跳了起来，给真由理打了电话。"


    "然后……"
    window hide

    window hide






    stop bgm 


    play bgm "fd2bgm14"


    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASC05"),"True","lh/CRS_ASC05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASB04"),"True","lh/DAR_ASB04a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "KYO01A_CRS0017"
    $ current_voice = "voice/KYO01A_CRS0017.ogg"
    "红莉栖" "「等，等等……这是啥声音」"
    $ stopvoc("DAR")
    play DAR "KYO01A_DAR0020"
    $ current_voice = "voice/KYO01A_DAR0020.ogg"
    "至" "「这个是，真由氏的手机的──」"
    $ stopvoc("OKA")
    play OKA "KYO01A_OKA0039"
    $ current_voice = "voice/KYO01A_OKA0039.ogg"
    "伦太郎" "「铃声！」"
    call hide_phone

    hide screen phonebtn
    "我们寻找着声音的源头。"
    window hide






















    $ loadBG(2,"BG02A1")



    "很快就找到了。"
    "在沙发边上的呜帕垫子的下面……真由理的手机躺在那里。"
    window hide



    stop bgm 


    $ loadBG(2,"PBG03A")



    hide screen phonebtn
    play bgm "BGM23"
    $ stopvoc("OKA")
    play OKA "KYO01A_OKA0040"
    $ current_voice = "voice/KYO01A_OKA0040.ogg"
    "伦太郎" "「那个笨蛋！　把手机留在这里了！」"
    $ stopvoc("CRS")
    play CRS "KYO01A_CRS0018"
    $ current_voice = "voice/KYO01A_CRS0018.ogg"
    "红莉栖" "「麻烦了呢……」"
    window hide



    $ loadBG(2,"BG02A1")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA01"),"True","lh/DAR_ASA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    show screen phonebtn



    $ stopvoc("DAR")
    play DAR "KYO01A_DAR0021"
    $ current_voice = "voice/KYO01A_DAR0021.ogg"
    "至" "「那，不如去琉华氏那里问问？」"

    $ stopvoc("OKA")
    play OKA "KYO01A_OKA0041"
    $ current_voice = "voice/KYO01A_OKA0041.ogg"
    "伦太郎" "「什，什么……？」"

    $ stopvoc("DAR")
    play DAR "KYO01A_DAR0022"
    $ current_voice = "voice/KYO01A_DAR0022.ogg"
    "至" "「喂，不是在我和牧濑氏出门买东西之前说的吗」"

    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_COMIMA"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_COMIMA"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_COMIMA"])
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_COSTUME"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_COSTUME"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_COSTUME"])

    $ stopvoc("DAR")
    play DAR "KYO01A_DAR0023"
    $ current_voice = "voice/KYO01A_DAR0023.ogg"
    "至" "「后天的{color=#f00}夏Ｃｏｍｉ{/color}上，为了让他穿上真由理做的{color=#f00}Ｃｏｓｐｌａｙ{/color}服，所以要去琉华子那里……」"

    "在桶子说完之前，我的手已经动了起来。"



    window hide
    hide screen phonebtn
    hide screen phonebtn2
    show screen phone(interact=False)
    "取出了手机，开始拨打琉华子的号码。"
    window hide










    window hide






    $ stopvoc("RUK")
    play RUK "KYO01A_RUK0000"
    $ current_voice = "voice/KYO01A_RUK0000.ogg"
    "琉华" "「喂，我是漆原。」"

    $ stopvoc("OKA")
    play OKA "KYO01A_OKA0042"
    $ current_voice = "voice/KYO01A_OKA0042.ogg"
    "伦太郎" "「琉华子！　真由理在──」"

    $ stopvoc("RUK")
    play RUK "KYO01A_RUK0001"
    $ current_voice = "voice/KYO01A_RUK0001.ogg"
    "琉华" "「但是现在没有办法接电话」"

    "切，是语音信箱吗……"

    $ stopvoc("RUK")
    play RUK "KYO01A_RUK0002"
    $ current_voice = "voice/KYO01A_RUK0002.ogg"
    "琉华" "「在哔的一声后，请留言」"

    window hide
    play se "SGSE071"

    $ stopvoc("OKA")
    play OKA "KYO01A_OKA0043"
    $ current_voice = "voice/KYO01A_OKA0043.ogg"
    "伦太郎" "「是我！　凶真！　在找真由理！　如果有消息的话请火速联系！」"
    window hide


    call hide_phone


    $ stopvoc("CRS")
    play CRS "KYO01A_CRS0019"
    $ current_voice = "voice/KYO01A_CRS0019.ogg"
    "红莉栖" "「语音信箱？」"
    $ stopvoc("OKA")
    play OKA "KYO01A_OKA0044"
    $ current_voice = "voice/KYO01A_OKA0044.ogg"
    "伦太郎" "「恩恩……」"
    "大家都沉默了。"


    play se "SGSE004L" loop
    "不知从何处传来蝉鸣声。"
    window hide

    play se "SGSE039"


    $ loadBG(2,"BG01A")




    "窗户外有人骑着一辆摩托车经过。"
    "在那声音消失的时候，桶子仿佛突然想到了什么般说道。"
    window hide

    stop se

    stop se



    $ loadBG(2,"BG02A1")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASB07"),"True","lh/CRS_ASB07a~ipad.png") at left as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA02"),"True","lh/DAR_ASA02a~ipad.png") at right as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    $ stopvoc("DAR")
    play DAR "KYO01A_DAR0024"
    $ current_voice = "voice/KYO01A_DAR0024.ogg"
    "至" "「呐，试着直接联系犯人如何？」"
    $ stopvoc("DAR")
    play DAR "KYO01A_DAR0025"
    $ current_voice = "voice/KYO01A_DAR0025.ogg"
    "至" "「『Ｉ ｃｈａｉｎ ｈｉｓ ｓｎａｋｅ』──邮件地址也不是知道么」"
    $ stopvoc("OKA")
    play OKA "KYO01A_OKA0045"
    $ current_voice = "voice/KYO01A_OKA0045.ogg"
    "伦太郎" "「但是发送邮件的『Ｉ ｃｈａｉｎ ｈｉｓ ｓｎａｋｅ』可是在未来的『Ｉ ｃｈａｉｎ ｈｉｓ ｓｎａｋｅ』哦？」"
    $ stopvoc("OKA")
    play OKA "KYO01A_OKA0046"
    $ current_voice = "voice/KYO01A_OKA0046.ogg"
    "伦太郎" "「啊，名字太长了好烦啊！后面就简称『ｉｃｈｓ』了。」"
    $ stopvoc("CRS")
    play CRS "KYO01A_CRS0020"
    $ current_voice = "voice/KYO01A_CRS0020.ogg"
    "红莉栖" "「ｉｃｈｓ？」"
    $ stopvoc("OKA")
    play OKA "KYO01A_OKA0047"
    $ current_voice = "voice/KYO01A_OKA0047.ogg"
    "伦太郎" "「把各单词的首字母取下来就是这个啊」"
    "顺便一提也含有正体不明的『Ｘ』的意思。"
    $ stopvoc("DAR")
    play DAR "KYO01A_DAR0026"
    $ current_voice = "voice/KYO01A_DAR0026.ogg"
    "至" "「总而言之我觉得应该要试着发一下邮件」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASA01"),"True","lh/CRS_ASA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "KYO01A_CRS0021"
    $ current_voice = "voice/KYO01A_CRS0021.ogg"
    "红莉栖" "「我也赞成。不这么做这样下去线索也太少了吧……」"
    $ stopvoc("CRS")
    play CRS "KYO01A_CRS0022"
    $ current_voice = "voice/KYO01A_CRS0022.ogg"
    "红莉栖" "「这也是一个可以趁机试探对方态度的机会」"
    $ stopvoc("OKA")
    play OKA "KYO01A_OKA0048"
    $ current_voice = "voice/KYO01A_OKA0048.ogg"
    "伦太郎" "「但，发什么好呢？」"
    $ stopvoc("CRS")
    play CRS "KYO01A_CRS0023"
    $ current_voice = "voice/KYO01A_CRS0023.ogg"
    "红莉栖" "「『想和你谈谈』……这就够了吧？」"
    $ stopvoc("CRS")
    play CRS "KYO01A_CRS0024"
    $ current_voice = "voice/KYO01A_CRS0024.ogg"
    "红莉栖" "「不要提到“真由理”或者“惯例物品”之类的东西」"
    hide screen phoneSD1
    window hide


    hide screen phonebtn
    "我困惑着。给ｉｃｈｓ发这样的邮件还是不发呢……"
    "如果因为发了邮件而导致真由理发生了什么的话怎么办？"
    "当然现在还没能确定真由理被诱拐了，说不定是在这之后的事。"
    "但是危险正在逐渐接近真由理的身边这一点不会有错。"
    "我并不觉得这封邮件是恶作剧。"
    "普通的邮件还有可能，但这可是Ｄｍａｉｌ。"
    "超越了时空的邮件——"
    "所以不是已经发生了什么，就是即将要发生什么事。"
    "所以，如果就这么呆在这里的话，连真由理的人身安全都无法保证。"
    "还有，虽然我们被恐吓邮件吓坏了，但是对于“除了我们以外的某人发送了Ｄｍａｉｌ”这一点也不能置之不理。"
    "这是会左右世界历史的重大事件。"
    "无论如何也要揭穿Ｉｃｈｓ的正体……！"
    window hide










    show screen phonebtn
    show screen phoneSD1
    "所以我说出了，那一句话。"
    $ stopvoc("OKA")
    play OKA "KYO01A_OKA0049"
    $ current_voice = "voice/KYO01A_OKA0049.ogg"
    "伦太郎" "「明白了」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    hide screen phonebtn
    hide screen phonebtn2
    show screen phone(interact=False)
    pause 2
    call send_mail (id=[15,16])

    $ targetmailid = gc["ScriptMacros"]["FM_KYO01A_EDIT_ICH01_00"]

    $ targetmailid = gc["ScriptMacros"]["FM_KYO01A_SEND_ICH01"]






    hide screen phoneSD1

    call hide_phone


    $ loadBG(0,"BG_BLACK")

    hide screen phonebtn
    "自从发送邮件了之后，经过了多久呢。"
    "５分钟吗，还是６分钟，或者是７分钟……"
    window hide


    $ loadBG(0,"BG02A1")

    show screen phonebtn
    show screen phoneSD1
    "并没有回信。"
    "墙壁上的时钟滴答滴答地向前走着。"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASA01"),"True","lh/CRS_ASA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "KYO01A_CRS0025"
    $ current_voice = "voice/KYO01A_CRS0025.ogg"
    "红莉栖" "「总之像现在这样是不行的，让我们行动起来吧！」"
    "就像是要驱散这沉重的空气一般，红莉栖发话了。"
    $ stopvoc("CRS")
    play CRS "KYO01A_CRS0026"
    $ current_voice = "voice/KYO01A_CRS0026.ogg"
    "红莉栖" "「我去柳林神社，冈部你就去大楼的保险柜那里看看，说不定能看到犯人的样子……」"
    $ stopvoc("OKA")
    play OKA "KYO01A_OKA0050"
    $ current_voice = "voice/KYO01A_OKA0050.ogg"
    "伦太郎" "「那关于“惯例物品”怎么处理？」"
    $ stopvoc("CRS")
    play CRS "KYO01A_CRS0027"
    $ current_voice = "voice/KYO01A_CRS0027.ogg"
    "红莉栖" "「在知道那是什么之前，我们什么也做不了吧？」"
    $ stopvoc("OKA")
    play OKA "KYO01A_OKA0051"
    $ current_voice = "voice/KYO01A_OKA0051.ogg"
    "伦太郎" "「那就空着手去吧？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASA02"),"True","lh/CRS_ASA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "KYO01A_CRS0028"
    $ current_voice = "voice/KYO01A_CRS0028.ogg"
    "红莉栖" "「觉得不妥的话，就带个点心盒去吧？」"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASA02"),"True","lh/CRS_ASA02a~ipad.png") at left as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA02"),"True","lh/DAR_ASA02a~ipad.png") at right as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "KYO01A_DAR0027"
    $ current_voice = "voice/KYO01A_DAR0027.ogg"
    "至" "「我呢？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASB01"),"True","lh/CRS_ASB01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "KYO01A_CRS0029"
    $ current_voice = "voice/KYO01A_CRS0029.ogg"
    "红莉栖" "「桥田就在这里待命。说不定真由理会回这里呢」"
    $ stopvoc("DAR")
    play DAR "KYO01A_DAR0028"
    $ current_voice = "voice/KYO01A_DAR0028.ogg"
    "至" "「Ｏｋｅｙ－Ｄｏｋｅｙ」"
    $ stopvoc("CRS")
    play CRS "KYO01A_CRS0030"
    $ current_voice = "voice/KYO01A_CRS0030.ogg"
    "红莉栖" "「那就这样，有什么的话再联系。我也会联系的」"
    $ stopvoc("OKA")
    play OKA "KYO01A_OKA0052"
    $ current_voice = "voice/KYO01A_OKA0052.ogg"
    "伦太郎" "「了解」"
    window hide
    hide lh5  with dissolve
    play se "SGSE024"

    "听到我的答复，红莉栖离开了Ｌａｂ。"
    window hide


    $ loadBG(2,"BG01A")



    "虽然我也想和她一样潇洒地离开……"
    window hide


    $ loadBG(2,"BG02A1")



    "在开门之前我却停住了脚步，回过头去。"
    "还有一件要搞清楚的事情。"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA01"),"True","lh/DAR_ASA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "KYO01A_DAR0029"
    $ current_voice = "voice/KYO01A_DAR0029.ogg"
    "至" "「怎么了？」"
    $ stopvoc("OKA")
    play OKA "KYO01A_OKA0053"
    $ current_voice = "voice/KYO01A_OKA0053.ogg"
    "伦太郎" "「不是，怎么说呢」"
    "随便糊弄一下就跑进了开发室。"
    window hide


    $ loadBG(2,"BG03A4")



    "朝棚子里看去，里面有一个眼熟的纸板箱。"
    window hide
    play se "SGSE135"



    $ loadBG(2,"IBGX075")



    hide screen phonebtn
    "里面放着ＩＢＮ５１００、"
    $ stopvoc("OKA")
    play OKA "KYO01A_OKA0054"
    $ current_voice = "voice/KYO01A_OKA0054.ogg"
    "伦太郎" "「在这条世界线里有这个吗……」"
    "稍微有些安心了。"
    "但是要是“惯例物品”是这个的话，就有些麻烦了。"
    "总而言之……"
    "总而言之不能让它落入敌人的手中！"
    window hide


    $ loadBG(2,"BG03A4")



    "我将纸板箱放回原处，急冲冲地赶往了大楼前的保险柜。"

    hide screen phoneSD1
    window hide

    stop bgm 




    hide screen phonebtn
    scene expression Solid("000000")  with fade
    return
