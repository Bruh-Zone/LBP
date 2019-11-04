label SGFD2_DAR02A:


    window hide


    $ loadBG(0,"BG38A")


    play bgm "FD2BGM10"


    $ date="8/15"
    $ day = "SUN"
    $ SndMail(74)
    $ RcvMail(75)
    $ ReadMail(75)
    $ RcvMail(76)
    $ ReadMail(76)
    $ RcvMail(77)
    $ ReadMail(77)
    $ RcvMail(78)
    $ ReadMail(78)
    $ SndMail(79)
    $ RcvMail(80)
    $ ReadMail(80)
    $ RcvMail(81)
    $ ReadMail(81)
    $ RcvMail(82)
    $ ReadMail(82)
    $ SndMail(83)
    $ RcvMail(84)
    $ ReadMail(84)
    $ SndMail(85)
    $ RcvMail(86)
    $ ReadMail(86)
    $ RcvMail(87)
    $ ReadMail(87)
    $ RcvMail(88)
    $ ReadMail(88)
    $ RcvMail(89)
    $ ReadMail(89)
    $ SndMail(90)
    $ RcvMail(91)
    $ ReadMail(91)
    show screen phonebtn
    show screen phoneSD1

    $ stopvoc("DAR")
    play DAR "DAR02A_DAR0000"
    $ current_voice = "voice/DAR02A_DAR0000.ogg"
    "至" "「呼、那个商品、总算是到手了」"
    $ stopvoc("DAR")
    play DAR "DAR02A_DAR0001"
    $ current_voice = "voice/DAR02A_DAR0001.ogg"
    "至" "「虽然没想到真的有一开卖就售罄的谣言、但是这种级别的情报战对我来说是没有用的」"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_LIMIT_ONE"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_LIMIT_ONE"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_LIMIT_ONE"])
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_TENBUYER"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_TENBUYER"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_TENBUYER"])

    $ stopvoc("DAR")
    play DAR "DAR02A_DAR0002"
    $ current_voice = "voice/DAR02A_DAR0002.ogg"
    "至" "「但是没想到会是{color=#f00}１人１限{/color}。可能是因为{color=#f00}转卖屋{/color}所遭受的阴影、所以肯定不会原谅这种事情发生的吧。常考」"
    $ stopvoc("DAR")
    play DAR "DAR02A_DAR0003"
    $ current_voice = "voice/DAR02A_DAR0003.ogg"
    "至" "「嘛、随便了。总之今天的战斗既然结束了、差不多该去Ｃｏｓｐｌａｙ广场露下面了」"
    window hide


    $ loadBG(2,"BG56A")



    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_GACHI"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_GACHI"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_GACHI"])
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_LAYER"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_LAYER"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_LAYER"])

    $ stopvoc("DAR")
    play DAR "DAR02A_DAR0004"
    $ current_voice = "voice/DAR02A_DAR0004.ogg"
    "至" "「哈～、人真多啊……。而且最近、{color=#f00}动真格的{/color}的{color=#f00}layer {/color}提升得太快了」"
    $ stopvoc("DAR")
    play DAR "DAR02A_DAR0005"
    $ current_voice = "voice/DAR02A_DAR0005.ogg"
    "至" "「啊、打扰下、能不能拍张照～？」"
    $ stopvoc("DAR")
    play DAR "DAR02A_DAR0006"
    $ current_voice = "voice/DAR02A_DAR0006.ogg"
    "至" "「那么请看下这边。来个可爱点的ＰＯＳＥ」"
    window hide
    play se "SGSE223"

    $ stopvoc("DAR")
    play DAR "DAR02A_DAR0007"
    $ current_voice = "voice/DAR02A_DAR0007.ogg"
    "至" "「哎哟哟、好的很好。非常的萌」"
    $ stopvoc("DAR")
    play DAR "DAR02A_DAR0008"
    $ current_voice = "voice/DAR02A_DAR0008.ogg"
    "至" "「非常感谢您的配合」"
    $ stopvoc("MAY")
    play MAY "DAR02A_MAY0000"
    $ current_voice = "voice/DAR02A_MAY0000.ogg"
    "真由理" "「桶子君」 "
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_ASA01"),"True","lh/MAY_ASA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "DAR02A_DAR0009"
    $ current_voice = "voice/DAR02A_DAR0009.ogg"
    "至" "「噢、真由氏啊。终于看到你了。我在广场闲逛了大概２０分钟了」"
    $ stopvoc("MAY")
    play MAY "DAR02A_MAY0001"
    $ current_voice = "voice/DAR02A_MAY0001.ogg"
    "真由理" "「明明打个电话就好了」"
    $ stopvoc("DAR")
    play DAR "DAR02A_DAR0010"
    $ current_voice = "voice/DAR02A_DAR0010.ogg"
    "至" "「当我以为在夏Ｃｏｍｉ会场还能打得通电话的时候，我还是太年轻了」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_ASA04"),"True","lh/MAY_ASA04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "DAR02A_MAY0002"
    $ current_voice = "voice/DAR02A_MAY0002.ogg"
    "真由理" "「啊、也是。确实我也有这种感觉。从刚才开始都在打电话给萌郁、但是一直说不在服务区。」"
    $ stopvoc("DAR")
    play DAR "DAR02A_DAR0011"
    $ current_voice = "voice/DAR02A_DAR0011.ogg"
    "至" "「诶？和桐生氏走散了吗？」"
    $ stopvoc("MAY")
    play MAY "DAR02A_MAY0003"
    $ current_voice = "voice/DAR02A_MAY0003.ogg"
    "真由理" "「可以说是走散了。早上开始到现在都在试图联系她，但今天一次都没见着」"
    $ stopvoc("MAY")
    play MAY "DAR02A_MAY0004"
    $ current_voice = "voice/DAR02A_MAY0004.ogg"
    "真由理" "「我想差不多可能回到这里了吧、真是搞不明白啊」"
    $ stopvoc("DAR")
    play DAR "DAR02A_DAR0012"
    $ current_voice = "voice/DAR02A_DAR0012.ogg"
    "至" "「唔、我明明是为了能够让桐生氏擅长工口ｃｏｓ才来到这里的」"
    $ stopvoc("MAY")
    play MAY "DAR02A_MAY0005"
    $ current_voice = "voice/DAR02A_MAY0005.ogg"
    "真由理" "「嗯……虽然我也在找铃羽」"
    $ stopvoc("DAR")
    play DAR "DAR02A_DAR0013"
    $ current_voice = "voice/DAR02A_DAR0013.ogg"
    "至" "「铃羽……是指阿万音氏吗？她也来了吗？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_ASA01"),"True","lh/MAY_ASA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "DAR02A_MAY0006"
    $ current_voice = "voice/DAR02A_MAY0006.ogg"
    "真由理" "「来了啊。刚才我突然被她叫了一声，吓了一跳哦」"
    $ stopvoc("DAR")
    play DAR "DAR02A_DAR0014"
    $ current_voice = "voice/DAR02A_DAR0014.ogg"
    "至" "「呵呵～，阿万音氏明明对夏Ｃｏｍｉ完全没有兴趣来着。真是感到意外啊」"
    $ stopvoc("MAY")
    play MAY "DAR02A_MAY0007"
    $ current_voice = "voice/DAR02A_MAY0007.ogg"
    "真由理" "「也是啊。啊、说曹操曹操就到」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    "顺着真由氏的手指看去，是平日打扮的阿万音氏。"
    "她一边挥着手一边走了过来。"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_ASA06"),"True","lh/SUZ_ASA06a~ipad.png") at left as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_ASA01"),"True","lh/MAY_ASA01a~ipad.png") at right as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "DAR02A_SUZ0000"
    $ current_voice = "voice/DAR02A_SUZ0000.ogg"
    "铃羽" "「椎名真由理～。虽然我也一直在找桐生萌郁、但很遗憾并没有找到」"
    $ stopvoc("DAR")
    play DAR "DAR02A_DAR0015"
    $ current_voice = "voice/DAR02A_DAR0015.ogg"
    "至" "「什么呀、阿万音氏你没有出ｃｏｓ啊……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_ASA01"),"True","lh/SUZ_ASA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "DAR02A_SUZ0001"
    $ current_voice = "voice/DAR02A_SUZ0001.ogg"
    "铃羽" "「早、早啊、桥田至。拿的东西真多啊。这些全部都是买的吗？」"
    $ stopvoc("DAR")
    play DAR "DAR02A_DAR0016"
    $ current_voice = "voice/DAR02A_DAR0016.ogg"
    "至" "「算是吧。这些就是今天的战利品」"
    $ stopvoc("DAR")
    play DAR "DAR02A_DAR0017"
    $ current_voice = "voice/DAR02A_DAR0017.ogg"
    "至" "「比起这个阿万音氏啊、你既然来到了这里、是不是对Ｃｏｓｐｌａｙ有兴趣啊？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_ASA03"),"True","lh/SUZ_ASA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "DAR02A_SUZ0002"
    $ current_voice = "voice/DAR02A_SUZ0002.ogg"
    "铃羽" "「诶？　嗯、嘛。啊哈哈」"
    $ stopvoc("DAR")
    play DAR "DAR02A_DAR0018"
    $ current_voice = "voice/DAR02A_DAR0018.ogg"
    "至" "「等下、这算什么微妙的反应」"
    $ stopvoc("SUZ")
    play SUZ "DAR02A_SUZ0003"
    $ current_voice = "voice/DAR02A_SUZ0003.ogg"
    "铃羽" "「呀、我对这东西嘛、完全没有相关知识啊。只不过、在找人而已」"
    $ stopvoc("DAR")
    play DAR "DAR02A_DAR0019"
    $ current_voice = "voice/DAR02A_DAR0019.ogg"
    "至" "「不是桐生氏吗？」"
    $ stopvoc("SUZ")
    play SUZ "DAR02A_SUZ0004"
    $ current_voice = "voice/DAR02A_SUZ0004.ogg"
    "铃羽" "「嗯、不是她。是我认识的一个人」"
    $ stopvoc("MAY")
    play MAY "DAR02A_MAY0008"
    $ current_voice = "voice/DAR02A_MAY0008.ogg"
    "真由理" "「是吗？　如果是ｃｏｓｅｒ的话、我还是认识不少的、要一起找吗？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_ASA01"),"True","lh/SUZ_ASA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "DAR02A_SUZ0005"
    $ current_voice = "voice/DAR02A_SUZ0005.ogg"
    "铃羽" "「没事了。也不是一定要去见她」"
    $ stopvoc("SUZ")
    play SUZ "DAR02A_SUZ0006"
    $ current_voice = "voice/DAR02A_SUZ0006.ogg"
    "铃羽" "「比起这个、桐生萌郁的事情怎么样？　还要再找下吗？」"
    $ stopvoc("DAR")
    play DAR "DAR02A_DAR0020"
    $ current_voice = "voice/DAR02A_DAR0020.ogg"
    "至" "「我也全力以赴地来找吧。」"
    $ stopvoc("DAR")
    play DAR "DAR02A_DAR0021"
    $ current_voice = "voice/DAR02A_DAR0021.ogg"
    "至" "「为了能够瞻仰到桐生氏宝贵的 Ｃｏｓ 、这只不过是小事。常考。」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_ASA02"),"True","lh/MAY_ASA02a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "DAR02A_MAY0009"
    $ current_voice = "voice/DAR02A_MAY0009.ogg"
    "真由理" "「桶子君、好帅气啊～♪」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_ASA06"),"True","lh/SUZ_ASA06a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "DAR02A_SUZ0007"
    $ current_voice = "voice/DAR02A_SUZ0007.ogg"
    "铃羽" "「是、是吗？　不如说是意图太明显了……」"
    $ stopvoc("DAR")
    play DAR "DAR02A_DAR0022"
    $ current_voice = "voice/DAR02A_DAR0022.ogg"
    "至" "「嗯？　那个？　在那里的那位、不就是桐生氏吗？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_ASA01"),"True","lh/SUZ_ASA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_ASA01"),"True","lh/MAY_ASA01a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "DAR02A_MAY0010"
    $ current_voice = "voice/DAR02A_MAY0010.ogg"
    "真由理" "「诶？　哪里？」"
    $ stopvoc("DAR")
    play DAR "DAR02A_DAR0023"
    $ current_voice = "voice/DAR02A_DAR0023.ogg"
    "至" "「看、在那儿！　虽然离得有点远」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_ASB02"),"True","lh/SUZ_ASB02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_ASC02"),"True","lh/MAY_ASC02a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "DAR02A_MAY0011"
    $ current_voice = "voice/DAR02A_MAY0011.ogg"
    "真由理" "「嗯～？」"
    $ stopvoc("SUZ")
    play SUZ "DAR02A_SUZ0008"
    $ current_voice = "voice/DAR02A_SUZ0008.ogg"
    "铃羽" "「我虽然视力很好、但是在这么多人的地方也没法精确地锁定目标」"
    $ stopvoc("DAR")
    play DAR "DAR02A_DAR0024"
    $ current_voice = "voice/DAR02A_DAR0024.ogg"
    "至" "「所以、那个看起来穿着紧身衣的不管怎么看都是黑猫嘛」"
    $ stopvoc("DAR")
    play DAR "DAR02A_DAR0025"
    $ current_voice = "voice/DAR02A_DAR0025.ogg"
    "至" "「那我就先去了！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_ASA03"),"True","lh/MAY_ASA03a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "DAR02A_MAY0012"
    $ current_voice = "voice/DAR02A_MAY0012.ogg"
    "真由理" "「啊、桶子君、等一下」"
    stop bgm 
    window hide


    $ loadBG(2,"IBGX048")



    play se "SGSE007L" loop
    hide screen phonebtn
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_CAMEKO"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_CAMEKO"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_CAMEKO"])
    "在摆出各种ＰＯＳＥ的ｃｏｓｅｒ和架好照相机的{color=#f00}相僧{/color}组成的空隙中穿梭着。"
    $ stopvoc("SUZ")
    play SUZ "DAR02A_SUZ0009"
    $ current_voice = "voice/DAR02A_SUZ0009.ogg"
    "铃羽" "「桥田至！　等、等一下──」"
    "后面阿万音氏的身影离我们越来越远。"
    $ stopvoc("DAR")
    play DAR "DAR02A_DAR0026"
    $ current_voice = "voice/DAR02A_DAR0026.ogg"
    "至" "「虽然感觉有点对不起阿万音氏、但作为头一回来夏Ｃｏｍｉ的新人、想跟上我还是不可能的」"
    "如果是普通的跑步和走路，我这样的体型连真由氏可能都比不过。"
    "但是、在夏Ｃｏｍｉ的人流中快速移动这一点可是谁都赢不了我的。"
    "而且我现在的状况可是，身上背着包，两手拿着几个袋子这样的重装备状态啊。"
    "嘛、当然对于夏Ｃｏｍｉ的参加者来说、这点程度的话自然是理所当然的了。"
    "就在这个时候眼前出现了桐生氏的身影。"
    $ stopvoc("DAR")
    play DAR "DAR02A_DAR0027"
    $ current_voice = "voice/DAR02A_DAR0027.ogg"
    "至" "「喔、有了有了、桐生氏──」"
    "招呼了一声后，马上就注意到了。"
    "那位ｃｏｓｅｒ不是桐生氏这件事。"
    "为什么呢，因为那个人穿的服装，不是黑猫的。"
    "然后再看了下脸，果然不是桐生。"
    "但是、也非常滴可爱。"
    "要是出了ｃｏｓｅｒ写真集的话绝对几个小时内就能卖掉一百本。"
    "但是、这个 Ｃｏｓ 的不是筷女吗！"
    "就凭这一点我就喜欢上了。"
    "我想娶她做老婆啊。"
    $ stopvoc("X06")
    play voc "DAR02A_X060000"
    $ current_voice = "voice/DAR02A_X060000.ogg"
    "???" "「啊」"
    "结果就和那个筷女的Ｃｏｓｅｒ背靠背地撞上了。"
    "这样摇曳着的少女、瞬间击溃了我的心理防线。"
    play se "SGSE014"

    stop se
    hide screen phoneSD1
    window hide
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_DAR001A"]]["Check"]=True


    $ loadBG(2,"EV_DAR001A")



    hide screen phonebtn
    $ stopvoc("X06")
    play voc "DAR02A_X060001"
    $ current_voice = "voice/DAR02A_X060001.ogg"
    "???" "「抱歉」"
    $ stopvoc("DAR")
    play DAR "DAR02A_DAR0028"
    $ current_voice = "voice/DAR02A_DAR0028.ogg"
    "至" "「哦、哦……」"
    play bgm "FD2BGM09"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_KUNKA"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_KUNKA"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_KUNKA"])
    "哇，味道好棒啊。感觉就要{color=#f00}咕哈咕哈{/color}啊哈啊哈了，但果然还是自重点。"
    "要是在这里犯下变态行为的话，就会瞬间传遍整个广场，然后我估计就会成为这里所有人的公敌，再也无法进入Ｃｏｓｐｌａｙ广场了。"
    "我不是变态、我是变态绅士。"
    "桥田至轻轻地走了，不带走一片云彩。"
    $ stopvoc("X06")
    play voc "DAR02A_X060002"
    $ current_voice = "voice/DAR02A_X060002.ogg"
    "???" "「真是非常抱歉」"
    $ stopvoc("X06")
    play voc "DAR02A_X060003"
    $ current_voice = "voice/DAR02A_X060003.ogg"
    "???" "「这个创可贴，请拿去用吧」"
    $ stopvoc("DAR")
    play DAR "DAR02A_DAR0029"
    $ current_voice = "voice/DAR02A_DAR0029.ogg"
    "至" "「没、没事的。没有什么问题」"
    "一边说着、不由得就接下了一个东西。"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_WOOPA"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_WOOPA"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_WOOPA"])
    "看了下、是在雷ＮＥＴ翔里出现过的“{color=#f00}呜啪{/color}”图案的创可贴。"
    "为什么是创可贴？"
    "明明我没有怎么受伤啊。"
    $ stopvoc("DAR")
    play DAR "DAR02A_DAR0030"
    $ current_voice = "voice/DAR02A_DAR0030.ogg"
    "至" "「那么」"
    stop bgm 
    window hide


    $ loadBG(2,"BG56A")



    show screen phonebtn
    show screen phoneSD1
    play se "SGSE007L" loop
    "跟筷女氏说再见后、只能回到真由氏那里了。"
    $ stopvoc("DAR")
    play DAR "DAR02A_DAR0031"
    $ current_voice = "voice/DAR02A_DAR0031.ogg"
    "至" "「……给撞倒的人递上创可贴、通常都会给人深刻的印象、常考。话又说回来、是想立个ＦＬＡＧ吗？」"
    "到底是以什么样的表情看我离开的呢，真是非常在意。"
    "突然转身一看。"
    $ stopvoc("DAR")
    play DAR "DAR02A_DAR0032"
    $ current_voice = "voice/DAR02A_DAR0032.ogg"
    "至" "「额、这么快就不见了啊！」"
    "我也知道其实她对我并没有任何兴趣。"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_ASB03"),"True","lh/SUZ_ASB03a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "DAR02A_SUZ0010"
    $ current_voice = "voice/DAR02A_SUZ0010.ogg"
    "铃羽" "「啊、有了！　桥田至、你啊、真是走得太快了！」"
    $ stopvoc("SUZ")
    play SUZ "DAR02A_SUZ0011"
    $ current_voice = "voice/DAR02A_SUZ0011.ogg"
    "铃羽" "「那个、怎么了呢？　脸上一副难过的表情啊」"
    $ stopvoc("DAR")
    play DAR "DAR02A_DAR0033"
    $ current_voice = "voice/DAR02A_DAR0033.ogg"
    "至" "「但是只有小白脸的忧伤才有意义」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_ASA03"),"True","lh/SUZ_ASA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("SUZ")
    play SUZ "DAR02A_SUZ0012"
    $ current_voice = "voice/DAR02A_SUZ0012.ogg"
    "铃羽" "「诶？」"
    $ stopvoc("DAR")
    play DAR "DAR02A_DAR0034"
    $ current_voice = "voice/DAR02A_DAR0034.ogg"
    "至" "「虽然很悲伤、但这就是现实」"
    "我的恋爱、只不过持续了３０秒。"
    $ stopvoc("DAR")
    play DAR "DAR02A_DAR0035"
    $ current_voice = "voice/DAR02A_DAR0035.ogg"
    "至" "「三次元的妹子攻略难度太高了。常考」"
    $ stopvoc("DAR")
    play DAR "DAR02A_DAR0036"
    $ current_voice = "voice/DAR02A_DAR0036.ogg"
    "至" "「唔哦哦哦、赶快回去刷通我的战利品吧！」"
    "其实心里是在流血的。"


    stop se
    hide screen phoneSD1
    window hide
    hide screen phonebtn
    $ loadBG(0,"BG_BLACK",trans=Fade(1,1,1))
    window hide






    return
