# -*- coding: utf-8 -*-
# Plugin for Kodi mediacenter
# Kodi Universe - screensaver
# Project "Berserk" - build Kodi for the Raspberry Pi platform, autor Alexander Demachev, site berserk.top
# license -  GNU GENERAL PUBLIC LICENSE. Version 2, June 1991

import sys
import xbmcaddon
import xbmcgui
import xbmc

__id__ = 'screensaver.kodi.universe'
__addon__ = xbmcaddon.Addon(id=__id__)
__path__ = __addon__.getAddonInfo('path')
_ = __addon__.getLocalizedString


class Screensaver(xbmcgui.WindowXMLDialog):

    class ExitMonitor(xbmc.Monitor):
        def __init__(self, exit_callback):
            self.exit_callback = exit_callback

        def onScreensaverDeactivated(self):
            print '3 ExitMonitor: sending exit_callback'
            self.exit_callback()

    def onInit(self):
        print '2 Screensaver: onInit'
        self.monitor = self.ExitMonitor(self.exit)
        # ALEX DEBUG
        ###xbmc.executebuiltin("PlayMedia(/tmp/test.avi)")
        xbmc.executebuiltin("PlayMedia(/tmp/test2.wmv)")
        xbmc.executebuiltin("PlayerControl(RepeatAll)")
        # Demachev A. check this
        #xbmc.executebuiltin("xbmc.playercontrol(RepeatAll)")
        #xbmc.executebuiltin("PlayerControl(Repeat)")



    def exit(self):
        print '4 Screensaver: Exit requested'
        # ALEX DEBUG
        xbmc.executebuiltin("PlayerControl(RepeatOff)", True)
        #xbmc.executebuiltin("PlayerControl(Stop)")

        self.close()


if __name__ == '__main__':
    print '1 Python Screensaver Started'
    screensaver_gui = Screensaver(
            "kodi-universe.xml",
            __path__,
            'default',
        )
    screensaver_gui.doModal()
    print '5 Python Screensaver Exited'
    #ALEX DEBUG xbmc.sleep(100)
    del screensaver_gui
    sys.modules.clear()
