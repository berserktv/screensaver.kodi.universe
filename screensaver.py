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
video_url = 'special://profile/addon_data/screensaver.kodi.universe/kodi-universe.mkv'

class BsPlaylist:
    def __init__(self,):
        pass

    def getPlaylist(self,):
        self.playlist = xbmc.PlayList(1)
        item = xbmcgui.ListItem("item1")
        self.playlist.add(video_url,item)
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
        xbmc.sleep(1000)
        li = BsPlaylist()
        self.vpl = li.getPlaylist()
        if self.vpl:
            self.player = BsPlayer()
            if not xbmc.getCondVisibility("Player.HasMedia"):
                self.player.play(self.vpl,windowed=True)

    def onAction(self,action):
        xbmc.PlayList(1).clear()
        xbmc.Player().stop()
        self.close()


if __name__ == '__main__':
    scr = Screensaver(
        'kodi-universe.xml',
        __path__,
        'default',
        '',
    )
    scr.doModal()
    del scr
