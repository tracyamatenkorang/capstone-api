from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not username:
            raise ValueError('The username field must be set')
        if not email:
            raise ValueError('The Email field must be set')
        
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('You must set is_superuser =True'))
        if extra_fields.get('is_staff') is not True:
            raise ValueError(('You must set is_staff =True'))
        return self.create_user(username, email, password, **extra_fields)

    
class CustomUser(AbstractUser):
    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email']

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['email'], name='unique_email')
        ]

    def _str_(self):
        return self.username

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',
        blank=True,
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',
        blank=True,
)