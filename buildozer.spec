# (str) Title of your application
title = YT

# (str) Package name
package.name = yt

# (str) Package domain (needed for android packaging)
package.domain = org.exodust

# (list) Application requirements
# NOTA: Incluimos yt-dlp como requerimiento directo de Python
requirements = python3, kivy, yt-dlp, certifi

# (list) Permissions
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE
