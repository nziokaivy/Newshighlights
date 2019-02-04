from flask import render_template
from app import app
from .request import get_sources
# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    general_category = get_sources('general')
    title = 'Home - The Best News Highlight Website Online'
    return render_template('index.html', title = title, general = general_category)