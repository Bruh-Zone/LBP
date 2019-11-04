label SGFD2_NAE03A:

    hide screen phonebtn
    scene expression Solid("000000")  with fade

    window hide


    $ loadBG(0,"BG_BLACK")

    play bgm "FD2BGM01"


    $ date="7/7"
    $ day="SUN"
    hide screen phonebtn
    show screen phoneSD1

    $ stopvoc("NAE")
    play NAE "NAE03A_NAE0000"
    $ current_voice = "voice/NAE03A_NAE0000.ogg"
    "绹" "「诶嘿」"
    "身体从狭窄的窗户里滑了进去。"
    "如果踏空的话，就有可能整个人栽进马桶里，所以必须要小心谨慎。"
    "如果放一个那种防止脚滑的东西就好了。"
    window hide


    $ loadBG(0,"BG02A3")

    show screen phonebtn
    "……说回来，我是知道从厕所出入的不便的。"
    "万一，打开窗户正好遇到桶子叔叔在办事，变成这种事态就麻烦了。"
    "糟透了。"
    "不堪想象。"
    "桶子叔叔肥大的身体躺在了沙发上。"
    "我以为他在睡觉。"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CSB01"),"True","lh/DAR_CSB01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "NAE03A_DAR0000"
    $ current_voice = "voice/NAE03A_DAR0000.ogg"
    "至" "「绹酱、买回来了？」"
    "感到我的气息，他霍地起身。"
    $ stopvoc("NAE")
    play NAE "NAE03A_NAE0001"
    $ current_voice = "voice/NAE03A_NAE0001.ogg"
    "绹" "「嗯。这个可以吗？」"
    play se "SGSE337"
    "昨天，说是想要让我帮他买些吃的，桶子叔叔给了我一些钱。"
    "桶子叔叔像是要一阵子都要在这里埋头苦干的样子。"
    "所以，出去买东西就成了我的工作。"
    stop se
    $ stopvoc("DAR")
    play DAR "NAE03A_DAR0001"
    $ current_voice = "voice/NAE03A_DAR0001.ogg"
    "至" "「呀啊，得救了。从昨天傍晚到现在什么都没吃，肚子饿得工口图都没法欣赏了。」"
    $ stopvoc("NAE")
    play NAE "NAE03A_NAE0002"
    $ current_voice = "voice/NAE03A_NAE0002.ogg"
    "绹" "「…………」"
    $ stopvoc("DAR")
    play DAR "NAE03A_DAR0002"
    $ current_voice = "voice/NAE03A_DAR0002.ogg"
    "至" "「钱够吗？」"
    $ stopvoc("NAE")
    play NAE "NAE03A_NAE0003"
    $ current_voice = "voice/NAE03A_NAE0003.ogg"
    "绹" "「你给我的、我都用完了」"
    "只剩有找的７元零钱。"
    "把这些递给桶子叔叔——"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CSA01"),"True","lh/DAR_CSA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "NAE03A_DAR0003"
    $ current_voice = "voice/NAE03A_DAR0003.ogg"
    "至" "「没必要了、收着吧」"
    $ stopvoc("NAE")
    play NAE "NAE03A_NAE0004"
    $ current_voice = "voice/NAE03A_NAE0004.ogg"
    "绹" "「不、算了」"

    $ targetmailid = 466

    $ LR_RM_CHANCE=4
    call CHECK_RM_RECEIVE
    "我可不想仅仅７元就被摆臭脸。"
    call CHECK_RM_RECEIVE
    "于是我随手把钱往桌上一丢。"
    call CHECK_RM_RECEIVE
    $ stopvoc("DAR")
    play DAR "NAE03A_DAR0004"
    $ current_voice = "voice/NAE03A_DAR0004.ogg"
    "至" "「另外，说来绹、会做料理吗？」"
    call CHECK_RM_RECEIVE
    $ stopvoc("NAE")
    play NAE "NAE03A_NAE0005"
    $ current_voice = "voice/NAE03A_NAE0005.ogg"
    "绹" "「以前是做过、现在不做了」"

    call CHECK_RM_RECEIVE

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CSA02"),"True","lh/DAR_CSA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_BIREZON"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_BIREZON"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_BIREZON"])
    $ stopvoc("DAR")
    play DAR "NAE03A_DAR0005"
    $ current_voice = "voice/NAE03A_DAR0005.ogg"
    "至" "「吼吼。也就是说手舞足蹈地收下女子初中生亲手做的便当的可能性也是微存的？」"
    $ stopvoc("NAE")
    play NAE "NAE03A_NAE0006"
    $ current_voice = "voice/NAE03A_NAE0006.ogg"
    "绹" "「微存……？」"
    "一如既往地，没能理解桶子叔叔说的话。"
    "不顾我的困惑，桶子叔叔迅速打开了便当，开始吃了起来。冷的也很好吃吗。"
    $ stopvoc("DAR")
    play DAR "NAE03A_DAR0006"
    $ current_voice = "voice/NAE03A_DAR0006.ogg"
    "至" "「啊、对了对了。那个啊、我还想让绹酱帮我买其他的很多很多的东西啊」"
    $ stopvoc("NAE")
    play NAE "NAE03A_NAE0007"
    $ current_voice = "voice/NAE03A_NAE0007.ogg"
    "绹" "「还是吃的东西吗？」"
    "明明已经买了能够维持两到三天的零食和便当了。"
    $ stopvoc("DAR")
    play DAR "NAE03A_DAR0007"
    $ current_voice = "voice/NAE03A_DAR0007.ogg"
    "至" "「也不是啊。其实我发现水非常重要。要说的话，水要是停了就完蛋了」"
    $ stopvoc("DAR")
    play DAR "NAE03A_DAR0008"
    $ current_voice = "voice/NAE03A_DAR0008.ogg"
    "至" "「下次出去、多买些水吧」"
    $ stopvoc("NAE")
    play NAE "NAE03A_NAE0008"
    $ current_voice = "voice/NAE03A_NAE0008.ogg"
    "绹" "「嗯」"
    $ stopvoc("DAR")
    play DAR "NAE03A_DAR0009"
    $ current_voice = "voice/NAE03A_DAR0009.ogg"
    "至" "「还有，除了吃的以外还有必要的东西啊。接下来要制作电话微波炉，因此有必要的东西」"
    $ stopvoc("NAE")
    play NAE "NAE03A_NAE0009"
    $ current_voice = "voice/NAE03A_NAE0009.ogg"
    "绹" "「……！」"
    "是啊。还有这样的东西，我不买来不行啊。"
    $ stopvoc("NAE")
    play NAE "NAE03A_NAE0010"
    $ current_voice = "voice/NAE03A_NAE0010.ogg"
    "绹" "「我知道了，请告诉我需要买什么」"
    $ stopvoc("DAR")
    play DAR "NAE03A_DAR0010"
    $ current_voice = "voice/NAE03A_DAR0010.ogg"
    "至" "「 首先的话，大部分的东西在秋叶原的零件商店应该能买齐喔」"
    $ stopvoc("DAR")
    play DAR "NAE03A_DAR0011"
    $ current_voice = "voice/NAE03A_DAR0011.ogg"
    "至" "「日曜大工系的工具也是必要的」"

    $ gd["RCVmailData"][gc["ScriptMacros"]["RM_NAE_RECV_FEI02_01"]]["late"]=True
    $ lml.append(gc["ScriptMacros"]["RM_NAE_RECV_FEI02_01"])

    $ stopvoc("DAR")
    play DAR "NAE03A_DAR0012"
    $ current_voice = "voice/NAE03A_DAR0012.ogg"
    "至" "「还有就是──」"
    $ stopvoc("NAE")
    play NAE "NAE03A_NAE0011"
    $ current_voice = "voice/NAE03A_NAE0011.ogg"
    "绹" "「就是？」"
    hide screen phoneSD1
    window hide

    stop bgm 



    $ loadBG(0,"BG_BLACK")

    hide screen phonebtn
    "……。"
    window hide

    $ loadBG(0,"BG75A")

    show screen phonebtn
    show screen phoneSD1
    play bgm "FD2BGM10"

    $ stopvoc("NAE")
    play NAE "NAE03A_NAE0012"
    $ current_voice = "voice/NAE03A_NAE0012.ogg"
    "绹" "「…………」"
    "完全被骗了。"
    "御宅族的圣地・中野，同人志的店铺。"
    "第一次来这种地方。"
    "呜，感觉很羞耻。"
    "顾客们都是男的。"
    "在里面的架子上，陈列着大量画着摆着很Ｈ的姿势的女性的本子。"
    "桶子叔叔的委托，有三个大的方面。"
    "一个是零件类。"
    "这些虽说在秋叶原能买到，但还是托桶子叔叔完完整整写的一个清单，才总算是买齐了。"
    "还有是日曜大工的五金工具类。"
    "锯子啊，钳子啊之类。"
    "然后最后一个是——"
    hide screen phoneSD1
    window hide


    $ loadBG(0,"BG02A3")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CSA02"),"True","lh/DAR_CSA02a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    hide screen phonebtn
    $ stopvoc("DAR")
    play DAR "NAE03A_DAR0013"
    $ current_voice = "voice/NAE03A_DAR0013.ogg"
    "至" "「从虎之穴、把『钢巴゛尔的罗塞塔本』（ＮＥＴＡ：动画机动执事钢巴雷尔，在机器人笔记中提及）买回来。社团叫做『扁面条屋』（ＮＥＴＡ：社团乌冬屋）呢。别买错哟，一定要买三册回来。」"
    $ stopvoc("DAR")
    play DAR "NAE03A_DAR0014"
    $ current_voice = "voice/NAE03A_DAR0014.ogg"
    "至" "「因为不是１８禁，绹酱也可以买哦」"
    window hide


    $ loadBG(0,"BG75A")

    show screen phonebtn
    show screen phoneSD1
    "这种状况下还让我买同人志什么的，真是个荒唐的人。"
    "但是，如果因为我不照办就不让我发Ｄｍａｉｌ的话就糟了。"
    "所以，我还是老老实实地跑到中野来买了……"
    "不对，如果是这种东西的话，应该好好抱怨一下的吧。"
    "果然不能相信他的那种不是Ｈ物所以没关系的的说法。"
    "来像这样的店还是头一回。事前预测什么的办不到啊。"
    "桶子叔叔指定书虽然不是ｈ的，但有这么多ｈ的书在卖……！"
    "是要我在这数量吓人的黄本中找到指定的那本吗……。"
    "毫无自信啊……"
    "怎么办啊。"
    "我没法再往里走了。"
    "站在门口连抬头都做不到。"
    "朝这样的我，从刚才店员先生就朝我不停地打着眼色。"
    "大概是因为我怎么看也只是个小孩，所以提醒我“不能来这样的店”吧。"
    "说不定这么做的话更令我高兴一些。"
    "也可以当做空手回去的理由。"
    "……但是。"
    "如果不买就回去的话，也许会被桶子叔叔认为是派不上用场的家伙。"
    "要是这样的话，又麻烦了。"
    "被看作小孩子，派不上用场什么的，我可不要。"
    "不在这里好好完成委托可不行……"
    $ stopvoc("NAE")
    play NAE "NAE03A_NAE0013"
    $ current_voice = "voice/NAE03A_NAE0013.ogg"
    "绹" "「好……」"
    "绝对，要买到回去。"
    "鼓起干劲，我抬起脸，下定决心地朝收银员走去。"
    "朝着还没搞清状况的男性店员的眼睛，直直地看过去。"
    $ stopvoc("NAE")
    play NAE "NAE03A_NAE0014"
    $ current_voice = "voice/NAE03A_NAE0014.ogg"
    "绹" "「那个、不好意思……！」"
    "脸唰地热了起来，但我不能在意。"
    "其他的客人们非常惊讶地看着我，我也不能在意。"
    $ stopvoc("NAE")
    play NAE "NAE03A_NAE0015"
    $ current_voice = "voice/NAE03A_NAE0015.ogg"
    "绹" "「我正再找『扁面条屋』社团的『钢巴゛尔的罗塞塔本』」"
    $ stopvoc("NAE")
    play NAE "NAE03A_NAE0016"
    $ current_voice = "voice/NAE03A_NAE0016.ogg"
    "绹" "「请问这里有吗？」"
    $ stopvoc("NAE")
    play NAE "NAE03A_NAE0017"
    $ current_voice = "voice/NAE03A_NAE0017.ogg"
    "绹" "「请给我３本」"
    "店员先生笑了。"
    "我想我也一定笑了。"
    hide screen phoneSD1
    window hide

    stop bgm 



    $ loadBG(0,"BG31A")
    play se "SGSE091L" loop


    show screen phonebtn
    show screen phoneSD1
    "…………。"
    "怎么说，连买个东西，也能累得这么厉害啊。"
    "桶子叔叔，卑鄙。"
    "绝对是在捉弄我。"
    "是因为我无理地要求帮他的忙吗？"
    "但我没有认输。"
    hide screen phoneSD1
    window hide
    stop se



    $ loadBG(0,"BG02A3")

    $ targetmailid = cml.setdefault("RM_NAE_SEND_FEI03","")

    $ LR_RM_CHANCE=0
    if phonemailring!= "":
        play se phonemailring
    if persistent.skipmail==False:
        $ renpy.choice_for_skipping()
    if targetmailid != "":
        $ RcvMail(targetmailid)
        $ targetmailid=""

    call CHECK_RM_RECEIVE

    $ gd["RCVmailData"][gc["ScriptMacros"]["RM_NAE_RECV_FEI02_02"]]["late"]=True
    $ lml.append(gc["ScriptMacros"]["RM_NAE_RECV_FEI02_02"])


    show screen phonebtn
    show screen phoneSD1
    play bgm "BGM13"

    $ stopvoc("NAE")
    play NAE "NAE03A_NAE0018"
    $ current_voice = "voice/NAE03A_NAE0018.ogg"
    "绹" "「买回来了」"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CSB04"),"True","lh/DAR_CSB04a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "NAE03A_DAR0015"
    $ current_voice = "voice/NAE03A_DAR0015.ogg"
    "至" "「真的！？」"
    "我拿出同人志，桶子叔叔非常的吃惊。"
    $ stopvoc("DAR")
    play DAR "NAE03A_DAR0016"
    $ current_voice = "voice/NAE03A_DAR0016.ogg"
    "至" "「说来、我是抱着不行就算了的想法拜托你的，结果真的买来了啊，绹酱真是厉害呢」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CSA02"),"True","lh/DAR_CSA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "NAE03A_DAR0017"
    $ current_voice = "voice/NAE03A_DAR0017.ogg"
    "至" "「毫不在意地完成了对人来说不可能的任务。然后以下略」"
    $ stopvoc("DAR")
    play DAR "NAE03A_DAR0018"
    $ current_voice = "voice/NAE03A_DAR0018.ogg"
    "至" "「啊，说起来绹酱，去虎之穴是第一次？」"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_KWSK"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_KWSK"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_KWSK"])
    $ stopvoc("DAR")
    play DAR "NAE03A_DAR0019"
    $ current_voice = "voice/NAE03A_DAR0019.ogg"
    "至" "「能稍微和我说说你到店里后的感想吗？可以的话{color=#f00}ｋｗｓｋ{/color}」"
    $ stopvoc("NAE")
    play NAE "NAE03A_NAE0019"
    $ current_voice = "voice/NAE03A_NAE0019.ogg"
    "绹" "「店员先生、很亲切」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CSB04"),"True","lh/DAR_CSB04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "NAE03A_DAR0020"
    $ current_voice = "voice/NAE03A_DAR0020.ogg"
    "至" "「喂，和店员搭话什么的，放出交流障碍者绝对办不到的大招什么的，绹酱，真是可怕的孩子……！」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    "桶子叔叔对买来的零件看都没看一眼，而是光盯着同人志在看。"
    "而且还，边读边发出奇怪的声音。"

    $ targetmailid = 469

    $ LR_RM_CHANCE=4
    call CHECK_RM_RECEIVE
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_GUNVARREL"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_GUNVARREL"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_GUNVARREL"])
    $ stopvoc("DAR")
    play DAR "NAE03A_DAR0021"
    $ current_voice = "voice/NAE03A_DAR0021.ogg"
    "至" "「哞咻ー，阿璐琪（ＮＥＴＡ乌冬屋画师あるちゅ）的{color=#f00}钢巴雷尔{/color}本，以后绝对是白金级的！而且居然还是非工口的那就更加了」"
    call CHECK_RM_RECEIVE
    $ stopvoc("DAR")
    play DAR "NAE03A_DAR0022"
    $ current_voice = "voice/NAE03A_DAR0022.ogg"
    "至" "「说来、如果我的预想正确的话，明年绝对钢巴雷尔就会开播呢。绝对不会错。Ｓｔａｆｆ表太真实了。是那种在日本不播就太不合理了的等级」"
    call CHECK_RM_RECEIVE
    $ stopvoc("NAE")
    play NAE "NAE03A_NAE0020"
    $ current_voice = "voice/NAE03A_NAE0020.ogg"
    "绹" "「…………」"
    call CHECK_RM_RECEIVE
    "桶子叔叔在我看来，就像奇珍异兽一样。"

    call CHECK_RM_RECEIVE
    "这样奇怪的人，在我就读的学校里不存在。"
    "两年前也不曾想过，这样荒唐，存在自身却是适当的。"
    "不如说，那个时候我很不擅长应对冈伦叔叔和桶子叔叔，总是躲着不和他们说话，也不是很清楚他们。"
    "那时的不擅长的感觉，是正解啊。"
    "生理上的不行，这么说，行吗。"
    "要是桶子叔叔是同时代的朋友，现在就想马上和他绝交了。"
    "可是。"
    "像是童话故事一样的话，不错。"
    "就像爱丽丝遇到白兔一样。"
    "就像在温迪眼前出现的彼得潘一样。"
    "对我来说桶子叔叔就是这样的存在。"
    $ stopvoc("NAE")
    play NAE "NAE03A_NAE0021"
    $ current_voice = "voice/NAE03A_NAE0021.ogg"
    "绹" "「现在不开始做时间机器吗？」"
    $ stopvoc("DAR")
    play DAR "NAE03A_DAR0023"
    $ current_voice = "voice/NAE03A_DAR0023.ogg"
    "至" "「明天开始再拿出真本事」"
    "真的……吗？"
    "考试前难得的星期六，我就这样浪费了。"

    $ gd["RCVmailData"][gc["ScriptMacros"]["RM_NAE_RECV_MAK02_01"]]["late"]=True
    $ lml.append(gc["ScriptMacros"]["RM_NAE_RECV_MAK02_01"])



    stop bgm 
    hide screen phoneSD1
    window hide





    hide screen phonebtn
    scene expression Solid("000000")  with fade
    return
