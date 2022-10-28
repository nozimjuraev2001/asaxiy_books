from django.db import models

# Create your models here.

class AuthorModel(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    phone = models.CharField(max_length=17)
    
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self):
        return self.full_name()    
    
    class Meta:
        verbose_name = 'author'
        verbose_name_plural = 'authors'


class TranslatorModel(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    

class PublisherModel(models.Model):
    name = models.CharField(max_length=100)
    

class FeaturesModel(models.Model):
    COVERS = [
        (1, 'Hard'),
        (0, 'Soft'),
    ]
    PAPER_TYPES = [
        (1, 'A3',),
        (2, 'A4',),
        (3, 'A5',),
    ]
    isbn = models.CharField(max_length=50)
    language = models.CharField(max_length = 50)
    write_type = models.CharField(max_length = 50)
    trasnlator = models.ForeignKey(TranslatorModel, on_delete=models.RESTRICT)
    page_size = models.PositiveBigIntegerField()
    publisher = models.ForeignKey(PublisherModel, on_delete=models.RESTRICT)
    cover = models.IntegerField(choices=COVERS)
    paper_format = models.IntegerField(choices=PAPER_TYPES)
    publication_date = models.DateField()
    
    def __str__(self):
        return self.isbn

class BookImageModel(models.Model):
    image = models.ImageField(upload_to='books')
    

class BookModel(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(AuthorModel, on_delete=models.RESTRICT)
    price = models.FloatField()
    real_price = models.FloatField()
    discount = models.SmallIntegerField(default=0)
    image = models.OneToOneField(BookImageModel, on_delete=models.RESTRICT)
    status = models.BooleanField(default=True)
    description = models.TextField()
    features = models.OneToOneField(FeaturesModel, on_delete=models.RESTRICT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    @property
    def is_discount(self):
        return self.discount != 0
    
    
    def __str__(self):
        return self. title
    
    
    class Meta:
        verbose_name = 'book'
        verbose_name_plural = 'books'