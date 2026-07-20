from django.db import models
from django.utils.safestring import mark_safe


# Create your models here.
class User(models.Model):
    firstName = models.CharField(max_length=60)
    lastName = models.CharField(max_length=60)
    email = models.EmailField()
    password = models.CharField(max_length=60)
    profile = models.ImageField(upload_to='Users')
    timestamp = models.DateTimeField(auto_now=True)

    def UserImage(self):
        return mark_safe('<img src={} width="200px">'.format(self.profile.url))

    def __str__(self):
        return f"{self.firstName} {self.lastName}"

class country(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name

class state(models.Model):
    country = models.ForeignKey(country, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class city(models.Model):
    state = models.ForeignKey(state, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class userprofile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10)
    address = models.TextField()
    country = models.ForeignKey(country, on_delete=models.CASCADE)
    state = models.ForeignKey(state, on_delete=models.CASCADE)
    city = models.ForeignKey(city, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)

class category(models.Model):
    categoryName = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='category')
    timestamp = models.DateTimeField(auto_now=True)
    def categoryImage(self):
        return mark_safe('<img src={} width="200px">'.format(self.image.url))
    def __str__(self):
        return self.categoryName

class game(models.Model):
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    address = models.TextField()
    city = models.ForeignKey(city, on_delete=models.CASCADE)
    pricePerHour = models.FloatField()
    totalSystem= models.IntegerField()
    availableSystem= models.IntegerField()
    image = models.ImageField(upload_to='game')
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    def gameImage(self):
        return mark_safe('<img src={} width="200px">'.format(self.image.url))

class GameImages(models.Model):
    game = models.ForeignKey(game, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='game')
    def GAMEImage(self):
        return mark_safe('<img src={} width="200px">'.format(self.image.url))

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(game, on_delete=models.CASCADE)
    bookingDate = models.DateTimeField()
    startTime = models.TimeField()
    endTime = models.TimeField()
    totalAmount = models.FloatField()
    status = models.CharField(max_length=100, choices=[('pending','Pending'),('confirmed','Confirmed'),('cancelled','Cancelled')])
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} / {self.startTime}-{self.endTime} / {self.bookingDate}"

class payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    game = models.ForeignKey(game, on_delete=models.CASCADE)
    amount = models.FloatField()
    paymentMethod = models.CharField(max_length=100, choices=[('credit_card','Credit_card'),('debit_card','Debit_card'),('paypal','PayPal')])
    paymentStatus= models.CharField(max_length=100, choices=[('pending','Pending'),('completed','Completed'),('failed','Failed')])
    paymentDate = models.DateTimeField(auto_now=True)


class reviews(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(game, on_delete=models.CASCADE)
    rating = models.FloatField()
    comment = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)

class ContactUs(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField()
    phone = models.BigIntegerField()
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)