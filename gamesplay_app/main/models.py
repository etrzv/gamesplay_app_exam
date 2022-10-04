from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Profile(models.Model):
    FIRST_NAME_MAX_LEN = 30
    LAST_NAME_MAX_LEN = 30
    PASSWORD_LEN = 30

    email = models.EmailField()

    # TODO: check:
    age = models.IntegerField(
        validators=(
            MinValueValidator(12),
        )
    )

    password = models.CharField(
        max_length=PASSWORD_LEN,
    )

    first_name = models.CharField(
        null=True,
        blank=True,
        max_length=FIRST_NAME_MAX_LEN
    )

    last_name = models.CharField(
        null=True,
        blank=True,
        max_length=LAST_NAME_MAX_LEN
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )


class Game(models.Model):
    ACTION = 'Action'
    ADVENTURE = 'Adventure'
    PUZZLE = 'Puzzle'
    STRATEGY = 'Strategy'
    SPORTS = 'Sports'
    BOARD_CARD_GAME = 'Board/Card Game'
    OTHER = 'Other'

    CHOICES = [(x, x) for x in (ACTION, ADVENTURE, PUZZLE, STRATEGY, SPORTS, BOARD_CARD_GAME, OTHER)]

    title = models.CharField(
        max_length=30,
        unique=True,
    )

    category = models.CharField(
        max_length=15,
        choices=CHOICES,
    )

    # TODO: between 0.1 - 5.0 inclusive
    rating = models.FloatField(
        validators=(
            MinValueValidator(0.1),
            MaxValueValidator(5.0),
        )

    )

    max_level = models.IntegerField(
        null=True,
        blank=True,
        validators=(
            MinValueValidator(1),
        )
    )

    image_url = models.URLField()

    summary = models.TextField(
        null=True,
        blank=True,
    )



#     title = models.CharField(verbose_name="Title", max_length=30, unique=True)
#     category = models.CharField(verbose_name="Category", max_length=30, choices=CATEGORY)
#     rating = models.FloatField(verbose_name="Rating", validators=[MinValueValidator(0.1), MaxValueValidator(5.0)])
#     max_level = models.IntegerField(verbose_name="Max Level", validators=[MinValueValidator(1)], null=True, blank=True)
#     image_url = models.URLField(verbose_name="Image URL")
#     summary = models.TextField(verbose_name="Summary", null=True, blank=True)