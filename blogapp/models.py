from django.db import models

class PortfolioItem(models.Model):
    # Campos
    image = models.ImageField(upload_to='portfolio')
    caption = models.CharField(max_length=200)
    target_modal = models.CharField(max_length=50)

    def __str__(self):
        return self.caption


class ContactMessage(models.Model):
    # Campos
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self):
        return self.name


class SocialLink(models.Model):
    # Campos
    name = models.CharField(max_length=50)
    url = models.URLField()

    def __str__(self):
        return self.name

class SearchForm(models.Model):
    query = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.query
    
class Portfolio(models.Model):
    # Campos
    title = models.CharField(max_length=200)
    description = models.TextField()
    items = models.ManyToManyField('PortfolioItem')

    def __str__(self):
        return self.title


class About(models.Model):
    # Campos
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title


class Contact(models.Model):
    # Campos
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.email