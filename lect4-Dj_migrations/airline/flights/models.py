from django.db import models

# Create your models here.

class Airport(models.Model):
	code = models.CharField(max_length=3)
	city = models.CharField(max_length=64)

	# The string representation of a model
	def __str__(self):
		return f"{self.city} ({self.code})"

		
class Flight(models.Model):
	origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="deparures")
	destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
	duration = models.IntegerField()

	# The string representation of a model
	def __str__(self):
		return f"{self.id}: {self.origin} to {self.destination}"
	
	# Test function for valid flight 
	def is_valid_flight(self):
		return self.origin != self.destination and self.duration >= 0


class Passenger(models.Model):
	first = models.CharField(max_length=64)
	last = models.CharField(max_length=64)

	# Association with flights, this can be an empty field
	# Related_name will, in reverse, return a list of all the passengers for a one Flght
	flights = models.ManyToManyField(Flight, blank=True, related_name="passengers")
	
	# The string representation of a model
	def __str__(self):
		return f"{self.first} {self.last}"