from django.db import models

from django.db import models
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField
from cloudinary.models import CloudinaryField

User = get_user_model()

category = (
    ("educative", "Educative"),
    ("social", "Social"),
    ("entertainment", "Entertainment"),
    ("health", "Health"),
    ("technology", "Technology"),
    ("politics", "Politics"),
    ("sports", "Sports"),
    ("arts", "Arts & Culture"),
    ("business", "Business & Finance"),
    ("science", "Science"),
    ("lifestyle", "Lifestyle"),
    ("travel", "Travel"),
    ("food", "Food & Drink"),
    ("environment", "Environment"),
    ("history", "History"),
    ("psychology", "Psychology"),
    ("relationships", "Relationships"),
    ("automotive", "Automotive"),
    ("economy", "Economy"),
    ("pets", "Pets & Animals"),
    ("spirituality", "Spirituality"),
    ("gaming", "Gaming"),
    ("literature", "Literature"),
    ("fashion", "Fashion"),
    ("real_estate", "Real Estate")
)


class Article(models.Model):

    author = models.ForeignKey(User,on_delete=models.CASCADE)
    category = models.CharField(choices=category,max_length=255)
    image = models.ImageField(upload_to="blog-images/",null=True,blank=True)
    title = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)
    intro = RichTextField(blank=True,null=True)
    body = RichTextField(blank=True,null=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    

    def save(self, *args, **kwargs):
        # Check if the article already has a slug or if the title has changed
        if not self.slug or self.title != Article.objects.get(id=self.id).title:
            # Generate slug
            self.slug = orig_slug = slugify(self.title)
            # Ensure the slug is unique (there could be articles with the same title)
            for x in range(1, 1000):  # Assuming no more than 1000 articles will have the same title
                if not Article.objects.filter(slug=self.slug).exclude(id=self.id).exists():
                    break
                self.slug = '%s-%d' % (orig_slug, x)
        super(Article, self).save(*args, **kwargs)

    def __str__(self):

        return f"{self.author} created {self.title}"


class Comments(models.Model):

    article = models.ForeignKey(Article, related_name="comments",on_delete=models.CASCADE)
    username = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True,related_name='replies')

    def __str__(self):

        return f"{self.username} commented {self.content[:35]}..."

class Like(models.Model):

    article = models.ForeignKey(Article,on_delete=models.CASCADE,related_name="likes")
    created_at = models.DateTimeField(auto_now_add=True)
    
