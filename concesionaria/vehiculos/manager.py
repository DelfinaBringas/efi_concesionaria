from django.db import models


class ProductQuerySet(models.QuerySet):

    def actives(self):
        return self.filter(active=True)

    def inactive(self):
        return self.filter(active=False)
    
    def price_total(self):
        total = 0
        for vehiculo in self:
            total += vehiculo.price
        return total
    