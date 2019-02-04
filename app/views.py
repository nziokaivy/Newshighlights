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


@app.route('/articles/<source_id>')
def articles(source_id):

    '''
    View articles page function that returns articles
    '''
    general_articles = get_articles(source_id)
    title = 'Articles'
    return render_template('articles.html', title = title, source_id = general_articles )
