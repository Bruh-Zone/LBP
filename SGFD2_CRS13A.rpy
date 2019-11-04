label SGFD2_CRS13A:
    window hide




    $ loadBG(2,"IBGX048")




    play bgm "FD2BGM08"

    $ date="8/14"
    hide screen phonebtn
    show screen phoneSD1

    "这其中大多的记忆我几乎都没有，大概那时的我，正海涛般地倾泻着自己的言语。"
    "重度的精神创伤以及和爸爸长年的龃龉，还有对现状的绝望和无法救助冈部的无力感，让我做出了近乎幼童的行为。"
    "把激动的感情全部倾泻而出，这种事要是平时的自己肯定要羞得恨不得找地缝钻进去，更别说偏偏对方还是爸爸。"
    "我记得的，也就只有边不断叫着冈部的名字，边不停地寻求帮助。"
    "身为研究者的矜持，身为社会人的修养和礼仪，全部都化为乌有。"
    "我就这样任由自己的感情毫不掩饰地爆发着，大概都没办法好好将话说清楚吧。"
    "然而就是这种时候，爸爸奇迹般地听进了我的话。"
    "可能是爸爸也因我的异常行为而感到了事情不同寻常。"
    "──也许爸爸中途也有插话进来，只是我没听到。"
    "但爸爸始终没有挂掉电话。"
    window hide
    $ loadBG(0,"BG26A")
    show screen phonebtn

    show screen phone(interact=False,transit=False)




    show screen phoneSD1




    $ stopvoc("NAK")
    play NAK "CRS13A_NAK0000"
    $ current_voice = "voice/CRS13A_NAK0000.ogg"
    "中钵" "「…………」"

    "回过神来……我已经对爸爸倾诉了20分钟以上。最后我的声音，只剩下了细细的啜泣。"
    $ stopvoc("CRS")
    play CRS "CRS13A_CRS0000"
    $ current_voice = "voice/CRS13A_CRS0000.ogg"
    "红莉栖" "「拜托了……爸爸」"

    $ stopvoc("NAK")
    play NAK "CRS13A_NAK0001"
    $ current_voice = "voice/CRS13A_NAK0001.ogg"
    "中钵" "「…………」"
    $ stopvoc("NAK")
    play NAK "CRS13A_NAK0002"
    $ current_voice = "voice/CRS13A_NAK0002.ogg"
    "中钵" "「真是……让人不快的家伙。为什么要我做这种事？ 你是说，要我去帮一个素未谋面的人……？」"

    $ stopvoc("CRS")
    play CRS "CRS13A_CRS0001"
    $ current_voice = "voice/CRS13A_CRS0001.ogg"
    "红莉栖" "「…………」"
    "爸爸的声音一下让我的心都凉了。像是冰刃插进了心脏一样，我的世界和时间都静止了。"
    "不能呼吸的错觉向我袭来，事实上，我也真的恐惧得像在渴求氧气般的张合着嘴唇。"

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='FPP')",DynamicDisplayable(mouthanime,"FPP_AMA01"),"True","lh/FPP_AMA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FPP")
    play FPP "CRS13A_FPP0000"
    $ current_voice = "voice/CRS13A_FPP0000.ogg"
    "菲利斯父亲" "「……容我失礼一下」"
    $ stopvoc("CRS")
    play CRS "CRS13A_CRS0002"
    $ current_voice = "voice/CRS13A_CRS0002.ogg"
    "红莉栖" "「诶？」"
    window hide


    $ loadBG(2,"BG26A")
    call hide_phone



    hide screen phonebtn
    "下个瞬间，我还没有反应过来，幸高叔叔已从我手里拿过了手机。"
    $ stopvoc("FPP")
    play FPP "CRS13A_FPP0001"
    $ current_voice = "voice/CRS13A_FPP0001.ogg"
    "菲利斯父亲" "「……章一，久违了啊。多少也要和朋友联系一下啊？」"
    "我只能这样毫无办法地任由手机被拿走，看着幸高叔叔开始和爸爸对话。"
    "但我也顾不上那么多了，我又被爸爸泼了这样的冷言冷语，看来他也不会替我担心冈部什么了吧。"
    window hide



    $ loadBG(2,"BG26A")





    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_CLC03"),"True","lh/FEI_CLC03a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    $ stopvoc("FEI")
    play FEI "CRS13A_FEI0000"
    $ current_voice = "voice/CRS13A_FEI0000.ogg"
    "菲利斯" "「红喵……」"
    "这时，菲利斯突然过来抱住了我。"
    "我还没有冷静下来，就这么靠在了她的身上。"
    $ stopvoc("CRS")
    play CRS "CRS13A_CRS0003"
    $ current_voice = "voice/CRS13A_CRS0003.ogg"
    "红莉栖" "「菲利斯……我……我……」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_CLC01"),"True","lh/FEI_CLC01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FEI")
    play FEI "CRS13A_FEI0001"
    $ current_voice = "voice/CRS13A_FEI0001.ogg"
    "菲利斯" "「现在，交给爸爸就好了……凶真他，已经让黑木带走了。」"
    $ stopvoc("CRS")
    play CRS "CRS13A_CRS0004"
    $ current_voice = "voice/CRS13A_CRS0004.ogg"
    "红莉栖" "「诶？」"
    window hide


    $ loadBG(2,"BG26A")



    "听了菲利斯的话后我环顾了客厅，确实没看到冈部的身影。似乎带到昨天休息的寝室去了。"
    window hide



    $ loadBG(2,"BG26A")





    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_CLC04"),"True","lh/FEI_CLC04a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    $ stopvoc("FEI")
    play FEI "CRS13A_FEI0002"
    $ current_voice = "voice/CRS13A_FEI0002.ogg"
    "菲利斯" "「现在的凶真，实在太过辛苦了。」"
    $ stopvoc("CRS")
    play CRS "CRS13A_CRS0005"
    $ current_voice = "voice/CRS13A_CRS0005.ogg"
    "红莉栖" "「……嗯……嗯」"
    "这时的我，又有一半回到了孩子的状态。"
    "所以虽然我自己也没资格说，刚才冈部的反应，我实在不忍心看下去。"
    "就像是什么东西被磨到了极限一样，冈部的身心某处也有什么超越了限界吧。"
    "这种时候，人只会有以下两种情况，对一切都感到麻木虚无，或是在激烈的恸哭下连自己的心都抹杀掉。"
    "不，无论哪种情况都等于自身消失掉了。 只不过，这回的反应是后者而已。"
    "那悲叹之深切，连未曾亲自经历过程的我都被深深撼动了。"
    "我居然会为爸爸以外的事如此感情用事，真的想都没想过。"
    "不过我注意到，这不就正恰恰说明了冈部经历的事情有多悲惨么。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_CLC01"),"True","lh/FEI_CLC01a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FEI")
    play FEI "CRS13A_FEI0003"
    $ current_voice = "voice/CRS13A_FEI0003.ogg"
    "菲利斯" "「……呐，红喵」"
    $ stopvoc("CRS")
    play CRS "CRS13A_CRS0006"
    $ current_voice = "voice/CRS13A_CRS0006.ogg"
    "红莉栖" "「……嗯」"
    "我多少找回了些冷静，菲利斯就这么抱着我，叫我的名字。"
    $ stopvoc("FEI")
    play FEI "CRS13A_FEI0004"
    $ current_voice = "voice/CRS13A_FEI0004.ogg"
    "菲利斯" "「昨天，凶真说过，他很多次看到了真由氏的死亡……」"
    $ stopvoc("FEI")
    play FEI "CRS13A_FEI0005"
    $ current_voice = "voice/CRS13A_FEI0005.ogg"
    "菲利斯" "「为了阻止真由氏的死，进行了无数次的时间跳跃……」"
    $ stopvoc("CRS")
    play CRS "CRS13A_CRS0007"
    $ current_voice = "voice/CRS13A_CRS0007.ogg"
    "红莉栖" "「……嗯。」"
    "菲利斯摸着我的头，时不时敲着我的背轻轻细语。"

    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_CLC03"),"True","lh/FEI_CLC03a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FEI")
    play FEI "CRS13A_FEI0006"
    $ current_voice = "voice/CRS13A_FEI0006.ogg"
    "菲利斯" "「那，和他一样进行时间回溯的话……能……救真由氏吗？」"
    "已死好友的性命。如果有取回的手段，无论那是怎样的手段，人们都会采取。"
    "而时间机器，就是这样禁断的果实。"
    "我……身为研究者，十分清楚那是多么需要谨慎的东西。"
    "可是……就算是那样，我也只能如此回答她。"
    $ stopvoc("CRS")
    play CRS "CRS13A_CRS0008"
    $ current_voice = "voice/CRS13A_CRS0008.ogg"
    "红莉栖" "「能救她的。真由理……一定会得救的。我会让事实变成那样的……」"
    "冈部目击真由理的死亡时，大概就是我现在这样的心情吧。"
    "时间机器的危险性和诱惑，以及对伦理观带来的威胁。即使把这些都放到天秤上衡量，只要有能救真由理的手段也还是会去用。"
    "无论这是多重的罪，还是怎样不容冒渎的万物法则，只要手段存在，人就必定会去使用。"
    "就算要屈服于那个法则也好……只要能救真由理，这些都算得了什么呢。"
    "如果可以让冈部不再露出那样的表情，这些都算得了什么呢。"
    "要背负多少罪都可以，要受什么样的惩罚都可以。 所以拜托了，以此为代价……把她的生命，还回来吧。"
    "我知道这是在反抗自然的真理，但是....... "
    $ stopvoc("FPP")
    play FPP "CRS13A_FPP0002"
    $ current_voice = "voice/CRS13A_FPP0002.ogg"
    "菲利斯父亲" "「红莉栖酱……」"
    window hide



    $ loadBG(2,"BG26A")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='FPP')",DynamicDisplayable(mouthanime,"FPP_ASA01"),"True","lh/FPP_ASA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    "这时幸高叔叔朝我说话了。手上还拿着处于通话状态的我的手机。"
    $ stopvoc("FPP")
    play FPP "CRS13A_FPP0003"
    $ current_voice = "voice/CRS13A_FPP0003.ogg"
    "菲利斯父亲" "「和章一说吧……我让他帮忙了。」"
    $ stopvoc("CRS")
    play CRS "CRS13A_CRS0009"
    $ current_voice = "voice/CRS13A_CRS0009.ogg"
    "红莉栖" "「诶……！」"
    "骗人的吧。"
    "爸爸？ 帮忙？ 怎么回事？"
    "这话对我来说太难以置信了，我一时没有反应过来。幸高叔叔在旁边看着我，把手机放在了桌上。"
    window hide


    $ loadBG(2,"IBG051A")




    "而且手机正处于所有人都能对话的扬声状态。"
    $ stopvoc("FPP")
    play FPP "CRS13A_FPP0004"
    $ current_voice = "voice/CRS13A_FPP0004.ogg"
    "菲利斯父亲" "「那，拜托你了。」"
    $ stopvoc("NAK")
    play NAK "CRS13A_NAK0003"
    $ current_voice = "voice/CRS13A_NAK0003.ogg"
    "中钵" "「哼……你总是这样。一会儿听人话一会儿又不听人说了。 到最后，总把人煽动得按你自己的意思去行事。」"
    $ stopvoc("FPP")
    play FPP "CRS13A_FPP0005"
    $ current_voice = "voice/CRS13A_FPP0005.ogg"
    "菲利斯父亲" "「我以前说过的吧？ 这也是商务技巧的一环。好了，开始吧。」"
    $ stopvoc("NAK")
    play NAK "CRS13A_NAK0004"
    $ current_voice = "voice/CRS13A_NAK0004.ogg"
    "中钵" "「哼……真是的。」"
    "我还没有理解清楚现状，幸高叔叔就这么在我眼前和爸爸在对话。"
    "这还真是已经很久很久没有见过的……不带怒吼不带情绪的爸爸的声音。"
    $ stopvoc("NAK")
    play NAK "CRS13A_NAK0005"
    $ current_voice = "voice/CRS13A_NAK0005.ogg"
    "中钵" "「红莉栖。」"
    $ stopvoc("CRS")
    play CRS "CRS13A_CRS0010"
    $ current_voice = "voice/CRS13A_CRS0010.ogg"
    "红莉栖" "「啊！ ……啊，嗯。 爸……爸爸。」"
    "冷不丁被叫了名字，我惊得冷汗都快出来了。总算是先答应了，但完全不像平时那么自然。"
    $ stopvoc("NAK")
    play NAK "CRS13A_NAK0006"
    $ current_voice = "voice/CRS13A_NAK0006.ogg"
    "中钵" "「……从幸高那里听了，虽然还有很多不清楚的地方。不过，总之这看起来不是在开玩笑。」"
    $ stopvoc("NAK")
    play NAK "CRS13A_NAK0007"
    $ current_voice = "voice/CRS13A_NAK0007.ogg"
    "中钵" "「…………」"
    "然后，爸爸沉默了一会儿。"
    "看起来像是不知道该说什么好。"
    "这也难怪。因为就连我自己，在认知电话微波炉的时候，也感到完全不能理解。"
    "虽然在我的哭泣和幸高叔叔的说服之下，爸爸理解这事态并不是开玩笑或恶作剧了，但一时间还是很难接受吧。"
    $ stopvoc("NAK")
    play NAK "CRS13A_NAK0008"
    $ current_voice = "voice/CRS13A_NAK0008.ogg"
    "中钵" "「……唔，先从最根本的开始吧。红莉栖，你真的做出了时间机器吗？」"
    $ stopvoc("CRS")
    play CRS "CRS13A_CRS0011"
    $ current_voice = "voice/CRS13A_CRS0011.ogg"
    "红莉栖" "「嗯，嗯嗯……做出来了。不过，肉体还……」"
    $ stopvoc("NAK")
    play NAK "CRS13A_NAK0009"
    $ current_voice = "voice/CRS13A_NAK0009.ogg"
    "中钵" "「基于什么理论？ 虫洞吗？ 还是发现了超光速物质？ 还是说，反粒子！」"
    $ stopvoc("NAK")
    play NAK "CRS13A_NAK0010"
    $ current_voice = "voice/CRS13A_NAK0010.ogg"
    "中钵" "「有把场内的能量变为无限大的办法吗，也太不现实了……！那这样，果然还是——」"
    window hide

    $ loadBG(2,"BG26A")



    "我说到一半，爸爸怒涛般的质问就开始了。"
    "这是在问我，还是他一个人的自问自答呢，我一下子分辨不出来。"
    "这是研究者常有的状态，但眼下爸爸变成这个状态，实在是让人头疼的事。"

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='FPP')",DynamicDisplayable(mouthanime,"FPP_ASA02"),"True","lh/FPP_ASA02a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("FPP")
    play FPP "CRS13A_FPP0006"
    $ current_voice = "voice/CRS13A_FPP0006.ogg"
    "菲利斯父亲" "「喂，章一。你跑题了。」"
    "看来幸高叔叔也一样感到困扰，而用为难的口气打断了爸爸。"
    "叔叔多半是为了给我打援助，才把电话调成扬声状态的吧。"
    $ stopvoc("NAK")
    play NAK "CRS13A_NAK0011"
    $ current_voice = "voice/CRS13A_NAK0011.ogg"
    "中钵" "「幸高，这种东西，如果不能完全理解，我也出不上主意。这可没法提供意见啊？」"
    $ stopvoc("FPP")
    play FPP "CRS13A_FPP0007"
    $ current_voice = "voice/CRS13A_FPP0007.ogg"
    "菲利斯父亲" "「这个我同意。不过人命关天啊，而且也没多少时间了。拜托了。」"
    $ stopvoc("NAK")
    play NAK "CRS13A_NAK0012"
    $ current_voice = "voice/CRS13A_NAK0012.ogg"
    "中钵" "「哼……」"
    "爸爸的语气明显很是不满，但并不是不高兴。恐怕爸爸对目前情况的认真程度，已经超乎我的想象了。"
    $ stopvoc("NAK")
    play NAK "CRS13A_NAK0013"
    $ current_voice = "voice/CRS13A_NAK0013.ogg"
    "中钵" "「哼，真没办法。……红莉栖，你做的那个时间机器，给我说说原理和状况。」"
    $ stopvoc("CRS")
    play CRS "CRS13A_CRS0012"
    $ current_voice = "voice/CRS13A_CRS0012.ogg"
    "红莉栖" "「好……好的」"
    "就连我，也还没有完全把握事态。"
    "可是我确实能感觉到，现在我们正一点一点地找回父女间的羁绊……"

    hide screen phoneSD1
    window hide

    stop bgm 





    scene expression Solid("000000")  with fade
    return
