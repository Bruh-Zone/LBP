label SGFD2_DAR08A:
    window hide


    $ loadBG(0,"BG16N1")
    play se "SGSE007L" loop



    $ date="8/16"
    show screen phonebtn
    show screen phoneSD1

    "因为是暑假，加上还有夏Ｃｏｍｉ，中央大道在傍晚的时候依然人山人海。"
    "一边推开周围的人群，我低着头一边不断地前进着。"
    "想要找的东西是下水道。"
    "在我十九年的人生里，今天大概是见到下水道井盖最多的一天了吧。"
    "诶，就算只是这么一边走一边找下水道，在这样的人群里也是够累的了。"
    "但是，下水道的数量也太多了吧（笑）。"
    "Ｌａｂ的附近没什么人的地方都看过了以后，我就这样去了中央大道。"
    "现在由季碳在＠ｃｈ里面写的号码『Ｂ１４　７Ｈ　８Ｈ　Ｙ９１』也没有找到。"
    "冈伦和牧濑氏应该也分头在找，但因为没联系我看来是没有找到吧。"
    "虽说身为天才少女的牧濑氏非常期待里面隐藏的秘密。"
    "如果能快点找到的话，我就可以不用这么四处奔波了实在是万分感谢。"
    $ stopvoc("DAR")
    play DAR "DAR08A_DAR0000"
    $ current_voice = "voice/DAR08A_DAR0000.ogg"
    "至" "「哈……哈……」"
    "一直这样东走西走的原因，身上已经全身是汗了。"
    "果然已经气喘吁吁了，扶着走道边上的栏杆上，稍微休息一下。"
    "接着看见了一个地方。"
    "在车流涌动的中央大道车道上。"
    "那里不是也有一个下水道吗？"
    $ stopvoc("DAR")
    play DAR "DAR08A_DAR0001"
    $ current_voice = "voice/DAR08A_DAR0001.ogg"
    "至" "「喂喂……」"
    "如果是车道的话，现在这个时间点上去调查的话可是非常危险的。"
    "抓好时机飞奔到那里的话估计可以，但如果那么做的话被巡警看见会被盯上吧。"
    "抑或是等到车非常少的深夜。但是肯定不会给我时间等的。"
    $ stopvoc("DAR")
    play DAR "DAR08A_DAR0002"
    $ current_voice = "voice/DAR08A_DAR0002.ogg"
    "至" "「不行，冷静点。已经没有给我时间慌了……」"
    "在这儿不断地嘟囔，不管如何先试着冷静下。"
    "由季碳解开暗号并输入的时间是什么时候来着。"
    "好像……是晚上八点到九点左右来着。等下，应该是昨天这个时候。"
    "眼前道上行驶的车还有很多。"
    "如果是这种车流量的话，一个女孩子到车道上面把下水道打开是不可能的吧常考。"
    "所以妹子去的那个下水道是车道上面这个的可能性很低……可能。"
    "就算这样强行给自己解释，休息完之后还是在不断地寻找着。"
    window hide

    stop se


    $ loadBG(2,"BG_BLACK")



    hide screen phonebtn
    "然后——"
    window hide


    $ loadBG(0,"BG40N")

    play bgm "FD2BGM04"
    "找到了……！"
    "ＬａＯＸ的小道里面。"
    window hide


    $ loadBG(2,"BG_BLACK",hold=True)
    $ loadBG(0,"IBG037B",png=True)






    hide screen phonebtn
    "有个下水道盖子，肯定就是我想找的那个！"
    "１４　７Ｈ　８Ｈ　９１"
    "不管确认多少次。都没有错误。颜色也符合。"
    "好好调查了下，盖子上面还有刚刚动过的痕迹。。"
    "应该是被打开过了，也许？"
    "那个盖子，能很简单地被打开吗。"
    "假装什么都没发生一样看了下四周，这简直就是准备过的隐藏下水道口啊。在离得不远的地方就有一个垃圾放置地边上有一根撬棍。"
    "试了下，把棍子插进盖子的小洞里面，随便一用力。"
    window hide
    play se "SGSE308"
    hide background-png 
    with moveoutright




    stop se
    show screen phonebtn
    $ stopvoc("DAR")
    play DAR "DAR08A_DAR0003"
    $ current_voice = "voice/DAR08A_DAR0003.ogg"
    "至" "「……！」"
    $ stopvoc("DAR")
    play DAR "DAR08A_DAR0004"
    $ current_voice = "voice/DAR08A_DAR0004.ogg"
    "至" "「等！怎么就开了啊……」"
    window hide


    $ loadBG(2,"BG40N")



    "ＬａＯＸ店内的顾客，不知道因为什么事情看着我这边。"
    "接着——"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MOE')",DynamicDisplayable(mouthanime,"MOE_ASB01"),"True","lh/MOE_ASB01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MOE")
    play MOE "DAR08A_MOE0000"
    $ current_voice = "voice/DAR08A_MOE0000.ogg"
    "萌郁" "「桥田君……？　你在干什么呢？」"
    "时机非常的好，好像非常眼熟身材非常丰满的三次元妹子桐生氏刚好走过。"
    "虽然在意她最后到底有没有在夏Ｃｏｍｉ和真由氏见面，不过现在怎么都好了。"
    $ stopvoc("DAR")
    play DAR "DAR08A_DAR0005"
    $ current_voice = "voice/DAR08A_DAR0005.ogg"
    "至" "「桐生氏，来得正好啊！　快点联络警察吧！　下面好像有人被抓了！」"
    "告诉了桐生氏以后，我就决定毫无顾忌地下去了。"
    hide screen phoneSD1
    window hide
    stop bgm 


    $ loadBG(2,"BG_BLACK")



    hide screen phonebtn
    play se "SGSE309L" loop
    "下面就是下水道了。"
    "那种臭味直接冲进我的鼻子。"
    "里面一片漆黑什么也看不见。"
    "总之只好先沿着下水道前进吧。"
    "说真的由季碳到底是不是在前面被抓了我真的不清楚。"
    "如果谁也没有，完全是我的异想天开的话，之后估计警察会很生气吧。"
    "但是，那种程度的后果也无所谓了。"
    "如果由季碳真的没事的话。"
    "如果出了什么事的话，阿万音氏会非常伤心的。"
    "由季碳的男朋友也会非常伤心的。"
    "我的话……说实在的没有什么关系了。"
    "自己也，不知道为什么为了去救一个不认识的妹子而做到这种地步。"
    "如果，在广播馆袭击我的那群家伙也在该咋办啊……"
    "果然没有想太多就下来这一点还是太轻率了啊。"
    "但是都已经来这里了，已经没法回头了吧。"
    "继续前进之后，我察觉到前面有微弱的光线。"
    "好像那已经是下水道的尽头了。"
    "停下脚步，看了看前面的情况。"
    "没有看到有人的踪迹。"
    "下定决心，向着前面。"

    hide screen phoneSD1
    window hide

    stop se



    $ loadBG(0,"BG70A")



    $ bad_denpa=True
    play bgm "BGM25"
    show screen phonebtn
    show screen phoneSD1(dar=True)
    $ stopvoc("DAR")
    play DAR "DAR08A_DAR0006"
    $ current_voice = "voice/DAR08A_DAR0006.ogg"
    "至" "「等下，这里……」"
    "好像挺眼熟的，在哪儿见过一样。"
    "那个确实，好像是网络新闻上面出现过来着。"
    "啥来着，这里。"
    "过一段时间后眼睛适应了黑暗，总算是看见墙壁上面挂的板子，看到后就想起来了。"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_OLD_MANSEIBASHI_STA"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_OLD_MANSEIBASHI_STA"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_OLD_MANSEIBASHI_STA"])
    "{color=#f00}旧・万世桥车站{/color}。"
    "现在已经没有使用，成为废墟的废弃车站。"
    "由季碳是被困在这里……？"
    "光线是从更里面出来的。"
    "因为现在是晚上，所以并不是太阳光。如果是这样的话……是灯光。"
    "那里看来有谁在。"
    "应该试着大声喊一下吧。"
    "但是，如果是在广播馆的那群人呢？"
    "警察还没有来。"
    "桐生氏到底有没有好好地通知呢。"
    "最好的话，当然是打电话叫冈伦他们过来。"
    window hide
    hide screen phonebtn
    hide screen phonebtn2
    show screen phone(interact=False)
    "看了下自己的手机。……信号很不理想。"
    "好的，就发个短信吧。"
    window hide
    call send_mail (id=[102,103,104,105])






    call hide_phone

    "这样的话，冈伦他们应该会来了。"
    "总之先别出声，悄悄地往里面走。"
    "如果大事不妙的话，就赶紧往回跑就好了。"
    "慢慢地，慢慢地。"
    window hide



    $ loadBG(0,"BG69A",trans=fade)

    "这是个房间……。"
    "只有这里的氛围和这个车站不同。"
    "就连门看起来都是新的。"
    "就像是，车站废弃后才建起来的。"
    $ stopvoc("X06")
    play voc "DAR08A_X060000"
    $ current_voice = "voice/DAR08A_X060000.ogg"
    "？？？" "「唔……唔唔……」"
    $ stopvoc("DAR")
    play DAR "DAR08A_DAR0007"
    $ current_voice = "voice/DAR08A_DAR0007.ogg"
    "至" "「……！」"
    "有声音从里面穿了出来。"
    "刚刚那个不管怎么听都是女孩子的哭声真是非常感谢上帝！"
    "可能是由季碳吧？"
    "如果是这样的话，就平安无事了。"
    "周围也没有其他人。"
    "应该……开口吗？"
    "总之先敲敲门吧。"
    $ stopvoc("DAR")
    play DAR "DAR08A_DAR0008"
    $ current_voice = "voice/DAR08A_DAR0008.ogg"
    "至" "「…………」"
    window hide
    play se "SGSE310"

    $ stopvoc("X06")
    play voc "DAR08A_X060001"
    $ current_voice = "voice/DAR08A_X060001.ogg"
    "？？？" "「……！」"
    $ stopvoc("X06")
    play voc "DAR08A_X060002"
    $ current_voice = "voice/DAR08A_X060002.ogg"
    "？？？" "「是谁？」"
    "果然里面有女孩子。"
    "没有别人的声音。只有她一个人。"
    "不对，但是也有可能里面藏了别人。"
    $ stopvoc("X06")
    play voc "DAR08A_X060003"
    $ current_voice = "voice/DAR08A_X060003.ogg"
    "？？？" "「到底是谁？」"
    "果然还是应该等警察过来啊。"
    "……但是，虽说桐生氏确实是Ｌａｂｍｅｍ，但是没有怎么说过话，然后刚才我的举动也非常的奇怪。"
    "会不会听了那样的我说的话之后通知警察也是未知数。"
    "那样的话估计我也就不会一个人到这里了吧……！"
    "好的，还是先返回吧。等和警察一起再来吧。"
    "至少已经确定由季碳没有大碍。"
    $ stopvoc("X06")
    play voc "DAR08A_X060004"
    $ current_voice = "voice/DAR08A_X060004.ogg"
    "？？？" "「请……救救我。把我从这里救出去……拜托了……」"
    $ stopvoc("DAR")
    play DAR "DAR08A_DAR0009"
    $ current_voice = "voice/DAR08A_DAR0009.ogg"
    "至" "「…………」"
    "把哭泣的女孩子放着不管不太好吧常考。"
    "从工口游戏里面学到了这一点。"
    $ stopvoc("DAR")
    play DAR "DAR08A_DAR0010"
    $ current_voice = "voice/DAR08A_DAR0010.ogg"
    "至" "「那个，你，是一个人？」"
    $ stopvoc("X06")
    play voc "DAR08A_X060005"
    $ current_voice = "voice/DAR08A_X060005.ogg"
    "？？？" "「……是的」"
    "ｋｔｋｒ！"
    "这样就不用提心吊胆的了。"
    $ stopvoc("DAR")
    play DAR "DAR08A_DAR0011"
    $ current_voice = "voice/DAR08A_DAR0011.ogg"
    "至" "「这个门，打不开吗？」"
    $ stopvoc("X06")
    play voc "DAR08A_X060006"
    $ current_voice = "voice/DAR08A_X060006.ogg"
    "？？？" "「是的……」"
    "看了下门。"
    "有三个钥匙孔。"
    "就算是拿着撬棍，我一个人也很难撬开这个。"
    "总之不要做无谓的挣扎了，老老实实等待救援吧。"
    $ stopvoc("DAR")
    play DAR "DAR08A_DAR0012"
    $ current_voice = "voice/DAR08A_DAR0012.ogg"
    "至" "「你现在，是不是穿着Ｃｈｏｐｓｔｉｃｋ　Ｇｉｒｌ的Ｃｏｓ？」"
    $ stopvoc("X06")
    play voc "DAR08A_X060007"
    $ current_voice = "voice/DAR08A_X060007.ogg"
    "？？？" "「诶？」"
    $ stopvoc("DAR")
    play DAR "DAR08A_DAR0013"
    $ current_voice = "voice/DAR08A_DAR0013.ogg"
    "至" "「昨天，在＠ＣＨ上面用了那个固定昵称开帖了是不是？」"
    $ stopvoc("X06")
    play voc "DAR08A_X060008"
    $ current_voice = "voice/DAR08A_X060008.ogg"
    "？？？" "「啊，是，是的！　确实开了帖！」"
    $ stopvoc("DAR")
    play DAR "DAR08A_DAR0014"
    $ current_voice = "voice/DAR08A_DAR0014.ogg"
    "至" "「嘘！　别说得那么大声」"
    $ stopvoc("X06")
    play voc "DAR08A_X060009"
    $ current_voice = "voice/DAR08A_X060009.ogg"
    "？？？" "「抱，抱歉……。现在没穿Ｃｏｓ服」"
    "真是遗憾啊。"
    $ stopvoc("X06")
    play voc "DAR08A_X060010"
    $ current_voice = "voice/DAR08A_X060010.ogg"
    "？？？" "「那么，你是，看见我开的帖子，过来救我的咯！」"
    "嘛，好像也可以这么说，但是好像也不能这么说。"
    $ stopvoc("DAR")
    play DAR "DAR08A_DAR0015"
    $ current_voice = "voice/DAR08A_DAR0015.ogg"
    "至" "「你的名字，叫阿万音由季。ＯＫ？」"
    $ stopvoc("X06")
    play voc "DAR08A_X060011"
    $ current_voice = "voice/DAR08A_X060011.ogg"
    "？？？" "「…………」"
    $ stopvoc("X06")
    play voc "DAR08A_X060012"
    $ current_voice = "voice/DAR08A_X060012.ogg"
    "？？？" "「为什么，知道？　我的，名字……」"
    $ stopvoc("DAR")
    play DAR "DAR08A_DAR0016"
    $ current_voice = "voice/DAR08A_DAR0016.ogg"
    "至" "「…………」"
    $ stopvoc("DAR")
    play DAR "DAR08A_DAR0017"
    $ current_voice = "voice/DAR08A_DAR0017.ogg"
    "至" "「从一位叫铃羽的人那里，打听到的」"
    $ stopvoc("X06")
    play voc "DAR08A_X060013"
    $ current_voice = "voice/DAR08A_X060013.ogg"
    "由季" "「铃羽……？」"
    $ stopvoc("DAR")
    play DAR "DAR08A_DAR0018"
    $ current_voice = "voice/DAR08A_DAR0018.ogg"
    "至" "「不知道吗？」"
    $ stopvoc("X06")
    play voc "DAR08A_X060014"
    $ current_voice = "voice/DAR08A_X060014.ogg"
    "由季" "「不知道……」"
    "……不知道啊。"
    "这样的话，阿万音氏说的话都是真的。"
    "可能这个阿万音由季女士，不是那位阿万音的姐姐或者妹妹。压根就不是这样吗。"
    $ stopvoc("X06")
    play voc "DAR08A_X060015"
    $ current_voice = "voice/DAR08A_X060015.ogg"
    "由季" "「那位叫铃羽的人，到底……」"
    "也就是说，这种情况下我随便蒙混一下就完了。"
    "那个，我想想。"
    $ stopvoc("DAR")
    play DAR "DAR08A_DAR0019"
    $ current_voice = "voice/DAR08A_DAR0019.ogg"
    "至" "「我，我是那个叫做Ｄａｓｈ的人，回复你帖子的人」"
    $ stopvoc("DAR")
    play DAR "DAR08A_DAR0020"
    $ current_voice = "voice/DAR08A_DAR0020.ogg"
    "至" "「Ｄａｒｕ・Ｔｈｅ・ＳｕｐｅｒＨａｃｋｅｒ，简称ＤａＳＨ。嘿嘿」"
    $ stopvoc("X06")
    play voc "DAR08A_X060016"
    $ current_voice = "voice/DAR08A_X060016.ogg"
    "由季" "「哈，哈啊……」"
    $ stopvoc("DAR")
    play DAR "DAR08A_DAR0021"
    $ current_voice = "voice/DAR08A_DAR0021.ogg"
    "至" "「因为是超级黑客，所以想调查到你的名字还是非常简单的。」"
    $ stopvoc("DAR")
    play DAR "DAR08A_DAR0022"
    $ current_voice = "voice/DAR08A_DAR0022.ogg"
    "至" "「看到帖子之后，我想你已经卷入到什么不得了的事情上面了。就自己调查了下，终于找到了这里」"
    $ stopvoc("DAR")
    play DAR "DAR08A_DAR0023"
    $ current_voice = "voice/DAR08A_DAR0023.ogg"
    "至" "「之后，几个小时之前打电话问你胖次的颜色是什么的也是我」"
    $ stopvoc("X06")
    play voc "DAR08A_X060017"
    $ current_voice = "voice/DAR08A_X060017.ogg"
    "由季" "「原来如此……」"
    "啊……。糟糕了，说了不该说的。"
    "完了，从正义的英雄瞬间变成变态了。不过，不算是变态了是变态绅士才对。"
    "唉，随便～了。"
    $ stopvoc("X06")
    play voc "DAR08A_X060018"
    $ current_voice = "voice/DAR08A_X060018.ogg"
    "由季" "「……谢谢。噗嗤。真的，打不开吗……」 "
    "哦，哦？"
    "看来由季碳已经没有心情注意我的自爆发言了。"
    "门的另一侧，传来了啜泣声。"
    $ stopvoc("DAR")
    play DAR "DAR08A_DAR0024"
    $ current_voice = "voice/DAR08A_DAR0024.ogg"
    "至" "「……很快，警察就会来了，别担心了」"
    $ stopvoc("X06")
    play voc "DAR08A_X060019"
    $ current_voice = "voice/DAR08A_X060019.ogg"
    "由季" "「是的……谢谢……」"
    $ stopvoc("DAR")
    play DAR "DAR08A_DAR0025"
    $ current_voice = "voice/DAR08A_DAR0025.ogg"
    "至" "「总之，没事就好」"
    $ stopvoc("DAR")
    play DAR "DAR08A_DAR0026"
    $ current_voice = "voice/DAR08A_DAR0026.ogg"
    "至" "「顺便说下，那个帖子，最后面宣布这个帖子是钓鱼贴的那条，不是你写的吧？」"
    $ stopvoc("X06")
    play voc "DAR08A_X060020"
    $ current_voice = "voice/DAR08A_X060020.ogg"
    "由季" "「不是……」"
    $ stopvoc("X06")
    play voc "DAR08A_X060021"
    $ current_voice = "voice/DAR08A_X060021.ogg"
    "由季" "「我注意到了那个纸条上的暗号是下水道的编号」 "
    $ stopvoc("X06")
    play voc "DAR08A_X060022"
    $ current_voice = "voice/DAR08A_X060022.ogg"
    "由季" "「虽然找到了那个下水道。刚好在那里，有一群可疑的男子……」"
    $ stopvoc("X06")
    play voc "DAR08A_X060023"
    $ current_voice = "voice/DAR08A_X060023.ogg"
    "由季" "「被抓住后，被关到了这里……」"
    $ stopvoc("DAR")
    play DAR "DAR08A_DAR0027"
    $ current_voice = "voice/DAR08A_DAR0027.ogg"
    "至" "「有炸弹什么的说了没有？」"
    $ stopvoc("X06")
    play voc "DAR08A_X060024"
    $ current_voice = "voice/DAR08A_X060024.ogg"
    "由季" "「……啊！　对，对了，我，被带到这里的时候，看到了。炸弹！」"
    $ stopvoc("X06")
    play voc "DAR08A_X060025"
    $ current_voice = "voice/DAR08A_X060025.ogg"
    "由季" "「那个时候手机还没有被没收，结果慌慌张张写的时候被发现了……」"
    $ stopvoc("X06")
    play voc "DAR08A_X060026"
    $ current_voice = "voice/DAR08A_X060026.ogg"
    "由季" "「没收了身上所有的东西后，被关到了这里」"
    $ stopvoc("X06")
    play voc "DAR08A_X060027"
    $ current_voice = "voice/DAR08A_X060027.ogg"
    "由季" "「嗯，或许，那个并不是炸弹。而是定时炸弹？」"
    $ stopvoc("X06")
    play voc "DAR08A_X060028"
    $ current_voice = "voice/DAR08A_X060028.ogg"
    "由季" "「和电视剧里面的很像。放在硬铝盒子里面，里面有装置和计时器……」"
    $ stopvoc("X06")
    play voc "DAR08A_X060029"
    $ current_voice = "voice/DAR08A_X060029.ogg"
    "由季" "「把我关进这里面的那群男人，在弄这种东西……！」"
    $ stopvoc("DAR")
    play DAR "DAR08A_DAR0028"
    $ current_voice = "voice/DAR08A_DAR0028.ogg"
    "至" "「这个炸弹，知道具体的位置吗？」"
    $ stopvoc("X06")
    play voc "DAR08A_X060030"
    $ current_voice = "voice/DAR08A_X060030.ogg"
    "由季" "「不清楚……」"
    "由季碳被关在里面，好像已经快２４小时了。"
    "看了看周围，在能看清的范围之内好像并没有炸弹一样的东西。"
    "也就是说，被之前那群男人给拿走了咯？"
    "如果是这样的话由季碳被关在里面是被他们设了套咯？"
    "为什么不杀掉以绝后患呢，还费劲地把她关在这里，是模仿犯吧。"
    "随便了，多亏这样由季碳才平安无事。"
    $ stopvoc("DAR")
    play DAR "DAR08A_DAR0029"
    $ current_voice = "voice/DAR08A_DAR0029.ogg"
    "至" "「对了，你的电话，从一对可疑的男子那里拿回来了。」"
    $ stopvoc("X06")
    play voc "DAR08A_X060031"
    $ current_voice = "voice/DAR08A_X060031.ogg"
    "由季" "「诶？」"
    $ stopvoc("DAR")
    play DAR "DAR08A_DAR0030"
    $ current_voice = "voice/DAR08A_DAR0030.ogg"
    "至" "「联络下亲属，把平安无事的消息，说一下」"
    $ stopvoc("X06")
    play voc "DAR08A_X060032"
    $ current_voice = "voice/DAR08A_X060032.ogg"
    "由季" "「诶，也是呢……」"
    "门上面有个很小的观察窗口。"
    "虽然手没法放进去，但是手机的话还是应该没有问题的。"
    "透过观察口，和门另一边的由季对上了眼"
    "从眼睛上就能够知道。"
    "由季是个大美人。"
    "唉，现在都不是考虑这个的时候。"
    "把手机塞进去后。"
    "巨大的呜啪挂坠卡在了那里。"
    "呜啪妨碍了手机过去。"
    $ stopvoc("X06")
    play voc "DAR08A_X060033"
    $ current_voice = "voice/DAR08A_X060033.ogg"
    "由季" "「把呜啪取下来就好了」"
    "照着说的这样做，强行取下了挂坠。"
    "放进自己口袋里面后，再一次把手机放进观察口。"
    "这次终于如愿地进去了。"
    "在递手机的时候，碰了下由季的手。"
    $ stopvoc("X06")
    play voc "DAR08A_X060034"
    $ current_voice = "voice/DAR08A_X060034.ogg"
    "由季" "「啊……」"
    $ stopvoc("DAR")
    play DAR "DAR08A_DAR0031"
    $ current_voice = "voice/DAR08A_DAR0031.ogg"
    "至" "「诶？」"
    $ stopvoc("X06")
    play voc "DAR08A_X060035"
    $ current_voice = "voice/DAR08A_X060035.ogg"
    "由季" "「那个创可贴……」"
    "碰到的那根手指，贴着呜帕的创口贴。"
    $ stopvoc("X06")
    play voc "DAR08A_X060036"
    $ current_voice = "voice/DAR08A_X060036.ogg"
    "由季" "「昨天，在夏Ｃｏｍｉ上遇到过呢」"
    "由季碳记起来了。"
    $ stopvoc("DAR")
    play DAR "DAR08A_DAR0032"
    $ current_voice = "voice/DAR08A_DAR0032.ogg"
    "至" "「嗯，偶，偶然而已」"
    $ stopvoc("X06")
    play voc "DAR08A_X060037"
    $ current_voice = "voice/DAR08A_X060037.ogg"
    "由季" "「能够再会，真是太高兴了」"
    $ stopvoc("DAR")
    play DAR "DAR08A_DAR0033"
    $ current_voice = "voice/DAR08A_DAR0033.ogg"
    "至" "「没什么了……」"

    "总之把手机交到由季碳的手上了。"
    "被扯下来的呜啪，之后再还回去吧。"
    "之后，就只要安心等警察来了。"
    window hide
    stop bgm 
    play se "SGSE311L" loop


    $ stopvoc("DAR")
    play DAR "DAR08A_DAR0034"
    $ current_voice = "voice/DAR08A_DAR0034.ogg"
    "至" "「……！」"
    $ stopvoc("X06")
    play voc "DAR08A_X060038"
    $ current_voice = "voice/DAR08A_X060038.ogg"
    "由季" "「……！」"
    "脚步声！？"
    hide screen phoneSD1
    window hide
    $ loadBG(0,"EV_DAR004A")












    stop se
    hide screen phonebtn
    "慌慌张张地看向下水道方向，有人影。"
    show expression "bg/EV_DAR004A~ipad.jpg" as background :
        yalign 1.0
        linear 1.0yalign 0.3
    $ stopvoc("DAR")
    play DAR "DAR08A_DAR0035"
    $ current_voice = "voice/DAR08A_DAR0035.ogg"
    "至" "「诶……！？」"
    window hide


    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MOE')",DynamicDisplayable(mouthanime,"MOE_BSB05"),"True","lh/MOE_BSB05a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    hide background 
    $ loadBG(0,"BG69A",trans=fade,hide=False)











    $ stopvoc("DAR")
    play DAR "DAR08A_DAR0036"
    $ current_voice = "voice/DAR08A_DAR0036.ogg"
    "至" "「桐生……氏……？」"
    $ stopvoc("DAR")
    play DAR "DAR08A_DAR0037"
    $ current_voice = "voice/DAR08A_DAR0037.ogg"
    "至" "「终于赶过来了？　不对，那个，什么时候换了衣服？」"
    "比起这个，还有更加奇怪的事情。"
    "她的手上——"
    hide screen phoneSD1
    hide lh5 
    window hide
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_DAR004A"]]["Check"]=True
    show expression "bg/EV_DAR004A~ipad.jpg" as background :
        yalign 0.0
        linear 1.0yalign 0.3







    play se "SGSE060"






    hide screen phonebtn

    play bgm "FD2BGM05"






    $ stopvoc("DAR")
    play DAR "DAR08A_DAR0038"
    $ current_voice = "voice/DAR08A_DAR0038.ogg"
    "至" "「为什么，拿着枪？」"
    "而且，枪口直接对准了我。"
    "这个是模型吗？"
    $ stopvoc("MOE")
    play MOE "DAR08A_MOE0001"
    $ current_voice = "voice/DAR08A_MOE0001.ogg"
    "萌郁" "「桥田君，你，是从哪里知道Ｒｏｕｎｄｅｒ的恐怖活动计划的？」"
    $ stopvoc("DAR")
    play DAR "DAR08A_DAR0039"
    $ current_voice = "voice/DAR08A_DAR0039.ogg"
    "至" "「啥，啥子……？」"
    "感觉并不太懂桐生氏在说什么。"
    $ stopvoc("MOE")
    play MOE "DAR08A_MOE0002"
    $ current_voice = "voice/DAR08A_MOE0002.ogg"
    "萌郁" "「你也和那个叫阿万音由季的人一样，来找这个地下指挥所的么？　说起来，阿万音铃羽？　两人是姐妹吗？」"
    $ stopvoc("MOE")
    play MOE "DAR08A_MOE0003"
    $ current_voice = "voice/DAR08A_MOE0003.ogg"
    "萌郁" "「从同伴听说了。也就是说几个小时前，广播馆是不是发生了什么。」 "
    $ stopvoc("DAR")
    play DAR "DAR08A_DAR0040"
    $ current_voice = "voice/DAR08A_DAR0040.ogg"
    "至" "「……！」"
    $ stopvoc("DAR")
    play DAR "DAR08A_DAR0041"
    $ current_voice = "voice/DAR08A_DAR0041.ogg"
    "至" "「诶，桐生氏，你也是那群人的同伙吗？」"
    "完全没有搞清楚状况。"
    $ stopvoc("MOE")
    play MOE "DAR08A_MOE0004"
    $ current_voice = "voice/DAR08A_MOE0004.ogg"
    "萌郁" "「原来应该是我收到的小纸条，被阿万音由季无意中收到了，或者说是故意那么做的。」"
    $ stopvoc("MOE")
    play MOE "DAR08A_MOE0005"
    $ current_voice = "voice/DAR08A_MOE0005.ogg"
    "萌郁" "「装成我的样子？　还是刚好只是和我穿的差不多？」"
    $ stopvoc("MOE")
    play MOE "DAR08A_MOE0006"
    $ current_voice = "voice/DAR08A_MOE0006.ogg"
    "萌郁" "「但是阿万音由季出现在了这个据点的入口。那个时候我就判断为敌人了」"
    $ stopvoc("MOE")
    play MOE "DAR08A_MOE0007"
    $ current_voice = "voice/DAR08A_MOE0007.ogg"
    "萌郁" "「桥田君是朋友？　还是黑幕？」"
    $ stopvoc("MOE")
    play MOE "DAR08A_MOE0008"
    $ current_voice = "voice/DAR08A_MOE0008.ogg"
    "萌郁" "「不管如何只要妨碍恐怖主义计划的话，就给我消失吧」"
    $ stopvoc("DAR")
    play DAR "DAR08A_DAR0042"
    $ current_voice = "voice/DAR08A_DAR0042.ogg"
    "至" "「等，等下啊！　你到底在说什么我完全不知道！」"
    $ stopvoc("DAR")
    play DAR "DAR08A_DAR0043"
    $ current_voice = "voice/DAR08A_DAR0043.ogg"
    "至" "「桐生氏你到底是什么人！？」"
    $ stopvoc("MOE")
    play MOE "DAR08A_MOE0009"
    $ current_voice = "voice/DAR08A_MOE0009.ogg"
    "萌郁" "「……都到这种地步了还装傻。如果是这样的话」"


    play se "SGSE060"





    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_DAR004A"]]["Check"]=True
    show expression "bg/EV_DAR004A~ipad.jpg" as background :
        yalign 0.3
        linear 1.0yalign 0.0
    $ stopvoc("DAR")
    play DAR "DAR08A_DAR0044"
    $ current_voice = "voice/DAR08A_DAR0044.ogg"
    "至" "「吓……！」"


    "慌忙举起双手。"
    $ stopvoc("DAR")
    play DAR "DAR08A_DAR0045"
    $ current_voice = "voice/DAR08A_DAR0045.ogg"
    "至" "「别，求你别开枪我什么都做！」"
    $ stopvoc("MOE")
    play MOE "DAR08A_MOE0010"
    $ current_voice = "voice/DAR08A_MOE0010.ogg"
    "萌郁" "「你们的伙伴到底是谁，说」 "
    $ stopvoc("DAR")
    play DAR "DAR08A_DAR0046"
    $ current_voice = "voice/DAR08A_DAR0046.ogg"
    "至" "「请别杀我留我一条小命就算是大恩大德了！」 "
    $ stopvoc("MOE")
    play MOE "DAR08A_MOE0011"
    $ current_voice = "voice/DAR08A_MOE0011.ogg"
    "萌郁" "「…………」"
    $ stopvoc("DAR")
    play DAR "DAR08A_DAR0047"
    $ current_voice = "voice/DAR08A_DAR0047.ogg"
    "至" "「我还不想死啊！　工口游戏还有那么多神作没玩，动画还没有完结！」"
    $ stopvoc("DAR")
    play DAR "DAR08A_DAR0048"
    $ current_voice = "voice/DAR08A_DAR0048.ogg"
    "至" "「明天即将要出的『寄生住内』通关之前、绝对不能死啊！」"
    $ stopvoc("MOE")
    play MOE "DAR08A_MOE0012"
    $ current_voice = "voice/DAR08A_MOE0012.ogg"
    "萌郁" "「…………」"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_REAJU"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_REAJU"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_REAJU"])
    $ stopvoc("DAR")
    play DAR "DAR08A_DAR0049"
    $ current_voice = "voice/DAR08A_DAR0049.ogg"
    "至" "「谁来救救偶啊！　这里面的{color=#f00}现充{/color}女孩子的事情怎么样都好了！」"
    $ stopvoc("DAR")
    play DAR "DAR08A_DAR0050"
    $ current_voice = "voice/DAR08A_DAR0050.ogg"
    "至" "「就放我一条生路吧！」"
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_DAR004A"]]["Check"]=True
    show expression "bg/EV_DAR004A~ipad.jpg" as background :
        yalign 0.0
        linear 1.0yalign 0.3






    "一边说着一边冲向桐生氏那里。"


    $ stopvoc("MOE")
    play MOE "DAR08A_MOE0013"
    $ current_voice = "voice/DAR08A_MOE0013.ogg"
    "萌郁" "「──！」"
    "一把抓过手上拿的枪，一口气夺了过来"
    window hide

    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_DAR004B"]]["Check"]=True

    $ loadBG(0,"BG_WHITE")

    $ stopvoc("DAR")
    play DAR "DAR08A_DAR0051"
    $ current_voice = "voice/DAR08A_DAR0051.ogg"
    "至" "「──！」"
    $ stopvoc("X06")
    play voc "DAR08A_X060039"
    $ current_voice = "voice/DAR08A_X060039.ogg"
    "由季" "「哇！　ＤａＳＨ先生！」"
    window hide
    play se "SGSE014"
    with whiteflash




    $ loadBG(0,"BG_BLACK")

    "就算是有脂肪分担但是还是受到了很大的冲击，身体很难保持平衡。"
    $ stopvoc("DAR")
    play DAR "DAR08A_DAR0052"
    $ current_voice = "voice/DAR08A_DAR0052.ogg"
    "至" "「啊，啊啊啊……」"
    window hide

    $ loadBG(0,"BG69A")
    show expression Solid("000") as black :
        alpha 0.0
        linear 0.5alpha 0.5
        linear 0.5alpha 0.0
        repeat






    "开，开了一枪？"
    "我，被击中了？"
    "说起来，也没有问她到底是不是真枪……"
    $ stopvoc("MOE")
    play MOE "DAR08A_MOE0014"
    $ current_voice = "voice/DAR08A_MOE0014.ogg"
    "萌郁" "「……抱，抱歉。但是，这都是，你的错」"
    "两脚使不出力气。"
    "没法站立起来。"
    $ stopvoc("DAR")
    play DAR "DAR08A_DAR0053"
    $ current_voice = "voice/DAR08A_DAR0053.ogg"
    "至" "「唔唔……疼，好疼……谁……能救救我……」"
    "由于太过疼痛，意识……瞬间断线了——"
    window hide
    hide black 




    $ loadBG(0,"BG_BLACK")

    "眼前，只有一片黑暗。"

    hide screen phoneSD1
    window hide






    return








    return
