
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class UserManager(BaseUserManager):
    def create_user(self, email,name,gender,age,desc, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not name:
            raise ValueError("Users must have an name")
        if not gender:
            raise ValueError("Users must have an gender")
        if not age:
            raise ValueError("Users must have an age")

        user = self.model(
            email=self.normalize_email(email),
            name = name,
            gender=gender,
            age=age,
            desc=desc,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,name,gender,age,desc, password=None):
        user = self.create_user(
            email,
            name,
            gender,
            age,
            desc,
            password=password,

        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    
    GENDER_CHOICES = (
        ("M", "남성"),
        ("F", "여성")
    )
    
    email = models.EmailField("이메일계정",
        max_length=255,
        unique=True,
    )

    name = models.CharField("사용자 이름",max_length=255, blank=False,
                            null=False)
    
    gender = models.CharField("성별",max_length=1,choices=GENDER_CHOICES)
    age = models.IntegerField("나이",null=False,blank=False)
    desc = models.TextField("자기소개",null=True,blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name", "gender", "age", "desc"]

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.is_admin
