label SGFD2_RUK04B:
    hide screen phonebtn
    scene expression Solid("000000")  with fade

    window hide


    $ loadBG(0,"BG16N1")

    play bgm "FD2BGM01"

    $ date="8/18"
    $ day = "WED"
    python:
        rml = []
        cml = {}
        lml = []
        sml = []
    show screen phonebtn
    show screen phoneSD1

    "我回到了１８号的晚上，走向了未来道具研究所。"
    "这个点的话，那个人应该还在那里。"
    window hide


    $ loadBG(2,"BG05N1")



    "我喘着气跑到了建大楼前面的时候，在楼梯的暗处有人刚好下来了。"
    $ stopvoc("RUK")
    play RUK "RUK04B_RUK0000"
    $ current_voice = "voice/RUK04B_RUK0000.ogg"
    "琉华" "「牧濑！」"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_HSC04"),"True","lh/CRS_HSC04a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "RUK04B_CRS0000"
    $ current_voice = "voice/RUK04B_CRS0000.ogg"
    "红莉栖" "「诶？」"
    $ stopvoc("RUK")
    play RUK "RUK04B_RUK0001"
    $ current_voice = "voice/RUK04B_RUK0001.ogg"
    "琉华" "「拜，拜托了，那个……牧濑！请帮帮我吧」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_HSC06"),"True","lh/CRS_HSC06a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "RUK04B_CRS0001"
    $ current_voice = "voice/RUK04B_CRS0001.ogg"
    "红莉栖" "「漆原……」"
    $ stopvoc("RUK")
    play RUK "RUK04B_RUK0002"
    $ current_voice = "voice/RUK04B_RUK0002.ogg"
    "琉华" "「拜托了，果然这样下去是不行的。所以请助我一臂之力……！」"
    $ stopvoc("CRS")
    play CRS "RUK04B_CRS0002"
    $ current_voice = "voice/RUK04B_CRS0002.ogg"
    "红莉栖" "「等，等一下漆原！　总之请冷静点好吗？！」"
    $ stopvoc("RUK")
    play RUK "RUK04B_RUK0003"
    $ current_voice = "voice/RUK04B_RUK0003.ogg"
    "琉华" "「啊……不好意思。我太心急了，一不小心就……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_HSA01"),"True","lh/CRS_HSA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "RUK04B_CRS0003"
    $ current_voice = "voice/RUK04B_CRS0003.ogg"
    "红莉栖" "「不，没关系哦。能告诉我为什么这么着急吗？是发生了什么吗？」"
    $ stopvoc("RUK")
    play RUK "RUK04B_RUK0004"
    $ current_voice = "voice/RUK04B_RUK0004.ogg"
    "琉华" "「那是……」"

    "我把到现在为止的事情都告诉了牧濑。"
    "在这之前，我都没有怎么跟牧濑说过话。但是这几天跟牧濑说话的次数增加了不少。 "
    "但是这样想的人也只有我吧。"
    "对于现在的牧濑来说，我之前并没有拜托她操作过时间机器。"
    "这是因为从现在的时间里，１５号之后发生的事都已经消失了。"
    "所以，就算我觉得和她说过很多次话了，也只是我的一厢情愿。"
    "那是——十分虚无的事。"
    "冈部师傅到现在这个地步了，应该也和我有着一样的想法吧。"
    "然后从现在开始也会——"
    "我会和冈部师傅一样一直重复下去。"
    "想到这些，感觉心很痛。"
    "但是，即使如此。"


    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_HSB06"),"True","lh/CRS_HSB06a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "RUK04B_CRS0004"
    $ current_voice = "voice/RUK04B_CRS0004.ogg"
    "红莉栖" "「真的好吗？」"
    $ stopvoc("RUK")
    play RUK "RUK04B_RUK0005"
    $ current_voice = "voice/RUK04B_RUK0005.ogg"
    "琉华" "「恩，已经决定了」"
    "就算如此，我也还是会选择这条路吧。"
    $ stopvoc("CRS")
    play CRS "RUK04B_CRS0005"
    $ current_voice = "voice/RUK04B_CRS0005.ogg"
    "红莉栖" "「是吗，既然你已经说到这个份上了，肯定是经过深思熟虑的吧。」"
    "就算，被冈部师傅所讨厌也无所谓。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_HSA01"),"True","lh/CRS_HSA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "RUK04B_CRS0006"
    $ current_voice = "voice/RUK04B_CRS0006.ogg"
    "红莉栖" "「明白了。那就去Ｌａｂ吧」"
    $ stopvoc("RUK")
    play RUK "RUK04B_RUK0006"
    $ current_voice = "voice/RUK04B_RUK0006.ogg"
    "琉华" "「好的」"
    window hide



    $ loadBG(0,"BG02N2")


    hide screen phoneSD1
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_RUK003B"]]["Check"]=True


    $ loadBG(2,"EV_RUK003B")



    hide screen phonebtn

    "冈部师傅果然还在房间的角落里面伤心着。"
    "大概连我们进入了房间也没察觉到。"
    "但是，现在这个也是值得庆幸的事情啊。"
    "知道我们要做什么的话，可能就会阻止我们了吧。"
    window hide



    $ loadBG(2,"BG03A4")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_HSA01"),"True","lh/CRS_HSA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    show screen phonebtn
    show screen phoneSD1
    $ stopvoc("CRS")
    play CRS "RUK04B_CRS0007"
    $ current_voice = "voice/RUK04B_CRS0007.ogg"
    "红莉栖" "「漆原」"
    "牧濑一边熟练的操作着机器，一边拿出一张备忘纸。"
    $ stopvoc("CRS")
    play CRS "RUK04B_CRS0008"
    $ current_voice = "voice/RUK04B_CRS0008.ogg"
    "红莉栖" "「刚刚谷歌了一下。大概是２０年前六项的ＢＰ机使用的数字到文字的变换表哦」"
    "她接下之后我递过的纸，然后快速地将那个表格写到了上面。"
    $ stopvoc("CRS")
    play CRS "RUK04B_CRS0009"
    $ current_voice = "voice/RUK04B_CRS0009.ogg"
    "红莉栖" "「这样明白了吗？」"
    $ stopvoc("RUK")
    play RUK "RUK04B_RUK0007"
    $ current_voice = "voice/RUK04B_RUK0007.ogg"
    "琉华" "「恩，没关系」"
    $ stopvoc("CRS")
    play CRS "RUK04B_CRS0010"
    $ current_voice = "voice/RUK04B_CRS0010.ogg"
    "红莉栖" "「那么，就拿另外一张纸根据这张表将文字转成数字写下来。」"
    $ stopvoc("CRS")
    play CRS "RUK04B_CRS0011"
    $ current_voice = "voice/RUK04B_CRS0011.ogg"
    "红莉栖" "「规则要求最初的『＊２＊２』是必须写的，剩下的请用１６个片假名完成」"
    $ stopvoc("CRS")
    play CRS "RUK04B_CRS0012"
    $ current_voice = "voice/RUK04B_CRS0012.ogg"
    "红莉栖" "「写完之后直接往电脑里面输入就能送到过去了。」"
    $ stopvoc("RUK")
    play RUK "RUK04B_RUK0008"
    $ current_voice = "voice/RUK04B_RUK0008.ogg"
    "琉华" "「好的」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    "冈部师傅为了能够让我变成女孩子，好像发送了让我的妈妈吃很多蔬菜的邮件。"
    "既然如此，现在我只要把与此相反的事情转换成数字发送过去就好了。"
    $ stopvoc("RUK")
    play RUK "RUK04B_RUK0009"
    $ current_voice = "voice/RUK04B_RUK0009.ogg"
    "琉华" "「完成了」"
    "收信地址是我母亲的ＢＰ机号。那个已经告诉牧濑了。"
    "牧濑将我写好的数字快速地输进了电脑。"
    "完成之后，她稍稍叹了口气，朝着我的方向转过来。"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_HSA01"),"True","lh/CRS_HSA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "RUK04B_CRS0013"
    $ current_voice = "voice/RUK04B_CRS0013.ogg"
    "红莉栖" "「电话微波炉启动之后，就按下回车键，那样就会将输入的数字发送到过去」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_HSC06"),"True","lh/CRS_HSC06a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "RUK04B_CRS0014"
    $ current_voice = "voice/RUK04B_CRS0014.ogg"
    "红莉栖" "「…………真的……没关系吗？」"
    $ stopvoc("RUK")
    play RUK "RUK04B_RUK0010"
    $ current_voice = "voice/RUK04B_RUK0010.ogg"
    "琉华" "「拜托了」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    stop bgm 
    "我点了的头后，牧濑就启动了机器，站了起来。"
    window hide
    show houden 

    play se "SGSE035L" loop

    "一时间房屋内电火花四处流走。"
    $ stopvoc("CRS")
    play CRS "RUK04B_CRS0015"
    $ current_voice = "voice/RUK04B_CRS0015.ogg"
    "红莉栖" "「回车键……你来按吧。」"
    $ stopvoc("RUK")
    play RUK "RUK04B_RUK0011"
    $ current_voice = "voice/RUK04B_RUK0011.ogg"
    "琉华" "「……好的」"
    "微微地吐了口气，我站在了键盘面前。"

    "说真的话，我还想以女孩子的姿态再告诉冈部师傅一次。"
    "喜欢他。"
    "想以女孩子的姿态说出来。"
    "还有告别。"
    "但是，因为这个已经做不到了"
    "所以，永别了。"
    "永别了，我的……"

    $ stopvoc("OKA")
    play OKA "RUK04B_OKA0000"
    $ current_voice = "voice/RUK04B_OKA0000.ogg"
    "伦太郎" "「等等，琉华子！」"
    $ stopvoc("RUK")
    play RUK "RUK04B_RUK0012"
    $ current_voice = "voice/RUK04B_RUK0012.ogg"
    "琉华" "「诶？」"
    window hide
    hide houden 

    stop se

    stop bgm 
    play se "SGSE020"




    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA06"),"True","lh/OKA_ASA06a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "RUK04B_OKA0001"
    $ current_voice = "voice/RUK04B_OKA0001.ogg"
    "伦太郎" "「琉华子……」"
    $ stopvoc("RUK")
    play RUK "RUK04B_RUK0013"
    $ current_voice = "voice/RUK04B_RUK0013.ogg"
    "琉华" "「冈部……师傅？」"
    "我抬起头，刚刚在角落里面伤心欲绝的冈部师傅站了起来。"
    $ stopvoc("CRS")
    play CRS "RUK04B_CRS0016"
    $ current_voice = "voice/RUK04B_CRS0016.ogg"
    "红莉栖" "「冈部师傅……」"
    $ stopvoc("RUK")
    play RUK "RUK04B_RUK0014"
    $ current_voice = "voice/RUK04B_RUK0014.ogg"
    "琉华" "「冈部师傅，怎么了？」"
    $ stopvoc("OKA")
    play OKA "RUK04B_OKA0002"
    $ current_voice = "voice/RUK04B_OKA0002.ogg"
    "伦太郎" "「终于追上你了……」"
    $ stopvoc("RUK")
    play RUK "RUK04B_RUK0015"
    $ current_voice = "voice/RUK04B_RUK0015.ogg"
    "琉华" "「追上了……什么……啊！」"
    $ stopvoc("RUK")
    play RUK "RUK04B_RUK0016"
    $ current_voice = "voice/RUK04B_RUK0016.ogg"
    "琉华" "「难道说，冈部师傅……进行了时间跳跃」"
    play bgm "FD2BGM06"
    "冈部师傅点了点头。"
    $ stopvoc("OKA")
    play OKA "RUK04B_OKA0003"
    $ current_voice = "voice/RUK04B_OKA0003.ogg"
    "伦太郎" "「你之前说过吧。已经习惯了时间跳跃了」"
    $ stopvoc("OKA")
    play OKA "RUK04B_OKA0004"
    $ current_voice = "voice/RUK04B_OKA0004.ogg"
    "伦太郎" "「按照之前你说的，你应该只用过一次机器。但是你却说出了这种话……我觉得有些蹊跷，就追了过来。」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_AMA06"),"True","lh/OKA_AMA06a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    "冈部师傅向我们走来。"
    "接着，看见了我好像要按下发射按钮的手，露出了惊讶的表情。"
    $ stopvoc("OKA")
    play OKA "RUK04B_OKA0005"
    $ current_voice = "voice/RUK04B_OKA0005.ogg"
    "伦太郎" "「琉华子。你，难道 ……」"
    $ stopvoc("RUK")
    play RUK "RUK04B_RUK0017"
    $ current_voice = "voice/RUK04B_RUK0017.ogg"
    "琉华" "「被发现了呢」"
    $ stopvoc("OKA")
    play OKA "RUK04B_OKA0006"
    $ current_voice = "voice/RUK04B_OKA0006.ogg"
    "伦太郎" "「那，果然……」"
    $ stopvoc("RUK")
    play RUK "RUK04B_RUK0018"
    $ current_voice = "voice/RUK04B_RUK0018.ogg"
    "琉华" "「……之前对您撒了谎，十分抱歉。其实我还是去了夏Ｃｏｍｉ」"
    $ stopvoc("RUK")
    play RUK "RUK04B_RUK0019"
    $ current_voice = "voice/RUK04B_RUK0019.ogg"
    "琉华" "「而且还和真由理酱拍了照片。真由理酱她……非常的开心，一直在笑着……」"
    $ stopvoc("OKA")
    play OKA "RUK04B_OKA0007"
    $ current_voice = "voice/RUK04B_OKA0007.ogg"
    "伦太郎" "「你是打算……将过去复原吗？」"
    $ stopvoc("RUK")
    play RUK "RUK04B_RUK0020"
    $ current_voice = "voice/RUK04B_RUK0020.ogg"
    "琉华" "「是的」"
    $ stopvoc("OKA")
    play OKA "RUK04B_OKA0008"
    $ current_voice = "voice/RUK04B_OKA0008.ogg"
    "伦太郎" "「为什么！？　你是知道的吧？　复原过去的话，你就会变成男孩子哦！？」"
    $ stopvoc("CRS")
    play CRS "RUK04B_CRS0017"
    $ current_voice = "voice/RUK04B_CRS0017.ogg"
    "红莉栖" "「冈部！」"
    "牧濑仿佛是为了喝住上前逼问我的冈部师傅而开口了。"
    "但是冈部师傅毫不在意地继续说下去。"
    $ stopvoc("OKA")
    play OKA "RUK04B_OKA0009"
    $ current_voice = "voice/RUK04B_OKA0009.ogg"
    "伦太郎" "「那么你作为女孩子度过的这１７年也会消失的哦！」"
    $ stopvoc("OKA")
    play OKA "RUK04B_OKA0010"
    $ current_voice = "voice/RUK04B_OKA0010.ogg"
    "伦太郎" "「就算这样也可以吗！？」"
    "被说了这样的话，如果是过去的我的话一定是不敢正面回答的。"
    "因为会不知所措地无言以对吧。"
    "但只有现在——只有现在我必须说服他。"
    "将这些话语。"
    "实现。"
    "全部驳回，然后必须立刻让他接受。"
    $ stopvoc("RUK")
    play RUK "RUK04B_RUK0021"
    $ current_voice = "voice/RUK04B_RUK0021.ogg"
    "琉华" "「就算那样也，没事的」"
    "不这样做的话，就无法传达到了。"
    $ stopvoc("RUK")
    play RUK "RUK04B_RUK0022"
    $ current_voice = "voice/RUK04B_RUK0022.ogg"
    "琉华" "「不对，必须那么做。因为，这些本来就是因为我的任性引起的」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_AMD01"),"True","lh/OKA_AMD01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "RUK04B_OKA0011"
    $ current_voice = "voice/RUK04B_OKA0011.ogg"
    "伦太郎" "「但是，最根本还是我的……」"
    $ stopvoc("RUK")
    play RUK "RUK04B_RUK0023"
    $ current_voice = "voice/RUK04B_RUK0023.ogg"
    "琉华" "「那个呢，冈部师傅。我是这么想的。」"
    $ stopvoc("RUK")
    play RUK "RUK04B_RUK0024"
    $ current_voice = "voice/RUK04B_RUK0024.ogg"
    "琉华" "「一直，在做着这样的梦」"
    $ stopvoc("RUK")
    play RUK "RUK04B_RUK0025"
    $ current_voice = "voice/RUK04B_RUK0025.ogg"
    "琉华" "「做着这个长达１７年的，长长的梦──」"
    "这是一种朦胧的心情。"
    "还是男孩子的时候的心情。"
    "是原本的我的——想法。"
    $ stopvoc("RUK")
    play RUK "RUK04B_RUK0026"
    $ current_voice = "voice/RUK04B_RUK0026.ogg"
    "琉华" "「想变成女孩子什么的。本来的话，那种梦想是不应该实现的」"
    $ stopvoc("RUK")
    play RUK "RUK04B_RUK0027"
    $ current_voice = "voice/RUK04B_RUK0027.ogg"
    "琉华" "「但是，我实现了那个梦想。１７年间——一直做着这样的梦」"
    $ stopvoc("RUK")
    play RUK "RUK04B_RUK0028"
    $ current_voice = "voice/RUK04B_RUK0028.ogg"
    "琉华" "「这样的梦想是冈部师傅认真地为我实现的」"
    $ stopvoc("RUK")
    play RUK "RUK04B_RUK0029"
    $ current_voice = "voice/RUK04B_RUK0029.ogg"
    "琉华" "「所以，这样就足够了」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_AMD01"),"True","lh/OKA_AMD01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "RUK04B_OKA0012"
    $ current_voice = "voice/RUK04B_OKA0012.ogg"
    "伦太郎" "「琉华子……」"
    $ stopvoc("RUK")
    play RUK "RUK04B_RUK0030"
    $ current_voice = "voice/RUK04B_RUK0030.ogg"
    "琉华" "「对不起，冈部师傅。大概我现在要说的这些话对于你来说是非常残酷的事情」"
    $ stopvoc("RUK")
    play RUK "RUK04B_RUK0031"
    $ current_voice = "voice/RUK04B_RUK0031.ogg"
    "琉华" "「那些话……我知道非常让人难受，但是我还是想要说出来」"
    $ stopvoc("RUK")
    play RUK "RUK04B_RUK0032"
    $ current_voice = "voice/RUK04B_RUK0032.ogg"
    "琉华" "「冈部师傅。请去拯救真由理酱吧！」"
    $ stopvoc("RUK")
    play RUK "RUK04B_RUK0033"
    $ current_voice = "voice/RUK04B_RUK0033.ogg"
    "琉华" "「因为如果不这样做的话，冈部师傅就可能不会再笑了。」"
    $ stopvoc("RUK")
    play RUK "RUK04B_RUK0034"
    $ current_voice = "voice/RUK04B_RUK0034.ogg"
    "琉华" "「我也……不会再笑了。」"
    $ stopvoc("CRS")
    play CRS "RUK04B_CRS0018"
    $ current_voice = "voice/RUK04B_CRS0018.ogg"
    "红莉栖" "「漆原……」"
    $ stopvoc("RUK")
    play RUK "RUK04B_RUK0035"
    $ current_voice = "voice/RUK04B_RUK0035.ogg"
    "琉华" "「冈部师傅说过呢，已经不想牺牲任何人的梦想了。」"
    $ stopvoc("RUK")
    play RUK "RUK04B_RUK0036"
    $ current_voice = "voice/RUK04B_RUK0036.ogg"
    "琉华" "「但是，我必须牺牲我自己的这一份。」"
    $ stopvoc("RUK")
    play RUK "RUK04B_RUK0037"
    $ current_voice = "voice/RUK04B_RUK0037.ogg"
    "琉华" "「因为我已经从冈部师傅那里得到了很重要的东西」"
    "我将冈部师傅的手放在自己胸口。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_AMA04"),"True","lh/OKA_AMA04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "RUK04B_OKA0013"
    $ current_voice = "voice/RUK04B_OKA0013.ogg"
    "伦太郎" "「琉华……子……」"
    "冈部师傅放在我胸口的手上传来了他的体温。"
    $ stopvoc("RUK")
    play RUK "RUK04B_RUK0038"
    $ current_voice = "voice/RUK04B_RUK0038.ogg"
    "琉华" "「冈部师傅，虽然我已经无法继续思念着冈部师傅了——但是这样也足够了」"
    $ stopvoc("RUK")
    play RUK "RUK04B_RUK0039"
    $ current_voice = "voice/RUK04B_RUK0039.ogg"
    "琉华" "「所以，这次就轮到把真由理的梦想……大家都能笑着，把这个当做梦想的真由理酱的梦想，好好地实现一下吧」"
    $ stopvoc("RUK")
    play RUK "RUK04B_RUK0040"
    $ current_voice = "voice/RUK04B_RUK0040.ogg"
    "琉华" "「把真由理的笑容——她的未来给取回来吧。」"
    $ stopvoc("RUK")
    play RUK "RUK04B_RUK0041"
    $ current_voice = "voice/RUK04B_RUK0041.ogg"
    "琉华" "「这一定是我们大家真实的愿望。」"
    "因为这是冈部师傅最真实的愿望。"
    "所以我要更加地高兴一些。"
    $ stopvoc("RUK")
    play RUK "RUK04B_RUK0042"
    $ current_voice = "voice/RUK04B_RUK0042.ogg"
    "琉华" "「但是……如果变得快要崩溃的话请务必告诉我啊！」"
    "我没事的，这么说的话。"
    $ stopvoc("RUK")
    play RUK "RUK04B_RUK0043"
    $ current_voice = "voice/RUK04B_RUK0043.ogg"
    "琉华" "「如果有难受的事的话大可直说。」"
    $ stopvoc("RUK")
    play RUK "RUK04B_RUK0044"
    $ current_voice = "voice/RUK04B_RUK0044.ogg"
    "琉华" "「虽然我没有办法体会到冈部师傅的真正的难过……但是，我也会一起想办法的，我也会一起哭的！」"
    "我现在能做到只有这些了。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_AMA01"),"True","lh/OKA_AMA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "RUK04B_OKA0014"
    $ current_voice = "voice/RUK04B_OKA0014.ogg"
    "伦太郎" "「…………明白了」"
    $ stopvoc("RUK")
    play RUK "RUK04B_RUK0045"
    $ current_voice = "voice/RUK04B_RUK0045.ogg"
    "琉华" "「…………」"
    $ stopvoc("OKA")
    play OKA "RUK04B_OKA0015"
    $ current_voice = "voice/RUK04B_OKA0015.ogg"
    "伦太郎" "「明白了哦。琉华子。那个时候，我会来拜托你的」"
    $ stopvoc("RUK")
    play RUK "RUK04B_RUK0046"
    $ current_voice = "voice/RUK04B_RUK0046.ogg"
    "琉华" "「冈部师傅……」"
    $ stopvoc("OKA")
    play OKA "RUK04B_OKA0016"
    $ current_voice = "voice/RUK04B_OKA0016.ogg"
    "伦太郎" "「好像感觉我搞错了什么……」"
    $ stopvoc("OKA")
    play OKA "RUK04B_OKA0017"
    $ current_voice = "voice/RUK04B_OKA0017.ogg"
    "伦太郎" "「是这样的吧。刚才忘记了哦。我们Ｌａｂｍｅｍ的梦想一定只有一个。而且目的也……」"
    $ stopvoc("CRS")
    play CRS "RUK04B_CRS0019"
    $ current_voice = "voice/RUK04B_CRS0019.ogg"
    "红莉栖" "「冈部师傅……」"
    $ stopvoc("OKA")
    play OKA "RUK04B_OKA0018"
    $ current_voice = "voice/RUK04B_OKA0018.ogg"
    "伦太郎" "「没想到，琉华子，竟然让你来告诉我这些……」"
    $ stopvoc("RUK")
    play RUK "RUK04B_RUK0047"
    $ current_voice = "voice/RUK04B_RUK0047.ogg"
    "琉华" "「冈部师傅……」"
    window hide
    stop bgm 
    show houden 

    play se "SGSE035L" loop

    "机器上面的数字在一个个地减少。"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    "我放开了冈部师傅的手，再一次走到键盘前面。"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_HSA01"),"True","lh/CRS_HSA01a~ipad.png") at left as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA01"),"True","lh/OKA_ASA01a~ipad.png") at right as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("RUK")
    play RUK "RUK04B_RUK0048"
    $ current_voice = "voice/RUK04B_RUK0048.ogg"
    "琉华" "「那就这样，冈部师傅。我就去了」"
    $ stopvoc("OKA")
    play OKA "RUK04B_OKA0019"
    $ current_voice = "voice/RUK04B_OKA0019.ogg"
    "伦太郎" "「啊啊……」"
    $ stopvoc("RUK")
    play RUK "RUK04B_RUK0049"
    $ current_voice = "voice/RUK04B_RUK0049.ogg"
    "琉华" "「牧濑也是。实在是十分感谢。下次能多聊一些的话我也会很高兴的」"
    $ stopvoc("CRS")
    play CRS "RUK04B_CRS0020"
    $ current_voice = "voice/RUK04B_CRS0020.ogg"
    "红莉栖" "「恩，是啊……」"
    "在最后的时候。"
    $ stopvoc("RUK")
    play RUK "RUK04B_RUK0050"
    $ current_voice = "voice/RUK04B_RUK0050.ogg"
    "琉华" "「冈部师傅」"
    "在最后的时候，再一次将我的心意。"
    $ stopvoc("RUK")
    play RUK "RUK04B_RUK0051"
    $ current_voice = "voice/RUK04B_RUK0051.ogg"
    "琉华" "「谢谢。我一直喜欢你……」"
    "因为最喜欢你。"
    $ stopvoc("RUK")
    play RUK "RUK04B_RUK0052"
    $ current_voice = "voice/RUK04B_RUK0052.ogg"
    "琉华" "「Ｅｌ・Ｐｓｙ・Ｃｏｎｇｒｏｏ……」"
    "所以。"
    $ stopvoc("OKA")
    play OKA "RUK04B_OKA0020"
    $ current_voice = "voice/RUK04B_OKA0020.ogg"
    "伦太郎" "「琉华子……」"

    "所以，永别了。"
    "永别了，身为女孩子的我。"
    "永别了。"
    "我的。"
    "重要的人。"
    "永别了。"
    "永别了。"

    hide screen phoneSD1
    hide screen phonebtn
    window hide


    play se "SGSE143"


    stop se



    hide houden 
    $ loadBG(0,"BG_BLACK")



    $ stopvoc("OKA")
    play OKA "RUK04B_OKA0021"
    $ current_voice = "voice/RUK04B_OKA0021.ogg"
    "伦太郎" "「琉华──！！」"
    "永……别了。"

    hide screen phoneSD1
    window hide





    hide screen phonebtn
    scene expression Solid("000000")  with fade
    show screen invisible
    $ renpy.movie_cutscene("video/imv03.avi")
    hide screen invisible
    return
