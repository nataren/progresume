from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    def __str__(self):
        return ' '.join([self.first_name, self.middle_name, self.last_name])

class Company(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)

    def __str__(self):
        return ' '.join([self.name, self.location])

class Employment(models.Model):
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    title = models.CharField(max_length=200)
    company = models.ForeignKey(
        'Company',
        on_delete=models.CASCADE,
    )
    person = models.ForeignKey(
        'Person',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return ' '.join(map(str, [self.company, self.title, self.start_date, self.end_date, self.person]))

