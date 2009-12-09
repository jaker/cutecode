from django.contrib.syndication.feeds import Feed
from apps.poster.models import Code

class LatestEntries(Feed):
  title = "Latest cuteco.de snippets"
  link = "/cute/"
  description = "The latest code snippets submitted to cuteco.de"

  def items(self):
    return Code.objects.order_by('-submitted')[:10]
