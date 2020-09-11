class Translation(object):
    START_TEXT = """Merhaba!
@ExelonUserBot APP-ID APP-HASH Alıcıya Hoşgeldiniz... 
Lütfen Telefon numaranızı +90 lı Şekilde Giriniz
Bilgilerinizi Yeniden Gİrmek İçin /start Butonunu Basınız"""
    AFTER_RECVD_CODE_TEXT = """Son Olarak!
Telegramdan Gelen Kodu Giriniz!

Bu kod sadece my.telegram.org'dan APP-ID'sini Almak amacıyla kullanılır!.

Bilgilerinizi Yeniden Gİrmek İçin /start Butonunu Basınız"""
    BEFORE_SUCC_LOGIN = "Alınan kod. Web sayfasına giriliyor..."
    ERRED_PAGE = "Hata uygulama kimliği alınamadı. \n\n@BristolMyers"
    CANCELLED_MESG = "Hoşçakal! Bot görüşmesini yeniden başlatmak için"
    IN_VALID_CODE_PVDED = "Üzgünüm, ancak giriş geçerli bir Telegram Web Oturum Açma kodu gibi görünmüyor"
    IN_VALID_PHNO_PVDED = "Üzgünüm, ancak giriş geçerli bir Telefon numarası gibi gözükmüyor"
