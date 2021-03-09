#!/usr/bin/env python3

import time
from simple_term_menu import TerminalMenu

import getSeasonUrl
import streamObject
import getEventUrl
import getElementUrl
import getStreamUrl
import authenticate
import getM3U8Stream
import subprocess
import os
import checkForLive
import getUrlById

# Main menu settings
main_menu_title = "  F1Hub Main Menu\n"
if checkForLive.checkForLive().checkForLive():
    main_menu_items = ["Live Session", "Season Select", "Play by Content ID", "F1TV Login", "F1TV Logout", "Quit"]
else:
    main_menu_items = ["Season Select", "Play by Content ID", "F1TV Login", "F1TV Logout", "Quit"]
main_menu_cursor = "> "
main_menu_cursor_style = ("fg_red", "bold")
main_menu_style = ("bg_red", "fg_yellow")

main_menu = TerminalMenu(menu_entries=main_menu_items,
                        title=main_menu_title,
                        menu_cursor=main_menu_cursor,
                        menu_cursor_style=main_menu_cursor_style,
                        menu_highlight_style=main_menu_style,
                        cycle_cursor=True,
                        clear_screen=True)

# Event menu settings
event_menu_items = []
event_menu_title = "    Event Menu\n"
event_menu = TerminalMenu(event_menu_items,
                        event_menu_title,
                        main_menu_cursor,
                        main_menu_cursor_style,
                        main_menu_style,
                        cycle_cursor=True,
                        clear_screen=True)
events = []

# ID menu settings
ID_menu_items = []
ID_menu_title = ""
ID_menu = TerminalMenu(ID_menu_items,
                        ID_menu_title,
                        main_menu_cursor,
                        main_menu_cursor_style,
                        main_menu_style,
                        cycle_cursor=True,
                        clear_screen=True)
sessions = []

# Session menu settings
session_menu_items = []
session_menu_title = "    Event Menu\n"
session_menu = TerminalMenu(session_menu_items,
                        session_menu_title,
                        main_menu_cursor,
                        main_menu_cursor_style,
                        main_menu_style,
                        cycle_cursor=True,
                        clear_screen=True)
sessions = []

# Weekend Selector
selector_menu_items = []
selector_menu_title =   "   Weekend Menu\n"
select_menu = TerminalMenu(selector_menu_items,
                        selector_menu_title,
                        main_menu_cursor,
                        main_menu_cursor_style,
                        main_menu_style,
                        cycle_cursor=True,
                        clear_screen=True)
selectors = []

# Stream Selector
stream_menu_items = []
stream_menu_title =   "   Feed Menu\n"
stream_menu = TerminalMenu(stream_menu_items,
                        stream_menu_title,
                        main_menu_cursor,
                        main_menu_cursor_style,
                        main_menu_style,
                        cycle_cursor=True,
                        clear_screen=True)
#selectors = []

# Play Selector
play_menu_items = ["Play with MPV", "Copy link to Clipboard", "Return to Session Menu"]
play_menu_title =   "   Play Menu\n"
play_menu = TerminalMenu(play_menu_items,
                        play_menu_title,
                        main_menu_cursor,
                        main_menu_cursor_style,
                        main_menu_style,
                        cycle_cursor=True,
                        clear_screen=True)

login_menu_items = ['Log In with password', "Log in with Entitlement Token", "Return to Main Menu"]
login_menu_title =  "   Login Menu\n"
login_menu = TerminalMenu(login_menu_items,
                        login_menu_title,
                        main_menu_cursor,
                        main_menu_cursor_style,
                        main_menu_style,
                        cycle_cursor=True,
                        clear_screen=True)


