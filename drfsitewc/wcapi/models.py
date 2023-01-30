from django.db import models

class Statistics(models.Model):
    user_id = models.CharField(max_length=255)
    total_received = models.CharField(max_length=255)
    number_of_transactions = models.CharField(max_length=255)
    date_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.total_received


class Settings(models.Model):
    user_id = models.CharField(max_length=255)
    language = models.CharField(max_length=255)
    main_currency = models.CharField(max_length=255)
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.language

class History(models.Model):
    user_id = models.CharField(max_length=255)
    payment_id = models.CharField(max_length=255)
    date_tranz = models.CharField(max_length=255)
    value_tranz = models.CharField(max_length=255)
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.payment_id