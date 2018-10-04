from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid
# Create your models here.

#new function for deal with duplicated name for the avatar
def scramble_uploaded_filename(instance, filename):
    extension = filename.split(".")[-1]
    return "{}.{}".format(uuid.uuid4(), extension)

class Skill(models.Model):

    SKILL_TYPE          = (
        (1, "technical skill"),
        (2, "soft skill")
    )
    name                = models.CharField(max_length=30)
    skill_type          = models.IntegerField(choices=SKILL_TYPE,default=1)
    description         = models.CharField(max_length=100, blank=True)

    class Meta:
        unique_together = ('name',)
        ordering        = ['name']

    def __unicode__(self):
        return '{0}: {1}'.format(self.name, self.description)


class Interest(models.Model):

    inte_name = models.CharField(max_length=30)
    description = models.CharField(max_length=100, blank=True)

    class Meta:
        ordering = ['inte_name']

    def __str__(self):
        return self.inte_name


#one-to-one relation
class Profile(models.Model):

    user                = models.OneToOneField(User,
                                on_delete = models.CASCADE)
    location            = models.CharField(max_length=64,blank=True)
    about               = models.TextField(max_length=100, blank=True, default='')
    phone               = models.IntegerField(null=True, blank=True)
    birthday            = models.DateField(null=True, blank=True)
    image               = models.ImageField('Avatar', upload_to=scramble_uploaded_filename, null=True, blank=True) #new
    linked_in_website   = models.URLField(null=True, blank=True)
    twitter_website     = models.URLField(null=True, blank=True)
    facebook_website    = models.URLField(null=True, blank=True)
    date_created        = models.DateTimeField(auto_now_add=True)
    date_updated        = models.DateTimeField(auto_now=True)
    owned_skills        = models.ManyToManyField(Skill,)
    chosen_interests     = models.ManyToManyField(Interest)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

# many to many relations
class OwnedSkills(models.Model):
    skill               = models.ForeignKey(Skill, on_delete=models.CASCADE)
    profile             = models.ForeignKey(Profile, on_delete=models.CASCADE)

#new transcript table

class Transcript(models.Model):
    profile             = models.ForeignKey(Profile, related_name='transcripts',on_delete=models.CASCADE, null=True)
    transcript          = models.FileField('Transcript',upload_to=scramble_uploaded_filename, null=True, blank=True) #new
    date_created        = models.DateTimeField(auto_now_add=True)
    date_updated        = models.DateTimeField(auto_now=True)


class ChosenInterests(models.Model):
    interest = models.ForeignKey(Interest, on_delete=models.CASCADE,
                                 null  = True,
                                 blank = True,)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)



#foreign Key relations
class Education(models.Model):

    edu_name      = models.CharField(max_length = 50)
    qualification = models.CharField(max_length = 30)
    institute     = models.CharField(max_length = 20)
    description   = models.CharField(max_length = 80, blank = True)


    profile = models.ForeignKey(
        Profile,
        on_delete = models.CASCADE,
        related_name = 'education',
        null = True,
        blank = True,
    )

    class Meta:
        ordering = ['edu_name']

    def __str__(self):
        return self.edu_name


class Wh (models.Model):

    work_name = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    company_name = models.CharField(max_length=30)
    description = models.CharField(max_length=100, blank=True)

    profile = models.ForeignKey(
        Profile,
        related_name = 'work_history',
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ['work_name']

    def __str__(self):
        return self.work_name

