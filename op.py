import os
import django
from django.conf import settings

os.environ.setdefault("DJANGO_SETTING_MODULE", "GDSCBlog.settings")
settings.configure()
django.setup()

from BlogApp.models import Post
from CommentApp.models import Comment

post1 = Post.objects.create(title = "First", category ="Passion", content = " Love of My passion" )
post2 = Post.objects.create(title = "Second", category = "Tech", content = "Technology revolution")
post3 = Post.obeject.create(title = "Third", category = "Game", content = "Fun with a lots of games")


pass_post = Post.objects.filter(categoty = "Passion")
for post in pass_post:
    print(post.title)

post1.content = "Update content of first post"
post1.save()

post3.delete()

comm1 = Comment.objects.create(content = "First Comment", author = "First Author", post = post1 )
comm2 = Comment.objects.create(content = "Second Comment", author = "Second Author", post = post2)
comm3 = Comment.objects.create(content = "Third Comment ", author = "Third Author", post = post3)

post2_comments = Comment.objects.filter(post=post2)
for comment in post2_comments:
    print(comment.content)

comm1.content = "Updated content of first comment"
comm1.save()

comm3.delete()
