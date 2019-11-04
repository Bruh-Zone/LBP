label CHECK_RM_RECEIVE:
    if targetmailid == "":
        $ LR_RM_CHANCE -= 1
        return
    elif LR_RM_CHANCE == 0:
        $ gd["RCVmailData"][rml[0]["MailNumber"]]["late"]=True
        return

    else:
        if len(rml) == 0 or gd["RCVmailData"][rml[0]["MailNumber"]]["mailID"]!=targetmailid:

            if phonemailring!= "":
                play se phonemailring
            if persistent.skipmail==True:
                pause
                $ renpy.choice_for_skipping()
            if targetmailid != "":
                $ RcvMail(targetmailid)
                $ targetmailid=""
        $ gd["RCVmailData"][rml[0]["MailNumber"]]["late"]=False
        $ LR_RM_CHANCE -= 1
    return
