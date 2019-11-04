label SGFD2_TEN07A:
    window hide



    $ loadBG(0,"BG_BLACK")


    $ date="7/16"
    $ day = "SAT"
    $ rml=[]
    $ sml=[]
    $ cml={}
    $ lml=[]
    hide screen phonebtn
    hide screen phoneSD1

    "开始了以后，就不能半途而废。"
    "从设计到施工，全部要到场。"
    "必须要造出不管是谁看了都挑不出毛病的完美大楼。"
    "大概过了一年左右的施工，终于……"
    window hide


    $ loadBG(0,"IBGX048")

    show screen phoneSD1
    $ stopvoc("TEN")
    play TEN "TEN07A_TEN0000"
    $ current_voice = "voice/TEN07A_TEN0000.ogg"
    "天王寺" "「那么，是时候公开了。看吧，大家！」"
    $ stopvoc("TEN")
    play TEN "TEN07A_TEN0001"
    $ current_voice = "voice/TEN07A_TEN0001.ogg"
    "天王寺" "「这就是重生后的新大桧山大楼！」"
    window hide







    show expression "bg/BG58A~ipad.jpg" as background :
        yalign 1.0
        1 
        linear 1.0yalign 0.0

















    play se "SGSE029"
    pause 3
    $ loadBG(1,"BG58A")
















    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA04"),"True","lh/OKA_ASA04a~ipad.png") at center as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)





    stop se
    play bgm "BGM18"
    show screen phonebtn
    $ stopvoc("OKA")
    play OKA "TEN07A_OKA0000"
    $ current_voice = "voice/TEN07A_OKA0000.ogg"
    "伦太郎" "「这、这是……」"
    $ stopvoc("TEN")
    play TEN "TEN07A_TEN0002"
    $ current_voice = "voice/TEN07A_TEN0002.ogg"
    "天王寺" "「怎么样，超厉害吧。哇哈哈哈哈哈！」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSB03"),"True","lh/MAY_CSB03a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='RUK')",DynamicDisplayable(mouthanime,"RUK_CSB04"),"True","lh/RUK_CSB04a~ipad.png") at left_t as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh7 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA04"),"True","lh/DAR_ASA04a~ipad.png") at right_t as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("MAY")
    play MAY "TEN07A_MAY0000"
    $ current_voice = "voice/TEN07A_MAY0000.ogg"
    "真由理" "「哇，闪闪发光呢」"
    $ stopvoc("DAR")
    play DAR "TEN07A_DAR0000"
    $ current_voice = "voice/TEN07A_DAR0000.ogg"
    "至" "「说是重生，感觉是完全不同的另一幢大楼了诶？」"
    $ stopvoc("RUK")
    play RUK "TEN07A_RUK0000"
    $ current_voice = "voice/TEN07A_RUK0000.ogg"
    "琉华" "「是呢，感觉完全找不到过去的影子了」"
    $ stopvoc("TEN")
    play TEN "TEN07A_TEN0003"
    $ current_voice = "voice/TEN07A_TEN0003.ogg"
    "天王寺" "「惊讶的话先说到这里。我带你们到里面参观一下吧」"
    window hide

    stop se


    $ loadBG(0,"BG59A")

    $ stopvoc("TEN")
    play TEN "TEN07A_TEN0004"
    $ current_voice = "voice/TEN07A_TEN0004.ogg"
    "天王寺" "「这里是新的２楼。你们的地盘」"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASC04"),"True","lh/CRS_ASC04a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_DSC02"),"True","lh/FEI_DSC02a~ipad.png") at right_t as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh7 
    show expression ConditionSwitch("renpy.music.get_playing(channel='MOE')",DynamicDisplayable(mouthanime,"MOE_ASB02"),"True","lh/MOE_ASB02a~ipad.png") at left_t as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "TEN07A_CRS0000"
    $ current_voice = "voice/TEN07A_CRS0000.ogg"
    "红莉栖" "「喂，这是哪里的办公室啊？」"
    $ stopvoc("FEI")
    play FEI "TEN07A_FEI0000"
    $ current_voice = "voice/TEN07A_FEI0000.ogg"
    "菲利斯" "「说是Ｌａｂ，感觉是公司呢」"
    $ stopvoc("MOE")
    play MOE "TEN07A_MOE0000"
    $ current_voice = "voice/TEN07A_MOE0000.ogg"
    "萌郁" "「入社……恭喜」"
    $ stopvoc("TEN")
    play TEN "TEN07A_TEN0005"
    $ current_voice = "voice/TEN07A_TEN0005.ogg"
    "天王寺" "「也就是说从今天起这座大楼就是我们新的城了」"
    $ stopvoc("TEN")
    play TEN "TEN07A_TEN0006"
    $ current_voice = "voice/TEN07A_TEN0006.ogg"
    "天王寺" "「像以前那样粗鲁的使用方式可是要吃拳头的哦。给我小心地用」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASC05"),"True","lh/CRS_ASC05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("CRS")
    play CRS "TEN07A_CRS0001"
    $ current_voice = "voice/TEN07A_CRS0001.ogg"
    "红莉栖" "「是、是……」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh8 
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA02"),"True","lh/DAR_ASA02a~ipad.png") at center as lh8 zorder (10-8) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("DAR")
    play DAR "TEN07A_DAR0001"
    $ current_voice = "voice/TEN07A_DAR0001.ogg"
    "至" "「不知为何有点紧张起来哦。我，这样的地方还是第一次来……」"
    $ stopvoc("TEN")
    play TEN "TEN07A_TEN0007"
    $ current_voice = "voice/TEN07A_TEN0007.ogg"
    "天王寺" "「绹，下面的店当然随你来，二楼的话想来玩也随时可以哦」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='NAE')",DynamicDisplayable(mouthanime,"NAE_ASA01"),"True","lh/NAE_ASA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("NAE")
    play NAE "TEN07A_NAE0000"
    $ current_voice = "voice/TEN07A_NAE0000.ogg"
    "绹" "「嗯……」"
    $ stopvoc("TEN")
    play TEN "TEN07A_TEN0008"
    $ current_voice = "voice/TEN07A_TEN0008.ogg"
    "天王寺" "「再也不会给你留下什么无聊的回忆了。这里应该会成为你最喜欢的家吧」"
    "不出所料，绹和其他人都毫无异议。"
    "肯定的吧，肯定的吧。"
    "这可是我天王寺裕吾，一生一世的大决战啊。"
    "再也不会让谁说这是幢破旧的大楼了呢。"
    scene expression Solid("000000")  with fade

    hide screen phoneSD1
    window hide

    stop bgm 





    return
