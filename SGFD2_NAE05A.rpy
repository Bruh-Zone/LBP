label SGFD2_NAE05A:
    hide screen phonebtn
    scene expression Solid("000000")  with fade

    window hide


    $ loadBG(0,"BG02A3")


    $ date="7/10"
    $ day="TUE"
    hide screen phonebtn
    show screen phoneSD1

    play bgm "FD2BGM07"

    $ stopvoc("NAE")
    play NAE "NAE05A_NAE0000"
    $ current_voice = "voice/NAE05A_NAE0000.ogg"
    "绹" "「诶、嘿」"
    "我将延长电缆从厕所里拉出来。"
    "电缆被拉了过来，在地上像蛇一样盘着。"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CSA01"),"True","lh/DAR_CSA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "NAE05A_DAR0000"
    $ current_voice = "voice/NAE05A_DAR0000.ogg"
    "至" "「唔哦，这是像从天上下来的恩惠呢，还是像朝着地狱下垂的蜘蛛丝呢」"
    $ stopvoc("NAE")
    play NAE "NAE05A_NAE0001"
    $ current_voice = "voice/NAE05A_NAE0001.ogg"
    "绹" "「蜘蛛……好可怕」"
    "桶子叔叔把手机充电器插到延长线的插座里。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CSA05"),"True","lh/DAR_CSA05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "NAE05A_DAR0001"
    $ current_voice = "voice/NAE05A_DAR0001.ogg"
    "至" "「有了」"
    "开始充电。"
    "我想着，这么做真的好吗。"
    "刚才，我在考试一结束就来到这里的时候，桶子叔叔将延长线交给了我。"
    "这样大楼里没有电的问题就解决了，好像是这么说的。"
    window hide


    $ loadBG(2,"BG01A3")



    "许多连在一起的延长线从厕所的窗户中穿过，连到了内侧的大楼里。"
    "运气不错的是，内侧的大楼的走廊里有插座。"
    "就刚刚，我把延长电缆给插了进去。"
    "好像就打算这么借着用了。"
    "那不就是变成偷电的了么。"
    "我这么说道，桶子叔叔却说。"
    $ stopvoc("DAR")
    play DAR "NAE05A_DAR0002"
    $ current_voice = "voice/NAE05A_DAR0002.ogg"
    "至" "「关于这一点，支援者们会妥善处理的。绹酱就不必担心了。如果只是一点点的话也不会构成犯罪」"
    "这么说着，挺起了胸膛。"
    "但是却不肯告诉我会怎么处理。"
    "总而言之这样的话，电的问题就解决了。……大概。"
    hide screen phoneSD1
    window hide

    stop bgm 



    $ loadBG(0,"BG03A7R")
    play se "SGSE338L" loop


    hide screen phonebtn
    show screen phoneSD1
    "小心地上下挪动着锯子。"
    "不管怎么做，总是会发出声音的。"
    "声音的大小十分关键。"
    "慢慢地，明白了要诀。"
    "用的力气不能太大，进度也很缓慢，但是小孔确确实实地在扩大着。"
    "星期天就开始工作了。"
    "昨天也好今天也好，中午考试一结束，就蹲在这里了。"
    "多亏这样今天的国语和社会课并没有预习。"
    "但是，通过自己的估分，我觉得我应该能有平均分。"
    "总之赶紧把这工作完成吧。"
    "桶子叔叔那边也好像在苦战着。"
    "虽然电力不再是一个问题了，但是要是太明显地使用的话，会被外面的黑衣人发现的吧。"
    "所以，他说着什么在做的时间机器做好了连试一下能不能用的机会都没有什么的。"
    "这样的话，我好像没有添麻烦。"
    "因为，那个小洞好像就要通了。"
    "现在，我正在用锯子切割着一楼的天花板。"
    "虽然想到可能用脚踩一下就可以打通了。"
    "但是因为那会发出很大的响声所以不行。"
    "太令人焦躁了。"
    "再快些啊。"
    "再快些啊。"
    "我是不是很焦躁呢。"
    "咬了咬牙。"
    "抹了一把额头上滴下的汗水。"
    "慢慢地，安静地，操作着锯子。"

    stop se
    window hide


    $ loadBG(2,"BG_BLACK")



    hide screen phonebtn
    "然后——"
    window hide

    $ loadBG(0,"BG03A7R")

    hide screen phonebtn
    $ stopvoc("NAE")
    play NAE "NAE05A_NAE0002"
    $ current_voice = "voice/NAE05A_NAE0002.ogg"
    "绹" "「……好嘞」"
    play bgm "FD2BGM11"
    "锯下来的形状是正方形的。"
    "稳稳地拿了起来。"
    "将它给在一边工作着的桶子叔叔看了下。"
    $ stopvoc("NAE")
    play NAE "NAE05A_NAE0003"
    $ current_voice = "voice/NAE05A_NAE0003.ogg"
    "绹" "「完成了哦……！」"
    window hide



    $ loadBG(2,"BG03A7")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CSB02"),"True","lh/DAR_CSB02a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    show screen phonebtn
    $ stopvoc("DAR")
    play DAR "NAE05A_DAR0003"
    $ current_voice = "voice/NAE05A_DAR0003.ogg"
    "至" "「哦哦，绹酱氏，手脚真快呢」"
    "这样，应该会认同我一些了吧。"
    "自然地有些高兴起来。"
    window hide


    $ loadBG(2,"BG03A7R")



    hide screen phonebtn
    "靠了过来的桶子叔叔从那个洞里看了看楼下的情况。"
    "就算打通了洞，楼下还是一片黑暗，什么也喊不到。"
    "唯一的卷闸门关上了，也没有窗户什么的，所以也是没办法的事。"
    window hide



    $ loadBG(2,"BG03A7")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CSB03"),"True","lh/DAR_CSB03a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    show screen phonebtn
    $ stopvoc("DAR")
    play DAR "NAE05A_DAR0004"
    $ current_voice = "voice/NAE05A_DAR0004.ogg"
    "至" "「说起来这个大小的洞的话，我不是过不去么？」"
    $ stopvoc("NAE")
    play NAE "NAE05A_NAE0004"
    $ current_voice = "voice/NAE05A_NAE0004.ogg"
    "绹" "「……诶，桶子叔叔想过去么？那不太可能吧。」"
    "大概是我勉强可以钻进去的大小。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CSB01"),"True","lh/DAR_CSB01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "NAE05A_DAR0005"
    $ current_voice = "voice/NAE05A_DAR0005.ogg"
    "至" "「那，绹酱氏，你下去试试？」"
    $ stopvoc("NAE")
    play NAE "NAE05A_NAE0005"
    $ current_voice = "voice/NAE05A_NAE0005.ogg"
    "绹" "「下去以后干什么呢？」"
    $ stopvoc("DAR")
    play DAR "NAE05A_DAR0006"
    $ current_voice = "voice/NAE05A_DAR0006.ogg"
    "至" "「总之，先去调查一下４２寸电视机打不打得开吧」"
    $ stopvoc("NAE")
    play NAE "NAE05A_NAE0006"
    $ current_voice = "voice/NAE05A_NAE0006.ogg"
    "绹" "「打得开的话？」"
    $ stopvoc("DAR")
    play DAR "NAE05A_DAR0007"
    $ current_voice = "voice/NAE05A_DAR0007.ogg"
    "至" "「那样的话绹酱氏的工作就结束了」"
    $ stopvoc("NAE")
    play NAE "NAE05A_NAE0007"
    $ current_voice = "voice/NAE05A_NAE0007.ogg"
    "绹" "「要是亮不起来呢？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CSA02"),"True","lh/DAR_CSA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "NAE05A_DAR0008"
    $ current_voice = "voice/NAE05A_DAR0008.ogg"
    "至" "「……世界完蛋了」"
    $ stopvoc("NAE")
    play NAE "NAE05A_NAE0008"
    $ current_voice = "voice/NAE05A_NAE0008.ogg"
    "绹" "「…………」"
    "好像没有考虑过开不起来的对策啊。"
    "说不定开不起来也不错，什么的，脑海里冒出了这样幼稚的想法。"
    "那样的话，好歹和我就还会有些关系……这么想道。"
    "桶子叔叔和我是不同世界的人一样。"
    "明天也会和今天一样在这里什么的，想都不敢想。"
    "和时间一起突然消失得无影无踪也一点也不奇怪。"
    "我现在连问他之前为何要撒谎的理由都没有。"
    "不管他怎么口胡，我现在除了相信他之外别无他法。"
    "思念至此，我有些不安。"
    "我还是希望变成如果没有我工作就无法完成的情况。"
    $ stopvoc("NAE")
    play NAE "NAE05A_NAE0009"
    $ current_voice = "voice/NAE05A_NAE0009.ogg"
    "绹" "「好任性啊，我……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CSA01"),"True","lh/DAR_CSA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "NAE05A_DAR0009"
    $ current_voice = "voice/NAE05A_DAR0009.ogg"
    "至" "「什么好任性？」"
    $ stopvoc("NAE")
    play NAE "NAE05A_NAE0010"
    $ current_voice = "voice/NAE05A_NAE0010.ogg"
    "绹" "「不是，什么也没有」"
    "于是就这样，我爬下了楼。"
    hide screen phoneSD1
    window hide
    stop bgm 


    $ loadBG(0,"BG_BLACK")


    hide screen phonebtn
    "用着买来的绳子，我降落在店里。"
    "用手电筒照亮四周。"
    window hide

    $ loadBG(0,"BG04A3")

    show screen phonebtn
    show screen phoneSD1
    play bgm "BGM19"
    "店内堆积着直到天花板的显像管电视机。"
    "虽然有足够落脚的地方，但是担心万一踩的位置不对可能会全部倒塌，所以没能踩下去。"
    "——如果摸了堆着的显像管电视机的话，经常会惹爸爸生气。"
    hide screen phonebtn
    hide screen phoneSD1
    window hide


    $ stopvoc("TEN")
    play TEN "NAE05A_TEN0000"
    $ current_voice = "voice/NAE05A_TEN0000.ogg"
    "天王寺" "听好了绹。那么做很危险所以绝对不要乱摸哦。是因为以绝妙的平衡才能堆起来的吧。"
    $ stopvoc("TEN")
    play TEN "NAE05A_TEN0001"
    $ current_voice = "voice/NAE05A_TEN0001.ogg"
    "天王寺" "如果随便乱动的话，会被显像管的大山给活埋的哦。"
    window hide


    show screen phonebtn
    show screen phoneSD1
    "店里的灰尘比楼上还要多。"
    "感觉自己快要咳出来了，我拼命忍耐着。"
    $ stopvoc("NAE")
    play NAE "NAE05A_NAE0011"
    $ current_voice = "voice/NAE05A_NAE0011.ogg"
    "绹" "「…………」"
    "我又一次环视店内。"
    "当年的景象浮现在眼前。"
    "从２年前，这家店的时间就已经停止了。"
    "总是来这里玩的店。"
    "爸爸的店。"
    "爸爸一直坐着的椅子现在也还在那里。"
    "小小的桌子上，还放着２年前８月份的新闻。"
    $ stopvoc("NAE")
    play NAE "NAE05A_NAE0012"
    $ current_voice = "voice/NAE05A_NAE0012.ogg"
    "绹" "「爸爸……」"
    "有点儿想哭。"
    "是眼睛里进了灰尘吗。"
    "还是因为想起了爸爸的音容？"
    $ stopvoc("DAR")
    play DAR "NAE05A_DAR0010"
    $ current_voice = "voice/NAE05A_DAR0010.ogg"
    "至" "「喂，电缆」"
    "从小洞的洞口里看到桶子叔叔的脸，以及伸下来的延长电缆。"
    "我接过那个，走到了位于店的最深处的４２寸显像管电视机。"
    window hide


    $ loadBG(2,"BG04A3R")



    "意外。"
    "这么看起来的话，感觉并没有那么大。"
    "明明２年前还觉得这么大的电视机这世界上不可能有第二台了。"
    "当然，和相同类型的液晶电视相比，还是要大的多。"
    "是我长大了的原因吗。"
    "还是因为看多了在秋叶家比这个还要大的多的电视机的原因吗。"
    "不管是哪个，总觉得有些寂寞呢。"
    "……这么想着，将４２寸电视机的电源插到插座上。"
    "吞了一口口水，我按下了电视机下方的主电源按钮。"
    play se "SGSE339"
    $ stopvoc("NAE")
    play NAE "NAE05A_NAE0013"
    $ current_voice = "voice/NAE05A_NAE0013.ogg"
    "绹" "「…………」"
    $ stopvoc("NAE")
    play NAE "NAE05A_NAE0014"
    $ current_voice = "voice/NAE05A_NAE0014.ogg"
    "绹" "「……………………」"
    $ stopvoc("NAE")
    play NAE "NAE05A_NAE0015"
    $ current_voice = "voice/NAE05A_NAE0015.ogg"
    "绹" "「打不开」"
    $ stopvoc("DAR")
    play DAR "NAE05A_DAR0011"
    $ current_voice = "voice/NAE05A_DAR0011.ogg"
    "至" "「有遥控器吗？」"
    "４２寸电视机的遥控器的位置，我当然是知道的。"
    window hide


    $ loadBG(2,"BG04A3")



    "是在爸爸一直坐着的椅子旁边的柜子里。"
    "果然，现在还是在那里。"
    "从桶子叔叔那里接过３节新电池装进去之后，我朝着电视机按下了电源按钮。"
    "但是，果然什么反应都没有。"
    "不管试几次，都不行。"
    "是我许下了那样的愿望的关系吗？"
    "要是打不开就好了，什么的。虽然不想那么想。"
    "明明是爸爸最喜欢的东西。"
    $ stopvoc("DAR")
    play DAR "NAE05A_DAR0012"
    $ current_voice = "voice/NAE05A_DAR0012.ogg"
    "至" "「啊，果然坏掉了啊——都放了两年了，刚就有些不好的预感了」"
    $ stopvoc("NAE")
    play NAE "NAE05A_NAE0016"
    $ current_voice = "voice/NAE05A_NAE0016.ogg"
    "绹" "「怎么办呢？」"
    $ stopvoc("DAR")
    play DAR "NAE05A_DAR0013"
    $ current_voice = "voice/NAE05A_DAR0013.ogg"
    "至" "「什么怎么办，任务结束了啊」"
    $ stopvoc("NAE")
    play NAE "NAE05A_NAE0017"
    $ current_voice = "voice/NAE05A_NAE0017.ogg"
    "绹" "「诶，结束了？」"
    $ stopvoc("DAR")
    play DAR "NAE05A_DAR0014"
    $ current_voice = "voice/NAE05A_DAR0014.ogg"
    "至" "「因为，４２寸电视机开不起来的话，就没办法了」"
    "我突然大声说道。"
    $ stopvoc("NAE")
    play NAE "NAE05A_NAE0018"
    $ current_voice = "voice/NAE05A_NAE0018.ogg"
    "绹" "「修理，请让我来做吧！」"
    stop bgm 
    $ stopvoc("DAR")
    play DAR "NAE05A_DAR0015"
    $ current_voice = "voice/NAE05A_DAR0015.ogg"
    "至" "「嘘！」"
    $ stopvoc("NAE")
    play NAE "NAE05A_NAE0019"
    $ current_voice = "voice/NAE05A_NAE0019.ogg"
    "绹" "「啊……」"
    "我赶紧用手捂住嘴巴。"
    "桶子叔叔朝我招招手，从洞口降下了绳子。"
    window hide



    $ loadBG(0,"BG03A7")

    play bgm "FD2BGM05"
    "回到了楼上。"
    "小学生的时候，在学校里的那种爬杆，我玩得很好。所以用这样的绳子上下也并不是难事。"
    "等我上来了以后，桶子叔叔开口说道。"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CSA01"),"True","lh/DAR_CSA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "NAE05A_DAR0016"
    $ current_voice = "voice/NAE05A_DAR0016.ogg"
    "至" "「再说一遍，任务到此结束了。进入撤离阶段」"
    $ stopvoc("NAE")
    play NAE "NAE05A_NAE0020"
    $ current_voice = "voice/NAE05A_NAE0020.ogg"
    "绹" "「修理、我可以做哦」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CSA06"),"True","lh/DAR_CSA06a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    "就算我这么说，桶子叔叔还是朝我投来怀疑的目光。"
    $ stopvoc("DAR")
    play DAR "NAE05A_DAR0017"
    $ current_voice = "voice/NAE05A_DAR0017.ogg"
    "至" "「这也太难了吧。因为那个电视机的话不管是那个洞还是厕所的窗户都是无法通过的」"
    $ stopvoc("DAR")
    play DAR "NAE05A_DAR0018"
    $ current_voice = "voice/NAE05A_DAR0018.ogg"
    "至" "「要是打开卷闸门拿到外面去的话，被黑衣人看到就完了」"

    $ targetmailid = 473

    $ LR_RM_CHANCE=4
    call CHECK_RM_RECEIVE
    $ stopvoc("NAE")
    play NAE "NAE05A_NAE0021"
    $ current_voice = "voice/NAE05A_NAE0021.ogg"
    "绹" "「没有必要拿到外面去哦」"
    call CHECK_RM_RECEIVE
    $ stopvoc("DAR")
    play DAR "NAE05A_DAR0019"
    $ current_voice = "voice/NAE05A_DAR0019.ogg"
    "至" "「那，谁来修啊？」"
    call CHECK_RM_RECEIVE
    $ stopvoc("NAE")
    play NAE "NAE05A_NAE0022"
    $ current_voice = "voice/NAE05A_NAE0022.ogg"
    "绹" "「我来」"
    call CHECK_RM_RECEIVE
    $ stopvoc("DAR")
    play DAR "NAE05A_DAR0020"
    $ current_voice = "voice/NAE05A_DAR0020.ogg"
    "至" "「……不不不」"

    call CHECK_RM_RECEIVE
    $ stopvoc("DAR")
    play DAR "NAE05A_DAR0021"
    $ current_voice = "voice/NAE05A_DAR0021.ogg"
    "至" "「显像管电视机的修理工作，可不能交给门外汉来做啊」"
    $ stopvoc("DAR")
    play DAR "NAE05A_DAR0022"
    $ current_voice = "voice/NAE05A_DAR0022.ogg"
    "至" "「而且也有听说一步弄错就触电身亡的事情」"
    $ stopvoc("NAE")
    play NAE "NAE05A_NAE0023"
    $ current_voice = "voice/NAE05A_NAE0023.ogg"
    "绹" "「那个的话，如果好好放电放完就没关系的。４２寸电视机已经２年没有接入电源了。」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CSA02"),"True","lh/DAR_CSA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "NAE05A_DAR0023"
    $ current_voice = "voice/NAE05A_DAR0023.ogg"
    "至" "「难道说，知道的很详细吗？」"
    "我点了点头。"
    $ stopvoc("NAE")
    play NAE "NAE05A_NAE0024"
    $ current_voice = "voice/NAE05A_NAE0024.ogg"
    "绹" "「以前的时候，爸爸稍微教过我一点」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CSA01"),"True","lh/DAR_CSA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "NAE05A_DAR0024"
    $ current_voice = "voice/NAE05A_DAR0024.ogg"
    "至" "「……但是，只是一点点吧？」"
    $ stopvoc("NAE")
    play NAE "NAE05A_NAE0025"
    $ current_voice = "voice/NAE05A_NAE0025.ogg"
    "绹" "「虽然是那样……」"
    $ stopvoc("NAE")
    play NAE "NAE05A_NAE0026"
    $ current_voice = "voice/NAE05A_NAE0026.ogg"
    "绹" "「但是，修好的可能性，虽然很少，还是有一点的」"
    $ stopvoc("NAE")
    play NAE "NAE05A_NAE0027"
    $ current_voice = "voice/NAE05A_NAE0027.ogg"
    "绹" "「比起直接放弃，是不是稍微好一些呢……的说」"
    $ stopvoc("NAE")
    play NAE "NAE05A_NAE0028"
    $ current_voice = "voice/NAE05A_NAE0028.ogg"
    "绹" "「我想尝试一些就算我也能做得到的修理方法」"
    $ stopvoc("DAR")
    play DAR "NAE05A_DAR0025"
    $ current_voice = "voice/NAE05A_DAR0025.ogg"
    "至" "「……没有危险吗？」"
    $ stopvoc("NAE")
    play NAE "NAE05A_NAE0029"
    $ current_voice = "voice/NAE05A_NAE0029.ogg"
    "绹" "「蓄电器啦，保险丝什么的我是不太懂，但至少……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CSA04"),"True","lh/DAR_CSA04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "NAE05A_DAR0026"
    $ current_voice = "voice/NAE05A_DAR0026.ogg"
    "至" "「但至少……！」"
    $ stopvoc("NAE")
    play NAE "NAE05A_NAE0030"
    $ current_voice = "voice/NAE05A_NAE0030.ogg"
    "绹" "「电源回路啦，基板什么的，还是可以检查一下的」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CSA01"),"True","lh/DAR_CSA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "NAE05A_DAR0027"
    $ current_voice = "voice/NAE05A_DAR0027.ogg"
    "至" "「那里也可能出问题吗？」"
    $ stopvoc("NAE")
    play NAE "NAE05A_NAE0031"
    $ current_voice = "voice/NAE05A_NAE0031.ogg"
    "绹" "「说不定是因为放久了焊接脱落了呢」"
    "焊铁什么的，小学的手工课上学过，爸爸也教过我一点。"
    "电焊铁的话，因为听桶子叔叔说过买了用电池的那种，所以没问题。"
    $ stopvoc("NAE")
    play NAE "NAE05A_NAE0032"
    $ current_voice = "voice/NAE05A_NAE0032.ogg"
    "绹" "「所以试着在基板上把原来的焊点全部再做一遍吧」"
    "所谓重新做一遍，就是在已经焊在一起的节点上，再焊一遍。"
    "我想起爸爸说过电路的基板会因为时间的流逝而损坏老化。"
    $ stopvoc("NAE")
    play NAE "NAE05A_NAE0033"
    $ current_voice = "voice/NAE05A_NAE0033.ogg"
    "绹" "「那样的话，再试着开一次。……怎么样？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CSA03"),"True","lh/DAR_CSA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "NAE05A_DAR0028"
    $ current_voice = "voice/NAE05A_DAR0028.ogg"
    "至" "「唔」"
    "桶子叔叔陷入了考虑中。"
    $ stopvoc("DAR")
    play DAR "NAE05A_DAR0029"
    $ current_voice = "voice/NAE05A_DAR0029.ogg"
    "至" "「没有别的要做的吗？」"
    $ stopvoc("NAE")
    play NAE "NAE05A_NAE0034"
    $ current_voice = "voice/NAE05A_NAE0034.ogg"
    "绹" "「没有。不如说……也做不了别的什么了」"
    "我实话实说。"

    $ gd["RCVmailData"][gc["ScriptMacros"]["RM_NAE_RECV_RUK02_01"]]["late"]=True
    $ lml.append(gc["ScriptMacros"]["RM_NAE_RECV_RUK02_01"])

    $ stopvoc("NAE")
    play NAE "NAE05A_NAE0035"
    $ current_voice = "voice/NAE05A_NAE0035.ogg"
    "绹" "「所以，请让我试试看吧。」"
    "我直直地望着他，拜托道。"
    "桶子叔叔小小地叹了口气。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CSA07"),"True","lh/DAR_CSA07a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "NAE05A_DAR0030"
    $ current_voice = "voice/NAE05A_DAR0030.ogg"
    "至" "「能把刚才的台词用更甜美的感觉再说一次吗？」"
    $ stopvoc("NAE")
    play NAE "NAE05A_NAE0036"
    $ current_voice = "voice/NAE05A_NAE0036.ogg"
    "绹" "「…………」"
    "虽然不是很懂他在说什么，但肯定是什么变态的事情没错。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CSB02"),"True","lh/DAR_CSB02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    "这么想着瞪过去的时候，发现桶子叔叔伸了个懒腰，亲切地笑着。"
    $ stopvoc("DAR")
    play DAR "NAE05A_DAR0031"
    $ current_voice = "voice/NAE05A_DAR0031.ogg"
    "至" "「还，还有，如果要做自己能做到的事的话，必须要为自己立一个Ｆｌａｇ什么的」"
    $ stopvoc("NAE")
    play NAE "NAE05A_NAE0037"
    $ current_voice = "voice/NAE05A_NAE0037.ogg"
    "绹" "「桶子叔叔……」"
    $ stopvoc("DAR")
    play DAR "NAE05A_DAR0032"
    $ current_voice = "voice/NAE05A_DAR0032.ogg"
    "至" "「这个，可是工口游戏攻略的铁则哦」"
    $ stopvoc("NAE")
    play NAE "NAE05A_NAE0038"
    $ current_voice = "voice/NAE05A_NAE0038.ogg"
    "绹" "「……是，是」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CSA01"),"True","lh/DAR_CSA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "NAE05A_DAR0033"
    $ current_voice = "voice/NAE05A_DAR0033.ogg"
    "至" "「嘛，如果没有危险的话，我觉得还是有价值试一下的。」"
    $ stopvoc("NAE")
    play NAE "NAE05A_NAE0039"
    $ current_voice = "voice/NAE05A_NAE0039.ogg"
    "绹" "「……恩。我会努力的。」"
    "正因为这是我能做到的事。"
    hide screen phoneSD1
    window hide

    stop bgm 



    $ loadBG(0,"BG04A4")
    $ loadBG(0,"IBG045A",png=True)



    hide screen phonebtn
    show screen phoneSD1
    play bgm "BGM15"
    "首先要做的是把外部的壳给去掉的工作。"
    "只靠手电筒用螺丝刀来拧螺丝，有些苦难。"
    "空气又不好，又很闷，再加上我有些睡眠不足，不知为何脑子里总有些不舒服。"
    "而且今天呆在这里差不多也有６个小时了。"
    "在这里呆太久也许不太好。"
    $ stopvoc("NAE")
    play NAE "NAE05A_NAE0040"
    $ current_voice = "voice/NAE05A_NAE0040.ogg"
    "绹" "「呐，桶子叔叔，我能再问一遍之前的问题吗？」"
    "我小声地朝楼上喊道。"
    $ stopvoc("NAE")
    play NAE "NAE05A_NAE0041"
    $ current_voice = "voice/NAE05A_NAE0041.ogg"
    "绹" "「为什么，是现在？」"
    $ stopvoc("DAR")
    play DAR "NAE05A_DAR0034"
    $ current_voice = "voice/NAE05A_DAR0034.ogg"
    "至" "「恩？　在说什么？」"
    "桶子叔叔从洞口里探出头来。"
    "感觉像倒过来的打地鼠那种感觉。"
    $ stopvoc("NAE")
    play NAE "NAE05A_NAE0042"
    $ current_voice = "voice/NAE05A_NAE0042.ogg"
    "绹" "「为什么桶子叔叔会选择现在这个时候回到秋叶原呢」"
    "最开始就听说了他之前在海外。"
    "但是也说过半年前就回到了日本。"
    "那这半年里，他都干了些什么呢。为什么会在７月的时候，回到这里来呢。"
    "之前问的时候，他说“有事情要办”，但是却没有回答为什么选择现在来、"
    $ stopvoc("DAR")
    play DAR "NAE05A_DAR0035"
    $ current_voice = "voice/NAE05A_DAR0035.ogg"
    "至" "「你听说过太阳风暴的传言吗？」"
    $ stopvoc("NAE")
    play NAE "NAE05A_NAE0043"
    $ current_voice = "voice/NAE05A_NAE0043.ogg"
    "绹" "「太阳风暴？」"
    $ stopvoc("DAR")
    play DAR "NAE05A_DAR0036"
    $ current_voice = "voice/NAE05A_DAR0036.ogg"
    "至" "「简单来说就是从太阳发射出来的看不见的电磁风暴，」"
    $ stopvoc("DAR")
    play DAR "NAE05A_DAR0037"
    $ current_voice = "voice/NAE05A_DAR0037.ogg"
    "至" "「最近啊，这个话题很热门呢。据说有史以来最大的太阳风暴要来了」"
    $ stopvoc("DAR")
    play DAR "NAE05A_DAR0038"
    $ current_voice = "voice/NAE05A_DAR0038.ogg"
    "至" "「如果到达了地球的话，电子仪器可能就会全部失灵」"
    $ stopvoc("NAE")
    play NAE "NAE05A_NAE0044"
    $ current_voice = "voice/NAE05A_NAE0044.ogg"
    "绹" "「也就是说，全部损坏？」"
    $ stopvoc("DAR")
    play DAR "NAE05A_DAR0039"
    $ current_voice = "voice/NAE05A_DAR0039.ogg"
    "至" "「是的，而且是世界规模的呢。太阳风暴就是这种能让全世界都完蛋的东西」"
    $ stopvoc("NAE")
    play NAE "NAE05A_NAE0045"
    $ current_voice = "voice/NAE05A_NAE0045.ogg"
    "绹" "「真的会来吗？」"
    $ stopvoc("DAR")
    play DAR "NAE05A_DAR0040"
    $ current_voice = "voice/NAE05A_DAR0040.ogg"
    "至" "「谁知道呢。你就算去问专家，意见也不一致」"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_INFRA"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_INFRA"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_INFRA"])
    $ stopvoc("DAR")
    play DAR "NAE05A_DAR0041"
    $ current_voice = "voice/NAE05A_DAR0041.ogg"
    "至" "「但是，就算来的话，眼睛也直接看不见吧。但是肯定{color=#f00}基础设施{/color}的复原就要花上很久」"
    $ stopvoc("DAR")
    play DAR "NAE05A_DAR0042"
    $ current_voice = "voice/NAE05A_DAR0042.ogg"
    "至" "「所以说，在太阳风暴到来的前后，Ｄｍａｉｌ的发送成功率可能会相差很多。」"
    $ stopvoc("DAR")
    play DAR "NAE05A_DAR0043"
    $ current_voice = "voice/NAE05A_DAR0043.ogg"
    "至" "「怀着以防万一的心情，就回到了这里」"
    $ stopvoc("NAE")
    play NAE "NAE05A_NAE0046"
    $ current_voice = "voice/NAE05A_NAE0046.ogg"
    "绹" "「唔……」"
    window hide
    hide background-png  with dissolve
    show screen phonebtn
    "听他说话的时候，螺丝已经拧下来了。"
    "我将外壳抱住取了下来。"
    "因为灰尘很多，很可能衣服上也被弄脏了。但是太暗了，没办法确认。"
    window hide
    $ loadBG(0,"IBG045B",png=True)


    hide screen phonebtn
    $ stopvoc("NAE")
    play NAE "NAE05A_NAE0047"
    $ current_voice = "voice/NAE05A_NAE0047.ogg"
    "绹" "「外壳，拿下来了」"
    $ stopvoc("DAR")
    play DAR "NAE05A_DAR0044"
    $ current_voice = "voice/NAE05A_DAR0044.ogg"
    "至" "「有什么发现吗？」"
    $ stopvoc("NAE")
    play NAE "NAE05A_NAE0048"
    $ current_voice = "voice/NAE05A_NAE0048.ogg"
    "绹" "「那个……」"
    "太暗了，很难看出来……"
    $ stopvoc("NAE")
    play NAE "NAE05A_NAE0049"
    $ current_voice = "voice/NAE05A_NAE0049.ogg"
    "绹" "「现在，还不知道……」"
    $ stopvoc("NAE")
    play NAE "NAE05A_NAE0050"
    $ current_voice = "voice/NAE05A_NAE0050.ogg"
    "绹" "「被其他零件挡住了，还看不到基板……」"
    $ stopvoc("DAR")
    play DAR "NAE05A_DAR0045"
    $ current_voice = "voice/NAE05A_DAR0045.ogg"
    "至" "「那把零件拆下来就能看出来了」"
    "说的倒……简单……"
    "拆电视这种事情，果然还是第一次干……"
    "不好好记住拆下来的顺序的话，就感觉没法装回去啊。"
    "难度好高……"
    "不，但是不能不做。"
    "我要是做不到的话，Ｄｍａｉｌ就发不出去了。"

    stop bgm 
    stop se
    stop se

    hide screen phonebtn
    $ targetmailid = gc["ScriptMacros"]["FM_NAE05A_RECV_FMM01"]
    if phonemailring!= "":
        play se phonemailring
    if persistent.skipmail==False:
        $ renpy.choice_for_skipping()
    if targetmailid != "":
        $ RcvMail(targetmailid)
        $ targetmailid=""

    hide background-png  with dissolve
    show screen phonebtn
    $ stopvoc("NAE")
    play NAE "NAE05A_NAE0051"
    $ current_voice = "voice/NAE05A_NAE0051.ogg"
    "绹" "「……！」"

    "突然，口袋里的手机响了。"

    window hide


    show screen phonebtn
    hide screen phonebtn
    hide screen phonebtn2
    show screen phone(interact=False)


    "邮件……是千佳音阿姨发过来的。"
    call read_last_mail (p=True)
    window hide





    $ stopvoc("NAE")
    play NAE "NAE05A_NAE0052"
    $ current_voice = "voice/NAE05A_NAE0052.ogg"
    "绹" "「……必须回去了」"
    "不能让秋叶家的人担心。"
    "要在朋友家开学习会所以会晚回去一些——"
    "就算撒了这样的慌，我心里还是闷的慌。"
    window hide
    call hide_phone

    "不能再让他们担心了。"

    hide screen phoneSD1
    window hide





    hide screen phonebtn
    scene expression Solid("000000")  with fade
    return
