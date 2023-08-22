from django.shortcuts import render
from .models import Games
from django.http import HttpResponse
from .models import Review
from django.utils import timezone
# Create your views here.

def game(request, game_id):
    req_game = Games.objects.get(pk=game_id)
    current_reviews = req_game.review_set.all()
    current_user_review = Review.objects.filter(user=request.user, game=req_game)
    return render(request, 'games/gameTemplate.html', context= {"game" : req_game, "reviews" : current_reviews, "user_review": current_user_review})

def submitReview(request, game_id):
    if request.method == "GET":
        user = request.user
        game = Games.objects.get(pk=game_id)
        
        hasReviewed = False if not Review.objects.filter(user=user, game=game).values() else True
        if hasReviewed:
            return updateReview(request, game_id)
        
        user_review = request.GET.get('review')
        isRecommended = 1 if request.GET.get('isRecommended') == 'on' else 0
        review = Review(user=user, game=game, verdict=isRecommended, review=user_review)
        review.save()
    
    current_reviews = game.review_set.all()
    new_user_review = Review.objects.filter(user=request.user, game=game)
    return render(request, 'games/gameTemplate.html', context= {"game" : game, "reviews": current_reviews, "user_review": new_user_review})

def updateReview(request, game_id):
    if request.method == 'GET':
        user = request.user
        game = Games.objects.get(pk=game_id)
        old_review = Review.objects.get(user=user, game=game)
        
        new_review = request.GET.get('review')
        new_verdict = 1 if request.GET.get('isRecommended') == 'on' else 0

        old_review.review = new_review
        old_review.verdict = new_verdict
        old_review.review_date = timezone.now()
        old_review.save()
        
    current_reviews = game.review_set.all()
    new_user_review = Review.objects.filter(user=request.user, game=game)
    return render(request, 'games/gameTemplate.html', context= {"game" : game, "reviews": current_reviews, "user_review": new_user_review})
            