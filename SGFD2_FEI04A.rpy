label SGFD2_FEI04A:
    play bgm "BGM23"
    hide screen phonebtn
    scene expression Solid("000000")  with fade

    window hide


    $ loadBG(0,"BG05N1")


    $ date="8/10"
    $ day="TUE"
    show screen phonebtn
    show screen phoneSD1

    "在显像管工房的边上，那些委员会的大人们已经叫来了警官，场面十分混乱。"
    "这个时间，平时的话大家早就沉沉入睡了，应该没什么声音才对，但是在显像管工房门前，那些委员会的人还有警官以及不知道发生了什么事的居民们正骚动着。"
    "与此同时红色的警灯也照亮着周围，告诉大家目前情况的紧急性。"
    "果然有什么坏事发生了啊……"
    "也就是说被卷入其中的是绹酱？"
    "我从人墙中努力踮起脚看向混乱的中心。但是在发现那里的天王寺先生之后，我反射性地将头缩了回来。"
    window hide



    $ loadBG(2,"BG05N1")





    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='TEN')",DynamicDisplayable(mouthanime,"TEN_ASA02"),"True","lh/TEN_ASA02a~ipad.png") at right_q1 as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    $ stopvoc("TEN")
    play TEN "FEI04A_TEN0000"
    $ current_voice = "voice/FEI04A_TEN0000.ogg"
    "天王寺" "「所以刚才就说过了吧！　已经不知道几个小时没能和绹联系上了！」"
    $ stopvoc("TEN")
    play TEN "FEI04A_TEN0001"
    $ current_voice = "voice/FEI04A_TEN0001.ogg"
    "天王寺" "「你们这群警察不是一直都这样的吗！　为什么最开始的时候告诉你们都不采取行动啊！」"
    $ stopvoc("TEN")
    play TEN "FEI04A_TEN0002"
    $ current_voice = "voice/FEI04A_TEN0002.ogg"
    "天王寺" "「你们在那边打太极的时候，知道我心里是怎么想的嘛！」"
    "那些委员会的大人们都在尽力阻止天王寺先生。那些警察一副输给天王寺先生的气势了的样子。"
    "但是看起来不是所有委员会的人都在那。剩下的人应该是和警察在一起寻找绹酱把。我从混乱的现场中不断地观察着，把握了大概情况。"
    "就算如此，我对于自己对那封邮件的处理方式很懊悔。"
    "如果知道会变成这样的话，就不应该让绹酱离开自己的视线。"
    "我用力地握紧拳头。"
    window hide

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA04"),"True","lh/OKA_ASA04a~ipad.png") at left_q1 as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh7 
    show expression ConditionSwitch("renpy.music.get_playing(channel='RUK')",DynamicDisplayable(mouthanime,"RUK_CSB02"),"True","lh/RUK_CSB02a~ipad.png") at right_q2 as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh8 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASC06"),"True","lh/CRS_ASC06a~ipad.png") at left_q2 as lh8 zorder (10-8) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "FEI04A_OKA0000"
    $ current_voice = "voice/FEI04A_OKA0000.ogg"
    "伦太郎" "「Ｍｒ．布朗！　虽然找了很久但是没有找到。她真的去了秋叶原车站吗？」"
    $ stopvoc("RUK")
    play RUK "FEI04A_RUK0000"
    $ current_voice = "voice/FEI04A_RUK0000.ogg"
    "琉华" "「神田川方向也没有找到」"
    $ stopvoc("CRS")
    play CRS "FEI04A_CRS0000"
    $ current_voice = "voice/FEI04A_CRS0000.ogg"
    "红莉栖" "「以防万一我沿着中央大道一直找到末广町站，都没有找到」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='TEN')",DynamicDisplayable(mouthanime,"TEN_ASA03"),"True","lh/TEN_ASA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("TEN")
    play TEN "FEI04A_TEN0003"
    $ current_voice = "voice/FEI04A_TEN0003.ogg"
    "天王寺" "「你们不用道歉」"
    $ stopvoc("TEN")
    play TEN "FEI04A_TEN0004"
    $ current_voice = "voice/FEI04A_TEN0004.ogg"
    "天王寺" "「但是绹确实说是去秋叶原站接她的朋友来着的，不应该消失啊……」"
    "搜索队中有桶子还有桐生，而且……"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_ASA03"),"True","lh/SUZ_ASA03a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "FEI04A_SUZ0000"
    $ current_voice = "voice/FEI04A_SUZ0000.ogg"
    "铃羽" "「已经三个小时了呢……手机也联系不上了？」"
    "『她』也在。"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_ASA03"),"True","lh/SUZ_ASA03a~ipad.png") at left as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='TEN')",DynamicDisplayable(mouthanime,"TEN_ASA02"),"True","lh/TEN_ASA02a~ipad.png") at right as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("TEN")
    play TEN "FEI04A_TEN0005"
    $ current_voice = "voice/FEI04A_TEN0005.ogg"
    "天王寺" "「……恩，明明有接通的声音的……可恶！」"
    "我也从这里出来加入到他们的搜索队伍里吧……"
    "看了一下，阿万音露出严肃的表情在和天王寺还有冈部说着什么。"
    "……事到如今，我都不知道该以什么表情去面对他们了。"
    "而且，那里还有天王寺先生。"
    window hide


    $ loadBG(2,"BG05N1")



    "注意到的时候我发现自己已经从那个地方逃开，开始寻找绹酱的踪影。"
    window hide


    $ loadBG(0,"BG20N")

    "一边朝着秋叶原方向走去，我一边不时看看小巷子里，还有大楼的边上，凝视着黑暗的地方。"
    "想要找到绹安然无恙的样子。"
    "但是不管我再怎么着急，也没有能找到她的影子。"
    "说起来……"
    hide screen phoneSD1
    window hide


    $ loadBG(0,"BG24A")


    hide lh7 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_EMA01"),"True","lh/SUZ_EMA01a~ipad.png") at center as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    hide screen phonebtn
    "我想起这一片就是我作为黑猫和阿万音一起四处奔走的地方。"
    "那个时候我享受着每时每刻，沉醉在解放自我的快感里。"
    window hide


    $ loadBG(2,"BG_BLACK")



    "如今却孓然一人……"
    "这样还不如消失……"
    "把一切都抛弃就这么消失也许更快乐一些……"
    "…………"
    "…………"
    "……消失？"
    window hide


    $ loadBG(2,"BG20N")



    show screen phonebtn
    show screen phoneSD1
    "难道这是所谓的人间蒸发的都市传说？"
    "但是那是天王寺先生他们的自导自演才对。"
    "……不，不对。只有那个传言有目击情报。"
    "确实……在万世桥附近。"


    hide screen phonebtn
    $ targetmailid = gc["ScriptMacros"]["FM_FEI04A_RECV_FEI01"]
    if phonemailring!= "":
        play se phonemailring
    if persistent.skipmail==False:
        $ renpy.choice_for_skipping()
    if targetmailid != "":
        $ RcvMail(targetmailid)
        $ targetmailid=""
    "这个时候的邮件？"

    "难道说是绹发来的！"

    window hide


    hide screen phonebtn
    hide screen phonebtn2
    call read_last_mail






    "我一下子就心跳加速了。"
    "就算是妄想也无妨，就算是偶然的巧合也无妨，有去找一下的价值。"
    window hide
    call hide_phone

    "总之现在赶紧去万世桥吧！"
    window hide

    stop bgm 




    $ loadBG(0,"BG78N")
    play se "SGSE152"

    $ stopvoc("FEI")
    play FEI "FEI04A_FEI0000"
    $ current_voice = "voice/FEI04A_FEI0000.ogg"
    "菲利斯" "「……哈、哈、哈」"
    "这附近就是人间蒸发的目击现场、"
    "右手边是已经拉下卷闸门的家电量贩店，左边是笔直的中央大道。"
    "但是那里也没有绹酱的身影。"
    "果然是我搞错了吗？只是白跑了一趟？"
    "……恩，这是？"
    "我环视周围的时候，感觉踢到了什么的样子，将视线落到了地面上。"
    window hide


    $ loadBG(2,"IBG006A",png=True)




    $ stopvoc("FEI")
    play FEI "FEI04A_FEI0001"
    $ current_voice = "voice/FEI04A_FEI0001.ogg"
    "菲利斯" "「乌帕的……钥匙串？」"
    "在人行道边上的通风口的格子里，有一个崭新的钥匙扣卡在那里。因为卡得挺紧的，稍微用了点力还拉不出来。"
    window hide



    hide background-png 
    "于是我就加大了力气，试图强行把它给拔出来。"
    "就在那时……"


    $ loadBG(2,"BG_BLACK")




    play se "SGSE365"


    $ stopvoc("FEI")
    play FEI "FEI04A_FEI0002"
    $ current_voice = "voice/FEI04A_FEI0002.ogg"
    "菲利斯" "「咿呀！」"


    "一瞬间不知道发生了什么、"
    "把那个拔出来之后，好像发出了什么声音，我脚下的通风口的盖子就消失了。"
    "然后我才注意到自己现在身处一片黑暗之中。虽然头顶上有明亮的月光，但是我很快发现它被一些细细的铁栏给遮住了。"
    "难道说我不小心按到了通向这个空间的开关？"
    "但是为什么会有这样的机关啊……"
    hide screen phonebtn
    "我取出手机，用它的背光照亮了周围。终于稍微把握了一下自己的处境。"
    window hide


    $ loadBG(0,"BG70A")
    play se "SGSE367"



    play bgm "BGM25"
    "这里看起来像是什么地下设施。"
    "直到刚才我还站在人行道的通风口上面。但是突然就滑到了这个隐秘的场所里。"
    "如果捡起那个呜帕的话，就相当于按了进入这里的秘密开关。就算如此，这到底是……"
    "我屁股下面是平缓的楼梯。"
    "混凝土制的天花板看起来破旧不堪。"
    "感觉这周围像地铁的入口的样子。那个通风口下面也有楼梯，应该就一直通向这里的地下设施。"
    "这个设施本身也很古老的样子。因为我掉下来的震动，头顶上落下来好多的灰尘。"
    "仅仅是大一点的声音就会有灰尘落下来……这样的话，看起来这个设施很是危险啊。"
    $ stopvoc("FEI")
    play FEI "FEI04A_FEI0003"
    $ current_voice = "voice/FEI04A_FEI0003.ogg"
    "菲利斯" "「这个……」"
    window hide


    $ loadBG(2,"IBG007A",png=True)




    "在背光的照耀下，我看到了一块用平假名写着『万世桥』的牌子。"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_OLD_MANSEIBASHI_STA"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_OLD_MANSEIBASHI_STA"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_OLD_MANSEIBASHI_STA"])
    "然后我就想起来了。这里是东京地铁的{color=#f00}旧・万世桥站{/color}。"
    "昭和５年１月开业，次年１１月废止的梦幻车站。"
    "虽然从爸爸那里听说过，但是没想到里面是这样的啊。"
    hide background-png 
    window hide





    $ loadBG(2,"BG_BLACK")




    "……我小心翼翼地沿着楼梯向下走。。"
    window hide
    $ loadBG(0,"BG69A")



    play se "SGSE375"

    "感觉又踩到了什么……那么想着，我将手机对准脚下。"
    window hide


    $ loadBG(2,"IBG008A",png=True)




    "那里有一个奇怪的铁块。形状像口红一样，前端稍微有些尖尖的。"
    "在背光下闪闪发光的表面。用手指拿起来之后，感觉有些沉。"
    "这难道是……子弹？"
    "为什么？难道说这里有银行强盗或者恐怖分子躲着吗？"
    window hide
    hide background-png 



    "我慌张地又照亮了脚边，但是没有看到地上有什么别的东西。为了开阔视野，我将手机举了起来，用背光照亮了周围。"

    "然后有了新的发现，那就是墙壁上有无数个贯通的小洞。"
    "仔细看看，在洞的内部有许多和我捡起来一样的子弹。"
    "乱射？　在这种地方……？"
    "用手指试着摸了一下，然后那里发出一些轻响，有一些开始啪啦啪啦地落下来。"
    "是因为风化加上新打的弹孔的关系吧。"
    "现在不是凭着好奇心随意观察的场合。"
    "这里很危险……要尽早赶出去。"
    "就在我这么想的时候。"
    "我的视线的一侧中出现了跳动的人影。"
    "不会是她吧，我想道。"
    "但是并没有搞错。"
    $ stopvoc("FEI")
    play FEI "FEI04A_FEI0004"
    $ current_voice = "voice/FEI04A_FEI0004.ogg"
    "菲利斯" "「绹喵！？」"
    "我没多想就喊了出去，随着我的声音又是一阵灰尘落了下来。"
    "这说不定还真是糟糕了……"
    $ stopvoc("FEI")
    play FEI "FEI04A_FEI0005"
    $ current_voice = "voice/FEI04A_FEI0005.ogg"
    "菲利斯" "「没事吧，绹喵」"
    "将子弹塞进口袋之后，我一边用手机背光照着路，一边沿着楼梯跑了下去，确认在楼梯最底下蹲着的她的情况。"
    $ stopvoc("NAE")
    play NAE "FEI04A_NAE0000"
    $ current_voice = "voice/FEI04A_NAE0000.ogg"
    "绹" "「恩……恩恩……」"
    "衣服有很多脏兮兮的地方，但是没有出血的痕迹。"
    "是直到刚才才恢复了意识吗，眼睛半开着，呆然地望着我这边。"

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='NAE')",DynamicDisplayable(mouthanime,"NAE_ASA06"),"True","lh/NAE_ASA06a~ipad.png") at center as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("NAE")
    play NAE "FEI04A_NAE0001"
    $ current_voice = "voice/FEI04A_NAE0001.ogg"
    "绹" "「猫……姐姐……？」"
    "好像也没有感到疼痛的样子。"
    "这样的话活动应该也没问题吧。"
    $ stopvoc("FEI")
    play FEI "FEI04A_FEI0006"
    $ current_voice = "voice/FEI04A_FEI0006.ogg"
    "菲利斯" "「大家都很担心你哦。总之先上来吧喵」"

    stop bgm 
    play se "SGSE369"

    $ stopvoc("FEI")
    play FEI "FEI04A_FEI0007"
    $ current_voice = "voice/FEI04A_FEI0007.ogg"
    "菲利斯" "「！？」"
    "我反射性地转过头去。"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_ASA01"),"True","lh/SUZ_ASA01a~ipad.png") at left as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='NAE')",DynamicDisplayable(mouthanime,"NAE_ASA06"),"True","lh/NAE_ASA06a~ipad.png") at right as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "FEI04A_SUZ0001"
    $ current_voice = "voice/FEI04A_SUZ0001.ogg"
    "铃羽" "「……Ｂｏｓｓ？　是我啦」"
    "她也用手机的背光照亮着周围，慢慢地向着这边走过来。"
    $ stopvoc("SUZ")
    play SUZ "FEI04A_SUZ0002"
    $ current_voice = "voice/FEI04A_SUZ0002.ogg"
    "铃羽" "「绹、这个……是你落下的吧？」"
    "这么说着，阿万音掏出了我刚才在通风口看到的钥匙扣。"
    $ stopvoc("SUZ")
    play SUZ "FEI04A_SUZ0003"
    $ current_voice = "voice/FEI04A_SUZ0003.ogg"
    "铃羽" "「在上面见到的」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='NAE')",DynamicDisplayable(mouthanime,"NAE_ASA01"),"True","lh/NAE_ASA01a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("NAE")
    play NAE "FEI04A_NAE0002"
    $ current_voice = "voice/FEI04A_NAE0002.ogg"
    "绹" "「谢谢你，打工姐姐……」"
    "在绹接过钥匙扣放进口袋里的时候，我看到她的口袋里还有一个没开封过的一样的钥匙扣。"
    $ stopvoc("FEI")
    play FEI "FEI04A_FEI0008"
    $ current_voice = "voice/FEI04A_FEI0008.ogg"
    "菲利斯" "「那个和这个是一样的吗？」"
    $ stopvoc("NAE")
    play NAE "FEI04A_NAE0003"
    $ current_voice = "voice/FEI04A_NAE0003.ogg"
    "绹" "「恩，这个呜帕是朋友之间说过想要的，所以才特意去买来了。」"
    "这样啊……肯定是打算交给朋友的吧。然后不小心掉了之后，捡起来的时候就掉到了这里。"
    $ stopvoc("FEI")
    play FEI "FEI04A_FEI0009"
    $ current_voice = "voice/FEI04A_FEI0009.ogg"
    "菲利斯" "「下次可要注意不要掉下来咯喵」"
    "我轻轻地摸着默默点头的绹酱，将她小小的身体背了起来。然后我向看着这边一副放心的样子的阿万音问道。"
    $ stopvoc("FEI")
    play FEI "FEI04A_FEI0010"
    $ current_voice = "voice/FEI04A_FEI0010.ogg"
    "菲利斯" "「为什么会知道在这儿啊喵」"
    $ stopvoc("SUZ")
    play SUZ "FEI04A_SUZ0004"
    $ current_voice = "voice/FEI04A_SUZ0004.ogg"
    "铃羽" "「为什么？　啊啊……是邮件哦。我也收到了」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    "我看到阿万音的手机里也有许多她自己给她发的邮件。"
    hide screen phoneSD1
    window hide


    $ loadBG(2,"PBG09A")



    hide screen phonebtn
    "第一条的内容是「去旧万世桥站」"
    window hide


    $ loadBG(2,"PBG09B")






    $ loadBG(2,"PBG09C")




    "在那之后是『去帮助留未穗』『吧去帮留未穗』这样神奇的切分方式的邮件，"
    "和我那时候一样。"
    "另一个自己发来的迷之邮件。"
    "但是多亏了这样我们才能把绹酱给救出来。"
    window hide



    $ loadBG(2,"BG69A")



    show screen phoneSD1
    hide screen phonebtn
    "解谜什么的之后再说，赶紧从这里脱身吧。"
    play se "SGSE368L" loop
    "阿万音走到我的身边，用手机背光给我照明脚下的路。"
    "我负责背绹酱。"
    window hide


    $ loadBG(2,"BG70A")



    "离出口并没有很远，大概１０米左右的距离。"
    "我慎重地拾级而上。"
    $ stopvoc("FEI")
    play FEI "FEI04A_FEI0011"
    $ current_voice = "voice/FEI04A_FEI0011.ogg"
    "菲利斯" "「…………」"
    $ stopvoc("SUZ")
    play SUZ "FEI04A_SUZ0005"
    $ current_voice = "voice/FEI04A_SUZ0005.ogg"
    "铃羽" "「…………」"

    stop se
    $ stopvoc("FEI")
    play FEI "FEI04A_FEI0012"
    $ current_voice = "voice/FEI04A_FEI0012.ogg"
    "菲利斯" "「还没到出发的时间喵？」"
    $ stopvoc("SUZ")
    play SUZ "FEI04A_SUZ0006"
    $ current_voice = "voice/FEI04A_SUZ0006.ogg"
    "铃羽" "「……！」"
    "阿万音的表情就算在微弱的光线中难以看清。"
    "但是听她的气息突然变乱了，我就明白了。"
    $ stopvoc("SUZ")
    play SUZ "FEI04A_SUZ0007"
    $ current_voice = "voice/FEI04A_SUZ0007.ogg"
    "铃羽" "「已经必须要走了。在下雨之前」"
    "…………。"
    $ stopvoc("FEI")
    play FEI "FEI04A_FEI0013"
    $ current_voice = "voice/FEI04A_FEI0013.ogg"
    "菲利斯" "「呐」"
    "必须在这里说出来。在离别之前。"
    $ stopvoc("SUZ")
    play SUZ "FEI04A_SUZ0008"
    $ current_voice = "voice/FEI04A_SUZ0008.ogg"
    "铃羽" "「……嗯？」"
    $ stopvoc("FEI")
    play FEI "FEI04A_FEI0014"
    $ current_voice = "voice/FEI04A_FEI0014.ogg"
    "菲利斯" "「白天的事情喵」"
    $ stopvoc("SUZ")
    play SUZ "FEI04A_SUZ0009"
    $ current_voice = "voice/FEI04A_SUZ0009.ogg"
    "铃羽" "「……嗯」"
    $ stopvoc("FEI")
    play FEI "FEI04A_FEI0015"
    $ current_voice = "voice/FEI04A_FEI0015.ogg"
    "菲利斯" "「最后变成那样，我必须要道歉……」"
    "在这么说的时候。"
    play se "SGSE376"

    "头上的尘土发出讨厌的声音，大片落下。"
    "……什么？"
    "我抬头的那瞬间。"
    $ stopvoc("SUZ")
    play SUZ "FEI04A_SUZ0010"
    $ current_voice = "voice/FEI04A_SUZ0010.ogg"
    "铃羽" "「……危险！」"
    window hide
    play se "SGSE015"
    with vpunch
    with vpunch
    $ stopvoc("FEI")
    play FEI "FEI04A_FEI0016"
    $ current_voice = "voice/FEI04A_FEI0016.ogg"
    "菲利斯" "「呀！」"
    $ stopvoc("NAE")
    play NAE "FEI04A_NAE0004"
    $ current_voice = "voice/FEI04A_NAE0004.ogg"
    "绹" "「……！」"
    "突然从边上被推了一把，我就那么背着绹酱，在楼梯上一个踉跄向前跑了几步。"
    play se "SGSE049L" loop
    "沙尘和瓦砾猛然坠落。"
    "因为重物落地的关系，地面摇晃着，我和绹酱面前出现了一堵土墙。"
    "那一切，发生在一瞬之间。"
    window hide

    play se "SGSE370"


    stop se

    $ loadBG(0,"BG71N")




    "我环顾四周。"
    "陶酱看着不安的我。"
    "阿万音……"
    "那一瞬间，我冷汗直流。"
    play bgm "BGM09"
    "……没有看到。"
    "不在……"
    "不在那！"
    "不会是真的吧，我这么想着，凝视着瓦砾堆起的小山。"
    "只能在那里了。"
    "阿万音她为了救我们，自己被瓦砾给埋了！"
    $ stopvoc("NAE")
    play NAE "FEI04A_NAE0005"
    $ current_voice = "voice/FEI04A_NAE0005.ogg"
    "绹" "「……打工姐姐呢？」"
    "那声音没有传到我的耳朵里。"
    "手在颤抖着，呼吸变的慌乱。"
    $ stopvoc("FEI")
    play FEI "FEI04A_FEI0017"
    $ current_voice = "voice/FEI04A_FEI0017.ogg"
    "菲利斯" "「阿万音……」"
    $ stopvoc("FEI")
    play FEI "FEI04A_FEI0018"
    $ current_voice = "voice/FEI04A_FEI0018.ogg"
    "菲利斯" "「阿万音！」"
    $ stopvoc("FEI")
    play FEI "FEI04A_FEI0019"
    $ current_voice = "voice/FEI04A_FEI0019.ogg"
    "菲利斯" "「铃羽！」"
    "我开始把眼前的瓦砾拨开，试图向里面挖掘。"
    play se "SGSE376"


    "但是不管怎么做总会有别的瓦砾落下来，挡在我的面前。"
    $ stopvoc("FEI")
    play FEI "FEI04A_FEI0020"
    $ current_voice = "voice/FEI04A_FEI0020.ogg"
    "菲利斯" "「……铃羽！　铃羽！」"
    $ stopvoc("NAE")
    play NAE "FEI04A_NAE0006"
    $ current_voice = "voice/FEI04A_NAE0006.ogg"
    "绹" "「姐姐！　赶紧去叫别的人来啊、姐姐！」"
    "从我的身后，一双小手拉住了我的衣服。"
    "我又看了一眼瓦砾堆成的小山。"
    "被那么活埋的铃羽能撑多久呢。"
    "……不对，没有时间浪费了。"
    $ stopvoc("FEI")
    play FEI "FEI04A_FEI0021"
    $ current_voice = "voice/FEI04A_FEI0021.ogg"
    "菲利斯" "「走吧，绹酱」"
    "我牵过小手，和她一起来到了地面上。"
    window hide



    $ loadBG(0,"BG78N")

    "这个时间了，周围谁也没有。"
    "没有人能够叫来帮忙。"
    $ stopvoc("FEI")
    play FEI "FEI04A_FEI0022"
    $ current_voice = "voice/FEI04A_FEI0022.ogg"
    "菲利斯" "「绹酱，我们要跑到Ｌａｂ哦」"

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='NAE')",DynamicDisplayable(mouthanime,"NAE_AMA05"),"True","lh/NAE_AMA05a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("NAE")
    play NAE "FEI04A_NAE0007"
    $ current_voice = "voice/FEI04A_NAE0007.ogg"
    "绹" "「……恩」"
    $ stopvoc("FEI")
    play FEI "FEI04A_FEI0023"
    $ current_voice = "voice/FEI04A_FEI0023.ogg"
    "菲利斯" "「快点！　铃羽她……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='NAE')",DynamicDisplayable(mouthanime,"NAE_AMA06"),"True","lh/NAE_AMA06a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("NAE")
    play NAE "FEI04A_NAE0008"
    $ current_voice = "voice/FEI04A_NAE0008.ogg"
    "绹" "「等下，姐姐，那么做的话赶不上的啦！」"
    $ stopvoc("FEI")
    play FEI "FEI04A_FEI0024"
    $ current_voice = "voice/FEI04A_FEI0024.ogg"
    "菲利斯" "「所以要尽早……！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='NAE')",DynamicDisplayable(mouthanime,"NAE_AMA04"),"True","lh/NAE_AMA04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("NAE")
    play NAE "FEI04A_NAE0009"
    $ current_voice = "voice/FEI04A_NAE0009.ogg"
    "绹" "「这个！」"
    "绹酱取出了她的手机。"
    $ stopvoc("FEI")
    play FEI "FEI04A_FEI0025"
    $ current_voice = "voice/FEI04A_FEI0025.ogg"
    "菲利斯" "「啊啊……绹酱，抱歉……我，不知道在想什么……」"
    "我咬紧牙关将自己的心情忍住。"
    "但是理性仿佛决了堤似的，炽热的感情化为了脸上的泪水。"
    "明明必须要冷静地行动的……"
    "明明事关铃羽的生命的……"
    "我抱住绹酱小小的身体，然后用沾满了砂土的手机给天王寺先生打了电话。"
    hide screen phoneSD1
    window hide


    $ loadBG(0,"BG_BLACK")

    hide screen phonebtn
    "………………。"
    window hide


    $ loadBG(0,"BG78N2")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='TEN')",DynamicDisplayable(mouthanime,"TEN_ASA02"),"True","lh/TEN_ASA02a~ipad.png") at right as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    hide lh7 
    show expression ConditionSwitch("renpy.music.get_playing(channel='NAE')",DynamicDisplayable(mouthanime,"NAE_ASA03"),"True","lh/NAE_ASA03a~ipad.png") at left as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    show screen phonebtn
    show screen phoneSD1
    $ stopvoc("TEN")
    play TEN "FEI04A_TEN0006"
    $ current_voice = "voice/FEI04A_TEN0006.ogg"
    "天王寺" "「绹！」"
    "从警车上面下来的天王寺先生面无血色地抱住了他女儿的小身板。"
    $ stopvoc("TEN")
    play TEN "FEI04A_TEN0007"
    $ current_voice = "voice/FEI04A_TEN0007.ogg"
    "天王寺" "「没事吧。有没有受伤！？」"
    $ stopvoc("NAE")
    play NAE "FEI04A_NAE0010"
    $ current_voice = "voice/FEI04A_NAE0010.ogg"
    "绹" "「……没有，没关系」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA01"),"True","lh/OKA_ASA01a~ipad.png") at center as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "FEI04A_OKA0001"
    $ current_voice = "voice/FEI04A_OKA0001.ogg"
    "伦太郎" "「菲利斯！」"
    "在崩塌现场已经有很多警车，救护车还有委员会的人的私家车赶过来了。"
    "冈部和天王寺也一起赶了过来。"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_AMA01"),"True","lh/OKA_AMA01a~ipad.png") at center as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "FEI04A_OKA0002"
    $ current_voice = "voice/FEI04A_OKA0002.ogg"
    "伦太郎" "「没事吧！？　电话里说车站什么的……」"
    $ stopvoc("FEI")
    play FEI "FEI04A_FEI0026"
    $ current_voice = "voice/FEI04A_FEI0026.ogg"
    "菲利斯" "「快去救铃羽……！　赶紧去救她……！」"
    "我抱住冈部，指向那个地狱一般的洞穴。"
    "已经没法说话了，总之至少把意思传达给他了。"
    "泪水不住地涌出，让我的理性一片混乱。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_AMA03"),"True","lh/OKA_AMA03a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "FEI04A_OKA0003"
    $ current_voice = "voice/FEI04A_OKA0003.ogg"
    "伦太郎" "「难道说……铃羽在里面！？」"
    "看着周围的冈部突然僵住了。"
    "我知道他紧张地咽了一口口水。"
    "那样是正常的。"
    "他的眼中是，一定是那个穿过地面的恶魔之口。"
    "内部完全被瓦砾所埋，通向地下的楼梯已经完全被吞没了。"
    "找不到可能可以救出她的空隙。"
    "现场满是绝望。"
    window hide

    stop bgm 


    $ loadBG(0,"BG78N2")


    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='TEN')",DynamicDisplayable(mouthanime,"TEN_ASA02"),"True","lh/TEN_ASA02a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    play bgm "BGM20"
    $ stopvoc("TEN")
    play TEN "FEI04A_TEN0008"
    $ current_voice = "voice/FEI04A_TEN0008.ogg"
    "天王寺" "「这可不得了了呢……」"
    "现场，警官，委员会的人，还有周围的居民还是一起将瓦砾移开。"
    "当然也调用了挖掘机。但是在这个争分夺秒的时刻，剩下的人也在用桶不停地向外运输着瓦砾。"
    $ stopvoc("FEI")
    play FEI "FEI04A_FEI0027"
    $ current_voice = "voice/FEI04A_FEI0027.ogg"
    "菲利斯" "「…………」"
    "我靠着家电量贩店的卷闸门，抱着膝盖，看着他们好不容易前进了几米的样子。"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_AMA05"),"True","lh/OKA_AMA05a~ipad.png") at center as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "FEI04A_OKA0004"
    $ current_voice = "voice/FEI04A_OKA0004.ogg"
    "伦太郎" "「交给大人们也无妨。这里不是我们出场的时候」"
    "冈部好像是担心我的样子，但是我没有从这里离开的打算。"
    "我只是咬着牙关，用自己哭红的双眼，确认着铃羽是否还安然无恙。"
    "冈部小小地叹了口气，在我的身边坐下。"
    $ stopvoc("OKA")
    play OKA "FEI04A_OKA0005"
    $ current_voice = "voice/FEI04A_OKA0005.ogg"
    "伦太郎" "「所以，你也稍微休──」"

    stop bgm 

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_AMA04"),"True","lh/OKA_AMA04a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "FEI04A_OKA0006"
    $ current_voice = "voice/FEI04A_OKA0006.ogg"
    "伦太郎" "「──」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_AMD01"),"True","lh/OKA_AMD01a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "FEI04A_OKA0007"
    $ current_voice = "voice/FEI04A_OKA0007.ogg"
    "伦太郎" "「……咕，唔」"
    $ stopvoc("FEI")
    play FEI "FEI04A_FEI0028"
    $ current_voice = "voice/FEI04A_FEI0028.ogg"
    "菲利斯" "「诶？」"
    "突然，冈部用手捂住头，露出痛苦的表情。"
    $ stopvoc("FEI")
    play FEI "FEI04A_FEI0029"
    $ current_voice = "voice/FEI04A_FEI0029.ogg"
    "菲利斯" "「怎么了？　没事吧？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_AMD02"),"True","lh/OKA_AMD02a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "FEI04A_OKA0008"
    $ current_voice = "voice/FEI04A_OKA0008.ogg"
    "伦太郎" "「咕、哈……哈哈、哈……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_AMD01"),"True","lh/OKA_AMD01a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "FEI04A_OKA0009"
    $ current_voice = "voice/FEI04A_OKA0009.ogg"
    "伦太郎" "「哦，哦哦……、菲利斯、没事……吗」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_AMA01"),"True","lh/OKA_AMA01a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    "他的样子很奇怪。"
    "好像头已经不痛了。"
    "一直盯着我看，好像舒了一口气的样子。"
    $ stopvoc("OKA")
    play OKA "FEI04A_OKA0010"
    $ current_voice = "voice/FEI04A_OKA0010.ogg"
    "伦太郎" "「铃羽的作战好像很顺利的样子呢」"
    $ stopvoc("FEI")
    play FEI "FEI04A_FEI0030"
    $ current_voice = "voice/FEI04A_FEI0030.ogg"
    "菲利斯" "「作战……？」"
    $ stopvoc("OKA")
    play OKA "FEI04A_OKA0011"
    $ current_voice = "voice/FEI04A_OKA0011.ogg"
    "伦太郎" "「为了避免你被活埋的未来，铃羽发送了Ｄｍａｉｌ哦。你的手机也应该收到了」"
    $ stopvoc("FEI")
    play FEI "FEI04A_FEI0031"
    $ current_voice = "voice/FEI04A_FEI0031.ogg"
    "菲利斯" "「────」"
    "是吗，那封邮件是……"
    $ stopvoc("FEI")
    play FEI "FEI04A_FEI0032"
    $ current_voice = "voice/FEI04A_FEI0032.ogg"
    "菲利斯" "「……但是，铃羽她……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_AMA03"),"True","lh/OKA_AMA03a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "FEI04A_OKA0012"
    $ current_voice = "voice/FEI04A_OKA0012.ogg"
    "伦太郎" "「什么？　怎么回事？　你快说明一下！」"
    "我于是又向不知为何看起来满脸疑惑的冈部说明了一次她代替我被活埋的事实。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_AMD01"),"True","lh/OKA_AMD01a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "FEI04A_OKA0013"
    $ current_voice = "voice/FEI04A_OKA0013.ogg"
    "伦太郎" "「啧，这样啊……、结果变成这样了……！」"
    $ stopvoc("FEI")
    play FEI "FEI04A_FEI0033"
    $ current_voice = "voice/FEI04A_FEI0033.ogg"
    "菲利斯" "「…………」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='TEN')",DynamicDisplayable(mouthanime,"TEN_AMA01"),"True","lh/TEN_AMA01a~ipad.png") at center as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    play bgm "BGM10"
    $ stopvoc("TEN")
    play TEN "FEI04A_TEN0009"
    $ current_voice = "voice/FEI04A_TEN0009.ogg"
    "天王寺" "「小姑娘，虽然我知道你很担心，但这里还是交给我吧」"
    "天王寺先生也朝这边走了过来。"
    "冈部默默地站了起来，将那个位置让给了天王寺先生，走到能看清现场情况的地方去了。"
    $ stopvoc("TEN")
    play TEN "FEI04A_TEN0010"
    $ current_voice = "voice/FEI04A_TEN0010.ogg"
    "天王寺" "「就那么不信任大人们吗？」"
    $ stopvoc("FEI")
    play FEI "FEI04A_FEI0034"
    $ current_voice = "voice/FEI04A_FEI0034.ogg"
    "菲利斯" "「…………」"
    $ stopvoc("TEN")
    play TEN "FEI04A_TEN0011"
    $ current_voice = "voice/FEI04A_TEN0011.ogg"
    "天王寺" "「……嘛，确实不能否定呢。大人们就是这么不会手下留情，就算对方是孩子也会将其击溃的」"
    $ stopvoc("FEI")
    play FEI "FEI04A_FEI0035"
    $ current_voice = "voice/FEI04A_FEI0035.ogg"
    "菲利斯" "「…………」"
    $ stopvoc("TEN")
    play TEN "FEI04A_TEN0012"
    $ current_voice = "voice/FEI04A_TEN0012.ogg"
    "天王寺" "「…………」"
    $ stopvoc("TEN")
    play TEN "FEI04A_TEN0013"
    $ current_voice = "voice/FEI04A_TEN0013.ogg"
    "天王寺" "「真是抱歉了，这次的事情」"
    $ stopvoc("FEI")
    play FEI "FEI04A_FEI0036"
    $ current_voice = "voice/FEI04A_FEI0036.ogg"
    "菲利斯" "「…………」"
    $ stopvoc("TEN")
    play TEN "FEI04A_TEN0014"
    $ current_voice = "voice/FEI04A_TEN0014.ogg"
    "天王寺" "「并不是想把你排除在外」"
    $ stopvoc("FEI")
    play FEI "FEI04A_FEI0037"
    $ current_voice = "voice/FEI04A_FEI0037.ogg"
    "菲利斯" "「…………」"
    $ stopvoc("TEN")
    play TEN "FEI04A_TEN0015"
    $ current_voice = "voice/FEI04A_TEN0015.ogg"
    "天王寺" "「那些决定欺骗大家的委员会的成员已经辞退了哦」"
    $ stopvoc("TEN")
    play TEN "FEI04A_TEN0016"
    $ current_voice = "voice/FEI04A_TEN0016.ogg"
    "天王寺" "「这就是所谓大人的责任吗」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    "天王寺先生一直看着现场的进度。"
    "那里只有一种信念。"
    "不会被动摇，贯彻到底的强劲。"
    "但是事态却向令人动摇的方向展开。"

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='TEN')",DynamicDisplayable(mouthanime,"TEN_AMA02"),"True","lh/TEN_AMA02a~ipad.png") at center as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("TEN")
    play TEN "FEI04A_TEN0017"
    $ current_voice = "voice/FEI04A_TEN0017.ogg"
    "天王寺" "「喂，怎么了吗！」"
    $ stopvoc("Y14")
    play KUR "FEI04A_Y140000"
    $ current_voice = "voice/FEI04A_Y140000.ogg"
    "操作员" "「那个……瓦砾现在保持着微妙的平衡，如果现在继续挖掘的话，有可能会全部塌陷，里面的女孩子就糟糕了」"
    $ stopvoc("FEI")
    play FEI "FEI04A_FEI0038"
    $ current_voice = "voice/FEI04A_FEI0038.ogg"
    "菲利斯" "「这种事怎么可以！」"
    "我毫不犹豫地站了起来。"
    $ stopvoc("TEN")
    play TEN "FEI04A_TEN0018"
    $ current_voice = "voice/FEI04A_TEN0018.ogg"
    "天王寺" "「冷静下来，小姑娘」"
    $ stopvoc("FEI")
    play FEI "FEI04A_FEI0039"
    $ current_voice = "voice/FEI04A_FEI0039.ogg"
    "菲利斯" "「但是铃羽她！」"
    $ stopvoc("TEN")
    play TEN "FEI04A_TEN0019"
    $ current_voice = "voice/FEI04A_TEN0019.ogg"
    "天王寺" "「好了」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='TEN')",DynamicDisplayable(mouthanime,"TEN_AMA01"),"True","lh/TEN_AMA01a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("TEN")
    play TEN "FEI04A_TEN0020"
    $ current_voice = "voice/FEI04A_TEN0020.ogg"
    "天王寺" "「……相信她吧」"
    $ stopvoc("FEI")
    play FEI "FEI04A_FEI0040"
    $ current_voice = "voice/FEI04A_FEI0040.ogg"
    "菲利斯" "「…………」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='TEN')",DynamicDisplayable(mouthanime,"TEN_AMA02"),"True","lh/TEN_AMA02a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("TEN")
    play TEN "FEI04A_TEN0021"
    $ current_voice = "voice/FEI04A_TEN0021.ogg"
    "天王寺" "「其他的方法呢？」"
    $ stopvoc("Y14")
    play KUR "FEI04A_Y140001"
    $ current_voice = "voice/FEI04A_Y140001.ogg"
    "操作员" "「挖开道路来确保别的脱逃口什么的吧……但总之现在的这个地方是没办法了」"
    "我握紧双手。"
    $ stopvoc("Y14")
    play KUR "FEI04A_Y140002"
    $ current_voice = "voice/FEI04A_Y140002.ogg"
    "操作员" "「总之我们已经设法朝着能看到人影的地方挖了，但是在这之上就很困难了」"
    $ stopvoc("TEN")
    play TEN "FEI04A_TEN0022"
    $ current_voice = "voice/FEI04A_TEN0022.ogg"
    "天王寺" "「没法从缝隙之间拉出来吗？」"
    $ stopvoc("Y14")
    play KUR "FEI04A_Y140003"
    $ current_voice = "voice/FEI04A_Y140003.ogg"
    "操作员" "「不太可能，缝隙太窄了。大概连小孩子都钻不过去的程度……」"
    $ stopvoc("FEI")
    play FEI "FEI04A_FEI0041"
    $ current_voice = "voice/FEI04A_FEI0041.ogg"
    "菲利斯" "「……让我去」"
    $ stopvoc("TEN")
    play TEN "FEI04A_TEN0023"
    $ current_voice = "voice/FEI04A_TEN0023.ogg"
    "天王寺" "「不行」"
    "那是仿佛已经看出了我会这么说的快速回答。"
    "但是我不会放弃的。"
    $ stopvoc("FEI")
    play FEI "FEI04A_FEI0042"
    $ current_voice = "voice/FEI04A_FEI0042.ogg"
    "菲利斯" "「我身材小，所以才有可能能过去」"
    $ stopvoc("TEN")
    play TEN "FEI04A_TEN0024"
    $ current_voice = "voice/FEI04A_TEN0024.ogg"
    "天王寺" "「不行」"
    $ stopvoc("FEI")
    play FEI "FEI04A_FEI0043"
    $ current_voice = "voice/FEI04A_FEI0043.ogg"
    "菲利斯" "「我发誓过要去帮助铃羽的……」"
    $ stopvoc("TEN")
    play TEN "FEI04A_TEN0025"
    $ current_voice = "voice/FEI04A_TEN0025.ogg"
    "天王寺" "「…………」"
    "天王寺先生第一次看着我的眼睛。"
    "那是仿佛能够看穿我内心深处的眼神。"
    "然后眼神突然变得缓和了。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='TEN')",DynamicDisplayable(mouthanime,"TEN_AMA03"),"True","lh/TEN_AMA03a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("TEN")
    play TEN "FEI04A_TEN0026"
    $ current_voice = "voice/FEI04A_TEN0026.ogg"
    "天王寺" "「……诶呀诶呀，真是的，一脉相承啊」"
    $ stopvoc("FEI")
    play FEI "FEI04A_FEI0044"
    $ current_voice = "voice/FEI04A_FEI0044.ogg"
    "菲利斯" "「……诶？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='TEN')",DynamicDisplayable(mouthanime,"TEN_AMA01"),"True","lh/TEN_AMA01a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("TEN")
    play TEN "FEI04A_TEN0027"
    $ current_voice = "voice/FEI04A_TEN0027.ogg"
    "天王寺" "「我是在说秋叶幸高哦，你有和你爸爸一样的眼神。」"
    $ stopvoc("TEN")
    play TEN "FEI04A_TEN0028"
    $ current_voice = "voice/FEI04A_TEN0028.ogg"
    "天王寺" "「那个人也是可以为了自己的信念而牺牲一切的人。所以你妈妈才会选择跟着他啊」"
    $ stopvoc("FEI")
    play FEI "FEI04A_FEI0045"
    $ current_voice = "voice/FEI04A_FEI0045.ogg"
    "菲利斯" "「和爸爸……」"
    "……一样的眼神？"

    show expression ConditionSwitch("renpy.music.get_playing(channel='TEN')",DynamicDisplayable(mouthanime,"TEN_AMA02"),"True","lh/TEN_AMA02a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("TEN")
    play TEN "FEI04A_TEN0029"
    $ current_voice = "voice/FEI04A_TEN0029.ogg"
    "天王寺" "「好嘞，那你和你就上吧！　代替我和我女儿去吧」"
    $ stopvoc("FEI")
    play FEI "FEI04A_FEI0046"
    $ current_voice = "voice/FEI04A_FEI0046.ogg"
    "菲利斯" "「天王寺、先生……？」"
    $ stopvoc("TEN")
    play TEN "FEI04A_TEN0030"
    $ current_voice = "voice/FEI04A_TEN0030.ogg"
    "天王寺" "「谁拿个绳子过来啊，还有给点光」"
    window hide

    hide lh7 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_AMA03"),"True","lh/OKA_AMA03a~ipad.png") at right_t as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "FEI04A_OKA0014"
    $ current_voice = "voice/FEI04A_OKA0014.ogg"
    "伦太郎" "「等，等一下Ｍｒ．布朗！　你打算让菲利斯做什么啊！」"
    $ stopvoc("FEI")
    play FEI "FEI04A_FEI0047"
    $ current_voice = "voice/FEI04A_FEI0047.ogg"
    "菲利斯" "「冈部，这是我自己的决定」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_AMA01"),"True","lh/OKA_AMA01a~ipad.png") as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "FEI04A_OKA0015"
    $ current_voice = "voice/FEI04A_OKA0015.ogg"
    "伦太郎" "「冈部……？　菲利斯你……」"
    $ stopvoc("FEI")
    play FEI "FEI04A_FEI0048"
    $ current_voice = "voice/FEI04A_FEI0048.ogg"
    "菲利斯" "「没关系、肯定会回来的。……和铃羽一起」"
    window hide

    stop bgm 



    $ loadBG(0,"BG_BLACK")

    "那里一片漆黑。瓦砾的间隙十分狭窄，也不知道我能不能穿过去。灰尘也到处都是。"
    window hide


    $ loadBG(0,"BG71N")

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='TEN')",DynamicDisplayable(mouthanime,"TEN_AMA01"),"True","lh/TEN_AMA01a~ipad.png") at center as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    play bgm "FD2BGM08"
    $ stopvoc("TEN")
    play TEN "FEI04A_TEN0031"
    $ current_voice = "voice/FEI04A_TEN0031.ogg"
    "天王寺" "「如果找到了打工的的话就给个信号，你拉一下脚上绑着的绳子我们就会把你拉出来。」"
    $ stopvoc("TEN")
    play TEN "FEI04A_TEN0032"
    $ current_voice = "voice/FEI04A_TEN0032.ogg"
    "天王寺" "「这是小型对讲机。使用的时候按下这个按钮就可以了」"
    $ stopvoc("FEI")
    play FEI "FEI04A_FEI0049"
    $ current_voice = "voice/FEI04A_FEI0049.ogg"
    "菲利斯" "「我明白了」"
    $ stopvoc("FEI")
    play FEI "FEI04A_FEI0050"
    $ current_voice = "voice/FEI04A_FEI0050.ogg"
    "菲利斯" "「说起来，这个……」"
    window hide


    $ loadBG(2,"IBG008A",png=True)




    "我将从口袋里取出来的东西，给天王寺先生看了。"
    "那是在这里找到的，那枚子弹。"
    window hide
    hide background-png 




    show expression ConditionSwitch("renpy.music.get_playing(channel='TEN')",DynamicDisplayable(mouthanime,"TEN_AMA02"),"True","lh/TEN_AMA02a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("TEN")
    play TEN "FEI04A_TEN0033"
    $ current_voice = "voice/FEI04A_TEN0033.ogg"
    "天王寺" "「这，这个是……？」"
    $ stopvoc("FEI")
    play FEI "FEI04A_FEI0051"
    $ current_voice = "voice/FEI04A_FEI0051.ogg"
    "菲利斯" "「在下面找到的。我是想交给警察他们……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='TEN')",DynamicDisplayable(mouthanime,"TEN_AMA01"),"True","lh/TEN_AMA01a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("TEN")
    play TEN "FEI04A_TEN0034"
    $ current_voice = "voice/FEI04A_TEN0034.ogg"
    "天王寺" "「这样啊……。说起来，这件事和谁说过了吗？」"
    $ stopvoc("FEI")
    play FEI "FEI04A_FEI0052"
    $ current_voice = "voice/FEI04A_FEI0052.ogg"
    "菲利斯" "「没有。我本来就是想先和大人谈谈这件事」"
    $ stopvoc("TEN")
    play TEN "FEI04A_TEN0035"
    $ current_voice = "voice/FEI04A_TEN0035.ogg"
    "天王寺" "「我明白了，这件事就交给我吧。你就担心打工的的事情就行了」"
    $ stopvoc("FEI")
    play FEI "FEI04A_FEI0053"
    $ current_voice = "voice/FEI04A_FEI0053.ogg"
    "菲利斯" "「……恩」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    "为了保证安全，我借来了施工用的头盔，然后把对讲机装在了头盔上。"
    "——是啊，就算不说我也知道。"
    "铃羽救了我。我一定会。"
    "确认准备完成之后，我缓缓地将身体挤入瓦砾的缝隙之间。"
    hide screen phoneSD1
    window hide
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_FEI004A"]]["Check"]=True


















    $ loadBG(0,"EV_FEI004A")

    hide screen phonebtn
    play se "SGSE376"

    "瓦砾之间的缝隙窄到连肘部的活动都要十分小心，因此我一直采取着细微的动作。"
    "双手确认着前方的情况，找到撑起来最安全的地方之后，我一口气钻进了瓦砾之中。"
    "那一步连１０厘米都没有，但是我就这么一步又一步地缩短着距离。"
    "到处都能听到吱嘎吱嘎的声音。"
    "那仿佛就是铃羽的悲鸣，包含着绝望的感情，夺取着我的冷静。"
    "而且灰尘也很厉害。要是下意识地咳嗽的话，就有可能会让这里全部崩坏也说不定。"
    "必须要忍耐。总之除了忍耐别无他法。"
    "眼前是精疲力尽的铃羽。"
    window hide
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_FEI004B"]]["Check"]=True


    $ loadBG(2,"EV_FEI004B")



    $ stopvoc("FEI")
    play FEI "FEI04A_FEI0054"
    $ current_voice = "voice/FEI04A_FEI0054.ogg"
    "菲利斯" "「铃羽……、铃羽……！」"
    "是意识还没有恢复吗，我叫了几声也没有反应。"
    "…………。"
    "……难道说，不对，不能考虑那种可能性。"
    "我驱散几乎要将自己压垮的不安，和之前一样向着前方的瓦砾伸出手去。……就在那时。"
    play se "SGSE371"

    "手刚动起来的时候，按到了无线对讲机的开关。"
    "必须要关掉。那么想着的时候——"
    window hide
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_FEI004C"]]["Check"]=True


    $ loadBG(2,"EV_FEI004C")



    $ stopvoc("OKA")
    play OKA "FEI04A_OKA0016"
    $ current_voice = "voice/FEI04A_OKA0016.ogg"
    "伦太郎" "「为什么让她就进去了啊，Ｍｒ．布朗」"
    "从耳机里传来了冈部的声音。"
    $ stopvoc("TEN")
    play TEN "FEI04A_TEN0036"
    $ current_voice = "voice/FEI04A_TEN0036.ogg"
    "天王寺" "「是那家伙决定的事情啊」"
    "然后是天王寺先生的。到底，在说些什么啊……"
    "难道说，虽然我无意中打开了对讲机，但是那边没有注意到的样子？"
    play se "SGSE376"
    "我一边在瓦砾中前进，一边听着从耳机里放出来的声音。"
    $ stopvoc("OKA")
    play OKA "FEI04A_OKA0017"
    $ current_voice = "voice/FEI04A_OKA0017.ogg"
    "伦太郎" "「就算是菲利斯决定的事情，你阻止下来的话不就好了……」"
    $ stopvoc("TEN")
    play TEN "FEI04A_TEN0037"
    $ current_voice = "voice/FEI04A_TEN0037.ogg"
    "天王寺" "「……那种事情是做不到的啊」"
    $ stopvoc("OKA")
    play OKA "FEI04A_OKA0018"
    $ current_voice = "voice/FEI04A_OKA0018.ogg"
    "伦太郎" "「为什么！？」"
    $ stopvoc("TEN")
    play TEN "FEI04A_TEN0038"
    $ current_voice = "voice/FEI04A_TEN0038.ogg"
    "天王寺" "「那家伙也是大人了啊」"
    "……！"
    $ stopvoc("OKA")
    play OKA "FEI04A_OKA0019"
    $ current_voice = "voice/FEI04A_OKA0019.ogg"
    "伦太郎" "「……大人？」"
    $ stopvoc("TEN")
    play TEN "FEI04A_TEN0039"
    $ current_voice = "voice/FEI04A_TEN0039.ogg"
    "天王寺" "「是啊，大人就是要决定自己的责任啊。相信她也是大人的工作啊」"
    "天王寺先生……"
    $ stopvoc("TEN")
    play TEN "FEI04A_TEN0040"
    $ current_voice = "voice/FEI04A_TEN0040.ogg"
    "天王寺" "「呐冈部，所谓大人呢，就是出了什么事情都会自己解决的家伙」"
    $ stopvoc("TEN")
    play TEN "FEI04A_TEN0041"
    $ current_voice = "voice/FEI04A_TEN0041.ogg"
    "天王寺" "「对于自己的行动有着自己的责任，失败的话也会接受被埋在那个洞里」"
    $ stopvoc("TEN")
    play TEN "FEI04A_TEN0042"
    $ current_voice = "voice/FEI04A_TEN0042.ogg"
    "天王寺" "「那家伙就是这样，在大人中斗争过来的呢」"
    $ stopvoc("OKA")
    play OKA "FEI04A_OKA0020"
    $ current_voice = "voice/FEI04A_OKA0020.ogg"
    "伦太郎" "「……菲利斯吗？」"
    "…………。"
    $ stopvoc("TEN")
    play TEN "FEI04A_TEN0043"
    $ current_voice = "voice/FEI04A_TEN0043.ogg"
    "天王寺" "「那家伙作为这街道的主人的家族生下来，对于这条街道爱的比谁都要深」"
    $ stopvoc("TEN")
    play TEN "FEI04A_TEN0044"
    $ current_voice = "voice/FEI04A_TEN0044.ogg"
    "天王寺" "「因为父亲遭遇事故去世了，所以这样的感情变得更加强烈」"
    $ stopvoc("TEN")
    play TEN "FEI04A_TEN0045"
    $ current_voice = "voice/FEI04A_TEN0045.ogg"
    "天王寺" "「这是爸爸爱着的街道，所以我要守护它……于是，就和大人们混在一起为了这条街道的繁荣而努力着」"
    $ stopvoc("OKA")
    play OKA "FEI04A_OKA0021"
    $ current_voice = "voice/FEI04A_OKA0021.ogg"
    "伦太郎" "「菲利斯……」"
    $ stopvoc("TEN")
    play TEN "FEI04A_TEN0046"
    $ current_voice = "voice/FEI04A_TEN0046.ogg"
    "天王寺" "「但那是很不容易的啊。不光光是个孩子，而且还是个女孩子」"
    $ stopvoc("TEN")
    play TEN "FEI04A_TEN0047"
    $ current_voice = "voice/FEI04A_TEN0047.ogg"
    "天王寺" "「那家伙的周围，都是一群被蜜糖吸引了的蚂蚁那样贪婪的大人」"
    $ stopvoc("TEN")
    play TEN "FEI04A_TEN0048"
    $ current_voice = "voice/FEI04A_TEN0048.ogg"
    "天王寺" "「被欺骗，被背叛，被伤害……不知道有多少次受挫，偷偷地哭泣过」"
    $ stopvoc("OKA")
    play OKA "FEI04A_OKA0022"
    $ current_voice = "voice/FEI04A_OKA0022.ogg"
    "伦太郎" "「你也有过吧」"
    $ stopvoc("TEN")
    play TEN "FEI04A_TEN0049"
    $ current_voice = "voice/FEI04A_TEN0049.ogg"
    "天王寺" "「我也有极限的啊。但是呢……」"
    $ stopvoc("TEN")
    play TEN "FEI04A_TEN0050"
    $ current_voice = "voice/FEI04A_TEN0050.ogg"
    "天王寺" "「就算那种时候，她也一个人坚持着，和那些怀着恶意的大人们斡旋，贯彻着自己给自己定下的责任。」"
    "…………。"
    $ stopvoc("OKA")
    play OKA "FEI04A_OKA0023"
    $ current_voice = "voice/FEI04A_OKA0023.ogg"
    "伦太郎" "「菲利斯还有这样的过去啊……」"
    $ stopvoc("TEN")
    play TEN "FEI04A_TEN0051"
    $ current_voice = "voice/FEI04A_TEN0051.ogg"
    "天王寺" "「她肯定是不会说的。那家伙就是这样的人」"
    $ stopvoc("TEN")
    play TEN "FEI04A_TEN0052"
    $ current_voice = "voice/FEI04A_TEN0052.ogg"
    "天王寺" "「想要认清自己……所以才会穿那种花哨的衣服啊」"
    $ stopvoc("TEN")
    play TEN "FEI04A_TEN0053"
    $ current_voice = "voice/FEI04A_TEN0053.ogg"
    "天王寺" "「那家伙其实比谁都要纯粹而容易受伤」"
    $ stopvoc("TEN")
    play TEN "FEI04A_TEN0054"
    $ current_voice = "voice/FEI04A_TEN0054.ogg"
    "天王寺" "「所以为了保护那么单纯的自己，她必须带着地区之主的女儿・秋叶留未穗和几乎就要变成她的真实性格的名为菲利斯的面具。」"
    $ stopvoc("TEN")
    play TEN "FEI04A_TEN0055"
    $ current_voice = "voice/FEI04A_TEN0055.ogg"
    "天王寺" "「……那就是她啊」"
    "天王寺先生。"
    window hide
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_FEI004D"]]["Check"]=True


    $ loadBG(2,"EV_FEI004D")



    play se "SGSE376"
    $ stopvoc("TEN")
    play TEN "FEI04A_TEN0056"
    $ current_voice = "voice/FEI04A_TEN0056.ogg"
    "天王寺" "「那些本来是我们必须要做的事情，却被她抢先给做掉」"
    $ stopvoc("TEN")
    play TEN "FEI04A_TEN0057"
    $ current_voice = "voice/FEI04A_TEN0057.ogg"
    "天王寺" "「……那家伙才是，这条街道的英雄啊」"
    "天王寺先生，是这样看我的啊……"
    "注意到的时候，我的脸上又沾满了泪水。"
    "虽然感觉自己对大人的世界了解了，但是却无法理解为什么会流泪。"
    window hide


    $ loadBG(0,"BG78N2")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='TEN')",DynamicDisplayable(mouthanime,"TEN_AMA01"),"True","lh/TEN_AMA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    $ stopvoc("TEN")
    play TEN "FEI04A_TEN0058"
    $ current_voice = "voice/FEI04A_TEN0058.ogg"
    "我是在说秋叶幸高哦，你有和你爸爸一样的眼神。"
    window hide


    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_FEI004A"]]["Check"]=True
    $ loadBG(0,"EV_FEI004A")


    "……是啊，不变成大人的话。"
    "变成像爸爸那样，优秀的大人的话……"
    "到铃羽的位置还有一点距离。"
    "稍微再过一会，应该就能到达用手能摸到她的地方了。"
    "必须负起自己的责任。这才是，真正的大人……"
    "这三天想起了真的是既漫长又短暂。"
    "和铃羽一起寻找蜥蜴人，让她留宿，和她一起欢笑。"
    "就算如此还是吵架了……"
    "像孩子一样说了任性的话。"
    "后悔也迟了，机会只有一次。"
    "…………"
    "我还没有和她道歉。"
    "就那么吵着架分开绝对不要。"
    "必须和铃羽道歉。"
    "在她踏上旅途之前。"
    "所以绝对要把她救出来。"
    "不想再次失去重要的人。"
    "注意到的时候，眼前已经是铃羽面无血色的脸了。"
    "手腕脱力地下垂着。"
    window hide
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_FEI004B"]]["Check"]=True


    $ loadBG(2,"EV_FEI004B")



    "伸出手去！"
    "……还差一点就够到了。"
    "够到吧！够到吧！够到吧！"
    window hide


    $ loadBG(0,"BG_WHITE")

    "…………！"
    "那个瞬间，我的指尖碰到了铃羽温暖的手——"
    window hide

    stop bgm 
    scene expression Solid("000000")  with fade



    $ loadBG(0,"BG11N5")


    play se "SGSE366L" loop

    show screen phonebtn
    show screen phoneSD1
    "和刚才相比刮起了一些风，空气也变湿了一些。"
    "应该是下了点雨吧。"
    "但是我毫不在意地一个人站在那里。"
    "眼前是破损严重的屋顶。"
    "应该在那里的东西已经消失了。"
    "我只是，呆呆地眺望着。"
    "…………。"
    "在那之后铃羽就以失去意识的状态被救护车送到了医院。"
    "……不对，应该是送到了。"
    "但是我之后赶到的时候，她已经不见了。"
    "我是知道她去了哪里的。"
    "她是用时间机器前往过去了。"
    "与我没有告别，我还没有为吵架的事道歉就……"
    window hide

    play se "SGSE084"



    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA01"),"True","lh/OKA_ASA01a~ipad.png") at center as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "FEI04A_OKA0024"
    $ current_voice = "voice/FEI04A_OKA0024.ogg"
    "伦太郎" "「……你在这种地方啊」"
    $ stopvoc("FEI")
    play FEI "FEI04A_FEI0055"
    $ current_voice = "voice/FEI04A_FEI0055.ogg"
    "菲利斯" "「…………」"
    $ stopvoc("OKA")
    play OKA "FEI04A_OKA0025"
    $ current_voice = "voice/FEI04A_OKA0025.ogg"
    "伦太郎" "「铃羽有拜托我转告你」"
    $ stopvoc("FEI")
    play FEI "FEI04A_FEI0056"
    $ current_voice = "voice/FEI04A_FEI0056.ogg"
    "菲利斯" "「……！？」"
    $ stopvoc("OKA")
    play OKA "FEI04A_OKA0026"
    $ current_voice = "voice/FEI04A_OKA0026.ogg"
    "伦太郎" "「连告别都没有说就出发了，这样」"
    "…………。"
    $ stopvoc("OKA")
    play OKA "FEI04A_OKA0027"
    $ current_voice = "voice/FEI04A_OKA0027.ogg"
    "伦太郎" "「她非常的急，好像是错过了预定的时间的话就完蛋了的样子」"
    $ stopvoc("FEI")
    play FEI "FEI04A_FEI0057"
    $ current_voice = "voice/FEI04A_FEI0057.ogg"
    "菲利斯" "「…………」"
    $ stopvoc("OKA")
    play OKA "FEI04A_OKA0028"
    $ current_voice = "voice/FEI04A_OKA0028.ogg"
    "伦太郎" "「那家伙也说过啊。在这之后的旅行是孤独的，十分的可怕哦。」"
    $ stopvoc("OKA")
    play OKA "FEI04A_OKA0029"
    $ current_voice = "voice/FEI04A_OKA0029.ogg"
    "伦太郎" "「但是好像已经不可怕了。那是因为菲利斯……」"
    $ stopvoc("OKA")
    play OKA "FEI04A_OKA0030"
    $ current_voice = "voice/FEI04A_OKA0030.ogg"
    "伦太郎" "「──有你的陪伴啊」"
    $ stopvoc("FEI")
    play FEI "FEI04A_FEI0058"
    $ current_voice = "voice/FEI04A_FEI0058.ogg"
    "菲利斯" "「……！」"
    $ stopvoc("OKA")
    play OKA "FEI04A_OKA0031"
    $ current_voice = "voice/FEI04A_OKA0031.ogg"
    "伦太郎" "「因为你成为了她的挚友，所以旅途已经不再可怕了」"
    $ stopvoc("OKA")
    play OKA "FEI04A_OKA0032"
    $ current_voice = "voice/FEI04A_OKA0032.ogg"
    "伦太郎" "「因为旅途的前方，还能再次见到你的……」"
    $ stopvoc("FEI")
    play FEI "FEI04A_FEI0059"
    $ current_voice = "voice/FEI04A_FEI0059.ogg"
    "菲利斯" "「冈部……」"
    $ stopvoc("OKA")
    play OKA "FEI04A_OKA0033"
    $ current_voice = "voice/FEI04A_OKA0033.ogg"
    "伦太郎" "「我只是在转述她的话而已。关于向过去旅行这部分，你可以随意自己想象」"
    $ stopvoc("FEI")
    play FEI "FEI04A_FEI0060"
    $ current_voice = "voice/FEI04A_FEI0060.ogg"
    "菲利斯" "「……恩」"
    $ stopvoc("OKA")
    play OKA "FEI04A_OKA0034"
    $ current_voice = "voice/FEI04A_OKA0034.ogg"
    "伦太郎" "「还有菲利斯，铃羽也这么说了」"
    $ stopvoc("FEI")
    play FEI "FEI04A_FEI0061"
    $ current_voice = "voice/FEI04A_FEI0061.ogg"
    "菲利斯" "「……诶？」"
    $ stopvoc("OKA")
    play OKA "FEI04A_OKA0035"
    $ current_voice = "voice/FEI04A_OKA0035.ogg"
    "伦太郎" "「菲利斯好不容易找到了取回率真的自己的方法，所以应该诚实地面对自己的心情，不要再说和母亲之间的疏远很难过之类的，而是设法消除你们之间的隔阂」"
    $ stopvoc("OKA")
    play OKA "FEI04A_OKA0036"
    $ current_voice = "voice/FEI04A_OKA0036.ogg"
    "伦太郎" "「我虽然没能和爸爸见面，但是不希望Ｂｏｓｓ留下那种悲伤的回忆，这么说……」"
    $ stopvoc("OKA")
    play OKA "FEI04A_OKA0037"
    $ current_voice = "voice/FEI04A_OKA0037.ogg"
    "伦太郎" "「与家人不和，形同陌路的话，是非常不幸的……」"
    $ stopvoc("FEI")
    play FEI "FEI04A_FEI0062"
    $ current_voice = "voice/FEI04A_FEI0062.ogg"
    "菲利斯" "「……！」"
    $ stopvoc("OKA")
    play OKA "FEI04A_OKA0038"
    $ current_voice = "voice/FEI04A_OKA0038.ogg"
    "伦太郎" "「那么铃羽的话就传达完毕了，你也赶紧回去休息吧」"
    $ stopvoc("FEI")
    play FEI "FEI04A_FEI0063"
    $ current_voice = "voice/FEI04A_FEI0063.ogg"
    "菲利斯" "「为什么……」"
    $ stopvoc("OKA")
    play OKA "FEI04A_OKA0039"
    $ current_voice = "voice/FEI04A_OKA0039.ogg"
    "伦太郎" "「……嗯？」"
    $ stopvoc("FEI")
    play FEI "FEI04A_FEI0064"
    $ current_voice = "voice/FEI04A_FEI0064.ogg"
    "菲利斯" "「为什么，就这么走了啊……」"
    $ stopvoc("FEI")
    play FEI "FEI04A_FEI0065"
    $ current_voice = "voice/FEI04A_FEI0065.ogg"
    "菲利斯" "「明明还想要好好地和你道别的……」"
    $ stopvoc("FEI")
    play FEI "FEI04A_FEI0066"
    $ current_voice = "voice/FEI04A_FEI0066.ogg"
    "菲利斯" "「明明还想要好好地和你道歉的……」"
    $ stopvoc("FEI")
    play FEI "FEI04A_FEI0067"
    $ current_voice = "voice/FEI04A_FEI0067.ogg"
    "菲利斯" "「明明还想要亲口把道歉的话说给你听的……！」"
    $ stopvoc("FEI")
    play FEI "FEI04A_FEI0068"
    $ current_voice = "voice/FEI04A_FEI0068.ogg"
    "菲利斯" "「为什么……」"
    $ stopvoc("FEI")
    play FEI "FEI04A_FEI0069"
    $ current_voice = "voice/FEI04A_FEI0069.ogg"
    "菲利斯" "「为什么……」"
    window hide

    play se "SGSE068L" loop


    stop se



    $ loadBG(2,"BG_BLACK")




    "那一天，雨点从毛毛细雨，逐渐变成了倾盆大雨，仿佛是上天对我的谴责——"

    hide screen phoneSD1
    window hide

    stop se

    stop bgm 
    hide screen phonebtn
    scene expression Solid("000000")  with fade

    stop se
    stop bgm 


    return













    return
