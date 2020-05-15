from django.shortcuts import render ,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Review
from django.utils import timezone
from django.contrib.auth.models import User

# Create your views here.
def home(request):
	if request.user.is_authenticated:
		full_name = request.user.get_full_name()
		return render(request, 'home.html',{'full_name':full_name})
	else:
		return render(request, 'home.html')

@login_required
def makereview(request):
	if request.method == 'POST':
		if request.POST['title'] and request.POST['body'] and request.POST['url'] and request.FILES['image']:
			#only if all the fields are exist
			review = Review()
			review.Title = request.POST['title']
			review.Body = request.POST['body']
			try:
				review.Source = request.POST['url']
			except:
				return render(request, 'makereview.html',{'error':"URL invalid"})
			review.Image = request.FILES['image']
			review.Date = timezone.datetime.now()
			review.User_name = request.user
			review.save()
			return redirect('/Reviews/' + str(review.id))
		else:
			return render(request, 'makereview.html',{'error':"All field's must be filled!"})
	else:
		return render(request, 'makereview.html')


def all_reviews(request):
	reviews = Review.objects
	return render(request,'all_reviews.html', {'reviews':reviews})

def review_detailed(request, review_id):
	detailreview = get_object_or_404(Review, pk=review_id)
	return render(request,'review_detailed.html', {'review':detailreview})