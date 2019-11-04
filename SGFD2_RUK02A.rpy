label SGFD2_RUK02A:
    hide screen phonebtn
    scene expression Solid("000000")  with fade
    python:
        cml = {}
        sml = []
        rml = []
        lml = []

    window hide


    $ loadBG(0,"BG16E1")

    play bgm "BGM07"

    $ date="8/18"
    hide screen phonebtn
    hide screen phoneSD1

    "到达秋叶原大道时，那里果然还是一成不变的景色。"
    "我现在真的是在两天前的世界吧？"
    $ stopvoc("RUK")
    play RUK "RUK02A_RUK0000"
    $ current_voice = "voice/RUK02A_RUK0000.ogg"
    "琉华" "「对了……！」"
    "我终于意识到了手里一直紧握着自己的手机。"
    "慌慌张张地确认了下日期"
    show screen phonebtn
    show screen phoneSD1
    "──８月１８日　１８点４６分。"
    "在那个房间——未来道具研究所里面看见的时间确实是为２０日。"
    "当然，说不定是手机坏掉了。但是从突然从未来道具研究所来到秋叶原站前这一点来看，回到两天前的可能性还是很高的。"



    $ loadBG(2,"IBGX033")



    "说起来我没有多少时间可以耽搁了。"
    "要说为什么，那是因为还要往回跳两天。"
    "又要感受一次那样的痛苦了，虽然这么想，但是作为惩罚的话那种程度的痛苦就根本不算什么了。"
    "我下定了决心，再次向研究所走去。"
    "与此同时，在路上看见了熟悉的人。"




    $ loadBG(2,"BG16E1")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA01"),"True","lh/DAR_ASA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    show screen phonebtn
    show screen phoneSD1
    stop bgm 

    $ targetmailid = gc["ScriptMacros"]["RM_RUK_RECV_UPP01_01"]

    $ LR_RM_CHANCE=2
    call CHECK_RM_RECEIVE
    $ stopvoc("RUK")
    play RUK "RUK02A_RUK0001"
    $ current_voice = "voice/RUK02A_RUK0001.ogg"
    "琉华" "「啊……」"
    call CHECK_RM_RECEIVE
    $ stopvoc("DAR")
    play DAR "RUK02A_DAR0000"
    $ current_voice = "voice/RUK02A_DAR0000.ogg"
    "至" "「……琉华氏……」"

    call CHECK_RM_RECEIVE
    play bgm "FD2BGM04"
    "几乎同时发现我的桥田君慢悠悠地靠了过来，小声地叫着我的名字。"
    $ stopvoc("RUK")
    play RUK "RUK02A_RUK0002"
    $ current_voice = "voice/RUK02A_RUK0002.ogg"
    "琉华" "「那、那个……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA08"),"True","lh/DAR_ASA08a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    $ stopvoc("DAR")
    play DAR "RUK02A_DAR0001"
    $ current_voice = "voice/RUK02A_DAR0001.ogg"
    "至" "「啊啊、虽然很抱歉但我没有去守夜哦。」"
    $ stopvoc("RUK")
    play RUK "RUK02A_RUK0003"
    $ current_voice = "voice/RUK02A_RUK0003.ogg"
    "琉华" "「诶？」"
    $ stopvoc("DAR")
    play DAR "RUK02A_DAR0002"
    $ current_voice = "voice/RUK02A_DAR0002.ogg"
    "至" "「诶？　琉华氏不是现在要去那个么，守夜。恩……真由氏的……」"
    $ stopvoc("RUK")
    play RUK "RUK02A_RUK0004"
    $ current_voice = "voice/RUK02A_RUK0004.ogg"
    "琉华" "「啊……」"

    "说起来……"
    "说起１８日，之后不就是真由理酱的守夜仪式么。"
    "真由理酱倒下的时候是１５日。"
    "本来应该１６日就举行守夜仪式的，但因为１７日据说是友引之日，就延期到了１８日。（友引：历书注释的一种，认为这一天无论做什么都不分胜败的日子。因有“拉朋友去”之意，所以这一天忌出殡）"
    "说起来……桥田当时确实没有来守夜。"
    "说起来……"
    "我现在才注意到自己穿着学校的制服。"
    "而且，不仅仍不清楚为何头痛，眼睑边上也感觉火辣辣地疼。"
    "这肯定是因为我这几天一直都在哭泣吧。"
    "那么，果然我已经回到了两天前——也就是１８日的世界了。"

    $ stopvoc("DAR")
    play DAR "RUK02A_DAR0003"
    $ current_voice = "voice/RUK02A_DAR0003.ogg"
    "至" "「所以说我先……」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    $ stopvoc("RUK")
    play RUK "RUK02A_RUK0005"
    $ current_voice = "voice/RUK02A_RUK0005.ogg"
    "琉华" "「那、那个！」"
    "我没有多想就叫住了正要离开的桥田君。"

    $ gd["RCVmailData"][gc["ScriptMacros"]["RM_RUK_RECV_UPP01_01"]]["late"]=True
    $ lml.append(gc["ScriptMacros"]["RM_RUK_RECV_UPP01_01"])

    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASB01"),"True","lh/DAR_ASB01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "RUK02A_DAR0004"
    $ current_voice = "voice/RUK02A_DAR0004.ogg"
    "至" "「……？　怎么了？」"
    $ stopvoc("RUK")
    play RUK "RUK02A_RUK0006"
    $ current_voice = "voice/RUK02A_RUK0006.ogg"
    "琉华" "「那个……为什么……」"
    $ stopvoc("RUK")
    play RUK "RUK02A_RUK0007"
    $ current_voice = "voice/RUK02A_RUK0007.ogg"
    "琉华" "「桥田君为什么不去呢？　守夜仪式……真由理酱的。」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASB09"),"True","lh/DAR_ASB09a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    $ stopvoc("DAR")
    play DAR "RUK02A_DAR0005"
    $ current_voice = "voice/RUK02A_DAR0005.ogg"
    "至" "「……那是因为……」"
    "桥田君稍稍压低了帽檐来隐藏自己的视线。"
    $ stopvoc("DAR")
    play DAR "RUK02A_DAR0006"
    $ current_voice = "voice/RUK02A_DAR0006.ogg"
    "至" "「去了的话，真的就必须承认了呐。」"
    $ stopvoc("RUK")
    play RUK "RUK02A_RUK0008"
    $ current_voice = "voice/RUK02A_RUK0008.ogg"
    "琉华" "「啊……」"
    $ stopvoc("DAR")
    play DAR "RUK02A_DAR0007"
    $ current_voice = "voice/RUK02A_DAR0007.ogg"
    "至" "「如果去守夜的话，真由氏就真的死掉了啊。」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA09"),"True","lh/DAR_ASA09a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    $ stopvoc("DAR")
    play DAR "RUK02A_DAR0008"
    $ current_voice = "voice/RUK02A_DAR0008.ogg"
    "至" "「虽然只是说说，但我还没能接受真由氏已经去世这件事呐。」"
    $ stopvoc("RUK")
    play RUK "RUK02A_RUK0009"
    $ current_voice = "voice/RUK02A_RUK0009.ogg"
    "琉华" "「桥田……」"
    $ stopvoc("DAR")
    play DAR "RUK02A_DAR0009"
    $ current_voice = "voice/RUK02A_DAR0009.ogg"
    "至" "「因为，你看真由氏在那之前一直都是很有活力的吧。向往常一样，一直都是很有精神地微笑着的吧。」"
    $ stopvoc("DAR")
    play DAR "RUK02A_DAR0010"
    $ current_voice = "voice/RUK02A_DAR0010.ogg"
    "至" "「明明是这样突然就死掉了什么的，就算告诉我我也没法相信嘛」"
    "桥田在15号那天和真由里一起去了夏Ｃｏｍｉ。"
    "事情正是发生在回来的路途上。"
    "所以桥田也在场。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA08"),"True","lh/DAR_ASA08a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    $ stopvoc("DAR")
    play DAR "RUK02A_DAR0011"
    $ current_voice = "voice/RUK02A_DAR0011.ogg"
    "至" "「琉华氏知道吗？ “事物是在由观测者观测后才决定下来的”。」（量子力学知识：在观测者的干涉之前，任何事物处于所有可能性的叠加状态，这种状态在观测者进行观测后坍缩成其中的一种）"
    $ stopvoc("DAR")
    play DAR "RUK02A_DAR0012"
    $ current_voice = "voice/RUK02A_DAR0012.ogg"
    "至" "「所以我不去看到话，真由氏就没有死掉哦。」"
    $ stopvoc("DAR")
    play DAR "RUK02A_DAR0013"
    $ current_voice = "voice/RUK02A_DAR0013.ogg"
    "至" "「在我心中，真由氏就没有死，一直好好地活着哟。」"
    $ stopvoc("RUK")
    play RUK "RUK02A_RUK0010"
    $ current_voice = "voice/RUK02A_RUK0010.ogg"
    "琉华" "「那个，那么说的话确实……」"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_CHUNI"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_CHUNI"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_CHUNI"])
    $ stopvoc("DAR")
    play DAR "RUK02A_DAR0014"
    $ current_voice = "voice/RUK02A_DAR0014.ogg"
    "至" "「量子力学。感觉如今已经变成{color=#f00}中二病{/color}必须掌握的知识。但现在又觉得中二病什么的，还是好想相信有这回事啊……」"
    "对了，以前这种事情冈部师傅和父亲都说过。"
    "量子力学……"
    "我虽然不怎么清楚……"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA01"),"True","lh/DAR_ASA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    $ stopvoc("DAR")
    play DAR "RUK02A_DAR0015"
    $ current_voice = "voice/RUK02A_DAR0015.ogg"
    "至" "「对了，琉华氏。顺便一说，小冈伦那去了也没啥用了。」"
    "说到这里，桥田君的声音变得冷淡起来。"
    $ stopvoc("RUK")
    play RUK "RUK02A_RUK0011"
    $ current_voice = "voice/RUK02A_RUK0011.ogg"
    "琉华" "「诶？　已经没用了嘛？」"
    $ stopvoc("DAR")
    play DAR "RUK02A_DAR0016"
    $ current_voice = "voice/RUK02A_DAR0016.ogg"
    "至" "「没用没用，一直窝在实验室，就算打了电话也不回。」"
    $ stopvoc("RUK")
    play RUK "RUK02A_RUK0012"
    $ current_voice = "voice/RUK02A_RUK0012.ogg"
    "琉华" "「…………」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASB12"),"True","lh/DAR_ASB12a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    $ stopvoc("DAR")
    play DAR "RUK02A_DAR0017"
    $ current_voice = "voice/RUK02A_DAR0017.ogg"
    "至" "「说来也是呢，现在才装出一副受打击的样子也太迟了点吧」"
    $ stopvoc("RUK")
    play RUK "RUK02A_RUK0013"
    $ current_voice = "voice/RUK02A_RUK0013.ogg"
    "琉华" "「装出？」"
    $ stopvoc("DAR")
    play DAR "RUK02A_DAR0018"
    $ current_voice = "voice/RUK02A_DAR0018.ogg"
    "至" "「是哦。琉华氏那时不在场不知道的说，但说实话我也确实看错了小冈伦呢。」"
    "确实受到了很大的冲击。"
    "我从来没见过桥田君这么评价冈部。"
    $ stopvoc("DAR")
    play DAR "RUK02A_DAR0019"
    $ current_voice = "voice/RUK02A_DAR0019.ogg"
    "至" "「那一天，从夏Ｃｏｍｉ回来的时候，你知道冈伦看到真由理突然倒在地上是什么表情吗？」"
    $ stopvoc("DAR")
    play DAR "RUK02A_DAR0020"
    $ current_voice = "voice/RUK02A_DAR0020.ogg"
    "至" "「完全不为所动地看着啊！」"
    "桥田君说到这里，口气变得激动起来。"
    $ stopvoc("DAR")
    play DAR "RUK02A_DAR0021"
    $ current_voice = "voice/RUK02A_DAR0021.ogg"
    "至" "「他就那样一副面无表情的样子说，真由理死了哦！」"
    $ stopvoc("DAR")
    play DAR "RUK02A_DAR0022"
    $ current_voice = "voice/RUK02A_DAR0022.ogg"
    "至" "「真难以相信啊！　那可是青梅竹马？　从小到大一直相伴身边的对象哦？」"
    $ stopvoc("DAR")
    play DAR "RUK02A_DAR0023"
    $ current_voice = "voice/RUK02A_DAR0023.ogg"
    "至" "「明明就那样突然倒在地上了！」"
    $ stopvoc("DAR")
    play DAR "RUK02A_DAR0024"
    $ current_voice = "voice/RUK02A_DAR0024.ogg"
    "至" "「真由氏已经死了没法回来了，还说什么“这些我知道”！」"
    $ stopvoc("RUK")
    play RUK "RUK02A_RUK0014"
    $ current_voice = "voice/RUK02A_RUK0014.ogg"
    "琉华" "「不、不对桥田君，那是因为……」"
    $ stopvoc("DAR")
    play DAR "RUK02A_DAR0025"
    $ current_voice = "voice/RUK02A_DAR0025.ogg"
    "至" "「不对？　哪里不对了！？」"

    $ targetmailid = cml.setdefault("RM_RUK_SEND_UPP01","")

    $ LR_RM_CHANCE=2
    call CHECK_RM_RECEIVE
    $ stopvoc("RUK")
    play RUK "RUK02A_RUK0015"
    $ current_voice = "voice/RUK02A_RUK0015.ogg"
    "琉华" "「那是、那个……」"
    call CHECK_RM_RECEIVE
    $ stopvoc("DAR")
    play DAR "RUK02A_DAR0026"
    $ current_voice = "voice/RUK02A_DAR0026.ogg"
    "至" "「我原本以为，小冈伦是个重情谊的家伙呢。」"

    call CHECK_RM_RECEIVE
    $ stopvoc("DAR")
    play DAR "RUK02A_DAR0027"
    $ current_voice = "voice/RUK02A_DAR0027.ogg"
    "至" "「以为他虽然平时满口中二病发言，但心底里还是很在意别人的心情。」"

    $ gd["RCVmailData"][gc["ScriptMacros"]["RM_RUK_RECV_UPP02_01"]]["late"]=True
    $ lml.append(gc["ScriptMacros"]["RM_RUK_RECV_UPP02_01"])


    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASB10"),"True","lh/DAR_ASB10a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    $ stopvoc("DAR")
    play DAR "RUK02A_DAR0028"
    $ current_voice = "voice/RUK02A_DAR0028.ogg"
    "至" "「但结果那也……太过分了吧……」"
    "不对！　冈部师傅是因为已经不知道经历了几次这样的现实才会……"
    "因为不断的轮回冈部师傅已经很疲倦了。"

    "就算是这样，我也没有说出来。"
    "冈部师傅也没有告诉桥田君这些。"
    "如果有告诉他的打算的话，应该早就说了。"
    "关于自己一次又一次地试着去拯救真由理这件事。"
    "关于自己一次又一次地在这样的痛苦与悲伤中往复的事。"
    "但是，冈部师傅并没有说出来。"
    "就这样甘愿被他人责备，也不愿意做任何辩解。"
    "说出来的话可能大家就能够谅解了，但是他选择了什么也不说，只是默默地去承担这一切。"
    "承担着对真由理见死不救的罪名。"
    "就这样接受着所有人的怨恨。"
    "冈部师傅说他所背负的罪就是那个吧。"
    "然后同时冈部师傅还在不断试图拯救真由里，这样的情况已经让冈部心力憔悴了。"
    "我又一次加强了对冈部师傅的觉悟的认识。"
    "背负罪责的觉悟。"


    hide screen phoneSD1
    window hide



    $ loadBG(0,"BG79E1",at=[Transform(yalign=1.0)])








    "与桥田君告别后，我向着未来道具研究所的大楼前进。"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_STUDIO_CRT"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_STUDIO_CRT"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_STUDIO_CRT"])
    "在大楼的一层有一个显像管工房，由叫做天王寺的稍微有些恐怖的店长经营着。"
    "冈部师傅说，开启的巨型显像管是时间跳跃的必要条件。"

    $ stopvoc("RUK")
    play RUK "RUK02A_RUK0016"
    $ current_voice = "voice/RUK02A_RUK0016.ogg"
    "琉华" "「太好了。还开着……」"
    "看见店里还有灯光，我舒了口气。"
    $ stopvoc("RUK")
    play RUK "RUK02A_RUK0017"
    $ current_voice = "voice/RUK02A_RUK0017.ogg"
    "琉华" "「…………」"
    window hide





    hide screen phonebtn
    "从二楼的窗外看外面。"
    "如果回到了过去的话就向过去的冈部师傅请求帮助，冈部师傅是这么对我说的。"
    window hide


    $ loadBG(0,"BG_BLACK")

    hide screen phonebtn

    stop bgm 
    "从大楼的狭窄阶梯向二楼走去。"
    play se "SGSE024"

    "打开铁门，沉重的铁门声音刺激着神经。"
    "室内非常的阴暗，感觉谁也不在。"
    window hide


    $ loadBG(0,"BG02E2")
    play se "SGSE112"


    show screen phonebtn
    "打开灯。"
    hide screen phonebtn

    show screen phonebtn
    $ stopvoc("RUK")
    play RUK "RUK02A_RUK0018"
    $ current_voice = "voice/RUK02A_RUK0018.ogg"
    "琉华" "「……！」"
    "不对。"
    "房间的里面。"
    "在那里。"
    hide screen phoneSD1
    window hide
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_RUK003A"]]["Check"]=True


    $ loadBG(2,"EV_RUK003A")



    hide screen phonebtn
    play bgm "FD2BGM05"

    $ stopvoc("RUK")
    play RUK "RUK02A_RUK0019"
    $ current_voice = "voice/RUK02A_RUK0019.ogg"
    "琉华" "「冈部……师傅」"
    "躺坐在沙发上的是，冈部师傅。"
    "一开始我以为他睡着了。"
    "因此他对于到来的我没有任何的反应。"
    "但是不对。"
    "冈部师傅的眼睛睁着。"
    "好像在凝望着虚空中的一点……"
    "难道说从１５日的晚上开始就没有睡过吗，眼睛周围的黑眼圈非常的明显。"
    "无精打采地伸了个懒腰，还哈欠连天。"
    "我下意识地屏住呼吸。"
    "冈部师傅已经非常疲倦了。"
    "这是我在真由理的事件发生后的——从实际的时间来看是两天后——第一次见到冈部师傅。"
    "虽然那个时候也很疲劳，但没有到这个程度。"
    "我明白了为何冈部师傅会那样的消沉。"
    "但是我也只是明白了冈部师傅的这个打算。"
    "……"
    $ stopvoc("RUK")
    play RUK "RUK02A_RUK0020"
    $ current_voice = "voice/RUK02A_RUK0020.ogg"
    "琉华" "「那个，冈部师傅……」"
    "试着叫了一下。"
    "但是什么反应都没有。"
    "视线没有动。"
    "真的还有气吗？我感到些许不安。"
    "反正两天后还能见到他，所以应该没问题，但我还是有些担心，所以靠近了一些。"
    $ stopvoc("OKA")
    play OKA "RUK02A_OKA0000"
    $ current_voice = "voice/RUK02A_OKA0000.ogg"
    "伦太郎" "「…………不起……」"
    "靠近了之后，听到了冈部的呢喃。"
    "如果不注意听或者耳朵不好的话根本听不见的细微声音。"
    $ stopvoc("OKA")
    play OKA "RUK02A_OKA0001"
    $ current_voice = "voice/RUK02A_OKA0001.ogg"
    "伦太郎" "「对不起，真由理……对不起……」"
    "说着这样道歉的话语。"
    "冈部不断地说着向真由里谢罪的话。"
    $ stopvoc("RUK")
    play RUK "RUK02A_RUK0021"
    $ current_voice = "voice/RUK02A_RUK0021.ogg"
    "琉华" "「冈部师傅……」"
    "我忍不住抱住了冈部师傅，将他的头抱在怀里。"
    "但是冈部依旧像坏掉的八音盒一样一直一直不断地重复着。"
    "真的想一直呆在冈部师傅的身边。"
    "至少能够分担一点。"
    "但是，还没有能够完成真由里的愿望。"
    $ stopvoc("RUK")
    play RUK "RUK02A_RUK0022"
    $ current_voice = "voice/RUK02A_RUK0022.ogg"
    "琉华" "「冈部师傅，请听我说。」"
    "我缓缓地放开了冈部，把事情说了出来。"
    "我来自两天后。"
    "为了来完成真由里的愿望，还需要继续向前跳跃。"
    "但是。"
    $ stopvoc("OKA")
    play OKA "RUK02A_OKA0002"
    $ current_voice = "voice/RUK02A_OKA0002.ogg"
    "伦太郎" "「抱歉……、抱歉啊、真由理……」"
    $ stopvoc("RUK")
    play RUK "RUK02A_RUK0023"
    $ current_voice = "voice/RUK02A_RUK0023.ogg"
    "琉华" "「…………」"
    "现在冈部师傅根本没法思考这些。"
    window hide


    $ loadBG(2,"BG02E2")



    show screen phonebtn
    show screen phoneSD1
    "到底怎么办呢。"
    "我现在明明只能拜托冈部师傅了。"

    "总之，已经到这个时候了没有时间了。"
    "必须赶快回到两天前，再回到１５日的早上。"
    "现在在这里浪费时间的话，即使回到两天前店面估计都关门了。因为是要回到１５日早上，可能就要多跳一次了。"
    "怎么办。"
    "我自己一个人用这台机器有些不安。"
    "然而也不能告诉桥田君这些事。"

    $ stopvoc("RUK")
    play RUK "RUK02A_RUK0024"
    $ current_voice = "voice/RUK02A_RUK0024.ogg"
    "琉华" "「啊……」"
    "对了，还有一个人。"
    hide screen phoneSD1
    window hide


    $ loadBG(0,"BG03A4")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_BSB01"),"True","lh/CRS_BSB01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    hide screen phonebtn
    $ stopvoc("RUK")
    play RUK "RUK02A_RUK0025"
    $ current_voice = "voice/RUK02A_RUK0025.ogg"
    "琉华" "「牧濑氏……」"
    "据说牧濑在制作时间回溯机器的过程中起了很大的作用。"
    "……"
    "不行，做不到啊。"
    "想一下的话，我都不知道怎么联络牧濑。"
    "可能冈部知道，但是这样擅自地翻他东西的话。"
    window hide


    $ loadBG(0,"BG02E2")

    show screen phonebtn
    show screen phoneSD1
    $ stopvoc("RUK")
    play RUK "RUK02A_RUK0026"
    $ current_voice = "voice/RUK02A_RUK0026.ogg"
    "琉华" "「…………！」"
    "现在这个情况不能考虑这么多了！"
    $ stopvoc("RUK")
    play RUK "RUK02A_RUK0027"
    $ current_voice = "voice/RUK02A_RUK0027.ogg"
    "琉华" "「对不住了，冈部师傅！」"
    window hide


    $ loadBG(2,"PBG01A")



    hide screen phonebtn
    "我捡起了掉落在冈部边上的手机。"
    hide screen phoneSD1
    window hide

    stop bgm 



    $ loadBG(0,"BG05N1")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_HSA01"),"True","lh/CRS_HSA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    show screen phonebtn
    show screen phoneSD1
    play bgm "FD2BGM11"

    $ stopvoc("CRS")
    play CRS "RUK02A_CRS0000"
    $ current_voice = "voice/RUK02A_CRS0000.ogg"
    "红莉栖" "「有点吃惊呢。突然有一个不知道的号码给我打电话，结果果然是漆原啊」"
    "接到电话以后牧濑以令人惊讶的速度赶到了实验室。"
    $ stopvoc("RUK")
    play RUK "RUK02A_RUK0028"
    $ current_voice = "voice/RUK02A_RUK0028.ogg"
    "琉华" "「那个……不好意思，突然把你叫出来。」"
    $ stopvoc("CRS")
    play CRS "RUK02A_CRS0001"
    $ current_voice = "voice/RUK02A_CRS0001.ogg"
    "红莉栖" "「没关系，不用在意。刚好就在附近所以不是很麻烦。」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_HSA05"),"True","lh/CRS_HSA05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "RUK02A_CRS0002"
    $ current_voice = "voice/RUK02A_CRS0002.ogg"
    "红莉栖" "「虽然说……本来是该去真由理的守夜式的……」"
    "为什么牧濑会和真由理酱在这么短的时间里就意气相投了呢？"
    $ stopvoc("RUK")
    play RUK "RUK02A_RUK0029"
    $ current_voice = "voice/RUK02A_RUK0029.ogg"
    "琉华" "「如果牧濑能去的话，真由理酱肯定会很开心的」"
    $ stopvoc("CRS")
    play CRS "RUK02A_CRS0003"
    $ current_voice = "voice/RUK02A_CRS0003.ogg"
    "红莉栖" "「应该……是的吧」"
    $ stopvoc("RUK")
    play RUK "RUK02A_RUK0030"
    $ current_voice = "voice/RUK02A_RUK0030.ogg"
    "琉华" "「恩……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_HSA01"),"True","lh/CRS_HSA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "RUK02A_CRS0004"
    $ current_voice = "voice/RUK02A_CRS0004.ogg"
    "红莉栖" "「是吗……既然漆原这么说的话……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_HSC05"),"True","lh/CRS_HSC05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "RUK02A_CRS0005"
    $ current_voice = "voice/RUK02A_CRS0005.ogg"
    "红莉栖" "「诶？　但是你不去吗？　你和真由理不是好……朋友吗？」"
    $ stopvoc("RUK")
    play RUK "RUK02A_RUK0031"
    $ current_voice = "voice/RUK02A_RUK0031.ogg"
    "琉华" "「啊，那个，其实呢……」"
    "就算说了也没事吧。"
    $ stopvoc("CRS")
    play CRS "RUK02A_CRS0006"
    $ current_voice = "voice/RUK02A_CRS0006.ogg"
    "红莉栖" "「……？」"
    "冈部也没有对桥田说实话。"
    "所以也没必要对牧濑说。"
    "但是。"
    $ stopvoc("RUK")
    play RUK "RUK02A_RUK0032"
    $ current_voice = "voice/RUK02A_RUK0032.ogg"
    "琉华" "「其实有一件事想告诉牧濑……！」"
    $ stopvoc("CRS")
    play CRS "RUK02A_CRS0007"
    $ current_voice = "voice/RUK02A_CRS0007.ogg"
    "红莉栖" "「告诉我……？　关于真由理吗？」"
    $ stopvoc("RUK")
    play RUK "RUK02A_RUK0033"
    $ current_voice = "voice/RUK02A_RUK0033.ogg"
    "琉华" "「是的……、其实……」"

    "最后我还是把所有的事情告诉了牧濑。"
    "现在一分一秒都不能浪费了。"
    "但是如果是牧濑的话，应该能够理解这一切并且原谅我们的所作所为的吧。"
    "正因为这么想……"


    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_HSA04"),"True","lh/CRS_HSA04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "RUK02A_CRS0008"
    $ current_voice = "voice/RUK02A_CRS0008.ogg"
    "红莉栖" "「等、等下！让我把思路理清一下。」"
    $ stopvoc("CRS")
    play CRS "RUK02A_CRS0009"
    $ current_voice = "voice/RUK02A_CRS0009.ogg"
    "红莉栖" "「也就是说你来自两天后的世界，而且还要往回跳跃两天，对吧？」"
    $ stopvoc("RUK")
    play RUK "RUK02A_RUK0034"
    $ current_voice = "voice/RUK02A_RUK0034.ogg"
    "琉华" "「对的……」"
    $ stopvoc("CRS")
    play CRS "RUK02A_CRS0010"
    $ current_voice = "voice/RUK02A_CRS0010.ogg"
    "红莉栖" "「用那个时间机器？」"
    $ stopvoc("RUK")
    play RUK "RUK02A_RUK0035"
    $ current_voice = "voice/RUK02A_RUK0035.ogg"
    "琉华" "「是的」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_HSB07"),"True","lh/CRS_HSB07a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "RUK02A_CRS0011"
    $ current_voice = "voice/RUK02A_CRS0011.ogg"
    "红莉栖" "「哦……」"
    "牧濑露出了思考的神情。"
    "关于冈部对于真由理见死不救这一点。"
    "然后是，关于决定两个人一起背负起这个罪行的这一点。"
    "在烦恼着如何定夺这个行为。"
    $ stopvoc("RUK")
    play RUK "RUK02A_RUK0036"
    $ current_voice = "voice/RUK02A_RUK0036.ogg"
    "琉华" "「那个！并不是冈部师傅的错！是我的错！虽然有点难以想象，但是是因为说了想成为女孩子才会让……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_HSC06"),"True","lh/CRS_HSC06a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "RUK02A_CRS0012"
    $ current_voice = "voice/RUK02A_CRS0012.ogg"
    "红莉栖" "「漆原……」"
    $ stopvoc("RUK")
    play RUK "RUK02A_RUK0037"
    $ current_voice = "voice/RUK02A_RUK0037.ogg"
    "琉华" "「是，是的」"
    $ stopvoc("CRS")
    play CRS "RUK02A_CRS0013"
    $ current_voice = "voice/RUK02A_CRS0013.ogg"
    "红莉栖" "「关于这件事，那个……没关系哦。那些……我也是知道的。」"
    $ stopvoc("RUK")
    play RUK "RUK02A_RUK0038"
    $ current_voice = "voice/RUK02A_RUK0038.ogg"
    "琉华" "「诶？」"
    $ stopvoc("CRS")
    play CRS "RUK02A_CRS0014"
    $ current_voice = "voice/RUK02A_CRS0014.ogg"
    "红莉栖" "「之前……和冈部谈过了。」"
    $ stopvoc("RUK")
    play RUK "RUK02A_RUK0039"
    $ current_voice = "voice/RUK02A_RUK0039.ogg"
    "琉华" "「这样……啊。」"
    $ stopvoc("CRS")
    play CRS "RUK02A_CRS0015"
    $ current_voice = "voice/RUK02A_CRS0015.ogg"
    "红莉栖" "「恩。但，冈部已经放弃了对真由理的拯救……什么的……」"
    $ stopvoc("RUK")
    play RUK "RUK02A_RUK0040"
    $ current_voice = "voice/RUK02A_RUK0040.ogg"
    "琉华" "「…………」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_HSB07"),"True","lh/CRS_HSB07a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "RUK02A_CRS0016"
    $ current_voice = "voice/RUK02A_CRS0016.ogg"
    "红莉栖" "「啊，抱歉。也并不是要责怪你们什么。但是，那样的话……」"
    $ stopvoc("CRS")
    play CRS "RUK02A_CRS0017"
    $ current_voice = "voice/RUK02A_CRS0017.ogg"
    "红莉栖" "「如果那是真的话……」"
    "对于接下来的话，我下意识地绷紧了身子。"
    $ stopvoc("CRS")
    play CRS "RUK02A_CRS0018"
    $ current_voice = "voice/RUK02A_CRS0018.ogg"
    "红莉栖" "「如果真是这样，我也就没有什么好说的了……」"
    $ stopvoc("RUK")
    play RUK "RUK02A_RUK0041"
    $ current_voice = "voice/RUK02A_RUK0041.ogg"
    "琉华" "「……」"
    $ stopvoc("CRS")
    play CRS "RUK02A_CRS0019"
    $ current_voice = "voice/RUK02A_CRS0019.ogg"
    "红莉栖" "「因为，可能你们两位的艰辛我真的无法理解吧。」"
    $ stopvoc("RUK")
    play RUK "RUK02A_RUK0042"
    $ current_voice = "voice/RUK02A_RUK0042.ogg"
    "琉华" "「牧濑……」"
    "果然跟牧濑谈这事是对的。"
    "我发自心底地那么认为。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_HSA01"),"True","lh/CRS_HSA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "RUK02A_CRS0020"
    $ current_voice = "voice/RUK02A_CRS0020.ogg"
    "红莉栖" "「那么，让我们出发吧」"
    $ stopvoc("RUK")
    play RUK "RUK02A_RUK0043"
    $ current_voice = "voice/RUK02A_RUK0043.ogg"
    "琉华" "「诶？」"
    $ stopvoc("CRS")
    play CRS "RUK02A_CRS0021"
    $ current_voice = "voice/RUK02A_CRS0021.ogg"
    "红莉栖" "「不是必须回到前天嘛？所以说，不快点的话。」"
    $ stopvoc("RUK")
    play RUK "RUK02A_RUK0044"
    $ current_voice = "voice/RUK02A_RUK0044.ogg"
    "琉华" "「啊……、是、是的！」"
    hide screen phoneSD1
    window hide



    $ loadBG(0,"BG02N2")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_HSA05"),"True","lh/CRS_HSA05a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    show screen phoneSD1
    $ stopvoc("CRS")
    play CRS "RUK02A_CRS0022"
    $ current_voice = "voice/RUK02A_CRS0022.ogg"
    "红莉栖" "「…………」"
    hide screen phoneSD1
    window hide
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_RUK003B"]]["Check"]=True


    $ loadBG(2,"EV_RUK003B")



    hide screen phonebtn
    $ stopvoc("OKA")
    play OKA "RUK02A_OKA0003"
    $ current_voice = "voice/RUK02A_OKA0003.ogg"
    "伦太郎" "「……对不起……、真由理……」"
    "进入房间的牧濑，用哀怨的目光看着神游物外的冈部师傅。"
    $ stopvoc("CRS")
    play CRS "RUK02A_CRS0023"
    $ current_voice = "voice/RUK02A_CRS0023.ogg"
    "红莉栖" "「冈部……」"
    $ stopvoc("RUK")
    play RUK "RUK02A_RUK0045"
    $ current_voice = "voice/RUK02A_RUK0045.ogg"
    "琉华" "「…………」"
    window hide



    $ loadBG(2,"BG02N2")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_HSA01"),"True","lh/CRS_HSA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    show screen phonebtn
    show screen phoneSD1
    $ stopvoc("CRS")
    play CRS "RUK02A_CRS0024"
    $ current_voice = "voice/RUK02A_CRS0024.ogg"
    "红莉栖" "「……抱歉。已经没时间了，那么快点来这里吧。」"
    $ stopvoc("RUK")
    play RUK "RUK02A_RUK0046"
    $ current_voice = "voice/RUK02A_RUK0046.ogg"
    "琉华" "「好、好的！」"
    window hide


    $ loadBG(2,"BG03A4")



    play se "SGSE342L" loop

    $ stopvoc("CRS")
    play CRS "RUK02A_CRS0025"
    $ current_voice = "voice/RUK02A_CRS0025.ogg"
    "红莉栖" "「说真的这东西不知道会对人体造成什么样的影响，尽可能的话不太想用……」"
    "一边轻快地准备着设备的牧濑如是说道。"
    $ stopvoc("CRS")
    play CRS "RUK02A_CRS0026"
    $ current_voice = "voice/RUK02A_CRS0026.ogg"
    "红莉栖" "「但是……是为了完成真由里的梦想啊。」"
    $ stopvoc("RUK")
    play RUK "RUK02A_RUK0047"
    $ current_voice = "voice/RUK02A_RUK0047.ogg"
    "琉华" "「牧濑……」"
    window hide
    stop se

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_HSC05"),"True","lh/CRS_HSC05a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "RUK02A_CRS0027"
    $ current_voice = "voice/RUK02A_CRS0027.ogg"
    "红莉栖" "「……漆原。我也拜托你了，让真由理做一个好梦……」"
    "不断眨眼的牧濑终于抑不住泪水。"
    $ stopvoc("CRS")
    play CRS "RUK02A_CRS0028"
    $ current_voice = "voice/RUK02A_CRS0028.ogg"
    "红莉栖" "「那么跳到１６日了以后就来和我联络吧」"
    $ stopvoc("RUK")
    play RUK "RUK02A_RUK0048"
    $ current_voice = "voice/RUK02A_RUK0048.ogg"
    "琉华" "「诶？」"
    $ stopvoc("CRS")
    play CRS "RUK02A_CRS0029"
    $ current_voice = "voice/RUK02A_CRS0029.ogg"
    "红莉栖" "「大概，两天前的冈部也在这么做……」"
    "对了，去了两天前的话现在的时间就不存在了。"
    $ stopvoc("RUK")
    play RUK "RUK02A_RUK0049"
    $ current_voice = "voice/RUK02A_RUK0049.ogg"
    "琉华" "「在下……、好像明白了」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_HSA01"),"True","lh/CRS_HSA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "RUK02A_CRS0030"
    $ current_voice = "voice/RUK02A_CRS0030.ogg"
    "红莉栖" "「明白了什么？」"
    $ stopvoc("RUK")
    play RUK "RUK02A_RUK0050"
    $ current_voice = "voice/RUK02A_RUK0050.ogg"
    "琉华" "「冈部师傅选择牧濑作为他的助手的……原因。」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_HSC06"),"True","lh/CRS_HSC06a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "RUK02A_CRS0031"
    $ current_voice = "voice/RUK02A_CRS0031.ogg"
    "红莉栖" "「…………助手、啊」"
    $ stopvoc("RUK")
    play RUK "RUK02A_RUK0051"
    $ current_voice = "voice/RUK02A_RUK0051.ogg"
    "琉华" "「……」"
    $ stopvoc("CRS")
    play CRS "RUK02A_CRS0032"
    $ current_voice = "voice/RUK02A_CRS0032.ogg"
    "红莉栖" "「……如果真把我当助手，这个节骨眼上拜托我不就好了……笨蛋……」"
    $ stopvoc("RUK")
    play RUK "RUK02A_RUK0052"
    $ current_voice = "voice/RUK02A_RUK0052.ogg"
    "琉华" "「牧濑、？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_HSA01"),"True","lh/CRS_HSA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "RUK02A_CRS0033"
    $ current_voice = "voice/RUK02A_CRS0033.ogg"
    "红莉栖" "「……抱歉，没什么。比起这个，这边已经准备好了哦。你那边呢？」"
    $ stopvoc("RUK")
    play RUK "RUK02A_RUK0053"
    $ current_voice = "voice/RUK02A_RUK0053.ogg"
    "琉华" "「恩，恩！我也没问题的说！」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    hide screen phonebtn
    hide screen phoneSD1

    stop bgm 
    "我带上了保护头套正了正身子。"
    "又得承受那样的痛苦了，真的不太想那样啊……这样任性的话可不能说啊。"
    $ stopvoc("CRS")
    play CRS "RUK02A_CRS0034"
    $ current_voice = "voice/RUK02A_CRS0034.ogg"
    "红莉栖" "「那么开始了哦。」"
    $ stopvoc("RUK")
    play RUK "RUK02A_RUK0054"
    $ current_voice = "voice/RUK02A_RUK0054.ogg"
    "琉华" "「好、好的！」"
    play se "SGSE143"
    "牧濑按下了回车键。"
    "地板上的电子微波炉又开始回转起来，而不久之后房间里也开始飞舞起电火花。"
    window hide
    show houden 

    play se "SGSE035L" loop

    "视界又一次进入空白。"
    "然后——"
    $ stopvoc("RUK")
    play RUK "RUK02A_RUK0055"
    $ current_voice = "voice/RUK02A_RUK0055.ogg"
    "琉华" "「──！！」"
    hide houden 

    window hide

    stop se

    play se "SGSE067"


    play se "SGSE053L" loop

    stop se


    play se "SGSE013"

    hide screen phoneSD1
    window hide


    hide screen phonebtn
    hide houden 
    scene expression Solid("000000")  with fade
    call timeleap (fromtime=[8,18,19,40], totime=[8,16,19,40], fromday=[3])


    return




    stop se








    hide screen phonebtn
    scene expression Solid("000000")  with fade
    return
