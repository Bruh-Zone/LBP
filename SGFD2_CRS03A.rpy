label SGFD2_CRS03A:
    window hide


    $ loadBG(0,"BG03A4")


    $ date="8/13"
    show screen phonebtn
    show screen phoneSD1

    "A little after that..."
    "I was finally able to calm myself down after getting worked up."
    "Mankind's first time traveler."
    "The temptation to time travel using the Time Leap Machine was quite large to be honest."
    "Because it would be a testament to a theory I had personally developed and also uncharted territory for humanity."
    "Because of this it was a feeling similar to those who first set foot on the moon probably."
    "But at the same time I was still afraid. There was also the fear of the unknown and also my fear of my own father."
    play bgm "FD2BGM05"
    "My father Makise Shoich was a time machine researcher."
    "And his theories hadn't been publicly recognized and he was considered a quack amongst the academic commuinty."
    "My father... papa was a labeled a quack and had lost everything."
    "He had been too obsessed with time machines and had lost his job as a researcher. Separating from my mother and I also became estranged with his old friend."
    "Of course doing research meant exploring the far regions which parted from general common sense."
    window hide


    $ loadBG(2,"IBGX044")



    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_BIGBANG"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_BIGBANG"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_BIGBANG"])
    "The{color=#f00}Big Bang Theory{/color}and research on black holes were all laughed at when they were first published."
    "Even the theories that were essential to proving the existence of the universe were considered ridiculous initially."
    "But even so, we shouldn't accept anything that any researcher suggests to be true. More than anything scientific verification was essential."
    "However even though I knew this was true in my head, it had been hard for me to accept."
    "Things that were too crazy or absurd were something I naturally avoided or repelled."
    "To be honest while the big bang theory and black holes seemed to be right. The majority of research was just a bunch of hit air."
    "Moreover there was hardly anything that could validate the theory of time travel actually there was mountins of evidence to deny its existence."
    "In fact one might as well call something that sounded ridiculous as ridiculous."
    "That's why myself as a researcher accepting such a thing caused me a great amount of stress."
    window hide



    $ loadBG(2,"BG03A4")



    "I had a constant fear of following in my father's footsteps and being cast out of the scientific community."
    "In addition it wasn't an exaggeration to say that my papa had dedicated his entire life to time machine research..."
    "If he found out that I and not he had created a time machine I didn't know how he would react. It scared me."
    "After all I had denied the theory of time travel since an early age and we had become estranged so..."
    "But at the same time maybe that's exactly why I had responded so strongly to the theory of time travel..."
    window hide


    $ loadBG(2,"IBG040A")



    hide screen phonebtn
    "Once a Time Leap had been completed and deemed possible. I didn't know whether that woukd mean my father's research would be accepted or not."
    "At the very least he wouldn't be considered ridiculous for researching time machines anymore."
    "Perhaps he would be able to work as a recognized researcher one day once it had become the norm."
    "When I thought like this I couldn't contain myself."
    "Within me I had realized there were several reasons to perform the Time Leap experiments."
    "The curiosity of uncharted territory. My desire as a researcher. My dad being socially recognized. Myself being recognized by my father too."
    "However that was all just my ego. Just for these selfish reasons I didn't have the right to wield the power of God."
    "Okabe's decision to stop experimenting had made me realize that."
    window hide



    $ loadBG(2,"BG03A4")



    show screen phonebtn
    "I sighed a little in my heart."
    "I thought it would take some time for me to acceptit."
    "I thought Okabe was amazing."
    "He made me aware of something that I had lost sight of."
    "He did amazing things but was also a Chuunibyou at times too."
    window hide


    $ loadBG(2,"BG02A2")

    stop bgm 




    "Suddenly I looked at the clock."
    "It was 4:54pm."
    $ stopvoc("CRS")
    play CRS "CRS03A_CRS0000"
    $ current_voice = "voice/CRS03A_CRS0000.ogg"
    "Kurisu" "「Oh it's already this late. With a lack of sleep I'm losing my sense of time.」"
    "It would soon be 5pm..."
    "After we had decided against conducting experiments Mayuri had suggested that we at least celebrate the completion of the machine."
    "After staying up all night working on it I guess it would be boring without some kind of event to get a sense of accomplishment."
    "It wasn't like I was that special or anything even at the American research institutes they held parties for various trival reasons."
    "Our professors and seniors often told us that researchers couldn't without doing such things."
    "For that reason the time to go out shopping for the party was getting closer."
    "Okabe and I were put in charge of buying food and drink and Mayuri had gone to invite the other LabMems. Hashida had his own errands to run."
    play bgm "fd2bgm12"

    $ stopvoc("OKA")
    play OKA "CRS03A_OKA0000"
    $ current_voice = "voice/CRS03A_OKA0000.ogg"
    "Rintarou" "「…………」"
    "At that time Okabe's phone rang unexpectedly."
    "Maybe it was somebody responding to an invitation to the party? Or maybe it was Mayuri or Hashida?"
    window hide
    play se "SGSE158"


    stop bgm 

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ASC01"),"True","lh/OKA_ASC01a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "CRS03A_OKA0001"
    $ current_voice = "voice/CRS03A_OKA0001.ogg"
    "Rintarou" "「…………」"
    "Okabe picked up the phone and let out a breath in silence."
    "From his reaction maybe Hashida had been talking about something. At the very least it didn't seem like Mayuri was calling him."
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    "In order to get ready to go out I headed to the couch where I had left my jacket."
    "And then I could see Okabe brandishing a metal chair in my peripheral vision."
    play bgm "BGM08"
    $ stopvoc("CRS")
    play CRS "CRS03A_CRS0001"
    $ current_voice = "voice/CRS03A_CRS0001.ogg"
    "Kurisu" "「Okabe! What are you doing?!」"
    window hide


    $ loadBG(3,"BG_BLACK")






    $ loadBG(1,"BG03A4")








    "I was astonished by the sight I saw and clung to Okabe."
    "I grabbed Okabe's hand which swung the metal chair in the air."
    "I was too surprised that my mind couldn't keep up."
    "What exactly was Okabe trying to do right now?"
    "I hadn't seen wrong the thing Okabe was trying to destroy before putting down the chair was..."
    window hide


    $ loadBG(2,"IBG040A")



    hide screen phonebtn
    "The Time Leap machine."
    $ stopvoc("CRS")
    play CRS "CRS03A_CRS0002"
    $ current_voice = "voice/CRS03A_CRS0002.ogg"
    "Kurisu" "「Just now did you try to destroy it?」"
    "I couldn't believe it."
    "The one who cared the most for that machine was Okabe himself."
    "Of course there were many things that we shouldn't use this machine for. But it's existence would surely bring a new dawn of development and advance mankind."
    "And now he wanted to destroy it?!"
    "Now that we had come this far this machine wasn't only ours but it belonged to the entire human race."
    "To destroy such a Time Leap machine from a single individuals will was something that should never happen."
    window hide



    $ loadBG(2,"BG03A4")

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_AMA06"),"True","lh/OKA_AMA06a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)



    show screen phonebtn
    $ stopvoc("OKA")
    play OKA "CRS03A_OKA0002"
    $ current_voice = "voice/CRS03A_OKA0002.ogg"
    "Rintarou" "「…………」"
    "Okabe remained silent looking around."
    "While he was looking towards me he wasn't looking at me."
    $ stopvoc("CRS")
    play CRS "CRS03A_CRS0003"
    $ current_voice = "voice/CRS03A_CRS0003.ogg"
    "Kurisu" "「I mean you don't need to destroy it...」"
    "My voice was trembling"
    "I couldn't understand..."
    "The Okabe that I was looking at was probably the most unknown he had ever been to me."
    $ stopvoc("CRS")
    play CRS "CRS03A_CRS0004"
    $ current_voice = "voice/CRS03A_CRS0004.ogg"
    "Kurisu" "「We decided we wouldn't Time Leap so that's fine right?!」"
    "There was a tinge of anger and confusion and anxiety. I was afraid of the unknown."
    "All these things were mixed within me in a perfect harmony."
    $ stopvoc("CRS")
    play CRS "CRS03A_CRS0005"
    $ current_voice = "voice/CRS03A_CRS0005.ogg"
    "Kurisu" "「Anyway put the chair down...」"
    $ stopvoc("OKA")
    play OKA "CRS03A_OKA0003"
    $ current_voice = "voice/CRS03A_OKA0003.ogg"
    "Rintarou" "「…………」"
    window hide

    stop bgm 
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    "While I was wondering what I was supposed to do once I had said that Okabe slowly lowered the chair."

    hide lh5 
    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_ALB07"),"True","lh/OKA_ALB07a~ipad.png") at center as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    play bgm "BGM23"
    "And then I finally realized."
    "Okabe's expression was now completely different from just a few minutes ago."
    "Just like an old man who had lived a life of hardship..."
    "While I didn't know the reason such woe had been engraved in Okabe's face."
    $ stopvoc("CRS")
    play CRS "CRS03A_CRS0006"
    $ current_voice = "voice/CRS03A_CRS0006.ogg"
    "Kurisu" "「You look pale. What happened?」"
    $ stopvoc("OKA")
    play OKA "CRS03A_OKA0004"
    $ current_voice = "voice/CRS03A_OKA0004.ogg"
    "Rintarou" "「…………」"
    "As if he couldn't put his thoughts into words Okabe didn't respond."
    "Like a clam shell which had shut its mouth he sealed his lips."
    "As I suspected that expression was one of anguish."
    "If he was his usual Chuunibou self that would have been fine. Actually I would have preferred that."
    "No matter how much he tried to trick me that Okabe would have been better than he was now."
    $ stopvoc("CRS")
    play CRS "CRS03A_CRS0007"
    $ current_voice = "voice/CRS03A_CRS0007.ogg"
    "Kurisu" "「Are you listening?!」"
    "My own annoyance could be heard in my tone as I couldn't understand what was going on."

    show expression ConditionSwitch("renpy.music.get_playing(channel='OKA')",DynamicDisplayable(mouthanime,"OKA_AMA06"),"True","lh/OKA_AMA06a~ipad.png") as lh5 zorder (10-5) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("OKA")
    play OKA "CRS03A_OKA0005"
    $ current_voice = "voice/CRS03A_OKA0005.ogg"
    "Rintarou" "「……！」"
    "But the action that Okabe chose was... to run away."
    window hide
    play se "SGSE182"
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    $ stopvoc("CRS")
    play CRS "CRS03A_CRS0008"
    $ current_voice = "voice/CRS03A_CRS0008.ogg"
    "Kurisu" "「Hey wait!」"
    "Ignoring my cries Okabe ran outside. As he was running at full speed I wasn't able to catch up to him."
    $ stopvoc("CRS")
    play CRS "CRS03A_CRS0009"
    $ current_voice = "voice/CRS03A_CRS0009.ogg"
    "Kurisu" "「Wait! I'm telling you to wait dammit!」"
    "While my voice was fraught with anger I chased Okabe through the streets of Akihabara."
    window hide


    $ loadBG(0,"BG05A1")

    "But his starting sprint was completely different and he disappeared from view."
    "Where the hell had he gone? What had made him act like that?!"
    "With my head full of questions I returned towards the lab. I heard the sound of the door open."

    hide lh7 
    show expression ConditionSwitch("renpy.music.get_playing(channel='TEN')",DynamicDisplayable(mouthanime,"TEN_BSA01"),"True","lh/TEN_BSA01a~ipad.png") at center as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("TEN")
    play TEN "CRS03A_TEN0000"
    $ current_voice = "voice/CRS03A_TEN0000.ogg"
    "Tennouji" "「Hey what happend... what was all that noise just now?」"
    "The one who called was the owner of the building Tennouji-san."
    $ stopvoc("CRS")
    play CRS "CRS03A_CRS0010"
    $ current_voice = "voice/CRS03A_CRS0010.ogg"
    "Kurisu" "「Oh... I'm sorry. Eh... Did you see which way Okabe went?」"

    show expression ConditionSwitch("renpy.music.get_playing(channel='TEN')",DynamicDisplayable(mouthanime,"TEN_BSA03"),"True","lh/TEN_BSA03a~ipad.png") as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("TEN")
    play TEN "CRS03A_TEN0001"
    $ current_voice = "voice/CRS03A_TEN0001.ogg"
    "Tennouji" "「Huh? That guy? He was definitely in a hurry. I was wondering what was going on so I came out...」"
    "Tilting his neck slightly Tennouji-san furrowed his brows. It seemed he had only witnessed it from within the store."

    hide lh8 
    show expression ConditionSwitch("renpy.music.get_playing(channel='NAE')",DynamicDisplayable(mouthanime,"NAE_ASA06"),"True","lh/NAE_ASA06a~ipad.png") at left_t as lh8 zorder (10-8) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    "While I wondered which way to go Nae came out of the store."
    $ stopvoc("NAE")
    play NAE "CRS03A_NAE0000"
    $ current_voice = "voice/CRS03A_NAE0000.ogg"
    "Nae" "「If you're looking for Uncle Okarin then he ran that way... He was a little scary...」"
    window hide
    hide lh5 
    hide lh6 
    hide lh7 
    hide lh8 
    with dissolve
    "I stared in the direction Nae was pointing."
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_KANDA_MYOJIN"]]["Check"]!=1:
        $ persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_KANDA_MYOJIN"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_KANDA_MYOJIN"])
    "Down the road about 50 meters was a T junction which split to the direction of{color=#f00}Kanda Shrine{/color}and Central Avenue"
    "Naturally I had no idea which way he went."
    "Okabe..."

    hide lh7 
    show expression ConditionSwitch("renpy.music.get_playing(channel='TEN')",DynamicDisplayable(mouthanime,"TEN_BSA03"),"True","lh/TEN_BSA03a~ipad.png") at center as lh7 zorder (10-7) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    hide lh8 
    show expression ConditionSwitch("renpy.music.get_playing(channel='NAE')",DynamicDisplayable(mouthanime,"NAE_ASA06"),"True","lh/NAE_ASA06a~ipad.png") at left_t as lh8 zorder (10-8) :
        yanchor 1.0
        ypos 1.15
    with Dissolve(.5)

    $ stopvoc("NAE")
    play NAE "CRS03A_NAE0001"
    $ current_voice = "voice/CRS03A_NAE0001.ogg"
    "Nae" "「What happend?」"
    $ stopvoc("CRS")
    play CRS "CRS03A_CRS0011"
    $ current_voice = "voice/CRS03A_CRS0011.ogg"
    "Kurisu" "「No it's nothing. He just was a little troubled. Thanks Nae!」"
    "Leaving Nae my thanks I started running towards the city to pursue Okabe myself. There was no way I could leave him in his current state."
    "Before something irreversible happened I needed to get him to explain to me what had happend."

    stop bgm 

    hide screen phoneSD1
    scene expression Solid("000000")  with fade
    window hide





    return
