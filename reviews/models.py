from django.db import models
from django.contrib.auth.models import User

class Review(models.Model):
	'''choices'''
	votes_choices = [
		(1,'1'),
		(2,'2'),
		(3,'3'),
		(4,'4'),
		(5,'5'),
		]
	Title = models.CharField(max_length = 100)
	Source = models.URLField(max_length = 100)
	Date = models.DateTimeField()
	Body = models.TextField()
	Votes = models.PositiveIntegerField(
		choices = votes_choices,
		default = '3',
		)#Allowes choices
	Votes_total = models.IntegerField()#stores total of stars
	Uploaded = models.DateField(auto_now = False, auto_now_add =True)
	Image = models.ImageField(upload_to ='product_images/')
	User_name = models.ForeignKey(User, on_delete=models.CASCADE)


	def add_vote(self,vote):
		total = self.Votes_total + vote
		return total

	def total_votes_average(self):
		average = self.Votes_total/len(list_of_voting_users)
		return average.round(2)

	def modified_date(self):
		return self.Date.strftime('%b / %e / %Y')

	def summarry(self):
		return self.Body[:100] + '...'
