from django.db import models
import re

# Create your models here.

class UserManager(models.Manager):
    def validator(self, postData):
        email_validate=re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        errors = {}
        if len(postData['first'])< 2:
            errors['first'] = "First name must be at least 2 characters!"
        if len(postData['last'])< 2:
            errors['last'] = "Last name must be at least 2 characters!"
        if not email_validate.match(postData['email']):
            errors['email'] = "Email must be in valid format!"
        if len(postData['password']) < 8:
            errors['password'] = "Password must be at least 8 characters"
        if postData['password'] != postData['confirm_password']:
            errors['confirm_password'] = "Passwords do not match!"
        return errors


class User(models.Model):
    first=models.CharField(max_length=225)
    last=models.CharField(max_length=225)
    email=models.CharField(max_length=225)
    password=models.CharField(max_length=225)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects = UserManager()

class MessageManager(models.Manager):
    def post_validator(self, postData):
        errors = ""
        if len(postData['content']) < 1:
            errors = "You must provide at least 1 character in your post!"
        return errors

class MessagePost(models.Model):
    content=models.TextField()
    poster=models.ForeignKey(User, related_name="messages", on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects = MessageManager()

class Comment(models.Model):
    content=models.TextField()
    post=models.ForeignKey(User,related_name="comments", on_delete=models.CASCADE)
    message=models.ForeignKey(MessagePost,related_name="comments", on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)