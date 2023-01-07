from django.shortcuts import render
from django.http import HttpResponse
from .models import Review

# Create your views here.
def show_review(request):
    review_list = Review.objects.order_by('create_at')
    context = {"review_list":review_list}
    return render(request, 'reviews/review_list.html', context)

