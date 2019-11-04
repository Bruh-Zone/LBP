label splashscreen:
    show expression Solid("000") as bg
    if not persistent.message:
        show expression Text("献给我的朋友三十张，\n一位因渐冻症去世的ACG爱好者，\n愿他在另一条世界线上过着健康快乐的生活") as text at truecenter
        with dissolve
        $ renpy.pause(5,hard=True)
        hide text
        with dissolve
        $ persistent.message = True
    play se "click12"
    show expression DynamicDisplayable(printer,[],list("D-SYSTEM||OK"),"s") as pretext1:
        pos (676,378)
    with None
    $ renpy.pause(2)
    hide pretext1
    play se "click12"
    show expression DynamicDisplayable(printer,list("D-SYSTEM||OK"),list("D-SYSTEM||OK"),"s",static=True) as pretext1:
        pos (676,378-58)
    show expression DynamicDisplayable(printer,[],list("T-SYSTEM||OK"),"s") as pretext2:
        pos (676,378)
    with None
    $ i = 0
    $ renpy.pause(2)
    play se "click12"
    show expression DynamicDisplayable(printer,list("D-SYSTEM||OK"),list("D-SYSTEM||OK"),"s",static=True) as pretext1:
        pos (676,378-58*2)
    show expression DynamicDisplayable(printer,list("T-SYSTEM||OK"),list("T-SYSTEM||OK"),"s",static=True) as pretext2:
        pos (676,378-58*1)
    show expression DynamicDisplayable(printer,[],list("R-SYSTEM||OK"),"s") as pretext3:
        pos (676,378)
    with None
    $ renpy.pause(2)
    play se "click8"
    show expression DynamicDisplayable(printer,list("D-SYSTEM||OK"),list("D-SYSTEM||OK"),"s",static=True) as pretext1:
        pos (676,378-58*3)
    show expression DynamicDisplayable(printer,list("T-SYSTEM||OK"),list("T-SYSTEM||OK"),"s",static=True) as pretext2:
        pos (676,378-58*2)
    show expression DynamicDisplayable(printer,list("R-SYSTEM||OK"),list("R-SYSTEM||OK"),"s",static=True) as pretext3:
        pos (676,378-58*1)
    show expression DynamicDisplayable(printer,[],list("COMPLETE"),"s") as pretext4:
        pos (676,378)
    with None
    $ renpy.pause(2)
    play se "click10"
    show expression DynamicDisplayable(printer,list("D-SYSTEM||OK"),list("D-SYSTEM||OK"),"s",static=True) as pretext1:
        pos (676,378-58*4)
    show expression DynamicDisplayable(printer,list("T-SYSTEM||OK"),list("T-SYSTEM||OK"),"s",static=True) as pretext2:
        pos (676,378-58*3)
    show expression DynamicDisplayable(printer,list("R-SYSTEM||OK"),list("R-SYSTEM||OK"),"s",static=True) as pretext3:
        pos (676,378-58*2)
    show expression DynamicDisplayable(printer,list("COMPLETE"),list("COMPLETE"),"s",static=True) as pretext4:
        pos (676,378-58*1)
    show expression DynamicDisplayable(printer,[],list("WELCOME TO"),"s") as pretext5:
        pos (676,378)
    with None
    $ renpy.pause(2)
    play se "click10"
    show expression DynamicDisplayable(printer,list("D-SYSTEM||OK"),list("D-SYSTEM||OK"),"s",static=True) as pretext1:
        pos (676,378-58*5)
    show expression DynamicDisplayable(printer,list("T-SYSTEM||OK"),list("T-SYSTEM||OK"),"s",static=True) as pretext2:
        pos (676,378-58*4)
    show expression DynamicDisplayable(printer,list("R-SYSTEM||OK"),list("R-SYSTEM||OK"),"s",static=True) as pretext3:
        pos (676,378-58*3)
    show expression DynamicDisplayable(printer,list("COMPLETE"),list("COMPLETE"),"s",static=True) as pretext4:
        pos (676,378-58*2)
    show expression DynamicDisplayable(printer,list("WELCOME TO"),list("WELCOME TO"),"s",static=True) as pretext5:
        pos (676,378-58*1)
    show expression DynamicDisplayable(printer,[],list("STEINS;GATE"),"s") as pretext6:
        pos (676,378)
    with None

    $ renpy.pause(2)
    stop se

    with None
    return


