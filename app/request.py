from app import app
import urllib.request,json
from .models import sources,articles
from datetime import datetime



Sources = sources.Sources

# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the source base url
sources_url = app.config["SOURCES_BASE_URL"]

# Getting the articles base url
articles_url = app.config["ARTICLES_BASE_URL"] 


def get_sources(category):
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = sources_url.format(category,api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response['sources']:
            sources_results = process_results(get_sources_response['sources'])


    return sources_results


def process_results(sources_list):
    '''
    Function  that processes the source result and transform them to a list of Objects

    Args:
        sources_list: A list of dictionaries that contain sources details

    Returns :
        sources_results: A list of movie objects
    '''
    sources_results = []
    for source in sources_list:
        id = source.get('id')
        name = source.get('name')
        description = source.get('description')
        url = source.get('url')
        category = source.get('category')
        country = source.get('country')

        if url:
            source_object = Sources(id,name,description,url,category,country)
            sources_results.append(source_object)

    return sources_results

def get_articles(source_id):
    '''
    Function that gets articles based on the source id
    '''
    get_article_location_url = articles_url.format(source_id,api_key)

    with urllib.request.urlopen(get_article_location_url) as url:
        articles_location_data = url.read()
        articles_location_response = json.loads(articles_location_data)

        articles_location_results = None

        if articles_location_response['articles']:
            author = articles_location_response.get('author')
            title = articles_location_response.get('title')
            description = articles_location_response.get('description')
            url= articles_location_response.get('url')
            urlToImage = articles_location_response.get('urlToImage')
            publishedAt = articles_location_response.get('publishedAt')
            
            articles_location_results = process_articles(articles_location_response['articles'])
           
    return articles_location_results    

def process_articles(articles_list):
    '''
    Function that processes the json results for the articles
    '''
    article_location_list = []
    
    for article in articles_list:
        author = article.get('author')
        title = article.get('title')
        description = article.get('description')
        url = article.get('url')
        urlToImage = article.get('urlToImage')
        date_published = article.get('publishedAt')

        publishedAt = datetime(year=int(date_published[0:4]),month=int(date_published[5:7]),day=int(date_published[8:10]),hour=int(date_published[11:13]),minute=int(date_published[14:16]))

        if urlToImage:
            article_source_object = Articles(author,title,description,url,urlToImage,publishedAt)
            article_location_list.append(article_source_object)
        
    return article_location_list


