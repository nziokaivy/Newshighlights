from flask import render_template
from app import app
from .request import get_sources,get_articles


# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    general_sources = get_sources('general')
    general_tech = get_sources('technology')
    general_business = get_sources('business')
    general_sports = get_sources('sports')
    title = 'Home - The Best News Highlight Website Online'
    return render_template('index.html', title = title, general = general_sources, technology = general_tech, business = general_business, sports = general_sports)


@app.route('/articles/<source_id>&<int:per_page>')
def articles(source_id,per_page):
    '''
    Function that returns articles based on their sources
    '''
    
    news_source = get_articles(source_id,per_page)
    title = f'{source_id} | All Articles'
    return render_template('articles.html', title = title, name = source_id, news = news_source)
