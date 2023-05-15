from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length


class MovieForm(FlaskForm):
    title = StringField("Название фильма", validators=[
        DataRequired(message='Поле "Название фильма" не может быть пустым'),
        Length(max=255, message="Название не может быть более 255 символов")
    ])
    description = TextAreaField("Описание фильма", validators=[
        DataRequired(message='Поле "Описание фильма" не может быть пустым')
    ])
    file = FileField("Постер фильма", validators=[
        DataRequired(message='Поле "Постер фильма" не может быть пустым')
    ])
    submit = SubmitField("Добавить фильм")


class ReviewForm(FlaskForm):
    name = StringField("Имя", validators=[
        DataRequired(message='Поле "Имя" не может быть пустым')
    ])
    text = TextAreaField("Отзыв", validators=[
        DataRequired(message='Поле "Отзыв" не может быть пустым')
    ])
    rating = SelectField("Рейтинг", choices=list(range(10, 0, -1)), default=10)
    submit = SubmitField("Добавить отзыв")
