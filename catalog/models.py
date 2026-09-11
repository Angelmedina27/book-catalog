from django.db import models

class Publisher(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    # Extra field of our choosing: stores a number with two decimal places
    price = models.DecimalField(max_digits=6, decimal_places=2)
    
    # Relationship: A publisher has many books
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Review(models.Model):
    body = models.TextField()
    
    # Relationship: A book has many reviews
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return f"Review for {self.book.title}: {self.body[:20]}..."