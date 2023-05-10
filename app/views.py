from flask import render_template, redirect, url_for

from . import app, db
from .models import Review, Movie
# from .forms import


def index():
    movies = Movie.query.order_by(Movie.id.desc()).all()

    return render_template("index.html", movies=movies)


def movie(id):
    movie_from_id = Movie.query.get(id)

    if movie_from_id.review:
        rating = round(sum([r.rating for r in movie_from_id.review])/len(movie_from_id.review), 2)
    else:
        rating = 0

    reviews_list = movie_from_id.review

    return render_template("movie.html", movie=movie_from_id, rating=rating, reviews=reviews_list)


def add_movie():
    return "Form"


def reviews():
    return "Reviews"


def delete_review():
    return "Delete review"


app.add_url_rule("/", "index", index)
app.add_url_rule("/movie/<int:id>", "movie", movie, methods=["GET", "POST"])
app.add_url_rule("/add_movie", "add_movie", add_movie, methods=["GET", "POST"])
app.add_url_rule("/reviews", "reviews", reviews)
app.add_url_rule("/delete_review", "delete_review", delete_review)
