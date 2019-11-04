label SGFD2_NAE02A:
    hide screen phonebtn
    scene expression Solid("000000")  with fade

    window hide


    $ loadBG(0,"BG_BLACK")

    play se "SGSE333L" loop



    $ date="7/6"
    $ day = "SAT"
    hide screen phonebtn
    hide screen phoneSD1

    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0000"
    $ current_voice = "voice/NAE02A_NAE0000.ogg"
    "绹" "「……唔、嗯」"
    window hide
    play se "SGSE112"


    stop se


    $ loadBG(2,"BG73A")



    play bgm "BGM18"
    "关掉闹钟，我从床上起身。"
    "上午 7点。"
    "对于一个人早上能起来这件事，我十分得意。"
    "父亲在的时候，也是自己起床，自己做早饭、把垃圾扔出去。"
    "从邻居那儿，得到了坚强的孩子这样的评价。"
    play se "SGSE056"
    "虽然还有些没睡醒，我还是很快脱掉睡衣，换上了校服。"
    "我们学校的校服，是一点也不漂亮的、朴素的水手服。"
    "不过，我自己也知道我对服装搭配没什么感觉，校服的存在帮了我大忙。从升入中学，我着实感到如此。"
    window hide
    stop se


    $ loadBG(0,"BG26A")
    play se "SGSE336"


    show screen phonebtn
    show screen phoneSD1
    "在洗脸台洗完脸后，我走向客厅。"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='FPP')",DynamicDisplayable(mouthanime,"FPP_ASA01"),"True","lh/FPP_ASA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FPP")
    play FPP "NAE02A_FPP0000"
    $ current_voice = "voice/NAE02A_FPP0000.ogg"
    "幸高叔叔" "「呀、绹。早上好」"
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0001"
    $ current_voice = "voice/NAE02A_NAE0001.ogg"
    "绹" "「啊、早上好」"
    "做好早上的准备的幸高伯正一边喝咖啡一边读着新闻。"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    "桌上摆着四个人的早餐。"
    "今天是青菜炒汉堡肉和番茄沙拉。"
    $ stopvoc("X02")
    play KUR "NAE02A_X020000"
    $ current_voice = "voice/NAE02A_X020000.ogg"
    "千佳音阿姨" "「绹酱、现在正在烤面包、先坐吧」"
    "从厨房传来了围裙装的千佳音阿姨的声音。"
    "我在椅子上坐下，向咖啡里加入牛奶。"
    "在这个家里生活，马上就快两年了。"
    "父亲死后，在没有亲戚的我不知所措之时，最先向我伸出援助之手的是留未穂姐。"
    "父亲和秋叶原商业街的人们有过交情的关系，幸高叔叔也知道我的情况。"
    "不仅一直以来让我寄食于此，还帮我垫付学费什么的。"
    "真是、一家非常好的人。"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='FPP')",DynamicDisplayable(mouthanime,"FPP_ASA01"),"True","lh/FPP_ASA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0002"
    $ current_voice = "voice/NAE02A_NAE0002.ogg"
    "绹" "「姐姐呢？」"
    $ stopvoc("FPP")
    play FPP "NAE02A_FPP0001"
    $ current_voice = "voice/NAE02A_FPP0001.ogg"
    "幸高叔叔" "「大概还在睡吧？　只不过昨天好像也睡到了很晚呢」"
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0003"
    $ current_voice = "voice/NAE02A_NAE0003.ogg"
    "绹" "「最近、她早上都不起来啊」"
    $ stopvoc("FPP")
    play FPP "NAE02A_FPP0002"
    $ current_voice = "voice/NAE02A_FPP0002.ogg"
    "幸高叔叔" "「毕竟是风投企业的社长、很忙的呀」"
    "留未穗姐今年春天高中毕业就自己开起了公司，虽然是成员只有三人的小公司，好歹也是个社长。"
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0004"
    $ current_voice = "voice/NAE02A_NAE0004.ogg"
    "绹" "「没问题吧？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='FPP')",DynamicDisplayable(mouthanime,"FPP_ASA03"),"True","lh/FPP_ASA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FPP")
    play FPP "NAE02A_FPP0003"
    $ current_voice = "voice/NAE02A_FPP0003.ogg"
    "幸高叔叔" "「留未穗有黑木跟在身边，就不用你担心了。那孩子看样子、也是坚强的孩子呢」"
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0005"
    $ current_voice = "voice/NAE02A_NAE0005.ogg"
    "绹" "「是嘛」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    "取的沙拉吃到差不多一半，千佳音阿姨拿着烤面包过来了。"
    "涂上爱吃的草莓果酱，我吃起了面包。"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='FPP')",DynamicDisplayable(mouthanime,"FPP_ASA01"),"True","lh/FPP_ASA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FPP")
    play FPP "NAE02A_FPP0004"
    $ current_voice = "voice/NAE02A_FPP0004.ogg"
    "幸高叔叔" "「比起这个绹，考试复习好了吗？　马上就要考试了啊？」"
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0006"
    $ current_voice = "voice/NAE02A_NAE0006.ogg"
    "绹" "「嗯。也好好预习了」"
    "这样看来，我还真是聪明呢。"
    "这次期末考试，也进了年级前十。"
    $ stopvoc("FPP")
    play FPP "NAE02A_FPP0005"
    $ current_voice = "voice/NAE02A_FPP0005.ogg"
    "幸高叔叔" "「今天早上也要晨练吗？」"
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0007"
    $ current_voice = "voice/NAE02A_NAE0007.ogg"
    "绹" "「不。考试之前这段时间暂停了」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    "我加入了羽毛球部，水平还勉勉强强。"
    "提到羽毛球时，我总会不知为何，有些不想回答。"
    "因为一直要晨练，所以提早３０分钟起床了。"
    "今天倒是不需要那么赶。"
    $ stopvoc("X02")
    play KUR "NAE02A_X020001"
    $ current_voice = "voice/NAE02A_X020001.ogg"
    "千佳音阿姨" "「明明可以不用这么急的」"
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0008"
    $ current_voice = "voice/NAE02A_NAE0008.ogg"
    "绹" "「啊……」"
    "不小心和平时一样，一口气把烤面包全吃了下去。"
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0009"
    $ current_voice = "voice/NAE02A_NAE0009.ogg"
    "绹" "「看来没有晨练只是说说而已，啊哈哈」"
    "我笑着，幸高叔叔和千佳音阿姨也露出了和蔼的笑容。"
    "托秋叶家收留我的好意，我才振作起来。"
    hide screen phoneSD1
    window hide



    $ loadBG(0,"BG27A")





    hide screen phonebtn
    show screen phoneSD1
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0010"
    $ current_voice = "voice/NAE02A_NAE0010.ogg"
    "绹" "「我出门啦」"
    window hide






    show screen phonebtn
    play se "SGSE094"

    "结果，和留未穗姐没见到面，我就走出了家门。"
    "学校在仲御徒町站附近，大约是步行半小时左右的路程。"
    "虽然骑自行车也不错，我还是一直步行往返校。"
    "也有一部分原因是因为不希望秋叶原家的人特意为我买一辆自行车吧。"
    "还有，我喜欢走路。"

    stop bgm 
    window hide


    $ loadBG(2,"IBGX048")



    hide screen phonebtn
    play bgm "FD2BGM08"

    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0011"
    $ current_voice = "voice/NAE02A_NAE0011.ogg"
    "绹" "「…………」"
    "走着走着，脑海中就浮现出了两年前的事。"
    "小学生的时候，经常走在这条路上，到父亲的大楼里去玩。"
    "当时，和父亲两人一起居住的家，是在御徒町的方向。"
    "这么说来那个家，现在变得怎样了呢。"
    "烂得差不多了的房子、现在也是看上去摇摇欲坠的样子。虽然卖了出去，一定没有人会住在那吧。"
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0012"
    $ current_voice = "voice/NAE02A_NAE0012.ogg"
    "绹" "「……一早上开始就不安起来了。」"
    "明明好不容易才、才精神满满地走家门的。"
    "只要一个人呆着，就马上想起那时的事情，这是我的坏习惯。"
    "马上就到和同班同学真子酱约好碰头的地方了。"
    "她同样参加了羽毛球部，是我在学校里最好的伙伴。"
    "所以，早上也有在一起去上学。"
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0013"
    $ current_voice = "voice/NAE02A_NAE0013.ogg"
    "绹" "「呼……」"
    "我用手拍响自己的脸。"
    "我没关系的。"
    "早上要好好地和她打招呼。"
    "学习和社团活动也很充实。"
    "学校里也有朋友。"
    "这样的生活继续下去，一定，会很幸福。"
    "什么时候，才能、忘了那个夏天的事呢。"
    "什么时候呢。"
    hide screen phoneSD1
    window hide

    stop bgm 



    $ loadBG(0,"BG22A")
    $ RcvMail(287)



    $ targetmailid = 456

    $ LR_RM_CHANCE=1
    if phonemailring!= "":
        play se phonemailring
    if persistent.skipmail==False:
        $ renpy.choice_for_skipping()
    if targetmailid != "":
        $ RcvMail(targetmailid)
        $ targetmailid=""

    call CHECK_RM_RECEIVE
    play se "SGSE007L" loop

    show screen phonebtn
    show screen phoneSD1
    "这周因为是考试周，所以没有社团活动。"
    "虽说放学了就该早早回家，但回去后也没有什么要做的功课，就稍微四处乱逛了会儿。"
    "于是，我又来到了久违的秘密场所。"
    "首先是友都八喜前的果汁摊买了一杯草莓果汁，站在那儿喝完。（译注：友都八喜是日本的一家大型连锁超市）"
    "这可以算得上是一种仪式了"
    "在这里喝完草莓果汁，一天的心情就会很好。"
    "由于零花钱有限的缘故，还是控制在了一周一次的程度。"

    $ gd["RCVmailData"][gc["ScriptMacros"]["RM_NAE_RECV_FEI01_01"]]["late"]=True
    $ lml.append(gc["ScriptMacros"]["RM_NAE_RECV_FEI01_01"])

    "就这么从昭和路走出去，目的地就是——"
    hide screen phoneSD1
    window hide
    stop se



    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_NAE002A"]]["Check"]=True
    $ loadBG(0,"EV_NAE002A")





    hide screen phonebtn
    play bgm "BGM26"





    "游戏中心。"
    "但是如果是从中央大道出去的话，就不是这样漂亮的地方。"
    "我很中意这个古旧的游戏中心。"
    "灯光昏暗、空气浑浊，来的客人大多都是成年的男性。"
    "在情侣中受欢迎的可爱的抓娃娃机一台也没有。"
    "但是，我很中意，这样昏暗的环境。因为，拜此所赐作为女中学生的我即使玩着游戏，也不用在意他人的目光。"
    "每周来一次这里，一个人玩着，是我秘密的快乐。"
    "本来想多运动一些，只是社团活动已经让我竭尽全力了。"
    "一直在玩的是叫做对战格斗类的游戏。"
    "选择好自己操作的角色，主要进行一对一战斗的游戏。"
    "虽然对手是电脑，也会有他人乱入而变成PVP。"
    "即使输了，也一直继续着。"
    "即使因有限的零花钱而小心谨慎地维持着，也非常的开心。"
    "擅长格斗游戏的强者们，果然还是在中央大道两边的大游戏中心里聚集着。我也偶尔进行过远征，但这里是主战场，我没有打算改变。"
    "那么接下来，今天玩什么游戏呢。"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_GW4"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_GW4"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_GW4"])
    "还是和平常一样，玩『黄金狼战士４』吧。"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_BLAZBLACK"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_BLAZBLACK"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_BLAZBLACK"])
    "啊、但是进来了『Ｂｒａｖｅ　Ｌｕｃｋ』的新作。"
    "今天还是试试这个吧。"
    window hide





    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_NAE002A"]]["Check"]=True
    $ loadBG(0,"EV_NAE002A")











    "投入１００日元，游戏开始。"
    "新角色还没玩上手，马上就被其他玩家乱入了。"
    "对战对手在面对的机器背后，所有看不到对手的脸。"
    "我就是喜欢对战格斗游戏的这一点。"
    "互相评价的标准，只有实力。"
    "我在这，没有被视为小孩。"
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0014"
    $ current_voice = "voice/NAE02A_NAE0014.ogg"
    "绹" "「…………」"
    "对手颇为强大。"
    "与强者战斗时，能集中精神。"
    "这种感觉，非常令人愉悦。"
    window hide
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_NAE002A"]]["Check"]=True
    $ loadBG(0,"EV_NAE002A")











    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0015"
    $ current_voice = "voice/NAE02A_NAE0015.ogg"
    "绹" "「啊……」"
    "Ｒｏｕｎｄ１我输掉了，不甘心。"
    "明明喝了草莓果汁的。"
    "一定是在使用新角色的原因。"
    "掌握要诀，大概还需要稍微花点时间吧。"
    "回合之间有一点儿时间。"
    "我伸展四肢，放松了下来。"
    window hide
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_NAE002B"]]["Check"]=True


    $ loadBG(2,"EV_NAE002B")



    "不意间，察觉到了视野一角的两个男人。"
    "为什么，我会觉得在意呢。"
    "两个人没有玩游戏，却坐在游戏机前的座椅上聊着。"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_McDy"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_McDy"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_McDy"])
    "明明这里不是{color=#f00}麦当捞{/color}。"
    "那样坐着，我怎么好好打游戏啊。"
    "特别胖的那个人，手里还拿着快餐店买的汉堡包和果汁。"
    "很不快的感觉。"
    "我并不是那么沉得住气的人。"
    "所以，虽然在玩想玩的游戏，但看着那样没有一点教养的人占着位子，我已经没法集中精神了。还是打道回府得了。"
    "像这样的大人，还是希望他们要有点大人的样子啊……。"
    "仅仅是在心中这么想着。"
    window hide
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_NAE002A"]]["Check"]=True
    $ loadBG(0,"EV_NAE002A")











    "Ｒｏｕｎｄ２已经开始了。"
    "不行，再不认真点，又要输掉了。"
    "刚才的二人组，胖的那位，吃完汉堡从座位上站了起来。"
    "不知为何，比起游戏我变得更在意那边。"
    "我怎么了啊？"
    "明明一直以来对其他的客人我都毫不在意的。"
    $ stopvoc("DAR")
    play DAR "NAE02A_DAR0000"
    $ current_voice = "voice/NAE02A_DAR0000.ogg"
    "至" "「那么、找到了资金方的话联系我」"
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0016"
    $ current_voice = "voice/NAE02A_NAE0016.ogg"
    "绹" "「…………切」"
    window hide
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_NAE002A"]]["Check"]=True
    $ loadBG(0,"EV_NAE002A")











    "操作着摇杆的手不听使唤了。"
    "一不小心半路中跳了起来，不出所料地被对手用对空技轻松击落，顺势又是一套连击。"
    "一瞬间我慌了。"
    "虽然想着要应对一下，但结果却反而慌张起来，使用了一击重踢之后被对面连上了。"
    "虽然还不至于被ＫＯ，站稳已经做不到了。"
    window hide
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_NAE002C"]]["Check"]=True


    $ loadBG(2,"EV_NAE002C")



    "抬头离开画面，寻找着刚才的胖子的身影。"
    "恰好看到正要走出门的宽大的背影。"
    "不去追的话。"
    "直觉地这么想。"
    "对战中起座违反规则。"
    "但是，这样下去就要跟丢了。"
    "所以，对不起了！"
    "混杂着嘈杂的游戏音，还是能听到一些他的声音。"
    "那个声音，似曾相识。"
    "也许是听错了也说不定。"
    "是两年前的那个夏天经常听到的声音，有这种感觉。"
    window hide

    stop bgm 



    $ loadBG(0,"BG14A")

    show screen phonebtn
    show screen phoneSD1
    play bgm "FD2BGM11"

    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0017"
    $ current_voice = "voice/NAE02A_NAE0017.ogg"
    "绹" "「……啊、去哪儿了……？」"
    "胖子的身影已经找不到了。"
    "也只扫视了站前来往的行人啊……。"
    "也试着在四周找找吧。"
    "那么胖的人，明明应该马上就能找到的。"
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0018"
    $ current_voice = "voice/NAE02A_NAE0018.ogg"
    "绹" "「啊、找到了」"
    "已经离得很远了。"
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0019"
    $ current_voice = "voice/NAE02A_NAE0019.ogg"
    "绹" "「等──」"
    "虽然想大声叫住——"
    "有很多的人在周围，大声喊叫有点羞耻。结果，只是挥了挥手。"
    "但是，无论怎么在胖子的背后挥着手，也不会被注意到。"
    "无论如何不跑过去追上的话……！"
    window hide


    $ loadBG(2,"BG20A")



    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_UPX"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_UPX"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_UPX"])
    "穿过高架铁路，走到UPX前面的地方，终于追到了。"
    "胖子仍然没有注意到我，还在悠闲地走着。"
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0020"
    $ current_voice = "voice/NAE02A_NAE0020.ogg"
    "绹" "「啊、啊那个……」"
    "下定决心，搭上了话。"
    $ stopvoc("DAR")
    play DAR "NAE02A_DAR0001"
    $ current_voice = "voice/NAE02A_DAR0001.ogg"
    "至" "「嗯？」"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CSA08"),"True","lh/DAR_CSA08a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    "胖子转过身来。"
    "四目相对。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CSA01"),"True","lh/DAR_CSA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    "这张脸，果然似曾相识。"
    "不会错。"
    "是两年前，在我父亲大楼二层里出入的，大学生。"
    "名字，记忆中是——"
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0021"
    $ current_voice = "voice/NAE02A_NAE0021.ogg"
    "绹" "「Ｄｕｃｋ……？」"
    "是这个名字吗？"
    "没有、自信。"
    "比起Ｄｕｃｋ、倒是更像是Ｐｉｇ。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CSB04"),"True","lh/DAR_CSB04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "NAE02A_DAR0002"
    $ current_voice = "voice/NAE02A_DAR0002.ogg"
    "至" "「呜哇、果然！」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    play se "SGSE182"
    "见了我，说着，胖胖的Ｄｕｃｋ先生飞快地逃走了。"
    "大大的身体摇晃着，啪嗒啪嗒地跑走了。"
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0022"
    $ current_voice = "voice/NAE02A_NAE0022.ogg"
    "绹" "「呃……」"
    "被人跑着躲开，我呆住了。"
    "怎么会、见了我逃跑什么的。"
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0023"
    $ current_voice = "voice/NAE02A_NAE0023.ogg"
    "绹" "「等、等一下！　Ｄｕｃｋ叔叔！」"
    play bgm "BGM12"
    "这回没有在意周围人眼光的余裕，大喊了起来。"
    "但是，Ｄｕｃｋ叔叔没有停下来。"
    "我也慌忙跟着追了上去。"
    "明明平时是不会做这样的事情的。"
    window hide
    play se "SGSE181"


    $ loadBG(2,"BG16A3")



    "Ｄｕｃｋ叔叔，偏偏又跑出了中央大道。"
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0024"
    $ current_voice = "voice/NAE02A_NAE0024.ogg"
    "绹" "「等等我啊！　你不记得我了么！？」"
    "人行道上的行人朝追着逃掉的Ｄｕｃｋ叔叔的我投来了问询的目光。"
    "Ｄｕｃｋ叔叔，跑得很慢。"
    "总像要断气似的，推开路人。"
    "这样下去就能轻松追上了。"
    window hide


    $ loadBG(2,"BG40A")



    "像是终于体力耗尽了，Ｄｕｃｋ叔叔停下了脚步。"
    "站在那手撑膝盖，呼哧呼哧地喘着粗气。"
    "追到之后的我，意识了到周围的目光。"
    "秋叶原的正中央。"
    "这样说来，同胖大叔搭话的女中学生的我，会被怎样看呢。"
    "……就算已经这样了，还是希望在人少一点的地方停下来啊。"
    "虽然有些不快，但是也不能就这么站着什么也不说。"
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0025"
    $ current_voice = "voice/NAE02A_NAE0025.ogg"
    "绹" "「那个、Ｄｕｃｋ叔叔、为什么要逃跑啊？」"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CSB04"),"True","lh/DAR_CSB04a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "NAE02A_DAR0003"
    $ current_voice = "voice/NAE02A_DAR0003.ogg"
    "至" "「诶？　哈啊、呼、你、谁？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CSA02"),"True","lh/DAR_CSA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "NAE02A_DAR0004"
    $ current_voice = "voice/NAE02A_DAR0004.ogg"
    "至" "「说起来、不好、来了……抓我的……！」"
    "注意到了、Ｄｕｃｋ叔叔的视线、并没有看着我、而是我的背后。"
    "我也回头一看。"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0026"
    $ current_voice = "voice/NAE02A_NAE0026.ogg"
    "绹" "「……啊」"
    "是“黑衣人”。"
    "在夏天仍然穿着看着就觉得热的黑色套装的严肃的男人有三名，推开人群一般朝着我们这边来了。"
    "是父亲大楼周围偶尔见到的人的同伴吗，我不知道。"
    "只是——"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CSB06"),"True","lh/DAR_CSB06a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0027"
    $ current_voice = "voice/NAE02A_NAE0027.ogg"
    "绹" "「难道说、你在被他们追着？」"
    $ stopvoc("DAR")
    play DAR "NAE02A_DAR0005"
    $ current_voice = "voice/NAE02A_DAR0005.ogg"
    "至" "「已经、跑不动了……」"
    "Ｄｕｃｋ叔叔浑身是汗，一副就要就地下蹲的样子。"
    "“黑衣人”们、马上就要追到这边了。"
    "真像是，漫画一样的展开……！"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CLB06"),"True","lh/DAR_CLB06a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide screen phonebtn
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0028"
    $ current_voice = "voice/NAE02A_NAE0028.ogg"
    "绹" "「…………这边！」"
    "我瞬间反应，行动了起来。"
    "扯着Ｄｕｃｋ叔叔的手，朝眼前的零件商店冲了进去。"
    window hide



    $ loadBG(0,"BG17A")

    "沿着零件商店的胡同冲刺，上到了二楼。"
    "于是，和Ｄｕｃｋ叔叔熟悉的店员打过招呼，很快就让我们藏了起来。"
    window hide


    $ loadBG(2,"BG_BLACK")



    "藏了大约十分钟之后，我们又回到了一层"
    "朝着小道的另一头看去，“黑衣人”已经确定不在了。"
    window hide


    $ loadBG(0,"BG17A")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CSA02"),"True","lh/DAR_CSA02a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    show screen phonebtn
    $ stopvoc("DAR")
    play DAR "NAE02A_DAR0006"
    $ current_voice = "voice/NAE02A_DAR0006.ogg"
    "至" "「他们已经走了？」"
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0029"
    $ current_voice = "voice/NAE02A_NAE0029.ogg"
    "绹" "「看起来是的」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CSB06"),"True","lh/DAR_CSB06a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    stop bgm 
    $ stopvoc("DAR")
    play DAR "NAE02A_DAR0007"
    $ current_voice = "voice/NAE02A_DAR0007.ogg"
    "至" "「呼——、得救了……」"
    $ stopvoc("DAR")
    play DAR "NAE02A_DAR0008"
    $ current_voice = "voice/NAE02A_DAR0008.ogg"
    "至" "「安心下来也觉得渴了」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    "说完这些，Ｄｕｃｋ叔叔就像是想要独自去什么的地方似的走了。"
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0030"
    $ current_voice = "voice/NAE02A_NAE0030.ogg"
    "绹" "「啊……嘛……」"
    "走掉了。"
    "要不见了。"
    "在这里分别的话，就再也见不到第二次了。"
    "所以，谁来，给我勇气……！"

    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0031"
    $ current_voice = "voice/NAE02A_NAE0031.ogg"
    "绹" "「等、等等我。Ｄｕｃｋ叔叔！」 "
    "下定决心叫住他。"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CSA01"),"True","lh/DAR_CSA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "NAE02A_DAR0009"
    $ current_voice = "voice/NAE02A_DAR0009.ogg"
    "至" "「啊、说来Ｄｕｃｋ叔叔是谁？　我？被这么叫我还是第一次」"
    $ stopvoc("DAR")
    play DAR "NAE02A_DAR0010"
    $ current_voice = "voice/NAE02A_DAR0010.ogg"
    "至" "「……还有、你是谁？　肯定不是真的中学生、绝对是骗子。强行推销画啊壶啊的吧，我知道得很」"
    "我一定是瞪着Ｄｕｃｋ叔叔了。"
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0032"
    $ current_voice = "voice/NAE02A_NAE0032.ogg"
    "绹" "「我是、天王寺……绹……！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CSA05"),"True","lh/DAR_CSA05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "NAE02A_DAR0011"
    $ current_voice = "voice/NAE02A_DAR0011.ogg"
    "至" "「…………」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CSA04"),"True","lh/DAR_CSA04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "NAE02A_DAR0012"
    $ current_voice = "voice/NAE02A_DAR0012.ogg"
    "至" "「哦哦、绹酱」"
    "这样才终于想起来一样。"
    "Ｄｕｃｋ叔叔那双圆溜溜的眼珠不停闪着。"
    window hide



    $ loadBG(0,"BG21A")

    play se "SGSE334"

    play bgm "FD2BGM08"


    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CSA01"),"True","lh/DAR_CSA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "NAE02A_DAR0013"
    $ current_voice = "voice/NAE02A_DAR0013.ogg"
    "至" "「给、这是帮了我的谢礼」"
    "从自动贩卖机买来果汁的Ｄｕｃｋ叔叔，不容推辞的向我递来。"

    $ targetmailid = cml.setdefault("RM_NAE_SEND_FEI01","")

    $ LR_RM_CHANCE=4
    call CHECK_RM_RECEIVE
    "无糖可乐。"
    call CHECK_RM_RECEIVE
    "碳酸饮料，不太能喝……。"
    call CHECK_RM_RECEIVE
    "至少，在买之前问问我喝什么啊。"
    call CHECK_RM_RECEIVE
    "想要着要不要拒绝，却没有办法地接受了。"

    call CHECK_RM_RECEIVE
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0033"
    $ current_voice = "voice/NAE02A_NAE0033.ogg"
    "绹" "「谢谢了……、Ｄｕｃｋ叔叔」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CSA02"),"True","lh/DAR_CSA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "NAE02A_DAR0014"
    $ current_voice = "voice/NAE02A_DAR0014.ogg"
    "至" "「说好别叫我Ｄｕｃｋ叔叔的。拜托请叫我『至欧尼酱』。或者『Ｄａｒｕ・ｔｈｅ・ＳｕｐｅｒＨａｃｋｅｒ』」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    play se "SGSE334"

    "说着，Ｄｕｃｋ叔叔又买了一瓶无糖可乐。"
    window hide
    play se "SGSE207"

    $ stopvoc("DAR")
    play DAR "NAE02A_DAR0015"
    $ current_voice = "voice/NAE02A_DAR0015.ogg"
    "至" "「咕哝、咕哝……」"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CSA02"),"True","lh/DAR_CSA02a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "NAE02A_DAR0016"
    $ current_voice = "voice/NAE02A_DAR0016.ogg"
    "至" "「噗啊！　剧烈运动后可乐真是太棒了。不接受任何异议」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CSA01"),"True","lh/DAR_CSA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "NAE02A_DAR0017"
    $ current_voice = "voice/NAE02A_DAR0017.ogg"
    "至" "「呀、这么说来两年之后再次来到秋叶原被中学生救了、这个中学生还是长大了的绹酱、放到黄油里不就完全是flag了嘛？」"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_GACHI"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_GACHI"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_GACHI"])
    $ stopvoc("DAR")
    play DAR "NAE02A_DAR0018"
    $ current_voice = "voice/NAE02A_DAR0018.ogg"
    "至" "「好好感受命运吧。从现在开始我和绹酱的、爱与冒险的日子开始了喔。动画化决定！」"
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0034"
    $ current_voice = "voice/NAE02A_NAE0034.ogg"
    "绹" "「…………」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CSB04"),"True","lh/DAR_CSB04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "NAE02A_DAR0019"
    $ current_voice = "voice/NAE02A_DAR0019.ogg"
    "至" "「啊、不、那么、不叫至欧尼酱也没关系。至桑、就好」"
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0035"
    $ current_voice = "voice/NAE02A_NAE0035.ogg"
    "绹" "「…………」"
    $ stopvoc("DAR")
    play DAR "NAE02A_DAR0020"
    $ current_voice = "voice/NAE02A_DAR0020.ogg"
    "至" "「……呐、绹酱？　眼神很可怕啊」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CSA01"),"True","lh/DAR_CSA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "NAE02A_DAR0021"
    $ current_voice = "voice/NAE02A_DAR0021.ogg"
    "至" "「那是当然、中学生冷冰冰的视线什么的、这也有这样的吧……」"
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0036"
    $ current_voice = "voice/NAE02A_NAE0036.ogg"
    "绹" "「…………」"
    "啊，想起来了。"
    "虽然一直在回忆着。"
    "这个人的名字。"
    "外号是桶子，“Ｌａｂｍｅｍ”的人是这样叫的。"
    "本名叫做，桥田，父亲这么叫他。"
    "现在，这个人说“叫我至欧尼酱”的话，全名应该是桥田至了。"
    "呼——、畅快多了。"
    $ stopvoc("DAR")
    play DAR "NAE02A_DAR0022"
    $ current_voice = "voice/NAE02A_DAR0022.ogg"
    "至" "「可乐、不喝吗？　零卡路里、即使在减肥也不用担心啊」"

    $ gd["RCVmailData"][gc["ScriptMacros"]["RM_NAE_RECV_FEI02_01"]]["late"]=True
    $ lml.append(gc["ScriptMacros"]["RM_NAE_RECV_FEI02_01"])

    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0037"
    $ current_voice = "voice/NAE02A_NAE0037.ogg"
    "绹" "「桶子叔叔、那个、能告诉我吗？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CSA04"),"True","lh/DAR_CSA04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "NAE02A_DAR0023"
    $ current_voice = "voice/NAE02A_DAR0023.ogg"
    "至" "「诶？　什么？」"
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0038"
    $ current_voice = "voice/NAE02A_NAE0038.ogg"
    "绹" "「两年前的夏天，发生了什么？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CSA11"),"True","lh/DAR_CSA11a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    "之前在游戏中心看到Ｄｕｃｋ叔叔──不，是桶子叔叔并追上去时，一点也没想到过问的那样的事。"
    "但是现在稍微冷静了下来，看到这个从两年前到现在体型也好言行也好没有丝毫改变的人。"
    "感觉像是时间突然回到了那个夏天。"
    "然后就，不小心，问出来了。"
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0039"
    $ current_voice = "voice/NAE02A_NAE0039.ogg"
    "绹" "「为什么大家，都突然不见了？」"
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0040"
    $ current_voice = "voice/NAE02A_NAE0040.ogg"
    "绹" "「Ｌａｂｍｅｍ，已经没法再一起了吗？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CSA03"),"True","lh/DAR_CSA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "NAE02A_DAR0024"
    $ current_voice = "voice/NAE02A_DAR0024.ogg"
    "至" "「…………」"
    "一直嘻嘻哈哈的桶子叔叔的表情，变了。"
    "总感觉很寂寞一样。"
    $ stopvoc("DAR")
    play DAR "NAE02A_DAR0025"
    $ current_voice = "voice/NAE02A_DAR0025.ogg"
    "至" "「已经，没法再一起了哟」"
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0041"
    $ current_voice = "voice/NAE02A_NAE0041.ogg"
    "绹" "「诶……」"
    $ stopvoc("DAR")
    play DAR "NAE02A_DAR0026"
    $ current_voice = "voice/NAE02A_DAR0026.ogg"
    "至" "「未来道具研究所，在空中解体了。大家，都各奔东西了……」"
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0042"
    $ current_voice = "voice/NAE02A_NAE0042.ogg"
    "绹" "「…………」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CSA02"),"True","lh/DAR_CSA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "NAE02A_DAR0027"
    $ current_voice = "voice/NAE02A_DAR0027.ogg"
    "至" "「顺便，我去年一年就一直在瑞士啊！是把世界骑在身下的超级黑客哦」"
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0043"
    $ current_voice = "voice/NAE02A_NAE0043.ogg"
    "绹" "「瑞士……。是旅行吗？」"
    $ stopvoc("DAR")
    play DAR "NAE02A_DAR0028"
    $ current_voice = "voice/NAE02A_DAR0028.ogg"
    "至" "「嗯、是的。冈伦和牧濑也一起」"
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0044"
    $ current_voice = "voice/NAE02A_NAE0044.ogg"
    "绹" "「冈伦叔叔……和红莉栖姐姐……」"
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0045"
    $ current_voice = "voice/NAE02A_NAE0045.ogg"
    "绹" "「三个人、一起？」"
    $ stopvoc("DAR")
    play DAR "NAE02A_DAR0029"
    $ current_voice = "voice/NAE02A_DAR0029.ogg"
    "至" "「是啊」"
    "……三人。"
    "得知那个回答，内心深处揪紧了一般地难受了起来。"
    "这之中、没有那个人的名字。"
    "……真由理姐姐。"
    hide screen phoneSD1
    window hide


    $ loadBG(0,"BG05A1")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_AMA02"),"True","lh/MAY_AMA02a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    hide screen phonebtn
    "在Ｌａｂｍｅｍ里，我最喜欢的人。"
    "会一直用温柔地笑容抱着我。"
    "好像母亲一样。"
    "和冈伦叔叔总是在一起。"
    window hide


    $ loadBG(0,"BG_BLACK")

    "然而却，没有一起去瑞士的样子。"
    "……隐隐约约，察觉到了。"
    "真由理姐姐，也消失了。"
    "而且，也许是在那个父亲的大楼里。"
    "那个时候我因为父亲的死而忙得不可开交，真由理姐姐到底遭遇了什么，葬礼也没有参加，具体我并不知道。"
    "但是，留未穗姐姐和柳林神社的琉华姐姐对我说的，总觉得，我能明白。"
    "真由理姐姐，已经不在了。"
    "现在桶子叔叔的话里，也是一样。"
    window hide

    $ loadBG(0,"BG21A")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CSA01"),"True","lh/DAR_CSA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    show screen phonebtn
    show screen phoneSD1
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0046"
    $ current_voice = "voice/NAE02A_NAE0046.ogg"
    "绹" "「为什么，会去外国呢？」"
    $ stopvoc("DAR")
    play DAR "NAE02A_DAR0030"
    $ current_voice = "voice/NAE02A_DAR0030.ogg"
    "至" "「我是被强行拉去的哦」"
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0047"
    $ current_voice = "voice/NAE02A_NAE0047.ogg"
    "绹" "「诶？」"
    "强行？"
    $ stopvoc("DAR")
    play DAR "NAE02A_DAR0031"
    $ current_voice = "voice/NAE02A_DAR0031.ogg"
    "至" "「我们被坏人抓到被关起来一年半多了吧……我和冈伦历尽千难万险才逃脱，这样才回到了日本。」"
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0048"
    $ current_voice = "voice/NAE02A_NAE0048.ogg"
    "绹" "「是、是这样啊……」"
    "呃、这个是……玩笑、吗？"
    "桶子叔叔的表情，还是和刚才一样。"
    "说的是认真的吗，还是谎话，我也分不清，头大了。"
    "能用留未穗姐的“柴郡猫・什么的”能力就好了，我这么想着。"
    "果然，无论我再怎么逞强，都还只是个孩子吗。"
    "大人是在说着真话呢还是说谎，我都没法辨别。"
    "好不甘心。"
    "所以，我有些上头了。"
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0049"
    $ current_voice = "voice/NAE02A_NAE0049.ogg"
    "绹" "「我父亲死的理由、你知道吗？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CSA04"),"True","lh/DAR_CSA04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "NAE02A_DAR0032"
    $ current_voice = "voice/NAE02A_DAR0032.ogg"
    "至" "「诶？……」"
    "刚才，桶子叔叔吃了一惊。他的表情，连我都看懂了。"
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0050"
    $ current_voice = "voice/NAE02A_NAE0050.ogg"
    "绹" "「你、知道些什么吗？」"
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0051"
    $ current_voice = "voice/NAE02A_NAE0051.ogg"
    "绹" "「请告诉我」"
    "我紧紧地看着他，向他问道。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CSA09"),"True","lh/DAR_CSA09a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "NAE02A_DAR0033"
    $ current_voice = "voice/NAE02A_DAR0033.ogg"
    "至" "「……呃、嗯，那个……我也、不是很清楚啊」"
    $ stopvoc("DAR")
    play DAR "NAE02A_DAR0034"
    $ current_voice = "voice/NAE02A_DAR0034.ogg"
    "至" "「而且啊、从那之后不是已经过了两年嘛？　事到如今来说、也有些空口无凭啊」"
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0052"
    $ current_voice = "voice/NAE02A_NAE0052.ogg"
    "绹" "「又是、这样子啊……」"
    "留未穗姐也是。"
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0053"
    $ current_voice = "voice/NAE02A_NAE0053.ogg"
    "绹" "「虽然我问了，但谁也、不告诉我」"
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0054"
    $ current_voice = "voice/NAE02A_NAE0054.ogg"
    "绹" "「是因为、我是小孩子吗？」"
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0055"
    $ current_voice = "voice/NAE02A_NAE0055.ogg"
    "绹" "「不是两年前的、当事者吗？」"
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0056"
    $ current_voice = "voice/NAE02A_NAE0056.ogg"
    "绹" "「…………」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CSB03"),"True","lh/DAR_CSB03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_SAHSEN"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_SAHSEN"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_SAHSEN"])
    $ stopvoc("DAR")
    play DAR "NAE02A_DAR0035"
    $ current_voice = "voice/NAE02A_DAR0035.ogg"
    "至" "「{color=#f00}抱歉鸟{/color}……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CSB01"),"True","lh/DAR_CSB01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "NAE02A_DAR0036"
    $ current_voice = "voice/NAE02A_DAR0036.ogg"
    "至" "「不管怎么样、我觉得绹酱和我们现在已经是毫无关系的人了。」"
    $ stopvoc("DAR")
    play DAR "NAE02A_DAR0037"
    $ current_voice = "voice/NAE02A_DAR0037.ogg"
    "至" "「那么」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    "桶子叔叔把喝完了的可乐罐往垃圾箱扔去，一个人抬腿走了。"
    "我自然地追了上去。"
    window hide



    $ loadBG(0,"BG23A")

    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0057"
    $ current_voice = "voice/NAE02A_NAE0057.ogg"
    "绹" "「你、会一直在秋叶原吗？」"
    $ stopvoc("DAR")
    play DAR "NAE02A_DAR0038"
    $ current_voice = "voice/NAE02A_DAR0038.ogg"
    "至" "「也不，大概下周就不会在了吧」"
    "下周之前么……。"
    "像两年前一样，不准备在这条街道上安居。"
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0058"
    $ current_voice = "voice/NAE02A_NAE0058.ogg"
    "绹" "「那为什么、现在却回到了秋叶原呢？」"
    $ stopvoc("DAR")
    play DAR "NAE02A_DAR0039"
    $ current_voice = "voice/NAE02A_DAR0039.ogg"
    "至" "「稍微有点事喔」"
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0059"
    $ current_voice = "voice/NAE02A_NAE0059.ogg"
    "绹" "「冈伦叔叔呢？」"
    $ stopvoc("DAR")
    play DAR "NAE02A_DAR0040"
    $ current_voice = "voice/NAE02A_DAR0040.ogg"
    "至" "「没有来呢」"
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0060"
    $ current_voice = "voice/NAE02A_NAE0060.ogg"
    "绹" "「接下来要去哪里？」"
    $ stopvoc("DAR")
    play DAR "NAE02A_DAR0041"
    $ current_voice = "voice/NAE02A_DAR0041.ogg"
    "至" "「……研究所」"
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0061"
    $ current_voice = "voice/NAE02A_NAE0061.ogg"
    "绹" "「研究所……」"
    "“Ｌａｂｍｅｍ”的人们称之为研究所的地方。"
    "只会、有一个。"
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0062"
    $ current_voice = "voice/NAE02A_NAE0062.ogg"
    "绹" "「要去……那栋大楼吗？」"
    $ stopvoc("DAR")
    play DAR "NAE02A_DAR0042"
    $ current_voice = "voice/NAE02A_DAR0042.ogg"
    "至" "「嘛，你如果能对别人保密就帮了大忙了」"

    $ targetmailid = 462

    $ LR_RM_CHANCE=4
    call CHECK_RM_RECEIVE
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0063"
    $ current_voice = "voice/NAE02A_NAE0063.ogg"
    "绹" "「那里，上着锁哦」"
    call CHECK_RM_RECEIVE
    $ stopvoc("DAR")
    play DAR "NAE02A_DAR0043"
    $ current_voice = "voice/NAE02A_DAR0043.ogg"
    "至" "「绹酱、你有钥匙吗？」"
    call CHECK_RM_RECEIVE
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0064"
    $ current_voice = "voice/NAE02A_NAE0064.ogg"
    "绹" "「有是有……」"

    stop bgm 
    call CHECK_RM_RECEIVE
    $ stopvoc("DAR")
    play DAR "NAE02A_DAR0044"
    $ current_voice = "voice/NAE02A_DAR0044.ogg"
    "至" "「……真的？」"

    call CHECK_RM_RECEIVE
    "看来，桶子叔叔以为我是开他的玩笑了。"
    "听到我的回答，非常惊讶。"
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0065"
    $ current_voice = "voice/NAE02A_NAE0065.ogg"
    "绹" "「父亲死了……、所以、我就成为了它的所有者。」"
    "虽然仅仅是名义上的。"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CSA01"),"True","lh/DAR_CSA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    play bgm "FD2BGM07"
    "桶子叔叔转过身来。"
    $ stopvoc("DAR")
    play DAR "NAE02A_DAR0045"
    $ current_voice = "voice/NAE02A_DAR0045.ogg"
    "至" "「再问一句，４２型布朗管电视机、现在也还在那吗？」"
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0066"
    $ current_voice = "voice/NAE02A_NAE0066.ogg"
    "绹" "「４２型……」"
    "是店里的显像管电视机里，最大的家伙。"
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0067"
    $ current_voice = "voice/NAE02A_NAE0067.ogg"
    "绹" "「大概、是放着的吧。从父亲死了以后、什么也没有带出来。」"
    "没有父亲的许可，也不能处置店里的老式电视机。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CSA05"),"True","lh/DAR_CSA05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "NAE02A_DAR0046"
    $ current_voice = "voice/NAE02A_DAR0046.ogg"
    "至" "「好、好！」"
    "桶子叔叔一个人兴奋地点起头。"
    $ stopvoc("DAR")
    play DAR "NAE02A_DAR0047"
    $ current_voice = "voice/NAE02A_DAR0047.ogg"
    "至" "「绹酱、店里的钥匙、能不能稍微借我下？」"
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0068"
    $ current_voice = "voice/NAE02A_NAE0068.ogg"
    "绹" "「…………」"
    $ stopvoc("DAR")
    play DAR "NAE02A_DAR0048"
    $ current_voice = "voice/NAE02A_DAR0048.ogg"
    "至" "「不行？」"

    $ gd["RCVmailData"][gc["ScriptMacros"]["RM_NAE_RECV_RUK01_01"]]["late"]=True
    $ lml.append(gc["ScriptMacros"]["RM_NAE_RECV_RUK01_01"])

    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0069"
    $ current_voice = "voice/NAE02A_NAE0069.ogg"
    "绹" "「你要在那里面，做些什么呢？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CSA06"),"True","lh/DAR_CSA06a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "NAE02A_DAR0049"
    $ current_voice = "voice/NAE02A_DAR0049.ogg"
    "至" "「这……」"
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0070"
    $ current_voice = "voice/NAE02A_NAE0070.ogg"
    "绹" "「什么也不告诉我、就要借走钥匙。这、这样的……如意算盘、打得太好了吧。」"
    "我鼓起勇气，抗诉道。"
    $ stopvoc("DAR")
    play DAR "NAE02A_DAR0050"
    $ current_voice = "voice/NAE02A_DAR0050.ogg"
    "至" "「嗯……、虽然冈伦说不让我告诉任何人……」"
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0071"
    $ current_voice = "voice/NAE02A_NAE0071.ogg"
    "绹" "「…………」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CSA02"),"True","lh/DAR_CSA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "NAE02A_DAR0051"
    $ current_voice = "voice/NAE02A_DAR0051.ogg"
    "至" "「绹酱、你能保守秘密？口风严实么？」"
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0072"
    $ current_voice = "voice/NAE02A_NAE0072.ogg"
    "绹" "「没事的」"
    "虽然、从前，铃羽姐姐就说过“绹有一不小心就泄漏秘密的坏习惯”。"
    "是在，两年前了。"
    "现在成为了中学生，一定不会的。"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CLB02"),"True","lh/DAR_CLB02a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "NAE02A_DAR0052"
    $ current_voice = "voice/NAE02A_DAR0052.ogg"
    "至" "「……这个、可是和谁都不能说的啊。绝对不能说啊」"
    $ stopvoc("DAR")
    play DAR "NAE02A_DAR0053"
    $ current_voice = "voice/NAE02A_DAR0053.ogg"
    "至" "「事实上啊」"
    $ stopvoc("DAR")
    play DAR "NAE02A_DAR0054"
    $ current_voice = "voice/NAE02A_DAR0054.ogg"
    "至" "「我们在向，过去，发送邮件哦」"
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0073"
    $ current_voice = "voice/NAE02A_NAE0073.ogg"
    "绹" "「……请别开玩笑了，我，是认真在说的」"
    $ stopvoc("DAR")
    play DAR "NAE02A_DAR0055"
    $ current_voice = "voice/NAE02A_DAR0055.ogg"
    "至" "「我超认真的说」"
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0074"
    $ current_voice = "voice/NAE02A_NAE0074.ogg"
    "绹" "「因为、向过去发送邮件什么的、这样的——」"
    "我这么说着，又想起来了。"
    hide screen phoneSD1
    window hide


    $ loadBG(0,"BG79A2",at=[Transform(yalign=1.0)])





    hide screen phonebtn
    "两年前。"
    "我去父亲的店里玩的时候。"
    window hide





    "从二楼的窗户，经常听到冈伦叔等人的说话声。"
    "在那里，经常听到的词句，那是——"
    window hide


    $ loadBG(0,"BG23A")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CLB02"),"True","lh/DAR_CLB02a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    show screen phonebtn
    show screen phoneSD1
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0075"
    $ current_voice = "voice/NAE02A_NAE0075.ogg"
    "绹" "「时间……机器……」"
    $ stopvoc("DAR")
    play DAR "NAE02A_DAR0056"
    $ current_voice = "voice/NAE02A_DAR0056.ogg"
    "至" "「Ｅｘｃａｔｌｙ。就是那么回事」"
    $ stopvoc("DAR")
    play DAR "NAE02A_DAR0057"
    $ current_voice = "voice/NAE02A_DAR0057.ogg"
    "至" "「两年前，我们发明了这个」"
    "为啥，听上去不是骗我的呢。"
    "那么，如果是真的的话。"
    "真由理姐姐死了这件事也好。"
    "“Ｌａｂｍｅｍ”的神秘消失也好。"
    "桶子叔叔也被抓到了外国。"
    "都可以理解了。"
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0076"
    $ current_voice = "voice/NAE02A_NAE0076.ogg"
    "绹" "「向过去……发邮件……是真的……？」"
    $ stopvoc("DAR")
    play DAR "NAE02A_DAR0058"
    $ current_voice = "voice/NAE02A_DAR0058.ogg"
    "至" "「虽然我们叫它Ｄｍａｉｌ。不是从实验室就发不了呢。」"
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0077"
    $ current_voice = "voice/NAE02A_NAE0077.ogg"
    "绹" "「时间机器，就藏在那里吗？」"
    $ stopvoc("DAR")
    play DAR "NAE02A_DAR0059"
    $ current_voice = "voice/NAE02A_DAR0059.ogg"
    "至" "「虽然藏着，大概也已经被Ｒｏｕｎｄｅｒ回收了，不重新再造一个不行啊」"
    "Ｒｏｕｎｄｅｒ，都是谁呢？"
    $ stopvoc("DAR")
    play DAR "NAE02A_DAR0060"
    $ current_voice = "voice/NAE02A_DAR0060.ogg"
    "至" "「不管怎么样了，我都必须去那个研究所」"
    $ stopvoc("DAR")
    play DAR "NAE02A_DAR0061"
    $ current_voice = "voice/NAE02A_DAR0061.ogg"
    "至" "「不然的话，之后各种事情就不好办了」"
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0078"
    $ current_voice = "voice/NAE02A_NAE0078.ogg"
    "绹" "「…………」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CLB02"),"True","lh/DAR_CLB02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "NAE02A_DAR0062"
    $ current_voice = "voice/NAE02A_DAR0062.ogg"
    "至" "「所以就这样！　请借给我吧！」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    "低下了头。"
    "声音，却非常大。"
    "周围的人，又要看过来了。"
    "而且。"
    stop bgm 
    $ stopvoc("Y19")
    play KUR "NAE02A_Y190000"
    $ current_voice = "voice/NAE02A_Y190000.ogg"
    "警官" "「那边的你们两个」"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CMB04"),"True","lh/DAR_CMB04a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "NAE02A_DAR0063"
    $ current_voice = "voice/NAE02A_DAR0063.ogg"
    "至" "「咳」"
    "正好路过的巡警先生、朝我们问话了。"
    " 确实我和桶子叔叔的组合，非常的，奇怪。"
    $ stopvoc("Y19")
    play KUR "NAE02A_Y190001"
    $ current_voice = "voice/NAE02A_Y190001.ogg"
    "警官" "「你没事吧？」"
    "巡警先生、并没有看桶子叔叔，而是对着我的眼睛询问着。"
    $ stopvoc("DAR")
    play DAR "NAE02A_DAR0064"
    $ current_voice = "voice/NAE02A_DAR0064.ogg"
    "至" "「不不，我不是什么奇怪的人，也没在做任何坏事，即使我在二次元中是萝莉控吧，但是在三次元的做出这种事什么的——」"
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0079"
    $ current_voice = "voice/NAE02A_NAE0079.ogg"
    "绹" "「桶子叔叔、你、自爆了」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CMB03"),"True","lh/DAR_CMB03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "NAE02A_DAR0065"
    $ current_voice = "voice/NAE02A_DAR0065.ogg"
    "至" "「呜……」"
    $ stopvoc("Y19")
    play KUR "NAE02A_Y190002"
    $ current_voice = "voice/NAE02A_Y190002.ogg"
    "警官" "「你们两个是什么关系？」"
    $ stopvoc("DAR")
    play DAR "NAE02A_DAR0066"
    $ current_voice = "voice/NAE02A_DAR0066.ogg"
    "至" "「那个、那是……」"
    "桶子叔叔朝我投来了求救的目光。"
    "我小小地叹了一口气。"
    play bgm "BGM16"

    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0080"
    $ current_voice = "voice/NAE02A_NAE0080.ogg"
    "绹" "「堂兄妹」"
    $ stopvoc("Y19")
    play KUR "NAE02A_Y190003"
    $ current_voice = "voice/NAE02A_Y190003.ogg"
    "警官" "「诶？」"
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0081"
    $ current_voice = "voice/NAE02A_NAE0081.ogg"
    "绹" "「是堂兄妹」"
    $ stopvoc("Y19")
    play KUR "NAE02A_Y190004"
    $ current_voice = "voice/NAE02A_Y190004.ogg"
    "警官" "「但是刚才、叔叔叫的」"
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0082"
    $ current_voice = "voice/NAE02A_NAE0082.ogg"
    "绹" "「也只是这样称呼」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CMB04"),"True","lh/DAR_CMB04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "NAE02A_DAR0067"
    $ current_voice = "voice/NAE02A_DAR0067.ogg"
    "至" "「啊、是的、是的！　堂兄妹！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CMA02"),"True","lh/DAR_CMA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "NAE02A_DAR0068"
    $ current_voice = "voice/NAE02A_DAR0068.ogg"
    "至" "「话说、我明明才２１，叔叔叫个不停、有点太过分了？」"
    $ stopvoc("Y19")
    play KUR "NAE02A_Y190005"
    $ current_voice = "voice/NAE02A_Y190005.ogg"
    "警官" "「…………」"
    $ stopvoc("Y19")
    play KUR "NAE02A_Y190006"
    $ current_voice = "voice/NAE02A_Y190006.ogg"
    "警官" "「是这样啊。我失礼了」"
    "虽然还扭头看着我们，巡警先生还是从我们身前离开了。"
    "桶子叔叔吐了一口大气。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CMB03"),"True","lh/DAR_CMB03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "NAE02A_DAR0069"
    $ current_voice = "voice/NAE02A_DAR0069.ogg"
    "至" "「呼、好危险。真够险的。要是这样被抓了的话会被由季碳杀掉的……」"
    "由季碳，说来的话，好像听过这个名字，但关于这个我没有寻根问底的想法。"
    "而且。"
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0083"
    $ current_voice = "voice/NAE02A_NAE0083.ogg"
    "绹" "「今天，这是第二回，帮了桶子叔叔你的忙了啊」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CMB01"),"True","lh/DAR_CMB01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "NAE02A_DAR0070"
    $ current_voice = "voice/NAE02A_DAR0070.ogg"
    "至" "「嗯啊？　嘛、好像是这样了啊」"
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0084"
    $ current_voice = "voice/NAE02A_NAE0084.ogg"
    "绹" "「才不是好像。就是呀」"
    "我在两年前，并没能成为当事人。"
    "造成了我现在什么都不知道的情况。"
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0085"
    $ current_voice = "voice/NAE02A_NAE0085.ogg"
    "绹" "「所以说，作为回报──」"
    "所以呢，只能自己跳进里面。"
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0086"
    $ current_voice = "voice/NAE02A_NAE0086.ogg"
    "绹" "「也让我来一起，发那个Ｄｍａｉｌ吧」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CMB04"),"True","lh/DAR_CMB04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "NAE02A_DAR0071"
    $ current_voice = "voice/NAE02A_DAR0071.ogg"
    "至" "「呃、这……」"
    "发完会变得怎样呢、我也只是一瞬间闪过。"
    "说到底我要向谁，发送怎样内容的邮件呢。"
    "我马上给出了答案。"
    hide screen phoneSD1
    window hide


    $ loadBG(0,"BG_BLACK")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='TEN')",DynamicDisplayable(mouthanime,"TEN_BSA01"),"True","lh/TEN_BSA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    hide screen phonebtn
    "我要，问问我的父亲。"
    "──两年前，为什么抛下我不管了呢？"
    window hide


    $ loadBG(0,"BG23A")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CMB04"),"True","lh/DAR_CMB04a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    show screen phonebtn
    show screen phoneSD1
    "只是，比质问的内容更重要的是。"
    "我想要借由在这里“跳进去”，成为两年前没能成为的当事人。"
    hide screen phoneSD1
    window hide

    stop bgm 



    $ loadBG(0,"IBGX033")

    hide screen phonebtn
    show screen phoneSD1
    play bgm "FD2BGM01"
    "桶子叔叔抱头苦恼了半个钟头，终于才接受了我的请求。"
    "向过去，发送Ｄｍａｉｌ。"
    "据桶子叔叔说，结果会有很大的差异。"
    "简单的说，从过去到未来可能会产生巨大的变化，也可能什么变化都不会发生。"
    "而且，即使能改变过去，对发送邮件的我和桶子叔叔来说，变化是无法确定的。"
    "清楚知晓变化的人似乎只有冈伦叔一个。"
    "不知道发生了变化的话也就没有意义了啊……我虽是这么想。"
    "要是在这里抱怨的话，桶子叔叔转变心思就麻烦了，"
    $ stopvoc("DAR")
    play DAR "NAE02A_DAR0072"
    $ current_voice = "voice/NAE02A_DAR0072.ogg"
    "至" "「你说、真的被监视了吗？」"
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0087"
    $ current_voice = "voice/NAE02A_NAE0087.ogg"
    "绹" "「要是太明目张胆的话、马上就会被发现」"
    "我和桶子叔叔来到了父亲大楼的附近。"
    "藏在隐蔽处，窥伺着大楼的情况。"
    window hide


    $ loadBG(2,"BG79E5",at=[Transform(yalign=1.0)])







    hide screen phonebtn
    "虽然才傍晚，街道上就完全看不到人了。"
    "从这一处看来，大楼也没有发生特别的变化。"
    $ stopvoc("DAR")
    play DAR "NAE02A_DAR0073"
    $ current_voice = "voice/NAE02A_DAR0073.ogg"
    "至" "「闲到这种地步啊，那群家伙。」"
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0088"
    $ current_voice = "voice/NAE02A_NAE0088.ogg"
    "绹" "「但是刚才，桶子叔叔你才被追着的」"
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0089"
    $ current_voice = "voice/NAE02A_NAE0089.ogg"
    "绹" "「那群人、跟丢了你之后，也许来了这边也说不定哟」"
    stop bgm 
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0090"
    $ current_voice = "voice/NAE02A_NAE0090.ogg"
    "绹" "「……啊！」"
    window hide


    $ loadBG(2,"BG_BLACK")




    hide screen phonebtn
    play bgm "BGM07"
    "我慌忙拉着桶子叔叔的手，躲到了暗处。"
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0091"
    $ current_voice = "voice/NAE02A_NAE0091.ogg"
    "绹" "「刚才，看到了！」"
    $ stopvoc("DAR")
    play DAR "NAE02A_DAR0074"
    $ current_voice = "voice/NAE02A_DAR0074.ogg"
    "至" "「真的？」"
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0092"
    $ current_voice = "voice/NAE02A_NAE0092.ogg"
    "绹" "「父亲大楼对面的那个杂居大楼，原本应该是空置着的那边的三楼里，却偶尔能看到人影」"
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0093"
    $ current_voice = "voice/NAE02A_NAE0093.ogg"
    "绹" "「现在也在那儿，不止一个人。三个」"
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0094"
    $ current_voice = "voice/NAE02A_NAE0094.ogg"
    "绹" "「是“黑衣人”……」"
    $ stopvoc("DAR")
    play DAR "NAE02A_DAR0075"
    $ current_voice = "voice/NAE02A_DAR0075.ogg"
    "至" "「嗯？哪儿哪儿……」"
    window hide


    $ loadBG(2,"IBGX033")



    "听了我的说明，桶子叔叔再次观察起了情况。"
    "然后立刻就缩回了头。"
    window hide


    $ loadBG(2,"BG_BLACK")



    $ stopvoc("DAR")
    play DAR "NAE02A_DAR0076"
    $ current_voice = "voice/NAE02A_DAR0076.ogg"
    "至" "「喂、真的在啊……！」"
    window hide



    $ loadBG(0,"BG18E2")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CSA02"),"True","lh/DAR_CSA02a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    show screen phonebtn
    show screen phoneSD1
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0095"
    $ current_voice = "voice/NAE02A_NAE0095.ogg"
    "绹" "「我又帮了桶子叔叔你一次呢」"
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0096"
    $ current_voice = "voice/NAE02A_NAE0096.ogg"
    "绹" "「如果、桶子叔叔你一个人就这样朝着大楼过去的话，现在就已经被“黑衣人”抓住了」"
    $ stopvoc("DAR")
    play DAR "NAE02A_DAR0077"
    $ current_voice = "voice/NAE02A_DAR0077.ogg"
    "至" "「难道绹酱、你喜欢我？　不是喜欢我的话、不会有中学生帮我三次这样的事情哦」"
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0097"
    $ current_voice = "voice/NAE02A_NAE0097.ogg"
    "绹" "「…………」"
    "为什么这个人总说着这么蠢的话，不肯说认真的呢。"
    "这么说来、冈伦叔也是这样的感觉。"
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0098"
    $ current_voice = "voice/NAE02A_NAE0098.ogg"
    "绹" "「还有其他的进去的办法吗？从相邻的大楼跳过去之类的」"
    "父亲大楼的左右两旁，也建着同样的杂居大楼。"
    "之间的间隙，人不能通过。"
    $ stopvoc("DAR")
    play DAR "NAE02A_DAR0078"
    $ current_voice = "voice/NAE02A_DAR0078.ogg"
    "至" "「这么说来，打开实验室厕所的窗户的话，能够看到后面大楼的窗户」"
    $ stopvoc("DAR")
    play DAR "NAE02A_DAR0079"
    $ current_voice = "voice/NAE02A_DAR0079.ogg"
    "至" "「里面……、外面？　昌平桥路边的大楼。拉面店旁边两家左右」"
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0099"
    $ current_voice = "voice/NAE02A_NAE0099.ogg"
    "绹" "「从那边的话、也许可以悄悄地潜进去」"
    "只要进去了的话，这边的人。"
    "只要不开灯，不弄出声响，从外面是不会知道里面有没有人的。"
    "总觉得像间谍一样的心惊，害怕。"
    "与此同时的，也感到激动与兴奋。"

    stop bgm 
    hide screen phoneSD1
    window hide


    $ loadBG(2,"BG_BLACK")



    hide screen phonebtn
    "虽然……这么感觉着……"

    window hide



    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_NAE003A"]]["Check"]=True
    $ loadBG(0,"EV_NAE003A")



    hide screen phonebtn





    $ stopvoc("DAR")
    play DAR "NAE02A_DAR0080"
    $ current_voice = "voice/NAE02A_DAR0080.ogg"
    "至" "「噗叽叽叽……」"


    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0100"
    $ current_voice = "voice/NAE02A_NAE0100.ogg"
    "绹" "「糟了……」"
    play bgm "FD2BGM10"
    "我眼前是一个，大尻。"
    "臃肿的腿踏足的样子，简直和猪一样。"
    "后面大楼走廊的小窗户与实验室的窗之间，有２０厘米左右的空隙，而且，运气非常好的是，厕所的窗户没有锁上。"
    "因此桶子叔叔就想马上穿过窗户。"
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0101"
    $ current_voice = "voice/NAE02A_NAE0101.ogg"
    "绹" "「太胖了啊，桶子叔叔……」"
    "肥大的肚子与屁股，被狭小的窗框卡住了。"
    $ stopvoc("DAR")
    play DAR "NAE02A_DAR0081"
    $ current_voice = "voice/NAE02A_DAR0081.ogg"
    "至" "「这样的感想什么都好、你、绹酱、想点办法啊……！」"
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0102"
    $ current_voice = "voice/NAE02A_NAE0102.ogg"
    "绹" "「就算你叫我想办法……」"
    "该怎么办才好呢。"
    "虽然不太想碰他。"
    "但是，这样下去就会被“黑衣人”发现了。"
    "没有办法啊……。"
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0103"
    $ current_voice = "voice/NAE02A_NAE0103.ogg"
    "绹" "「那么，我推了」"
    window hide
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_NAE003B"]]["Check"]=True


    $ loadBG(2,"EV_NAE003B")



    "双手使劲、往大屁股上推去。"
    "我的手，好像要沉没在屁股的肉中的感触。"
    "我感觉很难受。"
    "手臂上起了鸡皮疙瘩。"





    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0104"
    $ current_voice = "voice/NAE02A_NAE0104.ogg"
    "绹" "「唔～……！」"


    $ stopvoc("DAR")
    play DAR "NAE02A_DAR0082"
    $ current_voice = "voice/NAE02A_DAR0082.ogg"
    "至" "「啊～、感觉不错哦、在用力点也没关系哦。偶尔磨蹭两下就更好了」"





    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0105"
    $ current_voice = "voice/NAE02A_NAE0105.ogg"
    "绹" "「唔唔～……！」"


    "不管怎么推也一动不动。"
    "我想放弃，把这人丢在这不管，就这么走掉。"
    "但是，那样的话，我又会什么也不知道了。"
    "那样的，我不要。"





    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0106"
    $ current_voice = "voice/NAE02A_NAE0106.ogg"
    "绹" "「你、这～……！」"


    "不加油的话……！"
    "这次不是只手，肩膀也用上了。"
    $ stopvoc("DAR")
    play DAR "NAE02A_DAR0083"
    $ current_voice = "voice/NAE02A_DAR0083.ogg"
    "至" "「哞咻……！　啊，不好，被女中学生摸到那种地方……我的大斧已经饥渴难耐了……！」"
    "无视桶子叔叔的变态发言，我使出全身的力气推了进去。"





    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0107"
    $ current_voice = "voice/NAE02A_NAE0107.ogg"
    "绹" "「呼嗯～……！」"


    $ stopvoc("DAR")
    play DAR "NAE02A_DAR0084"
    $ current_voice = "voice/NAE02A_DAR0084.ogg"
    "至" "「呃、啊、痛、痛痛痛、喂、等！　等等啊、卡住了……」"
    window hide
    stop bgm 


    $ loadBG(2,"BG_BLACK")



    $ stopvoc("DAR")
    play DAR "NAE02A_DAR0085"
    $ current_voice = "voice/NAE02A_DAR0085.ogg"
    "至" "「啊——！」"

    window hide


    $ loadBG(0,"BG02E3")

    show screen phonebtn
    show screen phoneSD1
    "费了相当的功夫，才把桶子叔叔救了出来，潜入了实验室。"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CSB03"),"True","lh/DAR_CSB03a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0108"
    $ current_voice = "voice/NAE02A_NAE0108.ogg"
    "绹" "「…………」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    "我一面保持着与向着大街的窗户的距离，一面扫视着房间。"
    "已经废弃了两年了，这里积累了相当多的灰尘。"
    window hide
    play bgm "FD2BGM06"
    $ loadBG(0,"BG02E3S1",png=True)


    hide screen phonebtn
    "呜帕的玩偶。"
    $ loadBG(0,"BG02E3S2",png=True)


    "很多我不太懂的破烂。"
    $ loadBG(0,"BG02E3S3",png=True)


    "白板上写着，复杂的说明和公式。"
    window hide

    hide background-png  with dissolve
    show screen phonebtn
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0109"
    $ current_voice = "voice/NAE02A_NAE0109.ogg"
    "绹" "「还真是、一点也没变」"
    "两年前的，那个喧闹的夏天。"
    "我也曾几次被邀来这个房间里玩。"
    "这里的声音，从不曾停息。"
    "真是吵到了烦人的程度。"
    hide screen phonebtn
    hide screen phoneSD1
    window hide


    $ stopvoc("OKA")
    play OKA "NAE02A_OKA0000"
    $ current_voice = "voice/NAE02A_OKA0000.ogg"
    "伦太郎" "呼——哈哈哈！助手、该实验的准备了！"
    $ stopvoc("CRS")
    play CRS "NAE02A_CRS0000"
    $ current_voice = "voice/NAE02A_CRS0000.ogg"
    "红莉栖" "呐，不要叫我助手，我说了多少次了……"
    $ stopvoc("MAY")
    play MAY "NAE02A_MAY0000"
    $ current_voice = "voice/NAE02A_MAY0000.ogg"
    "真由理" "嘟嘟噜♪　各位，要吃炸鸡块吗ー？"
    window hide


    show screen phonebtn
    show screen phoneSD1
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0110"
    $ current_voice = "voice/NAE02A_NAE0110.ogg"
    "绹" "「声音……」"
    "感觉还能听见啊。"
    "那个时候“Ｌａｂｍｅｍ”的声音。"
    "但是——"
    window hide
    stop bgm 
    $ loadBG(0,"BG02E3S4",png=True)




    hide screen phonebtn






    "注意到地板上红黑色的印记的时候，这份怀念之情也随之瞬间消散了。"


    window hide

    hide background-png  with dissolve
    show screen phonebtn
    "……那样的印记是什么的，我没有去想，背过了脸。"
    $ stopvoc("DAR")
    play DAR "NAE02A_DAR0087"
    $ current_voice = "voice/NAE02A_DAR0087.ogg"
    "至" "「居然和原来一样，他们还是太年轻了啊」"
    "桶子叔叔蹑手蹑脚地走向房间深处。"
    window hide



    $ loadBG(2,"BG03A6")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CSA02"),"True","lh/DAR_CSA02a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    play bgm "BGM19"

    $ stopvoc("DAR")
    play DAR "NAE02A_DAR0088"
    $ current_voice = "voice/NAE02A_DAR0088.ogg"
    "至" "「我用的电脑啊，电话，都还好好在这儿啊」"
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0111"
    $ current_voice = "voice/NAE02A_NAE0111.ogg"
    "绹" "「时间机器、做得出来吗？」"
    $ stopvoc("DAR")
    play DAR "NAE02A_DAR0089"
    $ current_voice = "voice/NAE02A_DAR0089.ogg"
    "至" "「这个就、全靠４２型了」"
    "４２型……。"
    "桶子叔叔还是非常的拘泥于这个啊。"
    "时间机器好像一定需要父亲店里放着的４２型布朗管电视机一样。"
    "那个不通电的话没法正常工作了。"

    $ stopvoc("DAR")
    play DAR "NAE02A_DAR0090"
    $ current_voice = "voice/NAE02A_DAR0090.ogg"
    "至" "「哦哦，这个洞不是可以用上吗？」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    "桶子叔叔就地钻了进去。"
    "把地板的一部分撕开，洞口就出现了。"
    window hide


    $ loadBG(2,"BG03A6R")



    hide screen phonebtn
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0112"
    $ current_voice = "voice/NAE02A_NAE0112.ogg"
    "绹" "「这样的洞，是什么时候开的？」"
    $ stopvoc("DAR")
    play DAR "NAE02A_DAR0091"
    $ current_voice = "voice/NAE02A_DAR0091.ogg"
    "至" "「做实验的时候搞的，但也不是特意开的，因为某些错误」"
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0113"
    $ current_voice = "voice/NAE02A_NAE0113.ogg"
    "绹" "「和我父亲说了吗？」"
    $ stopvoc("DAR")
    play DAR "NAE02A_DAR0092"
    $ current_voice = "voice/NAE02A_DAR0092.ogg"
    "至" "「怎么可能，在地板上开了个洞这种事情说出来，不会被从这里赶出去吗」"
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0114"
    $ current_voice = "voice/NAE02A_NAE0114.ogg"
    "绹" "「…………」"

    $ targetmailid = cml.setdefault("RM_NAE_SEND_RUK01","")

    $ LR_RM_CHANCE=4
    call CHECK_RM_RECEIVE
    "这可真是……。"
    call CHECK_RM_RECEIVE
    "桶子叔叔从洞里看了下去。"
    call CHECK_RM_RECEIVE
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0115"
    $ current_voice = "voice/NAE02A_NAE0115.ogg"
    "绹" "「这么一来我父亲、是被偷偷监视着了……」"
    call CHECK_RM_RECEIVE
    $ stopvoc("DAR")
    play DAR "NAE02A_DAR0093"
    $ current_voice = "voice/NAE02A_DAR0093.ogg"
    "至" "「是……啊——」"

    call CHECK_RM_RECEIVE
    $ stopvoc("DAR")
    play DAR "NAE02A_DAR0094"
    $ current_voice = "voice/NAE02A_DAR0094.ogg"
    "至" "「不啊、把这个洞打通的话、不就可以到下面店子里去了吗？」"
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0116"
    $ current_voice = "voice/NAE02A_NAE0116.ogg"
    "绹" "「这样啊。“黑衣人”在、不能从外面进到店子里啊」"
    "但是要是不能进到店子里的话，就不能给４２型通电了。"
    "不去店子里面把配电盘的电源打开给电视机通电的话。"
    $ stopvoc("DAR")
    play DAR "NAE02A_DAR0095"
    $ current_voice = "voice/NAE02A_DAR0095.ogg"
    "至" "「不错哟不错哟～、这个洞、好好干的话就能打通了」"
    window hide



    $ loadBG(2,"BG03A6")

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CSB01"),"True","lh/DAR_CSB01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    show screen phonebtn
    "桶子叔叔起身，拍了拍手上的灰。"
    "穿着的衣服上也满是灰，但好像不怎么在意的样子。"
    $ stopvoc("DAR")
    play DAR "NAE02A_DAR0096"
    $ current_voice = "voice/NAE02A_DAR0096.ogg"
    "至" "「有钢筋和管道我还以为不行呢、没想到这么顺利」"
    $ stopvoc("DAR")
    play DAR "NAE02A_DAR0097"
    $ current_voice = "voice/NAE02A_DAR0097.ogg"
    "至" "「这可是了不起的偶然哦，就算不是冈伦我都想说这是命运石之门的选择了，呼哈哈」"
    window hide


    $ loadBG(2,"BG02E3")



    "桶子叔叔像累了一样往沙发靠去，噗哇地扬起灰尘。"
    "防着咳嗽，我慌忙用手捂住嘴。"
    "外头“黑衣人”还在。"
    "不能发出声音。"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_CSA01"),"True","lh/DAR_CSA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "NAE02A_DAR0098"
    $ current_voice = "voice/NAE02A_DAR0098.ogg"
    "至" "「嘛，这之后还要把电话微波炉修好这件大事等着我啊」"
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0117"
    $ current_voice = "voice/NAE02A_NAE0117.ogg"
    "绹" "「能成吗？」"
    $ stopvoc("DAR")
    play DAR "NAE02A_DAR0099"
    $ current_voice = "voice/NAE02A_DAR0099.ogg"
    "至" "「虽说知道怎么做倒是」"
    $ stopvoc("DAR")
    play DAR "NAE02A_DAR0100"
    $ current_voice = "voice/NAE02A_DAR0100.ogg"
    "至" "「如果全部进展顺利的话、也就是能确实地发出Ｄｍａｉｌ的话、发出的时候就是决胜负的时刻了哦」"
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0118"
    $ current_voice = "voice/NAE02A_NAE0118.ogg"
    "绹" "「这样啊……」"
    "可是、我已经跳进事件当中了。"
    "而且，桶子叔叔也不会有在这里打住不干的想法。冒着风险，也来到了这个实验室。"
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0119"
    $ current_voice = "voice/NAE02A_NAE0119.ogg"
    "绹" "「帮了忙在先、……。什么都做」"
    "像两年前一样，一个人小宝宝一样等着谁回来一样，我不想再这样了。"

    stop bgm 
    hide screen phoneSD1
    window hide



    $ loadBG(0,"BG26N",trans=fade)


    show screen phoneSD1
    play bgm "BGM13"

    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0120"
    $ current_voice = "voice/NAE02A_NAE0120.ogg"
    "绹" "「我回来啦～……」"
    "发生了很多事，回来迟了呢。"
    "这样的时间回来，从寄居在秋叶家后，也许是第一次……。"
    "桶子叔叔，说是要暂时住在实验室一段时间的样子。"
    "会不会被“黑衣人”发现呢，不管会不会，反正从那个小窗户再出来难于登天，我表示理解接受了。"
    $ stopvoc("X02")
    play KUR "NAE02A_X020002"
    $ current_voice = "voice/NAE02A_X020002.ogg"
    "千佳音阿姨" "「绹酱，回来这么晚啊」"
    "千晶婶出来接我了。"
    "这个时候幸高伯还在工作。"
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0121"
    $ current_voice = "voice/NAE02A_NAE0121.ogg"
    "绹" "「嗯、抱歉」"
    $ stopvoc("X02")
    play KUR "NAE02A_X020003"
    $ current_voice = "voice/NAE02A_X020003.ogg"
    "千佳音阿姨" "「衣服、弄得很脏了啊？」"
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0122"
    $ current_voice = "voice/NAE02A_NAE0122.ogg"
    "绹" "「没关系的」"
    $ stopvoc("X02")
    play KUR "NAE02A_X020004"
    $ current_voice = "voice/NAE02A_X020004.ogg"
    "千佳音阿姨" "「是么？要送去洗的话就和我说哦」"
    $ stopvoc("X02")
    play KUR "NAE02A_X020005"
    $ current_voice = "voice/NAE02A_X020005.ogg"
    "千佳音阿姨" "「晚饭也快好了、快些换衣服吧」"
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0123"
    $ current_voice = "voice/NAE02A_NAE0123.ogg"
    "绹" "「嗯」"
    hide screen phoneSD1
    window hide



    $ loadBG(0,"BG73N")

    hide screen phonebtn
    play se "SGSE056"
    "要是平常，已经是吃完晚饭很久的时间了。"
    "千晶婶还特地等着我回来啊。"
    "感觉十分愧疚，急忙换了衣服。"
    "衣服比自己之前想象的还要脏。"
    $ stopvoc("FEI")
    play FEI "NAE02A_FEI0000"
    $ current_voice = "voice/NAE02A_FEI0000.ogg"
    "菲利斯" "「绹？　进来可以喵？」"
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0124"
    $ current_voice = "voice/NAE02A_NAE0124.ogg"
    "绹" "「……啊、请」"
    "是留未穗姐姐。"
    window hide
    play se "SGSE336"


    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_HSA02"),"True","lh/FEI_HSA02a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FEI")
    play FEI "NAE02A_FEI0001"
    $ current_voice = "voice/NAE02A_FEI0001.ogg"
    "菲利斯" "「欢迎回家。今天有些晚了呢」"
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0125"
    $ current_voice = "voice/NAE02A_NAE0125.ogg"
    "绹" "「嗯……」"
    "留未穗姐姐，是个奇怪的人。"
    "一直像猫一样，说话用喵来结尾。"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_RAINET_AB"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_RAINET_AB"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_RAINET_AB"])
    "作为{color=#f00}雷ＡｃｃｅｓｓＢａｔｔｌｅｒｓ{/color}的王者，于是加上了那样的角色设定，才这么说话的。她是这么告诉我的。"
    "但是，也没有平日就喵喵地说话的道理啊，我觉得。"
    "做着自己办的公司的事务的时候也是这样说着话的吗？"

    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_HSC01"),"True","lh/FEI_HSC01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FEI")
    play FEI "NAE02A_FEI0002"
    $ current_voice = "voice/NAE02A_FEI0002.ogg"
    "菲利斯" "「头发」"
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0126"
    $ current_voice = "voice/NAE02A_NAE0126.ogg"
    "绹" "「诶？」"
    $ stopvoc("FEI")
    play FEI "NAE02A_FEI0003"
    $ current_voice = "voice/NAE02A_FEI0003.ogg"
    "菲利斯" "「粘着灰尘喵」"
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0127"
    $ current_voice = "voice/NAE02A_NAE0127.ogg"
    "绹" "「啊」"
    "慌忙用手擦过头发。"
    "蜘蛛网什么的，够受的了。"
    "好想马上就去洗澡。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_HSB02"),"True","lh/FEI_HSB02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FEI")
    play FEI "NAE02A_FEI0004"
    $ current_voice = "voice/NAE02A_FEI0004.ogg"
    "菲利斯" "「回家绕路了喵？难道和男孩子约会了？」"
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0128"
    $ current_voice = "voice/NAE02A_NAE0128.ogg"
    "绹" "「呃，不是的了」"
    "不过，和桶子叔叔在街上一起走的时候，也许被周围的人当成了约会吧。"
    "是这样还真是不想被人误会啊。"
    $ stopvoc("FEI")
    play FEI "NAE02A_FEI0005"
    $ current_voice = "voice/NAE02A_FEI0005.ogg"
    "菲利斯" "「那、是和朋友去喝茶什么的了喵？」"
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0129"
    $ current_voice = "voice/NAE02A_NAE0129.ogg"
    "绹" "「也不是，诶——」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    "一时间，我假装换衣服，背对着留未穗姐姐。"
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0130"
    $ current_voice = "voice/NAE02A_NAE0130.ogg"
    "绹" "「放学后、做空置教室的扫除去了」"
    $ stopvoc("FEI")
    play FEI "NAE02A_FEI0006"
    $ current_voice = "voice/NAE02A_FEI0006.ogg"
    "菲利斯" "「呼嗯？」"
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0131"
    $ current_voice = "voice/NAE02A_NAE0131.ogg"
    "绹" "「…………」"
    "……我、撒谎了。"
    "为什么呢？"
    $ stopvoc("FEI")
    play FEI "NAE02A_FEI0007"
    $ current_voice = "voice/NAE02A_FEI0007.ogg"
    "菲利斯" "「是这样啊。作为绹去外面偷吃的纪念，我想去买蛋糕喵」"
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0132"
    $ current_voice = "voice/NAE02A_NAE0132.ogg"
    "绹" "「纪念？」"
    $ stopvoc("FEI")
    play FEI "NAE02A_FEI0008"
    $ current_voice = "voice/NAE02A_FEI0008.ogg"
    "菲利斯" "「说起来，应该挺开心吧？」"
    $ stopvoc("FEI")
    play FEI "NAE02A_FEI0009"
    $ current_voice = "voice/NAE02A_FEI0009.ogg"
    "菲利斯" "「想和绹、一起更多更多地玩耍喵」"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_HSC01"),"True","lh/FEI_HSC01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0133"
    $ current_voice = "voice/NAE02A_NAE0133.ogg"
    "绹" "「留未穗姐姐……」"
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0134"
    $ current_voice = "voice/NAE02A_NAE0134.ogg"
    "绹" "「我光是社团活动就够忙了啦」"
    $ stopvoc("FEI")
    play FEI "NAE02A_FEI0010"
    $ current_voice = "voice/NAE02A_FEI0010.ogg"
    "菲利斯" "「喵呼呼、是这样啊喵」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_HSA02"),"True","lh/FEI_HSA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FEI")
    play FEI "NAE02A_FEI0011"
    $ current_voice = "voice/NAE02A_FEI0011.ogg"
    "菲利斯" "「来、快点把手洗了喵。妈妈在等了喵」"
    $ stopvoc("NAE")
    play NAE "NAE02A_NAE0135"
    $ current_voice = "voice/NAE02A_NAE0135.ogg"
    "绹" "「嗯」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    "目送留未穗姐走出房间，我小小叹了口气。"
    "我对留未穗姐撒谎了。"
    "无论多小的谎话，都会被看破。"
    "明明是这样……。"
    "也不是桶子叔叔要我保守秘密的原因。"
    "本来留未穗姐就是“Ｌａｂｍｅｍ”的一员，和桶子叔叔和冈伦叔本应是伙伴。"
    "所以，本来就应该告诉她的。"
    "我，为什么撒谎了呢？"



    stop bgm 
    hide screen phoneSD1
    window hide
    scene expression Solid("000000")  with fade




    hide screen phonebtn
    scene expression Solid("000000")  with fade
    return













    return





    return





    return
