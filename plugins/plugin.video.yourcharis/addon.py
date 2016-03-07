import xbmc
import xbmcgui
import xbmcaddon

addon = xbmcaddon.Addon('plugin.video.yourcharis')
title = addon.getAddonInfo('name')
icon = addon.getAddonInfo('icon')
link = 'plugin://plugin.video.youtube/play/?video_id=78VZ_8ZY-28'

li = xbmcgui.ListItem(label=title, iconImage=icon, thumbnailImage=icon, path=link)
li.setInfo(type='Video', infoLabels={ "title": title })
li.setProperty('IsPlayable', 'true')

xbmc.Player().play(item=link, listitem=li)