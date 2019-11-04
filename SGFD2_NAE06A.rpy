label SGFD2_NAE06A:
    hide screen phonebtn
    scene expression Solid("000000")  with fade

    window hide


    $ loadBG(0,"IBGX048")
    play se "SGSE366L" loop


    $ date="7/12"
    $ day="THU"
    hide screen phonebtn
    show screen phoneSD1

    "来到屋顶上，我猛地抬头仰望天空。"
    "为了不让黑衣人们看见，我尽可能地压低了身子，头也尽可能地放低。"
    "要是一直在风很大的屋顶上的话，感觉有点喘不过气来。但是现在只是想吹吹风而已。"
    "结果，考试成绩很一般。"
    "尤其是第二天的社会科目，只有平均分。"
    "是那种会被留未穗姐姐安慰的程度。"
    "感觉并没有吸取教训，我逃了考试之后再度开始的社团活动，今天也来到了这里。"
    hide screen phoneSD1
    window hide
    stop se
    stop se



    $ loadBG(0,"BG04A4")
    $ loadBG(0,"IBG045B",png=True)



    hide screen phonebtn
    show screen phoneSD1
    play bgm "BGM20"

    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0000"
    $ current_voice = "voice/NAE06A_NAE0000.ogg"
    "绹" "「唔……唔唔……」"
    "不小心，发出了声音。"
    "嘴里衔着手电筒，我将注意力集中到指尖。"
    "右手拿着电焊铁，左手拿着焊料。"
    "在基板上细小的焊点之间，慢慢地将焊料焊上去，随着铅融化的味道，一个个银色的小球出现了。"
    "昨天也好，今天也好。"
    "从放学的傍晚开始，我就一直在这昏暗的店内做着这样精细的工作。"
    "就算如此，４２寸电视机的基板很大、"
    "要焊接的地方，非常的多。"
    "从昨天开始已经不知道做了几个小时了，但感觉才做了一半左右。"
    "肯定是因为我效率太低了。"
    "这么一想，更加紧张起来。"
    "虽然是自己说出来的，但是一想到必须一次决胜负，就紧张得手指都要颤动起来了。"
    "在屋顶上休息还有什么意义哦……"
    "用力地呼了口气。"
    "桶子叔叔那边进度如何呢？"
    "万一已经快要做完的话，说不定都不需要我来帮忙了。"
    "说起来，从刚才开始一直就有听到很小的说话声诶……"
    "２楼除了桶子叔叔并没有别人。"

    stop bgm 
    "也就是说，电话？"
    "是在给谁打电话呢？"
    "刚好，电焊铁的电池快用光了，在换的时候顺便看一下吧。"
    window hide


    hide background-png  with dissolve


    $ loadBG(0,"BG03A7")

    show screen phonebtn
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0001"
    $ current_voice = "voice/NAE06A_NAE0001.ogg"
    "绹" "「恩……嘿」"
    window hide


    $ loadBG(2,"BG02A3")



    play bgm "BGM22"
    "偷偷地朝２楼看了一眼，发现桶子叔叔并没有在工作，而是整个人嵌在沙发里。"
    "一边吃着零食，一边在打电话。"
    $ stopvoc("DAR")
    play DAR "NAE06A_DAR0000"
    $ current_voice = "voice/NAE06A_DAR0000.ogg"
    "至" "「恩，是啊是啊，这样下去就要完不成了啊」"
    $ stopvoc("DAR")
    play DAR "NAE06A_DAR0001"
    $ current_voice = "voice/NAE06A_DAR0001.ogg"
    "至" "「……但是，我拒绝。方法就交给你那边去想吧。关于那个我怎样都可以」"

    $ targetmailid = 475

    $ LR_RM_CHANCE=3
    call CHECK_RM_RECEIVE
    $ stopvoc("DAR")
    play DAR "NAE06A_DAR0002"
    $ current_voice = "voice/NAE06A_DAR0002.ogg"
    "至" "「……是不是有点随便过头了啊。好了就这样吧，今天之内拜托了」"
    call CHECK_RM_RECEIVE
    $ stopvoc("DAR")
    play DAR "NAE06A_DAR0003"
    $ current_voice = "voice/NAE06A_DAR0003.ogg"
    "至" "「真的么？　那能不能拜托买一下Ｃｏｍｉｃ·ＬＯ？」"
    call CHECK_RM_RECEIVE
    $ stopvoc("DAR")
    play DAR "NAE06A_DAR0004"
    $ current_voice = "voice/NAE06A_DAR0004.ogg"
    "至" "「呜哇ｗｗｗＯｋｗｗｗ」"

    call CHECK_RM_RECEIVE

    $ gd["RCVmailData"][gc["ScriptMacros"]["RM_NAE_RECV_MAK03_01"]]["late"]=True
    $ lml.append(gc["ScriptMacros"]["RM_NAE_RECV_MAK03_01"])

    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0002"
    $ current_voice = "voice/NAE06A_NAE0002.ogg"
    "绹" "「…………」"
    "看起来很开心地聊着天……"
    "完全感受不到紧张感。"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CSA01"),"True","lh/DAR_CSA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "NAE06A_DAR0005"
    $ current_voice = "voice/NAE06A_DAR0005.ogg"
    "至" "「绹酱氏」"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0003"
    $ current_voice = "voice/NAE06A_NAE0003.ogg"
    "绹" "「诶……？」"
    "突然被叫了名字，我吓了一跳。"
    $ stopvoc("DAR")
    play DAR "NAE06A_DAR0006"
    $ current_voice = "voice/NAE06A_DAR0006.ogg"
    "至" "「我啊，要稍微出去一下」"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0004"
    $ current_voice = "voice/NAE06A_NAE0004.ogg"
    "绹" "「出，出去一下？」"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0005"
    $ current_voice = "voice/NAE06A_NAE0005.ogg"
    "绹" "「……出去的了吗？」"
    "桶子叔叔被关在这里差不多已经一周了。"
    "这一周里，他一次也没有出去过。"
    "桶子叔叔的庞大身躯要从厕所的那个小窗户里硬挤出去，实在是困难之极，在一边帮忙的我也是费劲了力气。"
    "于是——"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0006"
    $ current_voice = "voice/NAE06A_NAE0006.ogg"
    "绹" "「桶子叔叔，你可是被盯上的人哦？要是在外面走来走去的话，说不定很快就被发现了」"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0007"
    $ current_voice = "voice/NAE06A_NAE0007.ogg"
    "绹" "「要是被抓到了的话，怎么办啊？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CSA04"),"True","lh/DAR_CSA04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "NAE06A_DAR0007"
    $ current_voice = "voice/NAE06A_DAR0007.ogg"
    "至" "「哦哦，绹酱氏，莫非你在担心我？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CSA07"),"True","lh/DAR_CSA07a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "NAE06A_DAR0008"
    $ current_voice = "voice/NAE06A_DAR0008.ogg"
    "至" "「那样的话就再演得好一点。“请不要离开我，欧尼桑”这么说的话，我就一辈子都可以留在这里哦」"
    $ stopvoc("DAR")
    play DAR "NAE06A_DAR0009"
    $ current_voice = "voice/NAE06A_DAR0009.ogg"
    "至" "「尼特族赛高。工作的话就输了」"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0008"
    $ current_voice = "voice/NAE06A_NAE0008.ogg"
    "绹" "「又来了啊……」"
    "这么说着，就用些玩笑话就把话题扯开了。"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0009"
    $ current_voice = "voice/NAE06A_NAE0009.ogg"
    "绹" "「我认为桶子叔叔一个人没法从这里出去」"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0010"
    $ current_voice = "voice/NAE06A_NAE0010.ogg"
    "绹" "「如果是那个厕所的窗户的话，没有我在后面推桶子叔叔就会卡在那里」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CSA01"),"True","lh/DAR_CSA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_MUNEATSU"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_MUNEATSU"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_MUNEATSU"])
    $ stopvoc("DAR")
    play DAR "NAE06A_DAR0010"
    $ current_voice = "voice/NAE06A_DAR0010.ogg"
    "至" "「如果再能让绹酱氏摸一下我的大尻的话{color=#f00}胸热{/color}。在我们的业界这是赞美哦」"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0011"
    $ current_voice = "voice/NAE06A_NAE0011.ogg"
    "绹" "「……为什么要出去呢？」"

    stop bgm 

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CSA02"),"True","lh/DAR_CSA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "NAE06A_DAR0011"
    $ current_voice = "voice/NAE06A_DAR0011.ogg"
    "至" "「绹酱氏，我希望你只要记住这一点就好」"
    $ stopvoc("DAR")
    play DAR "NAE06A_DAR0012"
    $ current_voice = "voice/NAE06A_DAR0012.ogg"
    "至" "「有的时候，男人是可以为了浪漫不要性命的」"
    $ stopvoc("DAR")
    play DAR "NAE06A_DAR0013"
    $ current_voice = "voice/NAE06A_DAR0013.ogg"
    "至" "「这是，女性绝对无法理解的，男人的本性。」"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0012"
    $ current_voice = "voice/NAE06A_NAE0012.ogg"
    "绹" "「…………」"
    "不要……性命……"
    "直到刚才还在的轻浮感都消失了。"
    "桶子叔叔两眼发光地看着我。"
    "……那双眼睛没有在撒谎。"
    hide screen phoneSD1
    window hide



    $ loadBG(0,"IBGX033")

    hide screen phonebtn
    show screen phoneSD1
    "和之前一样用力地将桶子叔叔的大尻推了出去之后。"
    "从里侧的大楼的玄关里走了出去，和桶子叔叔一起前往车站方向。"
    window hide


    $ loadBG(2,"BG36E2")



    play bgm "BGM07"
    show screen phonebtn
    "接着，才没走了几步，我看到从前方走来的男人的脸之后，吓了一跳。"
    "赶紧慌张地拉着桶子叔叔的手，跑到了拉面屋内部的楼梯的阴暗处躲了起来。"
    window hide


    $ loadBG(2,"BG_BLACK")




    hide screen phonebtn
    $ stopvoc("DAR")
    play DAR "NAE06A_DAR0014"
    $ current_voice = "voice/NAE06A_DAR0014.ogg"
    "至" "「等等，绹酱氏。把我拉到这种阴暗的地方，是想对我动粗嘛？此处应有本子，此处应有本子」"
    $ stopvoc("DAR")
    play DAR "NAE06A_DAR0015"
    $ current_voice = "voice/NAE06A_DAR0015.ogg"
    "至" "「继续干下去也ＯＫ哦」"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0013"
    $ current_voice = "voice/NAE06A_NAE0013.ogg"
    "绹" "「嘘！」"
    "我用手堵住桶子叔叔的嘴。"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0014"
    $ current_voice = "voice/NAE06A_NAE0014.ogg"
    "绹" "「刚才走过去的是黑衣人哦」"
    $ stopvoc("DAR")
    play DAR "NAE06A_DAR0016"
    $ current_voice = "voice/NAE06A_DAR0016.ogg"
    "至" "「……当真？」"
    "我微微颔首。"
    "刚才那个黑衣人在我从放学后到这里的路上也看到了。那个时候，他在爸爸的大楼正对着的一辆车里。"
    "为什么，他会来这边哦。"
    "好巧不巧地遇到了。"
    window hide


    $ loadBG(2,"BG36E2")



    show screen phonebtn
    "我稍微探出头去看了一眼，发现黑衣人走过了我们所在的拉面屋，站在了我们进出的大楼前。"
    "在那里靠着扶手，开始使用手机。"
    "在那个位置的话，我们要是从大楼里出来就马上会被发现。"
    "而且……也有可能，他是在调查那个大楼。"
    "要是，走到２楼的走廊的话……"
    "从Ｌａｂ里伸出来的延长电缆就插在那里的插座上。"
    "桶子叔叔在那里出入过的事实绝对会暴露。"
    "不让他转移注意力的话。"
    $ stopvoc("DAR")
    play DAR "NAE06A_DAR0017"
    $ current_voice = "voice/NAE06A_DAR0017.ogg"
    "至" "「怎么办？」"
    "在我身后被我按着嘴巴的桶子叔叔朝我搭话。"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0015"
    $ current_voice = "voice/NAE06A_NAE0015.ogg"
    "绹" "「我去吸引他的注意，你赶紧去车站」"
    $ stopvoc("DAR")
    play DAR "NAE06A_DAR0018"
    $ current_voice = "voice/NAE06A_DAR0018.ogg"
    "至" "「Ｏｋａｙ　Ｄｏｋｅｙ」"
    "Ｏｋａｙ　Ｄｏｋｅｙ吗……"
    "听到这奇怪的说法，我想到的是。"
    hide screen phoneSD1
    window hide
    stop bgm 


    $ loadBG(0,"BG05A2")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_AMA02"),"True","lh/SUZ_AMA02a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    hide screen phonebtn
    $ stopvoc("SUZ")
    play SUZ "NAE06A_SUZ0000"
    $ current_voice = "voice/NAE06A_SUZ0000.ogg"
    "铃羽" "「 Ｏｋａｙ　Ｄｏｋｅｙ♪」"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0016"
    $ current_voice = "voice/NAE06A_NAE0016.ogg"
    "绹" "「…………」"
    "打工的，铃羽姐姐……"
    "虽然时间很短，但是我们交情不错。"
    "现在，她在哪里做着什么呢？"
    "结果，最后还是没让我骑她的自行车。"
    window hide


    window hide
    $ loadBG(0,"BG36E2")

    show screen phonebtn
    show screen phoneSD1
    play bgm "BGM07"
    "一边想着这种事，一边若无其事地走到了路上。"
    "那时刚好黑衣人打完了电话，就要进入大楼了。"
    "不行……！"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0017"
    $ current_voice = "voice/NAE06A_NAE0017.ogg"
    "绹" "「那，那个」"
    "赶紧和他搭话了。"
    "黑衣人把目光甩向我。"
    "我感觉自己紧张极了。"
    "心脏仿佛要从嘴巴里飞出来。"
    "但是，不做些什么的话……"
    "振作勇气，我朝黑衣人走去。"
    $ stopvoc("Y28")
    play KUR "NAE06A_Y280000"
    $ current_voice = "voice/NAE06A_Y280000.ogg"
    "黒服" "「……怎，怎么了啊你这家伙？」"
    "万一突然被捉住了该怎么办啊。"
    "万一突然被刺伤了该怎么办啊。"
    "膝盖颤抖着。"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0018"
    $ current_voice = "voice/NAE06A_NAE0018.ogg"
    "绹" "「那个……、之，之前也是，在这周围经常出现吧？」"
    $ stopvoc("Y28")
    play KUR "NAE06A_Y280001"
    $ current_voice = "voice/NAE06A_Y280001.ogg"
    "黒服" "「啊？」"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0019"
    $ current_voice = "voice/NAE06A_NAE0019.ogg"
    "绹" "「我在里面的大桧山大楼的前面看到过你，大概一个月之前吧。」"
    $ stopvoc("Y28")
    play KUR "NAE06A_Y280002"
    $ current_voice = "voice/NAE06A_Y280002.ogg"
    "黒服" "「肯定是认错人了」"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0020"
    $ current_voice = "voice/NAE06A_NAE0020.ogg"
    "绹" "「我，其实算是大桧山大楼的，主人吧」"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0021"
    $ current_voice = "voice/NAE06A_NAE0021.ogg"
    "绹" "「为什么，要一直在这边转悠呢？」"
    $ stopvoc("Y28")
    play KUR "NAE06A_Y280003"
    $ current_voice = "voice/NAE06A_Y280003.ogg"
    "黒服" "「…………」"
    "黑衣人一言不发。"
    $ stopvoc("Y28")
    play KUR "NAE06A_Y280004"
    $ current_voice = "voice/NAE06A_Y280004.ogg"
    "黒服" "「…………」"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0022"
    $ current_voice = "voice/NAE06A_NAE0022.ogg"
    "绹" "「…………」"
    "对话中断。"
    "不做些什么让对话继续下去的吧。"
    "不让他把注意力放在我身上的话。"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0023"
    $ current_voice = "voice/NAE06A_NAE0023.ogg"
    "绹" "「……你是我父亲的熟人吗？」"
    "偷偷地向拉面屋方向确认了一下。"
    "用余光看到了桶子叔叔正在蹑手蹑脚地朝着人行道走去。"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0024"
    $ current_voice = "voice/NAE06A_NAE0024.ogg"
    "绹" "「是来，给爸爸上坟的吗」"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0025"
    $ current_voice = "voice/NAE06A_NAE0025.ogg"
    "绹" "「那么，就拜托你处理一下墓碑的事吧」"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0026"
    $ current_voice = "voice/NAE06A_NAE0026.ogg"
    "绹" "「佛坛，现在也不在我这边」"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0027"
    $ current_voice = "voice/NAE06A_NAE0027.ogg"
    "绹" "「并不是被处理掉了。那种事，肯定不会做的。妈妈也好好地葬在佛坛里了」"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0028"
    $ current_voice = "voice/NAE06A_NAE0028.ogg"
    "绹" "「虽然爸爸他并不是对于宗教的事情很关心，但是果然，还是希望他能和妈妈葬在一起」"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0029"
    $ current_voice = "voice/NAE06A_NAE0029.ogg"
    "绹" "「但是，我现在留宿他家，再加上……」"
    $ stopvoc("Y28")
    play KUR "NAE06A_Y280005"
    $ current_voice = "voice/NAE06A_Y280005.ogg"
    "黒服" "「……不，不知道！」"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0030"
    $ current_voice = "voice/NAE06A_NAE0030.ogg"
    "绹" "「……！」"
    "突然，黑衣人将我一把推开，要走出去的样子。"
    "不行！"
    "如果朝那里走过去的话，就会看到桶子叔叔了！"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0031"
    $ current_voice = "voice/NAE06A_NAE0031.ogg"
    "绹" "「等，等等……！」"
    "脑海里一片空白。"
    "反应过来的时候，我已经站在黑衣人的面前了。"
    $ stopvoc("Y28")
    play KUR "NAE06A_Y280006"
    $ current_voice = "voice/NAE06A_Y280006.ogg"
    "黒服" "「……！」"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0032"
    $ current_voice = "voice/NAE06A_NAE0032.ogg"
    "绹" "「如果，和爸爸没有关系的话，请你，不要再来了……！」"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0033"
    $ current_voice = "voice/NAE06A_NAE0033.ogg"
    "绹" "「在这附近一直晃悠着的话，让我……很困扰……！」"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0034"
    $ current_voice = "voice/NAE06A_NAE0034.ogg"
    "绹" "「拜托了……！」"
    $ stopvoc("Y28")
    play KUR "NAE06A_Y280007"
    $ current_voice = "voice/NAE06A_Y280007.ogg"
    "黒服" "「你这小鬼！」"
    stop bgm 
    play se "SGSE340L" loop

    "这么说着，黑衣人的手机响了起来。"
    play se "SGSE158"


    stop se
    $ stopvoc("Y28")
    play KUR "NAE06A_Y280008"
    $ current_voice = "voice/NAE06A_Y280008.ogg"
    "黒服" "「好的……。是，是，明白了」"
    "黑衣人朝着电话的另一边回答着什么的样子。"
    $ stopvoc("Y28")
    play KUR "NAE06A_Y280009"
    $ current_voice = "voice/NAE06A_Y280009.ogg"
    "黒服" "「切……」"
    "朝着我啧了啧舌头，然后朝着反方向走了出去。"
    "这样的话，应该就不会撞见桶子叔叔了。"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0035"
    $ current_voice = "voice/NAE06A_NAE0035.ogg"
    "绹" "「…………」"
    "怎么，是不是有点做过头了。"
    "在哪里都看不到桶子叔叔的身影了。"
    window hide
    play se "SGSE056"


    $ loadBG(2,"BG_BLACK")



    hide screen phonebtn
    "一边确认着，一边在原地抱膝坐了下来。"
    "心还砰砰直跳。"
    "不知道深呼吸了几次。"
    window hide

    $ loadBG(0,"BG36E2")

    show screen phonebtn
    show screen phoneSD1
    hide screen phonebtn
    hide screen phonebtn2
    show screen phone(interact=False)
    "总之，先和桶子叔叔联系吧……"
    "如果能脱身的话，就用电话来取得联系，这是事前说好的。"
    "试着打了打桶子叔叔在离开Ｌａｂ前给我的号码。"
    window hide



    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0036"
    $ current_voice = "voice/NAE06A_NAE0036.ogg"
    "绹" "「……？」"
    "没有声音。"
    "普通的话，应该回想起嘟——的接通的声音。"
    "考虑了一下。"
    stop bgm 



    $ stopvoc("X05")
    play KUR "NAE06A_X050000"
    $ current_voice = "voice/NAE06A_X050000.ogg"
    "语音提示" "「您拨打的电话号码，目前无法接通。」"
    $ stopvoc("X05")
    play KUR "NAE06A_X050001"
    $ current_voice = "voice/NAE06A_X050001.ogg"
    "语音提示" "「请确认号码的正误后重新拨打」"

    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0037"
    $ current_voice = "voice/NAE06A_NAE0037.ogg"
    "绹" "「……诶」"
    "呼吸，仿佛要停止了一般。"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0038"
    $ current_voice = "voice/NAE06A_NAE0038.ogg"
    "绹" "「诶……呀？　诶呀？」"
    call hide_phone
    window hide


    $ loadBG(2,"IBGX033")



    hide screen phonebtn
    play bgm "FD2BGM04"
    "不管重拨几次。"
    "但是，每次总是无法接通。"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0039"
    $ current_voice = "voice/NAE06A_NAE0039.ogg"
    "绹" "「好奇怪啊……」"
    "难道说，虽然登录了，但是号码搞错了的话……"
    "唔，这种失误什么的。"
    "开始讨厌起自己了。"
    "怎么办啊。"
    "好歹我也告诉了桶子叔叔我的手机号码，那他也许会给我打电话吧。"
    "以防万一，是不是应该在Ｌａｂ等桶子叔叔回来啊。"
    window hide


    $ loadBG(2,"BG36E2")



    show screen phonebtn
    "甚至连那种想法都冒出来的时候，我突然一个激灵站了起来。"
    "环顾四周。"
    "车水马龙。"
    "就当我不存在一样，这么流过去。"
    "如果说——"
    "桶子叔叔就这么一去不回了该怎么办呢。"
    "桶子叔叔在发现４２寸显像管电视机坏掉的时候，就打退堂鼓了。"
    "是我说自己能修好才把他留下来的。"
    "但是，要是桶子叔叔不相信我说的话呢……？"
    "就像这样Ｄｕａｎｇ的一下就不见了呢……？"
    "就算如此，我也没有联系他的办法。"
    "没有任何手段。"
    "除了等待之外，并没有别的能做的事。"
    "就这么一个人，等待着一个不会回来的人——"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0040"
    $ current_voice = "voice/NAE06A_NAE0040.ogg"
    "绹" "「那种事……讨厌啊。」"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0041"
    $ current_voice = "voice/NAE06A_NAE0041.ogg"
    "绹" "「看到的世界……逐渐死去什么的。一切的颜色……都化为黑白什么的。」"
    hide screen phonebtn
    "不堪重负，我抱住了自己的身体。"
    "感觉仿佛要被这万钧的不安所压溃。"
    "难道说，又被置之不顾了吗。"
    "在不知道什么时候，不知何处，有什么事就这么结束了。"
    "在之后才知道这件事什么的。"
    "是那样的寂寞，悲伤，痛苦哦。"
    "当然，也不是说桶子叔叔一定就不会回来了。"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0042"
    $ current_voice = "voice/NAE06A_NAE0042.ogg"
    "绹" "「不找找看的话……」"
    "桶子叔叔应该还没有去很远的地方。"
    "一定，很快就能找到的。"
    window hide



    $ loadBG(0,"BG18E2")

    show screen phonebtn
    "快到傍晚了，路边来往的人多了起来。"
    "但是因为桶子叔叔很显眼，要是在路上走的话应该很容易发现才是……"
    window hide



    $ loadBG(0,"BG17A")

    "也去了之前躲起来过的零件店里面看了眼。"
    "并没有看到那样的身影，店员也说今天没有看到他。"
    window hide



    $ loadBG(0,"BG15E")

    "２年前的Ｌａｂｍｅｍ中，除了留未穗姐姐以外，还留在在这条街道里的，还有一个人。"
    "琉华姐姐。"
    "她的家在过了万世桥的柳林神社里。"
    "想着说不定会去找２年前的“Ｌａｂｍｅｍ”们，所以也去那里看了下。"
    "琉华姐姐去上学了，不在家里。问了她家里的人，也说并没有桶子叔叔那样的人来过。"
    window hide



    $ loadBG(0,"BG16N3")

    "太阳要下山了啊……"
    "还是，没有找到。"
    "束手无策。"
    "这么大的街区，光靠我一个人来找的话，根本是不可能的嘛……"
    "而且，这样找了一会没找到的话，桶子叔叔肯定是离这里更远了。"
    window hide



    $ loadBG(0,"BG79N5",at=[Transform(yalign=1.0)])






    "结果，天色暗下来的时候，又回到了这里。"
    "说不定桶子叔叔就突然回来了呢。我那么期待着。"
    "但是——"
    window hide



    $ loadBG(0,"BG02N3")


    $ targetmailid = 476

    $ LR_RM_CHANCE=1
    call CHECK_RM_RECEIVE

    call CHECK_RM_RECEIVE

    $ gd["RCVmailData"][gc["ScriptMacros"]["RM_NAE_RECV_RUK03_01"]]["late"]=True
    $ lml.append(gc["ScriptMacros"]["RM_NAE_RECV_RUK03_01"])

    "从厕所里偷偷地走了进去，但果然桶子叔叔也不在那里。"
    "不死心地打开了淋浴室看了一眼，但还是没有看到。"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0043"
    $ current_voice = "voice/NAE06A_NAE0043.ogg"
    "绹" "「…………」"
    "在沙发上弯下腰，疲劳就涌上来了。"
    "除了等待别无他法。"
    "桶子叔叔一定会回来的。"
    "只有那么相信着，等待下去……"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0044"
    $ current_voice = "voice/NAE06A_NAE0044.ogg"
    "绹" "「电焊铁的作业，不完成的话……」"
    "其实，已经到了必须回去的时间了。"
    "但是不想和桶子叔叔错过，所以不想回去。"
    "我强拖起因为东奔西走而疲惫不堪的身体，向楼下走去。"
    window hide


    $ loadBG(2,"BG_BLACK")



    hide screen phonebtn
    "但是，由于不安的压迫感，我有些无法集中注意力。"
    stop bgm 
    window hide

    $ loadBG(0,"BG04A4")






    show screen phonebtn
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0045"
    $ current_voice = "voice/NAE06A_NAE0045.ogg"
    "绹" "「……！」"

    "手机响了。"



    window hide
    hide screen phonebtn
    hide screen phonebtn2
    show screen phone(interact=False)

    "慌张地接起来。"





    play bgm "FD2BGM05"

    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0046"
    $ current_voice = "voice/NAE06A_NAE0046.ogg"
    "绹" "「喂喂！？」"

    $ stopvoc("FEI")
    play FEI "NAE06A_FEI0000"
    $ current_voice = "voice/NAE06A_FEI0000.ogg"
    "菲利斯姐姐" "「绹？　现在在哪里喵？　这么晚了还在外面闲逛是不行的喵」"

    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0047"
    $ current_voice = "voice/NAE06A_NAE0047.ogg"
    "绹" "「留未穂姐姐……」"

    $ stopvoc("FEI")
    play FEI "NAE06A_FEI0001"
    $ current_voice = "voice/NAE06A_FEI0001.ogg"
    "菲利斯姐姐" "「确实之前有和你说过，要再多玩一些的，但是也不能弄到这么晚啊」"
    $ stopvoc("FEI")
    play FEI "NAE06A_FEI0002"
    $ current_voice = "voice/NAE06A_FEI0002.ogg"
    "菲利斯姐姐" "「已经是中学生了，要学会好好判断回来的时间」"

    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0048"
    $ current_voice = "voice/NAE06A_NAE0048.ogg"
    "绹" "「比起那个，桶子叔叔有联系你吗！？」"

    $ stopvoc("FEI")
    play FEI "NAE06A_FEI0003"
    $ current_voice = "voice/NAE06A_FEI0003.ogg"
    "菲利斯姐姐" "「喵？　桶喵？」"
    $ stopvoc("FEI")
    play FEI "NAE06A_FEI0004"
    $ current_voice = "voice/NAE06A_FEI0004.ogg"
    "菲利斯姐姐" "「说起来之前也是，绹对于桶子叔叔也有所提及呢。为什么会这么在意？」"
    $ stopvoc("FEI")
    play FEI "NAE06A_FEI0005"
    $ current_voice = "voice/NAE06A_FEI0005.ogg"
    "菲利斯姐姐" "「……难道说，和桶子喵在一起？」"

    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0049"
    $ current_voice = "voice/NAE06A_NAE0049.ogg"
    "绹" "「……不」"
    "并不在一起。"
    "桶子叔叔，并没有回来。"

    $ stopvoc("FEI")
    play FEI "NAE06A_FEI0006"
    $ current_voice = "voice/NAE06A_FEI0006.ogg"
    "菲利斯姐姐" "「总之，今天先回来吧。爸爸妈妈都很担心」"

    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0050"
    $ current_voice = "voice/NAE06A_NAE0050.ogg"
    "绹" "「明白了……不好意思」"
    window hide
    call hide_phone


    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0051"
    $ current_voice = "voice/NAE06A_NAE0051.ogg"
    "绹" "「…………」"
    "什么也做不到。"
    "小孩子自己不管有多么重要的事情，要是很晚还留在外面的话，就会惹大人生气。"
    "就算是孩子晚上也想出去什么的，并不是那么一回事。"
    "我对于自己一个人找不到他这一点十分的焦躁。"
    window hide



    $ loadBG(0,"BG16N3")

    "人们正从秋叶原中撤退出去。"
    "哪儿的店都已经到了打烊的时间。"
    "因为好多连卷闸门都放下来了，人行道有些昏暗。"
    "我连走回家的时候都一直在找着桶子叔叔。"
    "努力看清擦身而过的男人的脸。"
    "但是，没找到。"
    "哪里都。"
    "没能找到……"
    window hide


    $ loadBG(2,"BG23N")



    "走到ＵＰＸ楼下的时候。"
    stop bgm 
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0052"
    $ current_voice = "voice/NAE06A_NAE0052.ogg"
    "绹" "「啊……」"
    play bgm "FD2BGM08"
    "在人影渐稀的秋叶原中。"
    "没有其他人的开放式咖啡厅的桌子边。"
    "坐着的庞大身躯。"
    "一看侧影就明白了。"
    "应该没有看错。"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0053"
    $ current_voice = "voice/NAE06A_NAE0053.ogg"
    "绹" "「桶子叔叔……！」"
    "自然地朝他那边跑去。"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CSA01"),"True","lh/DAR_CSA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "NAE06A_DAR0019"
    $ current_voice = "voice/NAE06A_DAR0019.ogg"
    "至" "「恩？　哦哦，绹酱氏」"
    "明明我这边这么拼命地在找他，桶子叔叔却毫无愧疚之意地和我打了招呼。"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0054"
    $ current_voice = "voice/NAE06A_NAE0054.ogg"
    "绹" "「为，为什么，不和我联系？明明一直，在找你的啊……」"
    "说到一半的时候，注意到了。"
    "桶子叔叔边上，还有一个人。"
    "没有见过。"
    "也不是“Ｌａｂｍｅｍ”。"
    "穿着笔挺的西装，就好像一个公务员一样的很厉害的人。但是，也没有感觉比桶子叔叔要老很多。"
    "目光锐利，总感觉有些像蛇一样。"
    "在他的手里，有银行的信封。"
    "这个人，是谁啊？"
    "是和桶子叔叔出门之前打电话的人吗？　看这个氛围感觉又有点不太像。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CSB01"),"True","lh/DAR_CSB01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "NAE06A_DAR0020"
    $ current_voice = "voice/NAE06A_DAR0020.ogg"
    "至" "「那，就是这么一回事。」"
    "桶子叔叔好像结束了话题，于是那个像蛇一样的人无言地将信封递给了桶子叔叔。"
    "就那么站了起来，看了一眼我之后，小小地点了点头离开了。"
    $ stopvoc("DAR")
    play DAR "NAE06A_DAR0021"
    $ current_voice = "voice/NAE06A_DAR0021.ogg"
    "至" "「接下来是，Ｃｏｍｉｃ　Ｅｌｏ！要好好地搞到手啊」"
    "就算桶子叔叔这么大声喊了，那个蛇一样的人也没有回头，朝着车站方向消失了。"
    "一句话也不愿意说。"
    "总感觉有些不快。"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0055"
    $ current_voice = "voice/NAE06A_NAE0055.ogg"
    "绹" "「那个……、刚才的人是……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CSA01"),"True","lh/DAR_CSA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "NAE06A_DAR0022"
    $ current_voice = "voice/NAE06A_DAR0022.ogg"
    "至" "「恩，协力者那样的家伙吧？」"
    "协力者……？"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    "桶子叔叔没有继续说下去，缓缓地站了起来。"
    window hide


    $ loadBG(2,"BG20N")



    "一边环顾四周，一边好像当我不存在一样走了起来。"
    "因为被黑衣人追着所以动作要快这一点我是明白的啦……"
    "但是，这样好像无视我的行为，让我很受伤。"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0056"
    $ current_voice = "voice/NAE06A_NAE0056.ogg"
    "绹" "「可以的话，希望，能联系我」"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0057"
    $ current_voice = "voice/NAE06A_NAE0057.ogg"
    "绹" "「说过要打电话来汇合的吧？」"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0058"
    $ current_voice = "voice/NAE06A_NAE0058.ogg"
    "绹" "「我刚才找了差不多两个小时都没有找到你，所以只好在Ｌａｂ等着了。」"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0059"
    $ current_voice = "voice/NAE06A_NAE0059.ogg"
    "绹" "「我没有能联系到你，真的很抱歉。」"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0060"
    $ current_voice = "voice/NAE06A_NAE0060.ogg"
    "绹" "「手机里的联系方式，号码好像有问题……」"
    $ stopvoc("DAR")
    play DAR "NAE06A_DAR0023"
    $ current_voice = "voice/NAE06A_DAR0023.ogg"
    "至" "「……诶？　怎么会？　哪个？」"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CMA01"),"True","lh/DAR_CMA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide screen phonebtn
    "桶子叔叔凑过来看我的手机。"
    "我给他看了电话号码。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CMA03"),"True","lh/DAR_CMA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    show screen phonebtn
    $ stopvoc("DAR")
    play DAR "NAE06A_DAR0024"
    $ current_voice = "voice/NAE06A_DAR0024.ogg"
    "至" "「啊，抱歉抱歉。那是因为我告诉你的号码是错的。」"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0061"
    $ current_voice = "voice/NAE06A_NAE0061.ogg"
    "绹" "「诶……？」"
    $ stopvoc("DAR")
    play DAR "NAE06A_DAR0025"
    $ current_voice = "voice/NAE06A_DAR0025.ogg"
    "至" "「那个，最近手机号码换得比较勤，自己也没能记住到底在用哪个。」"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0062"
    $ current_voice = "voice/NAE06A_NAE0062.ogg"
    "绹" "「…………」"
    "为什么……"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CMA02"),"True","lh/DAR_CMA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "NAE06A_DAR0026"
    $ current_voice = "voice/NAE06A_DAR0026.ogg"
    "至" "「抱歉鸟。啊，要是你说无法原谅我的话，也可以从后面狠狠地踹我几脚哦。不用在意请便」"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0063"
    $ current_voice = "voice/NAE06A_NAE0063.ogg"
    "绹" "「为什么，你会那么轻描淡写啊……？」"
    "这样的话语脱口而出。"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    "桶子叔叔是没有注意到我的低语嘛，一边走着一边开始看起了信封里的内容。"
    "看到那个，我震惊了。"
    "大捆的钞票。"
    "１万元的纸币，有好几百张……"
    "在漫画或者电视剧之外没有见过的巨款。"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0064"
    $ current_voice = "voice/NAE06A_NAE0064.ogg"
    "绹" "「那是……」"
    $ stopvoc("DAR")
    play DAR "NAE06A_DAR0027"
    $ current_voice = "voice/NAE06A_DAR0027.ogg"
    "至" "「是在中野区当土豪用的资金哦」（注：中野区是东京的一个区）"
    "中野……？"
    $ stopvoc("DAR")
    play DAR "NAE06A_DAR0028"
    $ current_voice = "voice/NAE06A_DAR0028.ogg"
    "至" "「果然啊，没有文化的人都是腐着的吧？啊，这里的腐可不是腐女的意思哦」"
    $ stopvoc("DAR")
    play DAR "NAE06A_DAR0029"
    $ current_voice = "voice/NAE06A_DAR0029.ogg"
    "至" "「总而言之就是说我快要忍不住了。现在不是制作电话微波炉的时候」"
    $ stopvoc("DAR")
    play DAR "NAE06A_DAR0030"
    $ current_voice = "voice/NAE06A_DAR0030.ogg"
    "至" "「总而言之最近２年完全无法入手的新作以及工口同人，还有动画全集什么的，我都超想要试一遍啊」"
    $ stopvoc("DAR")
    play DAR "NAE06A_DAR0031"
    $ current_voice = "voice/NAE06A_DAR0031.ogg"
    "至" "「但是钱完全不够吧？所以就这样让协力者来帮我解决这个问题」"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0065"
    $ current_voice = "voice/NAE06A_NAE0065.ogg"
    "绹" "「为了这种事……」"
    $ stopvoc("DAR")
    play DAR "NAE06A_DAR0032"
    $ current_voice = "voice/NAE06A_DAR0032.ogg"
    "至" "「是是。今天出门就是为了这个哦」"
    "为了这种事情……"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0066"
    $ current_voice = "voice/NAE06A_NAE0066.ogg"
    "绹" "「为什么……」"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CSA01"),"True","lh/DAR_CSA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "NAE06A_DAR0033"
    $ current_voice = "voice/NAE06A_DAR0033.ogg"
    "至" "「啊，绹酱氏绹酱氏，你能不能拿着这把钞票朝我的脸上拍几下？好想试一次的说──」"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0067"
    $ current_voice = "voice/NAE06A_NAE0067.ogg"
    "绹" "「为什么！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CSA04"),"True","lh/DAR_CSA04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "NAE06A_DAR0034"
    $ current_voice = "voice/NAE06A_DAR0034.ogg"
    "至" "「诶？」"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0068"
    $ current_voice = "voice/NAE06A_NAE0068.ogg"
    "绹" "「为什么，要开玩笑！？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CSA02"),"True","lh/DAR_CSA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0069"
    $ current_voice = "voice/NAE06A_NAE0069.ogg"
    "绹" "「为什么……！」"
    "视线模糊了。"
    "不想要自己露出困扰的表情。"
    "注意到的时候，眼泪已经流出来了。"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0070"
    $ current_voice = "voice/NAE06A_NAE0070.ogg"
    "绹" "「不是哦，我明白你不想告诉我的……」"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0071"
    $ current_voice = "voice/NAE06A_NAE0071.ogg"
    "绹" "「我明白的哦……」"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0072"
    $ current_voice = "voice/NAE06A_NAE0072.ogg"
    "绹" "「对于桶子叔叔来说，我是怎样都好的存在……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CSB03"),"True","lh/DAR_CSB03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "NAE06A_DAR0035"
    $ current_voice = "voice/NAE06A_DAR0035.ogg"
    "至" "「等……」"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0073"
    $ current_voice = "voice/NAE06A_NAE0073.ogg"
    "绹" "「并不是伙伴，也不是“Ｌａｂｍｅｍ”」"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0074"
    $ current_voice = "voice/NAE06A_NAE0074.ogg"
    "绹" "「只是一个外人。只是一个，认识的熟人而已……」"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0075"
    $ current_voice = "voice/NAE06A_NAE0075.ogg"
    "绹" "「但是！　我并不是因为喜欢才成为“熟人”的！」"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0076"
    $ current_voice = "voice/NAE06A_NAE0076.ogg"
    "绹" "「明明已经不想再一个人等待不会回来的人了！」"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0077"
    $ current_voice = "voice/NAE06A_NAE0077.ogg"
    "绹" "「我明明是想成为当事人的！」"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0078"
    $ current_voice = "voice/NAE06A_NAE0078.ogg"
    "绹" "「然而……」"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0079"
    $ current_voice = "voice/NAE06A_NAE0079.ogg"
    "绹" "「连和我认真的说话这么简单的事，都做不到吗……」"
    $ stopvoc("DAR")
    play DAR "NAE06A_DAR0036"
    $ current_voice = "voice/NAE06A_DAR0036.ogg"
    "至" "「那个……」"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0080"
    $ current_voice = "voice/NAE06A_NAE0080.ogg"
    "绹" "「已经够了……」"
    "我用手背擦掉了眼泪。"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0081"
    $ current_voice = "voice/NAE06A_NAE0081.ogg"
    "绹" "「我，已经，不会去爸爸的大楼了……」"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0082"
    $ current_voice = "voice/NAE06A_NAE0082.ogg"
    "绹" "「感觉去了也只是帮倒忙，还是算了……」"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0083"
    $ current_voice = "voice/NAE06A_NAE0083.ogg"
    "绹" "「所以，不管去哪里也都无所谓了」"
    "把能说的都说了。"
    window hide


    $ loadBG(2,"IBGX072")



    hide screen phonebtn
    play se "SGSE181"
    "我背过身去，从桶子叔叔的身边跑开了。"
    "一次也没有朝着桶子叔叔的方向回头。"
    hide screen phoneSD1
    window hide



    $ loadBG(0,"BG26N")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_HSA03"),"True","lh/FEI_HSA03a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    stop se

    stop se


    show screen phonebtn
    show screen phoneSD1
    $ stopvoc("FEI")
    play FEI "NAE06A_FEI0007"
    $ current_voice = "voice/NAE06A_FEI0007.ogg"
    "菲利斯" "「啊，绹。好慢喵。让我好担心啊──」"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0084"
    $ current_voice = "voice/NAE06A_NAE0084.ogg"
    "绹" "「非常抱歉……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_HSC04"),"True","lh/FEI_HSC04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FEI")
    play FEI "NAE06A_FEI0008"
    $ current_voice = "voice/NAE06A_FEI0008.ogg"
    "菲利斯" "「诶，绹……？」"
    "我躲避着留未穗姐姐的视线，跑回了自己的房间。"
    window hide



    $ loadBG(0,"BG73N2")

    hide screen phonebtn
    play bgm "FD2BGM04"
    "进了房间后，在床的角落里抱成了一团。"
    "已经累了。"
    "这一周里，因为桶子叔叔的事和考试的事，我都没能好好睡觉。"
    "明天就不去上课了，好好睡一觉吧……"
    "然后再一次的，回到每天的日常吧。"
    "回到和秋叶家的人一起度过的每一天吧。"
    "那才是，１３岁的天王寺绹应该有的生活。"
    "那样奇葩的人还是少打交道为好。"
    "应该那样做的。"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0085"
    $ current_voice = "voice/NAE06A_NAE0085.ogg"
    "绹" "「……呜」"
    "想了想今天的事情，眼泪又要流出来了。"
    hide screen phoneSD1
    window hide


    $ loadBG(2,"BG_BLACK")



    hide screen phonebtn
    "所以，赶紧把脸埋进了膝盖。"
    window hide
    play se "SGSE335"

    $ stopvoc("FEI")
    play FEI "NAE06A_FEI0009"
    $ current_voice = "voice/NAE06A_FEI0009.ogg"
    "菲利斯" "「绹？　我进来了哦？」"
    play se "SGSE336"
    "明明我没说可以进来，留未穗姐姐就那么进了我的房间，在我的身边弯下了腰。"
    window hide
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_NAE004A"]]["Check"]=True


    $ loadBG(2,"EV_NAE004A")



    $ stopvoc("FEI")
    play FEI "NAE06A_FEI0010"
    $ current_voice = "voice/NAE06A_FEI0010.ogg"
    "菲利斯" "「怎么了？　发生了什么吗？」"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0086"
    $ current_voice = "voice/NAE06A_NAE0086.ogg"
    "绹" "「…………」"
    "保持着低头的状态摇了摇头。"
    "但是。"
    $ stopvoc("FEI")
    play FEI "NAE06A_FEI0011"
    $ current_voice = "voice/NAE06A_FEI0011.ogg"
    "菲利斯" "「骗人，明明刚才还在哭」"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0087"
    $ current_voice = "voice/NAE06A_NAE0087.ogg"
    "绹" "「……没有哭过」"
    $ stopvoc("FEI")
    play FEI "NAE06A_FEI0012"
    $ current_voice = "voice/NAE06A_FEI0012.ogg"
    "菲利斯" "「哭过的啊」"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0088"
    $ current_voice = "voice/NAE06A_NAE0088.ogg"
    "绹" "「才没有」"
    $ stopvoc("FEI")
    play FEI "NAE06A_FEI0013"
    $ current_voice = "voice/NAE06A_FEI0013.ogg"
    "菲利斯" "「那，抬起头来看看？」"
    "当然不能抬头。"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0089"
    $ current_voice = "voice/NAE06A_NAE0089.ogg"
    "绹" "「留未穗姐姐平时的喵喵语呢……？」"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0090"
    $ current_voice = "voice/NAE06A_NAE0090.ogg"
    "绹" "「姐姐不说那个的话，就不是姐姐了呢」"
    $ stopvoc("FEI")
    play FEI "NAE06A_FEI0014"
    $ current_voice = "voice/NAE06A_FEI0014.ogg"
    "菲利斯" "「…………」"
    $ stopvoc("FEI")
    play FEI "NAE06A_FEI0015"
    $ current_voice = "voice/NAE06A_FEI0015.ogg"
    "菲利斯" "「还记得吗？我最初找到绹的时候，你也是这么哭着的哦」"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0091"
    $ current_voice = "voice/NAE06A_NAE0091.ogg"
    "绹" "「…………」"
    $ stopvoc("FEI")
    play FEI "NAE06A_FEI0016"
    $ current_voice = "voice/NAE06A_FEI0016.ogg"
    "菲利斯" "「要和我一起吗？」"
    $ stopvoc("FEI")
    play FEI "NAE06A_FEI0017"
    $ current_voice = "voice/NAE06A_FEI0017.ogg"
    "菲利斯" "「和我，住在一起」"
    $ stopvoc("FEI")
    play FEI "NAE06A_FEI0018"
    $ current_voice = "voice/NAE06A_FEI0018.ogg"
    "菲利斯" "「像那个时候一样，拜托我也可以哦？」"
    $ stopvoc("FEI")
    play FEI "NAE06A_FEI0019"
    $ current_voice = "voice/NAE06A_FEI0019.ogg"
    "菲利斯" "「就算再怎么辛苦，再怎么难受，都可以和我说哦？」"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0092"
    $ current_voice = "voice/NAE06A_NAE0092.ogg"
    "绹" "「…………」"
    window hide
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_NAE004B"]]["Check"]=True


    $ loadBG(2,"EV_NAE004B")



    "留未穗姐姐轻轻地摸着我的头。"
    "把肩膀借给我靠。我感到了一丝温暖。"
    "她这么做了之后，我再也没能忍住眼泪，哭了出来。"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0093"
    $ current_voice = "voice/NAE06A_NAE0093.ogg"
    "绹" "「留未穂姐姐……」"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0094"
    $ current_voice = "voice/NAE06A_NAE0094.ogg"
    "绹" "「我想……成为，当事者啊……」"
    $ stopvoc("FEI")
    play FEI "NAE06A_FEI0020"
    $ current_voice = "voice/NAE06A_FEI0020.ogg"
    "菲利斯" "「当事者……？」"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0095"
    $ current_voice = "voice/NAE06A_NAE0095.ogg"
    "绹" "「上周的时候，我找到了桶子叔叔……」"
    $ stopvoc("FEI")
    play FEI "NAE06A_FEI0021"
    $ current_voice = "voice/NAE06A_FEI0021.ogg"
    "菲利斯" "「……！」"
    $ stopvoc("FEI")
    play FEI "NAE06A_FEI0022"
    $ current_voice = "voice/NAE06A_FEI0022.ogg"
    "菲利斯" "「是吗。难怪最近经常问他的事情啊」"
    "我点点头，将这一周之间发生的事情，都告诉了留未穗姐姐，中间忍不住停下来哭了好几次。"
    "那个时候，姐姐就会温柔地抚摸着我的后背。"

    stop bgm 
    "多亏了那份温暖，在说完的时候，我也总算是冷静下来了。"
    window hide
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_NAE004C"]]["Check"]=True


    $ loadBG(2,"EV_NAE004C")



    play bgm "FD2BGM05"
    $ stopvoc("FEI")
    play FEI "NAE06A_FEI0023"
    $ current_voice = "voice/NAE06A_FEI0023.ogg"
    "菲利斯" "「未来道具研究所的活动，吗……」"
    $ stopvoc("FEI")
    play FEI "NAE06A_FEI0024"
    $ current_voice = "voice/NAE06A_FEI0024.ogg"
    "菲利斯" "「在做那种事情呢」"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0096"
    $ current_voice = "voice/NAE06A_NAE0096.ogg"
    "绹" "「我明明是那么用尽全力地在做……果然，桶子叔叔还是不相信我吗」"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0097"
    $ current_voice = "voice/NAE06A_NAE0097.ogg"
    "绹" "「当然，桶子叔叔和我在２年前也不是朋友就是了……」"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0098"
    $ current_voice = "voice/NAE06A_NAE0098.ogg"
    "绹" "「因为我还只是中学生，我也知道我是不那么可靠的……」"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0099"
    $ current_voice = "voice/NAE06A_NAE0099.ogg"
    "绹" "「但果然还是不想自己孤零零一个人啊……」"
    $ stopvoc("FEI")
    play FEI "NAE06A_FEI0025"
    $ current_voice = "voice/NAE06A_FEI0025.ogg"
    "菲利斯" "「…………」"
    $ stopvoc("FEI")
    play FEI "NAE06A_FEI0026"
    $ current_voice = "voice/NAE06A_FEI0026.ogg"
    "菲利斯" "「被扔到一边不管的，不止只有绹酱一个人哦」"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0100"
    $ current_voice = "voice/NAE06A_NAE0100.ogg"
    "绹" "「诶……？」"
    "听到了这意外的话语，我看向了留未穗姐姐。"
    "她的脸上带着微笑。"
    "但是……看起来，非常的寂寞……"
    $ stopvoc("FEI")
    play FEI "NAE06A_FEI0027"
    $ current_voice = "voice/NAE06A_FEI0027.ogg"
    "菲利斯" "「因为我也被抛下了呢」"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0101"
    $ current_voice = "voice/NAE06A_NAE0101.ogg"
    "绹" "「啊……」"
    "是这样……呢。"
    "留未穗姐姐也是“Ｌａｂｍｅｍ”中的一员。"
    "和同伴们之间的情谊，应该比我要深得多。"
    "就算如此，现在也只是在秋叶原生活着。"
    "并没有消失。"
    "而且……桶子叔叔回到了秋叶原这件事，也是刚刚听我说了才知道的。"
    "……从桶子叔叔或者冈伦叔叔那里，什么消息也没有听到。"
    $ stopvoc("FEI")
    play FEI "NAE06A_FEI0028"
    $ current_voice = "voice/NAE06A_FEI0028.ogg"
    "菲利斯" "「绹是为什么会想成为当事者的呢？」"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0102"
    $ current_voice = "voice/NAE06A_NAE0102.ogg"
    "绹" "「…………」"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0103"
    $ current_voice = "voice/NAE06A_NAE0103.ogg"
    "绹" "「不想再被抛下了」"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0104"
    $ current_voice = "voice/NAE06A_NAE0104.ogg"
    "绹" "「就算是留未穗姐姐，被大家抛下的时候，也会很伤心吧？」"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0105"
    $ current_voice = "voice/NAE06A_NAE0105.ogg"
    "绹" "「我，非常的难受……」"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0106"
    $ current_voice = "voice/NAE06A_NAE0106.ogg"
    "绹" "「自己什么也不知道」"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0107"
    $ current_voice = "voice/NAE06A_NAE0107.ogg"
    "绹" "「谁都没有告诉我」"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0108"
    $ current_voice = "voice/NAE06A_NAE0108.ogg"
    "绹" "「爸爸也好，谁也好，都不曾信任过我」"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0109"
    $ current_voice = "voice/NAE06A_NAE0109.ogg"
    "绹" "「我讨厌被这样对待的自己……」"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0110"
    $ current_voice = "voice/NAE06A_NAE0110.ogg"
    "绹" "「如果我能做的更好，能更成熟一点的话……就不会被抛下不管了，我现在还是这么觉得的……」"
    $ stopvoc("FEI")
    play FEI "NAE06A_FEI0029"
    $ current_voice = "voice/NAE06A_FEI0029.ogg"
    "菲利斯" "「不对哦，绹」"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0111"
    $ current_voice = "voice/NAE06A_NAE0111.ogg"
    "绹" "「诶……？」"
    $ stopvoc("FEI")
    play FEI "NAE06A_FEI0030"
    $ current_voice = "voice/NAE06A_FEI0030.ogg"
    "菲利斯" "「什么也没有告诉绹这一点，并不是不信任绹哦──」"
    $ stopvoc("FEI")
    play FEI "NAE06A_FEI0031"
    $ current_voice = "voice/NAE06A_FEI0031.ogg"
    "菲利斯" "「而是大家在守护着绹的证据哦」"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0112"
    $ current_voice = "voice/NAE06A_NAE0112.ogg"
    "绹" "「守护着……我……？」"
    $ stopvoc("FEI")
    play FEI "NAE06A_FEI0032"
    $ current_voice = "voice/NAE06A_FEI0032.ogg"
    "菲利斯" "「多多少少，我觉得绹的爸爸，也是因为想要守护绹才死去的」"
    $ stopvoc("FEI")
    play FEI "NAE06A_FEI0033"
    $ current_voice = "voice/NAE06A_FEI0033.ogg"
    "菲利斯" "「２年前──」"
    $ stopvoc("FEI")
    play FEI "NAE06A_FEI0034"
    $ current_voice = "voice/NAE06A_FEI0034.ogg"
    "菲利斯" "「你的父亲，在那一天——结束了自己的生命的那一天，曾经来过我爸爸这儿哦」"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0113"
    $ current_voice = "voice/NAE06A_NAE0113.ogg"
    "绹" "「诶……」"
    $ stopvoc("FEI")
    play FEI "NAE06A_FEI0035"
    $ current_voice = "voice/NAE06A_FEI0035.ogg"
    "菲利斯" "「虽然我不在那里，不知道到底说了些什么」"
    $ stopvoc("FEI")
    play FEI "NAE06A_FEI0036"
    $ current_voice = "voice/NAE06A_FEI0036.ogg"
    "菲利斯" "「但是爸爸说，他说了类似于“绹的事情就拜托了。我只担心绹的事情”之类的话」"
    $ stopvoc("FEI")
    play FEI "NAE06A_FEI0037"
    $ current_voice = "voice/NAE06A_FEI0037.ogg"
    "菲利斯" "「你的爸爸好像在被谁追着的样子。」"
    $ stopvoc("FEI")
    play FEI "NAE06A_FEI0038"
    $ current_voice = "voice/NAE06A_FEI0038.ogg"
    "菲利斯" "「所以一定是为了不希望你被卷入事件，才这么做的……」"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0114"
    $ current_voice = "voice/NAE06A_NAE0114.ogg"
    "绹" "「…………」"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0115"
    $ current_voice = "voice/NAE06A_NAE0115.ogg"
    "绹" "「那样真是，自作主张呢」"
    $ stopvoc("FEI")
    play FEI "NAE06A_FEI0039"
    $ current_voice = "voice/NAE06A_FEI0039.ogg"
    "菲利斯" "「天下父母皆如此。爸爸是这么说的」"
    $ stopvoc("FEI")
    play FEI "NAE06A_FEI0040"
    $ current_voice = "voice/NAE06A_FEI0040.ogg"
    "菲利斯" "「为了让自己的孩子不陷入危险，什么事都能做得出来」"
    $ stopvoc("FEI")
    play FEI "NAE06A_FEI0041"
    $ current_voice = "voice/NAE06A_FEI0041.ogg"
    "菲利斯" "「而且……朋友也是」"
    "留未穗姐姐说到这里，露出了一个寂寞的笑容。"
    $ stopvoc("FEI")
    play FEI "NAE06A_FEI0042"
    $ current_voice = "voice/NAE06A_FEI0042.ogg"
    "菲利斯" "「为了让自己重要的朋友不陷入危险的事件，所以就隐瞒事实，撒一些温柔的谎言」"
    $ stopvoc("FEI")
    play FEI "NAE06A_FEI0043"
    $ current_voice = "voice/NAE06A_FEI0043.ogg"
    "菲利斯" "「能有这样的朋友，真是非常的幸福」"
    "留未穗姐姐应该也是这么理解“Ｌａｂｍｅｍ”的各位的消失的吧。"
    $ stopvoc("FEI")
    play FEI "NAE06A_FEI0044"
    $ current_voice = "voice/NAE06A_FEI0044.ogg"
    "菲利斯" "「我现在还是认为，２年前没有成为当事人，真是太好了」"
    $ stopvoc("FEI")
    play FEI "NAE06A_FEI0045"
    $ current_voice = "voice/NAE06A_FEI0045.ogg"
    "菲利斯" "「那个时候，虽然注意到了“凶真”的状态非常的奇怪」"
    "凶真……冈伦叔叔的一个奇怪的名字。"
    $ stopvoc("FEI")
    play FEI "NAE06A_FEI0046"
    $ current_voice = "voice/NAE06A_FEI0046.ogg"
    "菲利斯" "「如果我和他处于相同的立场的话，大概心已经死了吧」"
    $ stopvoc("FEI")
    play FEI "NAE06A_FEI0047"
    $ current_voice = "voice/NAE06A_FEI0047.ogg"
    "菲利斯" "「我十分感谢守护了我的大家」"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0116"
    $ current_voice = "voice/NAE06A_NAE0116.ogg"
    "绹" "「明明还露出一副寂寞的表情」"
    $ stopvoc("FEI")
    play FEI "NAE06A_FEI0048"
    $ current_voice = "voice/NAE06A_FEI0048.ogg"
    "菲利斯" "「在我的心中，感谢与寂寞的感情并不矛盾」"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0117"
    $ current_voice = "voice/NAE06A_NAE0117.ogg"
    "绹" "「为什么？」"
    "那是为什么呢，无法理解"
    $ stopvoc("FEI")
    play FEI "NAE06A_FEI0049"
    $ current_voice = "voice/NAE06A_FEI0049.ogg"
    "菲利斯" "「感到寂寞，胸口的深处会隐隐作痛是因为──」"
    $ stopvoc("FEI")
    play FEI "NAE06A_FEI0050"
    $ current_voice = "voice/NAE06A_FEI0050.ogg"
    "菲利斯" "「将关于那个人的记忆，深深地刻在了自己的内心最深处啊」"
    $ stopvoc("FEI")
    play FEI "NAE06A_FEI0051"
    $ current_voice = "voice/NAE06A_FEI0051.ogg"
    "菲利斯" "「在内心的这块画布上，用无法抹去的铅笔，留下了一生难忘的伤痕」"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0118"
    $ current_voice = "voice/NAE06A_NAE0118.ogg"
    "绹" "「我的心里也是这样吗？」"
    $ stopvoc("FEI")
    play FEI "NAE06A_FEI0052"
    $ current_voice = "voice/NAE06A_FEI0052.ogg"
    "菲利斯" "「是啊。那伤口呢，总有一天会结痂愈合，然后开出美丽的花朵哦」"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0119"
    $ current_voice = "voice/NAE06A_NAE0119.ogg"
    "绹" "「如果愈合的话，就不会开花了呢……」"
    $ stopvoc("FEI")
    play FEI "NAE06A_FEI0053"
    $ current_voice = "voice/NAE06A_FEI0053.ogg"
    "菲利斯" "「真的吗？绹没有见过？」"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0120"
    $ current_voice = "voice/NAE06A_NAE0120.ogg"
    "绹" "「没有……」"
    $ stopvoc("FEI")
    play FEI "NAE06A_FEI0054"
    $ current_voice = "voice/NAE06A_FEI0054.ogg"
    "菲利斯" "「我有过呢。感觉是有过的。也许是在梦里也说不定」"
    $ stopvoc("FEI")
    play FEI "NAE06A_FEI0055"
    $ current_voice = "voice/NAE06A_FEI0055.ogg"
    "菲利斯" "「绹的心里，肯定也会开着花的吧」"
    $ stopvoc("FEI")
    play FEI "NAE06A_FEI0056"
    $ current_voice = "voice/NAE06A_FEI0056.ogg"
    "菲利斯" "「直到那样之前，就感受着这份寂寞，舔舐着这伤口──」"
    $ stopvoc("FEI")
    play FEI "NAE06A_FEI0057"
    $ current_voice = "voice/NAE06A_FEI0057.ogg"
    "菲利斯" "「同时，心怀感激地来迎接每一天」"
    $ stopvoc("FEI")
    play FEI "NAE06A_FEI0058"
    $ current_voice = "voice/NAE06A_FEI0058.ogg"
    "菲利斯" "「这样做的话，就好像绹与桶喵再次相遇那样，总有一天会在那里突然再相遇也说不定吧？」"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0121"
    $ current_voice = "voice/NAE06A_NAE0121.ogg"
    "绹" "「连已经去天国的爸爸，也遇得到吗？」"
    $ stopvoc("FEI")
    play FEI "NAE06A_FEI0059"
    $ current_voice = "voice/NAE06A_FEI0059.ogg"
    "菲利斯" "「能遇到哦。肯定的」"
    "留未穗姐姐看着我的脸，坚定地说道。"
    $ stopvoc("FEI")
    play FEI "NAE06A_FEI0060"
    $ current_voice = "voice/NAE06A_FEI0060.ogg"
    "菲利斯" "「怎么样？你觉得我的眼睛像是在撒谎的样子吗？」"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0122"
    $ current_voice = "voice/NAE06A_NAE0122.ogg"
    "绹" "「……恩。留未穗姐姐，在说谎。」"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0123"
    $ current_voice = "voice/NAE06A_NAE0123.ogg"
    "绹" "「但是……」"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0124"
    $ current_voice = "voice/NAE06A_NAE0124.ogg"
    "绹" "「是温柔的，谎言呢。」"
    $ stopvoc("FEI")
    play FEI "NAE06A_FEI0061"
    $ current_voice = "voice/NAE06A_FEI0061.ogg"
    "菲利斯" "「是吧？」"
    $ stopvoc("FEI")
    play FEI "NAE06A_FEI0062"
    $ current_voice = "voice/NAE06A_FEI0062.ogg"
    "菲利斯" "「桶喵也肯定，是在撒谎吧」"
    $ stopvoc("FEI")
    play FEI "NAE06A_FEI0063"
    $ current_voice = "voice/NAE06A_FEI0063.ogg"
    "菲利斯" "「男人的谎言都很容易识破，所以我只是听了绹的话就明白了哦」"
    "留未穗姐姐坏笑起来。"
    $ stopvoc("FEI")
    play FEI "NAE06A_FEI0064"
    $ current_voice = "voice/NAE06A_FEI0064.ogg"
    "菲利斯" "「是要去买同人志啦，告诉绹的电话号码弄错了，这些漫不经心的言行」"
    $ stopvoc("FEI")
    play FEI "NAE06A_FEI0065"
    $ current_voice = "voice/NAE06A_FEI0065.ogg"
    "菲利斯" "「是为了不让绹卷入事件的想法，早就暴露啦」"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0125"
    $ current_voice = "voice/NAE06A_NAE0125.ogg"
    "绹" "「是这样吗？」"
    $ stopvoc("FEI")
    play FEI "NAE06A_FEI0066"
    $ current_voice = "voice/NAE06A_FEI0066.ogg"
    "菲利斯" "「桶喵是在考虑黑衣人万一抓到了绹的时候的事情呢」"
    $ stopvoc("FEI")
    play FEI "NAE06A_FEI0067"
    $ current_voice = "voice/NAE06A_FEI0067.ogg"
    "菲利斯" "「万一绹知道他的电话的话，会被他们当做桶喵的同伴，然后可能会被做很多糟糕的事情」"
    $ stopvoc("FEI")
    play FEI "NAE06A_FEI0068"
    $ current_voice = "voice/NAE06A_FEI0068.ogg"
    "菲利斯" "「所以，才告诉了你错误的电话号码……」"
    $ stopvoc("FEI")
    play FEI "NAE06A_FEI0069"
    $ current_voice = "voice/NAE06A_FEI0069.ogg"
    "菲利斯" "「虽然这只是我的推测」"
    "是这样啊……"
    "那个，说不定是有意而为之。"
    "我是该认为那是不相信我的表现呢。"
    "还是我在被他守护着的表现呢。"
    "也就是说这仅仅是我的一念之差……罢了？"
    $ stopvoc("FEI")
    play FEI "NAE06A_FEI0070"
    $ current_voice = "voice/NAE06A_FEI0070.ogg"
    "菲利斯" "「如果说，偷偷地去Ｌａｂ看一下的话，可能他又在一个人做着时间机器也说不定哦」"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0126"
    $ current_voice = "voice/NAE06A_NAE0126.ogg"
    "绹" "「我该……怎么办才好呢？」"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0127"
    $ current_voice = "voice/NAE06A_NAE0127.ogg"
    "绹" "「如果桶子叔叔是那么想的话……果然，我还是不要再去爸爸的大楼会比较好吧」"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0128"
    $ current_voice = "voice/NAE06A_NAE0128.ogg"
    "绹" "「因为我好像不管怎么做都无法成为当事者的样子……」"
    $ stopvoc("FEI")
    play FEI "NAE06A_FEI0071"
    $ current_voice = "voice/NAE06A_FEI0071.ogg"
    "菲利斯" "「是呢。这次的话，我和桶喵的意见相同」"
    $ stopvoc("FEI")
    play FEI "NAE06A_FEI0072"
    $ current_voice = "voice/NAE06A_FEI0072.ogg"
    "菲利斯" "「凶真也好桶喵也好，有着就算天塌下来了也要去做的事情的样子」"
    $ stopvoc("FEI")
    play FEI "NAE06A_FEI0073"
    $ current_voice = "voice/NAE06A_FEI0073.ogg"
    "菲利斯" "「但是绹，你不一样。我也希望你能够和你父亲希望的那样，就这么普通地生活下去」"
    $ stopvoc("FEI")
    play FEI "NAE06A_FEI0074"
    $ current_voice = "voice/NAE06A_FEI0074.ogg"
    "菲利斯" "「至少现在，是这样呢」"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0129"
    $ current_voice = "voice/NAE06A_NAE0129.ogg"
    "绹" "「现在……」"
    $ stopvoc("FEI")
    play FEI "NAE06A_FEI0075"
    $ current_voice = "voice/NAE06A_FEI0075.ogg"
    "菲利斯" "「是呢。现在，绹先做一个旁观者就好」"
    $ stopvoc("FEI")
    play FEI "NAE06A_FEI0076"
    $ current_voice = "voice/NAE06A_FEI0076.ogg"
    "菲利斯" "「总有一天，绹也会作为当事人来被迫做出一些决断。但是那是以后的事」"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0130"
    $ current_voice = "voice/NAE06A_NAE0130.ogg"
    "绹" "「恩……」"
    $ stopvoc("FEI")
    play FEI "NAE06A_FEI0077"
    $ current_voice = "voice/NAE06A_FEI0077.ogg"
    "菲利斯" "「啊，但是」"
    $ stopvoc("FEI")
    play FEI "NAE06A_FEI0078"
    $ current_voice = "voice/NAE06A_FEI0078.ogg"
    "菲利斯" "「就算是旁观者，但也不是说就不能插一手了哦？」"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0131"
    $ current_voice = "voice/NAE06A_NAE0131.ogg"
    "绹" "「诶……」"
    window hide



    $ loadBG(2,"BG73N2")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_HMC01"),"True","lh/FEI_HMC01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    show screen phonebtn
    show screen phoneSD1
    "说到这里，留未穗姐姐从床边站了起来。"
    "又温柔地摸了摸我的头。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_HMA01"),"True","lh/FEI_HMA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FEI")
    play FEI "NAE06A_FEI0079"
    $ current_voice = "voice/NAE06A_FEI0079.ogg"
    "菲利斯" "「姐姐的话到这里就结束了喵。之后，根据自己的想法来行动吧喵」"
    $ stopvoc("FEI")
    play FEI "NAE06A_FEI0080"
    $ current_voice = "voice/NAE06A_FEI0080.ogg"
    "菲利斯" "「作为中学生，有什么能做的喵？」"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0132"
    $ current_voice = "voice/NAE06A_NAE0132.ogg"
    "绹" "「姐姐……」"
    window hide
    play se "SGSE031"


    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_HMC02"),"True","lh/FEI_HMC02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    "这么说着，我的肚子叫了一声。"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0133"
    $ current_voice = "voice/NAE06A_NAE0133.ogg"
    "绹" "「啊……」"
    "说起来，从中午开始就没吃东西了。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_HMC01"),"True","lh/FEI_HMC01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FEI")
    play FEI "NAE06A_FEI0081"
    $ current_voice = "voice/NAE06A_FEI0081.ogg"
    "菲利斯" "「我会给你做夜宵的，现在先去洗澡吧喵」"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0134"
    $ current_voice = "voice/NAE06A_NAE0134.ogg"
    "绹" "「……恩」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_HLC01"),"True","lh/FEI_HLC01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide screen phonebtn
    "我站了起来，紧紧地抱住了留未穗姐姐。"
    $ stopvoc("NAE")
    play NAE "NAE06A_NAE0135"
    $ current_voice = "voice/NAE06A_NAE0135.ogg"
    "绹" "「谢谢你」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_HLA02"),"True","lh/FEI_HLA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FEI")
    play FEI "NAE06A_FEI0082"
    $ current_voice = "voice/NAE06A_FEI0082.ogg"
    "菲利斯" "「这样才是乖孩子嘛喵」"
    "该怎么办呢。"
    "接下来，就轮到我来考虑了。"

    hide screen phoneSD1
    window hide





    hide screen phonebtn
    scene expression Solid("000000")  with fade
    return
