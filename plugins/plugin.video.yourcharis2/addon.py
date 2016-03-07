import xbmc
import xbmcgui
import xbmcaddon

addon = xbmcaddon.Addon('plugin.video.yourcharis2')
title = addon.getAddonInfo('name')
icon = addon.getAddonInfo('icon')

#link = 'plugin://plugin.video.youtube/play/?video_id=78VZ_8ZY-28'     # read people
link = 'plugin://plugin.video.youtube/play/?video_id=MfNXgmXIYLA'    # rapport 



li = xbmcgui.ListItem(label=title, iconImage=icon, thumbnailImage=icon, path=link)
li.setInfo(type='Video', infoLabels={ "title": title })
li.setProperty('IsPlayable', 'true')

xbmc.Player().play(item=link, listitem=li)


