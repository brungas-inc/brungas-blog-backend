from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.core.mail import EmailMultiAlternatives
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.urls import reverse

from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail  


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    email_plaintext_message = "{}?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key)

    send_mail(
        # title:
        "Password Reset for {title}".format(title="Some website title"),
        # message:
        email_plaintext_message,
        # from:
        "noreply@somehost.local",
        # to:
        [reset_password_token.user.email]
    )


class Post(models.Model):
    user= models.ForeignKey(User, on_delete=models.PROTECT)
    post_title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
  

    def __str__(self):
        return f'{self.post_title}'

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    post_id = models.AutoField(primary_key=True, editable=False)
    comment_text = models.TextField(null=True, blank=True)
    date_commented = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.comment_text}'

class PostLikes(models.Model):
    likeusers = models.ManyToManyField(User)
    likepost = models.ForeignKey(Post,on_delete=models.CASCADE,null=True,related_name='likepost')        