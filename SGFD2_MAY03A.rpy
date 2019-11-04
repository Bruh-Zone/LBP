label SGFD2_MAY03A:
    hide screen phonebtn
    scene expression Solid("000000")  with fade

    window hide


    $ loadBG(0,"IBG010A")

    play bgm "FD2BGM09"

    $ date="8/16"
    $ day="MON"
    hide screen phonebtn
    hide screen phoneSD1

    "昨天晚上被冈伦处以了团子之刑。"
    "团子和往常一样是炭火烤的。"
    "表面散发着香气，豆馅甜度适中，非常的好吃。"
    "和冈伦一起，吃了草团子和御手洗团子，一直吃到吃不下为止。"
    "真是分外怀念这久违的感觉。"
    "从每天来这里给外婆上坟那时的事情开始，自然地聊起了过去的事。"
    "比如冈伦向往着成为炎术士，经常戴着断指手套的事。"
    "比如真由喜开始制作ＣＯＳ服装的事。"
    "说了好多好多漫无边际而又平淡无奇的事。"
    "就好像回到了刚成立Ｌａｂ的时候，Ｌａｂｍｅｍ只有冈伦和真由喜两个人的时候一样。"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0000"
    $ current_voice = "voice/MAY03A_MAY0000.ogg"
    "真由理" "「是因为最近太忙了吗？　昨天久违地感觉到了时间过得很慢……」"
    "昨天其实是想在睡觉前写日记的，但是回到家洗完澡之后，就倒在床上睡着了。"
    "也没有做可怕的梦，感觉好久都没睡这么舒服了。"
    "不过醒来以后让人吓了一跳，别说睡到中午了，竟然是傍晚……"
    "被妈妈笑话说贪睡也要有个度啊。"
    "没吃到点心，而是吃了特别晚的早饭，之后我为了不让自己忘记昨天的团子之刑，开始记日记。"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0001"
    $ current_voice = "voice/MAY03A_MAY0001.ogg"
    "真由理" "「……写完了」"
    window hide


    $ loadBG(2,"BG62A")



    hide screen phonebtn
    hide screen phoneSD1
    "写完日记后，把封面盖上。"
    "带着完成工作的感觉，舒舒服服地伸了个懒腰。"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0002"
    $ current_voice = "voice/MAY03A_MAY0002.ogg"
    "真由理" "「对了，趁着还没忘，给冈伦发个感谢昨天的事的邮件吧」"
    "从包的口袋里掏出手机。"
    window hide
    show screen phonebtn



    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0003"
    $ current_voice = "voice/MAY03A_MAY0003.ogg"
    "真由理" "「不好，没有电了……」"
    window hide
    call hide_phone

    hide screen phonebtn
    show screen phoneSD1

    stop bgm 
    $ targetmailid = gc["ScriptMacros"]["FM_MAY03A_RECV_CRS01"]
    if phonemailring!= "":
        play se phonemailring
    if persistent.skipmail==False:
        $ renpy.choice_for_skipping()
    if targetmailid != "":
        $ RcvMail(targetmailid)
        $ targetmailid=""
    $ targetmailid = gc["ScriptMacros"]["FM_MAY03A_RECV_FEI01"]
    if phonemailring!= "":
        play se phonemailring
    if persistent.skipmail==False:
        $ renpy.choice_for_skipping()
    if targetmailid != "":
        $ RcvMail(targetmailid)
        $ targetmailid=""
    "把手机插上充电器以后，收到了大量的邮件。"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0004"
    $ current_voice = "voice/MAY03A_MAY0004.ogg"
    "真由理" "「哎？」"
    window hide

    stop bgm 
    show screen phonebtn
    hide screen phonebtn
    hide screen phonebtn2

    play bgm "FD2BGM04"
    $ targetmailid = gc["ScriptMacros"]["FM_MAY03A_RECV_CRS01"]




    $ targetmailid = gc["ScriptMacros"]["FM_MAY03A_RECV_FEI01"]
    call read_last_mail (1)
    call hide_phone
    call read_last_mail (0)
    call hide_phone





    "还收到了许多菲利斯的留言电话。"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0005"
    $ current_voice = "voice/MAY03A_MAY0005.ogg"
    "真由理" "「这是怎么了呢，菲利斯和红莉栖酱，发生什么事了呢？」"
    hide screen phonebtn
    show screen phone(interact=False)
    window hide



    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0006"
    $ current_voice = "voice/MAY03A_MAY0006.ogg"
    "真由理" "「……打不通」"
    "心里有一种不祥的预感。"
    window hide










    $ stopvoc("FEI")
    play FEI "MAY03A_FEI0000"
    $ current_voice = "voice/MAY03A_FEI0000.ogg"
    "菲利斯" "「喂喂！？　啊啊，真由喜！　我等着你的电话呢！」"

    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0007"
    $ current_voice = "voice/MAY03A_MAY0007.ogg"
    "真由理" "「菲利斯，联系晚了对不起呢，我到现在才发现手机没有电了……」"

    $ stopvoc("FEI")
    play FEI "MAY03A_FEI0001"
    $ current_voice = "voice/MAY03A_FEI0001.ogg"
    "菲利斯" "「没关系，反而该道歉的应该是菲利斯喵」"

    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0008"
    $ current_voice = "voice/MAY03A_MAY0008.ogg"
    "真由理" "「跟红莉栖酱之间发生什么了吗？」"



    $ stopvoc("FEI")
    play FEI "MAY03A_FEI0002"
    $ current_voice = "voice/MAY03A_FEI0002.ogg"
    "菲利斯" "「这个……菲利斯把红喵惹生气了喵」"

    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0009"
    $ current_voice = "voice/MAY03A_MAY0009.ogg"
    "真由理" "「诶诶？　怎么了？」"

    $ stopvoc("FEI")
    play FEI "MAY03A_FEI0003"
    $ current_voice = "voice/MAY03A_FEI0003.ogg"
    "菲利斯" "「红喵看起来在为父亲的事发愁的样子，没法放着不管，不经意间就说了很多不该说的话喵……」"

    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0010"
    $ current_voice = "voice/MAY03A_MAY0010.ogg"
    "真由理" "「父亲的事……」"

    $ stopvoc("FEI")
    play FEI "MAY03A_FEI0004"
    $ current_voice = "voice/MAY03A_FEI0004.ogg"
    "菲利斯" "「……菲利斯不想让她有同样的后悔，希望她们两个人能够和好。但是对于红喵来说，可能是多管闲事了喵」"
    $ stopvoc("FEI")
    play FEI "MAY03A_FEI0005"
    $ current_voice = "voice/MAY03A_FEI0005.ogg"
    "菲利斯" "「红喵，不知怎的就发起火来……留下了不明所以的话就跑到外面去了喵……」"

    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0011"
    $ current_voice = "voice/MAY03A_MAY0011.ogg"
    "真由理" "「不明所以的话？」"

    $ stopvoc("FEI")
    play FEI "MAY03A_FEI0006"
    $ current_voice = "voice/MAY03A_FEI0006.ogg"
    "菲利斯" "「『再也不会见面了』、『反正你也马上就会忘记我曾经在这里出现过了』什么的，非常耐人寻味的话语喵……」"

    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0012"
    $ current_voice = "voice/MAY03A_MAY0012.ogg"
    "真由理" "「红莉栖酱说了这种话！？」"
    "红莉栖酱不会毫无根据地说出这种话的。"
    "「反正你也马上就会忘记我曾经在这里出现过了」这句话让我在意的是，「你也」这个部分。"
    "意味着不光是菲利斯酱，其他的人也会忘记红莉栖的存在？"
    "虽说随着时间的流逝，人们会忘记很多的事情，不过那种场合，不会使用『马上』这个词。"
    "就是说马上，大家就会忘记红莉栖酱的存在？"
    "就是说不会再见到红莉栖酱了？"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0013"
    $ current_voice = "voice/MAY03A_MAY0013.ogg"
    "真由理" "「怎么会，是我想太多了……」"
    "摇了摇头，慌慌张张地驱散了不吉利的设想。"
    "可是，不好的预感，逐渐地膨胀了起来。"
    hide screen phoneSD1
    window hide

    call hide_phone

    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_MAY001A"]]["Check"]=True
    $ loadBG(0,"EV_MAY001A")

    $ stopvoc("CRS")
    play CRS "MAY03A_CRS0000"
    $ current_voice = "voice/MAY03A_CRS0000.ogg"
    "红莉栖" "「我、就在……这里」"
    window hide


    $ loadBG(0,"BG62A")
    show screen phonebtn
    hide screen phonebtn
    hide screen phonebtn2
    show screen phone(interact=False)



    show screen phoneSD1
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0014"
    $ current_voice = "voice/MAY03A_MAY0014.ogg"
    "真由理" "「红莉栖酱……」"



    $ stopvoc("FEI")
    play FEI "MAY03A_FEI0007"
    $ current_voice = "voice/MAY03A_FEI0007.ogg"
    "菲利斯" "「总之……红喵在听了凶真的话以后就像变了个人一样喵……非常想不开的样子喵……」"

    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0015"
    $ current_voice = "voice/MAY03A_MAY0015.ogg"
    "真由理" "「怪不得状态有些奇怪呢……原来红莉栖酱是纠结在了这个地方……没有想到啊」"
    "明明要是能注意到的话，在法事结束之后就会立刻赶到红莉栖酱的身边去了。"
    "至少如果手机还有电的话，也不会发现不了红莉栖酱发来的邮件，和菲利斯打来的电话了。"
    "真由喜我居然什么都不知道，悠闲地在和冈伦吃着团子。"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0016"
    $ current_voice = "voice/MAY03A_MAY0016.ogg"
    "真由理" "「对不起，菲利斯……」"

    $ stopvoc("FEI")
    play FEI "MAY03A_FEI0008"
    $ current_voice = "voice/MAY03A_FEI0008.ogg"
    "菲利斯" "「或许是菲利斯给了红喵最后一击也说不定喵……」"

    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0017"
    $ current_voice = "voice/MAY03A_MAY0017.ogg"
    "真由理" "「才不是呢，红莉栖酱给我发来了“帮我向菲利斯道歉的邮件”……菲利斯并没有错」"



    $ stopvoc("FEI")
    play FEI "MAY03A_FEI0009"
    $ current_voice = "voice/MAY03A_FEI0009.ogg"
    "菲利斯" "「……真由喜」"

    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0018"
    $ current_voice = "voice/MAY03A_MAY0018.ogg"
    "真由理" "「总之，现在虽然联系不上，但真由喜会想办法联系上红莉栖酱的」"

    $ stopvoc("FEI")
    play FEI "MAY03A_FEI0010"
    $ current_voice = "voice/MAY03A_FEI0010.ogg"
    "菲利斯" "「那就太好了喵……菲利斯有什么能帮上忙的喵？　命令黑木他们去探查红喵的住所喵？」"

    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0019"
    $ current_voice = "voice/MAY03A_MAY0019.ogg"
    "真由理" "「不，弄出大乱子就不太好了。先由真由喜来找找红莉栖酱试试看，到了真的没有办法的时候，可能会再来拜托菲利斯」"



    $ stopvoc("FEI")
    play FEI "MAY03A_FEI0011"
    $ current_voice = "voice/MAY03A_FEI0011.ogg"
    "菲利斯" "「明白了喵！　那么，菲利斯就原地待命随时等候派遣的喵！」"

    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0020"
    $ current_voice = "voice/MAY03A_MAY0020.ogg"
    "真由理" "「谢谢啦，菲利斯」"



    $ stopvoc("FEI")
    play FEI "MAY03A_FEI0012"
    $ current_voice = "voice/MAY03A_FEI0012.ogg"
    "菲利斯" "「总感觉……放不下红喵的事。感觉并不是跟自己无关的喵……」"

    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0021"
    $ current_voice = "voice/MAY03A_MAY0021.ogg"
    "真由理" "「这就是菲利斯一直所说的前世吧？」"



    $ stopvoc("FEI")
    play FEI "MAY03A_FEI0013"
    $ current_voice = "voice/MAY03A_FEI0013.ogg"
    "菲利斯" "「就是喵！　缘分是必须要珍惜的，爸爸也经常这么说。菲利斯要想想看自己能为红喵做点什么喵！」"

    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0022"
    $ current_voice = "voice/MAY03A_MAY0022.ogg"
    "真由理" "「谢谢。那么，有事再联系了！」"



    $ stopvoc("FEI")
    play FEI "MAY03A_FEI0014"
    $ current_voice = "voice/MAY03A_FEI0014.ogg"
    "菲利斯" "「拜托了喵♪」"

    window hide





    "挂断电话之后，再一次地试着给红莉栖酱打电话。"
    "红莉栖酱没有接电话。"

    "过了一会，转移到了语音信箱服务。"
    window hide
    call hide_phone

    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0023"
    $ current_voice = "voice/MAY03A_MAY0023.ogg"
    "真由理" "「红莉栖酱，没事吧……」"
    "或许只是单纯的因为太忙所以才没接电话……"
    "不祥的预感挥之不去，一直盘绕在心间。"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0024"
    $ current_voice = "voice/MAY03A_MAY0024.ogg"
    "真由理" "「发生什么事了呢？　真由喜是绝对不会忘记红莉栖酱的……」"
    "大家马上就会忘记红莉栖酱什么的。"
    "这种事，无法相信。"
    "马上，是指什么时候呢？"
    "红莉栖酱的状态奇怪就是因为这个吗？"
    "想要见到红莉栖酱。"
    "不，是必须要见到。"
    "没有办法安稳地呆下去了，于是就拿着手机，冲到了屋外。"
    hide screen phoneSD1
    window hide



    $ loadBG(0,"BG16A5")
    python:
        SndMail(57)
        SndMail(58)
        RcvMail(59)
        ReadMail(59)



    show screen phoneSD1
    "来到了秋叶原，在满是人的大街上，寻找红莉栖酱的身影。"
    "祈祷会像昨天一样偶然碰到。"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0025"
    $ current_voice = "voice/MAY03A_MAY0025.ogg"
    "真由理" "「……红莉栖酱，不在啊——」"
    "试着给红莉栖酱打了好多次电话，可是依然没有接。"
    "而且也尝试着给桶子君和冈伦发邮件问了问知不知道红莉栖酱在哪里，但回信的只有桶子君。"
    "桶子君像往常一样在Ｌａｂ里，但已经有两三天都没见着红莉栖酱了。"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0026"
    $ current_voice = "voice/MAY03A_MAY0026.ogg"
    "真由理" "「……冈伦也联系不上啊……是偶然吗？」"
    "想太多了。"
    "现在不是在乎那种事的时候。"
    "但是——"
    "脑袋里面乱成了一锅粥，让人不知所措。"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0027"
    $ current_voice = "voice/MAY03A_MAY0027.ogg"
    "真由理" "「冈伦的状态也很奇怪……」"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0028"
    $ current_voice = "voice/MAY03A_MAY0028.ogg"
    "真由理" "「那个、大概是真由喜的缘故……」"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0029"
    $ current_voice = "voice/MAY03A_MAY0029.ogg"
    "真由理" "「或许红莉栖酱也是因为真由喜……」"
    "知道自己的想法太过跳跃了。"
    "不过这就是所谓的直觉？"
    "当有不祥的预感的时候，很多情况下都是准的，所以不能无视。"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0030"
    $ current_voice = "voice/MAY03A_MAY0030.ogg"
    "真由理" "「……是这样的吗？」"
    window hide


    $ loadBG(2,"IBGX077")



    hide screen phonebtn
    "抬头仰望天空。"
    "刚才还是晴天呢，不知什么时候，灰色的云朵遮住了一片天空。"
    "正想着是不是要下雨呢，望着天空的这一会儿功夫，雨滴就落下来了。"
    window hide

    play se "SGSE364L" loop


    $ loadBG(2,"IBGX078")




    stop bgm 
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0031"
    $ current_voice = "voice/MAY03A_MAY0031.ogg"
    "真由理" "「啊、果然……下起来了」"
    "匆忙地跑到了店门口。"
    "雨滴下落的速度逐渐变快，一会儿的功夫就下起了倾盆大雨。"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0032"
    $ current_voice = "voice/MAY03A_MAY0032.ogg"
    "真由理" "「唉呀……总是这样啊。真是愁人……」"
    "从过去起就是，不知为何一到了关键时刻总会下起雨。"
    "用冈伦的话讲就是，真由喜是个不得了的雨女。"
    "每当跟冈伦在一起时下雨的话，他总会说「告诉过你了，让你出门的时候带好折叠伞！」，总是怪到真由喜的头上。"
    "「太麻烦了，我不带」真由喜这样回答之后，冈伦便念叨着「哎呀哎呀」，然后夸张地耸了耸肩，大大地叹了口气。"
    "不过随后，在便利店里买了把塑料伞，一起撑着。"
    "就像这样，从冈伦那里得到了好多的塑料伞。"
    "丢掉也怪可惜的，于是就成为了一种小收藏品。"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0033"
    $ current_voice = "voice/MAY03A_MAY0033.ogg"
    "真由理" "「阵雨吗？　这么快就停了……」"
    "冈伦现在，在哪里，做着什么呢？"
    "红莉栖酱还好吗？"
    "希望两个人没有被这突然的阵雨淋湿。"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0034"
    $ current_voice = "voice/MAY03A_MAY0034.ogg"
    "真由理" "「真由喜……成为他们两个的重担……了么？」"
    "念叨着，随后又慌忙地左右摇了摇头。"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0035"
    $ current_voice = "voice/MAY03A_MAY0035.ogg"
    "真由理" "「哇、不行不行，想太多了，进入了胡思乱想模式……」"
    "偶尔也有这种情况发生。"
    "平常明明不怎么在意细小的事情，但有时会对细微的事情在意得不得了，到让人精神恍惚的地步。"
    "在那时候冈伦会故弄玄虚地说道「你个真由理居然也会烦恼，不知好歹，这可不像你啊」"
    "现在冈伦要是在身边的话。"
    "「你个真由理，想太多啦」，这样一笑了之……"
    "不由得这么想到。"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0036"
    $ current_voice = "voice/MAY03A_MAY0036.ogg"
    "真由理" "「——或许真由喜，过于依赖冈伦了吧」"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0037"
    $ current_voice = "voice/MAY03A_MAY0037.ogg"
    "真由理" "「冈伦很温柔……就好像有点让人困扰的哥哥一样……在身边就会让人心安……心情舒畅……仅此而已……」"
    "像是在劝说自己一样念叨着。"
    "但是，越是这样念叨，就越感觉到不自然。"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0038"
    $ current_voice = "voice/MAY03A_MAY0038.ogg"
    "真由理" "「……仅此……而已……」"
    hide screen phoneSD1
    window hide

    stop se



    $ loadBG(0,"BG18E1")

    show screen phoneSD1
    "激烈的雨似乎是阵雨，不一会就停了。"
    "雨停了之后，继续开始寻找红莉栖酱。"
    "柏油路被雨淋湿，反射着耀眼的太阳光。"
    "擦亮眼睛在人来人往的道路中寻找红莉栖酱的身影。"
    "但是哪里都没有看到。　"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0039"
    $ current_voice = "voice/MAY03A_MAY0039.ogg"
    "真由理" "「带着手机，还以为什么时候都能见面呢……」"
    "在望着手机叹气的时候，被人叫住了。"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASB04"),"True","lh/DAR_ASB04a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    play bgm "BGM05"

    $ stopvoc("DAR")
    play DAR "MAY03A_DAR0000"
    $ current_voice = "voice/MAY03A_DAR0000.ogg"
    "至" "「真由氏，在这里干什么呢？」"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0040"
    $ current_voice = "voice/MAY03A_MAY0040.ogg"
    "真由理" "「啊、桶子君」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASB01"),"True","lh/DAR_ASB01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "MAY03A_DAR0001"
    $ current_voice = "voice/MAY03A_DAR0001.ogg"
    "至" "「我看到你的邮件了，还在找牧濑氏吗？」"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0041"
    $ current_voice = "voice/MAY03A_MAY0041.ogg"
    "真由理" "「……嗯，联系不上她」"
    $ stopvoc("DAR")
    play DAR "MAY03A_DAR0002"
    $ current_voice = "voice/MAY03A_DAR0002.ogg"
    "至" "「有什么急事吗？」"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0042"
    $ current_voice = "voice/MAY03A_MAY0042.ogg"
    "真由理" "「也不能算是急事……」"
    "不想让桶子君担心多余的事，于是就含糊了一下。"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0043"
    $ current_voice = "voice/MAY03A_MAY0043.ogg"
    "真由理" "「……桶子君呢？　接下来要去哪儿？」"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_NET_CAFE"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_NET_CAFE"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_NET_CAFE"])
    $ stopvoc("DAR")
    play DAR "MAY03A_DAR0003"
    $ current_voice = "voice/MAY03A_DAR0003.ogg"
    "至" "「嗯、先是ＭａｙＱｕｅｅｎ＋Ｎｙａ²，然后再去{color=#f00}Ｎｅｔ　Ｃａｆｅ{/color}转转吧」"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0044"
    $ current_voice = "voice/MAY03A_MAY0044.ogg"
    "真由理" "「哇，富翁啊」"
    $ stopvoc("DAR")
    play DAR "MAY03A_DAR0004"
    $ current_voice = "voice/MAY03A_DAR0004.ogg"
    "至" "「在每年两回的漫展时期，当然要随心所欲啦。而且我平常就在积攒资金」"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0045"
    $ current_voice = "voice/MAY03A_MAY0045.ogg"
    "真由理" "「真棒啊。为了夏Ｃｏｍｉ而攒钱，桶子君真的是宅男的典范啊」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASB02"),"True","lh/DAR_ASB02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "MAY03A_DAR0005"
    $ current_voice = "voice/MAY03A_DAR0005.ogg"
    "至" "「表扬我也没有好处的哦」"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0046"
    $ current_voice = "voice/MAY03A_MAY0046.ogg"
    "真由理" "「要是见到了红莉栖酱，就告诉真由喜哦」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASB01"),"True","lh/DAR_ASB01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "MAY03A_DAR0006"
    $ current_voice = "voice/MAY03A_DAR0006.ogg"
    "至" "「ＯＫ」"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0047"
    $ current_voice = "voice/MAY03A_MAY0047.ogg"
    "真由理" "「拜拜—」"
    $ stopvoc("DAR")
    play DAR "MAY03A_DAR0007"
    $ current_voice = "voice/MAY03A_DAR0007.ogg"
    "至" "「拜拜啦—」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    stop bgm 
    "跟桶子君道别后，再一次小小地叹了口气。"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0048"
    $ current_voice = "voice/MAY03A_MAY0048.ogg"
    "真由理" "「去Ｌａｂ看看吧？　说不定红莉栖酱跟桶子君走岔了，已经回到Ｌａｂ了呢……」"
    "想到这里，走向了Ｌａｂ。"
    window hide



    $ loadBG(0,"BG05E1")

    "来到Ｌａｂ所在的大楼前面，停下了脚步。"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0049"
    $ current_voice = "voice/MAY03A_MAY0049.ogg"
    "真由理" "「咦？　灯怎么亮着」"
    "虽然想到了可能是桶子君忘了关灯，但是从窗口那里看到了人影在动。"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0050"
    $ current_voice = "voice/MAY03A_MAY0050.ogg"
    "真由理" "「说不定是红莉栖酱！」"
    "三步并作两步地登上了楼梯。"

    window hide



    $ loadBG(0,"BG02E1")
    play se "SGSE024"


    "使劲地推开了门，冲入了Ｌａｂ。"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0051"
    $ current_voice = "voice/MAY03A_MAY0051.ogg"
    "真由理" "「红莉栖酱！　在吗！？」"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA04"),"True","lh/OKA_ASA04a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "MAY03A_OKA0000"
    $ current_voice = "voice/MAY03A_OKA0000.ogg"
    "伦太郎" "「真由……理？」"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0052"
    $ current_voice = "voice/MAY03A_MAY0052.ogg"
    "真由理" "「冈伦」"
    "从沙发上站起来的不是红莉栖酱，而是冈伦。"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ALA06"),"True","lh/OKA_ALA06a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    play bgm "FD2BGM05"

    $ stopvoc("OKA")
    play OKA "MAY03A_OKA0001"
    $ current_voice = "voice/MAY03A_OKA0001.ogg"
    "伦太郎" "「怎么了？　她出什么事了！？」"
    "冈伦变了脸色，抓住了真由喜的两臂。"
    "好大的劲，吓了我一跳。"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0053"
    $ current_voice = "voice/MAY03A_MAY0053.ogg"
    "真由理" "「那个……冈伦。对不起……胳膊……疼……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ALA07"),"True","lh/OKA_ALA07a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "MAY03A_OKA0002"
    $ current_voice = "voice/MAY03A_OKA0002.ogg"
    "伦太郎" "「……抱歉」"
    "回归神智的冈伦放开了真由喜的胳膊。"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA04"),"True","lh/OKA_ASA04a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0054"
    $ current_voice = "voice/MAY03A_MAY0054.ogg"
    "真由理" "「…………」"
    $ stopvoc("OKA")
    play OKA "MAY03A_OKA0003"
    $ current_voice = "voice/MAY03A_OKA0003.ogg"
    "伦太郎" "「…………」"
    "Ｌａｂ里弥漫着尴尬的氛围。"
    "不经意间看到了冈伦外衣的肩膀那里。"
    "用粉色的线缝得歪歪扭扭的。"
    "反射性地移开了目光。"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0055"
    $ current_voice = "voice/MAY03A_MAY0055.ogg"
    "真由理" "「冈伦……红莉栖酱……发生什么事了？」"
    $ stopvoc("OKA")
    play OKA "MAY03A_OKA0004"
    $ current_voice = "voice/MAY03A_OKA0004.ogg"
    "伦太郎" "「不……并不是这回事……」"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0056"
    $ current_voice = "voice/MAY03A_MAY0056.ogg"
    "真由理" "「要是没事的话，不会担心到这个地步的吧？」"
    $ stopvoc("OKA")
    play OKA "MAY03A_OKA0005"
    $ current_voice = "voice/MAY03A_OKA0005.ogg"
    "伦太郎" "「真由理……」"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0057"
    $ current_voice = "voice/MAY03A_MAY0057.ogg"
    "真由理" "「冈伦还有红莉栖酱……好奇怪啊……就算你说你不想现在说出来……还是好让人在意啊……」"
    $ stopvoc("OKA")
    play OKA "MAY03A_OKA0006"
    $ current_voice = "voice/MAY03A_OKA0006.ogg"
    "伦太郎" "「抱歉……」"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0058"
    $ current_voice = "voice/MAY03A_MAY0058.ogg"
    "真由理" "「在真由喜不知道的地方，是不是发生了什么不得了的事呢……或许真由喜成为的不是冈伦的重担，而是红莉栖酱的重担也说不定呢……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA03"),"True","lh/OKA_ASA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "MAY03A_OKA0007"
    $ current_voice = "voice/MAY03A_OKA0007.ogg"
    "伦太郎" "「才不是什么重荷」 "
    "冈伦从以前开始就不怎么擅长说谎。"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0059"
    $ current_voice = "voice/MAY03A_MAY0059.ogg"
    "真由理" "「我说，冈伦」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA04"),"True","lh/OKA_ASA04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "MAY03A_OKA0008"
    $ current_voice = "voice/MAY03A_OKA0008.ogg"
    "伦太郎" "「怎么了？」"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0060"
    $ current_voice = "voice/MAY03A_MAY0060.ogg"
    "真由理" "「红莉栖酱……不会消失吧？」"
    $ stopvoc("OKA")
    play OKA "MAY03A_OKA0009"
    $ current_voice = "voice/MAY03A_OKA0009.ogg"
    "伦太郎" "「…………」"
    "希望他能傻笑起来。"
    "然而，冈伦沉默不语。"
    "对不擅长说谎的冈伦来说，沉默与肯定是同一个意思。"
    "就是说，过不久红莉栖酱就要真的消失了？"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0061"
    $ current_voice = "voice/MAY03A_MAY0061.ogg"
    "真由理" "「怎么会……为什么？　红莉栖酱会消失……不要这样啊……」"
    "鼻子一阵酸痛，视线变得模糊，眼泪被地面吸了进去。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASD02"),"True","lh/OKA_ASD02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "MAY03A_OKA0010"
    $ current_voice = "voice/MAY03A_OKA0010.ogg"
    "伦太郎" "「──那样的未来，我绝对不认可！　我怎么……可能同意！」"
    "冈伦憔悴得让人心疼。"
    "但是他的眼睛里却闪着让人害怕的光。"
    $ stopvoc("OKA")
    play OKA "MAY03A_OKA0011"
    $ current_voice = "voice/MAY03A_OKA0011.ogg"
    "伦太郎" "「我……不会放弃……绝对要找到第三条路！　找到让我满意的未来。　在那之前我要无数次地重复过去！　世界的意志什么的，吃屎去吧！」"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0062"
    $ current_voice = "voice/MAY03A_MAY0062.ogg"
    "真由理" "「冈伦……」"
    "冈伦刚才的话。"
    "难道说冈伦已经重复了无数次时间跳跃？"
    "这是为了改变大家的未来？"
    "冈伦孤身一人在战斗？"
    "这种事，真由喜完全不知道。"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0063"
    $ current_voice = "voice/MAY03A_MAY0063.ogg"
    "真由理" "「……为什么……总是……」"
    "不知道该说什么好了。"
    hide screen phoneSD1
    window hide
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_MAY002A"]]["Check"]=True


    $ loadBG(2,"EV_MAY002A")



    hide screen phonebtn
    "拿过冈伦的手，放在了自己的脸上。"
    "脸蛋蹭着他那粗壮的手。"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0064"
    $ current_voice = "voice/MAY03A_MAY0064.ogg"
    "真由理" "「对不起……冈伦。没有注意到……」"
    "眼泪吧嗒吧嗒地往下掉，沾湿了冈伦的手心。"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0065"
    $ current_voice = "voice/MAY03A_MAY0065.ogg"
    "真由理" "「冈伦，已经这么痛苦了……不要再努力了……说不出口……」"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0066"
    $ current_voice = "voice/MAY03A_MAY0066.ogg"
    "真由理" "「对已经努力得超出极限的人……不要再努力了……说不出口」"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0067"
    $ current_voice = "voice/MAY03A_MAY0067.ogg"
    "真由理" "「红莉栖酱消失……真由喜不希望这样……」"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0068"
    $ current_voice = "voice/MAY03A_MAY0068.ogg"
    "真由理" "「能够帮助红莉栖酱的只有冈伦吗？」"
    $ stopvoc("OKA")
    play OKA "MAY03A_OKA0012"
    $ current_voice = "voice/MAY03A_OKA0012.ogg"
    "伦太郎" "「嗯──」"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0069"
    $ current_voice = "voice/MAY03A_MAY0069.ogg"
    "真由理" "「……为什么……只有冈伦啊？」"
    "没能帮上冈伦的忙，不甘心。"
    "冈伦在真由喜最困难的时候扶持着真由喜。"
    "想要在以后报答冈伦。"
    "想要在冈伦困难的时候，去扶持冈伦。"
    "然而真由喜却什么都做不了。"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0070"
    $ current_voice = "voice/MAY03A_MAY0070.ogg"
    "真由理" "「真由喜，真希望能够代替冈伦进行时间跳跃啊……」"
    "紧紧地握着冈伦的手。"
    $ stopvoc("OKA")
    play OKA "MAY03A_OKA0013"
    $ current_voice = "voice/MAY03A_OKA0013.ogg"
    "伦太郎" "「哼，不要说傻话了，真由理。你不可能代替我凤凰院凶真完成任务的」"
    window hide
    $ persistent.gd["EVData"][gc["ScriptMacros"]["fEV_MAY002B"]]["Check"]=True


    $ loadBG(2,"EV_MAY002B")



    "冈伦像往常那样邪笑了起来。"
    $ stopvoc("OKA")
    play OKA "MAY03A_OKA0014"
    $ current_voice = "voice/MAY03A_OKA0014.ogg"
    "伦太郎" "「一切都是……命运石之门的选择。所以你不需要烦恼」"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0071"
    $ current_voice = "voice/MAY03A_MAY0071.ogg"
    "真由理" "「……但是」"
    $ stopvoc("OKA")
    play OKA "MAY03A_OKA0015"
    $ current_voice = "voice/MAY03A_OKA0015.ogg"
    "伦太郎" "「人质就要像人质一样，老老实实地呆着就好了」"
    "冈伦额头的皱纹更加的深了。"
    "对烦恼至极的冈伦的表情，什么话也说不出来。"
    "真由喜并不是想让冈伦痛苦。"
    "不想见到这样的表情。"
    $ stopvoc("OKA")
    play OKA "MAY03A_OKA0016"
    $ current_voice = "voice/MAY03A_OKA0016.ogg"
    "伦太郎" "「真由理，我们说好了吧？　我会在可以说的时候把一切告诉你的──这个约定你忘了吗？」"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0072"
    $ current_voice = "voice/MAY03A_MAY0072.ogg"
    "真由理" "「……记得。但是，冈伦……」"
    "既然已经知道冈伦是孤身一人在战斗，怎么能在这里光等着……"
    "怎么样都行，想要成为冈伦的力量。"
    "真由喜……也想帮上忙。"
    "想要对冈伦这样说。"
    "然而在这些话刚到嘴边的时候，又勉强地咽下去了。"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0073"
    $ current_voice = "voice/MAY03A_MAY0073.ogg"
    "真由理" "「……约定……必须得遵守呢……」"
    "就像嗓子眼里塞着石头一样，没法好好说出话来。"
    $ stopvoc("OKA")
    play OKA "MAY03A_OKA0017"
    $ current_voice = "voice/MAY03A_OKA0017.ogg"
    "伦太郎" "「嗯」"
    "看到冈伦带有恐吓意味的严峻表情舒缓了下来，松了一口气。"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0074"
    $ current_voice = "voice/MAY03A_MAY0074.ogg"
    "真由理" "「但是、冈伦……拜托了……不要太勉强。努力的时候不要太勉强，虽然真由喜知道这是个无礼的请求」"
    $ stopvoc("OKA")
    play OKA "MAY03A_OKA0018"
    $ current_voice = "voice/MAY03A_OKA0018.ogg"
    "真由理" "「我没事。真由理，反倒是你……」"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0075"
    $ current_voice = "voice/MAY03A_MAY0075.ogg"
    "真由理" "「嗯？　怎么了？」"
    $ stopvoc("OKA")
    play OKA "MAY03A_OKA0019"
    $ current_voice = "voice/MAY03A_OKA0019.ogg"
    "伦太郎" "「你……没事吧？　刚才没发生什么吧？」"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0076"
    $ current_voice = "voice/MAY03A_MAY0076.ogg"
    "真由理" "「…………」"
    "被冈伦问了跟红莉栖酱同样的问题，一瞬间脑袋里变得一片空白。"
    window hide



    $ loadBG(2,"BG02E1")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ALA01"),"True","lh/OKA_ALA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    show screen phonebtn
    show screen phoneSD1
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0077"
    $ current_voice = "voice/MAY03A_MAY0077.ogg"
    "真由理" "「……真是的。冈伦，跟红莉栖酱也说过了，真由喜一直都是充满精神的……没事的哟？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ALA04"),"True","lh/OKA_ALA04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "MAY03A_OKA0020"
    $ current_voice = "voice/MAY03A_OKA0020.ogg"
    "伦太郎" "「是么……」"
    "冈伦的脸色阴沉了下来。"
    "红莉栖酱和冈伦似乎共享着某个不能对真由喜说的秘密。"
    "果然，让二人痛苦的原因就是真由喜啊……"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ALA01"),"True","lh/OKA_ALA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "MAY03A_OKA0021"
    $ current_voice = "voice/MAY03A_OKA0021.ogg"
    "伦太郎" "「──那么，Christina怎么了？　发生什么事了？」"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0078"
    $ current_voice = "voice/MAY03A_MAY0078.ogg"
    "真由理" "「……那个，完全联系不上她。之前状态也有点奇怪，担心她……在找她」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ALA04"),"True","lh/OKA_ALA04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "MAY03A_OKA0022"
    $ current_voice = "voice/MAY03A_OKA0022.ogg"
    "伦太郎" "「这样啊……」"
    "冈伦移开了目光，叹了口气。"
    "不是吓了一跳，而是果然是这样──这样的表情。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ALA01"),"True","lh/OKA_ALA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "MAY03A_OKA0023"
    $ current_voice = "voice/MAY03A_OKA0023.ogg"
    "伦太郎" "「知道了，我也一起找吧」"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0079"
    $ current_voice = "voice/MAY03A_MAY0079.ogg"
    "真由理" "「不、那个……好吗，冈伦，红莉栖酱的事就交给真由喜了好么？」"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0080"
    $ current_voice = "voice/MAY03A_MAY0080.ogg"
    "真由理" "「真由喜或许帮不上什么忙……」"
    $ stopvoc("OKA")
    play OKA "MAY03A_OKA0024"
    $ current_voice = "voice/MAY03A_OKA0024.ogg"
    "伦太郎" "「你……已经帮了足够的忙了」"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0081"
    $ current_voice = "voice/MAY03A_MAY0081.ogg"
    "真由理" "「是这样吗……」"
    $ stopvoc("OKA")
    play OKA "MAY03A_OKA0025"
    $ current_voice = "voice/MAY03A_OKA0025.ogg"
    "伦太郎" "「嗯，所以，不要说那样的话」"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0082"
    $ current_voice = "voice/MAY03A_MAY0082.ogg"
    "真由理" "「……冈伦」"
    $ stopvoc("OKA")
    play OKA "MAY03A_OKA0026"
    $ current_voice = "voice/MAY03A_OKA0026.ogg"
    "伦太郎" "「──也是啊，这里交给真由理或许比较好一点。她现在应该不想看到我的脸……」"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0083"
    $ current_voice = "voice/MAY03A_MAY0083.ogg"
    "真由理" "「冈伦，跟红莉栖酱吵架了吗？」"
    $ stopvoc("OKA")
    play OKA "MAY03A_OKA0027"
    $ current_voice = "voice/MAY03A_OKA0027.ogg"
    "伦太郎" "「……算是吧、今天傍晚……稍微」"
    "冈伦尴尬地说了出口。"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0084"
    $ current_voice = "voice/MAY03A_MAY0084.ogg"
    "真由理" "「阵雨下得很大吧，没事吧？」"
    $ stopvoc("OKA")
    play OKA "MAY03A_OKA0028"
    $ current_voice = "voice/MAY03A_OKA0028.ogg"
    "伦太郎" "「嗯……还好」"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0085"
    $ current_voice = "voice/MAY03A_MAY0085.ogg"
    "真由理" "「冈伦和红莉栖酱也在秋叶原吗？」"
    $ stopvoc("OKA")
    play OKA "MAY03A_OKA0029"
    $ current_voice = "voice/MAY03A_OKA0029.ogg"
    "伦太郎" "「嗯」"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0086"
    $ current_voice = "voice/MAY03A_MAY0086.ogg"
    "真由理" "「这样啊……」"
    $ stopvoc("OKA")
    play OKA "MAY03A_OKA0030"
    $ current_voice = "voice/MAY03A_OKA0030.ogg"
    "伦太郎" "「…………」"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0087"
    $ current_voice = "voice/MAY03A_MAY0087.ogg"
    "真由理" "「…………」"
    "对话到那里就断了。"
    "想要问他们去哪儿了，但不知怎的难以开口，于是就不问了。"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0088"
    $ current_voice = "voice/MAY03A_MAY0088.ogg"
    "真由理" "「吵架是不行的哦？　必须得好好相处」"
    $ stopvoc("OKA")
    play OKA "MAY03A_OKA0031"
    $ current_voice = "voice/MAY03A_OKA0031.ogg"
    "伦太郎" "「我跟Christina之间吵架是默认设定，这么说也不为过」"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0089"
    $ current_voice = "voice/MAY03A_MAY0089.ogg"
    "真由理" "「这是因为冈伦总是把红莉栖酱戏弄得太过火了哦？」"
    $ stopvoc("OKA")
    play OKA "MAY03A_OKA0032"
    $ current_voice = "voice/MAY03A_OKA0032.ogg"
    "伦太郎" "「那家伙，稍微戏弄一下，就发起脾气反驳回来。在美国长大，却听不懂美式笑话，真是太不像话了！」"
    "冈伦摆着与往常的毒舌不相搭的非常温和的表情，让人吓了一跳。"
    $ stopvoc("OKA")
    play OKA "MAY03A_OKA0033"
    $ current_voice = "voice/MAY03A_OKA0033.ogg"
    "伦太郎" "「──总之……这件事就交给你了」"
    "「交给你了」"
    "冈伦这短短的一句话，让真由喜有了精神和勇气。"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0090"
    $ current_voice = "voice/MAY03A_MAY0090.ogg"
    "真由理" "「嗯，承担了重大的任务。」"
    $ stopvoc("OKA")
    play OKA "MAY03A_OKA0034"
    $ current_voice = "voice/MAY03A_OKA0034.ogg"
    "伦太郎" "「啊啊，那家伙就拜托你了……」"
    "冈伦紧紧地握住了真由喜的双手。"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0091"
    $ current_voice = "voice/MAY03A_MAY0091.ogg"
    "真由理" "「知道了，红莉栖酱就交给真由喜了！」"
    "真由喜回握了那双大大的手，带着满面的笑容说罢，冈伦带着淡淡的微笑点了点头。"
    "真由喜还是希望冈伦脸上带着笑容。"
    "感觉要是为了这个，不管什么事都能做得到。"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA01"),"True","lh/OKA_ASA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0092"
    $ current_voice = "voice/MAY03A_MAY0092.ogg"
    "真由理" "「那么，找到了红莉栖酱之后就跟你联系」"
    $ stopvoc("OKA")
    play OKA "MAY03A_OKA0035"
    $ current_voice = "voice/MAY03A_OKA0035.ogg"
    "伦太郎" "「嗯，知道了。要是她到Ｌａｂ来了，我也会联系你的」"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0093"
    $ current_voice = "voice/MAY03A_MAY0093.ogg"
    "真由理" "「拜托了，那么再见啦。嘟嘟噜」"
    window hide


    $ loadBG(2,"IBGX033")



    "比起什么都做不到，还是身上有任务更让人高兴。"
    "要是能稍微帮上点冈伦的忙就好了。"
    "一边想着，一边跑下了大楼的楼梯。"
    hide screen phoneSD1
    window hide

    stop bgm 



    $ loadBG(0,"BG18N3")


    show screen phoneSD1
    play bgm "FD2BGM01"
    "与冈伦分别，再一次仔细地在Ｌａｂ和ＭａｙＱｕｅｅｎ＋Ｎｙａ²的周围试着寻找，但是没有找到红莉栖酱。"
    "电话也依然打不通。"
    "说好找到红莉栖酱就来联系的桶子君和冈伦也没有来电话。"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0094"
    $ current_voice = "voice/MAY03A_MAY0094.ogg"
    "真由理" "「红莉栖酱，到哪儿去了呢。这么找也没有找到的话，难道说不在秋叶原了吗」"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0095"
    $ current_voice = "voice/MAY03A_MAY0095.ogg"
    "真由理" "「但是，傍晚的时候她似乎还在秋叶原，而且她总是在Ｌａｂ留到很晚，现在应该还在秋叶原……」"

    $ targetmailid = gc["ScriptMacros"]["RM_MAY_RECV_OKA01_01"]

    $ LR_RM_CHANCE=3
    call CHECK_RM_RECEIVE
    "环视了一下周围。"
    call CHECK_RM_RECEIVE
    "夜晚的秋叶原跟白天截然不同，路上的人少了许多。"
    call CHECK_RM_RECEIVE
    "所以要比白天好找许多。"

    call CHECK_RM_RECEIVE
    "但是却找不到红莉栖酱的身影。"

    $ gd["RCVmailData"][gc["ScriptMacros"]["RM_MAY_RECV_OKA01_01"]]["late"]=True
    $ lml.append(gc["ScriptMacros"]["RM_MAY_RECV_OKA01_01"])

    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0096"
    $ current_voice = "voice/MAY03A_MAY0096.ogg"
    "真由理" "「秋叶原明明没那么大啊，为什么偏偏就是今天见不着她的人啊……」"
    "昨天在那么混杂的大街上偶然碰到，就好像是做梦一样。"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0097"
    $ current_voice = "voice/MAY03A_MAY0097.ogg"
    "真由理" "「都到这个地步了还见不到……红莉栖酱，难道真的消失了吗……」"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0098"
    $ current_voice = "voice/MAY03A_MAY0098.ogg"
    "真由理" "「不、没那种事……红莉栖酱不会消失的。冈伦都那样的努力了，肯定没问题的」"
    "慌张地打消了这不好的念头。"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0099"
    $ current_voice = "voice/MAY03A_MAY0099.ogg"
    "真由理" "「明明不是不安的时候──」"
    window hide


    $ loadBG(2,"IBGX072")



    hide screen phonebtn
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0100"
    $ current_voice = "voice/MAY03A_MAY0100.ogg"
    "真由理" "「想着想要见面的两个人，会不可思议地见面，奶奶就像口头禅一样说过这句话来着吧……」"
    "紧紧地握着怀酱，叹了口气。"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0101"
    $ current_voice = "voice/MAY03A_MAY0101.ogg"
    "真由理" "「……只有一个人想着想要见面，难道不行吗？」"
    "希望红莉栖酱也想着想要与真由喜见面。"
    window hide


    $ loadBG(2,"BG18N3")



    show screen phonebtn

    $ targetmailid = cml.setdefault("RM_MAY_SEND_OKA01","")

    $ LR_RM_CHANCE=1
    call CHECK_RM_RECEIVE
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0102"
    $ current_voice = "voice/MAY03A_MAY0102.ogg"
    "真由理" "「既然承担了任务，就一定要努力」"

    call CHECK_RM_RECEIVE

    $ gd["RCVmailData"][gc["ScriptMacros"]["RM_MAY_RECV_OKA02_01"]]["late"]=True
    $ lml.append(gc["ScriptMacros"]["RM_MAY_RECV_OKA02_01"])

    "酸痛的腿又有了精神，迈出了步子开始寻找红莉栖酱。"
    hide screen phoneSD1
    window hide
    stop bgm 



    $ loadBG(0,"BG20N")


    show screen phoneSD1
    play bgm "FD2BGM08"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0103"
    $ current_voice = "voice/MAY03A_MAY0103.ogg"
    "真由理" "「呼、居然这么难找……只能认为是被诅咒了啊……」"
    "不禁开始叫苦。"
    "在秋叶原中转了好几圈，试着去寻找红莉栖酱，但不管怎么样都找不到红莉栖酱。"
    "马上就要到第二天了。"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0104"
    $ current_voice = "voice/MAY03A_MAY0104.ogg"
    "真由理" "「要是在末班车之前都找不到的话，就只能明天再找了啊……」"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0105"
    $ current_voice = "voice/MAY03A_MAY0105.ogg"
    "真由理" "「到了明天，或许手机就能打通了……」"
    "尽可能乐观地去考虑。"
    "但是，焦虑并没有消失，稍许的拖延也是不行的。"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0106"
    $ current_voice = "voice/MAY03A_MAY0106.ogg"
    "真由理" "「……总之、现在真由喜要把能做的事都做了，因为不想后悔」"
    "抑制住沮丧的心情，抬起了头。"
    stop bgm 
    "在那时──"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_UPX"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_UPX"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_UPX"])
    "目光被{color=#f00}ＵＰＸ{/color}的天桥吸引住了。"
    "栗色的头发，改装了的制服──虽然距离远，但看错是不可能的。"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0107"
    $ current_voice = "voice/MAY03A_MAY0107.ogg"
    "真由理" "「──！？　红莉栖酱！？」"
    "红莉栖酱正在呆呆地从天桥上向下看。"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0108"
    $ current_voice = "voice/MAY03A_MAY0108.ogg"
    "真由理" "「红莉栖酱！　喂──！　红莉栖酱！」"
    "大大地挥着手，喊着红莉栖酱的名字。"
    "但是红莉栖酱没有注意到真由喜。"
    "依然是在天桥上呆呆地向下望着，一动也不动。"
    "天桥下面的道路上，车正在以飞快的速度行驶着。"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0109"
    $ current_voice = "voice/MAY03A_MAY0109.ogg"
    "真由理" "「红莉栖……酱？」"
    play bgm "FD2BGM04"
    "红莉栖酱叹了口气，仿佛要跳向在天桥下面行驶的车辆一样。"
    "下个瞬间，又开始忘我地攀登通往天桥上方的楼梯。"
    window hide



    $ loadBG(2,"BG24N")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASC06"),"True","lh/CRS_ASC06a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    "红莉栖酱的眼神迷离，哪里都没有看的样子。"
    "将手指放在嘴唇上，呆呆地望着天空。"
    "就好像没有灵魂的人偶一样。"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0110"
    $ current_voice = "voice/MAY03A_MAY0110.ogg"
    "真由理" "「……、红莉栖酱！」"
    "以最大速度奔跑，撞在了红莉栖酱身上。"
    window hide
    play se "SGSE015"




    $ loadBG(0,"BG_BLACK")

    hide screen phonebtn
    $ stopvoc("CRS")
    play CRS "MAY03A_CRS0001"
    $ current_voice = "voice/MAY03A_CRS0001.ogg"
    "红莉栖" "「……呀！？」"
    "抱在一起，一同倒在了天桥上。"
    $ stopvoc("CRS")
    play CRS "MAY03A_CRS0002"
    $ current_voice = "voice/MAY03A_CRS0002.ogg"
    "红莉栖" "「真……真由理？」"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0111"
    $ current_voice = "voice/MAY03A_MAY0111.ogg"
    "真由理" "「红莉栖酱！　不行，不要轻生！」"
    "紧紧地抱着红莉栖酱的身体，不让她离开。"

    stop bgm 
    $ stopvoc("CRS")
    play CRS "MAY03A_CRS0003"
    $ current_voice = "voice/MAY03A_CRS0003.ogg"
    "红莉栖" "「……哎，啊？　怎、怎么了？　突然之间……」"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0112"
    $ current_voice = "voice/MAY03A_MAY0112.ogg"
    "真由理" "「怎么？　可、可是……你刚才看起来好像要跳下去一样。想着必须得拦住你……」"
    window hide

    $ loadBG(0,"BG24NS1")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ALC05"),"True","lh/CRS_ALC05a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    hide screen phonebtn
    show screen phoneSD1
    $ stopvoc("CRS")
    play CRS "MAY03A_CRS0004"
    $ current_voice = "voice/MAY03A_CRS0004.ogg"
    "红莉栖" "「哎？　难道说，真由理，你觉得我是想要自杀？」"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0113"
    $ current_voice = "voice/MAY03A_MAY0113.ogg"
    "真由理" "「嗯、嗯……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ALC06"),"True","lh/CRS_ALC06a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MAY03A_CRS0005"
    $ current_voice = "voice/MAY03A_CRS0005.ogg"
    "红莉栖" "「哎呀，我怎么可能做那种事呢。不过我确实是在考虑事情……」"
    play bgm "BGM13"

    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0114"
    $ current_voice = "voice/MAY03A_MAY0114.ogg"
    "真由理" "「这样啊，那么就是真由喜误会了呢，太好了」"
    "松了口气，全身都失去了力量一样。"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0115"
    $ current_voice = "voice/MAY03A_MAY0115.ogg"
    "真由理" "「红莉栖酱，看上去很没有精神，而且还根本联系不上，真由喜特别的担心」"
    $ stopvoc("CRS")
    play CRS "MAY03A_CRS0006"
    $ current_voice = "voice/MAY03A_CRS0006.ogg"
    "红莉栖" "「这样啊。抱歉……没有功夫去在意手机……」"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0116"
    $ current_voice = "voice/MAY03A_MAY0116.ogg"
    "真由理" "「没关系，能够见到你真是太好了」"
    $ stopvoc("CRS")
    play CRS "MAY03A_CRS0007"
    $ current_voice = "voice/MAY03A_CRS0007.ogg"
    "红莉栖" "「该不会、真由理……你一直在找我？」"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0117"
    $ current_voice = "voice/MAY03A_MAY0117.ogg"
    "真由理" "「嗯」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ALC04"),"True","lh/CRS_ALC04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MAY03A_CRS0008"
    $ current_voice = "voice/MAY03A_CRS0008.ogg"
    "红莉栖" "「怎么会……都到这么晚了！？　已经是半夜了啊……」"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0118"
    $ current_voice = "voice/MAY03A_MAY0118.ogg"
    "真由理" "「嘿嘿，因为真由喜担心红莉栖酱。就稍微加油了一下」"
    $ stopvoc("CRS")
    play CRS "MAY03A_CRS0009"
    $ current_voice = "voice/MAY03A_CRS0009.ogg"
    "红莉栖" "「……真由理长得这么可爱，一个人深更半夜地在外面走是不行的哦。要是被坏人盯上了……会很危险的……」"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0119"
    $ current_voice = "voice/MAY03A_MAY0119.ogg"
    "真由理" "「红莉栖酱也是，这么晚了一个人走是不行的哦？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ALC02"),"True","lh/CRS_ALC02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MAY03A_CRS0010"
    $ current_voice = "voice/MAY03A_CRS0010.ogg"
    "红莉栖" "「我、我……跟真由理不同，我又不可爱。没关系的」"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0120"
    $ current_voice = "voice/MAY03A_MAY0120.ogg"
    "真由理" "「不、不行的」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ALC05"),"True","lh/CRS_ALC05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MAY03A_CRS0011"
    $ current_voice = "voice/MAY03A_CRS0011.ogg"
    "红莉栖" "「……真由理」"
    "红莉栖酱苦笑了一下，温柔地抚摸着真由喜的后背。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ALC03"),"True","lh/CRS_ALC03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MAY03A_CRS0012"
    $ current_voice = "voice/MAY03A_CRS0012.ogg"
    "红莉栖" "「……谢谢你来找我」"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0121"
    $ current_voice = "voice/MAY03A_MAY0121.ogg"
    "真由理" "「没关系，因为我们是朋友。担心也是当然的」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ALC01"),"True","lh/CRS_ALC01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MAY03A_CRS0013"
    $ current_voice = "voice/MAY03A_CRS0013.ogg"
    "红莉栖" "「对你来说担心是当然的……从小到大都没有人来找过我……对我来说并不是当然的」"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0122"
    $ current_voice = "voice/MAY03A_MAY0122.ogg"
    "真由理" "「红莉栖酱……」"
    $ stopvoc("CRS")
    play CRS "MAY03A_CRS0014"
    $ current_voice = "voice/MAY03A_CRS0014.ogg"
    "红莉栖" "「所有人都觉得我变成什么样都无所谓。甚至连我的亲爸爸都无视我──」"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0123"
    $ current_voice = "voice/MAY03A_MAY0123.ogg"
    "真由理" "「真由喜不会觉得红莉栖酱变成什么样都无所谓。菲利斯、冈伦……还有Ｌａｂ的大家都是这样想的！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ALC06"),"True","lh/CRS_ALC06a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    "真由喜不由得争辩了起来，红莉栖酱移开了望向真由喜的目光，痛苦地望向了远处。"
    "在短暂的沉默之后，苦恼地深深叹了一口气。"
    $ stopvoc("CRS")
    play CRS "MAY03A_CRS0015"
    $ current_voice = "voice/MAY03A_CRS0015.ogg"
    "红莉栖" "「真由理……真是个不得了的好孩子啊。我明明已经没有脸再见真由理了……」"
    "红莉栖咬着嘴唇低着头。"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0124"
    $ current_voice = "voice/MAY03A_MAY0124.ogg"
    "真由理" "「不要说这种话」"
    "再一次紧紧地抱住红莉栖酱纤细的身体。"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0125"
    $ current_voice = "voice/MAY03A_MAY0125.ogg"
    "真由理" "「不管发生什么，我们都是朋友──没事的，一点小事是无法左右人生的」"
    $ stopvoc("CRS")
    play CRS "MAY03A_CRS0016"
    $ current_voice = "voice/MAY03A_CRS0016.ogg"
    "红莉栖" "「……真由理」"
    "怯生生地抬起了头，发现红莉栖酱稍微摇了摇头。"
    $ stopvoc("CRS")
    play CRS "MAY03A_CRS0017"
    $ current_voice = "voice/MAY03A_CRS0017.ogg"
    "红莉栖" "「但要不是一点小事的话，该怎么办呢？」"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0126"
    $ current_voice = "voice/MAY03A_MAY0126.ogg"
    "真由理" "「就算那样……没事的，因为没有那种程度的觉悟，是不会成为朋友的」"
    $ stopvoc("CRS")
    play CRS "MAY03A_CRS0018"
    $ current_voice = "voice/MAY03A_CRS0018.ogg"
    "红莉栖" "「……觉悟」"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0127"
    $ current_voice = "voice/MAY03A_MAY0127.ogg"
    "真由理" "「比起温柔的谎言，即使是痛苦的事实，如实地说出来，也会让人高兴的吧？　比起瞒着不说……要好得多啊……」"
    "脑中浮想着冈伦的表情，同时试图使红莉栖同意。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ALC01"),"True","lh/CRS_ALC01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MAY03A_CRS0019"
    $ current_voice = "voice/MAY03A_CRS0019.ogg"
    "红莉栖" "「……是么，真由喜……很坚强呢」"
    "红莉栖抱着自己的胳膊，像是在劝说自己一样念叨着。"
    "两个人瞒着真由喜的秘密。"
    "冈伦没有说出来，不过红莉栖酱说不定愿意说出来。"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0128"
    $ current_voice = "voice/MAY03A_MAY0128.ogg"
    "真由理" "「红莉栖酱，还记得之前一起过夜的约定吗？」"
    $ stopvoc("CRS")
    play CRS "MAY03A_CRS0020"
    $ current_voice = "voice/MAY03A_CRS0020.ogg"
    "红莉栖" "「嗯，当然。当初说的是我住的宾馆，不是什么太好的宾馆，如果你愿意的话就行，对吧？」"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0129"
    $ current_voice = "voice/MAY03A_MAY0129.ogg"
    "真由理" "「嗯，就算宾馆不好也完全没关系。要想好好说话的话，一起睡一晚上是最好的。那个约定，现在兑现不行吗？　要是不麻烦的话……」"
    $ stopvoc("CRS")
    play CRS "MAY03A_CRS0021"
    $ current_voice = "voice/MAY03A_CRS0021.ogg"
    "红莉栖" "「……是啊。要是错过今晚的话……或许就很难了……」"
    "红莉栖酱思考了一小会儿之后，点了点头。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ALC03"),"True","lh/CRS_ALC03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MAY03A_CRS0022"
    $ current_voice = "voice/MAY03A_CRS0022.ogg"
    "红莉栖" "「知道了，ＯＫ」"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0130"
    $ current_voice = "voice/MAY03A_MAY0130.ogg"
    "真由理" "「谢谢！」"
    $ stopvoc("CRS")
    play CRS "MAY03A_CRS0023"
    $ current_voice = "voice/MAY03A_CRS0023.ogg"
    "红莉栖" "「不，应该道谢的人是我才对，应该道歉的人，也是我……」"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0131"
    $ current_voice = "voice/MAY03A_MAY0131.ogg"
    "真由理" "「嗯嗯～？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ALC01"),"True","lh/CRS_ALC01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MAY03A_CRS0024"
    $ current_voice = "voice/MAY03A_CRS0024.ogg"
    "红莉栖" "「……没什么」"
    window hide


    $ loadBG(2,"BG24N")




    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASC06"),"True","lh/CRS_ASC06a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    show screen phonebtn
    show screen phoneSD1
    "红莉栖酱站了起来，同时搀扶着真由喜的身体，一起站了起来。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASB01"),"True","lh/CRS_ASB01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MAY03A_CRS0025"
    $ current_voice = "voice/MAY03A_CRS0025.ogg"
    "红莉栖" "「明天……我有点事要早起。所以真由理可能没办法好好休息，即使这样也没关系吗？」"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0132"
    $ current_voice = "voice/MAY03A_MAY0132.ogg"
    "真由理" "「嗯，没关系！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASB08"),"True","lh/CRS_ASB08a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MAY03A_CRS0026"
    $ current_voice = "voice/MAY03A_CRS0026.ogg"
    "红莉栖" "「那么，到我这儿住吧。言出必行，说好的事必须要遵守」"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0133"
    $ current_voice = "voice/MAY03A_MAY0133.ogg"
    "真由理" "「诶嘿嘿，好高兴呢。谢谢！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASB01"),"True","lh/CRS_ASB01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    "必须得给冈伦他们发个邮件，说红莉栖酱已经被顺利地找到了。"
    hide screen phonebtn


    $ targetmailid = gc["ScriptMacros"]["FM_MAY03A_RECV_OKA01"]
    if phonemailring!= "":
        play se phonemailring
    if persistent.skipmail==False:
        $ renpy.choice_for_skipping()
    if targetmailid != "":
        $ RcvMail(targetmailid)
        $ targetmailid=""
    "在这么想的同时，发现有邮件来了。"

    window hide


    hide screen phonebtn
    hide screen phonebtn2
    call read_last_mail



    "看了一下手机，收到了一封邮件。"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0134"
    $ current_voice = "voice/MAY03A_MAY0134.ogg"
    "真由理" "「是冈伦发来的」"
    window hide







    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0135"
    $ current_voice = "voice/MAY03A_MAY0135.ogg"
    "真由理" "「什么呀。还以为是真由喜找到的红莉栖酱呢，居然被冈伦抢先了」"
    window hide
    call hide_phone

    $ stopvoc("CRS")
    play CRS "MAY03A_CRS0027"
    $ current_voice = "voice/MAY03A_CRS0027.ogg"
    "红莉栖" "「刚才的邮件是冈部发的？」"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0136"
    $ current_voice = "voice/MAY03A_MAY0136.ogg"
    "真由理" "「嗯，红莉栖酱，你在来这里之前到Ｌａｂ去了？　见到冈伦了？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASC06"),"True","lh/CRS_ASC06a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "MAY03A_CRS0028"
    $ current_voice = "voice/MAY03A_CRS0028.ogg"
    "红莉栖" "「……算是吧……」"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0137"
    $ current_voice = "voice/MAY03A_MAY0137.ogg"
    "真由理" "「这样啊，冈伦，为什么不马上联系真由喜呢？　都说好了要是红莉栖酱到Ｌａｂ了就联系真由喜」"

    stop bgm 
    $ stopvoc("CRS")
    play CRS "MAY03A_CRS0029"
    $ current_voice = "voice/MAY03A_CRS0029.ogg"
    "红莉栖" "「……这个……那个」"
    "红莉栖酱移开了目光，尴尬地眨着眼睛。"
    "可能跟冈伦之间发生什么了。"
    "看来不想被深究的样子。"
    "飘荡着尴尬的气氛。"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0138"
    $ current_voice = "voice/MAY03A_MAY0138.ogg"
    "真由理" "「嘛，或许只是邮件接收有延迟，冈伦本来发邮件就不仔细」"
    $ stopvoc("CRS")
    play CRS "MAY03A_CRS0030"
    $ current_voice = "voice/MAY03A_CRS0030.ogg"
    "红莉栖" "「……嗯、哎呀……嘛……是啊」"
    "红莉栖酱像是要说什么一样张开了口，但是什么都没有说。"
    $ stopvoc("MAY")
    play MAY "MAY03A_MAY0139"
    $ current_voice = "voice/MAY03A_MAY0139.ogg"
    "真由理" "「那么，红莉栖酱，我们走吧？」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMC05"),"True","lh/CRS_AMC05a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    "为了赶走这尴尬的气氛，我充满精神地说完这句话，然后抱着红莉栖酱的胳膊拉着她走了。"

    hide screen phoneSD1
    window hide





    hide screen phonebtn
    scene expression Solid("000000")  with fade
    return
