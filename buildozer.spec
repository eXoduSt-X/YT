[app]
title = YT
package.name = yt
package.domain = org.exodust
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy==2.3.0,yt-dlp,certifi

orientation = portrait
fullscreen = 0

# Iconos e interfaz
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

# Permisos requeridos para descargar
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

[buildozer]
log_level = 2
warn_on_root = 1