def main():
    main_menu_exit = False
    event_menu_back = False
    selector_menu_back = False
    session_menu_back = False
    play_menu_back = False
    stream_menu_back = False
    login_menu_back = False
    ID_menu_back = False

    auth = authenticate.authenticate("","")
    try:
        auth.authByEntitlementToken()
    except:
        pass

    events = []
    sessions = []

    # Season menu settings
    seasons = getSeasonUrl.getSeason().getAllSeasons()
    #print(getSeasonUrl.getSeason().getAllSeasons()[0].getName())
    #seasons = urlGetter.getAllSeasons()
    #toGet = seasons[0]
    #print(toGet.getName())
    season_menu_title = "  Season Menu\n"
    season_menu_items = []
    for x in range(len(seasons)):
        season_menu_items.append(seasons[x].getName())
    season_menu_items.append("Back to Main Menu")
    season_menu_back = False
    season_menu = TerminalMenu(season_menu_items,
                             season_menu_title,
                             main_menu_cursor,
                             main_menu_cursor_style,
                             main_menu_style,
                             cycle_cursor=True,
                             clear_screen=True)



    while not main_menu_exit:
        main_sel = main_menu.show()

        # IF LIVE SESSION IS ACTIVE, THE LENGTH OF THE MENU ITEMS IS DIFFERENT.
        # To solve this, a shift value of 1 will be applied if the live value is present.
        if main_menu_items[0] == "Live Session":
            shift_val = 1
        else:
            shift_val = 0

        if main_sel == 0+shift_val:
            while not season_menu_back:
                season_sel = season_menu.show()
                if season_sel == len(season_menu_items)-1:
                    season_menu_back = True
                    print("Back Selected")
                    
                else:
                    print("Season selected")
                    #populateEventList(seasons[season_sel].getUrl())
                    event_menu_items = getEventList(seasons[season_sel].getUrl())
                    event_menu = TerminalMenu(event_menu_items,
                             event_menu_title,
                             main_menu_cursor,
                             main_menu_cursor_style,
                             main_menu_style,
                             cycle_cursor=True,
                             clear_screen=True)

                    #Enter Event Menu
                    while not event_menu_back:
                        event_sel = event_menu.show()
                        if event_sel == len(event_menu_items)-1:
                            event_menu_back = True
                            print("Back Selected")
                        else:
                            #print(event_sel)
                            #evUrl = getEventlistUrl(seasons[season_sel].getUrl(), event_sel)
                            evUrl = getEventObj(seasons[season_sel].getUrl())[event_sel].getUrl()
                            #print(evUrl)
                            #time.sleep(2)
                            # Enter Selector Menu
                            selector_menu_items = getElementUrl.getElement(evUrl).getCats()
                            selector_menu_items.append("Back to Event Menu")
                            select_menu = TerminalMenu(selector_menu_items,
                                                        selector_menu_title,
                                                        main_menu_cursor,
                                                        main_menu_cursor_style,
                                                        main_menu_style,
                                                        cycle_cursor=True,
                                                        clear_screen=True)
                            #print(selector_menu_items)
                            #time.sleep(5)
                            while not selector_menu_back:
                                selector_sel = select_menu.show()
                                if selector_sel == len(selector_menu_items)-1:
                                    selector_menu_back = True
                                    # Back
                                    pass
                                else:
                                    # Start Session Selection
                                    tarUrl = evUrl
                                    session_menu_items = getSessionList(selector_sel, tarUrl)
                                    #print(session_menu_items)
                                    session_menu = TerminalMenu(session_menu_items,
                                                                session_menu_title,
                                                                main_menu_cursor,
                                                                main_menu_cursor_style,
                                                                main_menu_style,
                                                                cycle_cursor=True,
                                                                clear_screen=True)
                                    while not session_menu_back:
                                        sess_sel = session_menu.show()
                                        if sess_sel == len(session_menu_items)-1:
                                            session_menu_back = True
                                            #Back
                                        else:
                                            # Stream List
                                            while not stream_menu_back:
                                                stream_menu_items = getFeedList(selector_sel, tarUrl, sess_sel)
                                                stream_menu = TerminalMenu(stream_menu_items,
                                                                                    stream_menu_title,
                                                                                    main_menu_cursor,
                                                                                    main_menu_cursor_style,
                                                                                    main_menu_style,
                                                                                    cycle_cursor=True,
                                                                                    clear_screen=True)
                                                stream_sel = stream_menu.show()
                                                if stream_sel == len(stream_menu_items)-1:
                                                    stream_menu_back = True
                                                else:
                                                    while not play_menu_back:
                                                        play_sel = play_menu.show()
                                                        if play_sel == len(play_menu_items)-1:
                                                            play_menu_back = True
                                                        else:
                                                            try:
                                                                baseUrl = getFeedElements(selector_sel, tarUrl, sess_sel)[stream_sel].getUrl()
                                                                streamUrl = getM3U8Stream.getTokenizedUrl(baseUrl, auth).getUrl()
                                                                
                                                                try:
                                                                    subprocess.call(["gnome-terminal", "-x", "mpv", "--border=no", streamUrl])
                                                                except:
                                                                    print("Failed to start new video session. Please open an issue on the GitHub repo as soon as possible, including your Operating System. Thanks!")
                                                                    time.sleep(5)
                                                            except:
                                                                print("Failed to get playable link. Are you logged in?")
                                                                time.sleep(5)

                                                    play_menu_back = False
                                            stream_menu_back = False

                                    session_menu_back = False

                            selector_menu_back = False
                    event_menu_items = []
                    event_menu_back = False

            season_menu_back = False
        elif main_sel == 1+shift_val:
            print("Please enter the desired Content ID:")
            contentID = input()
            #time.sleep(3)
            try:
                idObj = getUrlById.getUrlByContentId(contentID)
            except:
                print("Couldn't find ID. Please try again")
                time.sleep(3)
                exit
            ID_menu_title = idObj.getObjName()
            ID_menu_items = getIdItems(idObj)
            ID_menu = TerminalMenu(ID_menu_items,
                        ID_menu_title,
                        main_menu_cursor,
                        main_menu_cursor_style,
                        main_menu_style,
                        cycle_cursor=True,
                        clear_screen=True)
            while not ID_menu_back:
                id_sel = ID_menu.show()
                if id_sel == len(ID_menu_items)-1:
                    ID_menu_back = True
                else:
                    while not play_menu_back:
                        play_sel = play_menu.show()
                        if play_sel == len(play_menu_items)-1:
                            play_menu_back = True
                        elif play_sel == 0:
                            # Play with MPV
                            try:
                                baseUrl = getIdSelectionUrl(idObj, id_sel)
                                streamUrl = streamUrl = getM3U8Stream.getTokenizedUrl(baseUrl, auth).getUrl()
                            
                                try:
                                    subprocess.call(["gnome-terminal", "-x", "mpv", "--border=no", streamUrl])
                                except:
                                    print("Failed to start new video session. Please open an issue on the GitHub repo as soon as possible, including your Operating System. Thanks!")
                            except:
                                print("Failed to get Playable Link... are you logged in?")
                                time.sleep(5)
                        elif play_sel == 1:
                            # Copy to clipboard
                            pass
                    play_menu_back = False
            ID_menu_back = False



        elif main_sel == 2+shift_val:
            print("Login Selected")
            while not login_menu_back:
                login_sel = login_menu.show()
                if login_sel == len(login_menu_items)-1:
                    login_menu_back = True
                elif login_sel == 0:
                    print("AS OF THIS VERSION, YOUR LOGIN CREDENTIALS WILL BE STORED IN PLAINTEXT ON YOUR COMPUTER. This is a potential security risk, if other people access your computer. Please be advised.")
                    print("Please enter your email address:")
                    email = input()
                    print("Please enter your password:")
                    passw = input()
                    print("Logging you in....")
                    try:
                        auth = authenticate.authenticate(email, passw)
                        auth.authenticate()
                        print("Successfully logged in.")
                        time.sleep(3)
                    except:
                        print("Something went wrong")
                        time.sleep(3)
                elif login_sel == 1:
                    try:
                        auth = authenticate.authenticate("","")
                        auth.authByEntitlementToken()
                    except:
                        print("Error reading entitlement File, is it empty?")
                        time.sleep(5)
                
            login_menu_back = True

        elif main_sel == 3+shift_val:
            open('./entitlement.json', 'w+').close()
            print("Logged out successfully.")
            time.sleep(3)
        elif main_sel == len(main_menu_items)-1:
            main_menu_exit = True
            #print("Quit Selected")#


