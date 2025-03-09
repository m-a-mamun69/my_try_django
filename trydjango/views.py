
import random
from django.http import HttpResponse
from articles.models import Articles

# HTML_STRING = "<h1>Hello World</h1>"

def home_view(request):

    random_id = random.randint(1,4)
    article_obj = Articles.objects.get(id=random_id)

    # For Templates
    H1_String = f"<h1>{article_obj.title} ({article_obj.id})!</h1>"
    P_String = f"<p>{article_obj.content}</p>"

    HTML_STRING = H1_String + P_String

    return HttpResponse(HTML_STRING)