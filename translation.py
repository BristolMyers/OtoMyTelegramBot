class Translation(object):
    START_TEXT = """Merhaba!
lütfen devam etmeden önce okuyun: https://t.me/BristolMyersAdvert/2
**Beni kullandığınız için teşekkür ederim 😬**
**My.telegram.org adresinden APP-ID'yi almak için Telegram Telefon Numaranızı girin**

/start **bilgilerinizi yeniden girmek için**"""
    AFTER_RECVD_CODE_TEXT = """Anlıyorum!
**Telegramdan gelen kodu girin!**

**bu kod sadece my.telegram.org'dan APP ID'sini almak amacıyla kullanılır!**.

/start **bilgilerinizi yeniden girmek için**"""
    BEFORE_SUCC_LOGIN = "alınan kod. Web sayfası keskinleştiriliyor ..."
    ERRED_PAGE = "yanlış bir şey. uygulama kimliği alınamadı. \n\n@BristolMyers"
    CANCELLED_MESG = "Hoşçakal! Bot görüşmesini yeniden başlatmak için /start "
    IN_VALID_CODE_PVDED = "üzgünüm, ancak giriş geçerli bir Telegram Web Oturum Açma kodu gibi görünmüyor"
    IN_VALID_PHNO_PVDED = "üzgünüm, ancak giriş geçerli bir telefon numarası gibi görünmüyor"