label SGFD2_ROUTE_OKA:
    #$ save_name = "扫描线上的化身博士"
    $ save_name = "Dr. Jekyll on lines"
    python:
        rml = []
        sml = []
        cml = {}
        lml = []
    stop music
    $ phonering = "SGSE700"
    $ phonemailring = "SGSE801"
    $ current_route = "oka"
    $ phonecg = "WALL_OKA"
    $ InitMail(current_route)
    $ bad_denpa = False
    show screen invisible
    show expression Solid("000") as background
    with fade
    $ renpy.movie_cutscene("video/imv03.avi")
    show expression Solid("000") as background
    with fade
    hide screen invisible
    call SGFD2_OKA01A
    call SGFD2_OKA02A
    call SGFD2_OKA03A
    call SGFD2_OKA04A
    call SGFD2_OKA05A
    call SGFD2_OKA06A
    call SGFD2_OKA07A
    $ persistent.OKA1 = True
    return


label SGFD2_ROUTE_DAR:
    #$ save_name = "绚烂假想的蛇蝎美人"
    $ save_name = "Bird Singing in Cage"
    python:
        rml = []
        sml = []
        cml = {}
        lml = []
    stop music
    $ phonering = "SGSE700"
    $ phonemailring = "SGSE801"
    $ current_route = "dar"
    $ phonecg = "WALL_DAR"
    $ bad_denpa = False
    $ InitMail(current_route)
    show screen invisible
    show expression Solid("000") as background
    with fade
    $ renpy.movie_cutscene("video/imv03.avi")
    show expression Solid("000") as background
    with fade
    hide screen invisible
    call SGFD2_DAR01A
    call SGFD2_DAR02A
    call SGFD2_DAR03A
    call SGFD2_DAR04A
    call SGFD2_DAR05A
    call SGFD2_DAR06A
    call SGFD2_DAR07A
    call SGFD2_DAR08A
    call SGFD2_DAR09A
    call SGFD2_DAR10A
    $ persistent.DAR = True
    return


label SGFD2_ROUTE_CRS:
    #$ save_name = "黄昏色的救世主"
    $ save_name = "Vermilion Sooteer"
    python:
        rml = []
        sml = []
        cml = {}
        lml = []
    stop music
    $ phonering = "SGSE700"
    $ phonemailring = "SGSE801"
    $ current_route = "crs"
    $ phonecg = "WALL_CRS"
    $ bad_denpa = False
    $ InitMail(current_route)
    show screen invisible
    show expression Solid("000") as background
    with fade
    $ renpy.movie_cutscene("video/imv03.avi")
    show expression Solid("000") as background
    with fade
    hide screen invisible
    call SGFD2_CRS01A
    call SGFD2_CRS02A
    call SGFD2_CRS03A
    call SGFD2_CRS04A
    call SGFD2_CRS05A
    call SGFD2_CRS06A
    call SGFD2_CRS07A
    call SGFD2_CRS08A
    call SGFD2_CRS09A
    call SGFD2_CRS10A
    call SGFD2_CRS11A
    call SGFD2_CRS12A
    call SGFD2_CRS13A
    call SGFD2_CRS14A
    call SGFD2_CRS15A
    call SGFD2_CRS16A
    call SGFD2_CRS17A

    $ persistent.CRS = True
    return


