from . import db
from datetime import datetime


class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=True)
    text = db.Column(db.Text, nullable=True)
    rating = db.Column(db.Integer, nullable=True)
    data = db.Column(db.DateTime, default=datetime.utcnow())
    movie_id = db.Column(db.Integer, db.ForeignKey("movie.id"), nullable=True)
    movie = db.relationship("Movie", back_populates="review")


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=True)
    description = db.Column(db.Text, nullable=True)
    img = db.Column(db.String(255), nullable=True)
    review = db.relationship("Review", back_populates="movie")
