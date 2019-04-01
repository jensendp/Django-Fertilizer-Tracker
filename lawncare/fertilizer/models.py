from django.db import models

class Fertilizer(models.Model):
    name = models.CharField(max_length=200)
    bag_weight = models.IntegerField(default=0)
    bag_coverage = models.IntegerField(default=0)
    percent_N = models.DecimalField(max_digits=4, decimal_places=2)
    percent_P = models.DecimalField(max_digits=4, decimal_places=2)
    percent_K = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return "%s %s-%s-%s" % (self.name, self.percent_N, self.percent_P, self.percent_K)

class Application(models.Model):
    Fertilizer = models.ForeignKey(Fertilizer, on_delete=models.CASCADE)
    bags_applied = models.DecimalField(max_digits=4, decimal_places=2)
    date_applied = models.DateField()

class ApplicationAmount:
    def __init__(self, application, applied_n, applied_p, applied_k):
        self.application = application
        self.applied_n = applied_n
        self.applied_p = applied_p
        self.applied_k = applied_k