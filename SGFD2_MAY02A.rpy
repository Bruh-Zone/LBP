label SGFD2_MAY02A:
    hide screen phonebtn
    scene expression Solid("000000")  with fade

    window hide


    $ loadBG(0,"BG56A")

    play bgm "BGM18"

    $ date="8/15"
    $ day = "SUN"
    show screen phonebtn
    show screen phoneSD1


    $ targetmailid = gc["ScriptMacros"]["RM_MAY_RECV_KAE01_01"]

    $ LR_RM_CHANCE=32
    call CHECK_RM_RECEIVE
    "今天是有外婆法事的重要日子。"
    call CHECK_RM_RECEIVE
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_COMIMA"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_COMIMA"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_COMIMA"])
    "但是，法事是在傍晚，我多想和枫酱还有吹雪酱，一起参加{color=#f00}夏Ｃｏｍｉ{/color}啊。"
    call CHECK_RM_RECEIVE
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_COSPLAY"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_COSPLAY"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_COSPLAY"])
    "枫酱，吹雪酱和真由喜一样都是参加着{color=#f00}Ｃｏｓｐｌａｙ{/color}这类社团呢。"
    call CHECK_RM_RECEIVE
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_COSTUME"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_COSTUME"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_COSTUME"])
    "真由喜总是在制作{color=#f00}ＣＯＳ{/color}用的服装，而这两位则是专门穿着这些服装。"
    call CHECK_RM_RECEIVE
    "像往常一样，今年的夏Ｃｏｍｉ现场也一定会非常热闹吧。"
    call CHECK_RM_RECEIVE
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_CAMEKO"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_CAMEKO"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_CAMEKO"])
    "枫酱和吹雪酱的ＣＯＳ，比起去年更受欢迎，一直被{color=#f00}相僧{/color}围着不放呢"
    call CHECK_RM_RECEIVE
    "看着那两人穿着我制作的ＣＯＳ服，被那么多的人给围住，沐浴着闪光灯的样子，作为制作者的我也感到很高兴。"
    call CHECK_RM_RECEIVE
    "但是，真由喜还是很在意冈伦的事。"
    call CHECK_RM_RECEIVE
    "现在无法集中精神在漫展上。"
    window hide



    $ loadBG(0,"BG38A")

    call CHECK_RM_RECEIVE
    "所以，比预想更早的离开漫展，推着装满战利品的小车向车站走去。"
    window hide
    $ loadBG(0,"IBG011A",png=True)

    call CHECK_RM_RECEIVE
    "手里拿着刚刚在花店买的一束百合花。"
    call CHECK_RM_RECEIVE
    "这是外婆的法事所必要的东西。"
    call CHECK_RM_RECEIVE
    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0000"
    $ current_voice = "voice/MAY02A_MAY0000.ogg"
    "真由理" "「非常漂亮，嗯～真香～。外婆会喜欢的吧ー」"
    call CHECK_RM_RECEIVE
    "一个人去祭拜时只需要一枝就够了，但法事时的花一定要华丽版本的。"
    call CHECK_RM_RECEIVE
    "花太贵了，光靠真由喜我的零花钱和打工的工资，这样华丽的花束是绝对买不起的。"
    call CHECK_RM_RECEIVE
    "有了爸爸妈妈的资助才能买得起。"
    call CHECK_RM_RECEIVE
    "等真由喜我长大后，得到最初的工资时，用自己的钱买下满手的百合花送给外婆该多好啊。但何时才能实现真由喜我这个小小的愿望呢。"
    window hide
    hide background-png  with dissolve
    call CHECK_RM_RECEIVE
    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0001"
    $ current_voice = "voice/MAY02A_MAY0001.ogg"
    "真由理" "「何时……能……」"
    call CHECK_RM_RECEIVE
    "高中毕业？大学毕业？"
    call CHECK_RM_RECEIVE
    "还是想些之后的事情吧。"
    call CHECK_RM_RECEIVE
    "看到了穿着西服快速出入于高级写字楼的白领，我试着想象一下穿着西服的自己。"
    call CHECK_RM_RECEIVE
    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0002"
    $ current_voice = "voice/MAY02A_MAY0002.ogg"
    "真由理" "「嗯、总觉得有些不太适合呢～」"
    call CHECK_RM_RECEIVE
    "不知何时变成大人的自己。"
    call CHECK_RM_RECEIVE
    "仍然无法想象。"
    call CHECK_RM_RECEIVE
    "虽然学校已经发了关于未来毕业后志愿的调查问卷，但是现在依然没有决定下来。"
    call CHECK_RM_RECEIVE
    "真由喜我会变成什么样的大人呢？"
    call CHECK_RM_RECEIVE
    "会从事什么职业呢？会变成ＯＬ吗？"
    call CHECK_RM_RECEIVE
    "能顺利地找到工作吗？"
    call CHECK_RM_RECEIVE
    "Ｌａｂ里的大家，都会去干些什么呢？"
    call CHECK_RM_RECEIVE
    "Ｌａｂ会怎么样呢？"
    call CHECK_RM_RECEIVE
    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0003"
    $ current_voice = "voice/MAY02A_MAY0003.ogg"
    "真由理" "「……真由喜我、多想永远和大家在一起啊～」"
    call CHECK_RM_RECEIVE
    "像现在这样的，几乎每天都在一起恐怕是不可能的了。"

    call CHECK_RM_RECEIVE
    "即使变成了大人，大家能再次聚在Ｌａｂ里，由冈伦来主持会议，这样该多好啊。"

    $ gd["RCVmailData"][gc["ScriptMacros"]["RM_MAY_RECV_KAE01_01"]]["late"]=True
    $ lml.append(gc["ScriptMacros"]["RM_MAY_RECV_KAE01_01"])

    window hide
    stop bgm 



    hide screen phonebtn
    hide screen phonebtn2
    show screen phone(interact=False)





    play bgm "BGM05"

    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0004"
    $ current_voice = "voice/MAY02A_MAY0004.ogg"
    "真由理" "「嘟嘟噜♪　是真由喜哦」"

    $ stopvoc("FEI")
    play FEI "MAY02A_FEI0000"
    $ current_voice = "voice/MAY02A_FEI0000.ogg"
    "菲利斯" "「真由喜、来帮帮忙喵～！」"

    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0005"
    $ current_voice = "voice/MAY02A_MAY0005.ogg"
    "真由理" "「菲利斯酱、怎么了？　店里很忙吗？」"

    $ stopvoc("FEI")
    play FEI "MAY02A_FEI0001"
    $ current_voice = "voice/MAY02A_FEI0001.ogg"
    "菲利斯" "「是这样的喵……今天有人因为急事而不能来打工了，大危机喵」"
    $ stopvoc("FEI")
    play FEI "MAY02A_FEI0001a"
    $ current_voice = "voice/MAY02A_FEI0001a.ogg"
    "菲利斯" "「午餐时间忙得恨不得连休息中的真由喜都要叫过来呢。即使知道真由喜忙于漫展的准备也想拜托你喵……」"

    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0006"
    $ current_voice = "voice/MAY02A_MAY0006.ogg"
    "真由理" "「这样啊。真由喜我没问题哦ー。正好。漫展的事情提早结束了。让我去帮忙吧？」"



    $ stopvoc("FEI")
    play FEI "MAY02A_FEI0002"
    $ current_voice = "voice/MAY02A_FEI0002.ogg"
    "菲利斯" "「嗯喵！　你能来真是帮大忙了喵！　要带的东西是、真由喜喵，好不容易有的休息喵、真的能拜托你吗喵？」"

    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0007"
    $ current_voice = "voice/MAY02A_MAY0007.ogg"
    "真由理" "「当然啦喵♪　今天要招待参加漫展的人们、明明知道会非常忙、却勉强请假的人是我才是。我帮点忙是应该的ー」"

    $ stopvoc("FEI")
    play FEI "MAY02A_FEI0003"
    $ current_voice = "voice/MAY02A_FEI0003.ogg"
    "菲利斯" "「真是帮大忙啦喵！　熬过午餐时间的话、就能好过一些喵！　稍微……拜托你一下可以吧？」"

    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0008"
    $ current_voice = "voice/MAY02A_MAY0008.ogg"
    "真由理" "「嗯♪　那么、我火速赶过来哦。３０分钟左右到」"

    $ stopvoc("FEI")
    play FEI "MAY02A_FEI0004"
    $ current_voice = "voice/MAY02A_FEI0004.ogg"
    "菲利斯" "「感激不尽喵♪」"

    window hide


    call hide_phone



    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0009"
    $ current_voice = "voice/MAY02A_MAY0009.ogg"
    "真由理" "「……现在、这种忙到连烦恼都无法顾及的状态对我而言说不定是件好事儿呢」"
    "不这样的话，就会光顾着考虑冈伦的事情呢。"
    "举起手振作了一下精神，我推着推车，赶去车站。"
    hide screen phoneSD1
    window hide

    stop bgm 



    $ loadBG(0,"BG36A")


    $ targetmailid = cml.setdefault("RM_MAY_SEND_KAE01","")

    $ LR_RM_CHANCE=1
    if phonemailring!= "":
        play se phonemailring
    if persistent.skipmail==False:
        $ renpy.choice_for_skipping()
    if targetmailid != "":
        $ RcvMail(targetmailid)
        $ targetmailid=""

    call CHECK_RM_RECEIVE



    play bgm "BGM06"
    show screen phoneSD1
    "急着赶向秋叶原的「ＭａｙＱｕｅｅｎ＋Ｎｙａ²咖啡厅」。"
    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0010"
    $ current_voice = "voice/MAY02A_MAY0010.ogg"
    "真由理" "「哇、好长的队伍……」"
    "从ＭａｙＱｕｅｅｎ＋Ｎｙａ²咖啡厅的入口开始，正排着几乎看不到队尾的长队。"
    "客人……不，能感受到主人们极大的热情呢。"
    "不用我们的热情去回应主人们的热情的话是不行的呢。"
    window hide


    $ loadBG(2,"BG_BLACK")



    hide screen phonebtn
    "从后门进入店里，在更衣室换好衣服，露出完美的笑脸，迈着轻快的步伐向大厅走去。"
    window hide

    $ loadBG(0,"BG28A1")

    show screen phonebtn
    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0011"
    $ current_voice = "voice/MAY02A_MAY0011.ogg"
    "真由理" "「嘟嘟噜♪　久等了♪ 真由喜・喵喵」"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_ALB02"),"True","lh/FEI_ALB02a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FEI")
    play FEI "MAY02A_FEI0005"
    $ current_voice = "voice/MAY02A_FEI0005.ogg"
    "菲利斯" "「喵！　真由喜、等你很久了！」"
    "菲利斯眼眶发红，一副感动至极的样子。"
    "像极了喉咙里发出呜咽声，随时准备一跃而起的猫咪。"
    "在打着温度很低的冷气的店里，菲利斯的身体却温暖又柔软，非常舒服。"
    "但是，一些主人的视线变得非常的浑浊起来，是错觉吗？"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_KIMASHI"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_KIMASHI"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_KIMASHI"])
    "什么嘛，「{color=#f00}百合系啊{/color}！」某处的主人这样喊着。"
    "我明明是叫真由喜又不是叫百合喜的说。"
    $ stopvoc("FEI")
    play FEI "MAY02A_FEI0006"
    $ current_voice = "voice/MAY02A_FEI0006.ogg"
    "菲利斯" "「真是帮大忙了喵、不愧是前世和菲利斯我缔结了义姐妹之契约的人喵！」"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_MARIA"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_MARIA"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_MARIA"])
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_SOEURS"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_SOEURS"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_SOEURS"])
    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0012"
    $ current_voice = "voice/MAY02A_MAY0012.ogg"
    "真由理" "「义姐妹？　嗯～、啊啊、{color=#f00}正如玛利亚所说{/color}的{color=#f00}Ｓｏｅｕｒ{/color}像那样喵？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_ALA02"),"True","lh/FEI_ALA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FEI")
    play FEI "MAY02A_FEI0007"
    $ current_voice = "voice/MAY02A_FEI0007.ogg"
    "菲利斯" "「是的喵！」"
    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0013"
    $ current_voice = "voice/MAY02A_MAY0013.ogg"
    "真由理" "「那、菲利斯、是我的姐姐大人嘛 ？」"



    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_ALA01"),"True","lh/FEI_ALA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)










    "一边演着正如玛利亚所说的那样的名场景，菲利斯一边帮我系好了女仆装的丝带、"
    $ stopvoc("FEI")
    play FEI "MAY02A_FEI0009"
    $ current_voice = "voice/MAY02A_FEI0009.ogg"
    "菲利斯" "「──姐姐我可是什么都能看穿的喵」"
    "菲利斯一边帮我把丝带重新系好，一边用余光盯着我。"
    "那大大的眼睛里一瞬间迸发出了光彩。"
    "真有一种被看穿一切的感觉，我迅速地避开了菲利斯的目光。"
    "菲利斯她，不光感觉很敏锐，而且脑袋也很聪明…… "

    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_ALC01"),"True","lh/FEI_ALC01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FEI")
    play FEI "MAY02A_FEI0010"
    $ current_voice = "voice/MAY02A_FEI0010.ogg"
    "菲利斯" "「嗯、真由喜、遇到了什么问题嘛？」"
    "唔，果 果然很敏锐呢。"
    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0014"
    $ current_voice = "voice/MAY02A_MAY0014.ogg"
    "真由理" "「嗯、嗯。没，没什么喵」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_ALC04"),"True","lh/FEI_ALC04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FEI")
    play FEI "MAY02A_FEI0011"
    $ current_voice = "voice/MAY02A_FEI0011.ogg"
    "菲利斯" "「真的喵？」"
    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0015"
    $ current_voice = "voice/MAY02A_MAY0015.ogg"
    "真由理" "「……嗯」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_ALB01"),"True","lh/FEI_ALB01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FEI")
    play FEI "MAY02A_FEI0012"
    $ current_voice = "voice/MAY02A_FEI0012.ogg"
    "菲利斯" "「有什么麻烦、随时可以找姐姐喵来商量喵」"
    "又一次，被菲利斯吓到了。"
    "果然，我不是菲利斯的对手啊。"
    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0016"
    $ current_voice = "voice/MAY02A_MAY0016.ogg"
    "真由理" "「谢谢」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_ALA01"),"True","lh/FEI_ALA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FEI")
    play FEI "MAY02A_FEI0013"
    $ current_voice = "voice/MAY02A_FEI0013.ogg"
    "菲利斯" "「总之、现在先把烦心事忘掉吧、充满干劲地、去为主人们服务喵！这样的话你也会元气满满呢！　主人们会把元气分给你喵♪　把元气吸过来喵♪」"
    "「好想被榨干啊！」主人们挥着拳头高呼道。"
    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0017"
    $ current_voice = "voice/MAY02A_MAY0017.ogg"
    "真由理" "「没、没错。我要加油了喵♪」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_ALA02"),"True","lh/FEI_ALA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FEI")
    play FEI "MAY02A_FEI0014"
    $ current_voice = "voice/MAY02A_FEI0014.ogg"
    "菲利斯" "「就是这样喵！」"
    "被菲利斯那威武的笑容所感染，我勉强挤出来的笑脸也变成了真正的笑容。"
    "不管是什么时候，菲利斯她总能变得充满活力并且非常开朗。"
    "连她周围的人也能变得精神起来。"
    "要是谁无精打采的话，马上就会被菲利斯察觉出来，接着被卷入菲利斯的世界里，从她那里得到活力。"
    "什么时候，真由喜我也能变得像菲利斯那样就好了。"
    hide screen phoneSD1
    window hide

    stop bgm 




    with fade
    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_ASC01"),"True","lh/FEI_ASC01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    show screen phoneSD1
    play bgm "FDBGM02"

    $ stopvoc("FEI")
    play FEI "MAY02A_FEI0015"
    $ current_voice = "voice/MAY02A_FEI0015.ogg"
    "菲利斯" "「真由喜、辛苦了喵。可以休息了喵。已经帮了大忙啦喵」"
    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0018"
    $ current_voice = "voice/MAY02A_MAY0018.ogg"
    "真由理" "「诶～？　午餐时间已经结束了吗？」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    "被菲利斯这么一说，猛然抬头看了看时间，已经过了一点半了。"
    "午餐菜谱的最后点餐时间已经过去了。"
    "到现在为止，明明一直觉得时间过得很慢，也就是眨眼间的功夫啊。"
    "午餐时间，会忙得晕头转向。"
    "嗯嗯，也的确够忙的了。"
    "实在是太忙了，途中连时间都已经搞不清楚了。"
    "好几次是在发呆的状态下为主人的蛋包饭上写字又或者是画画。"
    "我相信，现在的自己，要是拿到番茄酱的话一定会条件反射般地用它画画和写字。"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_ASC01"),"True","lh/FEI_ASC01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FEI")
    play FEI "MAY02A_FEI0016"
    $ current_voice = "voice/MAY02A_FEI0016.ogg"
    "菲利斯" "「午餐时间是最困难的时间段了喵。过了这段时间后接下来都没问题了喵。剩下的就交给菲利斯吧喵」"
    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0019"
    $ current_voice = "voice/MAY02A_MAY0019.ogg"
    "真由理" "「嗯、谢谢。在这个节骨眼儿上休息、真是对不起啦」"
    $ stopvoc("FEI")
    play FEI "MAY02A_FEI0017"
    $ current_voice = "voice/MAY02A_FEI0017.ogg"
    "菲利斯" "「嗯嗯、别介意喵。反正夏Ｃｏｍｉ的津贴也会好好分发的。」"
    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0020"
    $ current_voice = "voice/MAY02A_MAY0020.ogg"
    "真由理" "「是这样啊～」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_ASB01"),"True","lh/FEI_ASB01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FEI")
    play FEI "MAY02A_FEI0018"
    $ current_voice = "voice/MAY02A_FEI0018.ogg"
    "菲利斯" "「真由喜酱，精神恢复了吗？」"
    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0021"
    $ current_voice = "voice/MAY02A_MAY0021.ogg"
    "真由理" "「嗯，菲利斯，谢谢你。」"
    $ stopvoc("FEI")
    play FEI "MAY02A_FEI0019"
    $ current_voice = "voice/MAY02A_FEI0019.ogg"
    "菲利斯" "「烦恼的时候让自己忙个不停是最好的方法喵，之后呢，就是将烦恼的根源彻底地斩断♪」"
    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0022"
    $ current_voice = "voice/MAY02A_MAY0022.ogg"
    "真由理" "「把烦恼的根源斩断？」"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_GACHI"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_GACHI"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_GACHI"])
    $ stopvoc("FEI")
    play FEI "MAY02A_FEI0020"
    $ current_voice = "voice/MAY02A_FEI0020.ogg"
    "菲利斯" "「和成为烦恼原因的那个人、敞开胸怀{color=#f00}真心地{/color}把你所想的说出来就可以了喵」"
    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0023"
    $ current_voice = "voice/MAY02A_MAY0023.ogg"
    "真由理" "「毫无保留……」"
    $ stopvoc("FEI")
    play FEI "MAY02A_FEI0021"
    $ current_voice = "voice/MAY02A_FEI0021.ogg"
    "菲利斯" "「嗯嗯、能自己一个人解决的烦恼并不是那么多呢喵」"
    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0024"
    $ current_voice = "voice/MAY02A_MAY0024.ogg"
    "真由理" "「确实是这样，确实是这样没错，可能就是那样，现在除了想象以外其他什么都干不了……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_ASA01"),"True","lh/FEI_ASA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FEI")
    play FEI "MAY02A_FEI0022"
    $ current_voice = "voice/MAY02A_FEI0022.ogg"
    "菲利斯" "「就是就是！　想象终归是想象喵。正是这样、烦恼才会变长喵」"
    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0025"
    $ current_voice = "voice/MAY02A_MAY0025.ogg"
    "真由理" "「是这样啊……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_ASA02"),"True","lh/FEI_ASA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FEI")
    play FEI "MAY02A_FEI0023"
    $ current_voice = "voice/MAY02A_FEI0023.ogg"
    "菲利斯" "「那么、加油喵♪　辛苦了喵」"
    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0026"
    $ current_voice = "voice/MAY02A_MAY0026.ogg"
    "真由理" "「嗯、谢谢哦♪」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    "确实，最近和冈伦说话的时间减少了——"
    "像菲利斯说的那样，可能确实得找个机会试着和冈伦说一说才行啊。"
    "虽然只是一点点，但是好像找到了解决烦恼的突破口。"
    hide screen phoneSD1
    window hide



    $ loadBG(0,"BG18A1")

    show screen phoneSD1
    "在更衣室里换好衣服，边想着得赶在法事开始前把行李放在箱子里，边向Ｌａｂ走去。"
    "如果刚好能碰到冈伦的话就好了呢，我这么想到。"
    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0027"
    $ current_voice = "voice/MAY02A_MAY0027.ogg"
    "真由理" "「……冈伦他，应该在Ｌａｂ的吧？　如果能遇到就好了」"
    "虽然知道和冈伦好好谈谈会比较好，但我发现自己有些畏缩不前。"
    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0028"
    $ current_voice = "voice/MAY02A_MAY0028.ogg"
    "真由理" "「唔，不对。不是能见到就好了。是必须要见一下呢」"
    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0029"
    $ current_voice = "voice/MAY02A_MAY0029.ogg"
    "真由理" "「果然和菲利斯说的一样，不好好和冈伦谈一下的话是不行的……」"

    stop bgm 
    window hide
    hide screen phonebtn
    hide screen phonebtn2
    show screen phone(interact=False)
    "下定了决心之后，我停下脚步，取出了手机。"
    "不能这么期待偶然的相遇下去，一定要好好地找一个时间来和冈伦谈谈。"
    "这么想了以后，马上付诸了行动。"
    "试着给冈伦打了个电话。"


    "不知为何突然紧张了起来。"
    "真由喜是冈伦的人质的理由。"
    "想要知道与害怕知道的心情错综复杂地交织在一起。"
    "——没打通。"
    "虽然有些遗憾，同时也舒了一口气。"

    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0030"
    $ current_voice = "voice/MAY02A_MAY0030.ogg"
    "真由理" "「……那就发邮件试试吧」"
    window hide
    $ targetmailid = gc["ScriptMacros"]["FM_MAY02A_EDIT_OKA01_00"]

    $ targetmailid = gc["ScriptMacros"]["FM_MAY02A_EDIT_OKA01_60"]
    call send_mail (id=[27,28,29,30,31,32,33,34])


    "就这么把自己的不安一五一十地抛给别人什么的，想想都可怕。"
    "敲打着邮件的拇指颤抖着。"
    window hide
    $ targetmailid = gc["ScriptMacros"]["FM_MAY02A_SEND_OKA01"]


    "当我打完最后一个字的时候，我深深地吸了口气。"


    "将手指放到了发送键上。"
    "但是，不能很好地按下去。"
    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0031"
    $ current_voice = "voice/MAY02A_MAY0031.ogg"
    "真由理" "「如果不知道冈伦烦恼的理由的话，真由喜就没有办法为冈伦做点什么……」"
    window hide


    "鼓起勇气，我终于按下了发送键。"
    window hide


    call hide_phone

    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0032"
    $ current_voice = "voice/MAY02A_MAY0032.ogg"
    "真由理" "「……哈～、发出去了……」"
    "冈伦会回信吧？"
    "既希望他能回信，又希望他不要回复我……果然心情十分复杂。"
    "但是，比起就这样将这个谜团置之不理，固步自封下去总是要好一些的吧。"
    window hide


    $ loadBG(2,"IBGX048")



    hide screen phonebtn
    play bgm "BGM05"
    "关上手机，抬起头，我向前迈出脚步。"
    "感觉发了邮件之后，心情稍微变好了一些。"
    hide screen phoneSD1
    window hide



    $ loadBG(0,"BG05A1")

    show screen phonebtn
    show screen phoneSD1
    "直到到了Ｌａｂ，也没有收到冈伦的回复。"
    "也许还没有读邮件。"
    "冈伦不是那种喜欢用邮件交谈的人。"
    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0033"
    $ current_voice = "voice/MAY02A_MAY0033.ogg"
    "真由理" "「冈伦他，现在，在哪里干什么呢？」"
    window hide



    $ loadBG(0,"BG02A1")
    play se "SGSE024"

    "虽然冈伦不在Ｌａｂ，但桶子君在。"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_THIN_BOOK"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_THIN_BOOK"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_THIN_BOOK"])
    "缩在沙发里的桶子君气息慌乱，用炽热的眼神注视着小山一样的{color=#f00}小薄本{/color}。"
    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0034"
    $ current_voice = "voice/MAY02A_MAY0034.ogg"
    "真由理" "「咦，是桶子君啊，嘟嘟噜♪」"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA01"),"True","lh/DAR_ASA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_OTSU"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_OTSU"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_OTSU"])
    $ stopvoc("DAR")
    play DAR "MAY02A_DAR0000"
    $ current_voice = "voice/MAY02A_DAR0000.ogg"
    "至" "「哦哦，真由氏！　{color=#f00}乙{/color}～ 」"
    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0035"
    $ current_voice = "voice/MAY02A_MAY0035.ogg"
    "真由理" "「还以为你在夏Ｃｏｍｉ呢。已经回来了啊？」"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_JOKO"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_JOKO"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_JOKO"])
    $ stopvoc("DAR")
    play DAR "MAY02A_DAR0001"
    $ current_voice = "voice/MAY02A_DAR0001.ogg"
    "至" "「像我这样的壮士，真正的战斗从早上就开始了，{color=#f00}常考{/color}。想要的东西，大概过了中午就全部能入手了。」"
    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0036"
    $ current_voice = "voice/MAY02A_MAY0036.ogg"
    "真由理" "「不愧是桶子君，真·御宅族就是不一样呢」"
    $ stopvoc("DAR")
    play DAR "MAY02A_DAR0002"
    $ current_voice = "voice/MAY02A_DAR0002.ogg"
    "至" "「不要叫我真·御宅啦。难得的机会，真由氏要和我一起看看战利品吗？现在我正在品尝这丰硕的战果呢。这些都是我老婆哦」"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_HADAIRO"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_HADAIRO"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_HADAIRO"])
    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0037"
    $ current_voice = "voice/MAY02A_MAY0037.ogg"
    "真由理" "「诶诶？但是，桶子君和真由喜喜欢的本子类型不太一样呢。甲贺唯的本子的话倒是想看一下。桶子君喜欢的一般是那种{color=#f00}卖肉系{/color}不是吗？」"
    $ stopvoc("DAR")
    play DAR "MAY02A_DAR0003"
    $ current_voice = "voice/MAY02A_DAR0003.ogg"
    "至" "「小薄本的话，果然卖肉的比较多才对嘛，常考」"
    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0038"
    $ current_voice = "voice/MAY02A_MAY0038.ogg"
    "真由理" "「呐，桶子君，冈伦和红莉栖酱呢？今天他们没有来Ｌａｂ吗？」"



    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA04"),"True","lh/DAR_ASA04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)







    $ stopvoc("DAR")
    play DAR "MAY02A_DAR0004"
    $ current_voice = "voice/MAY02A_DAR0004.ogg"
    "至" "「唔！来了！真由氏的天然呆！就是这点超级赞的啊！说起来，冈伦和牧濑氏的话，今天没有看到过哦？」"


    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0039"
    $ current_voice = "voice/MAY02A_MAY0039.ogg"
    "真由理" "「……这样啊」"
    $ stopvoc("DAR")
    play DAR "MAY02A_DAR0005"
    $ current_voice = "voice/MAY02A_DAR0005.ogg"
    "至" "「是找他们有事情吗？」"
    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0040"
    $ current_voice = "voice/MAY02A_MAY0040.ogg"
    "真由理" "「不是，没有到“事情”那种程度……」"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_REAJU"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_REAJU"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_REAJU"])
    $ stopvoc("DAR")
    play DAR "MAY02A_DAR0006"
    $ current_voice = "voice/MAY02A_DAR0006.ogg"
    "至" "「肯定，现在两个人，又在一起过{color=#f00}现充{/color}的时间吧？」"
    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0041"
    $ current_voice = "voice/MAY02A_MAY0041.ogg"
    "真由理" "「……嗯嗯，那样也……说不定呢」"
    "其实，真由喜有时候也会想「说不定，是那样的哦？」，所以感觉不由得有些同意桶子君的观点。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA03"),"True","lh/DAR_ASA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "MAY02A_DAR0007"
    $ current_voice = "voice/MAY02A_DAR0007.ogg"
    "至" "「不对，真由氏，刚才只是吐槽而已啦。牧濑氏和那种重度厨二病的冈伦一起现充什么的，不可能的吧？」"
    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0042"
    $ current_voice = "voice/MAY02A_MAY0042.ogg"
    "真由理" "「啊哈哈，也许吧～？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA01"),"True","lh/DAR_ASA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "MAY02A_DAR0008"
    $ current_voice = "voice/MAY02A_DAR0008.ogg"
    "至" "「嗯嗯！」"
    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0043"
    $ current_voice = "voice/MAY02A_MAY0043.ogg"
    "真由理" "「……桶子君，谢谢～」"
    $ stopvoc("DAR")
    play DAR "MAY02A_DAR0009"
    $ current_voice = "voice/MAY02A_DAR0009.ogg"
    "至" "「嗯？　谢什么？」"
    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0044"
    $ current_voice = "voice/MAY02A_MAY0044.ogg"
    "真由理" "「嗯，没什么啦。说起来今天真是热啊。在夏Ｃｏｍｉ会场感觉都要热得汗流浃背了呢——」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA04"),"True","lh/DAR_ASA04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "MAY02A_DAR0010"
    $ current_voice = "voice/MAY02A_DAR0010.ogg"
    "至" "「……汁流……浃背……」"
    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0045"
    $ current_voice = "voice/MAY02A_MAY0045.ogg"
    "真由理" "「汁流？　不是哦，汗流浃背哦ー？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA02"),"True","lh/DAR_ASA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "MAY02A_DAR0011"
    $ current_voice = "voice/MAY02A_DAR0011.ogg"
    "至" "「……不对，错了，不如说正好。真由氏，刚才的『好热，都要汁流浃背了』麻烦再说一遍……」"
    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0046"
    $ current_voice = "voice/MAY02A_MAY0046.ogg"
    "真由理" "「诶诶～？　好热啊？　汁流浃背了？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA05"),"True","lh/DAR_ASA05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    $ stopvoc("DAR")
    play DAR "MAY02A_DAR0012"
    $ current_voice = "voice/MAY02A_DAR0012.ogg"
    "至" "「流下的汁，万分感激地收下了！」"
    "桶子君不知为何兴奋起来了。"
    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0047"
    $ current_voice = "voice/MAY02A_MAY0047.ogg"
    "真由理" "「那，真由喜要走了呢」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASB04"),"True","lh/DAR_ASB04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    $ stopvoc("DAR")
    play DAR "MAY02A_DAR0013"
    $ current_voice = "voice/MAY02A_DAR0013.ogg"
    "至" "「诶？　现在？」"
    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0048"
    $ current_voice = "voice/MAY02A_MAY0048.ogg"
    "真由理" "「嗯，本来来Ｌａｂ只是为了放一下行李而已，接下来要去法事啦」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA01"),"True","lh/DAR_ASA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "MAY02A_DAR0014"
    $ current_voice = "voice/MAY02A_DAR0014.ogg"
    "至" "「啊啊，是这样的。那么，小心点哦。但在那之前，刚才的台词，能不能再说一遍啊？」"
    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0049"
    $ current_voice = "voice/MAY02A_MAY0049.ogg"
    "真由理" "「诶～？难道刚才的，是Ｈ的台词吗」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA04"),"True","lh/DAR_ASA04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "MAY02A_DAR0015"
    $ current_voice = "voice/MAY02A_DAR0015.ogg"
    "至" "「不是，那个是……那个，咳咳……」"
    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0050"
    $ current_voice = "voice/MAY02A_MAY0050.ogg"
    "真由理" "「冈伦说过，如果桶子君让你再说什么Ｈ的台词的话，就告诉他『你老婆们的命已经没有了』」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA06"),"True","lh/DAR_ASA06a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "MAY02A_DAR0016"
    $ current_voice = "voice/MAY02A_DAR0016.ogg"
    "至" "「咕呃！？　冈，冈伦这家伙，打算对我的老婆们做什么！？」"
    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0051"
    $ current_voice = "voice/MAY02A_MAY0051.ogg"
    "真由理" "「谁知道呢？　真由喜也不是很明白就是了……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA05"),"True","lh/DAR_ASA05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "MAY02A_DAR0017"
    $ current_voice = "voice/MAY02A_DAR0017.ogg"
    "至" "「呜呜……那，下次要做的话就要更加不动声色地进行了！」"
    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0052"
    $ current_voice = "voice/MAY02A_MAY0052.ogg"
    "真由理" "「所以说不是那个方面的问题啊」"
    window hide

    stop bgm 


    $ loadBG(2,"BG01A")



    "一边苦笑着，我一边走出了Ｌａｂ，然后停下了脚步。"
    window hide


    $ loadBG(2,"BG02A1")



    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0053"
    $ current_voice = "voice/MAY02A_MAY0053.ogg"
    "真由理" "「……啊、哦、说起来。桶子君」"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA01"),"True","lh/DAR_ASA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "MAY02A_DAR0018"
    $ current_voice = "voice/MAY02A_DAR0018.ogg"
    "至" "「──嗯？」"
    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0054"
    $ current_voice = "voice/MAY02A_MAY0054.ogg"
    "真由理" "「那个……有一个请求，能听我说吗？」"
    play bgm "FD2BGM11"
    "以后万一要使用那个计划，我觉得还是现在先做一下准备比较好。"
    $ stopvoc("DAR")
    play DAR "MAY02A_DAR0019"
    $ current_voice = "voice/MAY02A_DAR0019.ogg"
    "至" "「向我的请求？　那是什么？」"
    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0055"
    $ current_voice = "voice/MAY02A_MAY0055.ogg"
    "真由理" "「……唔，那个……紧急时刻，希望你能帮帮我……」"
    $ stopvoc("DAR")
    play DAR "MAY02A_DAR0020"
    $ current_voice = "voice/MAY02A_DAR0020.ogg"
    "至" "「帮你？」"
    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0056"
    $ current_voice = "voice/MAY02A_MAY0056.ogg"
    "真由理" "「嗯……要向大家保密，可以拜托你吗？」"
    $ stopvoc("DAR")
    play DAR "MAY02A_DAR0021"
    $ current_voice = "voice/MAY02A_DAR0021.ogg"
    "至" "「……大家，也包括冈伦吗？」"
    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0057"
    $ current_voice = "voice/MAY02A_MAY0057.ogg"
    "真由理" "「嗯……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA02"),"True","lh/DAR_ASA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "MAY02A_DAR0022"
    $ current_voice = "voice/MAY02A_DAR0022.ogg"
    "至" "「好像有什么原因在里面吧」"
    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0058"
    $ current_voice = "voice/MAY02A_MAY0058.ogg"
    "真由理" "「那个……理由的话，如果能不说的话我会很高兴的。但是，是很重要的事情呢」"
    $ stopvoc("DAR")
    play DAR "MAY02A_DAR0023"
    $ current_voice = "voice/MAY02A_DAR0023.ogg"
    "至" "「…………」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA01"),"True","lh/DAR_ASA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "MAY02A_DAR0024"
    $ current_voice = "voice/MAY02A_DAR0024.ogg"
    "至" "「……ＯＫ、明白了。那就是我和真由氏之间的约定了」"
    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0059"
    $ current_voice = "voice/MAY02A_MAY0059.ogg"
    "真由理" "「十分感谢，桶子君」"
    $ stopvoc("DAR")
    play DAR "MAY02A_DAR0025"
    $ current_voice = "voice/MAY02A_DAR0025.ogg"
    "至" "「作为回礼的话，刚才的台词能让我录下来吗？」"
    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0060"
    $ current_voice = "voice/MAY02A_MAY0060.ogg"
    "真由理" "「真是的，桶子君，Ｈ可是禁止事项哦？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA02"),"True","lh/DAR_ASA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "MAY02A_DAR0026"
    $ current_voice = "voice/MAY02A_DAR0026.ogg"
    "至" "「关于这点请务必通融！」"
    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0061"
    $ current_voice = "voice/MAY02A_MAY0061.ogg"
    "真由理" "「但是，回礼是必须的呢。除了Ｈ以外的都可以哦」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA01"),"True","lh/DAR_ASA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "MAY02A_DAR0027"
    $ current_voice = "voice/MAY02A_DAR0027.ogg"
    "至" "「明明就算是Ｈ方面的也有很多可以做的呢。嘛，就不开玩笑了，真由氏的忙我是一定会帮的，回礼什么的就不需要了」"
    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0062"
    $ current_voice = "voice/MAY02A_MAY0062.ogg"
    "真由理" "「诶嘿嘿，这样说的话真由喜很开心啊」"
    $ stopvoc("DAR")
    play DAR "MAY02A_DAR0028"
    $ current_voice = "voice/MAY02A_DAR0028.ogg"
    "至" "「都是Ｌａｂｍｅｍ嘛。自然两肋插刀鼎力相助啦，常考」"
    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0063"
    $ current_voice = "voice/MAY02A_MAY0063.ogg"
    "真由理" "「果然，还是Ｌａｂｍｅｍ靠得住呢～♪　下次，真由喜要把炸鸡块Ｎｏ．１分给桶子君吃。」"
    $ stopvoc("DAR")
    play DAR "MAY02A_DAR0029"
    $ current_voice = "voice/MAY02A_DAR0029.ogg"
    "至" "「嗯、是那种说着“啊”然后放到我的嘴里来的吗？」"
    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0064"
    $ current_voice = "voice/MAY02A_MAY0064.ogg"
    "真由理" "「嗯？　可以哦？」"



    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASB04"),"True","lh/DAR_ASB04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)







    $ stopvoc("DAR")
    play DAR "MAY02A_DAR0030"
    $ current_voice = "voice/MAY02A_DAR0030.ogg"
    "至" "「哦哦哦哦哦哦！那是何等的萌啊！不讲道理，真是太不讲道理了！我明明已经有了二次元的老婆们了……还有，菲利斯碳也算在内的话……」"





    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA05"),"True","lh/DAR_ASA05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)







    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_HAREM"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_HAREM"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_HAREM"])
    $ stopvoc("DAR")
    play DAR "MAY02A_DAR0030a"
    $ current_voice = "voice/MAY02A_DAR0030a.ogg"
    "至" "「不对，但是，难道说……还存在{color=#f00}后宫路线{/color}……」"


    "桶子君好像在说着什么。"
    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0065"
    $ current_voice = "voice/MAY02A_MAY0065.ogg"
    "真由理" "「那么，桶子君，再见咯。嘟嘟噜♪」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASB01"),"True","lh/DAR_ASB01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "MAY02A_DAR0031"
    $ current_voice = "voice/MAY02A_DAR0031.ogg"
    "至" "「再见了～」"
    window hide


    $ loadBG(2,"BG01A")



    "虽然没见到冈伦，但这样一来到紧要关头也没有关系了。"
    "说真的，真希望那种紧要关头不要到来——"
    hide screen phoneSD1
    window hide

    stop bgm 



    $ loadBG(0,"BG13A1")


    show screen phoneSD1

    $ targetmailid = gc["ScriptMacros"]["FM_MAY02A_RECV_MMM01"]
    if phonemailring!= "":
        play se phonemailring
    if persistent.skipmail==False:
        $ renpy.choice_for_skipping()
    if targetmailid != "":
        $ RcvMail(targetmailid)
        $ targetmailid=""

    hide screen phonebtn
    "走出车站附近的时候，收到了邮件。"



    window hide
    hide screen phonebtn
    hide screen phonebtn2
    call read_last_mail







    "是妈妈发过来的。"
    "肯定又是担心我犯迷糊了吧。真由喜，明明是肯定不会忘记的。"
    "从夏Ｃｏｍｉ回来之后，经过精挑细选之后买下的花束。"
    "外婆最喜欢的白色百合。"
    window hide
    call hide_phone

    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0066"
    $ current_voice = "voice/MAY02A_MAY0066.ogg"
    "真由理" "「……咦、阿勒？」"
    play bgm "BGM23"
    "看看右手，再看了看左手，又看了下背包。"
    "哪儿也没有。"
    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0067"
    $ current_voice = "voice/MAY02A_MAY0067.ogg"
    "真由理" "「阿勒～？」"
    "歪着头，仔细思考了一下。"
    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0068"
    $ current_voice = "voice/MAY02A_MAY0068.ogg"
    "真由理" "「唔，怎么办啊……给外婆的花束，不知道忘在哪里了……是落在哪里了吧……明明是这么重要的东西……」"
    "考虑一下可能性的话……Ｌａｂ呀，或者ＭａｙＱｕｅｅｎ＋Ｎｙａ²之类的。"
    window hide
    hide screen phonebtn
    hide screen phonebtn2
    show screen phone(interact=False)

    "首先给桶子君打个电话吧。"
    window hide





    $ stopvoc("DAR")
    play DAR "MAY02A_DAR0032"
    $ current_voice = "voice/MAY02A_DAR0032.ogg"
    "至" "「喂，你好啊」"

    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0069"
    $ current_voice = "voice/MAY02A_MAY0069.ogg"
    "真由理" "「啊，桶子君，那个呢，想确认一下，真由喜有忘了花束在Ｌａｂ里吗？」"

    $ stopvoc("DAR")
    play DAR "MAY02A_DAR0033"
    $ current_voice = "voice/MAY02A_DAR0033.ogg"
    "至" "「花束？　说起来真由喜刚才来的时候，并没有带着花束呢」"

    "没有带着……"
    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0070"
    $ current_voice = "voice/MAY02A_MAY0070.ogg"
    "真由理" "「那看起来是不小心落在哪里了吧……」"

    $ stopvoc("DAR")
    play DAR "MAY02A_DAR0034"
    $ current_voice = "voice/MAY02A_DAR0034.ogg"
    "至" "「那样显眼的东西都能落下，看来真由氏的天然呆果然是纯正的天然呆啊～」"

    "呜呜，不愧是妈妈，对于真由喜的本性真是一清二楚。"
    "有些灰心地垂下肩低声说道。"
    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0071"
    $ current_voice = "voice/MAY02A_MAY0071.ogg"
    "真由理" "「呜呜呜……看来不去找是不行的了……不在Ｌａｂ的话，那看来就在ＭａｙＱｕｅｅｎ＋Ｎｙａ²了」"

    $ stopvoc("DAR")
    play DAR "MAY02A_DAR0035"
    $ current_voice = "voice/MAY02A_DAR0035.ogg"
    "至" "「要我也一起去找吗？」"

    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0072"
    $ current_voice = "voice/MAY02A_MAY0072.ogg"
    "真由理" "「嗯，不用了」"

    $ stopvoc("DAR")
    play DAR "MAY02A_DAR0036"
    $ current_voice = "voice/MAY02A_DAR0036.ogg"
    "至" "「这样啊。那如果怎么都找不到的话务必再次联系我哦」"

    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0073"
    $ current_voice = "voice/MAY02A_MAY0073.ogg"
    "真由理" "「明白了。那就这样～」"


    "那么，如果是那样的话就和菲利斯联系一下吧。"
    window hide
    $ targetmailid = gc["ScriptMacros"]["FM_MAY02A_EDIT_FEI01_00"]

    $ targetmailid = gc["ScriptMacros"]["FM_MAY02A_SEND_FEI01"]






    call send_mail (id=[36,37,38,39])
    call hide_phone


    stop bgm 
    "应该就没问题了。"
    "那么，就回ＭａｙＱｕｅｅｎ＋Ｎｙａ²吧。"
    window hide



    hide screen phonebtn
    hide screen phonebtn2
    show screen phone(interact=False)

    "这么想着，大概１分不到之后菲利斯就打了电话过来。"
    window hide




    play bgm "BGM05"

    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0074"
    $ current_voice = "voice/MAY02A_MAY0074.ogg"
    "真由理" "「你好，我是真由喜」"

    $ stopvoc("FEI")
    play FEI "MAY02A_FEI0024"
    $ current_voice = "voice/MAY02A_FEI0024.ogg"
    "菲利斯" "「真由喜，邮件我已经看了喵！你的花束，放在更衣室的保险柜上面了喵！」"

    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0075"
    $ current_voice = "voice/MAY02A_MAY0075.ogg"
    "真由理" "「真的吗！？　菲利斯，谢谢你了！是很重要的花束哦。帮大忙了！」"



    $ stopvoc("FEI")
    play FEI "MAY02A_FEI0025"
    $ current_voice = "voice/MAY02A_FEI0025.ogg"
    "菲利斯" "「我们之间还发什么邮件啊。直接打电话过来不就好了」"

    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0076"
    $ current_voice = "voice/MAY02A_MAY0076.ogg"
    "真由理" "「但是，要是你很忙的话感觉不太好吧……」"



    $ stopvoc("FEI")
    play FEI "MAY02A_FEI0026"
    $ current_voice = "voice/MAY02A_FEI0026.ogg"
    "菲利斯" "「完全不用担心这边的问题啦。主人们已经用完餐差不多都回家了，所以空得很。这都要多亏了中午真由喜的帮忙了哦」"

    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0077"
    $ current_voice = "voice/MAY02A_MAY0077.ogg"
    "真由理" "「诶嘿嘿，那么我就过来取了啊」"



    $ stopvoc("FEI")
    play FEI "MAY02A_FEI0027"
    $ current_voice = "voice/MAY02A_FEI0027.ogg"
    "菲利斯" "「我会等你来的喵」"

    window hide


    call hide_phone

    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0078"
    $ current_voice = "voice/MAY02A_MAY0078.ogg"
    "真由理" "「哈，太好了……外婆的花束，找到了……」"
    play se "SGSE031"
    "舒了一口气的同时，肚子“咕——”地叫了起来。"
    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0079"
    $ current_voice = "voice/MAY02A_MAY0079.ogg"
    "真由理" "「说起来，一直忙这忙那的，午饭都还没吃呢……」"
    "一旦注意到了肚子饿了这一点，就感觉肚子开始不停地抗议了。"
    "肚子的抗议对于真由喜来说可是一个大问题。"
    "顺便去一下便利店吧。"
    window hide
    stop bgm 



    $ loadBG(0,"BG16A1")
    play se "SGSE007L" loop


    "买了吃的以后，又回到了路上。"
    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0080"
    $ current_voice = "voice/MAY02A_MAY0080.ogg"
    "真由理" "「嗯嗯～♪　好吃♪」"
    "将几个『蘑菇山』一次性放进嘴里，然后感受着甘甜的美味在口中慢慢扩散开去。"
    "其实应该吃『炸鸡炸鸡君』的，但是很遗憾的是秋叶原附近并没有卖这种食物的便利店。"
    "外婆的花也找到了，肚子的问题也解决了，终于我有了余裕来看看周围的环境。"
    "虽然平时中央大街的人就很多，但感觉今天更甚一筹。"
    "应该有很多人是从夏Ｃｏｍｉ回来的。"
    "手里提着印着萌图的纸袋，个个脸上都是一副满足的表情。"
    "感觉就是充分燃烧的战士的表情。"
    "是受到了氛围的感染了吧，真由喜也感觉有点幸福了起来。"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_GOMI"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_GOMI"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_GOMI"])
    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0081"
    $ current_voice = "voice/MAY02A_MAY0081.ogg"
    "真由理" "「如果是冈伦的话，一定会说什么{color=#f00}看啊，人就像垃圾一样！{/color}　之类的话吧。还会一边呼哈哈哈哈这么大笑着」"
    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0082"
    $ current_voice = "voice/MAY02A_MAY0082.ogg"
    "真由理" "「但是他还是没有联系我啊～」"
    window hide



    hide screen phonebtn
    hide screen phonebtn2
    show screen phone(interact=False)



    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0083"
    $ current_voice = "voice/MAY02A_MAY0083.ogg"
    "真由理" "「喂喂，是妈妈啊？」"

    $ stopvoc("X03")
    play KUR "MAY02A_X030000"
    $ current_voice = "voice/MAY02A_X030000.ogg"
    "真由理妈妈" "「真由理，做法事的花没事么？」"

    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0084"
    $ current_voice = "voice/MAY02A_MAY0084.ogg"
    "真由理" "「……没问题的哦？」"

    $ stopvoc("X03")
    play KUR "MAY02A_X030001"
    $ current_voice = "voice/MAY02A_X030001.ogg"
    "真由理妈妈" "「刚刚，犹豫了一下啊，真的没问题吗？」"

    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0085"
    $ current_voice = "voice/MAY02A_MAY0085.ogg"
    "真由理" "「说了没问题了啊。只是，有点东西落下了。诶嘿嘿，现在就去取来啦」"

    $ stopvoc("X03")
    play KUR "MAY02A_X030002"
    $ current_voice = "voice/MAY02A_X030002.ogg"
    "真由理妈妈" "「……忘记的东西，是花束吧。真是的，真由理总是这样呢。法事的时间，赶得上吗？」"

    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0086"
    $ current_voice = "voice/MAY02A_MAY0086.ogg"
    "真由理" "「没关系，妈妈先去也可以。真由喜之后再和你们会合」"

    $ stopvoc("X03")
    play KUR "MAY02A_X030003"
    $ current_voice = "voice/MAY02A_X030003.ogg"
    "真由理妈妈" "「看起来要迟到一些呢……大概几分钟？」"

    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0087"
    $ current_voice = "voice/MAY02A_MAY0087.ogg"
    "真由理" "「嗯，大概要１５分钟的样子？」"

    $ stopvoc("X03")
    play KUR "MAY02A_X030004"
    $ current_voice = "voice/MAY02A_X030004.ogg"
    "真由理妈妈" "「明白了，那么请小心些哦。可不要遇到坏人了」"

    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0088"
    $ current_voice = "voice/MAY02A_MAY0088.ogg"
    "真由理" "「嗯，那就这样」"
    window hide


    $ stopvoc("CRS")
    play CRS "MAY02A_CRS0000"
    $ current_voice = "voice/MAY02A_CRS0000.ogg"
    "？？？" "「……由理！」"
    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0089"
    $ current_voice = "voice/MAY02A_MAY0089.ogg"
    "真由理" "「嗯？」"
    window hide
    call hide_phone
    "感觉好像有谁在叫我的名字，我停了下来。"
    "环顾四周。"
    "但是，因为人太多了，没能确认是谁在叫我。"
    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0090"
    $ current_voice = "voice/MAY02A_MAY0090.ogg"
    "真由理" "「嗯，是我的错觉吗？」"
    "于是回过神来，继续向前。"
    $ stopvoc("CRS")
    play CRS "MAY02A_CRS0001"
    $ current_voice = "voice/MAY02A_CRS0001.ogg"
    "红莉栖" "「真由理，这边。呐，听不到吗？」"
    "这次清楚地听到了。"
    "不是错觉。"
    "是红莉栖酱的声音——"
    "听清楚了之后，用力地踮起脚朝着那个方向看去。"
    "红莉栖酱，怎么了吗？"
    "总感觉刚才的声音有些声嘶力竭。"
    "在人群中好不容易找到了红莉栖酱的褐色头发之后，我朝着那边大声喊道。"
    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0091"
    $ current_voice = "voice/MAY02A_MAY0091.ogg"
    "真由理" "「是红莉栖酱啊。喂！」"
    "朝着红莉栖酱那边挥了挥手之后，有一瞬间感到她仿佛要哭出来了，然后便也用力地朝我挥着手。"
    "我竭尽全力分开人群，朝着红莉栖酱的方向赶去。"
    "红莉栖酱好像不知为何放下心来，站在原地不动了。"

    stop se
    hide screen phoneSD1
    window hide
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_MAY001A"]]["Check"]=True


    $ loadBG(2,"EV_MAY001A")



    hide screen phonebtn
    play bgm "FD2BGM05"

    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0092"
    $ current_voice = "voice/MAY02A_MAY0092.ogg"
    "真由理" "「红莉栖酱，抱歉了呢。人太多，所以开始没注意到」"
    $ stopvoc("CRS")
    play CRS "MAY02A_CRS0002"
    $ current_voice = "voice/MAY02A_CRS0002.ogg"
    "红莉栖" "「……里哦」"
    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0093"
    $ current_voice = "voice/MAY02A_MAY0093.ogg"
    "真由理" "「诶？」"
    $ stopvoc("CRS")
    play CRS "MAY02A_CRS0003"
    $ current_voice = "voice/MAY02A_CRS0003.ogg"
    "红莉栖" "「我，就在这里哦」"
    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0094"
    $ current_voice = "voice/MAY02A_MAY0094.ogg"
    "真由理" "「红莉栖酱？」"
    $ stopvoc("CRS")
    play CRS "MAY02A_CRS0004"
    $ current_voice = "voice/MAY02A_CRS0004.ogg"
    "红莉栖" "「…………」"
    "红莉栖酱的身体微微颤动着。"
    "不像平时威风凛凛的红莉栖酱。"
    "肯定有什么问题。"
    "我抓起红莉栖酱的手，注视着她问道。"
    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0095"
    $ current_voice = "voice/MAY02A_MAY0095.ogg"
    "真由理" "「红莉栖酱，没关系吗？　发生了什么？」"
    $ stopvoc("CRS")
    play CRS "MAY02A_CRS0005"
    $ current_voice = "voice/MAY02A_CRS0005.ogg"
    "红莉栖" "「……真由理，呜呜……什么也……没有」"
    "虽然一瞬间露出呆然的表情，但是红莉栖酱很快就取回了平时的稳重。"
    "但是——果然有什么问题。"
    "她的表情有点奇怪。"
    "是为了什么才出声叫我的呢。"
    "在我疑惑的时候，红莉栖酱反握住我的手，向我问道。"
    $ stopvoc("CRS")
    play CRS "MAY02A_CRS0006"
    $ current_voice = "voice/MAY02A_CRS0006.ogg"
    "红莉栖" "「我没……问题……真由理那边才是，没问题吧？身体还好吧？没有不舒服吧？」"
    "太过于用力而让我吓了一跳。"
    "冰冷的指尖颤抖着。"
    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0096"
    $ current_voice = "voice/MAY02A_MAY0096.ogg"
    "真由理" "「红莉栖酱……真由喜一直都很精神哦。现在超有活力的说」"
    $ stopvoc("CRS")
    play CRS "MAY02A_CRS0007"
    $ current_voice = "voice/MAY02A_CRS0007.ogg"
    "红莉栖" "「那样啊……太好了」"
    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0097"
    $ current_voice = "voice/MAY02A_MAY0097.ogg"
    "真由理" "「不如说我还比较担心红莉栖酱的状态哦？」"
    $ stopvoc("CRS")
    play CRS "MAY02A_CRS0008"
    $ current_voice = "voice/MAY02A_CRS0008.ogg"
    "红莉栖" "「……真由理」"
    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0098"
    $ current_voice = "voice/MAY02A_MAY0098.ogg"
    "真由理" "「和真由喜不管什么时候要谈什么都可以哦？不用顾虑的说？」"
    $ stopvoc("CRS")
    play CRS "MAY02A_CRS0009"
    $ current_voice = "voice/MAY02A_CRS0009.ogg"
    "红莉栖" "「……但是」"
    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0099"
    $ current_voice = "voice/MAY02A_MAY0099.ogg"
    "真由理" "「嗯？」"
    $ stopvoc("CRS")
    play CRS "MAY02A_CRS0010"
    $ current_voice = "voice/MAY02A_CRS0010.ogg"
    "红莉栖" "「总感觉还有些……不习惯那样……」"
    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0100"
    $ current_voice = "voice/MAY02A_MAY0100.ogg"
    "真由理" "「那么，慢慢习惯起来就好了。呐？」"
    $ stopvoc("CRS")
    play CRS "MAY02A_CRS0011"
    $ current_voice = "voice/MAY02A_CRS0011.ogg"
    "红莉栖" "「……真由理」"
    "想让红莉栖酱振作起来。"
    "就好像菲利斯让真由喜振作起来一样。"
    "有什么合适的方法呢，我努力地思考着。"
    "注意到的时候，我已经将一个『蘑菇山』放到了红莉栖酱的嘴里"
    window hide
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_MAY001B"]]["Check"]=True


    $ loadBG(2,"EV_MAY001B")



    stop bgm 
    $ stopvoc("CRS")
    play CRS "MAY02A_CRS0012"
    $ current_voice = "voice/MAY02A_CRS0012.ogg"
    "红莉栖" "「！？　嗯！？」"
    $ stopvoc("CRS")
    play CRS "MAY02A_CRS0013"
    $ current_voice = "voice/MAY02A_CRS0013.ogg"
    "红莉栖" "「什，什么呀……这个……巧克力……」"
    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0101"
    $ current_voice = "voice/MAY02A_MAY0101.ogg"
    "真由理" "「嗯，那个，是能让红莉栖酱打起精神来的咒语？」"
    $ stopvoc("CRS")
    play CRS "MAY02A_CRS0014"
    $ current_voice = "voice/MAY02A_CRS0014.ogg"
    "红莉栖" "「诶？　咒语？」"
    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0102"
    $ current_voice = "voice/MAY02A_MAY0102.ogg"
    "真由理" "「……是这么说呢。嘿嘿，其实是刚刚想到的就是了。但是呢，感觉吃了好吃的东西的话，就会打起精神来的」"
    window hide



    $ loadBG(2,"BG16A1")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMC04"),"True","lh/CRS_AMC04a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    show screen phonebtn
    show screen phoneSD1
    play bgm "BGM18"

    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0103"
    $ current_voice = "voice/MAY02A_MAY0103.ogg"
    "真由理" "「感觉是不是好一些了呢？　要不要再吃一个？」"
    "真由喜放了一个在自己的嘴里，也微笑着将另一个递给红莉栖酱。"
    "红莉栖酱也许对于咒语什么的完全不信吧。"
    "果然好吃的东西的疗效，简直效果拔群啊。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMB08"),"True","lh/CRS_AMB08a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MAY02A_CRS0015"
    $ current_voice = "voice/MAY02A_CRS0015.ogg"
    "红莉栖" "「……原来如此，咒语什么的就是日本的魔法吧？好像很有趣的样子。虽然不是科学的，但是也有所谓的安慰剂效应在里面吧。真是的，别老是把我当傻瓜哦……」"
    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0104"
    $ current_voice = "voice/MAY02A_MAY0104.ogg"
    "真由理" "「那个，真由喜对于安慰剂什么的完全不了解就是了，但是如果稍微有点效果的话就很开心了」"
    $ stopvoc("CRS")
    play CRS "MAY02A_CRS0016"
    $ current_voice = "voice/MAY02A_CRS0016.ogg"
    "红莉栖" "「真由理，非常感谢。刚才不知有点怎么了。真是的，这可不像平时的我啊」"
    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0105"
    $ current_voice = "voice/MAY02A_MAY0105.ogg"
    "真由理" "「嗯嗯」"
    "变回了平时的红莉栖酱之后，我呼了口气。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMA01"),"True","lh/CRS_AMA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MAY02A_CRS0017"
    $ current_voice = "voice/MAY02A_CRS0017.ogg"
    "红莉栖" "「……真由理，接下来有事情吗？」"
    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0106"
    $ current_voice = "voice/MAY02A_MAY0106.ogg"
    "真由理" "「啊，嗯。是呢，和妈妈约好了」"
    $ stopvoc("CRS")
    play CRS "MAY02A_CRS0018"
    $ current_voice = "voice/MAY02A_CRS0018.ogg"
    "红莉栖" "「……是吗。那么……再见……」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASA06"),"True","lh/CRS_ASA06a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MAY02A_CRS0019"
    $ current_voice = "voice/MAY02A_CRS0019.ogg"
    "红莉栖" "「…………」"
    "红莉栖酱的视线不再迷茫，朝着我有些不好意思地笑了。"
    "但是，从她的笑容中，我感到一种不能让她独自一人下去的冲动。"
    "于是，拉住了即将消失在人群中的她的袖子。"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMC05"),"True","lh/CRS_AMC05a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MAY02A_CRS0020"
    $ current_voice = "voice/MAY02A_CRS0020.ogg"
    "红莉栖" "「……怎么了？」"
    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0107"
    $ current_voice = "voice/MAY02A_MAY0107.ogg"
    "真由理" "「那个，红莉栖酱……和我一起去吧？」"
    $ stopvoc("CRS")
    play CRS "MAY02A_CRS0021"
    $ current_voice = "voice/MAY02A_CRS0021.ogg"
    "红莉栖" "「但是，真由理，你不是有事情要去做吗？」"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_MAID_CAFE"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_MAID_CAFE"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_MAID_CAFE"])
    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0108"
    $ current_voice = "voice/MAY02A_MAY0108.ogg"
    "真由理" "「嗯，但是，在那之前必须去店里一趟。……红莉栖酱对于{color=#f00}女仆咖啡厅{/color}有兴趣吗？」"
    $ stopvoc("CRS")
    play CRS "MAY02A_CRS0022"
    $ current_voice = "voice/MAY02A_CRS0022.ogg"
    "红莉栖" "「女仆咖啡……」"
    $ stopvoc("CRS")
    play CRS "MAY02A_CRS0023"
    $ current_voice = "voice/MAY02A_CRS0023.ogg"
    "红莉栖" "「也不是说没有兴趣……但总感觉有些难进去呢……或者说总感觉不适合那里的氛围呢……」"
    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0109"
    $ current_voice = "voice/MAY02A_MAY0109.ogg"
    "红莉栖" "「那是真由喜工作的店呢。喵喵帕菲可是绝品哦。吃了的话，可会变得生龙活虎的哦」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMA09"),"True","lh/CRS_AMA09a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MAY02A_CRS0024"
    $ current_voice = "voice/MAY02A_CRS0024.ogg"
    "红莉栖" "「……生龙活虎……就像仙豆那样呢？啊，不是……刚才那个不是什么奇怪的东西……」"
    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0110"
    $ current_voice = "voice/MAY02A_MAY0110.ogg"
    "真由理" "「嗯嗯，所以，一起去吧？真由喜可以请客的说」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMA01"),"True","lh/CRS_AMA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MAY02A_CRS0025"
    $ current_voice = "voice/MAY02A_CRS0025.ogg"
    "红莉栖" "「……嗯，那样的话……难得有机会……就只是稍微去看一下哦」"
    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0111"
    $ current_voice = "voice/MAY02A_MAY0111.ogg"
    "真由理" "「太好了！那样的话就决定了，红莉栖大小姐，请允许我来带路♪」"
    "用力地牵着红莉栖酱的手腕，朝着ＭａｙＱｕｅｅｎ＋Ｎｙａ²迈出脚步。"
    "红莉栖酱肯定会和真由喜一样被菲利斯鼓起干劲的。"
    "我那么相信着——"

    window hide



    $ loadBG(0,"BG36A")

    "回到店里了以后，将红莉栖酱介绍给菲利斯——"
    "其实真由喜也很想和红莉栖酱一起在ＭａｙＱｕｅｅｎ＋Ｎｙａ²里吃喵喵帕菲的，但是因为要和妈妈在约好的时间碰头的关系，只好忍住了这份心情。"
    "在拜托店长用我打工的薪水来付了红莉栖酱的帕菲之后，我离开了店里。"
    "菲利斯和红莉栖酱能成为好朋友的话就好了呢。"

    stop bgm 
    hide screen phoneSD1
    window hide



    $ loadBG(0,"BG57E")


    python:
        RcvMail(40)
        ReplyMail(40)
        SndMail(41)
        RcvMail(42)
        ReplyMail(42)
        SndMail(43)
        RcvMail(44)
        ReadMail(44)
        RcvMail(45)
        ReplyMail(45)
        SndMail(46)
        RcvMail(47)
        ReplyMail(47)
        SndMail(48)
        SndMail(49)
        RcvMail(50)
        ReplyMail(50)
        SndMail(51)
        RcvMail(52)
        ReplyMail(52)
        SndMail(53)
        RcvMail(54)
        ReadMail(54)
    show screen phoneSD1
    play bgm "FD2BGM08"
    "真由喜拿着再也不会忘记掉的花束和妈妈碰头之后，走向了寺庙。"
    "在寺庙里和叔叔婶婶一起完成了外婆的法事之后，真由喜和大家道别，一个人去了外婆的坟前。"
    "想和外婆久违地好好说上几句。"
    "墓地里安静的很。"
    "除了真由喜之外，谁也没有——应该是这样。"
    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0112"
    $ current_voice = "voice/MAY02A_MAY0112.ogg"
    "真由理" "「……咦？」"
    "在外婆的坟前，看到了熟悉的白衣。"
    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0113"
    $ current_voice = "voice/MAY02A_MAY0113.ogg"
    "真由理" "「冈伦」"
    "将双手放在膝盖上，用手扶着额头的冈伦像是在考虑着什么的样子，听到真由喜的呼声后抬起头来。"
    window hide



    $ loadBG(2,"BG64E")

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA04"),"True","lh/OKA_ASA04a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    $ stopvoc("OKA")
    play OKA "MAY02A_OKA0000"
    $ current_voice = "voice/MAY02A_OKA0000.ogg"
    "伦太郎" "「真由理」"
    "在看到冈伦思索着什么的眼睛瞬间，我心中的那份与他见面的欣喜之情溢于言表。"
    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0114"
    $ current_voice = "voice/MAY02A_MAY0114.ogg"
    "真由理" "「……冈伦，你为什么会在这里？」"
    $ stopvoc("OKA")
    play OKA "MAY02A_OKA0001"
    $ current_voice = "voice/MAY02A_OKA0001.ogg"
    "伦太郎" "「我在等你」"
    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0115"
    $ current_voice = "voice/MAY02A_MAY0115.ogg"
    "真由理" "「但是，真由喜，没有告诉冈伦会来这里哦？」"
    $ stopvoc("OKA")
    play OKA "MAY02A_OKA0002"
    $ current_voice = "voice/MAY02A_OKA0002.ogg"
    "伦太郎" "「身为Ｍａｄ　Ｓｃｉｅｎｔｉｓｔ，对于自己人质位置的把握自然是了然于胸的」"
    "和那个梦里一样的说法。"
    "但是，这么说着的冈伦，和梦里的那个相比，要憔悴的多。"
    "看着都让人觉得憔悴。"
    "周围寂静的可怕。"
    "害怕这份沉默，没有多想便开口了。"
    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0116"
    $ current_voice = "voice/MAY02A_MAY0116.ogg"
    "真由理" "「……那个，吓了一跳呢。因为做过和冈伦一起给外婆上坟的梦……和那个梦一模一样……」"
    $ stopvoc("OKA")
    play OKA "MAY02A_OKA0003"
    $ current_voice = "voice/MAY02A_OKA0003.ogg"
    "伦太郎" "「这样啊……」"
    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0117"
    $ current_voice = "voice/MAY02A_MAY0117.ogg"
    "真由理" "「要是梦能成真就好了……我是这么想的……」"
    "听了真由喜的话的冈伦，不知为何露出了苦涩的表情，脱力地笑了。"
    "肯定不是梦里的展开吧。"
    "那种事情，从一开始就有这样的感觉。"
    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0118"
    $ current_voice = "voice/MAY02A_MAY0118.ogg"
    "真由理" "「但是，怎么说呢……冈伦，看起来很难过呢。那样的话，还是不要变成梦里那样就好了……」"
    $ stopvoc("OKA")
    play OKA "MAY02A_OKA0004"
    $ current_voice = "voice/MAY02A_OKA0004.ogg"
    "伦太郎" "「并不是那样的！」"
    hide screen phonebtn
    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0119"
    $ current_voice = "voice/MAY02A_MAY0119.ogg"
    "真由理" "「因为——真由喜是，冈伦的……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA03"),"True","lh/OKA_ASA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    show screen phonebtn
    $ stopvoc("OKA")
    play OKA "MAY02A_OKA0005"
    $ current_voice = "voice/MAY02A_OKA0005.ogg"
    "伦太郎" "「才不是什么重荷！」"
    "被冈伦强行把要说的话给顶了回去。"
    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0120"
    $ current_voice = "voice/MAY02A_MAY0120.ogg"
    "真由理" "「……冈……伦？」"
    $ stopvoc("OKA")
    play OKA "MAY02A_OKA0006"
    $ current_voice = "voice/MAY02A_OKA0006.ogg"
    "伦太郎" "「你才不是什么重荷！我才没有因为你而感到有什么负担！」"
    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0121"
    $ current_voice = "voice/MAY02A_MAY0121.ogg"
    "真由理" "「……为什么……是知道真由喜会这么说吗？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA04"),"True","lh/OKA_ASA04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_SYNCHRO"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_SYNCHRO"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_SYNCHRO"])
    "感觉现在的场景与梦境有着不自然的{color=#f00}同步率{/color}。"
    "就好像是，不知道看了几次一样的电影之后，连台词都已经背下来了。"
    $ stopvoc("OKA")
    play OKA "MAY02A_OKA0007"
    $ current_voice = "voice/MAY02A_OKA0007.ogg"
    "伦太郎" "「那种事情，本凤凰院凶真才不屑去做！人质的想法什么的，一眼就能全部看穿──」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ALA04"),"True","lh/OKA_ALA04a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    "我一直走到了冈伦跟前。"
    "将花束放在膝上，和坐着的冈伦四目相对。"
    hide screen phonebtn
    "然后，将手放在了冈伦的手上，望向了他的瞳孔深处。"
    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0122"
    $ current_voice = "voice/MAY02A_MAY0122.ogg"
    "真由理" "「冈伦，最近有些怪哦？」"
    $ stopvoc("OKA")
    play OKA "MAY02A_OKA0008"
    $ current_voice = "voice/MAY02A_OKA0008.ogg"
    "伦太郎" "「……我一直就都很奇怪吧」"
    "冈伦摆出一副不在意的样子，避开我的目光。"
    "有时候，就会如此的顽固，这一点倒是未曾改变呢。"
    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0123"
    $ current_voice = "voice/MAY02A_MAY0123.ogg"
    "真由理" "「嗯，就算如此……果然还是很奇怪哦……」"
    $ stopvoc("OKA")
    play OKA "MAY02A_OKA0009"
    $ current_voice = "voice/MAY02A_OKA0009.ogg"
    "伦太郎" "「……对于我很奇怪这一点也或多或少否定一下啊」"
    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0124"
    $ current_voice = "voice/MAY02A_MAY0124.ogg"
    "真由理" "「因为……本来就很奇怪嘛」"
    $ stopvoc("OKA")
    play OKA "MAY02A_OKA0010"
    $ current_voice = "voice/MAY02A_OKA0010.ogg"
    "伦太郎" "「真由理，让你感到不安抱歉了。但是，希望现在什么也不要问我，直到我能和盘托出的时候再问好吗」"
    $ stopvoc("OKA")
    play OKA "MAY02A_OKA0011"
    $ current_voice = "voice/MAY02A_OKA0011.ogg"
    "伦太郎" "「如果能等到那个时候的话肯定会和你说的。所以说，拜托了！」"
    "冈伦的样子，和那个梦里的相比还要可怜，于是就再也没有问下去。"
    "不想让他更加难过了。"
    "虽然不是很明白理由，但是大概冈伦已经为了真由喜而十分痛苦了吧。"
    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0125"
    $ current_voice = "voice/MAY02A_MAY0125.ogg"
    "真由理" "「……嗯，明白了哦，冈伦」"
    $ stopvoc("OKA")
    play OKA "MAY02A_OKA0012"
    $ current_voice = "voice/MAY02A_OKA0012.ogg"
    "伦太郎" "「真由理……」"
    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0126"
    $ current_voice = "voice/MAY02A_MAY0126.ogg"
    "真由理" "「一直以来，真由喜，都受到冈伦照顾了呢，抱歉啊」"
    $ stopvoc("OKA")
    play OKA "MAY02A_OKA0013"
    $ current_voice = "voice/MAY02A_OKA0013.ogg"
    "伦太郎" "「不要道歉，因为必须道歉的是我才对啊──」"
    "虽然不是这样的啊。"
    "虽然想这么说，但是感觉这么说只会让冈伦徒添悲伤，于是开始考虑有没有其他说法。"
    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0127"
    $ current_voice = "voice/MAY02A_MAY0127.ogg"
    "真由理" "「……呐，冈伦，还想吃平时的团子吗？真由喜，肚子饿了哦」"
    $ stopvoc("OKA")
    play OKA "MAY02A_OKA0014"
    $ current_voice = "voice/MAY02A_OKA0014.ogg"
    "伦太郎" "「啊、啊啊……」"
    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0128"
    $ current_voice = "voice/MAY02A_MAY0128.ogg"
    "真由理" "「美味的食物吃了的话就会有精神了哦？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ALA01"),"True","lh/OKA_ALA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    stop bgm 
    $ stopvoc("OKA")
    play OKA "MAY02A_OKA0015"
    $ current_voice = "voice/MAY02A_OKA0015.ogg"
    "伦太郎" "「……那是因为真由理是个贪吃鬼啊。坦率地承认也可以」"
    "冈伦的严肃表情稍微有些放松。"
    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0129"
    $ current_voice = "voice/MAY02A_MAY0129.ogg"
    "真由理" "「我觉得不是只有真由喜，全人类都是贪吃鬼啦！」"
    "鼓起脸颊，我向冈伦抗议道。"
    $ stopvoc("OKA")
    play OKA "MAY02A_OKA0016"
    $ current_voice = "voice/MAY02A_OKA0016.ogg"
    "伦太郎" "「就算那样，我觉得真由理属于特别爱吃的贪吃鬼哦？」"
    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0130"
    $ current_voice = "voice/MAY02A_MAY0130.ogg"
    "真由理" "「诶，没有那种事啦？　真由喜很普通的说？」"
    $ stopvoc("OKA")
    play OKA "MAY02A_OKA0017"
    $ current_voice = "voice/MAY02A_OKA0017.ogg"
    "伦太郎" "「不管什么时候总是会吃点香蕉啦炸鸡块啦之类的东西吧？」"
    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0131"
    $ current_voice = "voice/MAY02A_MAY0131.ogg"
    "真由理" "「诶，好像是的哦？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ALA02"),"True","lh/OKA_ALA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "MAY02A_OKA0018"
    $ current_voice = "voice/MAY02A_OKA0018.ogg"
    "伦太郎" "「嗯，总而言之，真由理的字典里容不下空腹这两个字呢。必须处以吃团子吃到吃不下的惩罚──」"
    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0132"
    $ current_voice = "voice/MAY02A_MAY0132.ogg"
    "真由理" "「嗯♪　那种惩罚不论何时都大欢迎哦ー」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA01"),"True","lh/OKA_ASA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    "稍微取回了平时的腔调的冈伦站了起来。"
    $ stopvoc("MAY")
    play MAY "MAY02A_MAY0133"
    $ current_voice = "voice/MAY02A_MAY0133.ogg"
    "真由理" "「但是在那之前──」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve


    "将花束放在了外婆的坟前，合掌祭拜了一会。"
    "感觉边上的冈伦也在做相同的事。"
    "周围十分寂静。"
    "虽然有很多想和外婆说的事情——但今天只有一件。"
    "外婆啊。"
    "请务必，让冈伦的负担少一些吧。"
    "请分给真由喜……一些勇气。"
    window hide


    $ loadBG(2,"IBGX033")



    "坚定地祈愿之后，慢慢地睁开了眼睛，和往常一样寻找着北极星。"
    "立刻就找到了。"
    "我注视着北极星，再次在心中坚定地许下了心愿。北极星仿佛就好像回应着我的心愿一样，似乎朝着我眨了眨眼睛。"

    hide screen phoneSD1
    window hide





    hide screen phonebtn
    scene expression Solid("000000")  with fade
    return






    return






    return






    return






    return
