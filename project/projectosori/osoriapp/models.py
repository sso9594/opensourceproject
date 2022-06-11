from django.db import models
from django.forms import CharField, DateTimeField
from django.contrib.auth.models import User

# 게시물 모델

class Post(models.Model):
    title=models.CharField(max_length=200)
    body=models.TextField()
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    comment=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    post=models.ForeignKey(Post,null=True,blank=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.comment

class FreePost(models.Model):
    title=models.CharField(max_length=200)
    body=models.TextField()
    photo=models.ImageField(blank=True,null=True,upload_to='post_photo')
    date=models.DateTimeField(auto_now_add=True)
    author= models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title        

class FreeComment(models.Model):
    comment=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    post=models.ForeignKey(FreePost,null=True,blank=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.comment

class musinsa_model(models.Model):
    musinsa_key = models.IntegerField(primary_key = True)
    musinsa_image = models.TextField()
    musinsa_link = models.TextField()

    class Meta:
        db_table = 'musinsa'

class mixxo_model(models.Model):
    mixxo_key = models.IntegerField(primary_key = True)
    mixxo_image = models.TextField()
    mixxo_link = models.TextField()

    class Meta:
        db_table = 'mixxo'

class spao_model(models.Model):
    spao_key = models.IntegerField(primary_key = True)
    spao_image = models.TextField()
    spao_link = models.TextField()

    class Meta:
        db_table = 'spao'
    
    



class musinsa_rank(models.Model):
    musinsa_rank_key = models.IntegerField(primary_key = True)
    musinsa_rank_name = models.CharField(max_length= 100)
    musinsa_rank_link = models.TextField()

    class Meta:
        db_table = 'musinsa_rank'

        

class mixxo_rank(models.Model):
    mixxo_rank_key = models.IntegerField(primary_key = True)
    mixxo_rank_name = models.CharField(max_length=100)
    mixxo_rank_link = models.TextField()

    class Meta:
        db_table = 'mixxo_rank'

class spao_rank(models.Model):
    spao_rank_key= models.IntegerField(primary_key = True)
    spao_rank_name = models.CharField(max_length=100)
    spao_rank_link = models.TextField()

    class Meta:
        db_table = 'spao_rank'




