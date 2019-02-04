from flask import render_template
from app import app
from .request import get_sources
# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    general_sources = get_sources('general')
    title = 'Home - The Best News Highlight Website Online'
    return render_template('index.html', title = title, general = general_sources)

@app.route('/news/<source_id>')
def articles(source_id):

    '''
    View news page function that returns articles
    '''
    title = 'Articles'
    article_source = get_source(source_id)
    return render_template('articles.html', title = title, source_id = article_source)
