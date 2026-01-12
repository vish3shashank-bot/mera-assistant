[app]
title = DostAssistant
package.name = dostassistant
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# Ye requirements GitHub ke liye perfect hain
requirements = python3,kivy==2.2.1,requests,urllib3,certifi,chardet,idna

android.permissions = INTERNET, SYSTEM_ALERT_WINDOW, RECORD_AUDIO
android.api = 31
android.minapi = 21
android.sdk = 31
android.ndk = 25b
android.archs = armeabi-v7a
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1