label SGFD2_CRS04A:
    window hide


    $ loadBG(0,"BG21E")
    play se "SGSE152"

    play se "SGSE004L" loop


    $ date="8/13"
    show screen phonebtn
    show screen phoneSD1


    stop se
    "I had run all over Akihabara looking for Okabe from the Kanda Shrine and also Central Avenue. I ended up coming to an alley behind the large building."
    "The sun had almost set, the August evening sky was dyed in a shade of honey amber."
    $ stopvoc("CRS")
    play CRS "CRS04A_CRS0000"
    $ current_voice = "voice/CRS04A_CRS0000.ogg"
    "Kurisu" "「Where the hell are you……I'm……at my limit……」"
    "I was out of breath... While I wasn't out of shape. I hadn't run this much in a long time."
    window hide




























    "As I was thirsty I suddenly noticed a vending machine."
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_DOCPE"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_DOCPE"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_DOCPE"])
    $ stopvoc("CRS")
    play CRS "CRS04A_CRS0001"
    $ current_voice = "voice/CRS04A_CRS0001.ogg"
    "Kurisu" "「I see... They don't have{color=#f00} Ｄｒ．Ｐｅｐｐｅｒ {/color}.」"
    "Regardless of my usual self right now I really wanted to drink something fizzy but since they didn't have my favorite I reluctantly bought a can of coffee."
    $ stopvoc("CRS")
    play CRS "CRS04A_CRS0002"
    $ current_voice = "voice/CRS04A_CRS0002.ogg"
    "Kurisu" "「……」"



























    "Taking a breath I looked around."
    "There was no sign of Okabe here either..."
    $ stopvoc("CRS")
    play CRS "CRS04A_CRS0003"
    $ current_voice = "voice/CRS04A_CRS0003.ogg"
    "Kurisu" "「Where the hell did he go... that guy...」"
    play bgm "FDBGM04"
    "While my tone sounded like I wanted to abuse him it came more from a sense of worry than one of anger."
    "Throwing the empty can in the recycling I continued to look around."
    "Seriously why had I become so desperate..."
    $ stopvoc("CRS")
    play CRS "CRS04A_CRS0004"
    $ current_voice = "voice/CRS04A_CRS0004.ogg"
    "Kurisu" "「Because you're my close friend...」"
    "Probably because Okabe had said that to me..."
    "When did I start to worry so much about Okabe anyway..."
    "Recently I had found him fascinating to observe but when did it become something more than a mere interest?"
    "We had only met several days ago... A lot of my reservations had disappeared..."
    "I had initally thought him rude and a criminal so there was nothing to even think about being shy about..."
    "I hadn't been so aware of myself since I was putting on an act in America..."
    "Even when Hashida and Okabe talked about stupid things and although there were times I got it was never painful."
    "It seemed that... while I hated to admit it... I must be in love with... Okabe."
    "The turning point was probably when we went to Aomori together."
    hide screen phoneSD1
    window hide

    stop se


    $ loadBG(0,"BG03A4",trans=Fade(0.5,1.0,0.5,color="fff"))

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASA01"),"True","lh/OKA_ASA01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)


    hide screen phonebtn
    $ stopvoc("OKA")
    play OKA "CRS04A_OKA0000"
    $ current_voice = "voice/CRS04A_OKA0000.ogg"
    "Rintarou" "「You are my assistant. What worries you worries me. I plan to do anything to make sure you are in your best mental condition so you can work.」"
    "To be honest those lines sounded like a proposal. When I heard it, it was like time had stopped."
    window hide


    $ loadBG(0,"BG21E",trans=Fade(0.5,1.0,0.5,color="fff"))

    play se "SGSE004L" loop

    show screen phonebtn
    show screen phoneSD1
    $ stopvoc("CRS")
    play CRS "CRS04A_CRS0005"
    $ current_voice = "voice/CRS04A_CRS0005.ogg"
    "Kurisu" "「You are a little annoying……」"
    "I suspected that Okabe didn't just say that to anyone."
    "Otherwise of the 8 Labmems 6... I mean 5 wouldn't be girls."
    "Because he said such things a girl like me would end up misunderstanding..."
    "He probably knew that... that idiot..."
    "And even so I still liked him or perhaps it was because of the secretion of dopamine which caused this..."
    "Since that day we went to Amoroi even though I knew Okabe was an idiot I decided to let more of his idiocy slide."
    "And by doing so even his Chuuniboy actions sometimes had meaning to it and sometimes were even appropriate at times."
    window hide


    $ loadBG(2,"IBGX033")



    hide screen phonebtn
    "God dammnit! As I thought this was hard to admit!!!"
    "...It was hard to admit. While it was hard to admit.. that is to say.. I mean..."
    "As I thought he was cool..."
    "Without realizing my own heart had started to forgive him."
    "Imperceptibly he became a person I could relax with."
    "Actually now that I had realized my feelings I might be even more nervous..."
    "But it was too late to change. I couldn't change the way that I felt now that I had let him in."
    "Society's mask of a neuroscience researcher of the Victor Mitochondria University..."
    "Especially in front of Okabe I decided not to wear it."
    "And like I had never experienced in my life before my mind was at ease being myself."
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_ATTCHANNEL"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_ATTCHANNEL"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_ATTCHANNEL"])
    "That was exactly the comfort I got by writing threats on{color=#f00}＠ｃｈａｎｎｅｌ{/color}."
    "However... at the same time Okabe was being tormented by something. I could no longer proceed like before."
    "I still didn't know what the cause of it was. If he wasn't the same Okabe that I knew then it would drive me crazy too."
    "I felt stifled at the bottom of my heart."
    "I hated that feeling."
    window hide


    $ loadBG(2,"BG21E")



    show screen phonebtn
    $ stopvoc("CRS")
    play CRS "CRS04A_CRS0006"
    $ current_voice = "voice/CRS04A_CRS0006.ogg"
    "Kurisu" "「Just being burdened all by yourself... you should tell me about it too... You listened to my worries didn't you?」"

    stop bgm 


    stop se




    "My thinking was unexpectedly drowned out by the sound of my phone."

    "Was it Okabe?"



    window hide
    hide screen phonebtn
    hide screen phonebtn2
    show screen phone(interact=False)

    "I looked at the screen expectantly but only Hashida's name was displayed."





    $ stopvoc("CRS")
    play CRS "CRS04A_CRS0007"
    $ current_voice = "voice/CRS04A_CRS0007.ogg"
    "Kurisu" "「Hello?」"

    $ stopvoc("DAR")
    play DAR "CRS04A_DAR0000"
    $ current_voice = "voice/CRS04A_DAR0000.ogg"
    "Itaru" "「Ah hello Miss Makise? What happend? When I got back to the lab nobody was there...」"

    "I quickly explained about Okabe acting strange to Hashida."
    "I had tried looking alone based on my impulses but there were limits to what I could do by myself."

    $ stopvoc("DAR")
    play DAR "CRS04A_DAR0001"
    $ current_voice = "voice/CRS04A_DAR0001.ogg"
    "Itaru" "「Um... What happened to Okarin? I see. I'll try to figure something out too.」"
    $ stopvoc("DAR")
    play DAR "CRS04A_DAR0002"
    $ current_voice = "voice/CRS04A_DAR0002.ogg"
    "Itaru" "「I'll tell everyone to contact you if they figure something out.」"

    $ stopvoc("CRS")
    play CRS "CRS04A_CRS0008"
    $ current_voice = "voice/CRS04A_CRS0008.ogg"
    "Kurisu" "「Got it. Please do that.」"
    window hide


    "It would be great if someone could find some kind of clue but..."
    window hide
    call hide_phone
    "As I closed my phone I prayed that I could find Okabe and then started running once more in Akihabara."

    hide screen phoneSD1
    window hide
    scene expression Solid("000000")  with fade





    return
