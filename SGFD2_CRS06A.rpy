label SGFD2_CRS06A:
    window hide


    $ loadBG(0,"BG05N2")


    $ date="8/13"
    show screen phonebtn
    show screen phoneSD1

    "回到说好的汇合地点Ｌａｂ楼下，等在那儿的，是冈部，还有扶着她的娇小女仆和五十岁左右的管家。"
    "那位穿着女仆装的娇小女孩，就是菲利斯吧。"
    "旁边那微老的管家，简直就像从漫画或动画里跳出来的登场人物。"
    "冈部的脸色异常憔悴，似乎一个人就要站不住了。"
    "现在菲利斯和管家两人一同架着他的肩膀。"
    $ stopvoc("CRS")
    play CRS "CRS06A_CRS0000"
    $ current_voice = "voice/CRS06A_CRS0000.ogg"
    "红莉栖" "「冈部……」"
    "不由得加快了脚步。"

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_BMC03"),"True","lh/FEI_BMC03a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FEI")
    play FEI "CRS06A_FEI0000"
    $ current_voice = "voice/CRS06A_FEI0000.ogg"
    "菲利斯" "「你就是，牧濑？」"
    $ stopvoc("CRS")
    play CRS "CRS06A_CRS0001"
    $ current_voice = "voice/CRS06A_CRS0001.ogg"
    "红莉栖" "「嗯，谢谢你，菲利斯。多亏你找到了冈部。」"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_RAINET_AB"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_RAINET_AB"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_RAINET_AB"])
    "顺便一提，菲利斯·喵喵这名字，是她在{color=#f00}雷ＮｅｔＡＢ{/color}大赛时用的类似于艺名的称呼。这也是以前被桥田灌输的知识。"
    $ stopvoc("FEI")
    play FEI "CRS06A_FEI0001"
    $ current_voice = "voice/CRS06A_FEI0001.ogg"
    "菲利斯" "「嗯。接到桶子喵的联系后，菲利斯也是担心得不得了。」"
    $ stopvoc("FEI")
    play FEI "CRS06A_FEI0002"
    $ current_voice = "voice/CRS06A_FEI0002.ogg"
    "菲利斯" "「我就想啊，虽然不知道是怎么回事，总之先找找看吧。」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_BMA03"),"True","lh/FEI_BMA03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FEI")
    play FEI "CRS06A_FEI0003"
    $ current_voice = "voice/CRS06A_FEI0003.ogg"
    "菲利斯" "「可是，从刚才起就一直联系不上桶子喵。」"
    "桥田吗……？他还在寻找冈部吧。"
    "不过现在顾不上那么多了。"
    $ stopvoc("CRS")
    play CRS "CRS06A_CRS0002"
    $ current_voice = "voice/CRS06A_CRS0002.ogg"
    "红莉栖" "「那，冈部他……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_BMC03"),"True","lh/FEI_BMC03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_UPX"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_UPX"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_UPX"])
    $ stopvoc("FEI")
    play FEI "CRS06A_FEI0004"
    $ current_voice = "voice/CRS06A_FEI0004.ogg"
    "菲利斯" "「现在稍微冷静一点了。不过，在{color=#f00}ＵＰＸ{/color}的天桥上找到他时，菲利斯还真以为他要死了……」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_AMA07"),"True","lh/OKA_AMA07a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "CRS06A_OKA0000"
    $ current_voice = "voice/CRS06A_OKA0000.ogg"
    "伦太郎" "「…………」"
    "此时此刻，他的脸色像纸一样苍白。得知他的情况比刚才更加严重了，我就感到一阵揪心。"
    "冈部的所思、所想……我必须要弄清楚。"
    $ stopvoc("CRS")
    play CRS "CRS06A_CRS0003"
    $ current_voice = "voice/CRS06A_CRS0003.ogg"
    "红莉栖" "「冈部，到底出了什么事……」"
    $ stopvoc("OKA")
    play OKA "CRS06A_OKA0001"
    $ current_voice = "voice/CRS06A_OKA0001.ogg"
    "伦太郎" "「…………」"
    "可是，冈部的视线失去了焦点。"
    "根本没有在看着我。"
    $ stopvoc("CRS")
    play CRS "CRS06A_CRS0004"
    $ current_voice = "voice/CRS06A_CRS0004.ogg"
    "红莉栖" "「…………」"
    $ stopvoc("CRS")
    play CRS "CRS06A_CRS0005"
    $ current_voice = "voice/CRS06A_CRS0005.ogg"
    "红莉栖" "「无论如何，一直站在这里也不太好说话，先上楼到Ｌａｂ里去吧。」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    "管家架着眼神空虚的冈部，我们开门踏进了Ｌａｂ。"
    window hide



    $ loadBG(0,"BG01N")

    $ stopvoc("CRS")
    play CRS "CRS06A_CRS0006"
    $ current_voice = "voice/CRS06A_CRS0006.ogg"
    "红莉栖" "「…………！」"
    "打开房间的灯那瞬间，我整个人都惊呆了。"
    play bgm "BGM09"
    $ stopvoc("CRS")
    play CRS "CRS06A_CRS0007"
    $ current_voice = "voice/CRS06A_CRS0007.ogg"
    "红莉栖" "「这是……什么……」"
    "地板上，有血迹……！"
    $ stopvoc("FEI")
    play FEI "CRS06A_FEI0005"
    $ current_voice = "voice/CRS06A_FEI0005.ogg"
    "菲利斯" "「诶！？ 这，这个……是什么？」"
    "背后的菲利斯也发出吃惊的喊声。"
    "不过，反应更为激烈的是冈部。"
    window hide



    $ stopvoc("OKA")
    play OKA "CRS06A_OKA0002"
    $ current_voice = "voice/CRS06A_OKA0002.ogg"
    "伦太郎" "「哦……噢噢噢噢，噢噢……啊啊啊啊，呜哇啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊──」"
    $ stopvoc("OKA")
    play OKA "CRS06A_OKA0003"
    $ current_voice = "voice/CRS06A_OKA0003.ogg"
    "伦太郎" "「真……真由理……真由理！真由理！！！对不起，我……我！」"
    "惨叫声响彻了整个房间。他就那样慢慢地蹲了下去，呜咽地重复着真由理的名字。"
    $ stopvoc("CRS")
    play CRS "CRS06A_CRS0007A"
    $ current_voice = "voice/CRS06A_CRS0007A.ogg"
    "红莉栖" "「冈部……」"
    $ stopvoc("FEI")
    play FEI "CRS06A_FEI0006"
    $ current_voice = "voice/CRS06A_FEI0006.ogg"
    "菲利斯" "「凶真……」"
    "我们看到冈部这幅样子，一下不知该怎么办才好，就这么愣在了原地。"
    "我们之中，只有管家冷静地观察了一下房间。"
    $ stopvoc("Y13")
    play voc "CRS06A_Y130000"
    $ current_voice = "voice/CRS06A_Y130000.ogg"
    "黒木" "「唔……失礼了。」"
    window hide



    $ loadBG(2,"BG02N1")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='voc')",DynamicDisplayable(mouthanime,"KUR_ASA01"),"True","lh/KUR_ASA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    "他绕过狼狈不堪的我们，毫无顾忌地走近血迹，确认起了情况。"

    stop bgm 
    $ stopvoc("Y13")
    play voc "CRS06A_Y130001"
    $ current_voice = "voice/CRS06A_Y130001.ogg"
    "黒木" "「看起来，并没有人死亡。这个出血量，还不至于危及性命。」"
    "管家以冷静的口气如此说道。冈部听后猛地站起来，紧紧地抓住了管家。"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA06"),"True","lh/OKA_ASA06a~ipad.png") at left as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='voc')",DynamicDisplayable(mouthanime,"KUR_ASA01"),"True","lh/KUR_ASA01a~ipad.png") at right as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "CRS06A_OKA0005"
    $ current_voice = "voice/CRS06A_OKA0005.ogg"
    "伦太郎" "「不会危及到性命！？那，那就是没事吗，真由理吗？还有桶子也是！？」"
    "冈部的表情，说是恶鬼缠身也不为过。"
    "冈部他，认为地上的血迹是真由理或桶子的——几乎已经确信了。"
    $ stopvoc("Y13")
    play voc "CRS06A_Y130002"
    $ current_voice = "voice/CRS06A_Y130002.ogg"
    "黒木" "「至少能确定的是，没有谁在这里被杀掉。从血迹来看，应该是被枪一类的武器袭击，但没有倒下的痕迹。」"
    $ stopvoc("Y13")
    play voc "CRS06A_Y130003"
    $ current_voice = "voice/CRS06A_Y130003.ogg"
    "黒木" "「有争斗过的痕迹，不过是在站立的状态下进行的，恐怕是在有意识的状态下，力气用尽后被带走的……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA07"),"True","lh/OKA_ASA07a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "CRS06A_OKA0006"
    $ current_voice = "voice/CRS06A_OKA0006.ogg"
    "伦太郎" "「被带走了……ＳＥＲＮ……Ｒｏｕｎｄｅｒ……」"
    "泪水从眼角滚落，一脸绝望的冈部彻底崩溃了。"
    window hide



    $ loadBG(2,"BG02N1")





    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_AMA07"),"True","lh/OKA_AMA07a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    "此时我用力抓住了力尽快要倒下的冈部的手臂。"
    play bgm "BGM21"
    $ stopvoc("CRS")
    play CRS "CRS06A_CRS0008"
    $ current_voice = "voice/CRS06A_CRS0008.ogg"
    "红莉栖" "「好好告诉我，冈部！到底发生了什么！？真由理和桥田怎么了？」"
    "无论怎么想要冷静下来都办不到。因为有两名朋友，留下血迹后消失了。"
    $ stopvoc("OKA")
    play OKA "CRS06A_OKA0007"
    $ current_voice = "voice/CRS06A_OKA0007.ogg"
    "伦太郎" "「……恐怕，只恐怕，他们两人被ＳＥＲＮ的Ｒｏｕｎｄｅｒ给带走了。」"
    $ stopvoc("CRS")
    play CRS "CRS06A_CRS0009"
    $ current_voice = "voice/CRS06A_CRS0009.ogg"
    "红莉栖" "「ＳＥＲＮ……是指！？」"
    $ stopvoc("OKA")
    play OKA "CRS06A_OKA0008"
    $ current_voice = "voice/CRS06A_OKA0008.ogg"
    "伦太郎" "「是时间机器。那些家伙察觉到我们的存在了……」"
    "让人心跳骤停的冲击。"
    "ＳＥＲＮ。……欧洲原子能研究机构。世界最大的粒子物理学研究机构。"
    "但同时，这个组织已经进行了４０年以上的时间机器研究，并对世界隐瞒了其成果与真相。"
    "由于他们秘密进行的时间机器研究，已经不知有多少人在进行人体试验时牺牲了。"
    $ stopvoc("CRS")
    play CRS "CRS06A_CRS0010"
    $ current_voice = "voice/CRS06A_CRS0010.ogg"
    "红莉栖" "「等一下！就算是因为我们做出了时间跳跃机，可为什么ＳＥＲＮ要抓走真由理和桥田！？」"
    $ stopvoc("CRS")
    play CRS "CRS06A_CRS0011"
    $ current_voice = "voice/CRS06A_CRS0011.ogg"
    "红莉栖" "「还有，研究机关是怎么做到这种事的！？」"
    $ stopvoc("OKA")
    play OKA "CRS06A_OKA0009"
    $ current_voice = "voice/CRS06A_OKA0009.ogg"
    "伦太郎" "「在ＳＥＲＮ旗下，有个名为Ｒｏｕｎｄｅｒ的执行部队……」"
    $ stopvoc("OKA")
    play OKA "CRS06A_OKA0010"
    $ current_voice = "voice/CRS06A_OKA0010.ogg"
    "伦太郎" "「那帮家伙为了独占时间机器，袭击了正在办派对的我们……然后，在这里杀掉了真由理……」"
    $ stopvoc("CRS")
    play CRS "CRS06A_CRS0012"
    $ current_voice = "voice/CRS06A_CRS0012.ogg"
    "红莉栖" "「诶……可是，刚才管家说……」"
    window hide



    $ loadBG(2,"BG02N1")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='voc')",DynamicDisplayable(mouthanime,"KUR_ASA01"),"True","lh/KUR_ASA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    "冈部说的话，让我不由得望向了刚刚说「这里没有死人」的管家。"
    $ stopvoc("Y13")
    play voc "CRS06A_Y130004"
    $ current_voice = "voice/CRS06A_Y130004.ogg"
    "黒木" "「…………」"
    "管家面带惊讶地摇了摇头。看来他对自己的判断很有自信，但同时因冈部的话产生了疑问。"
    "这些疑问，在冈部接下来的话中得到了解答。"
    window hide



    $ loadBG(2,"BG02N1")





    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_AMA06"),"True","lh/OKA_AMA06a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    $ stopvoc("OKA")
    play OKA "CRS06A_OKA0011"
    $ current_voice = "voice/CRS06A_OKA0011.ogg"
    "伦太郎" "「所以我，为了改变过去进行了跳跃……用那个时间跳跃机！」"
    $ stopvoc("CRS")
    play CRS "CRS06A_CRS0013"
    $ current_voice = "voice/CRS06A_CRS0013.ogg"
    "红莉栖" "「那……这么说，你！？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_AMA07"),"True","lh/OKA_AMA07a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "CRS06A_OKA0012"
    $ current_voice = "voice/CRS06A_OKA0012.ogg"
    "伦太郎" "「我……穿越了时间。」"
    "顷刻间大脑一片空白。"
    "如果要证实这台机器的有效性，人体实验是必不可少的，为此我们甚至放弃了时间跳跃实验。"
    "我可以自信地说理论是完美的。但是，再完美的理论，不经过验证和实验，其正确性也是不能被认可的。"
    "所以在决定放弃实验而松了一口气的同时，果然还是有强烈的惋惜感。"
    "但是，刚才冈部的话，正是对时间跳跃机有效性的论证。"
    "要说不开心……那是骗人的。"
    "身为研究者，没有比自己的新理论被证明正确时更幸福的瞬间了。"
    "那一瞬间，我忘却了至此为止的一切，只想向冈部询问更多的问题。"
    "但是这个刚浮上来的念头，马上就被冈部悲痛的叫声打消了。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_AMA06"),"True","lh/OKA_AMA06a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "CRS06A_OKA0013"
    $ current_voice = "voice/CRS06A_OKA0013.ogg"
    "伦太郎" "「……为了救真由理！」"
    "救……真由理？"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_AMD02"),"True","lh/OKA_AMD02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "CRS06A_OKA0014"
    $ current_voice = "voice/CRS06A_OKA0014.ogg"
    "伦太郎" "「但是！这是为什么！？为什么，救不了她！为什么？为什么真由理一定要死！？」"
    "“真由理一定会死”"
    "这句残酷的话让我全身颤抖起来。"
    $ stopvoc("CRS")
    play CRS "CRS06A_CRS0014"
    $ current_voice = "voice/CRS06A_CRS0014.ogg"
    "红莉栖" "「等，等等啊！？如果这是真的，为什么不先去找警察呢？」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_AMA06"),"True","lh/OKA_AMA06a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "CRS06A_OKA0015"
    $ current_voice = "voice/CRS06A_OKA0015.ogg"
    "伦太郎" "「找过了，根本不信！这么荒唐滑稽的事，他们怎么可能相信！」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_AMD01"),"True","lh/OKA_AMD01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "CRS06A_OKA0016"
    $ current_voice = "voice/CRS06A_OKA0016.ogg"
    "伦太郎" "「……而且，真由理还曾被警察杀过。是偶然，是事故？还是说在警察中也有Ｒｏｕｎｄｅｒ的人……我也不知道具体的细节。」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_AMD02"),"True","lh/OKA_AMD02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "CRS06A_OKA0017"
    $ current_voice = "voice/CRS06A_OKA0017.ogg"
    "伦太郎" "「可是，无论我怎么做真由理都会被杀！我没法依赖任何人，没法告诉任何人……只能，一次次地反复重来！却救不了……真由理！！」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    "冈部悲痛欲绝地吼叫着。"
    "不断地不断地重复的，真由理的死。"
    "不断地不断地，反复进行时间跳跃。"
    "就像无限延伸的地狱般，残酷时刻的轮回着。永劫的悲剧循环。"
    "无论重来多少次，真由理必定会因某种形式、手段、情况，死于１９点至２０点中的某一刻。"
    "──说的更准确一点，有一次真由理的死发生在稍晚一点。"
    "那时候，大约２０点左右，收到了真由理被胶状化的照片。"
    window hide


    $ loadBG(2,"BG02N1")







    "我慌忙看了下时钟。"
    "已经，过了２０点。如果冈部所言的都是真的，那真由理已经——"
    $ stopvoc("OKA")
    play OKA "CRS06A_OKA0018"
    $ current_voice = "voice/CRS06A_OKA0018.ogg"
    "伦太郎" "「哈……！」"
    "冈部发出了声音。"
    window hide

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_AMA06"),"True","lh/OKA_AMA06a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)




    "看样子，他注意到我的视线移向了时钟，自己也向时钟看去。"
    "然后他发现，现在已经过了２０点。"
    "──糟了。"
    "在我咬牙切齿地痛恨自己的失误前，冈部已经目光呆滞。"
    "——绝望地目光呆滞。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_AMD02"),"True","lh/OKA_AMD02a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "CRS06A_OKA0019"
    $ current_voice = "voice/CRS06A_OKA0019.ogg"
    "伦太郎" "「啊啊啊啊啊啊啊，真、真由理……！我、我————————啊啊，啊啊啊啊啊啊啊，哇啊啊啊啊啊——————————————」"
    "如此的哀叹，迄今为止我从未听到过。"
    "大概，我今后的一生中也不会再听到吧。就是这种程度的哀叹。"
    "冈部大受打击，已经几近错乱。"
    "他使劲地抓着头，两手颤抖着，这时管家静静地靠了上去——"

    stop bgm 
    play se "SGSE080"

    $ stopvoc("OKA")
    play OKA "CRS06A_OKA0020"
    $ current_voice = "voice/CRS06A_OKA0020.ogg"
    "伦太郎" "「呜……」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    "下一个瞬间，冈部哼了一声便倒下了。"
    "……似乎是失去意识了。"
    window hide



    $ loadBG(2,"BG02N1")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='voc')",DynamicDisplayable(mouthanime,"KUR_ASA01"),"True","lh/KUR_ASA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    $ stopvoc("Y13")
    play voc "CRS06A_Y130005"
    $ current_voice = "voice/CRS06A_Y130005.ogg"
    "黒木" "「……实在是有些失礼。但这样下去会对冈部先生的心理健康造成危害。」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_BSC03"),"True","lh/FEI_BSC03a~ipad.png") at left as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh6 
    show expression ConditionSwitch("renpy.music.get_playing(channel='voc')",DynamicDisplayable(mouthanime,"KUR_ASA01"),"True","lh/KUR_ASA01a~ipad.png") at right as lh6 zorder (10-6) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FEI")
    play FEI "CRS06A_FEI0007"
    $ current_voice = "voice/CRS06A_FEI0007.ogg"
    "菲利斯" "「不……谢谢你，黑木。我也认为现在让凶真睡下来比较好。因为，因为……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_BSC04"),"True","lh/FEI_BSC04a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FEI")
    play FEI "CRS06A_FEI0008"
    $ current_voice = "voice/CRS06A_FEI0008.ogg"
    "菲利斯" "「他实在是……太痛苦了啊……」"
    "菲利斯的眼角也渗出了泪水。"
    "老实说，我也没办法将冈部说的话全部当作现实来接受。"
    "但是，看到冈部这幅样子，我不得不去相信。"
    "我想要，去相信他。"
    "既然这样……"
    $ stopvoc("CRS")
    play CRS "CRS06A_CRS0015"
    $ current_voice = "voice/CRS06A_CRS0015.ogg"
    "红莉栖" "「无论如何，不能这样就算了。不做点什么的话……」"
    "ＳＥＲＮ，３００人委员会，Ｒｏｕｎｄｅｒ。像是从冈部的厨二病妄想中穿越出来的，恶梦。"
    "但是，它们却真实存在于现实中，还连同绝望一道横挡在我们面前。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_BSC03"),"True","lh/FEI_BSC03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FEI")
    play FEI "CRS06A_FEI0009"
    $ current_voice = "voice/CRS06A_FEI0009.ogg"
    "菲利斯" "「该，该怎么办啊？我的思路完全跟不上……」"
    $ stopvoc("CRS")
    play CRS "CRS06A_CRS0016"
    $ current_voice = "voice/CRS06A_CRS0016.ogg"
    "红莉栖" "「不得不思考啊……」"
    "脑海中浮现出真由理和桥田的面容。"
    "以及，在我面前即使失去意识也痛苦着的冈部。"
    "……我实在无法放着不管。"
    "正如我在因爸爸的事情烦恼时，冈部不会置之不理一样……"

    hide screen phoneSD1
    window hide
    scene expression Solid("000000")  with fade





    return
