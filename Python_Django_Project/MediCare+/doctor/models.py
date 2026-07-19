from django.db import models
from django.utils.safestring import mark_safe
class User(models.Model):
    fName = models.CharField(max_length=100)
    lName = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=40)
    profile_pic = models.ImageField(upload_to='profile_pic')
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.fName} {self.lName}"

    def userprofileimage(self):
        if self.profile_pic:
            return mark_safe(f'<img src="{self.profile_pic.url}" width="100px">')
        return "No Image"
class Country(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class State(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class City(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class DoctorSpecialization(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='specialization')

    def __str__(self):
        return self.name

    def specializationImage(self):
        if self.image:
            return mark_safe(f'<img src="{self.image.url}" width="100px">')
        return "No Image"

class Doctor(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    specialization = models.ForeignKey(DoctorSpecialization, on_delete=models.CASCADE)
    experience_years = models.IntegerField()
    qualification = models.CharField(max_length=200)
    consultation_fees = models.DecimalField(max_digits=10, decimal_places=2)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    available_from = models.TimeField()
    available_to = models.TimeField()
    bio = models.TextField()
    image = models.ImageField(upload_to='doctor')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.fName

    def doctorImage(self):
        if self.image:
            return mark_safe(f'<img src="{self.image.url}" width="100px">')
        return "No Image"
class PatientProfile(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dob = models.DateField()
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other')])
    blood_group = models.CharField(max_length=5, choices=[('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-')])
    address = models.TextField()
    phone_no = models.CharField(max_length=15)
    image = models.ImageField(upload_to='patient')

    def __str__(self):
        return self.user.fName

    def patientImage(self):
        if self.image:
            return mark_safe(f'<img src="{self.image.url}" width="100px">')
        return "No Image"
class Appointment(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    appointment_date = models.DateField()
    time_slot = models.TimeField()

    symptoms = models.TextField()

    status = models.CharField(max_length=20, choices=[('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled')])

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient.fName} - {self.doctor.user.fName}"
class Prescription(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    doctor_notes = models.TextField()
    medicines = models.TextField()
    next_visit_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Prescription {self.id}"
class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=20, choices=[('credit_card', 'Credit Card'),('debit_card', 'Debit Card'),('paypal', 'PayPal'),('other', 'Other')])
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'),('completed', 'Completed'),('failed', 'Failed')])
    payment_date = models.DateTimeField()
    def __str__(self):
        return self.user.fName
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user.fName
class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name