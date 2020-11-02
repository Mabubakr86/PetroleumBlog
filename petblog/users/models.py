from django.db import models
from django.contrib.auth.models import User
from phone_field import PhoneField
from django.utils import timezone
from django.utils.text import slugify

class Profile(models.Model):
    first_name = models.CharField(max_length=200,blank=True, null=True)
    last_name = models.CharField(max_length=200,blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pic = models.ImageField(default='default.jpg', upload_to='pictures')
    company = models.CharField(max_length=200,blank=True, null=True)
    phone = PhoneField(blank=True, help_text='Contact phone number')  #external package
    profession_title = models.CharField(max_length=200,blank=True, null=True)
    created_at = models.DateField(default=timezone.now)
    updated_at = models.DateField(default=timezone.now)
    slug = models.SlugField(blank=True,null=True)

    # to create slug field
    def save(self,*args,**kwaargs):
        if self.first_name and self.last_name:
            name = f'{self.first_name} {self.last_name}'
            exists = Profile.objects.filter(slug=name).exists()
            # to ensure it is unique
            if exists:
                name_count = Profile.objects.filter(slug=name).count()
                self.slug = slugify(name+str(name_count+1))
            self.slug = slugify(name)
        else:
            self.slug = slugify(self.user.username)
        super(Profile,self).save(*args,**kwaargs)

    def __str__(self):
        return f'{self.user.username} profile'
