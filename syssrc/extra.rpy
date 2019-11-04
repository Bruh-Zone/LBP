init python:
    def cgroute(i):
        if i<=4:
            return persistent.OKA1
        elif i<=9:
            return persistent.DAR
        elif i<=14:
            return persistent.CRS
        elif i<=19:
            return persistent.SUZ
        elif i<=25:
            return persistent.TEN
        elif i<=30:
            return persistent.FEI
        elif i<=35:
            return persistent.RUK
        elif i<=40:
            return persistent.MAY
        elif i<=47:
            return persistent.MOE
        elif i<=56:
            return persistent.OKA2
        else:
            return persistent.NAE
screen cg_library tag menu:
    default cglist = [
    ["EV_OKA001A0~ipad.jpg","EV_OKA001B0~ipad.jpg","EV_OKA001C0~ipad.jpg","EV_OKA001D0~ipad.jpg","EV_OKA001E0~ipad.jpg"],
    ["EV_OKA002A~ipad.jpg","EV_OKA002B~ipad.jpg","EV_OKA002C~ipad.jpg"],
    ["EV_OKA003A~ipad.jpg"],
    ["EV_OKA004A~ipad.jpg"],
    ["EV_OKA005A~ipad.jpg","EV_OKA005B~ipad.jpg","EV_OKA005C~ipad.jpg"],
    ["EV_DAR001A~ipad.jpg"],
    ["EV_DAR002A~ipad.jpg"],
    ["EV_DAR003A~ipad.jpg"],
    ["EV_DAR004A~ipad.jpg","EV_DAR004B~ipad.jpg"],
    ["EV_DAR005A~ipad.jpg","EV_DAR005B~ipad.jpg"],
    ["EV_CRS001A~ipad.jpg","EV_CRS001B~ipad.jpg"],
    ["EV_CRS002A~ipad.jpg","EV_CRS002B~ipad.jpg","EV_CRS002C~ipad.jpg","EV_CRS002D~ipad.jpg"],
    ["EV_CRS003A~ipad.jpg"],
    ["EV_CRS004A~ipad.jpg"],
    ["EV_CRS005A~ipad.jpg"],
    ["EV_SUZ001A~ipad.jpg"],
    ["EV_SUZ002A~ipad.jpg","EV_SUZ002B~ipad.jpg","EV_SUZ002C~ipad.jpg","EV_SUZ002D~ipad.jpg","EV_SUZ002E~ipad.jpg"],
    ["EV_SUZ003A~ipad.jpg"],
    ["EV_SUZ004A~ipad.jpg"],
    ["EV_SUZ005A~ipad.jpg","EV_SUZ005B~ipad.jpg","EV_SUZ005C~ipad.jpg"],
    ["EV_TEN001A0~ipad.jpg"],
    ["EV_TEN002A~ipad.jpg"],
    ["EV_TEN003A~ipad.jpg"],
    ["EV_TEN004A~ipad.jpg"],
    ["EV_TEN005A~ipad.jpg"],
    ["EV_TEN006A~ipad.jpg"],
    ["EV_FEI001A~ipad.jpg","EV_FEI001B~ipad.jpg","EV_FEI001C~ipad.jpg","EV_FEI001D~ipad.jpg"],
    ["EV_FEI002A~ipad.jpg","EV_FEI002B~ipad.jpg","EV_FEI002C~ipad.jpg"],
    ["EV_FEI003A~ipad.jpg"],
    ["EV_FEI004A~ipad.jpg","EV_FEI004B~ipad.jpg","EV_FEI004C~ipad.jpg","EV_FEI004D~ipad.jpg"],
    ["EV_FEI005A~ipad.jpg"],
    ["EV_RUK001A~ipad.jpg"],
    ["EV_RUK002A~ipad.jpg","EV_RUK002B~ipad.jpg"],
    ["EV_RUK003A~ipad.jpg","EV_RUK003B~ipad.jpg","EV_RUK003C~ipad.jpg"],
    ["EV_RUK004A~ipad.jpg","EV_RUK004B~ipad.jpg"],
    ["EV_RUK005A~ipad.jpg"],
    ["EV_MAY001A~ipad.jpg","EV_MAY001B~ipad.jpg"],
    ["EV_MAY002A~ipad.jpg","EV_MAY002B~ipad.jpg"],
    ["EV_MAY003A~ipad.jpg","EV_MAY003B~ipad.jpg","EV_MAY003C~ipad.jpg","EV_MAY003D~ipad.jpg"],
    ["EV_MAY004A~ipad.jpg","EV_MAY004B~ipad.jpg","EV_MAY004C~ipad.jpg"],
    ["EV_MAY005A~ipad.jpg","EV_MAY005B~ipad.jpg"],
    ["EV_MOE001A~ipad.jpg"],
    ["EV_MOE007A~ipad.jpg","EV_MOE007B~ipad.jpg","EV_MOE008A~ipad.jpg","EV_MOE008B~ipad.jpg"],
    ["EV_MOE002A~ipad.jpg","EV_MOE002B~ipad.jpg"],
    ["EV_MOE003A~ipad.jpg","EV_MOE003B~ipad.jpg"],
    ["EV_MOE004A~ipad.jpg"],
    ["EV_MOE005A~ipad.jpg"],
    ["EV_MOE006A~ipad.jpg"],
    ["EV_KYO001A~ipad.jpg"],
    ["EV_KYO002A~ipad.jpg","EV_KYO002B~ipad.jpg"],
    ["EV_KYO003A~ipad.jpg"],
    ["EV_KYO004A~ipad.jpg"],
    ["EV_KYO005A~ipad.jpg"],
    ["EV_KYO006A~ipad.jpg","EV_KYO006B~ipad.jpg","EV_KYO006C~ipad.jpg"],
    ["EV_KYO007A~ipad.jpg","EV_KYO007B~ipad.jpg"],
    ["EV_KYO008A~ipad.jpg"],
    ["EV_KYO009A~ipad.jpg","EV_KYO009B~ipad.jpg"],
    ["EV_NAE001A~ipad.jpg"],
    ["EV_NAE002A~ipad.jpg","EV_NAE002B~ipad.jpg","EV_NAE002C~ipad.jpg"],
    ["EV_NAE003A~ipad.jpg","EV_NAE003B~ipad.jpg"],
    ["EV_NAE004A~ipad.jpg","EV_NAE004B~ipad.jpg","EV_NAE004C~ipad.jpg"],
    ["EV_NAE005A~ipad.jpg"],
    ["pub_ev01~ipad.jpg"],
    ["pub_ev02~ipad.jpg"],
    ["pub_ev03~ipad.jpg"],
    ["pub_ev04~ipad.jpg"],
    
    ]
    default page = 1
    window:
        style "mm_root"
        add "system/bgCGLib~ipad.jpg" at truecenter

    imagebutton idle LiveCrop((0,0,226,47),"system/btnClose~ipad.png") hover LiveCrop((226,0,226,47),"system/btnClose~ipad.png") selected_idle LiveCrop((226,0,226,47),"system/btnClose~ipad.png") selected_hover LiveCrop((226,0,226,47),"system/btnClose~ipad.png") action [With(dissolve),Return()] align (1.0,1.0)
    text str(page) pos (940,25) size 40

    fixed:
        pos (512-768/2,100)
        if page < 6:
            for i in range(12):
                if cgroute(i+page*12-12):
                    imagebutton:
                        pos (194*(i%4),110*(i/4))
                        idle "system/albumThumbNo"+("%02d" % (i+page*12-12))+"~ipad.png"
                        action Show("omake_cgview",cg=cglist[i+page*12-12])
                else:
                    add "system/albumThumbLockedNo"+("%02d" % (i+page*12-12))+"~ipad.png" pos (194*(i%4),110*(i/4))
        else:
            for i in range(6):
                if cgroute(i+page*12-12):
                    imagebutton:
                        pos (194*(i%4),110*(i/4))
                        idle "system/albumThumbNo"+("%02d" % (i+page*12-12))+"~ipad.png"
                        action Show("omake_cgview",cg=cglist[i+page*12-12])
                else:
                    add "system/albumThumbLockedNo"+("%02d" % (i+page*12-12))+"~ipad.png" pos (194*(i%4),110*(i/4))
    if page!= 1:
        textbutton "上一页" action SetScreenVariable("page",page-1) align (0.4,0.9) text_size 30
    if page!= 6:
        textbutton "下一页" action SetScreenVariable("page",page+1) align (0.6,0.9) text_size 30


