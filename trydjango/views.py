
import random
from django.http import HttpResponse
from articles.models import Articles
from django.template.loader import render_to_string

# HTML_STRING = "<h1>Hello World</h1>"

def home_view(request, *args, **kwargs):

    random_id = random.randint(1,4)
    article_obj = Articles.objects.get(id=random_id)
    article_queryset = Articles.objects.all()

    context = {
        "object_list": article_queryset,
        "object": article_obj,
        "id": article_obj.id,
        "title": article_obj.title,
        "content": article_obj.content
    }

    # For Templates
    # H1_String = f"<h1>{article_obj.title} ({article_obj.id})!</h1>"
    # P_String = f"<p>{article_obj.content}</p>"

    HTML_STRING = render_to_string("home-view.html", context=context)

    return HttpResponse(HTML_STRING)