label SGFD2_ROUTE_SUZ:
    #$ save_name = "幽灵障害的会合"
    $ save_name = "Ghosting Rendezvous"
    python:
        rml = []
        sml = []
        cml = {}
        lml = []
    stop music
    $ phonering = "SGSE700"
    $ phonemailring = "SGSE801"
    $ current_route = "suz"
    $ phonecg = "WALL_SUZ"
    $ InitMail(current_route)
    $ bad_denpa = False
    show screen invisible
    show expression Solid("000") as background
    with fade
    $ renpy.movie_cutscene("video/imv03.avi")
    show expression Solid("000") as background
    with fade
    hide screen invisible
    call SGFD2_SUZ01A
    call SGFD2_SUZ02A
    call SGFD2_SUZ03A
    call SGFD2_SUZ03B
    $ persistent.SUZ = True
    return


label SGFD2_ROUTE_TEN:
    #$ save_name = "雨铃铃曲的消除"
    $ save_name = "A Strange Building Filled of Love"
    python:
        rml = []
        sml = []
        cml = {}
        lml = []
    stop music
    $ phonering = "SGSE700"
    $ phonemailring = "SGSE801"
    $ current_route = "ten"
    $ phonecg = "WALL_TEN"
    $ bad_denpa = False
    $ InitMail(current_route)
    show screen invisible
    show expression Solid("000") as background
    with fade
    $ renpy.movie_cutscene("video/imv03.avi")
    show expression Solid("000") as background
    with fade
    hide screen invisible
    call SGFD2_TEN01A
    call SGFD2_TEN02A
    call SGFD2_TEN03A
    call SGFD2_TEN04A
    call SGFD2_TEN05A
    call SGFD2_TEN06A
    call SGFD2_TEN07A
    call SGFD2_TEN07B
    call SGFD2_TEN08A
    call SGFD2_TEN09A
    call SGFD2_TEN09B
    call SGFD2_TEN10A
    call SGFD2_TEN11A
    call SGFD2_TEN12A
    call SGFD2_TEN12B
    call SGFD2_TEN12C
    call SGFD2_TEN13A
    call SGFD2_TEN14A
    call SGFD2_TEN15A

    $ persistent.TEN = True
    return


label SGFD2_ROUTE_FEI:
    #$ save_name = "桃色幻都的黑猫"
    $ save_name = "Super hero Chat-noir"
    python:
        rml = []
        sml = []
        cml = {}
        lml = []
    stop music
    $ phonering = "SGSE700"
    $ phonemailring = "SGSE804"
    $ current_route = "fei"
    $ phonecg = "WALL_FEI"
    $ bad_denpa = False
    $ InitMail(current_route)
    show screen invisible
    show expression Solid("000") as background
    with fade
    $ renpy.movie_cutscene("video/imv03.avi")
    show expression Solid("000") as background
    with fade
    hide screen invisible
    call SGFD2_FEI01A
    call SGFD2_FEI02A
    call SGFD2_FEI03A
    call SGFD2_FEI04A
    call SGFD2_FEI05A

    $ persistent.FEI = True
    return


label SGFD2_ROUTE_RUK:
    #$ save_name = "迷宫错综的雌雄共体"
    $ save_name = "Hermaphroditus in Labyrinth"
    python:
        rml = []
        sml = []
        cml = {}
        lml = []
    stop music
    $ phonering = "SGSE700"
    $ phonemailring = "SGSE806"
    $ current_route = "ruk"
    $ phonecg = "WALL_RUK"
    $ bad_denpa = False
    $ InitMail(current_route)
    show screen invisible
    show expression Solid("000") as background
    with fade
    $ renpy.movie_cutscene("video/imv03.avi")
    show expression Solid("000") as background
    with fade
    hide screen invisible
    call SGFD2_RUK01A
    call SGFD2_RUK01B
    call SGFD2_RUK02A
    call SGFD2_RUK02B
    call SGFD2_RUK03A
    call SGFD2_RUK04A
    call SGFD2_RUK04B
    call SGFD2_RUK04C

    $ persistent.RUK = True
    return


