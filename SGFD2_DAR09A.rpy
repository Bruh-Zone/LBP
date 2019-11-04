label SGFD2_DAR09A:
    window hide


    $ loadBG(0,"BG_BLACK")



    $ date="8/16"
    hide screen phonebtn
    hide screen phoneSD1

    $ stopvoc("X06")
    play voc "DAR09A_X060000"
    $ current_voice = "voice/DAR09A_X060000.ogg"
    "？？？" "「……先生！」"
    $ stopvoc("X06")
    play voc "DAR09A_X060001"
    $ current_voice = "voice/DAR09A_X060001.ogg"
    "？？？" "「……ＳＨ先生！」"
    $ stopvoc("X06")
    play voc "DAR09A_X060002"
    $ current_voice = "voice/DAR09A_X060002.ogg"
    "？？？" "「ＤａＳＨ先生！　拜托了，快醒醒啊……！」"
    $ stopvoc("X06")
    play voc "DAR09A_X060003"
    $ current_voice = "voice/DAR09A_X060003.ogg"
    "？？？" "「ＤａＳＨ先生……！」"
    $ stopvoc("DAR")
    play DAR "DAR09A_DAR0000"
    $ current_voice = "voice/DAR09A_DAR0000.ogg"
    "至" "「唔，唔唔……」"
    $ stopvoc("X06")
    play voc "DAR09A_X060004"
    $ current_voice = "voice/DAR09A_X060004.ogg"
    "？？？" "「啊！　ＤａＳＨ先生！」"
    window hide

    $ loadBG(0,"BG69A")

    "睁开眼睛后，眼前只有已经快崩塌的混凝土天花板。"
    "意识虽然有点模糊，但是大腿根部的刺痛立刻让我清醒了过来。"
    $ stopvoc("DAR")
    play DAR "DAR09A_DAR0001"
    $ current_voice = "voice/DAR09A_DAR0001.ogg"
    "至" "「唔咕咕……！」"
    "就像烧红了的铁棍插进了腹部，然后在里面不断的搅拌……！"
    "忍不住摸了摸腰间看看。"
    window hide
    play se "SGSE312"

    $ stopvoc("DAR")
    play DAR "DAR09A_DAR0002"
    $ current_voice = "voice/DAR09A_DAR0002.ogg"
    "至" "「等……」"
    play bgm "BGM23"
    "右手被手铐铐住了。"
    "手铐的另一端是安在墙上的古老铁管。"
    $ stopvoc("DAR")
    play DAR "DAR09A_DAR0003"
    $ current_voice = "voice/DAR09A_DAR0003.ogg"
    "至" "「什，什么呀……」"
    "这让我顿时摸不着北。"
    "那个，我是来找由季碳的，说起旧万世桥车站的话，桐生氏来到这儿拿着枪对着我——"
    $ stopvoc("DAR")
    play DAR "DAR09A_DAR0004"
    $ current_voice = "voice/DAR09A_DAR0004.ogg"
    "至" "「我还活着……」"
    $ stopvoc("X06")
    play voc "DAR09A_X060005"
    $ current_voice = "voice/DAR09A_X060005.ogg"
    "由季" "「嗯，是这样的。ＤａＳＨ先生你，大概休克了１０分钟左右」"
    "用空着的左手试着去摸了一下发痛的地方。"
    $ stopvoc("DAR")
    play DAR "DAR09A_DAR0005"
    $ current_voice = "voice/DAR09A_DAR0005.ogg"
    "至" "「血也……没有出来……」"
    $ stopvoc("DAR")
    play DAR "DAR09A_DAR0006"
    $ current_voice = "voice/DAR09A_DAR0006.ogg"
    "至" "「我，刚刚明明被射到了的说……」"
    "到底是为什么呢？"
    $ stopvoc("X06")
    play voc "DAR09A_X060006"
    $ current_voice = "voice/DAR09A_X060006.ogg"
    "由季" "「是啊……到底是为什么呢？　我都以为ＤａＳＨ先生已经死了，但是我还是一直在试图叫醒你……」"
    $ stopvoc("X06")
    play voc "DAR09A_X060007"
    $ current_voice = "voice/DAR09A_X060007.ogg"
    "由季" "「总之，没事就好……」"
    "试着确认了下周围的情况。"
    "马上就感觉到“那个”的存在。"
    "被随便地放在不远的地方"
    window hide
    $ loadBG(1,"IBG038A",png=True)


    "硬铝金属箱。"
    "而且还是端端正正地打开放着。"
    "里面的装置和上面的倒计时能够很清楚地看见。"
    $ stopvoc("DAR")
    play DAR "DAR09A_DAR0007"
    $ current_voice = "voice/DAR09A_DAR0007.ogg"
    "至" "「时时时间……！」"
    "时间还剩１１分４３秒，４２秒，４１秒——"
    window hide
    hide background-png 
    with dissolve

    $ stopvoc("X06")
    play voc "DAR09A_X060008"
    $ current_voice = "voice/DAR09A_X060008.ogg"
    "由季" "「ＤａＳＨ先生，伤口真的没问题吗？」"
    $ stopvoc("DAR")
    play DAR "DAR09A_DAR0008"
    $ current_voice = "voice/DAR09A_DAR0008.ogg"
    "至" "「额，那个，怎么说呢……」"
    $ stopvoc("DAR")
    play DAR "DAR09A_DAR0009"
    $ current_voice = "voice/DAR09A_DAR0009.ogg"
    "至" "「由季碳，为什么感觉舒了一口气的样子！？」"
    $ stopvoc("X06")
    play voc "DAR09A_X060009"
    $ current_voice = "voice/DAR09A_X060009.ogg"
    "由季" "「抱，抱歉。因为看见ＤａＳＨ先生醒来了，终于安心了……」"
    $ stopvoc("DAR")
    play DAR "DAR09A_DAR0010"
    $ current_voice = "voice/DAR09A_DAR0010.ogg"
    "至" "「但是，还有１１分钟啊啊啊啊！」"
    $ stopvoc("X06")
    play voc "DAR09A_X060010"
    $ current_voice = "voice/DAR09A_X060010.ogg"
    "由季" "「诶？　１１分钟？　怎么，回事？"
    $ stopvoc("X06")
    play voc "DAR09A_X060011"
    $ current_voice = "voice/DAR09A_X060011.ogg"
    "由季" "「啊，是不是警察，要来了？」"
    $ stopvoc("DAR")
    play DAR "DAR09A_DAR0011"
    $ current_voice = "voice/DAR09A_DAR0011.ogg"
    "至" "「所以，那个……」"
    "突然注意到了。"
    "难道说由季碳不知道这里安装了炸弹，也有这种可能。"
    "所以桐生氏的事情，我想也不会在这设置好炸弹后再特意说明下。一直被关在那个房间里面，对炸弹设置的事情我估计她根本就不知道吧。"
    $ stopvoc("DAR")
    play DAR "DAR09A_DAR0012"
    $ current_voice = "voice/DAR09A_DAR0012.ogg"
    "至" "「…………」"
    $ stopvoc("X06")
    play voc "DAR09A_X060012"
    $ current_voice = "voice/DAR09A_X060012.ogg"
    "由季" "「ＤａＳＨ先生？」"
    $ stopvoc("DAR")
    play DAR "DAR09A_DAR0013"
    $ current_voice = "voice/DAR09A_DAR0013.ogg"
    "至" "「呀，没，什么……都没有」"
    "真是不好说出口啊……！"
    "按常识来说也不会说出口吧。"
    "我们现在的生命还有１１分钟——现在只有１０分２５秒了。为什么就是说不出口呢？"
    window hide
    play se "SGSE312"

    $ stopvoc("DAR")
    play DAR "DAR09A_DAR0014"
    $ current_voice = "voice/DAR09A_DAR0014.ogg"
    "至" "「可恶……！」"
    "万恶的桐生氏，还特意用手铐把我铐着。"
    "一心想要把我和由季碳给炸死，简直就是恐怖分子啊……！"
    "虽然在找拿到这里来的物理学圣剑（撬棍），但是附近却没有找到。"
    "逃不掉了……！"
    "警察呢……！？"
    "我已经进来很久了。为什么还没有来？"
    $ stopvoc("DAR")
    play DAR "DAR09A_DAR0015"
    $ current_voice = "voice/DAR09A_DAR0015.ogg"
    "至" "「……也就是说，压根不会来了！！！！」"
    window hide



    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MOE')",DynamicDisplayable(mouthanime,"MOE_ASB01"),"True","lh/MOE_ASB01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15

    $ loadBG(0,"BG40N",hide=False,trans=Fade(0.5,1,0.5,color="fff"))


    hide screen phonebtn
    "我拜托去报警的那个人，好巧不巧的就是误会了我的桐生氏！"
    "那个恐怖分子并没有通报这件事情。"
    window hide


    $ loadBG(0,"BG69A",trans=Fade(0.5,1,0.5,color="fff"))

    hide screen phonebtn
    $ stopvoc("DAR")
    play DAR "DAR09A_DAR0016"
    $ current_voice = "voice/DAR09A_DAR0016.ogg"
    "至" "「由季碳，你跟警察联络了吗？」"
    $ stopvoc("X06")
    play voc "DAR09A_X060013"
    $ current_voice = "voice/DAR09A_X060013.ogg"
    "由季" "「是的。但是……我的手机，一开始就联系上了，但是立马就没电了……」"
    "怎么这样。"
    "唯一的希望只有冈伦了。"
    window hide



    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA01"),"True","lh/OKA_ASA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15

    $ loadBG(0,"BG02N1",hide=False,trans=Fade(0.5,1,0.5,color="fff"))


    "如果是冈伦的话，如果是冈伦的话总会做些什么的……"
    "总之会……做些什么的……？"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASB01"),"True","lh/OKA_ASB01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    "那个厨二病患者？说实在的压根就不怎么靠谱。"
    "但是现在，只能够指望冈伦了。"
    "冈伦！快点来啊"
    window hide


    $ loadBG(0,"BG69A",trans=Fade(0.5,1,0.5,color="fff"))

    hide screen phonebtn
    "那个，在这儿干等着也是没有必要的"
    "自己打电话过去就好了！"
    "从口袋里拿出自己的手机。"
    "裤子的口袋里有烧焦的痕迹，看起来是子弹掠过产生的"
    $ stopvoc("DAR")
    play DAR "DAR09A_DAR0017"
    $ current_voice = "voice/DAR09A_DAR0017.ogg"
    "至" "「诶、诶诶诶……」"
    "难道是子弹，在击中我身体之前停止了？"
    $ stopvoc("DAR")
    play DAR "DAR09A_DAR0018"
    $ current_voice = "voice/DAR09A_DAR0018.ogg"
    "至" "「肯定是这样的，我的身体硬如钢铁。呃，有这种可能吗」"
    $ stopvoc("X06")
    play voc "DAR09A_X060014"
    $ current_voice = "voice/DAR09A_X060014.ogg"
    "由季" "「ＤａＳＨ先生？」"
    $ stopvoc("DAR")
    play DAR "DAR09A_DAR0019"
    $ current_voice = "voice/DAR09A_DAR0019.ogg"
    "至" "「不对，这边的话」"
    "在自己的口袋里摸着。"
    $ stopvoc("DAR")
    play DAR "DAR09A_DAR0020"
    $ current_voice = "voice/DAR09A_DAR0020.ogg"
    "至" "「哦！有了……」"
    window hide
    $ loadBG(0,"IBG039A",hold=True,png=True)
    with moveinbottom


    "从口袋里面掏出来的是由季手机上被扯下来的巨大的呜啪玩偶挂件。"
    "里面嵌这一刻子弹。"
    "是这个保护了我啊。"
    "真是可以称得上是奇迹了。好的就决定电影化。"
    "由于冲击力过大，呜啪已经瘪了。"
    "话说回来，这个被打瘪的呜啪……我好像在哪见过……"
    $ stopvoc("DAR")
    play DAR "DAR09A_DAR0021"
    $ current_voice = "voice/DAR09A_DAR0021.ogg"
    "至" "「啊……！」"
    window hide

    hide background-png 



    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_ASB04"),"True","lh/SUZ_ASB04a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    $ loadBG(0,"BG11E3",trans=Fade(0.5,1.0,0.5,color="fff"),hide=False)


    hide screen phonebtn
    $ stopvoc("SUZ")
    play SUZ "DAR09A_SUZ0000"
    $ current_voice = "voice/DAR09A_SUZ0000.ogg"
    "铃羽" "「这是父亲一直带着的纪念品。这个形状，是不是见过？」"
    window hide


    $ loadBG(0,"BG69A",trans=Fade(0.5,1.0,0.5,color="fff"))

    hide screen phonebtn
    "铃羽说的那东西，不就是阿万音氏那的这个吗。"
    "诶？　为什么？"
    $ stopvoc("DAR")
    play DAR "DAR09A_DAR0022"
    $ current_voice = "voice/DAR09A_DAR0022.ogg"
    "至" "「……也就是说，这到底是怎么一回事呢？」"
    "冷静地想下。"
    "经过仔细的思考。"
    "阿万音氏拿着的东西。可能是从未来拿过来的。父亲的纪念品。和由季碳的呜啪是一样的一个东西。"
    $ stopvoc("DAR")
    play DAR "DAR09A_DAR0023"
    $ current_voice = "voice/DAR09A_DAR0023.ogg"
    "至" "「嗯？」"
    "思考到这里，突然起了一身鸡皮疙瘩。"
    $ stopvoc("DAR")
    play DAR "DAR09A_DAR0024"
    $ current_voice = "voice/DAR09A_DAR0024.ogg"
    "至" "「真　是　这　样　的　吗」"
    "也就是说我莫非——"
    "我莫非是阿万音氏的父亲？"
    $ stopvoc("DAR")
    play DAR "DAR09A_DAR0025"
    $ current_voice = "voice/DAR09A_DAR0025.ogg"
    "至" "「……这是不可能的」"
    "把妄想终止。"
    "现在不是考虑这个的时候啊。"
    window hide
    show screen phonebtn
    show screen phoneSD1
    hide screen phonebtn
    hide screen phonebtn2
    show screen phone(interact=False)
    "另一方面，口袋里面的手机平安无事。"



    "虽然手机的信号很差，但也只能仰仗着手机联系警察了。"


    $ stopvoc("Y29")
    play voc "DAR09A_Y290000"
    $ current_voice = "voice/DAR09A_Y290000.ogg"
    "１１０接听员" "「这里是１１０报警电话处理中心。请问有什么事？　是事故吗？」"

    $ stopvoc("DAR")
    play DAR "DAR09A_DAR0026"
    $ current_voice = "voice/DAR09A_DAR0026.ogg"
    "至" "「快来救救我啊……！　炸……」"
    "虽然想说出这里装了炸弹这件事情，但是又强行把话给吞回肚子里了。"
    "这话由季碳肯定会听到的……"

    $ stopvoc("Y29")
    play voc "DAR09A_Y290001"
    $ current_voice = "voice/DAR09A_Y290001.ogg"
    "１１０接听员" "「喂喂喂？　到底怎么了？」"

    $ stopvoc("DAR")
    play DAR "DAR09A_DAR0027"
    $ current_voice = "voice/DAR09A_DAR0027.ogg"
    "至" "「旧，在旧万世桥站这里，我们被困在这里了。请快点过来救我们」"

    $ stopvoc("Y29")
    play voc "DAR09A_Y290002"
    $ current_voice = "voice/DAR09A_Y290002.ogg"
    "１１０接听员" "「啥？」"

    $ stopvoc("DAR")
    play DAR "DAR09A_DAR0028"
    $ current_voice = "voice/DAR09A_DAR0028.ogg"
    "至" "「就是我们被困了！　如果不快点过来的话就会糟糕！」"
    "心情过于焦躁，无法冷静地回答。"

    $ stopvoc("Y29")
    play voc "DAR09A_Y290003"
    $ current_voice = "voice/DAR09A_Y290003.ogg"
    "１１０接听员" "「具体的位置，知道吗？　您，现在在哪里？」"

    $ stopvoc("DAR")
    play DAR "DAR09A_DAR0029"
    $ current_voice = "voice/DAR09A_DAR0029.ogg"
    "至" "「秋叶原的地下，好像地下铁车站的废墟里面？　嗯，就是这！」。"

    $ stopvoc("Y29")
    play voc "DAR09A_Y290004"
    $ current_voice = "voice/DAR09A_Y290004.ogg"
    "１１０接听员" "「现在就被困在那里。只有您一位吗？」"

    $ stopvoc("DAR")
    play DAR "DAR09A_DAR0030"
    $ current_voice = "voice/DAR09A_DAR0030.ogg"
    "至" "「还有一位，是一位女士」"

    $ stopvoc("Y29")
    play voc "DAR09A_Y290005"
    $ current_voice = "voice/DAR09A_Y290005.ogg"
    "１１０接听员" "「有两位是吧。是从哪里进去的呢？」"

    "不小心瞥了一眼炸弹上面的定时器。"
    "上面剩下的时间只有８分钟了"
    $ stopvoc("DAR")
    play DAR "DAR09A_DAR0031"
    $ current_voice = "voice/DAR09A_DAR0031.ogg"
    "至" "「这都随便了……！　如果不快点的话──」"

    $ stopvoc("Y29")
    play voc "DAR09A_Y290006"
    $ current_voice = "voice/DAR09A_Y290006.ogg"
    "１１０接听员" "「但是如果不知道从哪里进去的话，我们也不能够帮您的」"

    $ stopvoc("DAR")
    play DAR "DAR09A_DAR0032"
    $ current_voice = "voice/DAR09A_DAR0032.ogg"
    "至" "「万世桥十字路口附近的下水道……，ＬａＯＸ边上的小道！」"

    $ stopvoc("Y29")
    play voc "DAR09A_Y290007"
    $ current_voice = "voice/DAR09A_Y290007.ogg"
    "１１０接听员" "「下水道啊……。那么，能否说明下里面的具体情况？」"

    $ stopvoc("DAR")
    play DAR "DAR09A_DAR0033"
    $ current_voice = "voice/DAR09A_DAR0033.ogg"
    "至" "「有锁着门的地下室。我被手铐拷住了没法取到……」"
    $ stopvoc("DAR")
    play DAR "DAR09A_DAR0034"
    $ current_voice = "voice/DAR09A_DAR0034.ogg"
    "至" "「是被恐怖分子，给铐上的。因为知道了不应该知道的东西……」"

    $ stopvoc("Y29")
    play voc "DAR09A_Y290008"
    $ current_voice = "voice/DAR09A_Y290008.ogg"
    "１１０接听员" "「原来如此，地下室……」"

    $ stopvoc("DAR")
    play DAR "DAR09A_DAR0035"
    $ current_voice = "voice/DAR09A_DAR0035.ogg"
    "至" "「绝对是真的！　请你相信我！　绝对不可能有开玩笑的功夫！　如果不快点的话就糟糕了！」"
    $ stopvoc("DAR")
    play DAR "DAR09A_DAR0036"
    $ current_voice = "voice/DAR09A_DAR0036.ogg"
    "至" "「那个，我所说的这些话确实感觉像厨二病发作或者是妄言，实际上如果是我在您的立场上面也只能微笑着说是」"
    $ stopvoc("DAR")
    play DAR "DAR09A_DAR0037"
    $ current_voice = "voice/DAR09A_DAR0037.ogg"
    "至" "「但这事绝对是真的！」"

    $ stopvoc("Y29")
    play voc "DAR09A_Y290009"
    $ current_voice = "voice/DAR09A_Y290009.ogg"
    "１１０接听员" "「知，知道了，请冷静点。现在就派警官到你那里去」"

    $ stopvoc("DAR")
    play DAR "DAR09A_DAR0038"
    $ current_voice = "voice/DAR09A_DAR0038.ogg"
    "至" "「快一点！　总之请你快一点！　这里有炸──」"
    $ stopvoc("DAR")
    play DAR "DAR09A_DAR0039"
    $ current_voice = "voice/DAR09A_DAR0039.ogg"
    "至" "「…………」"

    $ stopvoc("Y29")
    play voc "DAR09A_Y290010"
    $ current_voice = "voice/DAR09A_Y290010.ogg"
    "１１０接听员" "「请呆在那别动，安心等着」"



    $ stopvoc("DAR")
    play DAR "DAR09A_DAR0040"
    $ current_voice = "voice/DAR09A_DAR0040.ogg"
    "至" "「…………」"
    "不行。"
    "没法说出炸弹的事啊，真是一点都不能说。"
    "警察也完全没有紧迫感。"
    "我想８分钟内估计炸弹处理小队也不会来了。"
    $ stopvoc("X06")
    play voc "DAR09A_X060015"
    $ current_voice = "voice/DAR09A_X060015.ogg"
    "由季" "「……ＤａＳＨ先生？」"
    "但是正因为这样也不能轻易放弃！"
    $ stopvoc("DAR")
    play DAR "DAR09A_DAR0041"
    $ current_voice = "voice/DAR09A_DAR0041.ogg"
    "至" "「是冈伦的电话……」"
    "是冈伦打电话过来了。明明已经用邮件告诉过他具体位置了，到底在哪个地方瞎晃啊。"
    window hide



    "快……快点来啊冈伦！"


    $ stopvoc("OKA")
    play OKA "DAR09A_OKA0000"
    $ current_voice = "voice/DAR09A_OKA0000.ogg"
    "伦太郎" "「喂，桶子吗？」"

    $ stopvoc("DAR")
    play DAR "DAR09A_DAR0042"
    $ current_voice = "voice/DAR09A_DAR0042.ogg"
    "至" "「冈伦，现在在哪！？」"

    $ stopvoc("OKA")
    play OKA "DAR09A_OKA0001"
    $ current_voice = "voice/DAR09A_OKA0001.ogg"
    "伦太郎" "「在万世桥的十字路口。和助手在一起」"
    $ stopvoc("OKA")
    play OKA "DAR09A_OKA0002"
    $ current_voice = "voice/DAR09A_OKA0002.ogg"
    "伦太郎" "「虽然在万世桥车站那儿找入口，但是情况十分棘手啊」"

    "什么啊，还在那里啊……"
    $ stopvoc("DAR")
    play DAR "DAR09A_DAR0043"
    $ current_voice = "voice/DAR09A_DAR0043.ogg"
    "至" "「ＬａＯＸ边上小道的下水道啊。上面写了编号的」"

    $ stopvoc("OKA")
    play OKA "DAR09A_OKA0003"
    $ current_voice = "voice/DAR09A_OKA0003.ogg"
    "伦太郎" "「好的，我知道了。马上就来」"

    "看着不断闪烁的炸弹计时器"
    $ stopvoc("DAR")
    play DAR "DAR09A_DAR0044"
    $ current_voice = "voice/DAR09A_DAR0044.ogg"
    "至" "「６分钟……」"

    $ stopvoc("OKA")
    play OKA "DAR09A_OKA0004"
    $ current_voice = "voice/DAR09A_OKA0004.ogg"
    "伦太郎" "「嗯？　什么６分钟？」"

    $ stopvoc("DAR")
    play DAR "DAR09A_DAR0045"
    $ current_voice = "voice/DAR09A_DAR0045.ogg"
    "至" "「…………哈，哈哈」"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_MURIGEH"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_MURIGEH"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_MURIGEH"])
    "从常识来看就算现在冈伦到我这里来了，也绝对是{color=#f00}无理游戏{/color}让被手铐拷在墙上的我和被关在房间里的由季碳逃出去。"
    "那时候就会牵连到过来救我们的冈伦和牧濑氏两人……。"
    $ stopvoc("DAR")
    play DAR "DAR09A_DAR0046"
    $ current_voice = "voice/DAR09A_DAR0046.ogg"
    "至" "「…………」"
    $ stopvoc("DAR")
    play DAR "DAR09A_DAR0047"
    $ current_voice = "voice/DAR09A_DAR0047.ogg"
    "至" "「冈伦、我觉得……不过来、也没事……」"

    $ stopvoc("OKA")
    play OKA "DAR09A_OKA0005"
    $ current_voice = "voice/DAR09A_OKA0005.ogg"
    "伦太郎" "「什么？　到底怎么回事？」"

    $ stopvoc("DAR")
    play DAR "DAR09A_DAR0048"
    $ current_voice = "voice/DAR09A_DAR0048.ogg"
    "至" "「没啥，现在……刚好要进入和筷女氏的ＥＶＥＮＴ……」"

    $ stopvoc("OKA")
    play OKA "DAR09A_OKA0006"
    $ current_voice = "voice/DAR09A_OKA0006.ogg"
    "伦太郎" "「桶子？　你到底在说什么？」"

    $ stopvoc("DAR")
    play DAR "DAR09A_DAR0049"
    $ current_voice = "voice/DAR09A_DAR0049.ogg"
    "至" "「也就是说，我不希望你来妨碍我难得的现充时间」"
    $ stopvoc("DAR")
    play DAR "DAR09A_DAR0050"
    $ current_voice = "voice/DAR09A_DAR0050.ogg"
    "至" "「你就哪凉快哪待着去，你就和牧濑氏在那边逛逛吧」"

    $ stopvoc("OKA")
    play OKA "DAR09A_OKA0007"
    $ current_voice = "voice/DAR09A_OKA0007.ogg"
    "伦太郎" "「喂，这到底是怎么了──」"

    $ stopvoc("DAR")
    play DAR "DAR09A_DAR0051"
    $ current_voice = "voice/DAR09A_DAR0051.ogg"
    "至" "「那么，就这样了！」"

    "挂掉了电话。"
    "还得把另一个，会过来救助的可能性抹除。"
    "微微叹了口气。"
    window hide
    call hide_phone
    "就在此时计时器依旧在无情地走动着。"
    $ stopvoc("X06")
    play voc "DAR09A_X060016"
    $ current_voice = "voice/DAR09A_X060016.ogg"
    "由季" "「ＤａＳＨ先生……，是发生了什么吗？」"
    "从由季碳的语气里面可以听出来由季碳根本不信我说的话"
    "也是没办法的事情咯，明明打了电话求救却说不用来了。整个就是毫无逻辑可言。"
    "但是抱歉了。"
    "真的没法说明。"
    "而且，可能性还没有消失。"
    "还有，一个而已，还有一个机会。"
    window hide
    hide screen phonebtn
    hide screen phonebtn2
    show screen phone(interact=False)
    "准备拨打阿万音氏的电话。"
    "因为没有把阿万音氏的电话加到联系人里面，所以直接按着刚刚本人给我的小纸条上面的电话号码打了过去。"
    window hide





    $ stopvoc("SUZ")
    play SUZ "DAR09A_SUZ0001"
    $ current_voice = "voice/DAR09A_SUZ0001.ogg"
    "铃羽" "「是我」"

    $ stopvoc("DAR")
    play DAR "DAR09A_DAR0052"
    $ current_voice = "voice/DAR09A_DAR0052.ogg"
    "至" "「阿万……」"
    "我本来打算说阿万音氏的，但我突然打住了。"
    "在这里说阿万音的话，由季就会问“是和我同姓的人吗？”啥的，就会变得挺麻烦的。"
    $ stopvoc("DAR")
    play DAR "DAR09A_DAR0053"
    $ current_voice = "voice/DAR09A_DAR0053.ogg"
    "至" "「铃羽氏」"

    $ stopvoc("SUZ")
    play SUZ "DAR09A_SUZ0002"
    $ current_voice = "voice/DAR09A_SUZ0002.ogg"
    "铃羽" "「……发生了什么事？」"

    "我改变称呼这件事情，铃羽好像略有察觉。"

    $ stopvoc("SUZ")
    play SUZ "DAR09A_SUZ0003"
    $ current_voice = "voice/DAR09A_SUZ0003.ogg"
    "铃羽" "「不对，我知道了。你是不是和母亲在一起？」"

    $ stopvoc("DAR")
    play DAR "DAR09A_DAR0054"
    $ current_voice = "voice/DAR09A_DAR0054.ogg"
    "至" "「嗯……」"

    $ stopvoc("SUZ")
    play SUZ "DAR09A_SUZ0004"
    $ current_voice = "voice/DAR09A_SUZ0004.ogg"
    "铃羽" "「情况怎样？」"

    $ stopvoc("DAR")
    play DAR "DAR09A_DAR0055"
    $ current_voice = "voice/DAR09A_DAR0055.ogg"
    "至" "「………在旧万世桥车站身子动不了了」"
    $ stopvoc("DAR")
    play DAR "DAR09A_DAR0056"
    $ current_voice = "voice/DAR09A_DAR0056.ogg"
    "至" "「比起这个，４２寸显像管怎样了？」"

    $ stopvoc("SUZ")
    play SUZ "DAR09A_SUZ0005"
    $ current_voice = "voice/DAR09A_SUZ0005.ogg"
    "铃羽" "「不行啊。虽然返还给了厂家但是，果然在今天之内修好是不可能了」"

    $ stopvoc("DAR")
    play DAR "DAR09A_DAR0057"
    $ current_voice = "voice/DAR09A_DAR0057.ogg"
    "至" "「…………」"

    $ stopvoc("SUZ")
    play SUZ "DAR09A_SUZ0006"
    $ current_voice = "voice/DAR09A_SUZ0006.ogg"
    "铃羽" "「桥田至？」"

    $ stopvoc("DAR")
    play DAR "DAR09A_DAR0058"
    $ current_voice = "voice/DAR09A_DAR0058.ogg"
    "至" "「是，是的……」"
    "这样，就完全绝了后路了……。"
    "剩下的时间，从现在算的话，还有５分钟就完了。"

    $ stopvoc("SUZ")
    play SUZ "DAR09A_SUZ0007"
    $ current_voice = "voice/DAR09A_SUZ0007.ogg"
    "铃羽" "「…………」"

    $ stopvoc("DAR")
    play DAR "DAR09A_DAR0059"
    $ current_voice = "voice/DAR09A_DAR0059.ogg"
    "至" "「…………」"

    $ stopvoc("SUZ")
    play SUZ "DAR09A_SUZ0008"
    $ current_voice = "voice/DAR09A_SUZ0008.ogg"
    "铃羽" "「如果是没法说明的话，就是有难言之隐咯？」"
    $ stopvoc("SUZ")
    play SUZ "DAR09A_SUZ0009"
    $ current_voice = "voice/DAR09A_SUZ0009.ogg"
    "铃羽" "「是不是因为，母亲就在边上？」"

    $ stopvoc("DAR")
    play DAR "DAR09A_DAR0060"
    $ current_voice = "voice/DAR09A_DAR0060.ogg"
    "至" "「……是这么一回事」"

    $ stopvoc("SUZ")
    play SUZ "DAR09A_SUZ0010"
    $ current_voice = "voice/DAR09A_SUZ0010.ogg"
    "铃羽" "「那么我这边直接问吧」"
    $ stopvoc("SUZ")
    play SUZ "DAR09A_SUZ0011"
    $ current_voice = "voice/DAR09A_SUZ0011.ogg"
    "铃羽" "「是不是有炸弹？」"

    $ stopvoc("DAR")
    play DAR "DAR09A_DAR0061"
    $ current_voice = "voice/DAR09A_DAR0061.ogg"
    "至" "「有。就在我眼前」"

    $ stopvoc("SUZ")
    play SUZ "DAR09A_SUZ0012"
    $ current_voice = "voice/DAR09A_SUZ0012.ogg"
    "铃羽" "「还剩多久？」"

    $ stopvoc("DAR")
    play DAR "DAR09A_DAR0062"
    $ current_voice = "voice/DAR09A_DAR0062.ogg"
    "至" "「……不到５分钟」"

    $ stopvoc("SUZ")
    play SUZ "DAR09A_SUZ0013"
    $ current_voice = "voice/DAR09A_SUZ0013.ogg"
    "铃羽" "「可恶……！」"
    $ stopvoc("SUZ")
    play SUZ "DAR09A_SUZ0014"
    $ current_voice = "voice/DAR09A_SUZ0014.ogg"
    "铃羽" "「现在你可以拆除炸弹吗？」"

    $ stopvoc("DAR")
    play DAR "DAR09A_DAR0063"
    $ current_voice = "voice/DAR09A_DAR0063.ogg"
    "至" "「不行」"

    $ stopvoc("SUZ")
    play SUZ "DAR09A_SUZ0015"
    $ current_voice = "voice/DAR09A_SUZ0015.ogg"
    "铃羽" "「能不能逃出去？」"

    $ stopvoc("DAR")
    play DAR "DAR09A_DAR0064"
    $ current_voice = "voice/DAR09A_DAR0064.ogg"
    "至" "「现在我被拴在墙上。由季的话被关在屋子里」"

    $ stopvoc("SUZ")
    play SUZ "DAR09A_SUZ0016"
    $ current_voice = "voice/DAR09A_SUZ0016.ogg"
    "铃羽" "「…………」"

    $ stopvoc("DAR")
    play DAR "DAR09A_DAR0065"
    $ current_voice = "voice/DAR09A_DAR0065.ogg"
    "至" "「也就是说，非常抱歉铃羽」"
    "我没法，救出你的母亲……。"
    $ stopvoc("DAR")
    play DAR "DAR09A_DAR0066"
    $ current_voice = "voice/DAR09A_DAR0066.ogg"
    "至" "「顺带一提……」"
    $ stopvoc("DAR")
    play DAR "DAR09A_DAR0067"
    $ current_voice = "voice/DAR09A_DAR0067.ogg"
    "至" "「刚刚发现的，你的父亲……可能是我」"

    $ stopvoc("SUZ")
    play SUZ "DAR09A_SUZ0017"
    $ current_voice = "voice/DAR09A_SUZ0017.ogg"
    "铃羽" "「…………」"
    $ stopvoc("SUZ")
    play SUZ "DAR09A_SUZ0018"
    $ current_voice = "voice/DAR09A_SUZ0018.ogg"
    "铃羽" "「早知道了」"

    $ stopvoc("DAR")
    play DAR "DAR09A_DAR0068"
    $ current_voice = "voice/DAR09A_DAR0068.ogg"
    "至" "「啥……什么？」"

    $ stopvoc("SUZ")
    play SUZ "DAR09A_SUZ0019"
    $ current_voice = "voice/DAR09A_SUZ0019.ogg"
    "铃羽" "「没错。你就是我的父亲，桥田至」"

    $ stopvoc("DAR")
    play DAR "DAR09A_DAR0069"
    $ current_voice = "voice/DAR09A_DAR0069.ogg"
    "至" "「但是，你没有看过那个呜啪挂坠，的样子……」"

    $ stopvoc("SUZ")
    play SUZ "DAR09A_SUZ0020"
    $ current_voice = "voice/DAR09A_SUZ0020.ogg"
    "铃羽" "「话是这么说。但是在本人面前那个，不隐瞒事实的话就感觉有点」"

    $ stopvoc("DAR")
    play DAR "DAR09A_DAR0070"
    $ current_voice = "voice/DAR09A_DAR0070.ogg"
    "至" "「是吗，能够理解……」"
    "完了。"
    "现在感觉有点想笑。"
    "但同时眼泪从眼中涌出。"
    $ stopvoc("DAR")
    play DAR "DAR09A_DAR0071"
    $ current_voice = "voice/DAR09A_DAR0071.ogg"
    "至" "「我将来，娶个那么漂亮的老婆，还生了个这么漂亮的妹子啊」"
    $ stopvoc("DAR")
    play DAR "DAR09A_DAR0072"
    $ current_voice = "voice/DAR09A_DAR0072.ogg"
    "至" "「这真是现充爆炸的级别啊」"
    "虽然还有不到５分钟炸弹就要爆炸了。"
    "如果我和由季在这里死了的话，铃羽到底会怎么样呢？"
    "像某电影一样，一下子身体就消失了？"

    $ stopvoc("SUZ")
    play SUZ "DAR09A_SUZ0021"
    $ current_voice = "voice/DAR09A_SUZ0021.ogg"
    "铃羽" "「为什么说这些放弃的话！」"

    $ stopvoc("DAR")
    play DAR "DAR09A_DAR0073"
    $ current_voice = "voice/DAR09A_DAR0073.ogg"
    "至" "「……！」"

    $ stopvoc("SUZ")
    play SUZ "DAR09A_SUZ0022"
    $ current_voice = "voice/DAR09A_SUZ0022.ogg"
    "铃羽" "「现在我到底该怎么走！　快点告诉我地方！」"

    $ stopvoc("DAR")
    play DAR "DAR09A_DAR0074"
    $ current_voice = "voice/DAR09A_DAR0074.ogg"
    "至" "「来了也木有用了。５分钟够干个什么」"
    stop bgm 

    $ stopvoc("SUZ")
    play SUZ "DAR09A_SUZ0023"
    $ current_voice = "voice/DAR09A_SUZ0023.ogg"
    "铃羽" "「别小看我！」"

    $ stopvoc("DAR")
    play DAR "DAR09A_DAR0075"
    $ current_voice = "voice/DAR09A_DAR0075.ogg"
    "至" "「……！」"
    play bgm "FD2BGM11"


    $ stopvoc("SUZ")
    play SUZ "DAR09A_SUZ0024"
    $ current_voice = "voice/DAR09A_SUZ0024.ogg"
    "铃羽" "「别小看我阿万音铃羽」"
    $ stopvoc("SUZ")
    play SUZ "DAR09A_SUZ0025"
    $ current_voice = "voice/DAR09A_SUZ0025.ogg"
    "铃羽" "「不要看不起，桥田至和阿万音由季生的女儿」"
    $ stopvoc("SUZ")
    play SUZ "DAR09A_SUZ0026"
    $ current_voice = "voice/DAR09A_SUZ0026.ogg"
    "铃羽" "「而且！　在２０３６年我的父亲和母亲都还在世！」"
    $ stopvoc("SUZ")
    play SUZ "DAR09A_SUZ0027"
    $ current_voice = "voice/DAR09A_SUZ0027.ogg"
    "铃羽" "「所以，在２０１０年你们怎么可能会死！」"

    $ stopvoc("DAR")
    play DAR "DAR09A_DAR0076"
    $ current_voice = "voice/DAR09A_DAR0076.ogg"
    "至" "「那个……但是……」"
    "但是这个理由好怪啊。"
    "铃羽自己都这么说。"
    "如果出现了这事的话，根源就是我在夏Ｃｏｍｉ上见到了由季。"
    "也就是说是因为铃羽干涉了过去才见到的。"
    "和铃羽出生的那个世界有那么一点不同。"
    "所以说，铃羽所在的世界是在２０３６年出生的，在这个世界的我和由季是不一定能够保证能让我们俩活下来的。"

    $ stopvoc("SUZ")
    play SUZ "DAR09A_SUZ0028"
    $ current_voice = "voice/DAR09A_SUZ0028.ogg"
    "铃羽" "「别说这些有的没的！　地方在哪！？」"

    $ stopvoc("DAR")
    play DAR "DAR09A_DAR0077"
    $ current_voice = "voice/DAR09A_DAR0077.ogg"
    "至" "「万，万世桥，ＬａＯＸ边上小路的下水道……」"
    "啊，突然感到一股压迫不小心就说了出来……"

    $ stopvoc("SUZ")
    play SUZ "DAR09A_SUZ0029"
    $ current_voice = "voice/DAR09A_SUZ0029.ogg"
    "铃羽" "「Ｏｋａｙ　Ｄｏｋｅｙ！」"


    "……这样，就好了吧。"
    "铃羽好像是那种硬来的类型。"
    window hide
    call hide_phone
    $ loadBG(0,"IBG038A",png=True)


    "还有４分钟。就算来这里也没什么用了。"
    "好像也没有什么可以做的。"
    "如果还把铃羽牵扯进来的话……我，自己和未来的老婆还有未来的女儿全都没了。"
    "或者说，如果让铃羽活下来的话，也许能够让她使用时光机。"
    "也就说能够让她去往３人都还在的地方。"
    "我现在能够做的，硬要说的话，把炸弹当作假的。真是一点也笑不出来，虽然满怀希望地期待铃羽能来。"
    $ stopvoc("X06")
    play voc "DAR09A_X060017"
    $ current_voice = "voice/DAR09A_X060017.ogg"
    "由季" "「……铃羽小姐，是ＤａＳＨ先生的女朋友吗？」"
    stop bgm 
    window hide
    hide background-png 


    $ stopvoc("DAR")
    play DAR "DAR09A_DAR0078"
    $ current_voice = "voice/DAR09A_DAR0078.ogg"
    "至" "「噗」"
    "虽然没有喝什么东西，但还是做出了喷水的动作。"
    $ stopvoc("X06")
    play voc "DAR09A_X060018"
    $ current_voice = "voice/DAR09A_X060018.ogg"
    "由季" "「抱歉，刚刚的电话，稍微听了下……」"
    $ stopvoc("DAR")
    play DAR "DAR09A_DAR0079"
    $ current_voice = "voice/DAR09A_DAR0079.ogg"
    "至" "「也不是了，也不是女朋友什么的了……」"
    "是女儿，如果真说了的话我想我可以确定自己是变态了。我不是变态我是变态的绅士啊。"
    $ stopvoc("DAR")
    play DAR "DAR09A_DAR0080"
    $ current_voice = "voice/DAR09A_DAR0080.ogg"
    "至" "「是朋友」"
    $ stopvoc("X06")
    play voc "DAR09A_X060019"
    $ current_voice = "voice/DAR09A_X060019.ogg"
    "由季" "「是这样的啊」"
    $ stopvoc("DAR")
    play DAR "DAR09A_DAR0081"
    $ current_voice = "voice/DAR09A_DAR0081.ogg"
    "至" "「…………」"
    $ stopvoc("X06")
    play voc "DAR09A_X060020"
    $ current_voice = "voice/DAR09A_X060020.ogg"
    "由季" "「…………」"
    "由季碳好像非常地不安啊。也难怪，已经被关在房间里一整天了。"
    "剩下的时间大概还有４分钟。"
    play bgm "FD2BGM06"
    "至少在死去前，想让由季碳安心一点。"
    "虽然骗人是不好的，相比绝望，能够有更好点的心态。这肯定是我任性的猜想了。"
    "对了啊，正是因为这样特殊的时期就应该对自然的对话而感到伤心。"
    $ stopvoc("DAR")
    play DAR "DAR09A_DAR0082"
    $ current_voice = "voice/DAR09A_DAR0082.ogg"
    "至" "「由季碳的Ｃｈｏｐｓｔｉｃｋ　Ｇｉｒｌ的Ｃｏｓ，让我超级无比兴奋啊」"
    "……突然不知不觉地聊起这种绅士的话题。"
    "真是郁闷得想死啊。虽然很快就会挂了倒是真的。"
    $ stopvoc("X06")
    play voc "DAR09A_X060021"
    $ current_voice = "voice/DAR09A_X060021.ogg"
    "由季" "「那个ｃｏｓ，大多数人呢，因为是Ｃｈｏｐｓｔｉｃｋ　Ｇｉｒｌ所以不怎么关注……」"
    $ stopvoc("X06")
    play voc "DAR09A_X060022"
    $ current_voice = "voice/DAR09A_X060022.ogg"
    "由季" "「嗯，不如说能注意到这个的，可能只有ＤａＳＨ先生了」"
    $ stopvoc("DAR")
    play DAR "DAR09A_DAR0083"
    $ current_voice = "voice/DAR09A_DAR0083.ogg"
    "至" "「我，非常喜欢筷女哟」"
    $ stopvoc("X06")
    play voc "DAR09A_X060023"
    $ current_voice = "voice/DAR09A_X060023.ogg"
    "由季" "「我也是！　你也喜欢这种角色，我们两个，趣味相投呢」"
    $ stopvoc("DAR")
    play DAR "DAR09A_DAR0084"
    $ current_voice = "voice/DAR09A_DAR0084.ogg"
    "至" "「…………」"
    $ stopvoc("X06")
    play voc "DAR09A_X060024"
    $ current_voice = "voice/DAR09A_X060024.ogg"
    "由季" "「实际上，打倒Ｃｈｏｐｓｔｉｃｋ　Ｇｉｒｌ的Ｉｎｄｒａ　Ｐａｎｚｅｒ，也是非常喜欢的。啊哈哈」"
    $ stopvoc("DAR")
    play DAR "DAR09A_DAR0085"
    $ current_voice = "voice/DAR09A_DAR0085.ogg"
    "至" "「等，Ｉｎｄｒａ　Ｐａｎｚｅｒ，是不是那个光头大叔？」"
    $ stopvoc("X06")
    play voc "DAR09A_X060025"
    $ current_voice = "voice/DAR09A_X060025.ogg"
    "由季" "「是的，不愧是ＤａＳＨ先生。真是能够很快的想到」"
    $ stopvoc("X06")
    play voc "DAR09A_X060026"
    $ current_voice = "voice/DAR09A_X060026.ogg"
    "由季" "「是中东油老板的儿子，捋着胡子，光着头。是不是很小气？」"
    $ stopvoc("DAR")
    play DAR "DAR09A_DAR0086"
    $ current_voice = "voice/DAR09A_DAR0086.ogg"
    "至" "「噢，噢……」"
    "真是怪异的趣味啊……"
    $ stopvoc("X06")
    play voc "DAR09A_X060027"
    $ current_voice = "voice/DAR09A_X060027.ogg"
    "由季" "「话说回来ＤａＳＨ先生，打算买『寄生住内』吗？」"
    $ stopvoc("DAR")
    play DAR "DAR09A_DAR0087"
    $ current_voice = "voice/DAR09A_DAR0087.ogg"
    "至" "「啊，对了……好像是明天来着」"
    hide screen phoneSD1
    window hide


    $ loadBG(0,"IBG028A")

    hide screen phonebtn
    "已经完全忘掉了。"
    "这是本次夏Ｃｏｍｉ，我的超本命啊。"
    window hide


    $ loadBG(0,"BG69A")

    show screen phonebtn
    show screen phoneSD1
    $ stopvoc("DAR")
    play DAR "DAR09A_DAR0088"
    $ current_voice = "voice/DAR09A_DAR0088.ogg"
    "至" "「嗯，肯定已经决定要买了」。"
    "但是，反正也买不了了。"
    "对我来说明天已经不会到来了。"
    $ stopvoc("X06")
    play voc "DAR09A_X060028"
    $ current_voice = "voice/DAR09A_X060028.ogg"
    "由季" "「冰果子酱的衣服，非常可爱呢。我想在冬Ｃｏｍｉ上面出她的Ｃｏｓ」"
    $ stopvoc("X06")
    play voc "DAR09A_X060029"
    $ current_voice = "voice/DAR09A_X060029.ogg"
    "由季" "「如果可以的话能不能让我看看她的画像？」"
    $ stopvoc("X06")
    play voc "DAR09A_X060030"
    $ current_voice = "voice/DAR09A_X060030.ogg"
    "由季" "「那个作品的竞争太激烈了，我绝对能入手这种事，基本上不可能了……」"
    $ stopvoc("X06")
    play voc "DAR09A_X060031"
    $ current_voice = "voice/DAR09A_X060031.ogg"
    "由季" "「所以，非常希望能够借我呢。真是抱歉，在这种时候……」"
    $ stopvoc("DAR")
    play DAR "DAR09A_DAR0089"
    $ current_voice = "voice/DAR09A_DAR0089.ogg"
    "至" "「…………」"
    "这种做梦一样的请求，怎么可能拒绝啊。"
    "更不用说想和由季碳一起愉快地玩『寄生住内』了。"
    "但是……现在也是不可能的啊。"
    "就算这样约定了，也不可能实现啊。"
    window hide
    $ loadBG(0,"IBG038A",png=True)


    "我和你的生命还有２分钟就没了。"
    window hide
    hide background-png 

    $ stopvoc("DAR")
    play DAR "DAR09A_DAR0090"
    $ current_voice = "voice/DAR09A_DAR0090.ogg"
    "至" "「那个啊……」"
    $ stopvoc("X06")
    play voc "DAR09A_X060032"
    $ current_voice = "voice/DAR09A_X060032.ogg"
    "由季" "「什么？」"
    $ stopvoc("DAR")
    play DAR "DAR09A_DAR0091"
    $ current_voice = "voice/DAR09A_DAR0091.ogg"
    "至" "「如果由季碳，将来有自己的孩子的话，到底想生一个什么样的呢？」"
    "真　的　不　小　心　选　了"
    "一个非常恶心的问题。"
    "为什么我问这种事情啊。"
    "门另一侧的由季碳刚刚肯定惊呆了。"
    "反正只有两分钟就挂了，还不如以这种酷炫的桥田至的形象死去吧……"
    $ stopvoc("X06")
    play voc "DAR09A_X060033"
    $ current_voice = "voice/DAR09A_X060033.ogg"
    "由季" "「那个……」"
    $ stopvoc("X06")
    play voc "DAR09A_X060034"
    $ current_voice = "voice/DAR09A_X060034.ogg"
    "由季" "「健康自在的，这样的，应该是这样的感觉吧？　也没有，很认真的考虑过这种事情，所以也不怎么清楚」"
    $ stopvoc("DAR")
    play DAR "DAR09A_DAR0092"
    $ current_voice = "voice/DAR09A_DAR0092.ogg"
    "至" "「是嘛……可恶，我擦」"
    "诶！"
    "等ｗｗｗ好像ｗｗｗ有眼泪不断ｗｗｗ地涌出来啊ｗｗｗｗｗ"
    "到底怎么了ｗｗｗ"
    "哭成这样……好像除了ｗｗｗ看『库兰纳德』外没有过吧ｗｗｗ"
    $ stopvoc("DAR")
    play DAR "DAR09A_DAR0093"
    $ current_voice = "voice/DAR09A_DAR0093.ogg"
    "至" "「５５，５５５５……。对不起……由季碳……」"
    $ stopvoc("X06")
    play voc "DAR09A_X060035"
    $ current_voice = "voice/DAR09A_X060035.ogg"
    "由季" "「ＤａＳＨ先生……，果然，你那里发生了什么吧……？」"
    $ stopvoc("DAR")
    play DAR "DAR09A_DAR0094"
    $ current_voice = "voice/DAR09A_DAR0094.ogg"
    "至" "「（抽泣）……对不起……没能保护你……抱歉……」"
    $ stopvoc("X06")
    play voc "DAR09A_X060036"
    $ current_voice = "voice/DAR09A_X060036.ogg"
    "由季" "「……请别道歉了」"
    $ stopvoc("X06")
    play voc "DAR09A_X060037"
    $ current_voice = "voice/DAR09A_X060037.ogg"
    "由季" "「ＤａＳＨ先生，你一点也没有错。因为我，跑到这来救我」"
    $ stopvoc("X06")
    play voc "DAR09A_X060038"
    $ current_voice = "voice/DAR09A_X060038.ogg"
    "由季" "「理应道歉的，应该是我」"
    $ stopvoc("X06")
    play voc "DAR09A_X060039"
    $ current_voice = "voice/DAR09A_X060039.ogg"
    "由季" "「如果不是我，干了不该干的事情，还把你给卷了进来」"
    $ stopvoc("X06")
    play voc "DAR09A_X060040"
    $ current_voice = "voice/DAR09A_X060040.ogg"
    "由季" "「如果，能出去的话……我想肯定会好好地在你面前，道歉的……」"
    "“想说的”什么的，由季碳如是说了。"
    "虽然我什么都没有说明，而且连面都没见到，由季碳的直觉还是判断出来了。"
    "真是的，感觉自己就像一个负心汉一样。"
    "连一个弱小的女子都没法帮到，而且到最后还被女生给安慰。"
    $ stopvoc("DAR")
    play DAR "DAR09A_DAR0095"
    $ current_voice = "voice/DAR09A_DAR0095.ogg"
    "至" "「我啊，唔，呃，Ｃｈｏ，Ｃｈｏｐｓｔｉｃｋ　Ｇｉｒｌ，最喜欢了！」"
    "在这个时候——"
    stop bgm 
    play se "SGSE378"

    "下水道那边，好像听见了脚步声——"
    $ stopvoc("DAR")
    play DAR "DAR09A_DAR0096"
    $ current_voice = "voice/DAR09A_DAR0096.ogg"
    "至" "「难道说……」"
    $ stopvoc("SUZ")
    play SUZ "DAR09A_SUZ0030"
    $ current_voice = "voice/DAR09A_SUZ0030.ogg"
    "铃羽" "「桥田至！」"
    window hide
    stop se

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_ASB04"),"True","lh/SUZ_ASB04a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    play bgm "FD2BGM01"
    "从暗处出来的人和想的一样，是阿万音铃羽。"
    "额头上满是汗水，肩膀随着气息浮动，视线迅速扫动着，不断地观察着我和定时炸弹还有周围的情况。"
    "定时炸弹上面的计时器上面还有４１秒。"
    hide screen phonebtn
    $ stopvoc("DAR")
    play DAR "DAR09A_DAR0097"
    $ current_voice = "voice/DAR09A_DAR0097.ogg"
    "至" "「已经没用了，快走──」"
    show screen phonebtn
    "在我话还没说完。"
    hide screen phoneSD1
    window hide
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_DAR005A"]]["Check"]=True


    $ loadBG(2,"EV_DAR005A")



    hide screen phonebtn
    "铃羽毫不犹豫地拿起了炸弹。"
    $ stopvoc("DAR")
    play DAR "DAR09A_DAR0098"
    $ current_voice = "voice/DAR09A_DAR0098.ogg"
    "至" "「等！？」"
    "一般的话这样的抖动不是会导致爆炸的吗？"
    "但是好像什么也没发生"
    "只不过，计时器还在不断的跳动，能够看见还有２０秒。"
    "铃羽到底在干什么。"
    window hide
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_DAR005B"]]["Check"]=True


    $ loadBG(2,"EV_DAR005B")



    $ stopvoc("SUZ")
    play SUZ "DAR09A_SUZ0031"
    $ current_voice = "voice/DAR09A_SUZ0031.ogg"
    "铃羽" "「包在我身上吧，不是说过吗」"
    "我看着一直对我微笑的铃羽。"
    $ stopvoc("SUZ")
    play SUZ "DAR09A_SUZ0032"
    $ current_voice = "voice/DAR09A_SUZ0032.ogg"
    "铃羽" "「母亲的事，就拜托你了」"
    window hide


    $ loadBG(2,"BG69A")



    play se "SGSE378"

    show screen phonebtn
    show screen phoneSD1
    "扔下这句话之后转身就走，抱着定时炸弹驶向了下水道深处。"
    $ stopvoc("DAR")
    play DAR "DAR09A_DAR0099"
    $ current_voice = "voice/DAR09A_DAR0099.ogg"
    "至" "「不行的，铃羽！　不行的！　快点回来！」"

    stop se
    "脚步声愈发疏远。"
    $ stopvoc("DAR")
    play DAR "DAR09A_DAR0100"
    $ current_voice = "voice/DAR09A_DAR0100.ogg"
    "至" "「铃羽啊啊啊！！」"
    "我的声音——"
    hide screen phoneSD1
    window hide

    stop se

    stop bgm 
    play se "SGSE313"



    $ loadBG(0,"BG_BLACK",hold=True)


    hide screen phonebtn
    with Fade(0.5,2,0.5,color="fff")
    "随着惊天一响和爆炸产生的冲击消散在了空中。"

    window hide






    return
