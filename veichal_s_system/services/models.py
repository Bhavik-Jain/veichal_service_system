from django.db import models



class Component(models.Model):
    name = models.CharField(max_length=100)
    repair_price = models.DecimalField(max_digits=10, decimal_places=2)
    new_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Vehicle(models.Model):
    vehicle_id = models.CharField(max_length=50, unique=True)
    owner_name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.model} ({self.vehicle_id})"

class Issue(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='issues')
    description = models.TextField()
    component = models.ForeignKey(Component, on_delete=models.SET_NULL, null=True)
    is_new_component = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_price(self):
        return self.component.new_price if self.is_new_component else self.component.repair_price

    def __str__(self):
        return f"Issue for {self.vehicle.model} - {self.description[:20]}"

class Transaction(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transaction for {self.vehicle.vehicle_id} - ${self.total_price}"
