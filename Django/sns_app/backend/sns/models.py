import uuid
from django.db import models
from django.utils import timezone



class Users(models.Model):
    class Meta:
        db_table = 'users'
        ordering = ['name']
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=8, unique=True)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=16)
    password_confirm = models.CharField(max_length=16)



class Posts(models.Model):
    class Meta:
        db_table = 'posts'
        ordering = ['create_at']

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    create_at = models.DateTimeField(default=timezone.now)
    caption = models.CharField(max_length=200)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)



def media_path(user, post, filename):
    return f'{user.name}/{post.id}/{filename}'

class Photos(models.Model):
    class Meta:
        db_table = 'photos'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.FileField(upload_to=media_path)
    post_id = models.ForeignKey(Posts, on_delete=models.CASCADE)



class Comments(models.Model):
    class Meta:
        db_table = 'comments'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    comment = models.TextField(max_length=100)
    post_id = models.ForeignKey(Posts, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)



class Likes(models.Model):
    class Meta:
        db_table = 'likes'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    post_id = models.ForeignKey(Posts, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)


