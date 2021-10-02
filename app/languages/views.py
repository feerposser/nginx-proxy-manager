from django.db.models.base import Model
from django.shortcuts import render

from languages.models import ModelLanguage


def index(request):

  languages = ModelLanguage.objects.all()

  return render(request, "index.html", {"languages": languages})