screen omake_cgview(cg=[]):
    default index = 0
    window:
        style "mm_root"
    viewport:
        draggable True
        add "bg/"+cg[index]
    if index != 0:
        textbutton "上一张" action SetScreenVariable("index",index-1) align (0.0,1.0) text_size 30
    if index!= len(cg)-1:
        textbutton "下一张" action SetScreenVariable("index",index+1) align (0.2,1.0) text_size 30
    imagebutton idle LiveCrop((0,0,226,47),"system/btnClose~ipad.png") hover LiveCrop((226,0,226,47),"system/btnClose~ipad.png") selected_idle LiveCrop((226,0,226,47),"system/btnClose~ipad.png") selected_hover LiveCrop((226,0,226,47),"system/btnClose~ipad.png") action [Hide("omake_cgview",dissolve)] align (1.0,1.0)

screen sound_library tag menu:

    window:
        style "mm_root"
        add "system/bgMusic~ipad.jpg" at truecenter
    imagebutton idle LiveCrop((0,0,226,47),"system/btnClose~ipad.png") hover LiveCrop((226,0,226,47),"system/btnClose~ipad.png") selected_idle LiveCrop((226,0,226,47),"system/btnClose~ipad.png") selected_hover LiveCrop((226,0,226,47),"system/btnClose~ipad.png") action [With(dissolve),Return()] align (1.0,1.0)
    window:
        area (200,130,650,340)
        has viewport:
            draggable True
            scrollbars "vertical"
            mousewheel True
        grid 1 len(gd["BGMData"]):
            for index,bgm in enumerate(gd["BGMData"]):
                if persistent.OKA1:
                    textbutton ("%02d" % (index+1))+"{space=30}"+bgm["Title"]+"{space=50}"+bgm["Artist"] action Play("bgm",bgm["BGMName"]) xfill True
                else:
                    textbutton "???" action NullAction() xfill True

