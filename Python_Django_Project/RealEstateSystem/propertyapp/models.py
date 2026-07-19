from django.db import models
from django.utils.safestring import mark_safe

class country(models.Model):
    country_name = models.CharField(max_length=100)
    country_code = models.CharField(max_length=10)
    timestamp = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.country_name

class state(models.Model):
    country_id = models.ForeignKey(country, on_delete=models.CASCADE)
    state_name = models.CharField(max_length=100)
    state_code = models.CharField(max_length=10)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.state_name

class city(models.Model):
    country_id = models.ForeignKey(country, on_delete=models.CASCADE)
    state_id = models.ForeignKey(state, on_delete=models.CASCADE)
    city_name = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.city_name


class agent(models.Model):
    country_id = models.ForeignKey(country, on_delete=models.CASCADE)
    state_id = models.ForeignKey(state, on_delete=models.CASCADE)
    city_id = models.ForeignKey(city, on_delete=models.CASCADE)
    agent_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    profile_image = models.ImageField(upload_to='profile_image')
    experience = models.IntegerField()
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.agent_name
    def agentimage(self):
        return mark_safe('<img src={} width="100px">'.format(self.profile_image.url))

class PROPERTYCATEGORY(models.Model):
    category_name = models.CharField(max_length=100)
    category_image = models.ImageField(upload_to='category_image')
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category_name
    def propertyimage(self):
        return mark_safe('<img src={} width="100px">'.format(self.category_image.url))

class PROPERTY(models.Model):
    category_id = models.ForeignKey(PROPERTYCATEGORY, on_delete=models.CASCADE)
    agent_id = models.ForeignKey(agent, on_delete=models.CASCADE)
    property_title = models.CharField(max_length=100)
    description = models.TextField()
    property_type = models.CharField(max_length=20, choices=[('apartment', 'Apartment'),('villa', 'Villa'),
                                                             ('office', 'Office'),('shop', 'Shop'),('land', 'Land')])
    price = models.FloatField()
    address = models.TextField()
    property_image = models.ImageField(upload_to='property_image')
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.property_title
    def property(self):
        return mark_safe('<img src={} width="100px">'.format(self.property_image.url))

class customers(models.Model):
    country_id = models.ForeignKey(country, on_delete=models.CASCADE)
    state_id = models.ForeignKey(state, on_delete=models.CASCADE)
    city_id = models.ForeignKey(city, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    profile_image = models.ImageField(upload_to='profile_image')
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.customer_name
    def customerimage(self):
        return mark_safe('<img src={} width="100px">'.format(self.profile_image.url))

class propertyvisit(models.Model):
    customer_id = models.ForeignKey(customers, on_delete=models.CASCADE)
    property_id = models.ForeignKey(PROPERTY, on_delete=models.CASCADE)
    visit_date = models.DateField()
    visit_time = models.TimeField()
    status = models.CharField(max_length=20, choices=[('scheduled', 'Scheduled'),('completed', 'Completed'),
                                                      ('cancelled', 'Cancelled')])
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.customer_id} - {self.property_id}"

class propertyinquiry(models.Model):
    customer_id = models.ForeignKey(customers, on_delete=models.CASCADE)
    property_id = models.ForeignKey(PROPERTY, on_delete=models.CASCADE)
    message = models.TextField()
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'),('replied', 'Replied'),('closed', 'Closed')])
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.customer_id} - {self.property_id}"


class propertybooking(models.Model):
    customer_id = models.ForeignKey(customers, on_delete=models.CASCADE)
    property_id = models.ForeignKey(PROPERTY, on_delete=models.CASCADE)
    booking_amount = models.FloatField()
    booking_date = models.DateField()
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'),('confirmed', 'Confirmed'),('cancelled', 'Cancelled')])
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.customer_id} - {self.property_id}"

class payment(models.Model):
    booking_id = models.ForeignKey(propertybooking, on_delete=models.CASCADE)
    amount = models.FloatField()
    payment_method = models.CharField(max_length=20, choices=[('cash', 'Cash'),('card', 'Card'),
                                                              ('upi', 'UPI'),('net_banking', 'Net Banking')])
    transaction_id = models.CharField(max_length=100)
    payment_status = models.CharField(max_length=20, choices=[('pending', 'Pending'),('paid', 'Paid'),('failed', 'Failed')])
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.booking_id)


class review(models.Model):
    customer_id = models.ForeignKey(customers, on_delete=models.CASCADE)
    property_id = models.ForeignKey(PROPERTY, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.customer_id} - {self.property_id}"