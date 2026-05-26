[app]

# Nome do seu aplicativo
title = CRGBDA AI
# Nome do pacote
package.name = crgbdaai
package.domain = org.crgbda

# Versão
version = 1.0

# Onde estão seus arquivos
source.dir = .
source.include_exts = py,png,jpg,ttf,env

# Tudo que seu aplicativo precisa para funcionar
requirements = python3, kivy, python-dotenv

# Tela
orientation = portrait

# Versões do Android (tudo certinho aqui)
android.api = 33
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21
android.build_tools_version = 34.0.0

# Permissões para usar internet
android.permissions = INTERNET, ACCESS_NETWORK_STATE

[buildozer]
log_level = 2
warn_on_root = 0