transform zoom75:
    zoom .75

label op:
    $ renpy.movie_cutscene("video/op.avi")
    return
label ed1:
    $ renpy.movie_cutscene("video/fd2_ed.avi")
    return

label ed2:
    $ renpy.movie_cutscene("video/fd2_gend.avi")
    return

screen movie_library tag menu:

    window:
        style "mm_root"
        add "system/bgMovie~ipad.jpg" at truecenter
    imagebutton idle LiveCrop((0,0,226,47),"system/btnClose~ipad.png") hover LiveCrop((226,0,226,47),"system/btnClose~ipad.png") selected_idle LiveCrop((226,0,226,47),"system/btnClose~ipad.png") selected_hover LiveCrop((226,0,226,47),"system/btnClose~ipad.png") action [With(dissolve),Return()] align (1.0,1.0)
    if persistent.OKA1:
        imagebutton idle LiveCrop((52,152,280,157),"system/iconMovie~ipad.png") action Start("op") pos (52,152)
    if persistent.OKA2:
        imagebutton idle LiveCrop((352,152,300,157),"system/iconMovie~ipad.png") action Start("ed1") pos (352,152)
    if persistent.NAE:
        imagebutton idle LiveCrop((652,152,320,157),"system/iconMovie~ipad.png") action Start("ed2") pos (652,152)






screen clearlist tag menu:
    window:
        style "mm_root"
    add "system/bgCList~ipad.jpg" at truecenter

    text "TIPS数量" pos (80,150)
    python:
        tnum=0
        total=0
        for t in persistent.gd["TIPSData"]:
            if t["Check"]==1 or persistent.NAE:
                tnum+=1 
            total+=1
    text "[tnum]/192" xanchor 1.0 pos (300,150)
    viewport:
        mousewheel True
        draggable True
        pos (500,15)
        has vbox
        if persistent.OKA1:
            add "system/icoCList00~ipad.png"
        if persistent.DAR:
            add "system/icoCList01~ipad.png"
        if persistent.CRS:
            add "system/icoCList02~ipad.png"
        if persistent.SUZ:
            add "system/icoCList03~ipad.png"
        if persistent.TEN:
            add "system/icoCList04~ipad.png"
        if persistent.FEI:
            add "system/icoCList05~ipad.png"
        if persistent.RUK:
            add "system/icoCList06~ipad.png"
        if persistent.MAY:
            add "system/icoCList07~ipad.png"
        if persistent.MOE:
            add "system/icoCList08~ipad.png"
        if persistent.OKA2:
            add "system/icoCList09~ipad.png"
        if persistent.NAE:
            add "system/icoCList10~ipad.png"
    imagebutton idle LiveCrop((0,0,226,47),"system/btnClose~ipad.png") hover LiveCrop((226,0,226,47),"system/btnClose~ipad.png") selected_idle LiveCrop((226,0,226,47),"system/btnClose~ipad.png") selected_hover LiveCrop((226,0,226,47),"system/btnClose~ipad.png") action [With(dissolve),Return()] align (1.0,1.0)
