# -*- coding: utf-8 -*-
# Plugin for Kodi mediacenter
# Kodi Universe - Very Simple Screensaver, autor Alexander Demachev (http://berserk.top)
# GNU GENERAL PUBLIC LICENSE. Version 2, June 1991

import os
import sys
import xbmc
import urllib
import xbmcgui
import xbmcaddon

__id__ = 'screensaver.kodi.universe'
__addon__ = xbmcaddon.Addon(id=__id__)
__path__ = __addon__.getAddonInfo('path')
def_video_url = __path__+'/resources/skins/default/media/kodi-universe.mkv'

class BsPlaylist:
    def __init__(self,):
        pass

    def getPlaylist(self,):
        self.playlist = xbmc.PlayList(1)
        item = xbmcgui.ListItem("item1")
        self.playlist.add(__addon__.getSetting("videofile"),item)
        return self.playlist

class BsPlayer(xbmc.Player):
    def __init__(self,):
        pass

    def onPlayBackStarted(self):
        xbmc.executebuiltin("PlayerControl(RepeatAll)")

    def onPlayBackStopped(self):
        return


class Screensaver(xbmcgui.WindowXMLDialog):
    def __init__( self, *args, **kwargs ):
        pass
    
    def onInit(self):
        video_url = __addon__.getSetting("videofile")
        if (video_url == ""):
            video_url = def_video_url
            __addon__.setSetting("videofile", video_url)
        if (__addon__.getSetting("not-video") == "true" or not os.path.isfile(video_url) ):
            return

        li = BsPlaylist()
        self.vpl = li.getPlaylist()
        if self.vpl:
            xbmc.sleep(2000)
            self.getControl(1).setImage("black.jpg")
            self.player = BsPlayer()
            if not xbmc.getCondVisibility("Player.HasMedia"):
                self.player.play(self.vpl,windowed=True)

    def onAction(self,action):
        try: xbmc.PlayList(1).clear()
        except: pass
        try: xbmc.Player().stop()
        except: pass
        try: self.close()
        except: pass


if __name__ == '__main__':
    scr = Screensaver(
        'kodi-universe.xml',
        __path__,
        'default',
        '',
    )
    scr.doModal()
    del scr
