label SGFD2_TEN07B:
    $ loadBG(0,"BG58A")




    play se "SGSE017"



    $ date="7/19"
    $ day="TUE"
    show screen phonebtn
    show screen phoneSD1

    $ stopvoc("TEN")
    play TEN "TEN07B_TEN0000"
    $ current_voice = "voice/TEN07B_TEN0000.ogg"
    "天王寺" "「呼，今天也很热呢。那么」"
    "工作暂告一段落了，是不是该去看看楼上那群家伙呢。"
    "新大楼开张才几天，但他们好像已经很开心的样子了。"
    "感觉他们平时不太注意，现在应该在闹腾吧。"
    "让我瞧瞧……"


    $ loadBG(0,"BG59A")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASA01"),"True","lh/CRS_ASA01a~ipad.png") at left as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA01"),"True","lh/OKA_ASA01a~ipad.png") at right as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    play bgm "BGM26"
    $ stopvoc("CRS")
    play CRS "TEN07B_CRS0000"
    $ current_voice = "voice/TEN07B_CRS0000.ogg"
    "红莉栖" "「冈部，那今天我就做到这里，先告辞了」"
    $ stopvoc("OKA")
    play OKA "TEN07B_OKA0000"
    $ current_voice = "voice/TEN07B_OKA0000.ogg"
    "伦太郎" "「啊啊，辛苦了。交给你的资料记得看一眼」"
    window hide
    hide lh6  with dissolve

    hide lh7 
    show expression ConditionSwitch("renpy.music.get_playing(channel='RUK')",DynamicDisplayable(mouthanime,"RUK_CSB01"),"True","lh/RUK_CSB01a~ipad.png") at right as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("RUK")
    play RUK "TEN07B_RUK0000"
    $ current_voice = "voice/TEN07B_RUK0000.ogg"
    "琉华" "「牧濑，记得打了卡再回去哦」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASA07"),"True","lh/CRS_ASA07a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "TEN07B_CRS0001"
    $ current_voice = "voice/TEN07B_CRS0001.ogg"
    "红莉栖" "「等等冈部，打卡是什么鬼？又不是真正的公司」"
    window hide
    hide lh7 

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA01"),"True","lh/OKA_ASA01a~ipad.png") at right as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "TEN07B_OKA0001"
    $ current_voice = "voice/TEN07B_OKA0001.ogg"
    "伦太郎" "「这也是没办法的呀。进来的时候就有那个嘛。所以想先试试。」"

    hide lh8 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA02"),"True","lh/DAR_ASA02a~ipad.png") at right_q2 as lh8 zorder (10-8) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_OTSU"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_OTSU"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_OTSU"])
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_SHACHIKU"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_SHACHIKU"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_SHACHIKU"])

    $ stopvoc("DAR")
    play DAR "TEN07B_DAR0000"
    $ current_voice = "voice/TEN07B_DAR0000.ogg"
    "至" "「企业战士、{color=#f00}乙{/color}。我们才刚刚登上名为{color=#f00}社畜{/color}的坡道呢」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh7 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA01"),"True","lh/MAY_CSA01a~ipad.png") at left as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh8 
    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_DSA02"),"True","lh/FEI_DSA02a~ipad.png") at right as lh8 zorder (10-8) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "TEN07B_MAY0000"
    $ current_voice = "voice/TEN07B_MAY0000.ogg"
    "真由理" "「真由喜一直忘记上班之前要打卡。打工的时候明明不会忘记的说」"
    $ stopvoc("FEI")
    play FEI "TEN07B_FEI0000"
    $ current_voice = "voice/TEN07B_FEI0000.ogg"
    "菲利斯" "「红喵，回去之后不和菲利斯来一杯喵？……只是喝茶啦喵」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASB09"),"True","lh/CRS_ASB09a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "TEN07B_CRS0002"
    $ current_voice = "voice/TEN07B_CRS0002.ogg"
    "红莉栖" "「哈，总感觉好像真变成工薪族了」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh7 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MOE')",DynamicDisplayable(mouthanime,"MOE_ASB01"),"True","lh/MOE_ASB01a~ipad.png") at center as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MOE")
    play MOE "TEN07B_MOE0000"
    $ current_voice = "voice/TEN07B_MOE0000.ogg"
    "萌郁" "「没有工薪的……工薪族」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    "唔，看这样子，似乎不是很有意思啊。"
    "再看看吧。"

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA04"),"True","lh/OKA_ASA04a~ipad.png") at left as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh8 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASB01"),"True","lh/DAR_ASB01a~ipad.png") at right as lh8 zorder (10-8) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "TEN07B_OKA0002"
    $ current_voice = "voice/TEN07B_OKA0002.ogg"
    "伦太郎" "「喂，桶子。这里是你把果汁踢翻了吧？会留下印渍的呀。」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASB04"),"True","lh/DAR_ASB04a~ipad.png") as lh8 zorder (10-8) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "TEN07B_DAR0001"
    $ current_voice = "voice/TEN07B_DAR0001.ogg"
    "至" "「诶，这种事情，怎么都好吧？以前不是完全不在意的么」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA03"),"True","lh/OKA_ASA03a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "TEN07B_OKA0003"
    $ current_voice = "voice/TEN07B_OKA0003.ogg"
    "伦太郎" "「以前是因为一直都很脏所以无所谓。现在是新的了，不该注意一些吗」"

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSB01"),"True","lh/MAY_CSB01a~ipad.png") at left_q2 as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "TEN07B_MAY0001"
    $ current_voice = "voice/TEN07B_MAY0001.ogg"
    "真由理" "「嗯，冈伦，明明自己的房间不怎么打扫，对于Ｌａｂ却很在意呢」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA04"),"True","lh/OKA_ASA04a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "TEN07B_OKA0004"
    $ current_voice = "voice/TEN07B_OKA0004.ogg"
    "伦太郎" "「咕，那个归那个，这个归这个。还有脏不脏是和周围环境比较才能决定的啦」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASA01"),"True","lh/CRS_ASA01a~ipad.png") at left as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh7 
    show expression ConditionSwitch("renpy.music.get_playing(channel='RUK')",DynamicDisplayable(mouthanime,"RUK_CSB01"),"True","lh/RUK_CSB01a~ipad.png") at right as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("RUK")
    play RUK "TEN07B_RUK0001"
    $ current_voice = "voice/TEN07B_RUK0001.ogg"
    "琉华" "「那个……虽然房间之间有墙壁啦，但把里面的房间也用起来是不是会更好些？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASB06"),"True","lh/CRS_ASB06a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "TEN07B_CRS0003"
    $ current_voice = "voice/TEN07B_CRS0003.ogg"
    "红莉栖" "「虽说就算现在这样也比之前的空间大了」"
    $ stopvoc("RUK")
    play RUK "TEN07B_RUK0002"
    $ current_voice = "voice/TEN07B_RUK0002.ogg"
    "琉华" "「是的呢，但‘难得有机会’，所以就这样想了」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh7 
    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_DSA03"),"True","lh/FEI_DSA03a~ipad.png") at right as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh8 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MOE')",DynamicDisplayable(mouthanime,"MOE_ASB03"),"True","lh/MOE_ASB03a~ipad.png") at left as lh8 zorder (10-8) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FEI")
    play FEI "TEN07B_FEI0001"
    $ current_voice = "voice/TEN07B_FEI0001.ogg"
    "菲利斯" "「是的喵。感觉有好多都没造出来挺可惜的喵。淋浴室来澡堂啦虽然都有提出，但没能设计进去」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='MOE')",DynamicDisplayable(mouthanime,"MOE_ASB02"),"True","lh/MOE_ASB02a~ipad.png") as lh8 zorder (10-8) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MOE")
    play MOE "TEN07B_MOE0001"
    $ current_voice = "voice/TEN07B_MOE0001.ogg"
    "萌郁" "「桑拿室……也很想要。还有……酒窖」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA03"),"True","lh/OKA_ASA03a~ipad.png") at center as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "TEN07B_OKA0005"
    $ current_voice = "voice/TEN07B_OKA0005.ogg"
    "伦太郎" "「喂喂你们这些家伙，别废话了赶紧工作吧！」"
    $ stopvoc("OKA")
    play OKA "TEN07B_OKA0006"
    $ current_voice = "voice/TEN07B_OKA0006.ogg"
    "伦太郎" "「Ｌａｂ的环境可是十分严峻的。要尽快开发出最新的未来道具，将其商业化，确保热销才行」"

    hide lh8 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASB04"),"True","lh/DAR_ASB04a~ipad.png") at right_t as lh8 zorder (10-8) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "TEN07B_DAR0002"
    $ current_voice = "voice/TEN07B_DAR0002.ogg"
    "至" "「说起来冈伦，什么时候对于商业化这么热心了？搬到新Ｌａｂ以后受刺激了么？」"

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASB04"),"True","lh/CRS_ASB04a~ipad.png") at left_t as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "TEN07B_CRS0004"
    $ current_voice = "voice/TEN07B_CRS0004.ogg"
    "红莉栖" "「冈部也是，也不要成天无所事事了，想想下一个计划的内容吧？你写的文件里，不切实际的东西太多了」"
    window hide
    hide lh8 

    hide lh7 
    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_DSC03"),"True","lh/FEI_DSC03a~ipad.png") at right_t as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FEI")
    play FEI "TEN07B_FEI0002"
    $ current_voice = "voice/TEN07B_FEI0002.ogg"
    "菲利斯" "「是的喵。公司的运作可不是Ｆａｎｔａｓｙ喵。好好地正视现实吧喵」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA04"),"True","lh/OKA_ASA04a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "TEN07B_OKA0007"
    $ current_voice = "voice/TEN07B_OKA0007.ogg"
    "伦太郎" "「什么？没想到居然被菲利斯说要正视现实」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_DSC04"),"True","lh/FEI_DSC04a~ipad.png") as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FEI")
    play FEI "TEN07B_FEI0003"
    $ current_voice = "voice/TEN07B_FEI0003.ogg"
    "菲利斯" "「说起来这个月『ＭａｙＱｕｅｅｎ＋Ｎｙａ²』的客人数量稍微有些下降了喵……要考虑对策所以借我用一下ＰＣ喵」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh8 
    show expression ConditionSwitch("renpy.music.get_playing(channel='RUK')",DynamicDisplayable(mouthanime,"RUK_CSA01"),"True","lh/RUK_CSA01a~ipad.png") at center as lh8 zorder (10-8) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("RUK")
    play RUK "TEN07B_RUK0003"
    $ current_voice = "voice/TEN07B_RUK0003.ogg"
    "琉华" "「那个……菲利斯小姐？感觉在Ｌａｂ里面考虑这样的事情的话实在是太紧张了……」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh7 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MOE')",DynamicDisplayable(mouthanime,"MOE_ASB01"),"True","lh/MOE_ASB01a~ipad.png") at center as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MOE")
    play MOE "TEN07B_MOE0002"
    $ current_voice = "voice/TEN07B_MOE0002.ogg"
    "萌郁" "「我也……经常有这种时候。感觉……头脑里满是烦恼」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASB06"),"True","lh/CRS_ASB06a~ipad.png") at left as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA05"),"True","lh/OKA_ASA05a~ipad.png") at right as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "TEN07B_OKA0008"
    $ current_voice = "voice/TEN07B_OKA0008.ogg"
    "伦太郎" "「哼，别把这件事和普通的私事混为一谈了呐，指压师。这边可是关系到Ｌａｂ命运的大事呢。」"
    $ stopvoc("CRS")
    play CRS "TEN07B_CRS0005"
    $ current_voice = "voice/TEN07B_CRS0005.ogg"
    "红莉栖" "「所以你就给我早上早点来啊。连个石头都做不出来，你还好意思出任这样重要的职位？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA03"),"True","lh/OKA_ASA03a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "TEN07B_OKA0009"
    $ current_voice = "voice/TEN07B_OKA0009.ogg"
    "伦太郎" "「这算什么！是对本大爷有意见嘛」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh8 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA04"),"True","lh/MAY_CSA04a~ipad.png") at center as lh8 zorder (10-8) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "TEN07B_MAY0002"
    $ current_voice = "voice/TEN07B_MAY0002.ogg"
    "真由理" "「大家，不可以吵架哦」"

    stop bgm 
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    play bgm "BGM23"
    "什么呀这是。"
    "说是闹腾还不如说是在吵架。"
    "这是怎么回事。"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASB04"),"True","lh/CRS_ASB04a~ipad.png") at left as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA03"),"True","lh/OKA_ASA03a~ipad.png") at right as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "TEN07B_CRS0006"
    $ current_voice = "voice/TEN07B_CRS0006.ogg"
    "红莉栖" "「大概你是受新Ｌａｂ影响太严重了吧。怎么突然变得这么认真感觉像个傻瓜一样」"
    $ stopvoc("OKA")
    play OKA "TEN07B_OKA0010"
    $ current_voice = "voice/TEN07B_OKA0010.ogg"
    "伦太郎" "「就算是我，也不是说会想做什么就去做什么的。这一切都是因为这幢死板的大楼啊」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASB05"),"True","lh/CRS_ASB05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "TEN07B_CRS0007"
    $ current_voice = "voice/TEN07B_CRS0007.ogg"
    "红莉栖" "「所以说是大楼的原因？但不是你一直在那里说重建会更好么！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA05"),"True","lh/OKA_ASA05a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)





    $ stopvoc("OKA")
    play OKA "TEN07B_OKA0011"
    $ current_voice = "voice/TEN07B_OKA0011.ogg"
    "伦太郎" "「你也赞成了吧。哼，助手哦。你的脑袋和这幢大楼一样硬了呢」"


    $ stopvoc("CRS")
    play CRS "TEN07B_CRS0008"
    $ current_voice = "voice/TEN07B_CRS0008.ogg"
    "红莉栖" "「谁的脑袋和大楼一样啊！能别这么说吗？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA03"),"True","lh/OKA_ASA03a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "TEN07B_OKA0012"
    $ current_voice = "voice/TEN07B_OKA0012.ogg"
    "伦太郎" "「差不多嘛，都挺硬的」"
    $ stopvoc("CRS")
    play CRS "TEN07B_CRS0009"
    $ current_voice = "voice/TEN07B_CRS0009.ogg"
    "红莉栖" "「你才是呢」"
    $ stopvoc("OKA")
    play OKA "TEN07B_OKA0013"
    $ current_voice = "voice/TEN07B_OKA0013.ogg"
    "伦太郎" "「不—对，是你」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASB04"),"True","lh/CRS_ASB04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "TEN07B_CRS0010"
    $ current_voice = "voice/TEN07B_CRS0010.ogg"
    "红莉栖" "「是你！」"
    $ stopvoc("OKA")
    play OKA "TEN07B_OKA0014"
    $ current_voice = "voice/TEN07B_OKA0014.ogg"
    "伦太郎" "「是你，就是你！」"

    stop bgm 
    $ stopvoc("TEN")
    play TEN "TEN07B_TEN0001"
    $ current_voice = "voice/TEN07B_TEN0001.ogg"
    "天王寺" "「……喂」"
    $ stopvoc("OKA")
    play OKA "TEN07B_OKA0015"
    $ current_voice = "voice/TEN07B_OKA0015.ogg"
    "伦太郎" "「什么啊，现在忙着呢」"





    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASA07"),"True","lh/CRS_ASA07a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)







    $ stopvoc("CRS")
    play CRS "TEN07B_CRS0011"
    $ current_voice = "voice/TEN07B_CRS0011.ogg"
    "红莉栖" "「是啊？外人不要插嘴……咦，诶？」"



    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA04"),"True","lh/OKA_ASA04a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "TEN07B_OKA0016"
    $ current_voice = "voice/TEN07B_OKA0016.ogg"
    "伦太郎" "「Ｍ、Ｍｒ．布朗！？　为什么在这里！」"
    $ stopvoc("TEN")
    play TEN "TEN07B_TEN0002"
    $ current_voice = "voice/TEN07B_TEN0002.ogg"
    "天王寺" "「刚才好像听到了什么不能忽视的话呢。这大楼怎么了？」"
    $ stopvoc("OKA")
    play OKA "TEN07B_OKA0017"
    $ current_voice = "voice/TEN07B_OKA0017.ogg"
    "伦太郎" "「不是，那个是……用来反击的话吧……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASC05"),"True","lh/CRS_ASC05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "TEN07B_CRS0012"
    $ current_voice = "voice/TEN07B_CRS0012.ogg"
    "红莉栖" "「是啊是啊。不是真心话……的说」"
    $ stopvoc("TEN")
    play TEN "TEN07B_TEN0003"
    $ current_voice = "voice/TEN07B_TEN0003.ogg"
    "天王寺" "「给我出去」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA01"),"True","lh/OKA_ASA01a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "TEN07B_OKA0018"
    $ current_voice = "voice/TEN07B_OKA0018.ogg"
    "伦太郎" "「诶？」"
    play bgm "BGM08"
    $ stopvoc("TEN")
    play TEN "TEN07B_TEN0004"
    $ current_voice = "voice/TEN07B_TEN0004.ogg"
    "天王寺" "「全部出去！现在就出去！还敢在我面前露脸的话马上解决你哦！！！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA04"),"True","lh/OKA_ASA04a~ipad.png") as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "TEN07B_OKA0019"
    $ current_voice = "voice/TEN07B_OKA0019.ogg"
    "伦太郎" "「唔啊啊啊啊啊啊，全员撤退！快点，真由理」"
    $ stopvoc("MAY")
    play MAY "TEN07B_MAY0003"
    $ current_voice = "voice/TEN07B_MAY0003.ogg"
    "真由理" "「嗯，嗯……」"
    window hide

    stop bgm
    hide lh5 
    hide lh6 
    with dissolve




    play bgm "FD2BGM05"
    $ stopvoc("TEN")
    play TEN "TEN07B_TEN0005"
    $ current_voice = "voice/TEN07B_TEN0005.ogg"
    "天王寺" "「切！那群家伙说什么呢！」"
    "肆意践踏我的好意。"
    "对这栋大楼有什么不满吗？"
    "和之前比起来漂亮了好几倍吧。"
    "就算那样，那些家伙还是那么说了。"

    $ targetmailid = gc["ScriptMacros"]["RM_TEN_RECV_MOE03_01"]

    $ LR_RM_CHANCE=15

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='NAE')",DynamicDisplayable(mouthanime,"NAE_AMA01"),"True","lh/NAE_AMA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    call CHECK_RM_RECEIVE
    $ stopvoc("NAE")
    play NAE "TEN07B_NAE0000"
    $ current_voice = "voice/TEN07B_NAE0000.ogg"
    "绹" "「……爸爸」"
    call CHECK_RM_RECEIVE
    $ stopvoc("TEN")
    play TEN "TEN07B_TEN0006"
    $ current_voice = "voice/TEN07B_TEN0006.ogg"
    "天王寺" "「哦，是绹吗」"
    call CHECK_RM_RECEIVE
    $ stopvoc("NAE")
    play NAE "TEN07B_NAE0001"
    $ current_voice = "voice/TEN07B_NAE0001.ogg"
    "绹" "「刚才好像有什么很响的声音，大家在哪里？」"
    call CHECK_RM_RECEIVE
    $ stopvoc("TEN")
    play TEN "TEN07B_TEN0007"
    $ current_voice = "voice/TEN07B_TEN0007.ogg"
    "天王寺" "「……我让他们全部出去了。２楼还是变回原来空空的家吧」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='NAE')",DynamicDisplayable(mouthanime,"NAE_AMA05"),"True","lh/NAE_AMA05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    call CHECK_RM_RECEIVE
    $ stopvoc("NAE")
    play NAE "TEN07B_NAE0002"
    $ current_voice = "voice/TEN07B_NAE0002.ogg"
    "绹" "「诶——，为什么呀？」"
    call CHECK_RM_RECEIVE
    $ stopvoc("TEN")
    play TEN "TEN07B_TEN0008"
    $ current_voice = "voice/TEN07B_TEN0008.ogg"
    "天王寺" "「嘛，发生了各种各样的事情啦」"
    call CHECK_RM_RECEIVE
    $ stopvoc("NAE")
    play NAE "TEN07B_NAE0003"
    $ current_voice = "voice/TEN07B_NAE0003.ogg"
    "绹" "「真由理姐姐也不来了吗？」"
    call CHECK_RM_RECEIVE
    $ stopvoc("TEN")
    play TEN "TEN07B_TEN0009"
    $ current_voice = "voice/TEN07B_TEN0009.ogg"
    "天王寺" "「……啊啊，不会再来这里了呢」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='NAE')",DynamicDisplayable(mouthanime,"NAE_AMA03"),"True","lh/NAE_AMA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    call CHECK_RM_RECEIVE
    $ stopvoc("NAE")
    play NAE "TEN07B_NAE0004"
    $ current_voice = "voice/TEN07B_NAE0004.ogg"
    "绹" "「这样啊，真由理姐姐不来的话，又要变得寂寞了哦」"
    call CHECK_RM_RECEIVE
    $ stopvoc("TEN")
    play TEN "TEN07B_TEN0010"
    $ current_voice = "voice/TEN07B_TEN0010.ogg"
    "天王寺" "「呐，绹，还在旧大楼的时候，你是说过感觉缺少了些什么吧？」"
    call CHECK_RM_RECEIVE
    $ stopvoc("TEN")
    play TEN "TEN07B_TEN0011"
    $ current_voice = "voice/TEN07B_TEN0011.ogg"
    "天王寺" "「现在旧大楼变成新大楼了，如何？感觉有些变化了吗」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='NAE')",DynamicDisplayable(mouthanime,"NAE_AMA01"),"True","lh/NAE_AMA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    call CHECK_RM_RECEIVE
    $ stopvoc("NAE")
    play NAE "TEN07B_NAE0005"
    $ current_voice = "voice/TEN07B_NAE0005.ogg"
    "绹" "「……没有，果然还是感觉缺少了些什么。而且真由理姐姐不在了的话，感觉更加严重了」"
    call CHECK_RM_RECEIVE
    $ stopvoc("TEN")
    play TEN "TEN07B_TEN0012"
    $ current_voice = "voice/TEN07B_TEN0012.ogg"
    "天王寺" "「这样啊」"
    call CHECK_RM_RECEIVE
    "只是将外在变得更加好看并不能填补绹的空虚啊……"
    call CHECK_RM_RECEIVE
    "那么缺少的到底是什么呢？"

    call CHECK_RM_RECEIVE
    "虽然还是不太明白这个问题……"

    $ gd["RCVmailData"][gc["ScriptMacros"]["RM_TEN_RECV_MOE02_01"]]["late"]=True
    $ lml.append(gc["ScriptMacros"]["RM_TEN_RECV_MOE02_01"])

    $ stopvoc("TEN")
    play TEN "TEN07B_TEN0013"
    $ current_voice = "voice/TEN07B_TEN0013.ogg"
    "天王寺" "「呐，绹，缺少的东西是怎样的东西呢？」"
    $ stopvoc("TEN")
    play TEN "TEN07B_TEN0014"
    $ current_voice = "voice/TEN07B_TEN0014.ogg"
    "天王寺" "「如果说的再详细一点的话应该可以试试做出来」"
    $ stopvoc("NAE")
    play NAE "TEN07B_NAE0006"
    $ current_voice = "voice/TEN07B_NAE0006.ogg"
    "绹" "「详细？嗯，我自己也不是很清楚……」"
    $ stopvoc("NAE")
    play NAE "TEN07B_NAE0007"
    $ current_voice = "voice/TEN07B_NAE0007.ogg"
    "绹" "「那个呢，大概……」"
    $ stopvoc("TEN")
    play TEN "TEN07B_TEN0015"
    $ current_voice = "voice/TEN07B_TEN0015.ogg"
    "天王寺" "「大概，什么？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='NAE')",DynamicDisplayable(mouthanime,"NAE_AMA03"),"True","lh/NAE_AMA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("NAE")
    play NAE "TEN07B_NAE0008"
    $ current_voice = "voice/TEN07B_NAE0008.ogg"
    "绹" "「感觉缺少妈妈？那样的人。也许是这样」"
    $ stopvoc("TEN")
    play TEN "TEN07B_TEN0016"
    $ current_voice = "voice/TEN07B_TEN0016.ogg"
    "天王寺" "「妈妈……嘛？」"
    "妈妈……"
    "也就是——母亲。"
    "感觉头被锤子敲了一下。"
    "是吗，绹想要的是……母亲。"
    "确实她从出生以后，就一直和我在这栋大楼里工作。"
    "缺少的不是东西，而是人啊。"

    $ targetmailid = cml.setdefault("RM_TEN_SEND_MOE0","")

    $ LR_RM_CHANCE=4
    call CHECK_RM_RECEIVE
    $ stopvoc("TEN")
    play TEN "TEN07B_TEN0017"
    $ current_voice = "voice/TEN07B_TEN0017.ogg"
    "天王寺" "「真是抱歉，绹……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='NAE')",DynamicDisplayable(mouthanime,"NAE_AMA01"),"True","lh/NAE_AMA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    call CHECK_RM_RECEIVE
    $ stopvoc("NAE")
    play NAE "TEN07B_NAE0009"
    $ current_voice = "voice/TEN07B_NAE0009.ogg"
    "绹" "「爸爸？」"
    call CHECK_RM_RECEIVE
    $ stopvoc("TEN")
    play TEN "TEN07B_TEN0018"
    $ current_voice = "voice/TEN07B_TEN0018.ogg"
    "天王寺" "「是这样呢，就算看起来再怎么漂亮，要是缺少应该存在的人的话当然会感觉缺了些什么」"
    call CHECK_RM_RECEIVE
    "我又一次注意到了在很久之前就失去的人的那份重量。"

    call CHECK_RM_RECEIVE
    "为什么我之前没有好好确认过绹的心情呢。"


    $ stopvoc("TEN")
    play TEN "TEN07B_TEN0019"
    $ current_voice = "voice/TEN07B_TEN0019.ogg"
    "天王寺" "「那份钱，应该花在别的东西上啊。不应该用来重建大楼的……」"
    $ stopvoc("TEN")
    play TEN "TEN07B_TEN0020"
    $ current_voice = "voice/TEN07B_TEN0020.ogg"
    "天王寺" "「我要怎么才能弥补……」"
    window hide

    stop bgm 
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

    $ stopvoc("OKA")
    play OKA "TEN07B_OKA0020"
    $ current_voice = "voice/TEN07B_OKA0020.ogg"
    "伦太郎" "「咳咳。啊，Ｍｒ．布朗」"
    $ stopvoc("TEN")
    play TEN "TEN07B_TEN0021"
    $ current_voice = "voice/TEN07B_TEN0021.ogg"
    "天王寺" "「！？　冈部！」"
    $ stopvoc("NAE")
    play NAE "TEN07B_NAE0010"
    $ current_voice = "voice/TEN07B_NAE0010.ogg"
    "绹" "「冈伦叔叔……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA01"),"True","lh/OKA_ASA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "TEN07B_OKA0021"
    $ current_voice = "voice/TEN07B_OKA0021.ogg"
    "伦太郎" "「你们的话我都听到了。好像在后悔大楼的重建呢」"
    $ stopvoc("TEN")
    play TEN "TEN07B_TEN0022"
    $ current_voice = "voice/TEN07B_TEN0022.ogg"
    "天王寺" "「哼，那又怎样？已经没办法了呢」"
    $ stopvoc("TEN")
    play TEN "TEN07B_TEN0023"
    $ current_voice = "voice/TEN07B_TEN0023.ogg"
    "天王寺" "「钱已经全部花完了。现在注意到也迟了」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA05"),"True","lh/OKA_ASA05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "TEN07B_OKA0022"
    $ current_voice = "voice/TEN07B_OKA0022.ogg"
    "伦太郎" "「也许还有机会呢。如果你真心想要改变过去的话」"
    $ stopvoc("TEN")
    play TEN "TEN07B_TEN0024"
    $ current_voice = "voice/TEN07B_TEN0024.ogg"
    "天王寺" "「什么？　此话怎讲？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA01"),"True","lh/OKA_ASA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    play bgm "FD2BGM01"
    $ stopvoc("OKA")
    play OKA "TEN07B_OKA0023"
    $ current_voice = "voice/TEN07B_OKA0023.ogg"
    "伦太郎" "「不能透露太多。但，这并不是开玩笑，我是认真的」"
    $ stopvoc("OKA")
    play OKA "TEN07B_OKA0024"
    $ current_voice = "voice/TEN07B_OKA0024.ogg"
    "伦太郎" "「可以用某种方法改变过去。然后，现在的世界也将被改变」"
    $ stopvoc("TEN")
    play TEN "TEN07B_TEN0025"
    $ current_voice = "voice/TEN07B_TEN0025.ogg"
    "天王寺" "「你，你在说什么？」"
    $ stopvoc("OKA")
    play OKA "TEN07B_OKA0025"
    $ current_voice = "voice/TEN07B_OKA0025.ogg"
    "伦太郎" "「告诉过去的自己不就好了。显像管小姐所需要的不是新大楼，而是母亲这一点」"
    $ stopvoc("OKA")
    play OKA "TEN07B_OKA0026"
    $ current_voice = "voice/TEN07B_OKA0026.ogg"
    "伦太郎" "「如果过去的你注意到了的话，也就不会重建这栋破大楼了吧」"
    $ stopvoc("TEN")
    play TEN "TEN07B_TEN0026"
    $ current_voice = "voice/TEN07B_TEN0026.ogg"
    "天王寺" "「不准说破大楼！但，要是真能做到的话……」"
    $ stopvoc("OKA")
    play OKA "TEN07B_OKA0027"
    $ current_voice = "voice/TEN07B_OKA0027.ogg"
    "伦太郎" "「可以的。这不光是你的愿望，也是我的。不希望就这样失去我们的Ｌａｂ啊」"
    $ stopvoc("TEN")
    play TEN "TEN07B_TEN0027"
    $ current_voice = "voice/TEN07B_TEN0027.ogg"
    "天王寺" "「如果那真的是有一丝可能的话……我要怎么做呢」"
    $ stopvoc("OKA")
    play OKA "TEN07B_OKA0028"
    $ current_voice = "voice/TEN07B_OKA0028.ogg"
    "伦太郎" "「只需要做一件事。Ｍｒ．布朗，你来想一下要发送邮件的内容」"
    $ stopvoc("TEN")
    play TEN "TEN07B_TEN0028"
    $ current_voice = "voice/TEN07B_TEN0028.ogg"
    "天王寺" "「什么？什么内容？」"
    $ stopvoc("OKA")
    play OKA "TEN07B_OKA0029"
    $ current_voice = "voice/TEN07B_OKA0029.ogg"
    "伦太郎" "「是的。１８个字，分成３段。来告诉过去的自己你想要传达的事情」"
    $ stopvoc("OKA")
    play OKA "TEN07B_OKA0030"
    $ current_voice = "voice/TEN07B_OKA0030.ogg"
    "伦太郎" "「内容当然就是，显像管小姐想要的是母亲这件事。可以吗？？」"
    $ stopvoc("TEN")
    play TEN "TEN07B_TEN0029"
    $ current_voice = "voice/TEN07B_TEN0029.ogg"
    "天王寺" "「虽然不太明白怎么回事，但知道了」"
    $ stopvoc("TEN")
    play TEN "TEN07B_TEN0030"
    $ current_voice = "voice/TEN07B_TEN0030.ogg"
    "天王寺" "「这样不好，还是原来的样子好。试着配合你一下好了」"
    hide screen phoneSD1
    window hide



    hide screen phonebtn
    hide screen phoneSD1
    $ stopvoc("TEN")
    play TEN "TEN07B_TEN0031"
    $ current_voice = "voice/TEN07B_TEN0031.ogg"
    "天王寺" "「想好了冈部。这么说怎么样？」"
    window hide


    $ loadBG(2,"PBG22A")



    hide screen phonebtn
    $ stopvoc("TEN")
    play TEN "TEN07B_TEN0032"
    $ current_voice = "voice/TEN07B_TEN0032.ogg"
    "天王寺" "「『不要去重建。缺少的东西是妈妈』。虽说这么说有些直接」"
    $ stopvoc("OKA")
    play OKA "TEN07B_OKA0031"
    $ current_voice = "voice/TEN07B_OKA0031.ogg"
    "伦太郎" "「不错啊。问题是能不能让过去的你相信……有希望」"
    $ stopvoc("OKA")
    play OKA "TEN07B_OKA0032"
    $ current_voice = "voice/TEN07B_OKA0032.ogg"
    "伦太郎" "「收到如此有深意的邮件的话，应该会和显像管小姐确认一下的吧。这样应该就能改变过去了」"
    window hide



    $ loadBG(2,"BG59A")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_AMA01"),"True","lh/OKA_AMA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    show screen phonebtn
    show screen phoneSD1
    $ stopvoc("TEN")
    play TEN "TEN07B_TEN0033"
    $ current_voice = "voice/TEN07B_TEN0033.ogg"
    "天王寺" "「这样啊。那，该怎么发送呢？」"
    $ stopvoc("OKA")
    play OKA "TEN07B_OKA0033"
    $ current_voice = "voice/TEN07B_OKA0033.ogg"
    "伦太郎" "「使用电话微波炉（暂）。电话微波炉（暂）需要的楼下的显像管没问题，所以应该能正常启动。」"
    $ stopvoc("OKA")
    play OKA "TEN07B_OKA0034"
    $ current_voice = "voice/TEN07B_OKA0034.ogg"
    "伦太郎" "「那么就将现在的消息发送给正要下定决心重建大楼的时候的你吧」"
    window hide


    $ loadBG(2,"IBG040A")



    hide screen phonebtn
    "这么说着，冈部操作着电子微波炉和电话。"
    "到底在搞什么鬼？"
    "虽然以为自己只是一时糊涂信了他的鬼话……"
    window hide


    $ loadBG(2,"BG59A")
    show houden 





    play se "SGSE035L" loop

    show screen phonebtn
    $ stopvoc("TEN")
    play TEN "TEN07B_TEN0034"
    $ current_voice = "voice/TEN07B_TEN0034.ogg"
    "天王寺" "「喂，喂，怎么了这是！？火花四溅了啊？」"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_AMA01"),"True","lh/OKA_AMA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("TEN")
    play TEN "TEN07B_TEN0035"
    $ current_voice = "voice/TEN07B_TEN0035.ogg"
    "天王寺" "「笨蛋，快住手！　要起火的！」"
    $ stopvoc("OKA")
    play OKA "TEN07B_OKA0035"
    $ current_voice = "voice/TEN07B_OKA0035.ogg"
    "伦太郎" "「没关系。之前的大楼也没发生过什么，现在这大楼耐火性提高了就更没问题了」"
    $ stopvoc("OKA")
    play OKA "TEN07B_OKA0036"
    $ current_voice = "voice/TEN07B_OKA0036.ogg"
    "伦太郎" "「然后这个放电现象就是——通向过去的大门被打开的证明。」"
    play se "SGSE049L" loop
    $ stopvoc("TEN")
    play TEN "TEN07B_TEN0036"
    $ current_voice = "voice/TEN07B_TEN0036.ogg"
    "天王寺" "「唔哦，地震吗？　不对，这个震动是……！」"
    "以前大楼经常出现的震动。"
    "说起来，难道说……"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_AMA05"),"True","lh/OKA_AMA05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "TEN07B_OKA0037"
    $ current_voice = "voice/TEN07B_OKA0037.ogg"
    "伦太郎" "「邮件哦，回到过去吧。穿越时空，向着一年前的Ｍｒ．布朗！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_AMB01"),"True","lh/OKA_AMB01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "TEN07B_OKA0038"
    $ current_voice = "voice/TEN07B_OKA0038.ogg"
    "伦太郎" "「现在正是重新创造历史的时刻。呼哈哈哈哈！」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='NAE')",DynamicDisplayable(mouthanime,"NAE_AMA01"),"True","lh/NAE_AMA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("NAE")
    play NAE "TEN07B_NAE0011"
    $ current_voice = "voice/TEN07B_NAE0011.ogg"
    "绹" "「爸，爸爸……」"
    $ stopvoc("TEN")
    play TEN "TEN07B_TEN0037"
    $ current_voice = "voice/TEN07B_TEN0037.ogg"
    "天王寺" "「喂冈部，快说明一下。这晃动是因为微波炉的关系吗。是这样吗！？」"
    $ stopvoc("TEN")
    play TEN "TEN07B_TEN0038"
    $ current_voice = "voice/TEN07B_TEN0038.ogg"
    "天王寺" "「你到底……是什么人？难道说真的……唔哇啊啊啊啊啊！！」"

    hide screen phoneSD1
    hide screen phonebtn
    with whiteflash
    show screen invisible
    $ renpy.movie_cutscene("video/imv03.avi")
    hide screen invisible
    scene expression Solid("000000")  with fade








    return







    return







    return




    return
