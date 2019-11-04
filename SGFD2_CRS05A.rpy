label SGFD2_CRS05A:
    window hide


    $ loadBG(0,"BG13N2")


    $ date="8/13"
    show screen phonebtn
    show screen phoneSD1

    "As I wandered the streets in search of Okabe I suddenly noticed how crowded the streets were."
    $ stopvoc("Y30")
    play voc "CRS05A_Y300000"
    $ current_voice = "voice/CRS05A_Y300000.ogg"
    "Worker A" "「Hey the trains have stopped due to terrorism...」"
    $ stopvoc("X07")
    play voc "CRS05A_X070000"
    $ current_voice = "voice/CRS05A_X070000.ogg"
    "Worker B" "「Huh? Terrorism oh! I'm going to be late to a meeting!」"
    "Disturbing words reached my ears."
    play bgm "BGM25"
    "Terrorism... in Japan?!"
    "Of course the times had changed from the old days and political unrest was rising along with probability of terrorism occuring."
    "Become my research institutes was also a possible target I had been forced to attend lecture about this."
    "But as I suspected Japan had a sterotype of being a peaceful country where little to no terrorism occured."
    "When i looked indeed the trains had stopped. The trains that usually incessantly arrived were nowhere to be seen."
    window hide
    hide screen phonebtn
    hide screen phonebtn2
    show screen phone(interact=False)
    "Opening my phone and looking at @channel it seemed this was one of the hot topics that had broken on the news."
    window hide
    call hide_phone
 #   call screen phoneweb("txt/ATCH_PH001.txt")
    call screen phoneweb("txt/ATCH_PH001e.txt")

    "An image of the stations staff stopping trains and customers had been posted on @channel."
    "Some time had passed since this commotion started."
    "And in front of Akihabara station there were too many people that it would also be hard to cross to the other side of the station on foot."
    "What should I do... With this situation it would be hard to search for Okabe..."
    "But... if Okabe was caught up in some terrorist plot..."
    "Several possibilities were bubbling up in my brain whirling around and disappearing."
    "Anxiety. Optimism. Pessimism. Fear. Impatience. Uneasiness."
    "I was itching to do something."
    "But I couldn't decide what the right thing to do was."
    "Moving carelessly would be fatal then what should I do? I couldn't come to a conclusion at all."
    window hide
    $ targetmailid = gc["ScriptMacros"]["FM_CRS05A_RECV_FEI01"]
    if phonemailring!= "":
        play se phonemailring
    if persistent.skipmail==False:
        $ renpy.choice_for_skipping()
    if targetmailid != "":
        $ RcvMail(targetmailid)
        $ targetmailid=""

    hide screen phonebtn
    hide screen phonebtn2
    show screen phone(interact=False)
    pause 2
    call read_last_mail




    stop bgm 
    "Faris-San? If I remember correctly she was LabMem 007."
    window hide



    "What a relief. It seems Okabe was found."
    "However I was still worried that he was acting strange."
    "I didn't know what exactly had happend but an unpleasant premonition slid down my spine."
    window hide








    call send_mail (id=[107,108,109,110])
    $ ReplyMail(106)
    call hide_phone

    "Sending a reply I took a deep breath."
    "The anxiety felt like it would crush my chest."
    $ stopvoc("CRS")
    play CRS "CRS05A_CRS0000"
    $ current_voice = "voice/CRS05A_CRS0000.ogg"
    "Kurisu" "「Okabe... What happend to you...」"
    "Dragging my feet behind me I turned back the way I had come."

    hide screen phoneSD1
    window hide
    scene expression Solid("000000")  with fade





    return
