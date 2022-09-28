from django.shortcuts import render
from .models import Listing

# Create your views here.


def all_listings(request):
    """ View to return all listings """

    listings = Listing.objects.all()

    context = {
        'listings': listings,
    }

    return render(request, 'listings/listings.html', context)
