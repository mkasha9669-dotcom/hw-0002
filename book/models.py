from django.db import models

# Create your models here.



class Author(models.Model):
    first_name = models.CharField(max_length=200)   
    last_name = models.CharField(max_length=200)    
    nationality = models.CharField(max_length=200)  
    age = models.PositiveIntegerField()              
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)      

    def total_books(self):
       return self.books.count()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class CoverType(models.TextChoices):
    HARD = 'hard', 'Qattu jilt'
    SOFT = 'soft', 'Yumsho jilt'


class Book(models.Model):
    author = models.ForeignKey(
        'Author',
        on_delete=models.CASCADE,
        related_name='book'
    )

    pages = models.PositiveIntegerField()        
    price = models.DecimalField(max_digits=10, decimal_places=2)  
    cover_type = models.CharField(
        max_length=10,
        choices=CoverType.choices
    )  

    image = models.ImageField(upload_to='Al Jabr/', blank=True, null=True)  

    total_sold = models.PositiveIntegerField(default=0)  
    in_stock = models.BooleanField(default=True)       
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)     
    def __str__(self):
        return f"Book - {self.author}"





class BookStore(models.Model):
    name = models.CharField(max_length=150)     
    address = models.CharField(max_length=255)  

    books = models.ManyToManyField(
        'Book',
        related_name='bookstores'
    )  

    seller = models.ForeignKey(
        BookStore,
        on_delete=models.CASCADE,
        related_name='bookstores'
    )  

    total_sold = models.PositiveIntegerField(default=0)  

    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)    

    def __str__(self):
        return self.name
