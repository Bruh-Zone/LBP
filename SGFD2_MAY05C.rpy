label SGFD2_MAY05C:
    hide screen phonebtn
    scene expression Solid("000000")  with fade

    window hide


    $ loadBG(0,"BG16N1")


    play bgm "FD2BGM09"

    $ date="7/7"
    $ day = "THU"
    show screen phonebtn
    show screen phoneSD1
    python:
        RcvMail(69)
        ReplyMail(69)
        SndMail(70)


    $ targetmailid = gc["ScriptMacros"]["RM_MAY_RECV_KAE03_01"]

    $ LR_RM_CHANCE=20
    call CHECK_RM_RECEIVE
    "──从那以后过去了一年。"
    call CHECK_RM_RECEIVE
    "升到了三年级，应试复习很辛苦，今年的暑假基本上就在假期补课班里度过了。"
    call CHECK_RM_RECEIVE
    "即使这样也绝对要想办法挤出时间，参加夏Ｃｏｍｉ，现在正在一点点地进行着准备。"
    call CHECK_RM_RECEIVE
    "夏Ｃｏｍｉ，就在考试的前几天，要参加的话着实很困难。"
    call CHECK_RM_RECEIVE
    "因此，要在夏Ｃｏｍｉ把没能玩到的玩回来。"
    call CHECK_RM_RECEIVE
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_DOMA_DOGI"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_DOMA_DOGI"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_DOMA_DOGI"])
    "吹雪酱、枫还有真由喜三个人，今天准备挑战{color=#f00}晓☆园{/color}的魔法少女ＣＯＳ。"
    call CHECK_RM_RECEIVE
    "今天难得地喘口气，来到了吹雪酱打工的女仆咖啡店来玩。"
    call CHECK_RM_RECEIVE
    "作为礼物，收到了小小的竹子枝。"
    call CHECK_RM_RECEIVE
    "不错啊，在女仆咖啡店打工，真由喜也想试一回啊。"
    call CHECK_RM_RECEIVE
    "考试结束以后一定要去当女仆。"
    call CHECK_RM_RECEIVE
    "就像这样真由喜度过着愉快的每一天。"
    call CHECK_RM_RECEIVE
    "真由喜也有着好多的朋友。"
    call CHECK_RM_RECEIVE
    "但是──"
    call CHECK_RM_RECEIVE
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0199"
    $ current_voice = "voice/MAY05A_MAY0199.ogg"
    "真由理" "「为什么呢，有时候觉得缺点什么，明明什么都不缺啊……」"
    call CHECK_RM_RECEIVE
    "想着是不是得了奢侈病。"
    call CHECK_RM_RECEIVE
    "但感觉并不是这样……"
    call CHECK_RM_RECEIVE
    "心里开的一个空洞，偶尔就会疼起来，让人犯难。"
    call CHECK_RM_RECEIVE
    "不光是如此，有时眼泪突然流了下来，有时还会去做不明所以的事……"
    call CHECK_RM_RECEIVE
    "自从去年参拜了奶奶的墓地以后，感觉真由喜就不是真由喜了，这种不可思议的感觉一直在困扰着真由喜。"
    call CHECK_RM_RECEIVE
    "虽然感觉有什么不对劲，但是却不知道那是什么，让人心里感觉到焦躁。"

    call CHECK_RM_RECEIVE
    "停下脚步，叹了口气。"

    $ gd["RCVmailData"][gc["ScriptMacros"]["RM_MAY_RECV_KAE03_01"]]["late"]=True
    $ lml.append(gc["ScriptMacros"]["RM_MAY_RECV_KAE03_01"])

    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0200"
    $ current_voice = "voice/MAY05A_MAY0200.ogg"
    "真由理" "「……不行不行，今天是难得的七夕，焦躁不安就没法玩了，必须得转换心情」"
    "每年到了七夕的时候，都会去花店买一枝小小的竹枝，把写着愿望的纸条挂起来，一边吃团子，一边眺望星空，这就是真由喜小小的乐趣。"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0201"
    $ current_voice = "voice/MAY05A_MAY0201.ogg"
    "真由理" "「啊，对了。机会难得，就许愿让心中的这种焦躁感消失吧～？」"
    window hide


    $ loadBG(2,"IBG044A")



    hide screen phonebtn
    "这或许是个好主意，高兴了起来，抬头仰望夜空。"
    "但是，夜空因为照明的缘故变得很亮，就像笼罩着一层雾一样，看不清楚。"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0202"
    $ current_voice = "voice/MAY05A_MAY0202.ogg"
    "真由理" "「果然，在这里就太亮了，看不清楚星星啊～」"
    window hide

    stop bgm 



    $ loadBG(0,"BG13N1")
    play se "SGSE007L" loop

    show screen phonebtn
    show screen phoneSD1
    "想要回到老家所在的蒲田，但是却在车站的检票口被拦住了。"
    "月票没有了……"
    "好奇怪啊，明明已经放在包里了。"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0203"
    $ current_voice = "voice/MAY05A_MAY0203.ogg"
    "真由理" "「啊……」"
    "说起来今天去女仆咖啡店玩的时候摔了一跤，包里面的东西全都掉了出来。"
    "或许是在那个时候漏了没有捡起来。"
    window hide
    hide screen phonebtn
    hide screen phonebtn2
    show screen phone(interact=False)
    "试着给吹雪酱发了个短信。"
    window hide
    call send_mail (id=[71,72,73])
    $ targetmailid = gc["ScriptMacros"]["FM_MAY05C_EDIT_FUB02_00"]

    $ targetmailid = gc["ScriptMacros"]["FM_MAY05C_SEND_FUB02"]






    call hide_phone

    "但是在发了之后意识到了。"
    "吹雪酱还在打工中，没有办法确认短信。"
    "没有办法，回到店里去吧。"
    window hide
    stop se



    $ loadBG(0,"BG30N")
    play se "SGSE042"


    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0204"
    $ current_voice = "voice/MAY05A_MAY0204.ogg"
    "真由理" "「嗯～？　走错路了吗？」"
    "并不是女仆咖啡店所在的那条宽马路，而是来到了后巷。"
    "嗯──，怎么办呢……"
    "一边看着周围，一边走──"
    window hide
    stop se



    $ loadBG(0,"BG79N9",at=[Transform(yalign=1.0)])





    play bgm "FD2BGM08"
    "突然，在古老的大楼前，停下了脚步。"
    window hide




    hide screen phonebtn
    "一楼是卖旧电视的商店，二楼的窗户上贴着「有空房」的告示。"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0205"
    $ current_voice = "voice/MAY05A_MAY0205.ogg"
    "真由理" "「这栋大楼……」"
    "怎么回事呢。"






    "抬头向上看之后，不知为何感觉到了悲伤。"


    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0206"
    $ current_voice = "voice/MAY05A_MAY0206.ogg"
    "真由理" "「怎么、楼顶上……有人在……？」"
    "太暗了看不太清，不过感觉那是个人影。"
    window hide


    $ loadBG(2,"BG79N9")







    show screen phonebtn
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0207"
    $ current_voice = "voice/MAY05A_MAY0207.ogg"
    "真由理" "「……是错觉吧……是这样吧。而且，屋顶上有什么人，也跟真由喜没有关系……」"
    "像是在劝说自己一样念叨着，但像往常一样的焦躁的心情，在心里膨胀了起来。"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0208"
    $ current_voice = "voice/MAY05A_MAY0208.ogg"
    "真由理" "「……为什么会这样在意呢？」"
    "非常在意那屋顶上若隐若现的人影。"
    "想要无视它，从大楼前走过，但是腿却挪不动地方。"
    "像是要被想要确认影子的真面目这种心情切裂了一样。"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0209"
    $ current_voice = "voice/MAY05A_MAY0209.ogg"
    "真由理" "「必须要去确认──」"
    "缓缓地登上大楼古旧的台阶。"
    window hide



    $ loadBG(0,"BG65N")

    "缓缓地爬上了连廊灯都没有的楼梯，来到了屋顶。"
    "大楼的屋顶黑乎乎的，一片寂静。"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0210"
    $ current_voice = "voice/MAY05A_MAY0210.ogg"
    "真由理" "「那个～，有人在吗～？」"
    "环视了一下四周，试着喊了一声。"
    "但是却没有人回答，也没有人的气息。"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0211"
    $ current_voice = "voice/MAY05A_MAY0211.ogg"
    "真由理" "「是真由喜的错觉吗～？」"
    "带着迷惑不解的心情，不经意地仰望夜空，留意到了漫天的星空。"
    window hide


    $ loadBG(2,"IBGX072")



    hide screen phonebtn
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0212"
    $ current_voice = "voice/MAY05A_MAY0212.ogg"
    "真由理" "「哇，在秋叶原也能很清楚地看到星星啊，我还不知道呢」"
    "车站周围因为高度的开发，就算到了夜里也有很多地方是亮的，而这栋楼的附近老旧的店铺多，到了这个时间，基本上都放下了卷帘门，或许是因为这个原因。"
    window hide


    $ loadBG(2,"BG65N")



    show screen phonebtn
    "古老的没有人的气息的大楼，一般的话会感觉到害怕的，但不知道为何，并没有感觉到害怕。"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0213"
    $ current_voice = "voice/MAY05A_MAY0213.ogg"
    "真由理" "「为什么呢？　感觉特别的熟悉」"
    "明明是第一次来到这里，却感觉并不是第一次。"
    "不，不仅如此，还有一种终于回到了这里来的感觉。"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0214"
    $ current_voice = "voice/MAY05A_MAY0214.ogg"
    "真由理" "「好想见到你……」"
    "回过神来，发现自己说了这么一句话。"
    "见谁？"
    "不知道。"
    "只是能感觉到是好久没有见的重要的人。"
    "就像七夕的传说一样──"
    window hide


    $ loadBG(2,"IBGX072")



    hide screen phonebtn
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0215"
    $ current_voice = "voice/MAY05A_MAY0215.ogg"
    "真由理" "「……织女和牛郎，有没有见面呢？」"
    "望着夜空，想象了起来。"
    "一年只能见一次的两个人。"
    "要是下雨的话，就又一年见不着面了，会非常的失望吧。"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0216"
    $ current_voice = "voice/MAY05A_MAY0216.ogg"
    "真由理" "「但是，这样的话，见面的时候就会倍感喜悦吧～」"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0217"
    $ current_voice = "voice/MAY05A_MAY0217.ogg"
    "真由理" "「……比起再也见不到……要好得多吧」"
    window hide


    $ loadBG(2,"BG65N")



    show screen phonebtn
    "注目于手里拿着的小竹枝。"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0218"
    $ current_voice = "voice/MAY05A_MAY0218.ogg"
    "真由理" "「试着许个愿吧？」"
    "从包里掏出了活页本，折成了细长的长方形，用手顺着折痕撕成了小条。"
    "虽然想写希望治好焦躁的感情，但感觉这么写好像没有意思啊～，于是重新考虑其他的愿望。"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0219"
    $ current_voice = "voice/MAY05A_MAY0219.ogg"
    "真由理" "「──希望想着想要见面的两个人能够见面」"
    "在小条上写了一个非常粗略的愿望。"
    "想着神是不是也会犯愁呢～，顺着小条上的洞，系在了竹枝上。"
    "握着捆上了小条的竹枝，将它指向了天空。"
    window hide


    $ loadBG(2,"IBGX072")



    hide screen phonebtn
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0220"
    $ current_voice = "voice/MAY05A_MAY0220.ogg"
    "真由理" "「希望愿望能够传达到天上──」"
    "又像往常那样无意识地寻找着星星。"
    "立刻就找到了那颗星星。"
    "一直在同一个地方发光的那颗北极星。"
    "是奶奶最开始教给真由喜的星星。"
    "一直盯着它，就变得想要哭泣了。"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0221"
    $ current_voice = "voice/MAY05A_MAY0221.ogg"
    "真由理" "「奶奶说过，想着想要见面的两个人，终有一天会再见面的是吧，这就是缘分……」"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0222"
    $ current_voice = "voice/MAY05A_MAY0222.ogg"
    "真由理" "「真由喜似乎有想要见的人，但不知道那个人是谁」"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0223"
    $ current_voice = "voice/MAY05A_MAY0223.ogg"
    "真由理" "「就算不知道想要见的人是谁……许愿想要见面的话……能不能见到呢……」"
    "踮起脚尖，带着愿望，把竹枝伸向了北极星。"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0224"
    $ current_voice = "voice/MAY05A_MAY0224.ogg"
    "真由理" "「希望二人能够见面……」"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0225"
    $ current_voice = "voice/MAY05A_MAY0225.ogg"
    "真由理" "「……愿望……传达到吧」"
    "用力地，用力地许愿。"
    "在那时──"
    stop bgm 
    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0108"
    $ current_voice = "voice/MAY05A_OKA0108.ogg"
    "？？？" "「星屑的握手么」"
    window hide


    $ loadBG(2,"BG65N")



    show screen phonebtn
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0226"
    $ current_voice = "voice/MAY05A_MAY0226.ogg"
    "真由理" "「！？」"


    play se "SGSE366L" loop

    "身后传来了声音。"
    "听到那低沉的声音的瞬间，全身颤抖了起来，屏住了呼吸。"
    "那简直是太过熟悉的声音了──"
    "明明想要回头看，却不敢回头看。"

    stop se
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0227"
    $ current_voice = "voice/MAY05A_MAY0227.ogg"
    "真由理" "「……谁？」"
    "定在那里，用颤抖的声音向身后询问。"
    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0109"
    $ current_voice = "voice/MAY05A_OKA0109.ogg"
    "？？？" "「椎名真由理，你应该认识我」"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0228"
    $ current_voice = "voice/MAY05A_MAY0228.ogg"
    "真由理" "「为什么……知道真由喜的名字……」"
    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0110"
    $ current_voice = "voice/MAY05A_OKA0110.ogg"
    "？？？" "「──我……认识你。一直在找你」"
    hide screen phoneSD1
    window hide
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_MAY005A"]]["Check"]=True


    $ loadBG(2,"EV_MAY005A")



    hide screen phonebtn
    play bgm "FD2BGM09"

    "被突然从背后抱住了。"
    "熟悉的味道充满了内心。"
    "不可能的情况。"
    "然而却不可思议的心里很沉着。"
    "两个人的眼里都留下了泪水。"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0229"
    $ current_voice = "voice/MAY05A_MAY0229.ogg"
    "真由理" "「一直在……找真由喜吗？」"
    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0111"
    $ current_voice = "voice/MAY05A_OKA0111.ogg"
    "？？？" "「嗯、是的」"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0230"
    $ current_voice = "voice/MAY05A_MAY0230.ogg"
    "真由理" "「……为什么？ 你是……谁？」"
    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0112"
    $ current_voice = "voice/MAY05A_OKA0112.ogg"
    "？？？" "「小孩子的时候，你住在池袋，你还记得那时，住在附近的一个臭小子吗？」"
    "听到这种话，想起了过去的事。"
    "确实，在奶奶去世之后，搬到了现在的蒲田。"
    "在那以前，真由喜一直住在池袋。"
    "在那里，经常跟一个年纪稍微比真由喜大的男孩子一起玩……好像是。"
    "对什么都具有旺盛的好奇心，一天到晚搞恶作剧的男孩子。"
    "总是被邻居的叔叔阿姨们骂。"
    "名字记得是──"
    window hide
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_MAY005B"]]["Check"]=True


    $ loadBG(2,"EV_MAY005B")



    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0231"
    $ current_voice = "voice/MAY05A_MAY0231.ogg"
    "真由理" "「……伦太君？」"
    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0113"
    $ current_voice = "voice/MAY05A_OKA0113.ogg"
    "伦太郎" "「那种叫法……还真是怀念啊……」"
    "凄凉的声音让心不由得一紧。"
    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0114"
    $ current_voice = "voice/MAY05A_OKA0114.ogg"
    "伦太郎" "「这条世界线上……对真由理来说我不过只是经常一起玩的少年Ａ罢了」"
    "被紧紧地抱住了，紧得几乎喘不上气。"
    "感觉到了伦太君也跟真由喜一样地在颤抖。"
    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0115"
    $ current_voice = "voice/MAY05A_OKA0115.ogg"
    "伦太郎" "「──身为人质居然敢随便地逃走，我凤凰院凶真绝对不允许。怎么可能让你一直逃下去！」"
    "人质，凤凰院凶真，像演戏一样的语调。"
    "非常的熟悉……简直太熟悉了……"
    "虽然熟悉……但却想不起来。"
    "这、让人伤悲。"
    "泪水止不住了。"
    $ stopvoc("OKA")
    play OKA "MAY05A_OKA0116"
    $ current_voice = "voice/MAY05A_OKA0116.ogg"
    "伦太郎" "「──真是的，让人操心的人质啊。你知道我找了你多久么……」"
    "被温柔地抚摸着头。"
    "像这样被摸着头，感觉非常的舒服。"
    $ stopvoc("MAY")
    play MAY "MAY05A_MAY0232"
    $ current_voice = "voice/MAY05A_MAY0232.ogg"
    "真由理" "「……谢谢你……找到了……真由喜」"

    hide screen phoneSD1
    window hide

    stop bgm





    hide screen phonebtn
    scene expression Solid("000000")  with fade
    show screen invisible
    $ renpy.movie_cutscene("video/imv06.avi")
    hide screen invisible
    "「悠远不变的北极星·完成」"

    return
