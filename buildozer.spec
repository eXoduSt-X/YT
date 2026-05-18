[app]
title = YT
package.name = yt
package.domain = org.exodust
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0

# Requerimientos esenciales para Kivy + las descargas de videos
requirements = python3,kivy==2.3.0,yt-dlp,certifi

orientation = portrait
fullscreen = 0

# Arquitecturas estándar para celulares modernos
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

# Permisos requeridos para la red y almacenamiento local
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

[buildozer]
log_level = 2
warn_on_root = 1
