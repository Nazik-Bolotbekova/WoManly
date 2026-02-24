from django.db import models
from .choice import StaffPosition, Status, Priority
from apps.users.models import CustomUser


class Contact(models.Model):
    organization_name = models.CharField(max_length=200,blank=True,null=True)
    email = models.EmailField()
    telegram = models.CharField(max_length=25,blank=True,null=True)
    phone_number = models.CharField(max_length=20,blank=True,null=True)
    social_links = models.JSONField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.organization_name
    
    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'



class BasePost(models.Model):
    header = models.CharField(max_length=50)
    text = models.TextField(max_length=500)
    contacts = models.ForeignKey(Contact,on_delete=models.SET_NULL,null=True,blank=True)#связь с контактс
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
 


class Category(models.Model):
    name = models.CharField(max_length=100,unique=True,)
    short_description = models.CharField(max_length=100,)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'



class Article(BasePost):
    author = models.ForeignKey(CustomUser,on_delete=models.CASCADE) # author это же по сути user да?
    image = models.ImageField(upload_to='articles_images',null=True,blank=True)
    is_published = models.BooleanField(default=False)
    slug = models.SlugField()
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    views_count = models.PositiveIntegerField(default=0)
    updated_at = models.DateField(auto_now=True)



    def __str__(self):
        return self.author
    
    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'



class Opportunity(models.Model):
    image = models.ImageField(upload_to='opportunity_images',null=True,blank=True)
    deadline = models.DateField()
    is_active = models.BooleanField(default=True)
    application_link = models.CharField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)


    def __str__(self):
        return self.header
    
    class Meta:
        verbose_name = 'Возможность'
        verbose_name_plural = 'Возможности'



class StaffMember(models.Model):
    name = models.CharField(max_length=25,null=False,blank=False)
    position = models.CharField(max_length=25,choices=StaffPosition.choices,default=StaffPosition.team_staff)
    tg_username = models.CharField(unique=True,blank=True,null=True) 
    image = models.ImageField(upload_to='WoManly/img')
    bio = models.TextField(max_length=100)
    is_active = models.BooleanField(default=True)
    social_links = models.JSONField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Член Команды'
        verbose_name_plural = 'Члены Команды'



class Achievements(models.Model):
    header = models.CharField(max_length=50)
    achievement = models.TextField(max_length=500)
    image = models.ImageField(upload_to='achievment_images',null=True,blank=True)
    text = models.TextField(max_length=500,null=False,blank=False)
    date_archieved = models.DateField()
    category = models.ForeignKey(Category,on_delete=models.DO_NOTHING)
    is_featured = models.BooleanField(default=False)
    person = models.ForeignKey(CustomUser,on_delete=models.CASCADE) #связь с юзером
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.header

    class Meta:
        verbose_name = 'Достижение'
        verbose_name_plural = 'Достижения'



class SupportRequest(models.Model):
    text = models.TextField()
    subject = models.CharField(max_length=25)
    status = models.CharField(choices=Status.choices,default=Status.new)
    created_at = models.DateTimeField(auto_now_add=True,)
    assigned_to = models.ForeignKey(StaffMember,on_delete=models.DO_NOTHING)
    priority = models.CharField(choices=Priority.choices)  
    updated_at = models.DateTimeField(auto_now=True,)
    response = models.TextField()  



class Review(models.Model):
    email = models.EmailField()
    full_name = models.CharField(max_length=100,)
    review = models.TextField()
    rating = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True,)
    updated_at = models.DateTimeField(auto_now=True,)
    is_approved = models.BooleanField(default=False)


    def  __str__(self):
        return self.full_name


    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