label SGFD2_ROUTE_MAY:
    #$ save_name = "悠远不变的北极星"
    $ save_name = "Eternal Polaris"
    python:
        rml = []
        sml = []
        cml = {}
        lml = []
    stop music
    $ phonering = "SGSE700"
    $ phonemailring = "SGSE803"
    $ current_route = "may"
    $ phonecg = "WALL_MAY"
    $ bad_denpa = False
    $ InitMail(current_route)
    show screen invisible
    show expression Solid("000") as background
    with fade
    $ renpy.movie_cutscene("video/imv03.avi")
    show expression Solid("000") as background
    with fade
    hide screen invisible
    call SGFD2_MAY01A
    call SGFD2_MAY02A
    call SGFD2_MAY03A
    call SGFD2_MAY04A
    call SGFD2_MAY05A
    call SGFD2_MAY05B
    call SGFD2_MAY05C

    $ persistent.MAY = True
    return


label SGFD2_ROUTE_MOE:
    #$ save_name = "昏睡励起的量子"
    $ save_name = "Quantum excited in Coma"
    python:
        rml = []
        sml = []
        cml = {}
        lml = []
    stop music
    $ phonering = "SGSE700"
    $ phonemailring = "SGSE804"
    $ current_route = "moe"
    $ phonecg = "WALL_MOE"
    $ bad_denpa = False
    $ InitMail(current_route)
    show screen invisible
    show expression Solid("000") as background
    with fade
    $ renpy.movie_cutscene("video/imv03.avi")
    show expression Solid("000") as background
    with fade
    hide screen invisible
    call SGFD2_MOE01A
    call SGFD2_MOE02A
    call SGFD2_MOE02B
    call SGFD2_MOE03A
    call SGFD2_MOE04A
    call SGFD2_MOE05A
    call SGFD2_MOE06A
    call SGFD2_MOE07A
    call SGFD2_MOE08A
    call SGFD2_MOE09A

    $ persistent.MOE = True
    return


label SGFD2_ROUTE_KYO:
    #$ save_name = "三世因果的绑架"
    $ save_name = "Three Contrapasso About The Abduction"
    python:
        rml = []
        sml = []
        cml = {}
        lml = []
    stop music
    $ phonering = "SGSE700"
    $ phonemailring = "SGSE801"
    $ current_route = "oka"
    $ phonecg = "WALL_OKA"
    $ bad_denpa = False
    $ InitMail(current_route)
    show screen invisible
    show expression Solid("000") as background
    with fade
    $ renpy.movie_cutscene("video/imv03.avi")
    show expression Solid("000") as background
    with fade
    hide screen invisible
    call SGFD2_KYO01A
    call SGFD2_KYO01B
    call SGFD2_KYO02A
    call SGFD2_KYO02B
    call SGFD2_KYO03A
    call SGFD2_KYO04A
    call SGFD2_KYO04B
    call SGFD2_KYO05A
    call SGFD2_KYO06A
    call SGFD2_KYO07A
    call SGFD2_KYO08A
    call SGFD2_KYO08B
    call SGFD2_KYO09A

    $ persistent.OKA2 = True
    return


label SGFD2_ROUTE_NAE:
    #$ save_name = "月晕的彩虹桥"
    $ save_name = "Lunar Halo Bifröst"
    python:
        rml = []
        sml = []
        cml = {}
        lml = []
    stop music
    $ phonering = "SGSE700"
    $ phonemailring = "SGSE808"
    $ current_route = "nae"
    $ phonecg = "WALL_NAE"
    $ bad_denpa = False
    $ InitMail(current_route)
    show screen invisible
    show expression Solid("000") as background
    with fade
    $ renpy.movie_cutscene("video/imv03.avi")
    show expression Solid("000") as background
    with fade
    hide screen invisible
    call SGFD2_NAE01A
    call SGFD2_NAE02A
    call SGFD2_NAE03A
    call SGFD2_NAE04A
    call SGFD2_NAE04B
    call SGFD2_NAE05A
    call SGFD2_NAE06A
    call SGFD2_NAE07A
    call SGFD2_NAE08A
    call SGFD2_NAE09A

    $ persistent.NAE = True
    return
    