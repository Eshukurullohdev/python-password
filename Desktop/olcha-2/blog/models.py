from django.db import models
from django.utils.crypto import get_random_string
from django.core.validators import RegexValidator


class Gadjet(models.Model):
    unique_id = models.CharField(
        max_length=90,
        validators=[
            RegexValidator(
                regex=r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*])[^?&^]{-}$",
                message="Bu symbollardan tashqari ?&^",
                code="hato_boldi",
            )
        ],
        unique=True,  # yagona bo'lishi uchun
        null=True,
        blank=True,
        help_text="Bu yerda faqat 90ta lik random string, number va symboldan iborat bo'ladi va siz buni yaratishiz shart emas, dastur o'zi yaratib beradi",
    )
    img = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    cost = models.CharField(max_length=200)
    skitka = models.BooleanField(default=False, null=True)

    def calculate_3month(self):
        return int((int(self.cost) /3))
    
    def calculate_6month(self):
        return int((int(self.cost) /6))

    def calculate_12month(self):
        return int((int(self.cost) /12))

    def save(self, *args, **kwargs):
        if not self.unique_id:
            self.unique_id = get_random_string(
                length=90,
                allowed_chars="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789",
            )
        super().save(*args, **kwargs)


class Tovar(models.Model):
    unique_id = models.CharField(
        max_length=90,
        validators=[
            RegexValidator(
                regex=r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*])[^?&^]{-}$",
                message="Field must contain at least 1 letter, 1 number, and 1 symbol except ? & ^.%*",
                code="hato_boldi",
            )
        ],
        unique=True,
        null=True,
        blank=True,
    )
    img = models.CharField(max_length=200)
    name = models.CharField(max_length=250)
    cost = models.CharField(max_length=250, null=True)
    skitka = models.BooleanField(default=False)

    def calculate_3month(self):
        return int((int(self.cost) /3))
    
    def calculate_6month(self):
        return int((int(self.cost) /6))

    def calculate_12month(self):
        return int((int(self.cost) /12))

    
    

    def save(self, *args, **kwargs):
        if not self.unique_id:
            self.unique_id = get_random_string(
                length=90,
                allowed_chars="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789",
            )
        super().save(*args, **kwargs)


class Texnika(models.Model):
    unique_id = models.CharField(
        max_length=90,
        validators=[
            RegexValidator(
                regex=r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*])[^?&^]{-}$",
                message="Field must contain at least 1 letter, 1 number, and 1 symbol except ? & ^.%*",
                code="hato_boldi",
            )
        ],
        unique=True,
        null=True,
        blank=True,
    )
    img = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    cost = models.CharField(max_length=200)
    skitka = models.BooleanField(default=False, null=True)

    def calculate_3month(self):
        return int((int(self.cost) /3))
    
    def calculate_6month(self):
        return int((int(self.cost) /6))

    def calculate_12month(self):
        return int((int(self.cost) /12))

    def save(self, *args, **kwargs):
        if not self.unique_id:
            self.unique_id = get_random_string(
                length=90,
                allowed_chars="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789",
            )
        super().save(*args, **kwargs)


class Kitob(models.Model):



    unique_id = models.CharField(
        max_length=90,
        validators=[
            RegexValidator(
                regex=r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*])[^?&^]{-}$",
                message="Bu symbollardan tashqari ?&^",
                code="hato_boldi",
            )
        ],
        unique=True,  # yagona bo'lishi uchun
        null=True,
        blank=True,
        help_text="Bu yerda faqat 90ta lik random string, number va symboldan iborat bo'ladi va siz buni yaratishiz shart emas, dastur o'zi yaratib beradi",
    )
    img = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    cost = models.CharField(max_length=200)
    skitka = models.BooleanField(default=False, null=True)

    def calculate_3month(self):
        return int((int(self.cost) /3))
    
    def calculate_6month(self):
        return int((int(self.cost) /6))

    def calculate_12month(self):
        return int((int(self.cost) /12))
    
    def save(self, *args, **kwargs):
        if not self.unique_id:
            self.unique_id = get_random_string(
                length=90,
                allowed_chars="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789",
            )
        super().save(*args, **kwargs)

class Tv(models.Model):
    unique_id = models.CharField(
        max_length=90,
        validators=[
            RegexValidator(
                regex=r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*])[^?&^]{-}$",
                message="Bu symbollardan tashqari ?&^",
                code="hato_boldi",
            )
        ],
        unique=True,  # yagona bo'lishi uchun
        null=True,
        blank=True,
        help_text="Bu yerda faqat 90ta lik random string, number va symboldan iborat bo'ladi va siz buni yaratishiz shart emas, dastur o'zi yaratib beradi",
    )


    
    img = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    cost = models.CharField(max_length=200)
    skitka = models.BooleanField(default=False, null=True)


    def calculate_3month(self):
        return int((int(self.cost) /3))
    
    def calculate_6month(self):
        return int((int(self.cost) /6))

    def calculate_12month(self):
        return int((int(self.cost) /12))

    def save(self, *args, **kwargs):
        if not self.unique_id:
            self.unique_id = get_random_string(
                length=90,
                allowed_chars="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789",
            )
        super().save(*args, **kwargs)


