from django.db import models
# Create your models here.
# To make your model visible and manageable in the Django admin interface, you need to register it in admin.py
class Customer_Record(models.Model):

    GENDER = (
        ('MALE', 'MALE'),
        ('FEMALE', 'FEMALE'),
    )

    SUFFIXES = (
        ('JR', 'JR'),
        ('SR', 'SR'),
        ('II', 'II'),
        ('III', 'III'),
        ('IV', 'IV'),
        ('V', 'V'),
        ('VI', 'VI'),
    )
    
    BRGY_CHOICES = (
        ('1 (HEN. M. ALVAREZ)','1 (HEN. M. ALVAREZ)'),
        ('2 (C. TIRONA)','2 (C. TIRONA)'),
        ('3 (HEN. E. AGUINALDO)','3 (HEN. E. AGUINALDO)'),
        ('4 (HEN. M. TRIAS)','4 (HEN. M. TRIAS)'),
        ('5 (HEN. E. EVANGELISTA)','5 (HEN. E. EVANGELISTA)'),
        ('6 (DIEGO SILANG)','6 (DIEGO SILANG)'),
        ('7 (KAPITAN KONG)','7 (KAPITAN KONG)'),
        ('8 (MANUEL S. ROJAS)','8 (MANUEL S. ROJAS)'),
        ('9 (KANAWAY)','9 (KANAWAY)'),
        ('10 (KINGFISHER)','10 (KINGFISHER)'),
        ('10-A (KINGFISHER-A)','10-A (KINGFISHER-A)'),
        ('10-B (KINGFISHER-B)','10-B (KINGFISHER-B)'),
        ('11 (LAWIN)','11 (LAWIN)'),
        ('12 (LOVE BIRD)','12 (LOVE BIRD)'),
        ('13 (AGUILA)','13 (AGUILA)'),
        ('14 (LORO)','14 (LORO)'),
        ('15 (KILYAWAN)','15 (KILYAWAN)'),
        ('16 (MARTINES)','16 (MARTINES)'),
        ('17 (KALAPATI)','17 (KALAPATI)'),
        ('18 (MAYA)','18 (MAYA)'),
        ('19 (GEMINI)','19 (GEMINI)'),
        ('20 (VIRGO)','20 (VIRGO)'),
        ('21 (SCORPIO)','21 (SCORPIO)'),
        ('22 (LEO)','22 (LEO)'),
        ('22-A (LEO A)','22-A (LEO A)'),
        ('23 (AQUARIUS)','23 (AQUARIUS)'),
        ('24 (LIBRA)','24 (LIBRA)'),
        ('25 (CAPRICORN)','25 (CAPRICORN)'),
        ('26 (CANCER)','26 (CANCER)'),
        ('27 (SAGITARIUS)','27 (SAGITARIUS)'),
        ('28 (TAURUS)','28 (TAURUS)'),
        ('29 (LAO-LAO)','29 (LAO-LAO)'),
        ('29-A (LAO-LAO A)','29-A (LAO-LAO A)'),
        ('30 (BID-BID)','30 (BID-BID)'),
        ('31 (MAYA-MAYA)','31 (MAYA-MAYA)'),
        ('32 (SALAY-SALAY)','32 (SALAY-SALAY)'),
        ('33 (BUWAN-BUWAN)','33 (BUWAN-BUWAN)'),
        ('34 (LAPU-LAPU)','34 (LAPU-LAPU)'),
        ('35 (HASA-HASA)','35 (HASA-HASA)'),
        ('36 (SAP-SAP)','36 (SAP-SAP)'),
        ('36-A (SAP-SAP A)','36-A (SAP-SAP A)'),
        ('37 (CADENA DE AMOR)','37 (CADENA DE AMOR)'),
        ('37-A (CADENA DE AMOR A)','37-A (CADENA DE AMOR A)'),
        ('38 (SAMPAGUITA)','38 (SAMPAGUITA)'),
        ('38-A (SAMPAGUITA A)','38-A (SAMPAGUITA A)'),
        ('39 (JASMIN)','39 (JASMIN)'),
        ('40 (GUMAMELA)','40 (GUMAMELA)'),
        ('41 (ROSAL)','41 (ROSAL)'),
        ('42 (PINAGBUKLOD)','42 (PINAGBUKLOD)'),
        ('42-A (PINAGBUKLOD A)','42-A (PINAGBUKLOD A)'),
        ('42-B (PINAGBUKLOD B)','42-B (PINAGBUKLOD B)'),
        ('42-C (PINAGBUKLOD C)','42-C (PINAGBUKLOD C)'),
        ('43 (PINAGPALA)','43 (PINAGPALA)'),
        ('44 (MALIGAYA)','44 (MALIGAYA)'),
        ('45 (KAUNLARAN)','45 (KAUNLARAN)'),
        ('45-A (KAUNLARAN A)','45-A (KAUNLARAN A)'),
        ('46 (SINAGTALA)','46 (SINAGTALA)'),
        ('47 (PAGKAKAISA)','47 (PAGKAKAISA)'),
        ('47-A (PAGKAKAISA A)','47-A (PAGKAKAISA A)'),
        ('47-B (PAGKAKAISA B)','47-B (PAGKAKAISA B)'),
        ('48 (NARRA)','48 (NARRA)'),
        ('48-A (NARRA A)','48-A (NARRA A)'),
        ('49 (AKASYA)','49 (AKASYA)'),
        ('49-A (AKASYA A)','49-A (AKASYA A)'),
        ('50 (KABALYERO)','50 (KABALYERO)'),
        ('51 (KAMAGONG)','51 (KAMAGONG)'),
        ('52 (IPIL)','52 (IPIL)'),
        ('53 (YAKAL)','53 (YAKAL)'),
        ('53-A (YAKAL A)','53-A (YAKAL A)'),
        ('53-B (YAKAL B)','53-B (YAKAL B)'),
        ('54 (PECHAY)','54 (PECHAY)'),
        ('54-A (PECHAY A)','54-A (PECHAY A)'),
        ('55 (AMPALAYA)','55 (AMPALAYA)'),
        ('56 (LABANOS)','56 (LABANOS)'),
        ('57 (REPOLYO)','57 (REPOLYO)'),
        ('58 (PATOLA)','58 (PATOLA)'),
        ('58-A (PATOLA A)','58-A (PATOLA A)'),
        ('59 (SITAW)','59 (SITAW)'),
        ('60 (LETSUGAS)','60 (LETSUGAS)'),
        ('61 (TALONG)','61 (TALONG)'),
        ('61-A (TALONG A)','61-A (TALONG A)'),
        ('62 (KANGKONG)','62 (KANGKONG)'),
        ('62-A (KANGKONG A)','62-A (KANGKONG A)'),
        ('62-B (KANGKONG B)','62-B (KANGKONG B)')
    )

    created_at = models.DateTimeField(auto_now_add=True)
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True)
    suffix = models.CharField(max_length=15, blank=True, choices=SUFFIXES)
    gender = models.CharField(max_length=20, choices=GENDER)
    email = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=100)
    brgy = models.CharField(max_length=50, choices=BRGY_CHOICES)
    upload_image = models.ImageField(null=True, blank=True, upload_to='images/')

    def __str__(self):
        return (f'{self.last_name} {self.suffix}, {self.first_name} {self.middle_name}')