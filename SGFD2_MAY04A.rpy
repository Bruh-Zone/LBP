label SGFD2_MAY04A:
    hide screen phonebtn
    scene expression Solid("000000")  with fade

    window hide


    $ loadBG(0,"BG55N1")


    play bgm "BGM05"

    $ date="8/17"
    $ day="TUE"
    show screen phonebtn
    show screen phoneSD1


    python:
        SndMail(64)
        RcvMail(370)
    play se phonemailring

    "虽然之前已经联系过家里人，说今天要晚一点回家。现在又给爸爸打电话说「错过了末班电车，可以在红莉栖酱的宾馆住一夜吗？」，于是得到了允许。"
    "是因为这通电话太突然了么，爸爸慌张得要命，误以为真由喜成为了不良少女，闹出了大乱子。"
    "不过，红莉栖酱接过了电话，向爸爸清晰地解释了原因，漂亮地说服了爸爸。"
    "往常要是提前联系说要在别人那里过夜的话都是没问题的，爸爸这次这么慌张有点让我吓了一跳。"

    call CHECK_RM_RECEIVE
    "就这样顺利得到过夜的许可之后，两个人在便利店买了点心之类的东西，来到了红莉栖酱的宾馆。"

    $ gd["RCVmailData"][gc["ScriptMacros"]["RM_MAY_RECV_FEI01_01"]]["late"]=True
    $ lml.append(gc["ScriptMacros"]["RM_MAY_RECV_FEI01_01"])

    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASA01"),"True","lh/CRS_ASA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0000"
    $ current_voice = "voice/MAY04A_MAY0000.ogg"
    "真由理" "「诶嘿嘿，能与红莉栖酱一起过夜，好高兴啊。谢谢你帮真由喜说服了爸爸。要是真由喜的话，可能说服不了？」"
    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0000"
    $ current_voice = "voice/MAY04A_CRS0000.ogg"
    "真由理" "「因为我已经习惯了去驳倒别人。虽然自己知道这一点也不可爱，但这已经变成了像习惯一样的东西了」"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0001"
    $ current_voice = "voice/MAY04A_MAY0001.ogg"
    "真由理" "「真没想到爸爸会慌张到那个样子啊～。平常说要在Ｌａｂ过夜也完全没问题的啊？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASC05"),"True","lh/CRS_ASC05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0001"
    $ current_voice = "voice/MAY04A_CRS0001.ogg"
    "真由理" "「但是，真由理，你只说了『今天太晚了，我就在宾馆过夜了！♪』不是么？　被往坏处想了也不奇怪啊」"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0002"
    $ current_voice = "voice/MAY04A_MAY0002.ogg"
    "真由理" "「诶诶诶？　真由喜觉得Ｌａｂ和宾馆没什么区别呀～？」"
    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0002"
    $ current_voice = "voice/MAY04A_CRS0002.ogg"
    "红莉栖" "「……那要看是什么宾馆了。那个……根据状况来看，是被误会成不太好的宾馆了」"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0003"
    $ current_voice = "voice/MAY04A_MAY0003.ogg"
    "真由理" "「宾馆还分为好的和不好的啊～？」"
    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0003"
    $ current_voice = "voice/MAY04A_CRS0003.ogg"
    "红莉栖" "「嘛、嘛……是……啊。放心吧」，我住的宾馆并不是什么不正经的宾馆」"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0004"
    $ current_voice = "voice/MAY04A_MAY0004.ogg"
    "真由理" "「嗯～，不正经～？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASB09"),"True","lh/CRS_ASB09a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0004"
    $ current_voice = "voice/MAY04A_CRS0004.ogg"
    "红莉栖" "「……咳咳，就不说下去了吧。反正目前嫌疑已经被解除了」"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0005"
    $ current_voice = "voice/MAY04A_MAY0005.ogg"
    "真由理" "「嗯，多亏了红莉栖酱的劝说啊～。在旁边听着的时候，真心觉得好厉害啊」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASB08"),"True","lh/CRS_ASB08a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0005"
    $ current_voice = "voice/MAY04A_CRS0005.ogg"
    "红莉栖" "「没那回事啦」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASB01"),"True","lh/CRS_ASB01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    $ targetmailid = cml.setdefault("RM_MAY_SEND_FEI03","")

    $ LR_RM_CHANCE=17
    call CHECK_RM_RECEIVE
    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0006"
    $ current_voice = "voice/MAY04A_CRS0006.ogg"
    "红莉栖" "「……真由理才是很厉害呢，被父亲那样地爱着」"
    call CHECK_RM_RECEIVE
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0006"
    $ current_voice = "voice/MAY04A_MAY0006.ogg"
    "真由理" "「嗯～，是吗？」"
    call CHECK_RM_RECEIVE
    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0007"
    $ current_voice = "voice/MAY04A_CRS0007.ogg"
    "红莉栖" "「不然就不会担心到那种地步了」"
    call CHECK_RM_RECEIVE
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0007"
    $ current_voice = "voice/MAY04A_MAY0007.ogg"
    "真由理" "「真由喜觉得爸爸只是爱操心罢了～」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASB02"),"True","lh/CRS_ASB02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    call CHECK_RM_RECEIVE
    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0008"
    $ current_voice = "voice/MAY04A_CRS0008.ogg"
    "红莉栖" "「就算只是操心，也足够值得感谢的了」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    call CHECK_RM_RECEIVE
    "红莉栖酱苦笑着，拿出了两个纸杯，然后看了一下小型冰箱和柜子。"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASB07"),"True","lh/CRS_ASB07a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    call CHECK_RM_RECEIVE
    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0009"
    $ current_voice = "voice/MAY04A_CRS0009.ogg"
    "红莉栖" "「嗯──，要是提前买些好一点的点心就好了啊。抱歉了，没能拿出点像样的东西招待你」"
    call CHECK_RM_RECEIVE
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0008"
    $ current_voice = "voice/MAY04A_MAY0008.ogg"
    "真由理" "「没关系，是真由喜突然说要来的。不用那么在意」"
    call CHECK_RM_RECEIVE
    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0010"
    $ current_voice = "voice/MAY04A_CRS0010.ogg"
    "红莉栖" "「我基本上只预备泡面之类的东西。有一个人说我是土豪十七什么的蠢话，但我根本就不是土豪」"
    call CHECK_RM_RECEIVE
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0009"
    $ current_voice = "voice/MAY04A_MAY0009.ogg"
    "真由理" "「已经买了挺多东西了，足够了」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASB01"),"True","lh/CRS_ASB01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    call CHECK_RM_RECEIVE
    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0011"
    $ current_voice = "voice/MAY04A_CRS0011.ogg"
    "红莉栖" "「但是机会难得，要叫客房服务吗？」"
    call CHECK_RM_RECEIVE
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0010"
    $ current_voice = "voice/MAY04A_MAY0010.ogg"
    "真由理" "「没关系，不用了。能跟红莉栖酱说好多好多的话，真由喜觉得这样就足够了」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASB02"),"True","lh/CRS_ASB02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    call CHECK_RM_RECEIVE
    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0012"
    $ current_voice = "voice/MAY04A_CRS0012.ogg"
    "红莉栖" "「嗯，所谓的过夜会，就是这样的呢」"
    call CHECK_RM_RECEIVE
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0011"
    $ current_voice = "voice/MAY04A_MAY0011.ogg"
    "真由理" "「嗯嗯，就是这样的」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASB01"),"True","lh/CRS_ASB01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    call CHECK_RM_RECEIVE
    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0013"
    $ current_voice = "voice/MAY04A_CRS0013.ogg"
    "红莉栖" "「那么，方便面，海鲜味和咖喱味的，要哪个？」"
    call CHECK_RM_RECEIVE
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0012"
    $ current_voice = "voice/MAY04A_MAY0012.ogg"
    "真由理" "「咖喱味的吧」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASC03"),"True","lh/CRS_ASC03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    call CHECK_RM_RECEIVE
    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0014"
    $ current_voice = "voice/MAY04A_CRS0014.ogg"
    "红莉栖" "「ＯＫ」"

    call CHECK_RM_RECEIVE

    $ gd["RCVmailData"][gc["ScriptMacros"]["RM_MAY_RECV_FEI02_01"]]["late"]=True
    $ lml.append(gc["ScriptMacros"]["RM_MAY_RECV_FEI02_01"])

    hide screen phoneSD1
    window hide

    stop bgm 
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_MAY003A"]]["Check"]=True


    $ loadBG(2,"EV_MAY003A")



    hide screen phonebtn
    "红莉栖酱烧开了热水，然后把热水倒在了方便面里，递了过来。"
    call CHECK_RM_RECEIVE
    "在这期间，真由喜打开了零食的袋子，在地上摆成了一大排。"
    play bgm "FDBGM02"

    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0013"
    $ current_voice = "voice/MAY04A_MAY0013.ogg"
    "真由理" "「那么，为了第一次的过夜会，干杯──」"
    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0015"
    $ current_voice = "voice/MAY04A_CRS0015.ogg"
    "红莉栖" "「干杯」"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_DOCPE"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_DOCPE"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_DOCPE"])
    "举起倒了{color=f00}Ｄｒ．Ｐｅｐｐｅｒ{/color}的纸杯干杯了之后，一口气喝光了。"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0014"
    $ current_voice = "voice/MAY04A_MAY0014.ogg"
    "真由理" "「呜～～！　好好喝～♪」"
    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0016"
    $ current_voice = "voice/MAY04A_CRS0016.ogg"
    "红莉栖" "「啊哈、真由喜。这样子挺像个大叔的哦？」"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0015"
    $ current_voice = "voice/MAY04A_MAY0015.ogg"
    "真由理" "「诶嘿嘿，「我就是为了这一杯而活」是吧？　爸爸经常这么说」"
    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0017"
    $ current_voice = "voice/MAY04A_CRS0017.ogg"
    "红莉栖" "「哎呀真由理真是的」"
    "红莉栖酱用叉子吃了一口方便面之后笑道。"
    "终于见到了红莉栖酱的笑脸，松了一口气。"
    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0018"
    $ current_voice = "voice/MAY04A_CRS0018.ogg"
    "红莉栖" "「哈──、感觉……比平常要好吃得多……」"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0016"
    $ current_voice = "voice/MAY04A_MAY0016.ogg"
    "真由理" "「是啊，因为肚子已经饿瘪了」"
    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0019"
    $ current_voice = "voice/MAY04A_CRS0019.ogg"
    "红莉栖" "「刚才看了一下手机。真由理，从傍晚开始就一直在联系我啊。没有注意到，对不起了」"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0017"
    $ current_voice = "voice/MAY04A_MAY0017.ogg"
    "真由理" "「没关系，真由喜也没资格指责别人。结局好就一切都好。因为要不是这样的话，就不能像这样跟红莉栖酱一起在宾馆过夜了」"
    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0020"
    $ current_voice = "voice/MAY04A_CRS0020.ogg"
    "红莉栖" "「确实……」"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0018"
    $ current_voice = "voice/MAY04A_MAY0018.ogg"
    "真由理" "「最后就像这样，任何事情都会在它们该发生的时候发生，真由喜想」"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_FATALISM"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_FATALISM"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_FATALISM"])
    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0021"
    $ current_voice = "voice/MAY04A_CRS0021.ogg"
    "红莉栖" "「{color=#f00}命运论{/color}吗……」"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0019"
    $ current_voice = "voice/MAY04A_MAY0019.ogg"
    "真由理" "「发生了不好的事，确实在那个时候可能非常地失落，但之后回过头来看，因为那件事而产生的好事也有很多」"
    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0022"
    $ current_voice = "voice/MAY04A_CRS0022.ogg"
    "红莉栖" "「……我，不赞同命运论。我相信，未来不是被事先决定好的，而是通过自己的双手开拓出来的」"
    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0023"
    $ current_voice = "voice/MAY04A_CRS0023.ogg"
    "红莉栖" "「如果未来是被事先决定而不可以改变的，那就是在否定科学本身」"
    window hide
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_MAY003D"]]["Check"]=True


    $ loadBG(2,"EV_MAY003D")



    "红莉栖酱停下了正在吃方便面的手，像自言自语一样继续说着。"
    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0024"
    $ current_voice = "voice/MAY04A_CRS0024.ogg"
    "红莉栖" "「科学改变了世界，改变了未来。尤其是在２０世纪有着极其巨大的变化，人们的一切梦想与欲望以着极其强大的势头实现了」"
    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0025"
    $ current_voice = "voice/MAY04A_CRS0025.ogg"
    "红莉栖" "「电话微波炉也蕴藏着无限的可能性。这个可能性我也不想去否定」"
    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0026"
    $ current_voice = "voice/MAY04A_CRS0026.ogg"
    "红莉栖" "「……但是，最近我意识到了。说不定，连自己觉得是通过自己的手来开拓的未来都是已经预先决定好的事也说不定」"
    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0027"
    $ current_voice = "voice/MAY04A_CRS0027.ogg"
    "红莉栖" "「虽然不想承认……但结果，不管怎么努力想要改变未来，尽管枝叶不同，最后还是会收束到同一个未来的……」"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0020"
    $ current_voice = "voice/MAY04A_MAY0020.ogg"
    "真由理" "「真难呢……」"
    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0028"
    $ current_voice = "voice/MAY04A_CRS0028.ogg"
    "红莉栖" "「是啊……非常难的问题……老老实实地接受被预先决定的未来什么的，我们又不是圣人君子，怎么可能做到」"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0021"
    $ current_voice = "voice/MAY04A_MAY0021.ogg"
    "真由理" "「嗯……」"
    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0029"
    $ current_voice = "voice/MAY04A_CRS0029.ogg"
    "红莉栖" "「凡人只是想选择一个让自己重要的人们获得幸福的未来，有什么不行吗……这个我明白，但是……」"
    "红莉栖酱沉默了下来，闭口不语。"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0022"
    $ current_voice = "voice/MAY04A_MAY0022.ogg"
    "真由理" "「红莉栖酱……」"
    window hide
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_MAY003B"]]["Check"]=True


    $ loadBG(2,"EV_MAY003B")



    "看到红莉栖酱的眼睛好像湿了，于是慌慌张张地往她的嘴里塞了一块炸鸡。"
    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0030"
    $ current_voice = "voice/MAY04A_CRS0030.ogg"
    "红莉栖" "「嗯！？」"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0023"
    $ current_voice = "voice/MAY04A_MAY0023.ogg"
    "真由理" "「一边谈复杂的事一边吃饭的话，美味就会减半，那样太浪费了」"
    window hide
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_MAY003C"]]["Check"]=True


    $ loadBG(2,"EV_MAY003C")



    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0031"
    $ current_voice = "voice/MAY04A_CRS0031.ogg"
    "红莉栖" "「……是啊，这大概是没有答案的问题。而且我也不是想跟真由理展开辩论什么的」"
    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0032"
    $ current_voice = "voice/MAY04A_CRS0032.ogg"
    "红莉栖" "「但是……过夜会，一般都聊什么呢？　这种东西，其实至今为止都跟我无缘」"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0024"
    $ current_voice = "voice/MAY04A_MAY0024.ogg"
    "真由理" "「嗯～～，要说女生的过夜会，必不可少的就是Ｇｉｒｌｓ　Ｔａｌｋ吧？」"
    window hide
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_MAY003B"]]["Check"]=True


    $ loadBG(2,"EV_MAY003B")



    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0033"
    $ current_voice = "voice/MAY04A_CRS0033.ogg"
    "红莉栖" "「Ｇｉｒｌｓ　Ｔａｌｋ！？　那是什么啊啊！？」"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0025"
    $ current_voice = "voice/MAY04A_MAY0025.ogg"
    "真由理" "「坦白平常不能说的话，互相知道对方的事，让关系变得更加融洽」"
    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0034"
    $ current_voice = "voice/MAY04A_CRS0034.ogg"
    "红莉栖" "「平常不能说的话……」"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_COUPLING"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_COUPLING"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_COUPLING"])
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0026"
    $ current_voice = "voice/MAY04A_MAY0026.ogg"
    "真由理" "「偶尔也跟吹雪她们开过夜会，比如说其实在暗地里喜欢某对特别稀有的{color=#f00}ＣＰ{/color}啦，坦白像这样的冲击性的事实。也挺让人激动的哦？」"
    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0035"
    $ current_voice = "voice/MAY04A_CRS0035.ogg"
    "红莉栖" "「嗯……原、原来如此……」"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0027"
    $ current_voice = "voice/MAY04A_MAY0027.ogg"
    "真由理" "「不用想得那么复杂。什么烦恼啊，恋爱话题啊，真由喜全都没问题，红莉栖酱！」"
    "拍了一下手，然后朝着红莉栖酱张开了双臂。"
    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0036"
    $ current_voice = "voice/MAY04A_CRS0036.ogg"
    "红莉栖" "「突、突然跟我这么说我也。嗯嗯～」"
    window hide

    stop bgm 
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_MAY003D"]]["Check"]=True


    $ loadBG(2,"EV_MAY003D")



    "红莉栖酱抱着胳膊，陷入了沉思。"
    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0037"
    $ current_voice = "voice/MAY04A_CRS0037.ogg"
    "红莉栖" "「烦恼……么……我不太喜欢把自己的弱点告诉别人啊」"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0028"
    $ current_voice = "voice/MAY04A_MAY0028.ogg"
    "真由理" "「是吗？　真由喜认为这是解决自己怎么都没法处理的问题的一个机遇」"
    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0038"
    $ current_voice = "voice/MAY04A_CRS0038.ogg"
    "红莉栖" "「嘛，也有道理。因为至今为止，我一直都不想让周围的人知道我的弱点……」"
    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0039"
    $ current_voice = "voice/MAY04A_CRS0039.ogg"
    "红莉栖" "「……甚至不会把弱点告诉自己的父母」"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0029"
    $ current_voice = "voice/MAY04A_MAY0029.ogg"
    "真由理" "「红莉栖酱……」"
    play bgm "FD2BGM09"

    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0040"
    $ current_voice = "voice/MAY04A_CRS0040.ogg"
    "红莉栖" "「……不过，真由理不一样」"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0030"
    $ current_voice = "voice/MAY04A_MAY0030.ogg"
    "真由理" "「诶嘿嘿，有点害羞呢」"
    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0041"
    $ current_voice = "voice/MAY04A_CRS0041.ogg"
    "红莉栖" "「是啊。真由理跟父亲关系很好，这样的人的建议，或许可以作为参考……」"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0031"
    $ current_voice = "voice/MAY04A_MAY0031.ogg"
    "真由理" "「烦恼是关于父亲的事？」"
    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0042"
    $ current_voice = "voice/MAY04A_CRS0042.ogg"
    "红莉栖" "「那个……不光是这样，还有很多……从哪儿说起比较好呢……」"
    window hide
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_MAY003C"]]["Check"]=True


    $ loadBG(2,"EV_MAY003C")



    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0032"
    $ current_voice = "voice/MAY04A_MAY0032.ogg"
    "真由理" "「一点一点来就好。关于红莉栖酱父亲的事，从菲利斯那里也稍微听说过了。菲利斯也很担心红莉栖酱」"
    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0043"
    $ current_voice = "voice/MAY04A_CRS0043.ogg"
    "红莉栖" "「菲利斯吗？　我做了像是拿她当出气筒一样的事……」"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0033"
    $ current_voice = "voice/MAY04A_MAY0033.ogg"
    "真由理" "「她说，没有办法丢下红莉栖酱不管」"
    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0044"
    $ current_voice = "voice/MAY04A_CRS0044.ogg"
    "红莉栖" "「是么……真是个好人呢。菲利斯」"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0034"
    $ current_voice = "voice/MAY04A_MAY0034.ogg"
    "真由理" "「嗯，菲利斯是个非常好的人。　她很在意是不是把红莉栖酱给惹生气了」"
    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0045"
    $ current_voice = "voice/MAY04A_CRS0045.ogg"
    "红莉栖" "「……不是的，菲利斯什么错都没有。我被父亲讨厌了。但是，菲利斯劝我说，这样子是不行的，应该去和好……」"
    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0046"
    $ current_voice = "voice/MAY04A_CRS0046.ogg"
    "红莉栖" "「然后，我给父亲打电话想要道歉，但却被无情地拒绝了……」"
    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0047"
    $ current_voice = "voice/MAY04A_CRS0047.ogg"
    "红莉栖" "「不对，Ｇｉｒｌｓ　Ｔａｌｋ，不应该讲这么沉重的话题……讲讲更加有意思的话题比较好是吧？」"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0035"
    $ current_voice = "voice/MAY04A_MAY0035.ogg"
    "真由理" "「不，没关系的。讲什么都好」"
    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0048"
    $ current_voice = "voice/MAY04A_CRS0048.ogg"
    "红莉栖" "「是、是么……感觉这种事情好羞耻啊……有点紧张……不习惯的感觉」"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0036"
    $ current_voice = "voice/MAY04A_MAY0036.ogg"
    "真由理" "「真由喜想听听后面发生了什么啊？」"
    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0049"
    $ current_voice = "voice/MAY04A_CRS0049.ogg"
    "红莉栖" "「……啊、然后……就不由得生起气来，跑了出去，不过现在非常的后悔……」"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0037"
    $ current_voice = "voice/MAY04A_MAY0037.ogg"
    "真由理" "「红莉栖酱很喜欢父亲吧？」"
    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0050"
    $ current_voice = "voice/MAY04A_CRS0050.ogg"
    "红莉栖" "「那种人我最讨厌了！」"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0038"
    $ current_voice = "voice/MAY04A_MAY0038.ogg"
    "真由理" "「但是，要是真的讨厌的话，就算被拒绝了也不会受到打击的吧？」"
    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0051"
    $ current_voice = "voice/MAY04A_CRS0051.ogg"
    "红莉栖" "「……这个」"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0039"
    $ current_voice = "voice/MAY04A_MAY0039.ogg"
    "真由理" "「就算没法一下子传达，慢慢地一步一步地持续传达自己喜欢的感情，总有一天能够相通的吧？　短信和邮件都可以的」"
    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0052"
    $ current_voice = "voice/MAY04A_CRS0052.ogg"
    "红莉栖" "「反正还是会像之前那样以被拒绝收场」"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0040"
    $ current_voice = "voice/MAY04A_MAY0040.ogg"
    "真由理" "「即使这样，也要继续传达，那会怎么样呢？」"
    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0053"
    $ current_voice = "voice/MAY04A_CRS0053.ogg"
    "红莉栖" "「办不到的。我已经没有时间了！」"
    "没有时间了──被红莉栖酱的这句话吓了一跳。"
    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0054"
    $ current_voice = "voice/MAY04A_CRS0054.ogg"
    "红莉栖" "「对不起、真由理……我自己也知道，这样子很不像话，但是我没有办法了」"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0041"
    $ current_voice = "voice/MAY04A_MAY0041.ogg"
    "真由理" "「不，没关系的。不要介意」"
    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0055"
    $ current_voice = "voice/MAY04A_CRS0055.ogg"
    "红莉栖" "「居然把脾气撒在了真由理身上，我真的是脑袋有问题了。最近发生太多事了，已经被装满了……没有空余了的样子」"
    window hide
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_MAY003D"]]["Check"]=True


    $ loadBG(2,"EV_MAY003D")



    "红莉栖酱拢了拢前发，叹了一口气。"
    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0056"
    $ current_voice = "voice/MAY04A_CRS0056.ogg"
    "红莉栖" "「还以为自己的脑容量能够更高一点呢，结果完全不行，随随便便地就超出容量了。这样的自己真是难为情，讨厌自己，已经快要崩溃了」"
    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0057"
    $ current_voice = "voice/MAY04A_CRS0057.ogg"
    "红莉栖" "「──人的心要是也能像方程一样有个明确的解就好了。依靠着不合逻辑的感情四处奔波，简直太不合理了」"
    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0058"
    $ current_voice = "voice/MAY04A_CRS0058.ogg"
    "红莉栖" "「真想给自己那一天到晚净想着无聊事情的脑袋做一个脑白质切除术」"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0042"
    $ current_voice = "voice/MAY04A_MAY0042.ogg"
    "真由理" "「那个……真由喜啊，容量什么的，脑白质什么的，不太了解。是不是说红莉栖酱的脑袋里充满了烦恼，已经乱成一锅粥了？」"
    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0059"
    $ current_voice = "voice/MAY04A_CRS0059.ogg"
    "红莉栖" "「……是的」"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0043"
    $ current_voice = "voice/MAY04A_MAY0043.ogg"
    "真由理" "「真由喜也有这种时候啊。不光是红莉栖酱，大家都一样的」"
    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0060"
    $ current_voice = "voice/MAY04A_CRS0060.ogg"
    "红莉栖" "「……真由理跟我不同，一直都是笑脸……谁都喜欢对吧？　跟讨厌自己是无缘的……」"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0044"
    $ current_voice = "voice/MAY04A_MAY0044.ogg"
    "真由理" "「不、没那回事。真由喜在没能帮上重要的人的忙的时候，成为了别人的重担的时候，也是会非常讨厌自己的啊？」"
    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0061"
    $ current_voice = "voice/MAY04A_CRS0061.ogg"
    "红莉栖" "「重要的人，是吗？」"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0045"
    $ current_voice = "voice/MAY04A_MAY0045.ogg"
    "真由理" "「嗯」"
    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0062"
    $ current_voice = "voice/MAY04A_CRS0062.ogg"
    "红莉栖" "「那个人……果然指的是他吧」"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0046"
    $ current_voice = "voice/MAY04A_MAY0046.ogg"
    "真由理" "「不光是冈伦，红莉栖酱也是重要的人」"
    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0063"
    $ current_voice = "voice/MAY04A_CRS0063.ogg"
    "红莉栖" "「……真由理」"

    stop bgm 
    "要问那件事──只有现在了。"
    "想到这里，大口地深呼吸，做好觉悟，试着询问。"
    window hide



    $ loadBG(2,"BG55N1")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMA05"),"True","lh/CRS_AMA05a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    show screen phonebtn
    show screen phoneSD1
    play bgm "FD2BGM05"

    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0047"
    $ current_voice = "voice/MAY04A_MAY0047.ogg"
    "真由理" "「那个……真由喜，没有成为两个人的重担吧？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMA01"),"True","lh/CRS_AMA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0064"
    $ current_voice = "voice/MAY04A_CRS0064.ogg"
    "红莉栖" "「……为什么突然之间说这种话？　完全不是重担」"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0048"
    $ current_voice = "voice/MAY04A_MAY0048.ogg"
    "真由理" "「那就好，真由喜在想冈伦和红莉栖酱是不是因为真由喜的缘故在烦恼呢。这就是真由喜的烦恼」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMA03"),"True","lh/CRS_AMA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0065"
    $ current_voice = "voice/MAY04A_CRS0065.ogg"
    "红莉栖" "「难道那家伙跟真由理说什么了吗！？」"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0049"
    $ current_voice = "voice/MAY04A_MAY0049.ogg"
    "真由理" "「没有，冈伦什么都没有说。但是在想了很多之后，觉得说不定就是这个缘故」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMA04"),"True","lh/CRS_AMA04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0066"
    $ current_voice = "voice/MAY04A_CRS0066.ogg"
    "红莉栖" "「是吗……」"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0050"
    $ current_voice = "voice/MAY04A_MAY0050.ogg"
    "真由理" "「果然，红莉栖酱知道冈伦为什么烦恼啊」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMC05"),"True","lh/CRS_AMC05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0067"
    $ current_voice = "voice/MAY04A_CRS0067.ogg"
    "红莉栖" "「……那是」"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0051"
    $ current_voice = "voice/MAY04A_MAY0051.ogg"
    "真由理" "「冈伦不肯告诉真由喜，是不是因为真由喜帮不上冈伦的忙呢……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMA07"),"True","lh/CRS_AMA07a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0068"
    $ current_voice = "voice/MAY04A_CRS0068.ogg"
    "红莉栖" "「不是的！　那是因为，他认为真由理比其他的任何人都重要！　不想让你受到伤害，想要保护你！」"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0052"
    $ current_voice = "voice/MAY04A_MAY0052.ogg"
    "真由理" "「红莉栖酱……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMA05"),"True","lh/CRS_AMA05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0069"
    $ current_voice = "voice/MAY04A_CRS0069.ogg"
    "红莉栖" "「真由理，唯独这一点你不要搞错了。要不然，他所做的事就得不到回报了……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMC01"),"True","lh/CRS_AMC01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0070"
    $ current_voice = "voice/MAY04A_CRS0070.ogg"
    "红莉栖" "「不过……那种笨蛋之王，得不得到回报，可跟我一点关系都没有」"
    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0071"
    $ current_voice = "voice/MAY04A_CRS0071.ogg"
    "红莉栖" "「那家伙真是蠢到家了……蠢到让人无法忍受」"
    "红莉栖酱的话语，虽然带刺──但非常地温柔。"
    "和冈伦一样。"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0053"
    $ current_voice = "voice/MAY04A_MAY0053.ogg"
    "真由理" "「冈伦和红莉栖酱很像呢」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMA03"),"True","lh/CRS_AMA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0072"
    $ current_voice = "voice/MAY04A_CRS0072.ogg"
    "红莉栖" "「哈！？　不不不！　我说啊真由理，听好了！　把我跟那种不知好歹黑白颠倒的白痴划分到了一类，那可真是太让人伤心了」"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0054"
    $ current_voice = "voice/MAY04A_MAY0054.ogg"
    "真由理" "「相像的两个人，真由喜觉得很般配啊？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMB04"),"True","lh/CRS_AMB04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0073"
    $ current_voice = "voice/MAY04A_CRS0073.ogg"
    "红莉栖" "「开玩笑呢吧！？　那家伙跟我！？　不可能不可能！　绝对不可能！　难以置信！」"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0055"
    $ current_voice = "voice/MAY04A_MAY0055.ogg"
    "真由理" "「是吗？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMC02"),"True","lh/CRS_AMC02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0074"
    $ current_voice = "voice/MAY04A_CRS0074.ogg"
    "红莉栖" "「那种厨二病……谁会……」"
    "和嘴里说的话形成鲜明对比的是，红莉栖酱满脸通红的脸色。"
    "看来红莉栖酱也不是很擅长说谎。"
    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0075"
    $ current_voice = "voice/MAY04A_CRS0075.ogg"
    "红莉栖" "「比起我，真由理才更加的……跟那家伙相处的时间更长……」"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0056"
    $ current_voice = "voice/MAY04A_MAY0056.ogg"
    "真由理" "「冈伦……对真由喜来说就好像哥哥一样的存在……」"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0057"
    $ current_voice = "voice/MAY04A_MAY0057.ogg"
    "真由理" "「但是……仅此而已……」"
    "想说的话越多，不知怎的到嘴边就越说不出来了。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMB07"),"True","lh/CRS_AMB07a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide screen phonebtn
    "看到真由喜在犯难，红莉栖酱捏住了真由喜的脸蛋，然后向外拉。"
    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0076"
    $ current_voice = "voice/MAY04A_CRS0076.ogg"
    "红莉栖" "「真由理，你在勉强自己，我看得一清二楚」"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0058"
    $ current_voice = "voice/MAY04A_MAY0058.ogg"
    "真由理" "「……吼咿七」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMB01"),"True","lh/CRS_AMB01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    show screen phonebtn
    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0077"
    $ current_voice = "voice/MAY04A_CRS0077.ogg"
    "红莉栖" "「Ｇｉｒｌｓ　Ｔａｌｋ不是要把平常不能说的事毫无隐瞒地说出来么？　那么就诚实地说出来吧。我也……诚实地说出来」"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0059"
    $ current_voice = "voice/MAY04A_MAY0059.ogg"
    "真由理" "「嗯……」"
    "互相看着对方的眼睛，用力地点了点头。"
    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0078"
    $ current_voice = "voice/MAY04A_CRS0078.ogg"
    "红莉栖" "「真由理喜欢冈部是吧？」"
    "已经无法从红莉栖酱那强烈的视线中逃脱出去了。"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0060"
    $ current_voice = "voice/MAY04A_MAY0060.ogg"
    "真由理" "「……嗯」"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0061"
    $ current_voice = "voice/MAY04A_MAY0061.ogg"
    "真由理" "「但是真由喜也知道冈伦喜欢的是红莉栖酱」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMC04"),"True","lh/CRS_AMC04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0079"
    $ current_voice = "voice/MAY04A_CRS0079.ogg"
    "红莉栖" "「呜！　为什么要这么说？」"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0062"
    $ current_voice = "voice/MAY04A_MAY0062.ogg"
    "真由理" "「多看一看就会明白的。真由喜是冈伦的人质，所以一直在旁边看着冈伦……于是就知道了」"
    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0080"
    $ current_voice = "voice/MAY04A_CRS0080.ogg"
    "红莉栖" "「…………」"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0063"
    $ current_voice = "voice/MAY04A_MAY0063.ogg"
    "真由理" "「那么，这次轮到红莉栖酱了。实话实说，红莉栖酱，喜欢冈伦吗？」"
    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0081"
    $ current_voice = "voice/MAY04A_CRS0081.ogg"
    "红莉栖" "「我、我──」"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0064"
    $ current_voice = "voice/MAY04A_MAY0064.ogg"
    "真由理" "「嗯？」"
    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0082"
    $ current_voice = "voice/MAY04A_CRS0082.ogg"
    "红莉栖" "「……那种笨蛋，最讨厌了」"
    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0083"
    $ current_voice = "voice/MAY04A_CRS0083.ogg"
    "红莉栖" "「……然而……今天，那家伙跟我说了多余的话……因为那个让我混乱了而已……」"
    "红莉栖酱捂住了嘴，摇了摇头。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMA05"),"True","lh/CRS_AMA05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0084"
    $ current_voice = "voice/MAY04A_CRS0084.ogg"
    "红莉栖" "「啊、真是的……抱歉。感觉……乱七八糟的。我所说的话，支离破碎的」"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0065"
    $ current_voice = "voice/MAY04A_MAY0065.ogg"
    "真由理" "「没有，听得懂的，没关系，继续吧」"
    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0085"
    $ current_voice = "voice/MAY04A_CRS0085.ogg"
    "红莉栖" "「……是么」"
    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0086"
    $ current_voice = "voice/MAY04A_CRS0086.ogg"
    "红莉栖" "「知道了……我会如实地告诉真由理的……」"
    "红莉栖酱反复深呼吸了好几次，在吐气地同时说道。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMA01"),"True","lh/CRS_AMA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0087"
    $ current_voice = "voice/MAY04A_CRS0087.ogg"
    "红莉栖" "「……其实我刚才被冈部表白了」"
    "一瞬间，脑袋里变得一片空白。"
    "感觉必须得说点什么，张开了嘴，却什么也说不出来。"
    "过了一会之后，终于说出来了一句话，不过那句话蠢到连自己都吓了一跳。"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0066"
    $ current_voice = "voice/MAY04A_MAY0066.ogg"
    "真由理" "「这样啊……」"
    "跟奶奶去世的时候很像。"
    "痛苦什么的、悲伤什么的，完全感觉不到。"
    "只能感觉到心里像是被掏了一个洞一样。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMB05"),"True","lh/CRS_AMB05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0088"
    $ current_voice = "voice/MAY04A_CRS0088.ogg"
    "红莉栖" "「但是，这一定是有什么搞错了。那家伙，完全地把对象搞错了……要犯傻也得有个度！」"
    "红莉栖酱在为真由喜而生气。"
    "但是冈伦并没有搞错。"
    "真由喜是知道的。"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0067"
    $ current_voice = "voice/MAY04A_MAY0067.ogg"
    "真由理" "「并不是这样的，红莉栖酱」"
    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0089"
    $ current_voice = "voice/MAY04A_CRS0089.ogg"
    "红莉栖" "「可是对他来说，真由理的事比任何人都要重要，那家伙，就算把自己弄得遍体鳞伤，也绝对不放弃拯救真由理的啊！？」"
    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0090"
    $ current_voice = "voice/MAY04A_CRS0090.ogg"
    "红莉栖" "「然后，他找到了拯救真由理的方法。都已经这样了──」"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0068"
    $ current_voice = "voice/MAY04A_MAY0068.ogg"
    "真由理" "「冈伦要救真由喜？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMC04"),"True","lh/CRS_AMC04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    "红莉栖酱回过神来，闭上了嘴。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMC06"),"True","lh/CRS_AMC06a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0091"
    $ current_voice = "voice/MAY04A_CRS0091.ogg"
    "红莉栖" "「……真是的……现在的我，真的是，脑袋出问题了。对不起，真由理，我不能……再说了」"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0069"
    $ current_voice = "voice/MAY04A_MAY0069.ogg"
    "真由理" "「没关系，说出来」"
    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0092"
    $ current_voice = "voice/MAY04A_CRS0092.ogg"
    "红莉栖" "「但是……」"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0070"
    $ current_voice = "voice/MAY04A_MAY0070.ogg"
    "真由理" "「拜托了，红莉栖酱。如果在真由喜不知道的地方发生了什么，真由喜也想要清楚地知道啊」"
    "盯着红莉栖酱的眼睛，拼命地请求。"
    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0093"
    $ current_voice = "voice/MAY04A_CRS0093.ogg"
    "红莉栖" "「……但是，我和冈部都不想让真由理受伤。最重要的是，我不想让真由理尝到跟我一样的感觉」"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0071"
    $ current_voice = "voice/MAY04A_MAY0071.ogg"
    "真由理" "「即使受伤也没关系，拜托了，告诉我。冈伦和红莉栖酱都已经受伤了，只有真由喜没有受伤，这样不好」"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0072"
    $ current_voice = "voice/MAY04A_MAY0072.ogg"
    "真由理" "「不管是快乐的时候还是痛苦的时候……都要同甘共苦！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMA05"),"True","lh/CRS_AMA05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0094"
    $ current_voice = "voice/MAY04A_CRS0094.ogg"
    "红莉栖" "「……真由理」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    stop bgm 
    "红莉栖酱紧紧地握着双手，盯着地板沉默不语。"
    "只能以祈祷的想法望着红莉栖酱。"
    "过了一会，红莉栖酱抬起了头。"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMA04"),"True","lh/CRS_AMA04a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0095"
    $ current_voice = "voice/MAY04A_CRS0095.ogg"
    "红莉栖" "「真由理，不会后悔吗？」"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0073"
    $ current_voice = "voice/MAY04A_MAY0073.ogg"
    "真由理" "「嗯，心理准备已经做好了，没事的」"
    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0096"
    $ current_voice = "voice/MAY04A_CRS0096.ogg"
    "红莉栖" "「……是吗……真由理也跟我一样吗」"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0074"
    $ current_voice = "voice/MAY04A_MAY0074.ogg"
    "真由理" "「嗯」"
    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0097"
    $ current_voice = "voice/MAY04A_CRS0097.ogg"
    "红莉栖" "「那么，就像冈部把事情告诉我的那样，我也应该把事情告诉真由理呢……瞒着不说也不公平……」"
    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0098"
    $ current_voice = "voice/MAY04A_CRS0098.ogg"
    "红莉栖" "「再瞒下去也没有意义了啊……知道了，我说」"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0075"
    $ current_voice = "voice/MAY04A_MAY0075.ogg"
    "真由理" "「谢谢，红莉栖酱」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMA01"),"True","lh/CRS_AMA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    "红莉栖酱盯着真由喜的眼睛。"
    "紧张了起来。"
    "周围变得寂静了下来。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMA04"),"True","lh/CRS_AMA04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    play bgm "FD2BGM06"

    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0099"
    $ current_voice = "voice/MAY04A_CRS0099.ogg"
    "红莉栖" "「……因为世界线曾经被改变了……这样下去的话，真由理将会死」"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0076"
    $ current_voice = "voice/MAY04A_MAY0076.ogg"
    "真由理" "「──诶？」"
    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0100"
    $ current_voice = "voice/MAY04A_CRS0100.ogg"
    "红莉栖" "「冈部为了避免真由理的死，无数次地重复着时间跳跃」"
    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0101"
    $ current_voice = "voice/MAY04A_CRS0101.ogg"
    "红莉栖" "「虽然已经劝告过了他，时间跳跃还有很多不确定的因素，是很危险的，但是他尝试了所有的手段，来寻找真由理能够活下来的未来」"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0077"
    $ current_voice = "voice/MAY04A_MAY0077.ogg"
    "真由理" "「……怎么会」"
    "想到最近一直在做恶梦，回过了神来。"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0078"
    $ current_voice = "voice/MAY04A_MAY0078.ogg"
    "真由理" "「最近经常做恶梦……真由喜好几次都快要死了，但每到了那个时候，冈伦就会过来救真由喜」"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0079"
    $ current_voice = "voice/MAY04A_MAY0079.ogg"
    "真由理" "「即使这样，真由喜要死掉了那也只是个梦……难道说，那并不是梦？」"
    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0102"
    $ current_voice = "voice/MAY04A_CRS0102.ogg"
    "红莉栖" "「……这种可能性也不能否定。在冈部每次进行时间跳跃的时候，过去就会被覆盖。被覆盖之前的过去，可能就以梦的形式残留了下来」"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0080"
    $ current_voice = "voice/MAY04A_MAY0080.ogg"
    "真由理" "「这样啊……那不是梦啊……」"
    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0103"
    $ current_voice = "voice/MAY04A_CRS0103.ogg"
    "红莉栖" "「冈部基于如果把作为世界线变化的原因的Ｄｍａｉｌ取消的话，就能回到原来的世界线这个假说，重复进行着时间跳跃」"
    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0104"
    $ current_voice = "voice/MAY04A_CRS0104.ogg"
    "红莉栖" "「我想那个假说是正确的。并且，需要取消的Ｄｍａｉｌ，现在还剩下一封。目前胜利近在咫尺」"
    "真由喜虽不能完全理解红莉栖酱所说的话，但是在拼命地思考着。"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0081"
    $ current_voice = "voice/MAY04A_MAY0081.ogg"
    "真由理" "「那个，冈伦为了救真由喜，想要把通过Ｄｍａｉｌ而改变的世界线恢复原状。因为他的努力，马上就要全部恢复成原来的样子了？」"
    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0105"
    $ current_voice = "voice/MAY04A_CRS0105.ogg"
    "红莉栖" "「是的，不过，这时候冈部注意到了……」"
    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0106"
    $ current_voice = "voice/MAY04A_CRS0106.ogg"
    "红莉栖" "「在原来的世界线里，我在两周前就已经死了」"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0082"
    $ current_voice = "voice/MAY04A_MAY0082.ogg"
    "真由理" "「诶……」"
    "一瞬间听不懂红莉栖酱在说什么。"
    "不，比起听不懂，说成不愿去理解可能更加的正确。"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0083"
    $ current_voice = "voice/MAY04A_MAY0083.ogg"
    "真由理" "「真由喜不相信那种事，不愿相信……是哪里弄错了……」"
    "冈伦即使让自己变得遍体鳞伤，也想要回到那个世界线去。"
    "但是，在那个原来的世界线里，红莉栖酱已经死了。"
    "简直太残酷了……太残酷了。"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_RADIKAN"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_RADIKAN"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_RADIKAN"])
    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0107"
    $ current_voice = "voice/MAY04A_CRS0107.ogg"
    "红莉栖" "「真由理，你还记得冈部说过我在{color=#f00}广播馆{/color}被杀了之类的奇怪的话吗？」"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0084"
    $ current_voice = "voice/MAY04A_MAY0084.ogg"
    "真由理" "「记得……但觉得那是像往常一样冈伦的设定……」"
    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0108"
    $ current_voice = "voice/MAY04A_CRS0108.ogg"
    "红莉栖" "「我之前也是这么觉得的，但是，那并不是这样。大概那是原来的世界线中发生的事实」"
    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0109"
    $ current_voice = "voice/MAY04A_CRS0109.ogg"
    "红莉栖" "「原来的世界线中，那一天──７月２８日，我死了」"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0085"
    $ current_voice = "voice/MAY04A_MAY0085.ogg"
    "真由理" "「……就是说，要是回到了原来的世界线……红莉栖酱就会」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMC01"),"True","lh/CRS_AMC01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    "红莉栖酱皮笑肉不笑地笑了一下，抱住了自己的胳膊。"
    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0110"
    $ current_voice = "voice/MAY04A_CRS0110.ogg"
    "红莉栖" "「已经死了的人存在，这样想才更加不合道理。死后的世界什么的，至今为止想都没有想过……」"
    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0111"
    $ current_voice = "voice/MAY04A_CRS0111.ogg"
    "红莉栖" "「大概我……会从世界上消失」"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0086"
    $ current_voice = "voice/MAY04A_MAY0086.ogg"
    "真由理" "「…………」"
    "颤抖停不下来。"
    "明明已经做好了不管是什么样的事实都要接受的觉悟……"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0087"
    $ current_voice = "voice/MAY04A_MAY0087.ogg"
    "真由理" "「红莉栖酱会消失……不要这样。有什么……肯定会有什么好的方法的……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMA04"),"True","lh/CRS_AMA04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    "红莉栖酱静静地摇了摇头，打断了真由喜的话语。"
    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0112"
    $ current_voice = "voice/MAY04A_CRS0112.ogg"
    "红莉栖" "「虽然考虑了所有的手段，但得到的都是同一个答案。如果世界线不回到原来的样子，真由理就会死，如果世界线回到了原来的样子，那么我就会死」"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0088"
    $ current_voice = "voice/MAY04A_MAY0088.ogg"
    "真由理" "「……不管怎么做也没有办法？」"
    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0113"
    $ current_voice = "voice/MAY04A_CRS0113.ogg"
    "红莉栖" "「是的，冈部也在拼命地寻找着能够同时让我和真由理活下来的选择。多次重复着时间跳跃，用尽了所有的方法」"
    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0114"
    $ current_voice = "voice/MAY04A_CRS0114.ogg"
    "红莉栖" "「……即使这样，依然还是不行」"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0089"
    $ current_voice = "voice/MAY04A_MAY0089.ogg"
    "真由理" "「……怎么会」"
    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0115"
    $ current_voice = "voice/MAY04A_CRS0115.ogg"
    "红莉栖" "「把世界线恢复成原样都已经很辛苦了……还要去寻找其他的世界线……乱来也得有个限度……世界不会那么顺着你的意思走的」"
    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0116"
    $ current_voice = "voice/MAY04A_CRS0116.ogg"
    "红莉栖" "「这样下去冈部坏掉也只是时间的问题了。实际上已经半死不活了……」"
    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0117"
    $ current_voice = "voice/MAY04A_CRS0117.ogg"
    "红莉栖" "「这也是当然的。不管怎么说，自己重要的人一次又一次地在自己的面前被杀掉。反而没坏掉才不合道理。不，就算已经坏掉了也不奇怪」"
    "没想到，冈伦已经到了这么窘迫的地步。"
    "冈伦和红莉栖酱……都在因为真由喜，饱受煎熬。"
    "由于心中的歉意，已经什么都说不出来了。"
    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0118"
    $ current_voice = "voice/MAY04A_CRS0118.ogg"
    "红莉栖" "「虽然可能很残酷，但是明明都已经得出结论了，还要重复进行时间跳跃，那只不过是为了延缓做决定的一种逃避」"
    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0119"
    $ current_voice = "voice/MAY04A_CRS0119.ogg"
    "红莉栖" "「假设，真由理刚才所说的命运论是正确的话，我已经死了的世界线，才是原本应该存在的世界线」"
    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0120"
    $ current_voice = "voice/MAY04A_CRS0120.ogg"
    "红莉栖" "「所以冈部应该选择救真由理──我是这样劝说他的。虽然他不讲情理，但最后还是接受了」"
    "红莉栖酱淡淡地说着，好像现在就要消失了一样。"
    hide screen phonebtn
    "慌张地紧紧抱住了红莉栖酱的身体。"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0090"
    $ current_voice = "voice/MAY04A_MAY0090.ogg"
    "真由理" "「……这种事……不要，不要这样」"
    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0121"
    $ current_voice = "voice/MAY04A_CRS0121.ogg"
    "红莉栖" "「……真由理」"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0091"
    $ current_voice = "voice/MAY04A_MAY0091.ogg"
    "真由理" "「对不起，红莉栖酱。只有真由喜一个人……什么都不知道，刚才还在说着过分的话……」"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0092"
    $ current_voice = "voice/MAY04A_MAY0092.ogg"
    "真由理" "「红莉栖酱应该死的世界……这种被决定好的命运，真由喜绝对不要这样……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMA06"),"True","lh/CRS_AMA06a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0122"
    $ current_voice = "voice/MAY04A_CRS0122.ogg"
    "红莉栖" "「但是，这才是正确的。搞清楚吧，真由理」"
    "红莉栖酱像是在哄孩子一样，温柔地摸着真由喜的头。"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0093"
    $ current_voice = "voice/MAY04A_MAY0093.ogg"
    "真由理" "「正不正确怎么样都无所谓！　红莉栖酱会消失什么的……这样的未来，不管怎么样都想要改变。真由喜也是这么想的」"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0094"
    $ current_voice = "voice/MAY04A_MAY0094.ogg"
    "真由理" "「冈伦和红莉栖酱……都已经苦恼了很久了……然而真由喜却……什么都不知道……」"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0095"
    $ current_voice = "voice/MAY04A_MAY0095.ogg"
    "真由理" "「对不起……真的对不起」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMA05"),"True","lh/CRS_AMA05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0123"
    $ current_voice = "voice/MAY04A_CRS0123.ogg"
    "红莉栖" "「为什么真由理要道歉！？　必须得道歉的是我才对」"
    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0124"
    $ current_voice = "voice/MAY04A_CRS0124.ogg"
    "红莉栖" "「我不想背叛真由理。　我不想被真由理讨厌。我希望真由理一直露着笑容。所以我──」"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0096"
    $ current_voice = "voice/MAY04A_MAY0096.ogg"
    "真由理" "「红莉栖酱才没有背叛真由喜啊？　真由喜已经知道会有这么一天来临了」"
    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0125"
    $ current_voice = "voice/MAY04A_CRS0125.ogg"
    "红莉栖" "「真由理……」"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0097"
    $ current_voice = "voice/MAY04A_MAY0097.ogg"
    "真由理" "「红莉栖酱在冈伦最痛苦的时候，支撑了冈伦是吧？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMC06"),"True","lh/CRS_AMC06a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0126"
    $ current_voice = "voice/MAY04A_CRS0126.ogg"
    "红莉栖" "「并、并没有……我可没有那种想法……只是，那家伙实在太傻了……没有办法放着他不管而已……」"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0098"
    $ current_voice = "voice/MAY04A_MAY0098.ogg"
    "真由理" "「人是会喜欢上在真正困难的时候帮助自己的人的。因为真由喜也是这样的……」"
    "说出来以后，再次感受到了，啊，原来真由喜到现在才意识到自己是真的喜欢冈伦啊。"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0099"
    $ current_voice = "voice/MAY04A_MAY0099.ogg"
    "真由理" "「能让冈伦获得幸福的……不是真由喜而是红莉栖酱啊」"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0100"
    $ current_voice = "voice/MAY04A_MAY0100.ogg"
    "真由理" "「所以，红莉栖酱，不要对真由喜客气，冈伦就拜托给你了」"
    window hide


    $ loadBG(2,"BG_BLACK")



    "想着这句话说得就好像冈伦的妈妈一样啊，同时低下了头。"
    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0127"
    $ current_voice = "voice/MAY04A_CRS0127.ogg"
    "红莉栖" "「……拜、拜托给我了什么的……我会很困扰的……」"
    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0128"
    $ current_voice = "voice/MAY04A_CRS0128.ogg"
    "红莉栖" "「我已经决定好了要回到美国了，所以不行」"
    window hide

    $ loadBG(0,"BG55N1")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMC06"),"True","lh/CRS_AMC06a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0101"
    $ current_voice = "voice/MAY04A_MAY0101.ogg"
    "真由理" "「诶，怎么会……什么时候？」"
    "慌张地抬起了头，红莉栖酱摆出了困惑的表情，正在望向远处。"
    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0129"
    $ current_voice = "voice/MAY04A_CRS0129.ogg"
    "红莉栖" "「明天，不过现在已经是今天了吧。虽然时间还没决定……但我已经决定了要离开日本」"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0102"
    $ current_voice = "voice/MAY04A_MAY0102.ogg"
    "真由理" "「……有事指的就是这个？　太着急了啊……为什么……」"
    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0130"
    $ current_voice = "voice/MAY04A_CRS0130.ogg"
    "红莉栖" "「想了很多之后，觉得这就是相对来讲最好的选择了」"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0103"
    $ current_voice = "voice/MAY04A_MAY0103.ogg"
    "真由理" "「……冈伦知道这件事吧」"
    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0131"
    $ current_voice = "voice/MAY04A_CRS0131.ogg"
    "红莉栖" "「知道」"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0104"
    $ current_voice = "voice/MAY04A_MAY0104.ogg"
    "真由理" "「怎么会……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMA05"),"True","lh/CRS_AMA05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0132"
    $ current_voice = "voice/MAY04A_CRS0132.ogg"
    "红莉栖" "「这是我和冈部得出的结论，不打算改变」"
    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0133"
    $ current_voice = "voice/MAY04A_CRS0133.ogg"
    "红莉栖" "「……冈部已经战斗得足够久了。我也跟他说好了不要忘记我。这样子我就足够了」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMA06"),"True","lh/CRS_AMA06a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0134"
    $ current_voice = "voice/MAY04A_CRS0134.ogg"
    "红莉栖" "「所以拜托了，真由理也接受了吧」"
    "红莉栖酱痛苦的笑脸在泪水中模糊了。"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0105"
    $ current_voice = "voice/MAY04A_MAY0105.ogg"
    "真由理" "「不要，不想接受。真由喜……不想牺牲掉红莉栖酱而活着」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMA07"),"True","lh/CRS_AMA07a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0135"
    $ current_voice = "voice/MAY04A_CRS0135.ogg"
    "红莉栖" "「我也是一样的啊！」"
    "这一点决不能让步，互相以可怕的眼光注视着。"
    "红莉栖酱的眼睛像是燃烧了一样放着强烈的光，就快要被她压倒了。"
    "她那强韧的决心丝毫不动摇。"
    "但是──真由喜有着唯一的绝招。"
    "如果可以的话不想使用这个绝招。"
    "但是既然已经没有其他的方法了，就只能这么做了。"
    "安静地，慢慢地，决心逐渐地加固。"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0106"
    $ current_voice = "voice/MAY04A_MAY0106.ogg"
    "真由理" "「……呐，红莉栖酱相信缘分吗？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMA01"),"True","lh/CRS_AMA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0136"
    $ current_voice = "voice/MAY04A_CRS0136.ogg"
    "红莉栖" "「缘分？」"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0107"
    $ current_voice = "voice/MAY04A_MAY0107.ogg"
    "真由理" "「嗯，有缘的两个人，不管在哪个世界，就算物种不同……也绝对能相见的。真由喜的奶奶这么说过」"
    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0137"
    $ current_voice = "voice/MAY04A_CRS0137.ogg"
    "红莉栖" "「是啊，虽然没有丝毫的科学根据──但现在我希望这是真的」"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0108"
    $ current_voice = "voice/MAY04A_MAY0108.ogg"
    "真由理" "「真由喜也希望这是真的」"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0109"
    $ current_voice = "voice/MAY04A_MAY0109.ogg"
    "真由理" "「只要是活着，肯定还会有再见面的机会的。因为互相思念的两个人之间是互相吸引的」"
    "像是在开导自己一样说着，对红莉栖酱微笑。"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0110"
    $ current_voice = "voice/MAY04A_MAY0110.ogg"
    "真由理" "「所以……真由喜，还不想放弃」"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0111"
    $ current_voice = "voice/MAY04A_MAY0111.ogg"
    "真由理" "「因为真由喜还什么都没有做呢，不想在什么都没有做的时候就放弃，那样就太让人不甘心了」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMA05"),"True","lh/CRS_AMA05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0138"
    $ current_voice = "voice/MAY04A_CRS0138.ogg"
    "红莉栖" "「真由理，你的心情我很高兴，但是，结论已经得出来了。连能够感知到世界线移动的冈部都束手无策了，我们就更没有办法了」"
    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0139"
    $ current_voice = "voice/MAY04A_CRS0139.ogg"
    "红莉栖" "「虽然已经想了各种各样的方法，但是我们并没有找到办法。已经无从应对了。没有办法引发奇迹」"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0112"
    $ current_voice = "voice/MAY04A_MAY0112.ogg"
    "真由理" "「红莉栖酱……」"
    "真由喜还以为这是最后的绝招呢，可是这根本不是绝招，或许是没有用的东西。"
    "即使这样──也还是不想在什么都没有做的时候放弃。"
    "这种心情是不会变的。"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0113"
    $ current_voice = "voice/MAY04A_MAY0113.ogg"
    "真由理" "「……或许很勉强……或许是没用的，但即使这样也必须要试试看」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMC01"),"True","lh/CRS_AMC01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0140"
    $ current_voice = "voice/MAY04A_CRS0140.ogg"
    "红莉栖" "「真由理？刚才说了什么──」"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0114"
    $ current_voice = "voice/MAY04A_MAY0114.ogg"
    "真由理" "「没有，没说什么……」"
    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0141"
    $ current_voice = "voice/MAY04A_CRS0141.ogg"
    "红莉栖" "「是吗……」"
    "气氛变得尴尬起来，不知道该说什么好了。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMA02"),"True","lh/CRS_AMA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0142"
    $ current_voice = "voice/MAY04A_CRS0142.ogg"
    "红莉栖" "「嘛，这种沉重的话题就到此为止吧。现在一分一秒都很宝贵，想要珍惜它」"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0115"
    $ current_voice = "voice/MAY04A_MAY0115.ogg"
    "真由理" "「嗯……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMA01"),"True","lh/CRS_AMA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0143"
    $ current_voice = "voice/MAY04A_CRS0143.ogg"
    "红莉栖" "「……冈部什么时候会把世界线恢复成原状还不知道，不过能够像这样兑现了诺言真是太好了」"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0116"
    $ current_voice = "voice/MAY04A_MAY0116.ogg"
    "真由理" "「谢谢，红莉栖酱」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMA06"),"True","lh/CRS_AMA06a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0144"
    $ current_voice = "voice/MAY04A_CRS0144.ogg"
    "红莉栖" "「不，我才要谢谢你」"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0117"
    $ current_voice = "voice/MAY04A_MAY0117.ogg"
    "真由理" "「那么我们聊什么好呢？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMA02"),"True","lh/CRS_AMA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0145"
    $ current_voice = "voice/MAY04A_CRS0145.ogg"
    "红莉栖" "「是呢，能让人开怀大笑的事？」"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0118"
    $ current_voice = "voice/MAY04A_MAY0118.ogg"
    "真由理" "「那么真由喜就把压箱底的故事掏出来吧～？　冈伦的有趣又羞耻又虐心的武勇传」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMB08"),"True","lh/CRS_AMB08a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0146"
    $ current_voice = "voice/MAY04A_CRS0146.ogg"
    "红莉栖" "「诶，还有那种事吗！？　一定要给我讲讲！」"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0119"
    $ current_voice = "voice/MAY04A_MAY0119.ogg"
    "真由理" "「那是在冈伦初中二年级的时候吧～」"
    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0147"
    $ current_voice = "voice/MAY04A_CRS0147.ogg"
    "红莉栖" "「嗯嗯！」"
    "红莉栖酱眼睛里闪着光，把身子凑了过来。"
    "还想见到红莉栖酱更多的笑脸。"
    "一边回想着有趣又可笑的故事，一边讲着。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMA09"),"True","lh/CRS_AMA09a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0148"
    $ current_voice = "voice/MAY04A_CRS0148.ogg"
    "红莉栖" "「啊哈哈，这是真的！？　冈部初二时候的厨二病，比现在还要严重啊。不过现在也相当严重」"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0120"
    $ current_voice = "voice/MAY04A_MAY0120.ogg"
    "真由理" "「这是真的呀～。用签字笔在右手上画上奇怪的图案，然后把那只手用绷带一圈一圈地缠上，之后就这样去上学。又没有受伤却这么做，让人觉得好奇怪哦……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMB02"),"True","lh/CRS_AMB02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MAY04A_CRS0149"
    $ current_voice = "voice/MAY04A_CRS0149.ogg"
    "红莉栖" "「反正他会说“我右手的封印开始痛了！？”之类的吧？　我知道」"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0121"
    $ current_voice = "voice/MAY04A_MAY0121.ogg"
    "真由理" "「是的是的！　然后呢～」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMB08"),"True","lh/CRS_AMB08a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    "这样开心地聊天，红莉栖酱消失的最后期限正在迫近这种事就好像不存在一样"
    "但是，那确实是存在的。"
    "虽然很着急，想要抓紧时间做点什么，但是到明天早上这段时间里什么也做不到。"
    "所以，现在只能去实现红莉栖酱的「一分一秒都要珍惜」这个愿望了，于是就专注于聊天当中了。"
    hide screen phoneSD1
    window hide
    stop bgm 



    $ loadBG(0,"BG13A1")

    play se "SGSE007L" loop


    show screen phonebtn
    show screen phoneSD1
    "在通宵跟红莉栖酱开心地聊天之后，因为她必须得收拾行李，就跟她道别了。"
    "跟她说好了，就算回到了美国也要通过邮件什么的经常联系。"
    "离开御茶水宾馆之后，立刻回到了秋叶原，赶往Ｌａｂ。"

    window hide


    $ loadBG(2,"BG40A")



    "不知道红莉栖酱会在什么时候消失。"
    "自然地加快了脚步。"
    "看了下时间。"
    "现在快到10点了──"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0122"
    $ current_voice = "voice/MAY04A_MAY0122.ogg"
    "真由理" "「还差一点──等等我、红莉栖酱……」"
    "无法抑制焦躁的心情，跑了起来。"
    window hide

    stop se



    $ loadBG(0,"BG79A1",at=[Transform(yalign=1.0)])






    "来到了Ｌａｂ门前。"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_STUDIO_CRT"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_STUDIO_CRT"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_STUDIO_CRT"])
    "确认{color=#f00}显像管工房{/color}开着店之后，抬头向Ｌａｂ望去。"
    window hide



















    $ loadBG(0,"BG79A1",at=[Transform(yalign=0.0)])
    hide screen phonebtn
    "那时，意识到了位于屋顶上的人影。"
    "早已看惯的白大褂正随风飘荡着。"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0123"
    $ current_voice = "voice/MAY04A_MAY0123.ogg"
    "真由理" "「冈伦……」"
    "冈伦正眺望着天空，似乎是在呆然地考虑着事情。"
    "还没有注意到真由喜。"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0124"
    $ current_voice = "voice/MAY04A_MAY0124.ogg"
    "真由理" "「……冈伦，真由喜也会努力的」"
    window hide


    $ loadBG(2,"BG_BLACK")



    "为了不让冈伦发现，踮着脚走上了楼梯。"
    window hide


    $ loadBG(0,"BG02A1")

    play bgm "BGM31"
    show screen phonebtn
    "门没有锁。"
    "偷偷地溜了进去。"
    "一个人都没有的Ｌａｂ，异常地安静。"
    "朝阳温和地射入了房间里。"
    "回想起了Ｌａｂ里还只有冈伦和真由喜两个人的时候。"
    "有一次，夜里刮台风，Ｌａｂ停电了。"
    "但是，第二天，台风过去了，迎来了就像今早一样平静的早晨，让人有点扫兴。"
    "那天夜里，那样害怕的真由喜，到底是怎么回事呢。"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0125"
    $ current_voice = "voice/MAY04A_MAY0125.ogg"
    "真由理" "「那时候冈伦也给我打气了呢……」"
    "风声和雨声轰轰作响，非常地担心这古老的建筑会不会塌掉。"
    "冈伦用像往常一样装模作样的口气鼓励怕得要命的真由喜。"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_KIKAN"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_KIKAN"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_KIKAN"])
    "『这是“{color=#f00}机关{/color}”的妨碍，但，我凤凰院凶真是不会屈服的！　哇哈哈哈！』是不是这么说的？"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0126"
    $ current_voice = "voice/MAY04A_MAY0126.ogg"
    "真由理" "「真怀念啊……」"
    "“机关”什么的，妨碍什么的，这些全都是冈伦编造出来的设定。"
    "这跟小时候玩的过家家游戏很像，非常的有意思。"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0127"
    $ current_voice = "voice/MAY04A_MAY0127.ogg"
    "真由理" "「没想到居然成为了现实啊……」"
    "几乎每天都做的恶梦，并不是梦。"
    "那是冈伦为了救真由喜而战的记忆的碎片之类的东西。"
    window hide

    "一想起被拿着枪的可怕的人包围的场景，脑袋里面就一阵剧痛。"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0128"
    $ current_voice = "voice/MAY04A_MAY0128.ogg"
    "真由理" "「呜……必须要改变……」"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0129"
    $ current_voice = "voice/MAY04A_MAY0129.ogg"
    "真由理" "「就像红莉栖酱所说的那样……奇迹或许不管怎么做也不会发生」"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0130"
    $ current_voice = "voice/MAY04A_MAY0130.ogg"
    "真由理" "「但比起什么都不做只是后悔时要好得多……」"
    window hide


    $ loadBG(2,"BG03A4")



    "趔趄地走向了里面的开发室。"
    "开发室的电脑，电源一直开着。"
    "使用方法刚才已经打电话向桶子君问来了。"
    "虽然有点难，没关系，会有办法的……应该。"
    hide screen phonebtn
    "输入了真由喜的手机号码，退回的时间，意识到了手机没有电这件事，于是设置为了充完电的时间。"
    "然后，用颤抖的手把头戴设备戴在了头上。"
    "害怕──"
    "红莉栖酱说过，时间跳跃可能会有危险，但到底会变成什么样呢。"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0131"
    $ current_voice = "voice/MAY04A_MAY0131.ogg"
    "真由理" "「冈伦为了真由喜，已经遭受了好多次这样可怕的事了」"
    "虽然想哭，但现在不是哭的时候。"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0132"
    $ current_voice = "voice/MAY04A_MAY0132.ogg"
    "真由理" "「……对不起，冈伦」"
    window hide
    show screen phonebtn
    hide screen phonebtn
    hide screen phonebtn2
    show screen phone(interact=False)
    "之后，只需启动机器，然后向电话微波炉拨号。"
    "慢慢地重复深呼吸。"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0133"
    $ current_voice = "voice/MAY04A_MAY0133.ogg"
    "真由理" "「没事的……不怕……不怕」"
    "安慰了自己之后，把大拇指放在了手机的拨号按钮上。"
    "那时──"
    stop bgm 
    window hide
    play se "SGSE024"

    $ stopvoc("OKA")
    play OKA "MAY04A_OKA0000"
    $ current_voice = "voice/MAY04A_OKA0000.ogg"
    "？？？" "「有人在吗！？」"
    window hide
    play bgm "FD2BGM11"
    call hide_phone

    hide screen phonebtn
    "在门被用力打开的声音响起的同时，冈伦那洪亮的声音在Ｌａｂ中回荡着。"
    window hide



    $ loadBG(2,"BG01A")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA03"),"True","lh/OKA_ASA03a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0134"
    $ current_voice = "voice/MAY04A_MAY0134.ogg"
    "真由理" "「冈伦……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA04"),"True","lh/OKA_ASA04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "MAY04A_OKA0001"
    $ current_voice = "voice/MAY04A_OKA0001.ogg"
    "伦太郎" "「真由理！？」"
    window hide


    $ loadBG(2,"BG03A4")



    "看到冈伦正在冲向真由喜，于是急忙地启动了机器。"
    window hide
    show houden 

    play se "SGSE035L" loop

    "下一个瞬间，蓝白色的光闪烁了起来。"
    "蓝白色的光逐渐地变强，地面在剧烈地晃动。"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0135"
    $ current_voice = "voice/MAY04A_MAY0135.ogg"
    "真由理" "「呜呜……啊啊啊啊！」"
    "头……好疼。"
    "要裂成两半了。"
    "没办法站直，蹲了下去。"
    $ stopvoc("OKA")
    play OKA "MAY04A_OKA0002"
    $ current_voice = "voice/MAY04A_OKA0002.ogg"
    "伦太郎" "「真由理！　你想干什么！」"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0136"
    $ current_voice = "voice/MAY04A_MAY0136.ogg"
    "真由理" "「……对不…起。冈伦。真由喜……不想要放弃……」"
    window hide
    show screen phonebtn
    hide screen phonebtn
    hide screen phonebtn2
    show screen phone(interact=False)

    "用颤抖的手指按下了拨号按钮。"
    window hide



    "视线扭曲了。"
    "脑袋好像要碎开一样，传来了剧烈的疼痛与呕吐感。"
    $ stopvoc("OKA")
    play OKA "MAY04A_OKA0003"
    $ current_voice = "voice/MAY04A_OKA0003.ogg"
    "伦太郎" "「真由理，停下来！」"
    "冈伦那可怕的表情，马上就要到这边来了。"
    "一切都像慢动作一样缓缓地进行着。"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ALA06"),"True","lh/OKA_ALA06a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    "强大的力量抓住了手腕。"
    "冈伦想要用蛮力来夺走真由喜身上的头戴装置。"
    "一边推搡着，一边拼命保护着头戴装置。"
    $ stopvoc("MAY")
    play MAY "MAY04A_MAY0137"
    $ current_voice = "voice/MAY04A_MAY0137.ogg"
    "真由理" "「不要阻止……拜托了，让真由喜去吧！　冈伦！」"
    "喊出来的瞬间。"

    window hide

    stop se
    stop se
    $ stopvoc("")

    "世界出现了裂缝，裂缝随后像蜘蛛的巢一样扩散开──"
    "周围一切都碎成粉末散开了。"
    stop bgm
    call hide_phone

    window hide

    play se "SGSE013"

    hide screen phoneSD1


    hide screen phonebtn
    hide screen phonebtn
    hide houden 
    scene expression Solid("000000")  with fade
    call timeleap (fromtime=[8,17,10,31], totime=[8,16,15,31], fromday=[2])


    return








    hide screen phoneSD1
    window hide





    hide screen phonebtn
    scene expression Solid("000000")  with fade
    return
