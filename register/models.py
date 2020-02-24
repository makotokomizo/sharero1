from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.contrib.auth.validators import UnicodeUsernameValidator
from property.models import Property

from django.conf import settings
from email.mime.text import MIMEText
import smtplib

class CustomUserManager(UserManager):
    """ユーザーマネージャー"""
    use_in_migrations = True

    def _create_user(self, username, email, password, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(username, email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """カスタムユーザーモデル

    usernameを使わず、emailアドレスをユーザー名として使うようにしています。

    """
    GENDER_CHOICES = (
        ('1', '女性'),
        ('2', '男性'),
    )
    
    username = models.CharField(_('username'), max_length=20,null=True, unique=True)
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=150, blank=True)
    #last_name = models.CharField(_('last name'), max_length=150, blank=True)
    
    gender = models.CharField(_('gender性別'),max_length=2, choices=GENDER_CHOICES, blank=True)
    adress = models.CharField(_('adress'),max_length=20, blank=True)
    phone = models.CharField(_('phone'),max_length=20, blank=True)
    birth_date = models.DateField(_('年齢'),null=True, blank=True)
    houseImage = models.ImageField(_('画像'),upload_to='register/',null=True, blank=True)
    memo = models.TextField(_('備考'),max_length=20, blank=True)
    price = models.CharField(_('家賃'),max_length=20, blank=True)
    # homeProperty = models.OneToOneField(Property, related_name="homeProperty",on_delete=models.SET_NULL, null=True, blank=True)
    is_Nester = models.BooleanField(
        _('Nester'),
        default=False,
        help_text=_(
            'NESTER Designates whether the user can log into this admin site.'),
    )

    #last2_name = models.CharField(_('last2 name'), max_length=150, blank=True)

    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_(
            'Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = CustomUserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        """Return the first_name plus the last_name, with a space in
        between."""
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""

        EMAIL = settings.DEFAULT_FROM_EMAIL
        PASSWORD = settings.EMAIL_HOST_PASSWRD
        TO = self.email

        msg = MIMEText(message)

        msg['Subject'] = subject
        msg['From'] = EMAIL
        # msg['To'] = TO

        s = smtplib.SMTP(host='smtp.gmail.com', port=587)
        s.starttls()
        s.login(EMAIL, PASSWORD)
        s.sendmail(EMAIL, TO, msg.as_string())
        s.quit()
        # print(self.email)
        # from_email = settings.DEFAULT_FROM_EMAIL
        # send_mail(subject, message, from_email, [self.email], **kwargs)
        # print("here")
        # send_mail(subject, message, "test2019reiwafirst@gmail.com", ["poiprince8888@gmail.com"], **kwargs)

    # @property
    # def username(self):
    #     return self.email


