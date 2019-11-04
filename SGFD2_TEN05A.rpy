label SGFD2_TEN05A:
    window hide



    $ loadBG(0,"BG37A")


    $ date="8/18"
    show screen phonebtn
    show screen phoneSD1

    "这样就好了吧。"
    "是啊，已经没有什么可以迷茫的了。"
    "就算大楼变了，人不会变。"
    "这样听起来的话不错呢。"
    "虽然这栋大楼里满是与你的回忆，但是请原谅我吧。"
    "这一切都是为了绹啊。"
    window hide


    $ loadBG(0,"BG15A")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='FPP')",DynamicDisplayable(mouthanime,"FPP_AMA01"),"True","lh/FPP_AMA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    play se "SGSE004L" loop

    $ targetmailid = gc["ScriptMacros"]["RM_TEN_RECV_MOE01_01"]

    $ LR_RM_CHANCE=13
    call CHECK_RM_RECEIVE
    $ stopvoc("FPP")
    play FPP "TEN05A_FPP0000"
    $ current_voice = "voice/TEN05A_FPP0000.ogg"
    "秋叶" "「这样啊。下定决心了吗？」"
    call CHECK_RM_RECEIVE
    $ stopvoc("TEN")
    play TEN "TEN05A_TEN0000"
    $ current_voice = "voice/TEN05A_TEN0000.ogg"
    "天王寺" "「嗯嗯，如你所言，秋叶先生。我太拘泥于一些细小的事情了。」"
    call CHECK_RM_RECEIVE
    $ stopvoc("TEN")
    play TEN "TEN05A_TEN0001"
    $ current_voice = "voice/TEN05A_TEN0001.ogg"
    "天王寺" "「打算重建大楼了。那个……虽然反对意见好像有点多。」"
    call CHECK_RM_RECEIVE
    $ stopvoc("FPP")
    play FPP "TEN05A_FPP0001"
    $ current_voice = "voice/TEN05A_FPP0001.ogg"
    "秋叶" "「是呢。我当时也是反对女儿的提案的。」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='FPP')",DynamicDisplayable(mouthanime,"FPP_AMA03"),"True","lh/FPP_AMA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    call CHECK_RM_RECEIVE
    $ stopvoc("FPP")
    play FPP "TEN05A_FPP0002"
    $ current_voice = "voice/TEN05A_FPP0002.ogg"
    "秋叶" "「但现在已经接受了，觉得真是太好了。给这条街道带来了新的气息呢。」"
    call CHECK_RM_RECEIVE
    $ stopvoc("TEN")
    play TEN "TEN05A_TEN0002"
    $ current_voice = "voice/TEN05A_TEN0002.ogg"
    "天王寺" "「…………」"
    window hide


    $ loadBG(3,"IBGX048",over=True)




    call CHECK_RM_RECEIVE
    "也许有什么会改变。"
    call CHECK_RM_RECEIVE
    "那种事情不是早就知道了吗。"
    call CHECK_RM_RECEIVE
    "这个人说的话是对的。"
    call CHECK_RM_RECEIVE
    "不能被那种微妙的伤感蒙蔽了双眼。"
    call CHECK_RM_RECEIVE
    "大概，所谓追求理想，就是抛弃那些不完全的东西吧？"
    call CHECK_RM_RECEIVE
    "那样的话除了破坏便别无他法了。"
    call CHECK_RM_RECEIVE
    "受你照顾了呢，大桧山大楼。"

    call CHECK_RM_RECEIVE
    "长久以来十分感谢。"

    $ gd["RCVmailData"][gc["ScriptMacros"]["RM_TEN_RECV_MOE01_01"]]["late"]=True
    $ lml.append(gc["ScriptMacros"]["RM_TEN_RECV_MOE01_01"])

    hide background-over 
    window hide

    show expression ConditionSwitch("renpy.music.get_playing(channel='FPP')",DynamicDisplayable(mouthanime,"FPP_AMA01"),"True","lh/FPP_AMA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)




    $ stopvoc("FPP")
    play FPP "TEN05A_FPP0003"
    $ current_voice = "voice/TEN05A_FPP0003.ogg"
    "秋叶" "「能这么说该怎么说呢，我觉得是不错的判断哦。虽然有的东西是越旧越值钱……」"
    $ stopvoc("FPP")
    play FPP "TEN05A_FPP0004"
    $ current_voice = "voice/TEN05A_FPP0004.ogg"
    "秋叶" "「但失去价值的东西的消失也是自然的。那是理所当然的吧」"
    $ stopvoc("TEN")
    play TEN "TEN05A_TEN0003"
    $ current_voice = "voice/TEN05A_TEN0003.ogg"
    "天王寺" "「………」"
    stop se
    "失去价值的东西的消失……是自然的？"
    "消失是自然的……"
    $ stopvoc("TEN")
    play TEN "TEN05A_TEN0004"
    $ current_voice = "voice/TEN05A_TEN0004.ogg"
    "天王寺" "「喂，稍微等等啊」"
    $ stopvoc("FPP")
    play FPP "TEN05A_FPP0005"
    $ current_voice = "voice/TEN05A_FPP0005.ogg"
    "秋叶" "「怎么了吗、天王寺先生？」"
    $ stopvoc("TEN")
    play TEN "TEN05A_TEN0005"
    $ current_voice = "voice/TEN05A_TEN0005.ogg"
    "天王寺" "「稍微等一下，消失这件事是自然的。你刚才这么说了吧？」"
    $ stopvoc("FPP")
    play FPP "TEN05A_FPP0006"
    $ current_voice = "voice/TEN05A_FPP0006.ogg"
    "秋叶" "「诶诶，确实这么说了。」"
    $ stopvoc("TEN")
    play TEN "TEN05A_TEN0006"
    $ current_voice = "voice/TEN05A_TEN0006.ogg"
    "天王寺" "「虽然从常理来说，也许确实如此。但是如果是有所留恋之物，就不是那么回事了吧」"
    $ stopvoc("TEN")
    play TEN "TEN05A_TEN0007"
    $ current_voice = "voice/TEN05A_TEN0007.ogg"
    "天王寺" "「这样消失的东西中也有贵重的东西哦。只是能够理解它的价值的人减少了而已」"
    $ stopvoc("TEN")
    play TEN "TEN05A_TEN0008"
    $ current_voice = "voice/TEN05A_TEN0008.ogg"
    "天王寺" "「在大部分的人都没有注意到它的价值的时候……那家伙注意到了。是啊，只有那家伙。」"
    $ stopvoc("FPP")
    play FPP "TEN05A_FPP0007"
    $ current_voice = "voice/TEN05A_FPP0007.ogg"
    "秋叶" "「……那家伙？」"
    hide screen phoneSD1
    window hide


    $ loadBG(0,"BG04A2")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA04"),"True","lh/OKA_ASA04a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    hide screen phonebtn
    play bgm "BGM31"
    $ stopvoc("OKA")
    play OKA "TEN05A_OKA0000"
    $ current_voice = "voice/TEN05A_OKA0000.ogg"
    "伦太郎" "「归处……对，这地方对于我来说是必要的归处！」"
    $ stopvoc("TEN")
    play TEN "TEN05A_TEN0009"
    $ current_voice = "voice/TEN05A_TEN0009.ogg"
    "天王寺" "「归处？你有这么和我说过吗？」"
    $ stopvoc("TEN")
    play TEN "TEN05A_TEN0010"
    $ current_voice = "voice/TEN05A_TEN0010.ogg"
    "天王寺" "「通常来说，没钱的话去租些便宜的郊区房子不就行了。不是这里也没有关系吧」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA03"),"True","lh/OKA_ASA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "TEN05A_OKA0001"
    $ current_voice = "voice/TEN05A_OKA0001.ogg"
    "伦太郎" "「那样不行，不在这个秋叶原的话！！」"
    $ stopvoc("TEN")
    play TEN "TEN05A_TEN0011"
    $ current_voice = "voice/TEN05A_TEN0011.ogg"
    "天王寺" "「嘘，别叫那么大声。果然是个烦人的家伙呢。为什么就一定要在这条街上？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA01"),"True","lh/OKA_ASA01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "TEN05A_OKA0002"
    $ current_voice = "voice/TEN05A_OKA0002.ogg"
    "伦太郎" "「一切都存在与此啊。新的东西，旧的东西，全部在这里」"
    $ stopvoc("TEN")
    play TEN "TEN05A_TEN0012"
    $ current_voice = "voice/TEN05A_TEN0012.ogg"
    "天王寺" "「全部？　这是在说什么」"
    $ stopvoc("OKA")
    play OKA "TEN05A_OKA0003"
    $ current_voice = "voice/TEN05A_OKA0003.ogg"
    "伦太郎" "「在这个秋叶原里并不只有最尖端的文化。旧文明的遗产也长眠于此。」"
    $ stopvoc("OKA")
    play OKA "TEN05A_OKA0004"
    $ current_voice = "voice/TEN05A_OKA0004.ogg"
    "伦太郎" "「那所谓的遗产，也就是从时代的洪流中被遗忘的各种各样的技术！」"
    $ stopvoc("TEN")
    play TEN "TEN05A_TEN0013"
    $ current_voice = "voice/TEN05A_TEN0013.ogg"
    "天王寺" "「技术？」"
    $ stopvoc("OKA")
    play OKA "TEN05A_OKA0005"
    $ current_voice = "voice/TEN05A_OKA0005.ogg"
    "伦太郎" "「是的。对于常人来说只是些无聊的小玩意的遗物。但在那其中，是伟大发明的根源啊」"
    $ stopvoc("OKA")
    play OKA "TEN05A_OKA0006"
    $ current_voice = "voice/TEN05A_OKA0006.ogg"
    "伦太郎" "「逐渐消失的支流中诞生出了如今的干流。追寻那支流，就是凤凰院凶真的目标！」"
    $ stopvoc("TEN")
    play TEN "TEN05A_TEN0014"
    $ current_voice = "voice/TEN05A_TEN0014.ogg"
    "天王寺" "「在说什么呀。你这家伙……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA03"),"True","lh/OKA_ASA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "TEN05A_OKA0007"
    $ current_voice = "voice/TEN05A_OKA0007.ogg"
    "伦太郎" "「在那些只有表层的街道建立Ｌａｂ的话，能做到什么呢？什么也做不到啊。因为在那样没有积淀的街道上什么也无法诞生出来」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA05"),"True","lh/OKA_ASA05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "TEN05A_OKA0008"
    $ current_voice = "voice/TEN05A_OKA0008.ogg"
    "伦太郎" "「在这新旧文化交错的秋叶原，才是吾之Ｌａｂ所应诞生之地！混沌之处实乃吾之故乡！唔哈哈哈哈！」"
    $ stopvoc("TEN")
    play TEN "TEN05A_TEN0015"
    $ current_voice = "voice/TEN05A_TEN0015.ogg"
    "天王寺" "「…………」"
    $ stopvoc("TEN")
    play TEN "TEN05A_TEN0016"
    $ current_voice = "voice/TEN05A_TEN0016.ogg"
    "天王寺" "「你这家伙，果然脑子不太正常吧？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA04"),"True","lh/OKA_ASA04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "TEN05A_OKA0009"
    $ current_voice = "voice/TEN05A_OKA0009.ogg"
    "伦太郎" "「什、什么！？可没有发疯哦，一直都是很正经的」"
    $ stopvoc("TEN")
    play TEN "TEN05A_TEN0017"
    $ current_voice = "voice/TEN05A_TEN0017.ogg"
    "天王寺" "「确实……就算是些破旧的东西也还是有它们的价值这一点我也同意。就算是旧东西也有有用的啊」"
    $ stopvoc("TEN")
    play TEN "TEN05A_TEN0018"
    $ current_voice = "voice/TEN05A_TEN0018.ogg"
    "天王寺" "「你这家伙，对于显像管有兴趣么？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA05"),"True","lh/OKA_ASA05a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "TEN05A_OKA0010"
    $ current_voice = "voice/TEN05A_OKA0010.ogg"
    "伦太郎" "「显像管？　哼，一根头发的兴趣都没有！」"
    $ stopvoc("TEN")
    play TEN "TEN05A_TEN0019"
    $ current_voice = "voice/TEN05A_TEN0019.ogg"
    "天王寺" "「什么！？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA04"),"True","lh/OKA_ASA04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "TEN05A_OKA0011"
    $ current_voice = "voice/TEN05A_OKA0011.ogg"
    "伦太郎" "「……不对，有兴趣。突然有兴趣了。」"
    $ stopvoc("TEN")
    play TEN "TEN05A_TEN0020"
    $ current_voice = "voice/TEN05A_TEN0020.ogg"
    "天王寺" "「是吗。那么从今天开始就一直有兴趣下去了吗？」"
    $ stopvoc("TEN")
    play TEN "TEN05A_TEN0021"
    $ current_voice = "voice/TEN05A_TEN0021.ogg"
    "天王寺" "「虽然你这家伙有些奇怪，但看起来也不是什么不识货的人呢」"
    window hide

    stop bgm 


    $ loadBG(0,"BG15A")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='FPP')",DynamicDisplayable(mouthanime,"FPP_AMA02"),"True","lh/FPP_AMA02a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    show screen phonebtn
    show screen phoneSD1
    play bgm "BGM11"
    $ stopvoc("TEN")
    play TEN "TEN05A_TEN0022"
    $ current_voice = "voice/TEN05A_TEN0022.ogg"
    "天王寺" "「价值稀薄的东西并不等于没有价值的东西哦。冈部是知道这点的吧。那我就把２楼租给他了。」"
    $ stopvoc("FPP")
    play FPP "TEN05A_FPP0008"
    $ current_voice = "voice/TEN05A_FPP0008.ogg"
    "秋叶" "「…………」"
    $ stopvoc("TEN")
    play TEN "TEN05A_TEN0023"
    $ current_voice = "voice/TEN05A_TEN0023.ogg"
    "天王寺" "「秋叶先生，我现在还收购着使用显像管的电视。从旁人的角度来看，也许它们已经是时代的眼泪，没有价值的东西了呢。但是……」"
    $ stopvoc("TEN")
    play TEN "TEN05A_TEN0024"
    $ current_voice = "voice/TEN05A_TEN0024.ogg"
    "天王寺" "「也还是有喜欢显像管的家伙存在着的呢。那种静电的手感与独特的亮度，那种感觉在液晶电视上可找不到」"
    $ stopvoc("TEN")
    play TEN "TEN05A_TEN0025"
    $ current_voice = "voice/TEN05A_TEN0025.ogg"
    "天王寺" "「所以没有价值的东西消失是理所当然的吗？我实在是不喜欢那样没有情怀的思考方式」"
    $ stopvoc("TEN")
    play TEN "TEN05A_TEN0026"
    $ current_voice = "voice/TEN05A_TEN0026.ogg"
    "天王寺" "「您确实是位好人。但是我觉得您的心里可能“有什么不对的地方”。那么想的理由终于明白了呢。」"
    $ stopvoc("TEN")
    play TEN "TEN05A_TEN0027"
    $ current_voice = "voice/TEN05A_TEN0027.ogg"
    "天王寺" "「您太善于抛弃过去了。而我确实一直无法割舍过去这么活着。大概，是因为不是同一种人吧。」"
    $ stopvoc("FPP")
    play FPP "TEN05A_FPP0009"
    $ current_voice = "voice/TEN05A_FPP0009.ogg"
    "秋叶" "「天王寺先生……」"
    $ stopvoc("TEN")
    play TEN "TEN05A_TEN0028"
    $ current_voice = "voice/TEN05A_TEN0028.ogg"
    "天王寺" "「虽然很抱歉，但是我无法认同您的想法。就在刚刚，我又改变主意了。」"
    $ stopvoc("TEN")
    play TEN "TEN05A_TEN0029"
    $ current_voice = "voice/TEN05A_TEN0029.ogg"
    "天王寺" "「大桧山大楼——就像现在这样继续存在下去吧。」"
    $ stopvoc("FPP")
    play FPP "TEN05A_FPP0010"
    $ current_voice = "voice/TEN05A_FPP0010.ogg"
    "フェイリスパパ３" "「…………」"
    $ stopvoc("FPP")
    play FPP "TEN05A_FPP0011"
    $ current_voice = "voice/TEN05A_FPP0011.ogg"
    "秋叶" "「这样吗。好遗憾呢。好像看起来让您误解了呢」"
    $ stopvoc("FPP")
    play FPP "TEN05A_FPP0012"
    $ current_voice = "voice/TEN05A_FPP0012.ogg"
    "秋叶" "「那栋大楼附近的区域好像今后人流量会变大。如果要重建的话，我本来想要稍微出点钱的」"
    $ stopvoc("TEN")
    play TEN "TEN05A_TEN0030"
    $ current_voice = "voice/TEN05A_TEN0030.ogg"
    "天王寺" "「诶、出点钱？」"
    $ stopvoc("FPP")
    play FPP "TEN05A_FPP0013"
    $ current_voice = "voice/TEN05A_FPP0013.ogg"
    "秋叶" "「是的。就算３亿日元能够重建完成，但是连运营费都要包括进去的话我觉得有些勉强了」"
    $ stopvoc("FPP")
    play FPP "TEN05A_FPP0014"
    $ current_voice = "voice/TEN05A_FPP0014.ogg"
    "秋叶" "「诶呀，请忘了吧。对于现在的你来说一定是个厚脸皮的提案吧……」"

    $ targetmailid = cml.setdefault("RM_TEN_SEND_MOE01","")

    $ LR_RM_CHANCE=6

    stop bgm 
    call CHECK_RM_RECEIVE
    $ stopvoc("TEN")
    play TEN "TEN05A_TEN0031"
    $ current_voice = "voice/TEN05A_TEN0031.ogg"
    "天王寺" "「那就重建」"
    call CHECK_RM_RECEIVE
    $ stopvoc("FPP")
    play FPP "TEN05A_FPP0015"
    $ current_voice = "voice/TEN05A_FPP0015.ogg"
    "秋叶" "「……诶？」"
    play bgm "BGM22"
    call CHECK_RM_RECEIVE
    $ stopvoc("TEN")
    play TEN "TEN05A_TEN0032"
    $ current_voice = "voice/TEN05A_TEN0032.ogg"
    "天王寺" "「果然还是重建吧。不不该说秋叶先生真是坏呢。有这种事的话早点告诉我就好了」"
    call CHECK_RM_RECEIVE
    $ stopvoc("FPP")
    play FPP "TEN05A_FPP0016"
    $ current_voice = "voice/TEN05A_FPP0016.ogg"
    "秋叶" "「但是，真的好吗？刚刚，还不是说和我脾气不合什么的……」"
    call CHECK_RM_RECEIVE
    $ stopvoc("TEN")
    play TEN "TEN05A_TEN0033"
    $ current_voice = "voice/TEN05A_TEN0033.ogg"
    "天王寺" "「脾气不合的话让它合起来就好了。不要在意这些细节嘛」"
    call CHECK_RM_RECEIVE
    $ stopvoc("TEN")
    play TEN "TEN05A_TEN0034"
    $ current_voice = "voice/TEN05A_TEN0034.ogg"
    "天王寺" "「是吗要出点钱嘛。不，是要帮助那家伙吗。哈哈哈哈」"

    call CHECK_RM_RECEIVE
    $ stopvoc("FPP")
    play FPP "TEN05A_FPP0017"
    $ current_voice = "voice/TEN05A_FPP0017.ogg"
    "秋叶" "「哈……」"

    $ gd["RCVmailData"][gc["ScriptMacros"]["RM_TEN_RECV_MOE02_01"]]["late"]=True
    $ lml.append(gc["ScriptMacros"]["RM_TEN_RECV_MOE02_01"])


    hide screen phoneSD1
    window hide
    hide screen phonebtn
    scene expression Solid("000000")  with fade





    return
