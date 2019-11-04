label SGFD2_KYO04B:
    hide screen phonebtn
    scene expression Solid("000000")  with fade

    window hide


    $ loadBG(0,"BG02E2")


    $ date="8/13"
    show screen phonebtn
    show screen phoneSD1
    play se "SGSE321"


    play se "SGSE322"


    "突然，从门外传来一阵厚重的低音。"
    "是车门关闭的声音……"
    "有些不好的预感……"
    window hide


    $ loadBG(2,"BG01E")



    "我赶紧跑到窗户边上，偷偷向下看去。"
    hide screen phoneSD1
    window hide
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_KYO002B"]]["Check"]=True


    $ loadBG(2,"EV_KYO002B")








    hide screen phonebtn
    "在显像管工房前面听着一台车。"
    "黑色的ＳＵＶ——窗户贴着黑色的膜。"
    "不管怎么看都不像是正经的车子。"
    "但是，在一旁有着更不寻常的存在。"
    "在车的周围……"
    window hide







    play bgm "BGM09"
    "站着一群披着黑色斗篷的男人。"
    $ stopvoc("OKA")
    play OKA "KYO04B_OKA0000"
    $ current_voice = "voice/KYO04B_OKA0000.ogg"
    "伦太郎" "「喂喂，给我等下……。谁啊，那群人……」"
    "男子都用着黑色斗篷的帽子遮住了脸，脸上还带着可怕的面具。"
    "不对，不是可怕的面具。"
    "那种打扮……光是站着就很有诡异的感觉了。"
    "难道说……是Ｒｏｕｎｄｅｒ？"
    "虽然一瞬间有过这个想法，但是那样的念头很快就消失了。"
    "那群家伙不是Ｒｏｕｎｄｅｒ。"
    "Ｒｏｕｎｄｅｒ的服装不会这么显眼，而且和在别的世界线的袭击时间也不同。"
    "那……是来讨债的？"
    "那个可能性也很快被我否决了。"
    "根据借用书来看，确实还钱的期限是明年啊。"
    "而且明明昨天才借了钱，今天怎么说都不会上门来讨啊。"
    "那样的话……这群家伙到底是——"
    "这时候终于注意到了。"
    "回想起来，在真由理手机里的那封Ｄｍａｉｌ里……"
    hide screen phoneSD1
    window hide


    $ loadBG(0,"PBG17C")

    hide screen phonebtn
    "『和黑万十战斗』"
    "那不是『黑馒头』而是『黑斗篷』"
    window hide


    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_KYO002B"]]["Check"]=True
    $ loadBG(0,"EV_KYO002B")

    hide screen phonebtn
    "说起来，他们……"
    $ stopvoc("MAY")
    play MAY "KYO04B_MAY0000"
    $ current_voice = "voice/KYO04B_MAY0000.ogg"
    "真由理" "「呐呐，怎么了呀，冈伦」"
    window hide



    $ loadBG(2,"BG02E2")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA02"),"True","lh/MAY_CSA02a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    show screen phonebtn
    show screen phoneSD1
    "回头看去，是朝着这里走过来的真由理。"
    $ stopvoc("OKA")
    play OKA "KYO04B_OKA0001"
    $ current_voice = "voice/KYO04B_OKA0001.ogg"
    "伦太郎" "「笨蛋！　快蹲下！」"
    "我用力地将真由理的头按了下去。"
    hide screen phoneSD1
    window hide
    play se "SGSE056"



    $ loadBG(2,"BG_BLACK")





    hide screen phonebtn
    $ stopvoc("MAY")
    play MAY "KYO04B_MAY0001"
    $ current_voice = "voice/KYO04B_MAY0001.ogg"
    "真由理" "「诶？　什么？」"
    $ stopvoc("OKA")
    play OKA "KYO04B_OKA0002"
    $ current_voice = "voice/KYO04B_OKA0002.ogg"
    "伦太郎" "「显像管工房前面有奇怪的家伙」"
    $ stopvoc("MAY")
    play MAY "KYO04B_MAY0002"
    $ current_voice = "voice/KYO04B_MAY0002.ogg"
    "真由理" "「“机关”？」"
    $ stopvoc("OKA")
    play OKA "KYO04B_OKA0003"
    $ current_voice = "voice/KYO04B_OKA0003.ogg"
    "伦太郎" "「可，可能吧，但应该不是」"
    $ stopvoc("MAY")
    play MAY "KYO04B_MAY0003"
    $ current_voice = "voice/KYO04B_MAY0003.ogg"
    "真由理" "「诶，真由喜也想看看啊」"
    $ stopvoc("OKA")
    play OKA "KYO04B_OKA0004"
    $ current_voice = "voice/KYO04B_OKA0004.ogg"
    "伦太郎" "「不行！」"
    $ stopvoc("MAY")
    play MAY "KYO04B_MAY0004"
    $ current_voice = "voice/KYO04B_MAY0004.ogg"
    "真由理" "「为什么？」"
    "到这个点也瞒不下去了。"
    "我爽快地告诉了她。"
    $ stopvoc("OKA")
    play OKA "KYO04B_OKA0005"
    $ current_voice = "voice/KYO04B_OKA0005.ogg"
    "伦太郎" "「真由理，听好了」"
    $ stopvoc("OKA")
    play OKA "KYO04B_OKA0006"
    $ current_voice = "voice/KYO04B_OKA0006.ogg"
    "伦太郎" "「你在别的世界线被诱拐了。在这条世界线上被可能被诱拐。也就是说你被谁盯上了啦……」"
    "这么说了以后真由理歪着脑袋。"
    $ stopvoc("MAY")
    play MAY "KYO04B_MAY0005"
    $ current_voice = "voice/KYO04B_MAY0005.ogg"
    "真由理" "「咦？」"
    "说了一句。"
    $ stopvoc("OKA")
    play OKA "KYO04B_OKA0007"
    $ current_voice = "voice/KYO04B_OKA0007.ogg"
    "伦太郎" "「总而言之，外面那群家伙就是诱拐犯也说不定。如果是那样的话，你在这里说不定就暴露了。所以说──」"
    $ stopvoc("MAY")
    play MAY "KYO04B_MAY0006"
    $ current_voice = "voice/KYO04B_MAY0006.ogg"
    "真由理" "「恩，虽然不太明白，但知道了啊。那样的话真由喜就去开发室里面了。」"
    "真由理那么说着，在地板上悄悄地挪进了开发室里。"
    $ stopvoc("OKA")
    play OKA "KYO04B_OKA0008"
    $ current_voice = "voice/KYO04B_OKA0008.ogg"
    "伦太郎" "「危机感……为零啊……」"
    "我这么说着，再次向窗户外面投去了目光。"
    window hide

    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_KYO002B"]]["Check"]=True
    $ loadBG(0,"EV_KYO002B")

    "虽然刚才差点陷入真由理的安稳的节奏中，但是看到的情况已经是极度危险的紧急事态了。"
    "在显像管工房前面站着５个来路不明的人，看起来是要阻止一切出去的手段。"
    window hide


    $ loadBG(2,"BG01E")



    show screen phonebtn
    show screen phoneSD1
    "因为这幢大桧山大楼的左右两侧和后面都是相同的大楼，没有丝毫的间隔，所以并不存在从其他什么暗道逃脱的办法。"
    "总之考虑了一下从厕所的窗户逃到另外一栋大楼里的方法，"
    window hide


    $ loadBG(2,"BG_BLACK")



    hide screen phonebtn
    "但是确认之后，发现另一侧的大楼那边好像放了一个巨大的柜子，所以进不去。"
    window hide
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_KYO002B"]]["Check"]=True


    $ loadBG(2,"EV_KYO002B")



    hide screen phonebtn
    "为了从这群人手里逃走，只能带着真由理跑下楼梯并突破他们的包围网了。"
    "但是，我觉得我做不到。"
    "我一个人突破就够困难了，不用说还要带着真由理强行突破，这简直就是无谋的程度了。"
    "那样的话该怎么办……？该怎么办才好……"
    window hide


    $ loadBG(2,"BG01E")



    show screen phonebtn
    show screen phoneSD1
    "玄关的门锁得紧紧的。"
    "但我知道那扇门属于一踹就破的类型。"
    "如果让那５个人进来的话就完蛋了。"
    "就算是我这样掌握着清心斩魔流剑法的人，如果没有剑的话也只是普通的人类而已。"
    "要从５个人手中保护下真由理什么的，果然还是太勉强了……"
    "这么想着的时候——"





    "手机响了。"



    window hide
    hide screen phonebtn
    hide screen phonebtn2
    show screen phone(interact=False)

    "我像是抓住了救命稻草一样将手机取了出来。"
    "画面上显示的是『公共电话』。"
    "也就是说，应该不是外面那群家伙打过来的。"
    "那是谁呢……？"
    "不对，这个时候谁都行了！"
    "如果能将我从这个绝境中救出来的话谁都好了……！"
    "带着这个愿望，我按下了手机的通话键。"






    $ stopvoc("CRS")
    play CRS "KYO04B_CRS0000"
    $ current_voice = "voice/KYO04B_CRS0000.ogg"
    "红莉栖？" "「冈部────！！！」"

    "传到耳朵里的是一阵地动山摇的喊声……"
    "但是我对于这个声音有印象。"
    $ stopvoc("OKA")
    play OKA "KYO04B_OKA0009"
    $ current_voice = "voice/KYO04B_OKA0009.ogg"
    "伦太郎" "「山村先生？　中学时候当我的班主任的那位……」"

    $ stopvoc("CRS")
    play CRS "KYO04B_CRS0001"
    $ current_voice = "voice/KYO04B_CRS0001.ogg"
    "山村先生？" "「不对啊啊啊────！！！」"

    $ stopvoc("OKA")
    play OKA "KYO04B_OKA0010"
    $ current_voice = "voice/KYO04B_OKA0010.ogg"
    "伦太郎" "「所以说你是谁啊！　快报上名来！」"

    $ stopvoc("CRS")
    play CRS "KYO04B_CRS0002"
    $ current_voice = "voice/KYO04B_CRS0002.ogg"
    "红莉栖" "「牧濑啊！　牧濑红莉栖！　明白了吗！？」"

    $ stopvoc("OKA")
    play OKA "KYO04B_OKA0011"
    $ current_voice = "voice/KYO04B_OKA0011.ogg"
    "伦太郎" "「哦哦，＠ｃｈａｎｎｅｌ红莉栖啊！　正是时候！」"

    $ stopvoc("CRS")
    play CRS "KYO04B_CRS0003"
    $ current_voice = "voice/KYO04B_CRS0003.ogg"
    "红莉栖" "「别用那个叫法啊！」"

    $ stopvoc("OKA")
    play OKA "KYO04B_OKA0012"
    $ current_voice = "voice/KYO04B_OKA0012.ogg"
    "伦太郎" "「总之先听我说，克里斯提娜！　发生不得了的事情了！」"

    $ stopvoc("CRS")
    play CRS "KYO04B_CRS0004"
    $ current_voice = "voice/KYO04B_CRS0004.ogg"
    "红莉栖" "「我这边也发生不得了的事情了！　全部是你的错啊！」"

    $ stopvoc("OKA")
    play OKA "KYO04B_OKA0013"
    $ current_voice = "voice/KYO04B_OKA0013.ogg"
    "伦太郎" "「怎么了……？」"

    $ stopvoc("CRS")
    play CRS "KYO04B_CRS0005"
    $ current_voice = "voice/KYO04B_CRS0005.ogg"
    "红莉栖" "「手机掉了啦！」"

    $ stopvoc("OKA")
    play OKA "KYO04B_OKA0014"
    $ current_voice = "voice/KYO04B_OKA0014.ogg"
    "伦太郎" "「掉到哪里了……？」"

    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_SALVEGE"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_SALVEGE"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_SALVEGE"])

    $ stopvoc("CRS")
    play CRS "KYO04B_CRS0006"
    $ current_voice = "voice/KYO04B_CRS0006.ogg"
    "红莉栖" "「厕所里！　都进水了！　{color=f00}Ｓａｖａｌｇｅ{/color}虽然成功了，但是连响都不会响一下了！」"

    $ stopvoc("OKA")
    play OKA "KYO04B_OKA0015"
    $ current_voice = "voice/KYO04B_OKA0015.ogg"
    "伦太郎" "「也就是，坏掉了？」"

    $ stopvoc("CRS")
    play CRS "KYO04B_CRS0007"
    $ current_voice = "voice/KYO04B_CRS0007.ogg"
    "红莉栖" "「是啊！　所以才用公共电话和你联系啊！」"

    $ stopvoc("OKA")
    play OKA "KYO04B_OKA0016"
    $ current_voice = "voice/KYO04B_OKA0016.ogg"
    "伦太郎" "「那真是那真是……我深表哀悼」"

    $ stopvoc("CRS")
    play CRS "KYO04B_CRS0008"
    $ current_voice = "voice/KYO04B_CRS0008.ogg"
    "红莉栖" "「你在开玩笑吗！？」"

    $ stopvoc("OKA")
    play OKA "KYO04B_OKA0017"
    $ current_voice = "voice/KYO04B_OKA0017.ogg"
    "伦太郎" "「但那个怎么就变成我的错了？」"

    $ stopvoc("CRS")
    play CRS "KYO04B_CRS0009"
    $ current_voice = "voice/KYO04B_CRS0009.ogg"
    "红莉栖" "「都怪你突然说什么『开发评议会终止』！明明我们东西才买了一半」"
    $ stopvoc("CRS")
    play CRS "KYO04B_CRS0010"
    $ current_voice = "voice/KYO04B_CRS0010.ogg"
    "红莉栖" "「突然打了个电话过来，连理由都不说就单方面宣布了终止评议会……！所以我才会这么烦躁……」"

    $ stopvoc("OKA")
    play OKA "KYO04B_OKA0018"
    $ current_voice = "voice/KYO04B_OKA0018.ogg"
    "伦太郎" "「烦躁着……？」"

    $ stopvoc("CRS")
    play CRS "KYO04B_CRS0011"
    $ current_voice = "voice/KYO04B_CRS0011.ogg"
    "红莉栖" "「来到了……这个网咖……」"

    $ stopvoc("OKA")
    play OKA "KYO04B_OKA0019"
    $ current_voice = "voice/KYO04B_OKA0019.ogg"
    "伦太郎" "「呼……在网咖啊，你这家伙」"

    $ stopvoc("CRS")
    play CRS "KYO04B_CRS0012"
    $ current_voice = "voice/KYO04B_CRS0012.ogg"
    "红莉栖" "「啊，你刚才笑了吧！」"

    $ stopvoc("OKA")
    play OKA "KYO04B_OKA0020"
    $ current_voice = "voice/KYO04B_OKA0020.ogg"
    "伦太郎" "「才没有，只是长了点草而已」（注：网上经常可以看到ｗｗｗ这样的字符表示笑，多了以后看起来像草）"

    $ stopvoc("CRS")
    play CRS "KYO04B_CRS0013"
    $ current_voice = "voice/KYO04B_CRS0013.ogg"
    "红莉栖" "「唔咕……」"

    $ stopvoc("OKA")
    play OKA "KYO04B_OKA0021"
    $ current_voice = "voice/KYO04B_OKA0021.ogg"
    "伦太郎" "「所以也就是在那个网咖的厕所里手机掉了对吧……」"

    $ stopvoc("CRS")
    play CRS "KYO04B_CRS0014"
    $ current_voice = "voice/KYO04B_CRS0014.ogg"
    "红莉栖" "「是啊！　所以全部——是你的错啊！」"

    "虽然觉得这个因果关系有点远……嘛算了。"
    "现在不是纠结那个的时候。"
    $ stopvoc("OKA")
    play OKA "KYO04B_OKA0022"
    $ current_voice = "voice/KYO04B_OKA0022.ogg"
    "伦太郎" "「克里斯提娜，冷静下来了吗……？」"

    $ stopvoc("CRS")
    play CRS "KYO04B_CRS0015"
    $ current_voice = "voice/KYO04B_CRS0015.ogg"
    "红莉栖" "「怎，怎么……？」"

    $ stopvoc("OKA")
    play OKA "KYO04B_OKA0023"
    $ current_voice = "voice/KYO04B_OKA0023.ogg"
    "伦太郎" "「听起来好像是暂时冷静下来了呢。」"

    $ stopvoc("CRS")
    play CRS "KYO04B_CRS0016"
    $ current_voice = "voice/KYO04B_CRS0016.ogg"
    "红莉栖" "「所以说怎么了啊……？」"

    $ stopvoc("OKA")
    play OKA "KYO04B_OKA0024"
    $ current_voice = "voice/KYO04B_OKA0024.ogg"
    "伦太郎" "「那么就听好了，我再说一次，发生了不得了的事情。」"
    "我就把在Ｌａｂ前的奇怪家伙，已经到现在为止发生过的一切全部所有的事情说了一遍。"
    "听完了我说的话以后，红莉栖小小地叹了一口气。"

    $ stopvoc("CRS")
    play CRS "KYO04B_CRS0017"
    $ current_voice = "voice/KYO04B_CRS0017.ogg"
    "红莉栖" "「明白了啊……」"
    $ stopvoc("CRS")
    play CRS "KYO04B_CRS0018"
    $ current_voice = "voice/KYO04B_CRS0018.ogg"
    "红莉栖" "「总之眼下的最优先事项应该是保证真由理的人身安全吧……」"

    "沉默降临。"
    "从手机的另一侧只传来些许的噪音。"
    "然而这份寂静并没有持续太久。"
    play se "SGSE022"

    "我听到了玄关的门被敲的声音。"
    $ stopvoc("OKA")
    play OKA "KYO04B_OKA0025"
    $ current_voice = "voice/KYO04B_OKA0025.ogg"
    "伦太郎" "「难道说……」"

    $ stopvoc("CRS")
    play CRS "KYO04B_CRS0019"
    $ current_voice = "voice/KYO04B_CRS0019.ogg"
    "红莉栖" "「怎么了！？」"

    "我立刻朝窗外瞄了一眼。"
    hide screen phoneSD1
    window hide
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_KYO002A"]]["Check"]=True


    $ loadBG(2,"EV_KYO002A")



    hide screen phonebtn
    "谁也没有……"
    "车周围的那群黑斗篷男不见了。"
    "也就是说……"
    window hide


    $ loadBG(2,"BG01E")



    show screen phonebtn
    show screen phoneSD1
    play se "SGSE022"




    $ stopvoc("OKA")
    play OKA "KYO04B_OKA0026"
    $ current_voice = "voice/KYO04B_OKA0026.ogg"
    "伦太郎" "「麻烦了，现在，那群家伙已经到门外了」"

    $ stopvoc("CRS")
    play CRS "KYO04B_CRS0020"
    $ current_voice = "voice/KYO04B_CRS0020.ogg"
    "红莉栖" "「锁呢……？」"

    $ stopvoc("OKA")
    play OKA "KYO04B_OKA0027"
    $ current_voice = "voice/KYO04B_OKA0027.ogg"
    "伦太郎" "「锁着，但是破门而入只是时间问题吧」"
    "再次降临的沉默……"
    "手心开始出汗。"
    "感觉右手就要拿不住手机了，于是就用左手也扶着。"
    "又过了一会，红莉栖说道。"

    $ stopvoc("CRS")
    play CRS "KYO04B_CRS0021"
    $ current_voice = "voice/KYO04B_CRS0021.ogg"
    "红莉栖" "「按照我说的去做吧，我有个想法」"

    $ stopvoc("OKA")
    play OKA "KYO04B_OKA0028"
    $ current_voice = "voice/KYO04B_OKA0028.ogg"
    "伦太郎" "「想法……？」"

    $ stopvoc("CRS")
    play CRS "KYO04B_CRS0022"
    $ current_voice = "voice/KYO04B_CRS0022.ogg"
    "红莉栖" "「禁止提问哦。那群人已经在门外了吧？没有时间了，赶紧行动吧」"

    $ stopvoc("OKA")
    play OKA "KYO04B_OKA0029"
    $ current_voice = "voice/KYO04B_OKA0029.ogg"
    "伦太郎" "「就算你说要行动……该做什么啊？」"

    $ stopvoc("CRS")
    play CRS "KYO04B_CRS0023"
    $ current_voice = "voice/KYO04B_CRS0023.ogg"
    "红莉栖" "「设定电话微波炉……。发送Ｄｍａｉｌ」"

    $ stopvoc("OKA")
    play OKA "KYO04B_OKA0030"
    $ current_voice = "voice/KYO04B_OKA0030.ogg"
    "伦太郎" "「Ｄｍａｉｌ？」"

    $ stopvoc("CRS")
    play CRS "KYO04B_CRS0024"
    $ current_voice = "voice/KYO04B_CRS0024.ogg"
    "红莉栖" "「不是说禁止提问了吗？」"

    $ stopvoc("OKA")
    play OKA "KYO04B_OKA0031"
    $ current_voice = "voice/KYO04B_OKA0031.ogg"
    "伦太郎" "「就算你那么说，我该发送什么样的Ｄｍａｉｌ总得告诉我吧……」"

    $ stopvoc("CRS")
    play CRS "KYO04B_CRS0025"
    $ current_voice = "voice/KYO04B_CRS0025.ogg"
    "红莉栖" "「别搞错了，不是你要发送Ｄｍａｉｌ，是我来发」"

    $ stopvoc("OKA")
    play OKA "KYO04B_OKA0032"
    $ current_voice = "voice/KYO04B_OKA0032.ogg"
    "伦太郎" "「…………」"

    $ stopvoc("CRS")
    play CRS "KYO04B_CRS0026"
    $ current_voice = "voice/KYO04B_CRS0026.ogg"
    "红莉栖" "「好啦，知道的话就赶紧行动吧！」"

    window hide
    call hide_phone

    hide screen phonebtn
    "眼下好像只有按照她的指示来行动了。"
    "我为了设定电话微波炉（暂），而跑进了开发室。"
    window hide


    $ loadBG(2,"BG03A4")



    "在那里看到了真由理。"
    "真由理在屋子的一个角落里抱着膝盖坐着。"
    "头上戴着耳机。"
    "好像是在听着ＭＰ３里的音乐。"
    "从这里看过去，歪着头的真由理……"
    "我将手掌朝着真由理，用口型说了一句『不用在意』。"
    "然后启动了Ｘ６８０００——"
    window hide
    show screen phonebtn


    "将手机放在耳边，我说道。"
    $ stopvoc("OKA")
    play OKA "KYO04B_OKA0033"
    $ current_voice = "voice/KYO04B_OKA0033.ogg"
    "伦太郎" "「告诉我一件事吧，为什么不用时间跳跃而是用Ｄｍａｉｌ？」"

    $ stopvoc("CRS")
    play CRS "KYO04B_CRS0027"
    $ current_voice = "voice/KYO04B_CRS0027.ogg"
    "红莉栖" "「别的世界线的我说过『时间机器是残次品』这样的话吧，我只是相信我自己说的，所以才这么决定」"

    "但是，我刚刚才成功地进行过时间跳跃。"
    "虽说那就是个反例……"
    play se "SGSE117"

    "但是那想法被门把的剧烈摇晃声所打断了。"
    "看起来已经是不能多嘴的场合了。"
    $ stopvoc("OKA")
    play OKA "KYO04B_OKA0034"
    $ current_voice = "voice/KYO04B_OKA0034.ogg"
    "伦太郎" "「明白了啊。那么……Ｄｍａｉｌ发送到的时间和收件人是？」"

    $ stopvoc("CRS")
    play CRS "KYO04B_CRS0028"
    $ current_voice = "voice/KYO04B_CRS0028.ogg"
    "红莉栖" "「发送时间是冈部的手机。时间是……那个……」"
    $ stopvoc("CRS")
    play CRS "KYO04B_CRS0029"
    $ current_voice = "voice/KYO04B_CRS0029.ogg"
    "红莉栖" "「３小时前──把定时器设置为１８０秒吧」"

    $ stopvoc("OKA")
    play OKA "KYO04B_OKA0035"
    $ current_voice = "voice/KYO04B_OKA0035.ogg"
    "伦太郎" "「为什么是３小时前……？」"

    $ stopvoc("CRS")
    play CRS "KYO04B_CRS0030"
    $ current_voice = "voice/KYO04B_CRS0030.ogg"
    "红莉栖" "「烦死了！　哪来那么多问题啊！　还想不想救真由理了啊！？」"

    play se "SGSE022"

    "切……"
    "我砸了砸舌，完成了设定。"
    hide screen phoneSD1
    window hide

    call hide_phone

    $ loadBG(0,"BG_BLACK")

    hide screen phonebtn
    "…………"
    window hide

    $ loadBG(0,"BG03A4")
    show screen phonebtn



    show screen phoneSD1
    $ stopvoc("OKA")
    play OKA "KYO04B_OKA0036"
    $ current_voice = "voice/KYO04B_OKA0036.ogg"
    "伦太郎" "「完成了，收件人是我的手机。定时器设定为１８０秒了」"

    $ stopvoc("CRS")
    play CRS "KYO04B_CRS0031"
    $ current_voice = "voice/KYO04B_CRS0031.ogg"
    "红莉栖" "「那么，从现在开始３分钟后请准时启动电话微波炉，拜托了哦」"

    $ stopvoc("OKA")
    play OKA "KYO04B_OKA0037"
    $ current_voice = "voice/KYO04B_OKA0037.ogg"
    "伦太郎" "「喂，给我等等，为什么──」"

    "还想问一下为什么是３分钟以后启动，但是她已经挂掉了电话。"
    $ stopvoc("OKA")
    play OKA "KYO04B_OKA0038"
    $ current_voice = "voice/KYO04B_OKA0038.ogg"
    "伦太郎" "「可恶……！」"
    window hide
    call hide_phone
    hide screen phoneSD1
    window hide


    hide screen phonebtn
    "然后无限漫长的３分钟过去了。"
    "在那期间，室内一直向着门把手被不停转动的声音。"
    "敲门声也没有停下来。"
    "我想反正那门迟早要被踹破，所以没有在意。"
    "与我的紧张形成鲜明对比，真由理用指尖打着拍子，还哼着歌。"

    window hide




    show screen phonebtn
    show screen phoneSD1
    "然后……时间终于到了。"
    "不明白红莉栖在计划着什么。"
    "但现在除了相信她也没有别的办法了"
    "那家伙肯定会设法做点什么的……"
    "我怀着祈祷的心情启动了电话微波炉。"
    window hide

    play se "SGSE035L" loop

    "很快，放电现象发生了——"
    show houden 





    "在那之后然后电话响了。"



    window hide
    hide screen phonebtn
    hide screen phonebtn2
    show screen phone(interact=False)

    "朝手机的画面看了一眼，是和刚才一样的公共电话。"
    "是红莉栖……发生了什么吗……！？"
    "我慌忙地按下了接通键。"






    $ stopvoc("CRS")
    play CRS "KYO04B_CRS0032"
    $ current_voice = "voice/KYO04B_CRS0032.ogg"
    "红莉栖" "「抱歉！　现在请立刻改变收件人！」"

    $ stopvoc("OKA")
    play OKA "KYO04B_OKA0039"
    $ current_voice = "voice/KYO04B_OKA0039.ogg"
    "伦太郎" "「什——什么！？　放电现象已经开始了哦！」"

    $ stopvoc("CRS")
    play CRS "KYO04B_CRS0033"
    $ current_voice = "voice/KYO04B_CRS0033.ogg"
    "红莉栖" "「好了快点！　把收件人设置成真由理！」"
    $ stopvoc("CRS")
    play CRS "KYO04B_CRS0034"
    $ current_voice = "voice/KYO04B_CRS0034.ogg"
    "红莉栖" "「注意到了啊！　这样的话暴露给敌人的可能性会低一些！」"

    "头脑里充满了问号。"
    "但是已经没有时间问清楚了。"
    "在放电现象发生的时候改变收件人，这还是第一次。"
    "应该还是没问题的吧……？"
    "不太清楚……虽然不太确定……"
    "但是没有其他选项了，只有这么做才行。"
    "我按照红莉栖的指示，将收件人改成了真由理。"
    $ stopvoc("OKA")
    play OKA "KYO04B_OKA0040"
    $ current_voice = "voice/KYO04B_OKA0040.ogg"
    "伦太郎" "「完成了！」"

    $ stopvoc("CRS")
    play CRS "KYO04B_CRS0035"
    $ current_voice = "voice/KYO04B_CRS0035.ogg"
    "红莉栖" "「Ｔｈａｎｋｓ……间不容发地赶上了呢」"
    $ stopvoc("CRS")
    play CRS "KYO04B_CRS0036"
    $ current_voice = "voice/KYO04B_CRS0036.ogg"
    "红莉栖" "「这样就都完成了啊。很快Ｒｅａｄｉｎｇ・Ｓｔｅｉｎｅｒ就该发动了」"
    $ stopvoc("CRS")
    play CRS "KYO04B_CRS0037"
    $ current_voice = "voice/KYO04B_CRS0037.ogg"
    "红莉栖" "「我写的邮件，设置为了延迟发送，所以很快就……」"

    $ stopvoc("OKA")
    play OKA "KYO04B_OKA0041"
    $ current_voice = "voice/KYO04B_OKA0041.ogg"
    "伦太郎" "「……？」"

    $ stopvoc("CRS")
    play CRS "KYO04B_CRS0038"
    $ current_voice = "voice/KYO04B_CRS0038.ogg"
    "红莉栖" "「啊啊，对了对了，最后告诉你一点吧」"
    $ stopvoc("CRS")
    play CRS "KYO04B_CRS0039"
    $ current_voice = "voice/KYO04B_CRS0039.ogg"
    "红莉栖" "「将Ｄｍａｉｌ发送到３小时之前的理由──」"
    $ stopvoc("CRS")
    play CRS "KYO04B_CRS0040"
    $ current_voice = "voice/KYO04B_CRS0040.ogg"
    "红莉栖" "「现在是『１８点１８分』对吧？」"
    $ stopvoc("CRS")
    play CRS "KYO04B_CRS0041"
    $ current_voice = "voice/KYO04B_CRS0041.ogg"
    "红莉栖" "「我呢，想在帮助真由理的同时也……顺便救一下自己的手机。」"
    $ stopvoc("CRS")
    play CRS "KYO04B_CRS0042"
    $ current_voice = "voice/KYO04B_CRS0042.ogg"
    "红莉栖" "「那，之后请多关照了」"

    window hide


    call hide_phone
    "电话就这么断了，但我心中仍然有一件在意的事。"
    "『Ｄｍａｉｌ的内容呢……？』"
    "但是那个疑问，逐渐消溶在摇晃起来的视界中。"


    stop bgm 
    hide screen phoneSD1




    hide houden 
    $ loadBG(2,"BG_BLACK")
    hide screen phonebtn
    show screen invisible
    $ renpy.movie_cutscene("video/WDIMV_03A.avi")
    hide screen invisible

    return


    stop se

    return
