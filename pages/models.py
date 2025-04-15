from django.db import models
from ckeditor.fields import RichTextField
from user_authintication.models import Profile

# Create your models here.

condition_choices = (
    ('New', "New"),
    ('Best', 'Best'),
    ('Better', "Better")
)

class Book(models.Model):

    name = models.CharField(max_length=250)
    description = RichTextField()

    genre = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    language = models.CharField(max_length=50)


    condition = models.CharField(max_length=50, choices=condition_choices, default='New')

    price = models.IntegerField()

    location = models.CharField(max_length=250)

    book_image = models.ImageField(upload_to='books/', null=True, blank=True)


    def __str__(self):

        return f'{self.id} - {self.name}'
    

class LendBorrow(models.Model):

    book = models.ForeignKey(Book, related_name='book', on_delete=models.CASCADE)

    lender = models.OneToOneField(Profile, related_name='lender', on_delete=models.CASCADE)

    borrower = models.OneToOneField(Profile, related_name='borrower', on_delete=models.CASCADE)

    @property
    def lendTitle(self):
        return f'{self.lender.name} lends {self.book.name} to {self.borrower.name}'
    


    def __str__(self):

        return f'{self.lender.name} lent {self.book.name} to {self.borrower.name}'
