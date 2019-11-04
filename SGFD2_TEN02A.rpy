label SGFD2_TEN02A:
    window hide


    $ loadBG(0,"BG37A")

    play bgm "BGM18"

    play se "SGSE024"



    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='NAE')",DynamicDisplayable(mouthanime,"NAE_AMA01"),"True","lh/NAE_AMA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    $ date="8/12"
    $ day="THU"
    show screen phonebtn
    show screen phoneSD1

    $ stopvoc("NAE")
    play NAE "TEN02A_NAE0000"
    $ current_voice = "voice/TEN02A_NAE0000.ogg"
    "绹" "「我回来了，爸爸」"
    $ stopvoc("TEN")
    play TEN "TEN02A_TEN0000"
    $ current_voice = "voice/TEN02A_TEN0000.ogg"
    "天王寺" "「哦，是绹啊。今天挺早的嘛。暑假的补习班结束了？」"
    $ stopvoc("NAE")
    play NAE "TEN02A_NAE0001"
    $ current_voice = "voice/TEN02A_NAE0001.ogg"
    "绹" "「嗯。虽然说是补习班但只有一个小时啦。」"
    $ stopvoc("TEN")
    play TEN "TEN02A_TEN0001"
    $ current_voice = "voice/TEN02A_TEN0001.ogg"
    "天王寺" "「这样啊。虽然不太好意思，但我现在必须要去一趟店里。看家的任务就交给你了啊。」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='NAE')",DynamicDisplayable(mouthanime,"NAE_AMA02"),"True","lh/NAE_AMA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("NAE")
    play NAE "TEN02A_NAE0002"
    $ current_voice = "voice/TEN02A_NAE0002.ogg"
    "绹" "「好的。爸爸慢走。」"
    "如果是普通的家庭的话，暑假的时候双亲肯定会带着孩子去哪里玩吧。"
    "但是，我不太能挤得出时间陪她。"
    "虽然很抱歉，但请原谅我吧绹。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='NAE')",DynamicDisplayable(mouthanime,"NAE_AMA05"),"True","lh/NAE_AMA05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("NAE")
    play NAE "TEN02A_NAE0003"
    $ current_voice = "voice/TEN02A_NAE0003.ogg"
    "绹" "「咦？爸爸，那个是什么？」"
    $ stopvoc("TEN")
    play TEN "TEN02A_TEN0002"
    $ current_voice = "voice/TEN02A_TEN0002.ogg"
    "天王寺" "「嗯？　哪个？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='NAE')",DynamicDisplayable(mouthanime,"NAE_AMA01"),"True","lh/NAE_AMA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("NAE")
    play NAE "TEN02A_NAE0004"
    $ current_voice = "voice/TEN02A_NAE0004.ogg"
    "绹" "「那个放在桌子上的东西。是彩票？」"
    $ stopvoc("TEN")
    play TEN "TEN02A_TEN0003"
    $ current_voice = "voice/TEN02A_TEN0003.ogg"
    "天王寺" "「啊啊，最近买着玩的。每年夏天的惯例呢。」"
    "虽说我对于彩票并没有特别的兴趣，但夏天和冬天的时候会习惯性地买一点。"
    $ stopvoc("TEN")
    play TEN "TEN02A_TEN0004"
    $ current_voice = "voice/TEN02A_TEN0004.ogg"
    "天王寺" "「说起来昨天好像就是开奖日呢。如果有空的话，帮我看一下中奖号码吧。」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='NAE')",DynamicDisplayable(mouthanime,"NAE_AMA02"),"True","lh/NAE_AMA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("NAE")
    play NAE "TEN02A_NAE0005"
    $ current_voice = "voice/TEN02A_NAE0005.ogg"
    "绹" "「唔，明白了。」"
    window hide
    hide lh5  with dissolve
    "就算这么说，结果自然是不言而喻。"
    "每次只买不到１０张的我，怎么可能中奖呢。"
    "没中过超过３００円的奖。"
    "绹翻开了报纸，寻找着中奖号码。"
    "接着——"

    stop bgm 

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='NAE')",DynamicDisplayable(mouthanime,"NAE_AMA06"),"True","lh/NAE_AMA06a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("NAE")
    play NAE "TEN02A_NAE0006"
    $ current_voice = "voice/TEN02A_NAE0006.ogg"
    "绹" "「爸爸……」"
    $ stopvoc("TEN")
    play TEN "TEN02A_TEN0005"
    $ current_voice = "voice/TEN02A_TEN0005.ogg"
    "天王寺" "「嗯？　怎么了？」"
    $ stopvoc("NAE")
    play NAE "TEN02A_NAE0007"
    $ current_voice = "voice/TEN02A_NAE0007.ogg"
    "绹" "「爸爸，这个……」"
    $ stopvoc("TEN")
    play TEN "TEN02A_TEN0006"
    $ current_voice = "voice/TEN02A_TEN0006.ogg"
    "天王寺" "「哈哈哈，难道说中了一等奖？」"
    "反正是开玩笑，不如开得大一些。"
    "大概，是在找号码的时候，看到了什么在意的新闻吧。"
    $ stopvoc("NAE")
    play NAE "TEN02A_NAE0008"
    $ current_voice = "voice/TEN02A_NAE0008.ogg"
    "绹" "「嗯，中了哦，一等奖……」"
    $ stopvoc("TEN")
    play TEN "TEN02A_TEN0007"
    $ current_voice = "voice/TEN02A_TEN0007.ogg"
    "天王寺" "「喂喂绹，你不用配合我也可以哦」"
    $ stopvoc("NAE")
    play NAE "TEN02A_NAE0009"
    $ current_voice = "voice/TEN02A_NAE0009.ogg"
    "绹" "「不是开玩笑啦。真的中了一等奖哦！」"
    $ stopvoc("TEN")
    play TEN "TEN02A_TEN0008"
    $ current_voice = "voice/TEN02A_TEN0008.ogg"
    "天王寺" "「哈？　……来来快给我看看」"
    "肯定是『上当了呢～』这样的小把戏呢，不过就算是这样这种场合做爸爸的也要配合一下。"
    "我会被绹捉弄，真是难得啊……"
    hide screen phoneSD1
    window hide








    $ loadBG(6,"EV_TEN001A1",hold=True)




    $ loadBG(4,"EV_TEN001A4",png=True,hold=True)




    show expression "system/EV_TEN001A5~ipad.png" as lottery zorder 200 :
        pos (-1,-1)
        0.03 
        pos (0,1)
        0.03 
        pos (1,1)
        0.03 
        pos (1,-1)
        0.03 
        pos (-1,0)
        0.03 
        repeat
    with dissolve



















    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_TEN001A"]]["Check"]=True
    hide screen phonebtn





    $ stopvoc("TEN")
    play TEN "TEN02A_TEN0009"
    $ current_voice = "voice/TEN02A_TEN0009.ogg"
    "天王寺" "「唔哦，等等！这是……」"





    show expression "system/EV_TEN001A2~ipad.png" as nae_jump_left :
        linear 0.2pos (-50,-50)
        linear 0.2pos (0,0)
    pause 0.5
    hide nae_jump_left 
















    $ stopvoc("NAE")
    play NAE "TEN02A_NAE0010"
    $ current_voice = "voice/TEN02A_NAE0010.ogg"
    "绹" "「呐？　所以说刚才就说了」"


    play bgm "FD2BGM10"





    $ stopvoc("TEN")
    play TEN "TEN02A_TEN0010"
    $ current_voice = "voice/TEN02A_TEN0010.ogg"
    "天王寺" "「还真的是一样的号码？但给我等等，这不可能啊。中了一等奖什么的……」"


    "我反复比较彩票和报纸上刊登的号码。"
    $ stopvoc("TEN")
    play TEN "TEN02A_TEN0011"
    $ current_voice = "voice/TEN02A_TEN0011.ogg"
    "天王寺" "「１０４８６９。这边是……１０４８６９。一模一样。」"
    $ stopvoc("TEN")
    play TEN "TEN02A_TEN0012"
    $ current_voice = "voice/TEN02A_TEN0012.ogg"
    "天王寺" "「但是，肯定组对不上！肯定是那样没错。那样的话，可能金额不会很大也说不定」（注：日本彩票除了号码之外还有组的概念，如果组也对上的话会有额外奖励，即下文的“前后赏”）"
    show expression "system/EV_TEN001A3~ipad.png" as nae_jump_right :
        linear 0.2pos (50,-50)
        linear 0.2pos (0,0)
    pause 0.5
    hide nae_jump_right 





    $ stopvoc("NAE")
    play NAE "TEN02A_NAE0011"
    $ current_voice = "voice/TEN02A_NAE0011.ogg"
    "绹" "「组也对上了哦。你看你看」"


    $ stopvoc("TEN")
    play TEN "TEN02A_TEN0013"
    $ current_voice = "voice/TEN02A_TEN0013.ogg"
    "天王寺" "「８１组的１０４８６９。然后，这边是……８１组！？　不可能……」"





    $ stopvoc("NAE")
    play NAE "TEN02A_NAE0012"
    $ current_voice = "voice/TEN02A_NAE0012.ogg"
    "绹" "「呐，真的是中奖了呀？」"


    $ stopvoc("TEN")
    play TEN "TEN02A_TEN0014"
    $ current_voice = "voice/TEN02A_TEN0014.ogg"
    "天王寺" "「为啥真中了啊……」"
    "这一定是奇迹。"
    "不，已经超过了奇迹的程度了吧……"
    "明明没中过３００円以上的奖，这次好像撞大运了。"
    $ stopvoc("TEN")
    play TEN "TEN02A_TEN0015"
    $ current_voice = "voice/TEN02A_TEN0015.ogg"
    "天王寺" "「绹、绹……。这个彩票的一等奖，有多少钱？」"
    $ stopvoc("NAE")
    play NAE "TEN02A_NAE0013"
    $ current_voice = "voice/TEN02A_NAE0013.ogg"
    "绹" "「那个，前后赏我们也中了呢。加起来的话——」"
    $ stopvoc("NAE")
    play NAE "TEN02A_NAE0014"
    $ current_voice = "voice/TEN02A_NAE0014.ogg"
    "绹" "「１等奖是２亿日元，前后赏各５千万日元。所以一共是……」"















    $ stopvoc("MIX")
    play voc "TEN02A_MIX0000"
    $ current_voice = "voice/TEN02A_MIX0000.ogg"
    "天王寺＆绹" "「３亿日元……！」\n「３亿日元……！」"









    $ stopvoc("TEN")
    play TEN "TEN02A_TEN0017"
    $ current_voice = "voice/TEN02A_TEN0017.ogg"
    "天王寺" "「这是真的吗……」"
    "这是多少钱啊……简直难以想象。"
    "就算作为这栋大楼的房主，我也没见过这么多钱。"
    $ stopvoc("TEN")
    play TEN "TEN02A_TEN0018"
    $ current_voice = "voice/TEN02A_TEN0018.ogg"
    "天王寺" "「真的是真的吗？彩票的期数没看错吧？」"
    $ stopvoc("NAE")
    play NAE "TEN02A_NAE0016"
    $ current_voice = "voice/TEN02A_NAE0016.ogg"
    "绹" "「嗯，没问题哦。那里写得很清楚，第５６６回期」"
    $ stopvoc("TEN")
    play TEN "TEN02A_TEN0019"
    $ current_voice = "voice/TEN02A_TEN0019.ogg"
    "天王寺" "「真的……中奖了么」"
    "就算已经接受了无可非议的现实，但是完全不知道该怎么反应。"
    "３亿日元该怎么用呢。"









    $ stopvoc("TEN")
    play TEN "TEN02A_TEN0020"
    $ current_voice = "voice/TEN02A_TEN0020.ogg"
    "天王寺" "「这，这样啊绹。总之先买些什么吧。买你喜欢的东西」"


    $ stopvoc("NAE")
    play NAE "TEN02A_NAE0017"
    $ current_voice = "voice/TEN02A_NAE0017.ogg"
    "绹" "「真的？谢谢你，爸爸！」"
    $ stopvoc("TEN")
    play TEN "TEN02A_TEN0021"
    $ current_voice = "voice/TEN02A_TEN0021.ogg"
    "天王寺" "「比起道谢，先说说你想要什么吧」"





    $ stopvoc("NAE")
    play NAE "TEN02A_NAE0018"
    $ current_voice = "voice/TEN02A_NAE0018.ogg"
    "绹" "「但就算你突然这么问我……」"


    $ stopvoc("TEN")
    play TEN "TEN02A_TEN0022"
    $ current_voice = "voice/TEN02A_TEN0022.ogg"
    "天王寺" "「想到什么说什么吧，来，快点」"








    $ stopvoc("NAE")
    play NAE "TEN02A_NAE0019"
    $ current_voice = "voice/TEN02A_NAE0019.ogg"
    "绹" "「那，肉馒头」"


    $ stopvoc("TEN")
    play TEN "TEN02A_TEN0023"
    $ current_voice = "voice/TEN02A_TEN0023.ogg"
    "天王寺" "「肉馒头？这么热的天还想吃肉馒头吗？更加奢侈一点的东西也可以哦」"








    $ stopvoc("NAE")
    play NAE "TEN02A_NAE0020"
    $ current_voice = "voice/TEN02A_NAE0020.ogg"
    "绹" "「那，肉馒头两个！」"


    $ stopvoc("TEN")
    play TEN "TEN02A_TEN0024"
    $ current_voice = "voice/TEN02A_TEN0024.ogg"
    "天王寺" "「再厉害点，夸张一些」"








    $ stopvoc("NAE")
    play NAE "TEN02A_NAE0021"
    $ current_voice = "voice/TEN02A_NAE0021.ogg"
    "绹" "「那，肉馒头５个！！」"


    $ stopvoc("TEN")
    play TEN "TEN02A_TEN0025"
    $ current_voice = "voice/TEN02A_TEN0025.ogg"
    "天王寺" "「喂喂，那肯定会吃撑的吧。而且一般来说会带个豆沙馒头吧？」"








    $ stopvoc("NAE")
    play NAE "TEN02A_NAE0022"
    $ current_voice = "voice/TEN02A_NAE0022.ogg"
    "绹" "「那我要肉馒头４个和豆沙馒头１个！」"


    "虽然觉得没必要减少肉馒头的数量，但那怎样都好了。"
    "是因为我和绹都太兴奋了么，对话好像一直停留在很肤浅的状态。"
    "但是……"





    $ stopvoc("TEN")
    play TEN "TEN02A_TEN0026"
    $ current_voice = "voice/TEN02A_TEN0026.ogg"
    "天王寺" "「等等哦。说不定这次的奖金是个好机会呢」"


    $ stopvoc("NAE")
    play NAE "TEN02A_NAE0023"
    $ current_voice = "voice/TEN02A_NAE0023.ogg"
    "绹" "「……爸爸？」"
    "有３亿元的话，大部分东西都能买到了。"
    "不管想要什么都可以搞到手。"
    "不光可以把家里重新装修一遍，还能买些家具。"
    "看来我刚刚得到了通向幸福的车票。"
    "有了这３亿元的话，我一定能做出绹的“理想的家”来。"
    "虽然还不知道到底该做成什么样子，但至少资金是不用愁了。"
    $ stopvoc("TEN")
    play TEN "TEN02A_TEN0027"
    $ current_voice = "voice/TEN02A_TEN0027.ogg"
    "天王寺" "「好勒，绹。我想到了个好主意，交给我吧」"





    $ stopvoc("NAE")
    play NAE "TEN02A_NAE0024"
    $ current_voice = "voice/TEN02A_NAE0024.ogg"
    "绹" "「把什么交给你？」"


    $ stopvoc("TEN")
    play TEN "TEN02A_TEN0028"
    $ current_voice = "voice/TEN02A_TEN0028.ogg"
    "天王寺" "「你只要相信我就行了。就让你看看我的绝世好点子吧」"
    window hide

    stop bgm
    hide lottery 
    hide background-png 






    $ loadBG(2,"BG79A3")








    show screen phonebtn
    show screen phoneSD1






    $ stopvoc("MIX")
    play voc "TEN02A_MIX0001"
    $ current_voice = "voice/TEN02A_MIX0001.ogg"
    "Ｌａｂｍｅｍ们" "「「「「「「要翻新大楼！？」」」」」」"


    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA04"),"True","lh/OKA_ASA04a~ipad.png") at right_q1 as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSB02"),"True","lh/MAY_CSB02a~ipad.png") at left_q2 as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15

    hide lh7 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASC04"),"True","lh/CRS_ASC04a~ipad.png") at left_q1 as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15

    hide lh8 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASB04"),"True","lh/DAR_ASB04a~ipad.png") at right_q2 as lh8 zorder (10-8) :
        yanchor 1.0
        ypos 1.15
    $ loadBG(0,"BG01A",hide=False)


    play bgm "BGM05"



    $ stopvoc("TEN")
    play TEN "TEN02A_TEN0029"
    $ current_voice = "voice/TEN02A_TEN0029.ogg"
    "天王寺" "「啊啊，是的。说出来吓你们一跳哦。其实我中了彩票的一等奖呢。」"
    $ stopvoc("TEN")
    play TEN "TEN02A_TEN0030"
    $ current_voice = "voice/TEN02A_TEN0030.ogg"
    "天王寺" "「然后我转念一想，这个大楼已经挺破旧了，是时候给绹建一个新家了。」"
    $ stopvoc("CRS")
    play CRS "TEN02A_CRS0001"
    $ current_voice = "voice/TEN02A_CRS0001.ogg"
    "红莉栖" "「彩票一等奖！？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSB01"),"True","lh/MAY_CSB01a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "TEN02A_MAY0001"
    $ current_voice = "voice/TEN02A_MAY0001.ogg"
    "真由理" "「唔哇，好厉害呀ー」"
    $ stopvoc("DAR")
    play DAR "TEN02A_DAR0001"
    $ current_voice = "voice/TEN02A_DAR0001.ogg"
    "至" "「竟然还能有这样的超展开嗷」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA03"),"True","lh/OKA_ASA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "TEN02A_OKA0001"
    $ current_voice = "voice/TEN02A_OKA0001.ogg"
    "伦太郎" "「太脏了！太脏了啊Ｍｒ．布朗！」"
    $ stopvoc("TEN")
    play TEN "TEN02A_TEN0031"
    $ current_voice = "voice/TEN02A_TEN0031.ogg"
    "天王寺" "「啊？　脏什么的，你在说啥啊冈部？」"
    $ stopvoc("OKA")
    play OKA "TEN02A_OKA0002"
    $ current_voice = "voice/TEN02A_OKA0002.ogg"
    "伦太郎" "「就连我们之前的最后也只中了三等奖，你这家伙不仅毫不客气地把自己的欲望说了出来，还实现了啊。」"
    $ stopvoc("OKA")
    play OKA "TEN02A_OKA0003"
    $ current_voice = "voice/TEN02A_OKA0003.ogg"
    "伦太郎" "「顽冥不灵的愚者因为无知将所期望之物攫入手中。这便是所谓混沌中的真实吗？」"
    $ stopvoc("TEN")
    play TEN "TEN02A_TEN0032"
    $ current_voice = "voice/TEN02A_TEN0032.ogg"
    "天王寺" "「和平时一样还是完全无法理解你的发言呢」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSC02"),"True","lh/MAY_CSC02a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "TEN02A_MAY0002"
    $ current_voice = "voice/TEN02A_MAY0002.ogg"
    "真由理" "「就是啊冈伦。三等奖是在说什么？」"
    $ stopvoc("OKA")
    play OKA "TEN02A_OKA0004"
    $ current_voice = "voice/TEN02A_OKA0004.ogg"
    "伦太郎" "「难道忘了吗，真由理哦。之前用Ｄｍａｉｌ的时候……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA04"),"True","lh/OKA_ASA04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "TEN02A_OKA0005"
    $ current_voice = "voice/TEN02A_OKA0005.ogg"
    "伦太郎" "「……不对，没事。想了一下好像是你们不知道的事情」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSB03"),"True","lh/MAY_CSB03a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "TEN02A_MAY0003"
    $ current_voice = "voice/TEN02A_MAY0003.ogg"
    "真由理" "「嗯？」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh7 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MOE')",DynamicDisplayable(mouthanime,"MOE_ASA01"),"True","lh/MOE_ASA01a~ipad.png") at center as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    $ targetmailid = gc["ScriptMacros"]["FM_TEN02A_RECV_MOE01"]
    if phonemailring!= "":
        play se phonemailring
    if persistent.skipmail==False:
        $ renpy.choice_for_skipping()
    if targetmailid != "":
        $ RcvMail(targetmailid)
        $ targetmailid=""

    show expression ConditionSwitch("renpy.music.get_playing(channel='MOE')",DynamicDisplayable(mouthanime,"MOE_ASB01"),"True","lh/MOE_ASB01a~ipad.png") at center as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    hide screen phonebtn
    hide screen phonebtn2 
    call read_last_mail



    $ stopvoc("TEN")
    play TEN "TEN02A_TEN0033"
    $ current_voice = "voice/TEN02A_TEN0033.ogg"
    "天王寺" "「萌郁。你还是喜欢发邮件吗。在面前的时候就好好地说话啊，好好地」"
    call hide_phone
    window hide

    hide lh7 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MOE')",DynamicDisplayable(mouthanime,"MOE_ASA01"),"True","lh/MOE_ASA01a~ipad.png") at center as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    $ targetmailid = gc["ScriptMacros"]["FM_TEN02A_RECV_MOE02"]
    if phonemailring!= "":
        play se phonemailring
    if persistent.skipmail==False:
        $ renpy.choice_for_skipping()
    if targetmailid != "":
        $ RcvMail(targetmailid)
        $ targetmailid=""

    show expression ConditionSwitch("renpy.music.get_playing(channel='MOE')",DynamicDisplayable(mouthanime,"MOE_ASB01"),"True","lh/MOE_ASB01a~ipad.png") at center as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)








    call read_last_mail
    $ stopvoc("TEN")
    play TEN "TEN02A_TEN0034"
    $ current_voice = "voice/TEN02A_TEN0034.ogg"
    "天王寺" "「哈，真拿你没办法啊……」"
    window hide
    call hide_phone


    show expression im.AlphaMask("bg/BG_BLACK~ipad.jpg",im.Scale(im.MatrixColor("mask/mask17.png",im.matrix.invert()),1024,576)) as bg2 behind lh5 
    hide screen phonebtn
    "这家伙是桐生萌郁。"
    "她和我关系稍微深一些。"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_STUDIO_CRT"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_STUDIO_CRT"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_STUDIO_CRT"])

    "嘛，但也没办法呢。"
    "我在出差的时候店里没人看管，比起那样的话有人在总还稍微好一些吧。"
    window hide
    hide bg2 

    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA01"),"True","lh/OKA_ASA01a~ipad.png") at right as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASA01"),"True","lh/CRS_ASA01a~ipad.png") at left as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    show screen phonebtn
    $ stopvoc("CRS")
    play CRS "TEN02A_CRS0002"
    $ current_voice = "voice/TEN02A_CRS0002.ogg"
    "红莉栖" "「店长。如果把大楼翻新的话，我们是不是也能在崭新的Ｌａｂ里活动了？」"
    $ stopvoc("OKA")
    play OKA "TEN02A_OKA0006"
    $ current_voice = "voice/TEN02A_OKA0006.ogg"
    "伦太郎" "「唔，不用想都知道是这样的吧。但是可不能涨房租哦，Ｍｒ．布朗。我们之前的合同可是灵魂契约一样的存在哦。」"
    $ stopvoc("TEN")
    play TEN "TEN02A_TEN0035"
    $ current_voice = "voice/TEN02A_TEN0035.ogg"
    "天王寺" "「放心吧，不会涨房租的。大楼翻新的话，房客也要翻新呢。没有给你们租的地方了」"
    $ stopvoc("TEN")
    play TEN "TEN02A_TEN0036"
    $ current_voice = "voice/TEN02A_TEN0036.ogg"
    "天王寺" "「所以现在全部给我出去，就现在」"
    window hide


    $ loadBG(2,"BG79A3")
















    with vpunch
    $ stopvoc("MIX")
    play voc "TEN02A_MIX0002"
    $ current_voice = "voice/TEN02A_MIX0002.ogg"
    "Ｌａｂｍｅｍ们" "「「「「「「什───么───！？」」」」」」"


    window hide
    with dissolve





    $ targetmailid = gc["ScriptMacros"]["RM_TEN_RECV_NAE01_01"]

    $ LR_RM_CHANCE=6
    call CHECK_RM_RECEIVE
    $ stopvoc("TEN")
    play TEN "TEN02A_TEN0037"
    $ current_voice = "voice/TEN02A_TEN0037.ogg"
    "天王寺" "「笨蛋。玩笑，是玩笑啦。你们好夸张哦」"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA04"),"True","lh/OKA_ASA04a~ipad.png") at right_q1 as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='RUK')",DynamicDisplayable(mouthanime,"RUK_CSA02"),"True","lh/RUK_CSA02a~ipad.png") at left_q2 as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15

    hide lh7 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASC04"),"True","lh/CRS_ASC04a~ipad.png") at left_q1 as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15

    hide lh8 
    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_DSA03"),"True","lh/FEI_DSA03a~ipad.png") at right_q2 as lh8 zorder (10-8) :
        yanchor 1.0
        ypos 1.15
    $ loadBG(0,"BG01A",hide=False)

    call CHECK_RM_RECEIVE
    $ stopvoc("RUK")
    play RUK "TEN02A_RUK0002"
    $ current_voice = "voice/TEN02A_RUK0002.ogg"
    "琉华" "「这玩笑对心脏不太好哦……是吧，冈部师傅。」"
    call CHECK_RM_RECEIVE
    $ stopvoc("FEI")
    play FEI "TEN02A_FEI0002"
    $ current_voice = "voice/TEN02A_FEI0002.ogg"
    "菲利斯" "「汗毛都竖起来了喵。以为这么好的地方就要没有了喵」"
    call CHECK_RM_RECEIVE
    $ stopvoc("TEN")
    play TEN "TEN02A_TEN0038"
    $ current_voice = "voice/TEN02A_TEN0038.ogg"
    "天王寺" "「总之别当真了。你们连这点玩笑都开不起嘛」"
    call CHECK_RM_RECEIVE
    $ stopvoc("OKA")
    play OKA "TEN02A_OKA0008"
    $ current_voice = "voice/TEN02A_OKA0008.ogg"
    "伦太郎" "「真真真真是的。这个Ｌａｂ当然不会消失的咯。哈哈哈哈……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASB07"),"True","lh/CRS_ASB07a~ipad.png") as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    call CHECK_RM_RECEIVE
    $ stopvoc("CRS")
    play CRS "TEN02A_CRS0004"
    $ current_voice = "voice/TEN02A_CRS0004.ogg"
    "红莉栖" "「喂，你才是怕得最厉害的那个吧」"

    call CHECK_RM_RECEIVE
    $ stopvoc("OKA")
    play OKA "TEN02A_OKA0009"
    $ current_voice = "voice/TEN02A_OKA0009.ogg"
    "伦太郎" "「烦烦烦烦死了！这是……夏天太热了所以身体紧张得颤抖起来了，也就是所谓的炎热的微焦躁( Fran men・Weis Palace )，才不是吓得口吃了！」"

    $ gd["RCVmailData"][gc["ScriptMacros"]["RM_TEN_RECV_NAE01_01"]]["late"]=True
    $ lml.append(gc["ScriptMacros"]["RM_TEN_RECV_NAE01_01"])

    $ stopvoc("TEN")
    play TEN "TEN02A_TEN0039"
    $ current_voice = "voice/TEN02A_TEN0039.ogg"
    "天王寺" "「那么，差不多该进入正题了。在翻新大楼之前，也想听听你们的建议啊」"
    $ stopvoc("TEN")
    play TEN "TEN02A_TEN0040"
    $ current_voice = "voice/TEN02A_TEN0040.ogg"
    "天王寺" "「是按照现在的样子简单地进行装修呢，还是完全地重造呢，哪边会比较好……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA05"),"True","lh/OKA_ASA05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "TEN02A_OKA0010"
    $ current_voice = "voice/TEN02A_OKA0010.ogg"
    "伦太郎" "「原来如此，是想来听听我们的高见啊。」"
    $ stopvoc("TEN")
    play TEN "TEN02A_TEN0041"
    $ current_voice = "voice/TEN02A_TEN0041.ogg"
    "天王寺" "「没你说的那么夸张。就是参考一下而已」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_DSA02"),"True","lh/FEI_DSA02a~ipad.png") as lh8 zorder (10-8) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FEI")
    play FEI "TEN02A_FEI0003"
    $ current_voice = "voice/TEN02A_FEI0003.ogg"
    "菲利斯" "「好的好的！这样的话，我觉得这么做不错哦」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    "开始这个话题后，大家都你一言我一语地说了起来。"
    "为了让这里变成绹能感到快乐的地方，当然要听听年轻人的意见咯。"

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASB01"),"True","lh/CRS_ASB01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA01"),"True","lh/MAY_CSA01a~ipad.png") at left_t as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh7 
    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_DSA01"),"True","lh/FEI_DSA01a~ipad.png") at right_t as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    $ targetmailid = cml.setdefault("RM_TEN_SEND_NAE01","")

    $ LR_RM_CHANCE=18
    call CHECK_RM_RECEIVE
    $ stopvoc("CRS")
    play CRS "TEN02A_CRS0005"
    $ current_voice = "voice/TEN02A_CRS0005.ogg"
    "红莉栖" "「显像管工房和Ｌａｂ可以只做翻新，问题是三楼以上的部分该怎么规划」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_DSB01"),"True","lh/FEI_DSB01a~ipad.png") as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    call CHECK_RM_RECEIVE
    $ stopvoc("FEI")
    play FEI "TEN02A_FEI0004"
    $ current_voice = "voice/TEN02A_FEI0004.ogg"
    "菲利斯" "「说起来改造成？『ＭａｙＱｕｅｅｎ＋Ｎｙａ²』２号店如何啊」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA02"),"True","lh/MAY_CSA02a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    call CHECK_RM_RECEIVE
    $ stopvoc("MAY")
    play MAY "TEN02A_MAY0005"
    $ current_voice = "voice/TEN02A_MAY0005.ogg"
    "真由理" "「哇，如果楼上变成咖啡厅的话，打工就超级方便了呢」"
    hide lh6  with dissolve

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='RUK')",DynamicDisplayable(mouthanime,"RUK_CSB01"),"True","lh/RUK_CSB01a~ipad.png") at left_t as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    call CHECK_RM_RECEIVE
    $ stopvoc("RUK")
    play RUK "TEN02A_RUK0003"
    $ current_voice = "voice/TEN02A_RUK0003.ogg"
    "琉华" "「但是，这个大楼的面积对于咖啡厅来说是不是有点太小了？」"
    hide lh7 

    hide lh7 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA07"),"True","lh/DAR_ASA07a~ipad.png") at right_t as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    call CHECK_RM_RECEIVE
    $ stopvoc("DAR")
    play DAR "TEN02A_DAR0003"
    $ current_voice = "voice/TEN02A_DAR0003.ogg"
    "至" "「太小的话，就会又小又挤，听起来感觉不错呢」"




    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASB04"),"True","lh/CRS_ASB04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)







    call CHECK_RM_RECEIVE
    $ stopvoc("CRS")
    play CRS "TEN02A_CRS0006"
    $ current_voice = "voice/TEN02A_CRS0006.ogg"
    "红莉栖" "「闭嘴ＨＥＮＴＡＩ。其他还有呢？」"


    hide lh7 

    hide lh7 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA01"),"True","lh/OKA_ASA01a~ipad.png") at right_t as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    call CHECK_RM_RECEIVE
    $ stopvoc("OKA")
    play OKA "TEN02A_OKA0011"
    $ current_voice = "voice/TEN02A_OKA0011.ogg"
    "伦太郎" "「嘛，确实如琉华子所说作为店铺是太小了。但作为小的办公室或者住处就挺不错的哦」"
    hide lh6  with dissolve

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSB03"),"True","lh/MAY_CSB03a~ipad.png") at left_t as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    call CHECK_RM_RECEIVE
    $ stopvoc("MAY")
    play MAY "TEN02A_MAY0006"
    $ current_voice = "voice/TEN02A_MAY0006.ogg"
    "真由理" "「住处？把Ｌａｂ上面变成别人的家吗？」"
    call CHECK_RM_RECEIVE
    $ stopvoc("OKA")
    play OKA "TEN02A_OKA0012"
    $ current_voice = "voice/TEN02A_OKA0012.ogg"
    "伦太郎" "「是的哦。单人间的出租啦分售啦。然后还可以让Christina住进去。」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASC04"),"True","lh/CRS_ASC04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    call CHECK_RM_RECEIVE
    $ stopvoc("CRS")
    play CRS "TEN02A_CRS0007"
    $ current_voice = "voice/TEN02A_CRS0007.ogg"
    "红莉栖" "「我吗？为什么呢？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASB01"),"True","lh/OKA_ASB01a~ipad.png") as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    call CHECK_RM_RECEIVE
    $ stopvoc("OKA")
    play OKA "TEN02A_OKA0013"
    $ current_voice = "voice/TEN02A_OKA0013.ogg"
    "伦太郎" "「现在你还是住在宾馆的，所以这边的房租也就一起付一下吧？然后你的新住处还可以暂时充当Ｌａｂ的材料仓库。唔哈哈哈哈哈！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASB04"),"True","lh/CRS_ASB04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    call CHECK_RM_RECEIVE
    $ stopvoc("CRS")
    play CRS "TEN02A_CRS0008"
    $ current_voice = "voice/TEN02A_CRS0008.ogg"
    "红莉栖" "「住宾馆还真是抱歉了哈！而且怎么听上去就没打算让我住进去的感觉啊！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA03"),"True","lh/MAY_CSA03a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    call CHECK_RM_RECEIVE
    $ stopvoc("MAY")
    play MAY "TEN02A_MAY0007"
    $ current_voice = "voice/TEN02A_MAY0007.ogg"
    "真由理" "「啊、但是」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA01"),"True","lh/OKA_ASA01a~ipad.png") as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    call CHECK_RM_RECEIVE
    $ stopvoc("OKA")
    play OKA "TEN02A_OKA0014"
    $ current_voice = "voice/TEN02A_OKA0014.ogg"
    "伦太郎" "「怎么了真由理？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA04"),"True","lh/MAY_CSA04a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    call CHECK_RM_RECEIVE
    $ stopvoc("MAY")
    play MAY "TEN02A_MAY0008"
    $ current_voice = "voice/TEN02A_MAY0008.ogg"
    "真由理" "「先不说楼上。如果大楼被翻新了，这个Ｌａｂ不就要完全变成另一个房间了么。那样的话有点寂寞呢。」"
    hide lh6  with dissolve

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='RUK')",DynamicDisplayable(mouthanime,"RUK_CSA02"),"True","lh/RUK_CSA02a~ipad.png") at left_t as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    call CHECK_RM_RECEIVE
    $ stopvoc("RUK")
    play RUK "TEN02A_RUK0004"
    $ current_voice = "voice/TEN02A_RUK0004.ogg"
    "琉华" "「啊，是呢。不是光光换个样子，肯定房间的布局什么的都要变吧」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASC05"),"True","lh/CRS_ASC05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    call CHECK_RM_RECEIVE
    $ stopvoc("CRS")
    play CRS "TEN02A_CRS0009"
    $ current_voice = "voice/TEN02A_CRS0009.ogg"
    "红莉栖" "「如果房间的配置变化了，说不定会影响电话微波炉的性能呢……」"
    call CHECK_RM_RECEIVE
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_DENWA_RANGE"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_DENWA_RANGE"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_DENWA_RANGE"])
    $ stopvoc("OKA")
    play OKA "TEN02A_OKA0015"
    $ current_voice = "voice/TEN02A_OKA0015.ogg"
    "伦太郎" "「狭隘！太狭隘了啊，你们。为了科学的发展，肯定有所牺牲嘛。{color=#f00}电话微波炉（暂）{/color}的话，放在和原来一样的位置的话就没问题了。」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASB01"),"True","lh/OKA_ASB01a~ipad.png") as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    call CHECK_RM_RECEIVE
    $ stopvoc("OKA")
    play OKA "TEN02A_OKA0016"
    $ current_voice = "voice/TEN02A_OKA0016.ogg"
    "伦太郎" "「终于到了这个时候了！我们的据点终于要从破旧的大楼重生成最新的科学要塞了。唔哈哈哈哈哈！」"

    $ gd["RCVmailData"][gc["ScriptMacros"]["RM_TEN_RECV_NAE02_01"]]["late"]=True
    $ lml.append(gc["ScriptMacros"]["RM_TEN_RECV_NAE02_01"])

    $ stopvoc("TEN")
    play TEN "TEN02A_TEN0042"
    $ current_voice = "voice/TEN02A_TEN0042.ogg"
    "天王寺" "「什么呀冈部。你这家伙，刚刚说的和之前说的相去甚远呢」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA05"),"True","lh/OKA_ASA05a~ipad.png") as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "TEN02A_OKA0017"
    $ current_voice = "voice/TEN02A_OKA0017.ogg"
    "伦太郎" "「嗯？　之前说的？」"
    $ stopvoc("TEN")
    play TEN "TEN02A_TEN0043"
    $ current_voice = "voice/TEN02A_TEN0043.ogg"
    "天王寺" "「明明在租房子之前还说什么“这样的居住环境最棒了”的话」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASC04"),"True","lh/CRS_ASC04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    show expression ConditionSwitch("renpy.music.get_playing(channel='RUK')",DynamicDisplayable(mouthanime,"RUK_CSB04"),"True","lh/RUK_CSB04a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("RUK")
    play RUK "TEN02A_RUK0005"
    $ current_voice = "voice/TEN02A_RUK0005.ogg"
    "琉华" "「租房子之前？有说过那样的话么？」"
    $ stopvoc("TEN")
    play TEN "TEN02A_TEN0044"
    $ current_voice = "voice/TEN02A_TEN0044.ogg"
    "天王寺" "「啊啊，可能忘了吧。大概是半年之前的事了……」"
    window hide
    hide screen phonebtn
    hide screen phoneSD1

    stop bgm 


    $ loadBG(0,"BG04A2")

    play bgm "BGM13"

    play se "SGSE017"

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA01"),"True","lh/OKA_ASA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "TEN02A_OKA0018"
    $ current_voice = "voice/TEN02A_OKA0018.ogg"
    "伦太郎" "「店长！　店长在吗？」"
    $ stopvoc("TEN")
    play TEN "TEN02A_TEN0045"
    $ current_voice = "voice/TEN02A_TEN0045.ogg"
    "天王寺" "「我就是，你这家伙怎么了吗」"
    "一个喘着气的奇怪家伙跑了进来。"
    "这幅打扮，是学者什么的吗？"
    "不对，他太年轻了，而且也没有研究者的那种感觉。"
    "大概是个烦人的家伙吧。"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_AMA01"),"True","lh/OKA_AMA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "TEN02A_OKA0019"
    $ current_voice = "voice/TEN02A_OKA0019.ogg"
    "伦太郎" "「看到外面的告示进来的，这个大楼的２楼还在出租中吗？」"
    $ stopvoc("TEN")
    play TEN "TEN02A_TEN0046"
    $ current_voice = "voice/TEN02A_TEN0046.ogg"
    "天王寺" "「啊啊，确实。」"
    $ stopvoc("OKA")
    play OKA "TEN02A_OKA0020"
    $ current_voice = "voice/TEN02A_OKA0020.ogg"
    "伦太郎" "「“租金面议”也是？」"
    $ stopvoc("TEN")
    play TEN "TEN02A_TEN0047"
    $ current_voice = "voice/TEN02A_TEN0047.ogg"
    "天王寺" "「啊啊，如你所见，这并不是什么高价的大楼」"
    $ stopvoc("OKA")
    play OKA "TEN02A_OKA0021"
    $ current_voice = "voice/TEN02A_OKA0021.ogg"
    "伦太郎" "「那，那样的话能租给我吗？当然我能付多少付多少。」"
    $ stopvoc("TEN")
    play TEN "TEN02A_TEN0048"
    $ current_voice = "voice/TEN02A_TEN0048.ogg"
    "天王寺" "「你打算给多少？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_AMA04"),"True","lh/OKA_AMA04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "TEN02A_OKA0022"
    $ current_voice = "voice/TEN02A_OKA0022.ogg"
    "伦太郎" "「……诶？」"
    $ stopvoc("TEN")
    play TEN "TEN02A_TEN0049"
    $ current_voice = "voice/TEN02A_TEN0049.ogg"
    "天王寺" "「慢慢说吧。你说说你能出多少」"
    $ stopvoc("OKA")
    play OKA "TEN02A_OKA0023"
    $ current_voice = "voice/TEN02A_OKA0023.ogg"
    "伦太郎" "「这、这个价格怎么样？」"
    "那小鬼打了一会儿计算器，然后告诉了我。"
    $ stopvoc("TEN")
    play TEN "TEN02A_TEN0050"
    $ current_voice = "voice/TEN02A_TEN0050.ogg"
    "天王寺" "「你这家伙，是来讨架打的么？」"
    $ stopvoc("OKA")
    play OKA "TEN02A_OKA0024"
    $ current_voice = "voice/TEN02A_OKA0024.ogg"
    "伦太郎" "「不是，并没有那个意思……」"
    $ stopvoc("TEN")
    play TEN "TEN02A_TEN0051"
    $ current_voice = "voice/TEN02A_TEN0051.ogg"
    "天王寺" "「那样的话就学得识相点。会有那种价格把一层楼租出去的家伙么」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_AMA03"),"True","lh/OKA_AMA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "TEN02A_OKA0025"
    $ current_voice = "voice/TEN02A_OKA0025.ogg"
    "伦太郎" "「那怎么说呢！我对于……对于这个大楼非常的喜欢。它的风格啦，那种在这个时代坚挺下去的氛围啦」"
    $ stopvoc("OKA")
    play OKA "TEN02A_OKA0026"
    $ current_voice = "voice/TEN02A_OKA0026.ogg"
    "伦太郎" "「其实我认为这里的氛围很棒！　我的Ｌａｂ非这栋大楼莫属了！」"
    $ stopvoc("TEN")
    play TEN "TEN02A_TEN0052"
    $ current_voice = "voice/TEN02A_TEN0052.ogg"
    "天王寺" "「Ｌａｂ？你这家伙，果然是研究者什么的吗？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_AMB01"),"True","lh/OKA_AMB01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "TEN02A_OKA0027"
    $ current_voice = "voice/TEN02A_OKA0027.ogg"
    "伦太郎" "「不对，不光光是研究者。我这个人是，终将让世界震撼的狂气的疯狂科学家，凤凰院凶真。唔哈哈哈哈哈！」"
    $ stopvoc("TEN")
    play TEN "TEN02A_TEN0053"
    $ current_voice = "voice/TEN02A_TEN0053.ogg"
    "天王寺" "「给我回去吧」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_AMA04"),"True","lh/OKA_AMA04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "TEN02A_OKA0028"
    $ current_voice = "voice/TEN02A_OKA0028.ogg"
    "伦太郎" "「……我叫冈部伦太郎。」"
    window hide

    stop bgm 


    $ loadBG(0,"BG01A")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA01"),"True","lh/OKA_ASA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    show screen phonebtn
    show screen phoneSD1
    play bgm "BGM05"
    $ stopvoc("TEN")
    play TEN "TEN02A_TEN0054"
    $ current_voice = "voice/TEN02A_TEN0054.ogg"
    "天王寺" "「刚刚还不是说自己有多牛x么」"
    $ stopvoc("OKA")
    play OKA "TEN02A_OKA0029"
    $ current_voice = "voice/TEN02A_OKA0029.ogg"
    "伦太郎" "「哼，刚才只是非我本意的自夸罢了」"

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='RUK')",DynamicDisplayable(mouthanime,"RUK_CSB04"),"True","lh/RUK_CSB04a~ipad.png") at left_t as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("RUK")
    play RUK "TEN02A_RUK0006"
    $ current_voice = "voice/TEN02A_RUK0006.ogg"
    "琉华" "「诶……还有这样的事啊。就那样租给冈部师傅了吗？」"
    $ stopvoc("TEN")
    play TEN "TEN02A_TEN0055"
    $ current_voice = "voice/TEN02A_TEN0055.ogg"
    "天王寺" "「没有，没租给他。那个时候就觉得只是个烦人的家伙罢了。」"
    hide lh6  with dissolve

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASB07"),"True","lh/CRS_ASB07a~ipad.png") at left_t as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "TEN02A_CRS0010"
    $ current_voice = "voice/TEN02A_CRS0010.ogg"
    "红莉栖" "「……不管是谁都会那么做吧。」"

    hide lh7 
    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_DSC01"),"True","lh/FEI_DSC01a~ipad.png") at right_t as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FEI")
    play FEI "TEN02A_FEI0005"
    $ current_voice = "voice/TEN02A_FEI0005.ogg"
    "菲利斯" "「那，为什么最后又变成租给凶真了喵？」"
    $ stopvoc("TEN")
    play TEN "TEN02A_TEN0056"
    $ current_voice = "voice/TEN02A_TEN0056.ogg"
    "天王寺" "「那个呢。……以后有机会说给你们听吧。今天没时间了。」"
    $ stopvoc("TEN")
    play TEN "TEN02A_TEN0057"
    $ current_voice = "voice/TEN02A_TEN0057.ogg"
    "天王寺" "「也就是说对于大楼的重建既有赞成的也有反对的。是这样吧？」"
    $ stopvoc("OKA")
    play OKA "TEN02A_OKA0030"
    $ current_voice = "voice/TEN02A_OKA0030.ogg"
    "伦太郎" "「啊啊。没关系。看起来是赞成方占优势所以没事。」"
    $ stopvoc("TEN")
    play TEN "TEN02A_TEN0058"
    $ current_voice = "voice/TEN02A_TEN0058.ogg"
    "天王寺" "「这不是优势吧冈部，只是你这家伙声音比较大而已。那就这样了，打扰了。」"
    window hide

    stop bgm 



    $ loadBG(0,"BG79E1",at=[Transform(yalign=1.0)])





    play bgm "BGM26"
    "然后。"
    "总之先回去工作吧。"

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CMA04"),"True","lh/MAY_CMA04a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "TEN02A_MAY0009"
    $ current_voice = "voice/TEN02A_MAY0009.ogg"
    "真由理" "「那个」"
    $ stopvoc("TEN")
    play TEN "TEN02A_TEN0059"
    $ current_voice = "voice/TEN02A_TEN0059.ogg"
    "天王寺" "「嗯？怎么了吗，小姐？」"
    "这个小姑娘是和冈部一起从春天开始就在２楼的孩子。"
    "和绹打成一片，所以不能怠慢了她。"
    $ stopvoc("MAY")
    play MAY "TEN02A_MAY0010"
    $ current_voice = "voice/TEN02A_MAY0010.ogg"
    "真由理" "「真由喜有一个不情之请。」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CMA03"),"True","lh/MAY_CMA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "TEN02A_MAY0011"
    $ current_voice = "voice/TEN02A_MAY0011.ogg"
    "真由理" "「那个，如果可能的话希望能保持Ｌａｂ现在的样子呐」"
    $ stopvoc("TEN")
    play TEN "TEN02A_TEN0060"
    $ current_voice = "voice/TEN02A_TEN0060.ogg"
    "天王寺" "「这样啊。你是重建的反对派么。对现在的房间有所留恋呢。」"
    $ stopvoc("MAY")
    play MAY "TEN02A_MAY0012"
    $ current_voice = "voice/TEN02A_MAY0012.ogg"
    "真由理" "「……是的」"
    $ stopvoc("TEN")
    play TEN "TEN02A_TEN0061"
    $ current_voice = "voice/TEN02A_TEN0061.ogg"
    "天王寺" "「明白了哦。和我一样对于这房子有所怀恋呢。」"
    "这栋大楼已经住了很久了呢。"
    "虽说已经破旧不堪了，但重建的话果然还是有些舍不得。"
    $ stopvoc("TEN")
    play TEN "TEN02A_TEN0062"
    $ current_voice = "voice/TEN02A_TEN0062.ogg"
    "天王寺" "「你的要求我明白了。我还没有敲定最终方案。我还要想想怎么做才能让绹感觉最好」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CMA02"),"True","lh/MAY_CMA02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "TEN02A_MAY0013"
    $ current_voice = "voice/TEN02A_MAY0013.ogg"
    "真由理" "「好的。拜托了」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    "她低头行礼，然后返回了二楼。"
    "对于这样破旧的大楼还有所留恋的人也是存在的啊，感觉还不错。"

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMC01"),"True","lh/CRS_AMC01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "TEN02A_CRS0011"
    $ current_voice = "voice/TEN02A_CRS0011.ogg"
    "红莉栖" "「那个，店长」"
    $ stopvoc("TEN")
    play TEN "TEN02A_TEN0063"
    $ current_voice = "voice/TEN02A_TEN0063.ogg"
    "天王寺" "「嗯，这次又怎么了吗？你也想保留Ｌａｂ么？」"
    $ stopvoc("CRS")
    play CRS "TEN02A_CRS0012"
    $ current_voice = "voice/TEN02A_CRS0012.ogg"
    "红莉栖" "「不是，和那个无关。如果要翻新的话，楼上也会有出租的房间什么的，刚才是这么说的吧？」"
    $ stopvoc("TEN")
    play TEN "TEN02A_TEN0064"
    $ current_voice = "voice/TEN02A_TEN0064.ogg"
    "天王寺" "「啊啊，确实有这样的方案呢。我也会考虑的。」"
    $ stopvoc("CRS")
    play CRS "TEN02A_CRS0013"
    $ current_voice = "voice/TEN02A_CRS0013.ogg"
    "红莉栖" "「那样的话，如果真的有机会了请务必告诉我一下啊？」"
    $ stopvoc("TEN")
    play TEN "TEN02A_TEN0065"
    $ current_voice = "voice/TEN02A_TEN0065.ogg"
    "天王寺" "「啊？等等你真要租啊？刚才不是说会被当成仓库什么的不要那样么？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMC06"),"True","lh/CRS_AMC06a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "TEN02A_CRS0014"
    $ current_voice = "voice/TEN02A_CRS0014.ogg"
    "红莉栖" "「当然当仓库，但是考虑一下便利性的话确实那样是最好的方案」"
    $ stopvoc("TEN")
    play TEN "TEN02A_TEN0066"
    $ current_voice = "voice/TEN02A_TEN0066.ogg"
    "天王寺" "「租赁的话先不说，如果是分售的话可是永久的哦。你明白你在说什么吗？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMC01"),"True","lh/CRS_AMC01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "TEN02A_CRS0015"
    $ current_voice = "voice/TEN02A_CRS0015.ogg"
    "红莉栖" "「──我明白。」"
    $ stopvoc("TEN")
    play TEN "TEN02A_TEN0067"
    $ current_voice = "voice/TEN02A_TEN0067.ogg"
    "天王寺" "「……喂喂。」"
    "我不知为何注视着她。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMB01"),"True","lh/CRS_AMB01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "TEN02A_CRS0016"
    $ current_voice = "voice/TEN02A_CRS0016.ogg"
    "红莉栖" "「不论怎样，我感觉我会一直参与这个Ｌａｂ下去」"
    $ stopvoc("CRS")
    play CRS "TEN02A_CRS0017"
    $ current_voice = "voice/TEN02A_CRS0017.ogg"
    "红莉栖" "「所以就算分售是永久的也没关系。考虑了很久才这么决定的。」"
    $ stopvoc("TEN")
    play TEN "TEN02A_TEN0068"
    $ current_voice = "voice/TEN02A_TEN0068.ogg"
    "天王寺" "「这样啊。但是不要太意气用事了哦」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMC04"),"True","lh/CRS_AMC04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "TEN02A_CRS0018"
    $ current_voice = "voice/TEN02A_CRS0018.ogg"
    "红莉栖" "「……诶？」"
    "我轻轻地伸了个懒腰。"
    $ stopvoc("TEN")
    play TEN "TEN02A_TEN0069"
    $ current_voice = "voice/TEN02A_TEN0069.ogg"
    "天王寺" "「年轻的时候一时冲动，老了可就没有后悔药了哦」"
    $ stopvoc("TEN")
    play TEN "TEN02A_TEN0070"
    $ current_voice = "voice/TEN02A_TEN0070.ogg"
    "天王寺" "「就算你现在这么想，１年后，２年后会是怎样想的现在不可能知道吧？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMC05"),"True","lh/CRS_AMC05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "TEN02A_CRS0019"
    $ current_voice = "voice/TEN02A_CRS0019.ogg"
    "红莉栖" "「那，那个是……」"
    $ stopvoc("TEN")
    play TEN "TEN02A_TEN0071"
    $ current_voice = "voice/TEN02A_TEN0071.ogg"
    "天王寺" "「等冷静下来以后，好好地考虑一下吧。如果要分售的话，我会第一个告诉你哦。这样可以了吗？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMC03"),"True","lh/CRS_AMC03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "TEN02A_CRS0020"
    $ current_voice = "voice/TEN02A_CRS0020.ogg"
    "红莉栖" "「好的，没问题！　请多关照了」"

    stop bgm 
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    $ targetmailid = cml.setdefault("RM_TEN_SEND_NAE02","")

    $ LR_RM_CHANCE=10
    call CHECK_RM_RECEIVE
    "和刚才的小姑娘不一样，她直直地低下了头，然后快速跑开了。"
    call CHECK_RM_RECEIVE
    "从别处听来的，那孩子好像在美国被认为是极具潜力的学者。"
    call CHECK_RM_RECEIVE
    "这样的人物，要住在这样的大楼里……"
    call CHECK_RM_RECEIVE
    $ stopvoc("TEN")
    play TEN "TEN02A_TEN0072"
    $ current_voice = "voice/TEN02A_TEN0072.ogg"
    "天王寺" "「还真能有这种事啊」"
    call CHECK_RM_RECEIVE
    "看来，人的将来不能用身份来断定啊。"
    call CHECK_RM_RECEIVE
    "在哪里怎样地生活是由“味道”决定的。"
    call CHECK_RM_RECEIVE
    "不管找什么理由，最后还是会选择适合自己的地方。"
    call CHECK_RM_RECEIVE
    "那样安顿下来的人，我已经见了不少了。"
    call CHECK_RM_RECEIVE
    $ stopvoc("TEN")
    play TEN "TEN02A_TEN0073"
    $ current_voice = "voice/TEN02A_TEN0073.ogg"
    "天王寺" "「嘛，至少也是听了我一句嘛」"
    call CHECK_RM_RECEIVE
    "就算那样那姑娘也会一直留在秋叶原吧。"

    call CHECK_RM_RECEIVE





    "因为喜欢这样的“气味”。"

    $ gd["RCVmailData"][gc["ScriptMacros"]["RM_TEN_RECV_NAE02_01"]]["late"]=True
    $ lml.append(gc["ScriptMacros"]["RM_TEN_RECV_NAE02_01"])


    hide screen phoneSD1
    window hide

    stop bgm 
    window hide
    hide screen phonebtn
    scene expression Solid("000000")  with fade





    return






















    return

































    return




















    return

































    return























    return


















    return

















    return























    return

































    return

















    return
























    return














    return








    return
