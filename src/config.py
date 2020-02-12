import os

class Config:
	CACHE = 'cache'
	LANGUAGE = 'fr'
	MINECRAFT_DIRECTORY = ('%s/AppData/Roaming/.minecraft' if os.name == 'nt' else '%s/.minecraft') % os.path.expanduser('~')
	UPSCALER = 'ImageResizer-r129.exe'