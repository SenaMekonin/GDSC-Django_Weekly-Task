# orm_operations.py
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "GDSCBlog.settings")
django.setup()

from BlogApp.models import Post
from CommentApp.models import Comment

# Posts operations
def create_posts():
    Post.objects.create(title="Title 1", content="Content 1", category="Category 1", tags=["tag1", "tag2"])
    Post.objects.create(title="Title 2", content="Content 2", category="Category 2", tags=["tag2", "tag3"])
    Post.objects.create(title="Title 3", content="Content 3", category="Category 1", tags=["tag1", "tag3"])

def query_posts_by_category(category):
    posts = Post.objects.filter(category=category)
    for post in posts:
        print(post.title, post.content)

def update_post_content(post_title, new_content):
    post = Post.objects.get(title=post_title)
    post.content = new_content
    post.save()

def delete_post(post_title):
    Post.objects.get(title=post_title).delete()

# Comments operations
def create_comments():
    post1 = Post.objects.get(title="Title 1")
    post2 = Post.objects.get(title="Title 2")
    
    Comment.objects.create(content="Comment 1", author="Author 1", published_date="2024-01-23 12:00:00", post=post1)
    Comment.objects.create(content="Comment 2", author="Author 2", published_date="2024-01-23 12:30:00", post=post2)
    Comment.objects.create(content="Comment 3", author="Author 3", published_date="2024-01-23 13:00:00", post=post1)

def query_comments_by_post(post_title):
    post = Post.objects.get(title=post_title)
    comments = Comment.objects.filter(post=post)
    for comment in comments:
        print(comment.author, comment.content)

def update_comment_content(comment_id, new_content):
    comment = Comment.objects.get(id=comment_id)
    comment.content = new_content
    comment.save()

def delete_comment(comment_id):
    Comment.objects.get(id=comment_id).delete()

if __name__ == "__main__":
    create_posts()
    query_posts_by_category("Category 1")
    update_post_content("Title 1", "Updated content for Title 1")
    delete_post("Title 2")

    create_comments()
    query_comments_by_post("Title 1")
    update_comment_content(1, "Updated content for Comment 1")
    delete_comment(2)
