from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    """
    A model representing a blog post.

    Attributes:
        user (ForeignKey): The user who created the post.
        title (CharField): The title of the post.
        content (TextField): The content of the post.
        created_at (DateTimeField): The date and time when the post was created.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Returns the title of the post.

        Returns:
            str: The title of the post.
        """
        return self.title

