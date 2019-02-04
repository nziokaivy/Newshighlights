from app import app
import urllib.request,json
from .models import sources

# Getting api key
api_key = app.config['NEWS_API_KEY']