class Expesiv(models.Model):

    
    unique_id = models.CharField(
        max_length=90,
        validators=[
            RegexValidator(
                regex=r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*])[^?&^]{-}$",
                message="Bu symbollardan tashqari ?&^",
                code="hato_boldi",
            )
        ],
        unique=True,  # yagona bo'lishi uchun
        null=True,
        blank=True,
        help_text="Bu yerda faqat 90ta lik random string, number va symboldan iborat bo'ladi va siz buni yaratishiz shart emas, dastur o'zi yaratib beradi",
    )
    img = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    cost = models.CharField(max_length=200)
    skitka = models.BooleanField(default=False, null=True)
    
    def calculate_3month(self):
        return int((int(self.cost) /3))
    
    def calculate_6month(self):
        return int((int(self.cost) /6))

    def calculate_12month(self):
        return int((int(self.cost) /12))

    def save(self, *args, **kwargs):
        if not self.unique_id:
            self.unique_id = get_random_string(
                length=90,
                allowed_chars="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789",
            )
        super().save(*args, **kwargs)



class Notebook(models.Model):


    unique_id = models.CharField(
        max_length=90,
        validators=[
            RegexValidator(
                regex=r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*])[^?&^]{-}$",
                message="Bu symbollardan tashqari ?&^",
                code="hato_boldi",
            )
        ],
        unique=True,  # yagona bo'lishi uchun
        null=True,
        blank=True,
        help_text="Bu yerda faqat 90ta lik random string, number va symboldan iborat bo'ladi va siz buni yaratishiz shart emas, dastur o'zi yaratib beradi",
    )
    img = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    cost = models.CharField(max_length=200)
    skitka = models.BooleanField(default=False, null=True)

    def calculate_3month(self):
        return int((int(self.cost) /3))
    
    def calculate_6month(self):
        return int((int(self.cost) /6))

    def calculate_12month(self):
        return int((int(self.cost) /12))

    def save(self, *args, **kwargs):
        if not self.unique_id:
            self.unique_id = get_random_string(
                length=90,
                allowed_chars="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789",
            )
        super().save(*args, **kwargs)


class Cart(models.Model):

    unique_id = models.CharField(
        max_length=90,
        validators=[
            RegexValidator(
                regex=r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*])[^?&^]{-}$",
                message="Bu symbollardan tashqari ?&^",
                code="hato_boldi",
            )
        ],
        unique=True,  # yagona bo'lishi uchun
        null=True,
        blank=True,
        help_text="Bu yerda faqat 90ta lik random string, number va symboldan iborat bo'ladi va siz buni yaratishiz shart emas, dastur o'zi yaratib beradi",
    )
    tovar = models.ForeignKey(Tovar, on_delete=models.SET_NULL, null=True, blank=True)
    gadjet = models.ForeignKey(Gadjet, on_delete=models.SET_NULL, null=True, blank=True)
    notebook = models.ForeignKey(Notebook, on_delete=models.SET_NULL, null=True, blank=True)
    texnika = models.ForeignKey(Texnika, on_delete=models.SET_NULL, null=True, blank=True)
    time_added = models.DateTimeField(auto_now_add=True)

    def calculate_3month(self):
        return int((int(self.cost) /3))
    
    def calculate_6month(self):
        return int((int(self.cost) /6))

    def calculate_12month(self):
        return int((int(self.cost) /12))

    def save(self, *args, **kwargs):
        if not self.unique_id:
            self.unique_id = get_random_string(
                length=90,
                allowed_chars="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789",
            )
        super().save(*args, **kwargs)
    
    def __str__(self):
        return str(self.id)

class ThumbsUp(models.Model):
    """
    ThumbsUp -- like bosish, yoqtirish
    """
    tovar = models.ForeignKey(Tovar, on_delete=models.SET_NULL, null=True, blank=True)
    gadjet = models.ForeignKey(Gadjet, on_delete=models.SET_NULL, null=True, blank=True)
    notebook = models.ForeignKey(Notebook, on_delete=models.SET_NULL, null=True, blank=True)
    texnika = models.ForeignKey(Texnika, on_delete=models.SET_NULL, null=True, blank=True)
    tv = models.ForeignKey(Tv, on_delete=models.SET_NULL, null=True, blank=True)
    kitob = models.ForeignKey(Kitob, on_delete=models.SET_NULL, null=True, blank=True)
    expesive = models.ForeignKey(Expesiv, on_delete=models.SET_NULL, null=True, blank=True)
    time_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Like bosilganlar"
        verbose_name_plural = "Like bosilganlar"

    def __str__(self):
        return str(self.id)
    
class Smm(models.Model):
    message = models.CharField(max_length=200)
    tovar = models.ForeignKey(Tovar, on_delete=models.SET_NULL, null=True, blank=True)
    gadjet = models.ForeignKey(Gadjet, on_delete=models.SET_NULL, null=True, blank=True)
    notebook = models.ForeignKey(Notebook, on_delete=models.SET_NULL, null=True, blank=True)
    texnika = models.ForeignKey(Texnika, on_delete=models.SET_NULL, null=True, blank=True)
    tv = models.ForeignKey(Tv, on_delete=models.SET_NULL, null=True, blank=True)
    kitob = models.ForeignKey(Kitob, on_delete=models.SET_NULL, null=True, blank=True)
    expesive = models.ForeignKey(Expesiv, on_delete=models.SET_NULL, null=True, blank=True)
    time_added = models.DateTimeField(auto_now_add=True, null=True)



    