def getIdItems(idObj):
    nameList = []
    for x in range(len(idObj.getAdditionalStreams())):
        nameList.append(idObj.getAdditionalStreams()[x].getName())
    nameList.append("Back to Main Menu")
    return nameList

def getIdSelectionUrl(idObj, sel):
    return idObj.getAdditionalStreams()[sel].getUrl()

def populateEventList(url):
    events = getEventUrl.getEvent(url).getAllEvents()
    for x in range(len(events)):
        event_menu_items.append(events[x].getName())
    event_menu_items.append("Back to Season Selection")
    updateEventMenu()
    currsessUrl = url

def getEventlistUrl(sessUrl, EvSel):
    events = getEventUrl.getEvent(sessUrl).getAllEvents()
    return events[EvSel].getUrl()

def getEventList(url):
    events = getEventUrl.getEvent(url).getAllEvents()
    ret = []
    for x in range(len(events)):
        ret.append(events[x].getName())
    ret.append("Back to Season Selection")
    updateEventMenu()
    return ret

def getEventObj(url):
    events = getEventUrl.getEvent(url).getAllEvents()
    return events

def emptyEventList():
    event_menu_items = []

def getSessionList(cat, url):
    elements = getElementUrl.getElement(url).getElements(cat)
    ret = []
    for x in range(len(elements)):
        ret.append(elements[x].getName())
    ret.append("Return to Category Selection")
    return ret

def getSessionElement(cat, url, sel):
    elements = getElementUrl.getElement(url).getElements(cat)
    return elements[sel]

def getSessionLink(cat, url, sel):
    tarUrl = getSessionElement(cat, url, sel).getUrl()
    return tarUrl

def getFeedList(cat, url, sessSel):
    link = getSessionLink(cat, url, sessSel)
    elements = getStreamUrl.getStream(link).getStreams()
    ret = []
    for x in range(len(elements)):
        ret.append(elements[x].getName())
    ret.append("Return to session selector")
    return ret

def getFeedElements(cat, url, sessSel):
    link = getSessionLink(cat, url, sessSel)
    #print("Link: ", link)
    elements = getStreamUrl.getStream(link).getStreams()
    #for x in range(len(elements)):
    #    print(elements[x].getName(), elements[x].getUrl())
    #time.sleep(60)
    return elements

def updateEventMenu():
    event_menu = TerminalMenu(event_menu_items,
                             event_menu_title,
                             main_menu_cursor,
                             main_menu_cursor_style,
                             main_menu_style,
                             cycle_cursor=True,
                             clear_screen=True)
updateEventMenu()
if __name__ == "__main__":
    main()