from flask import Blueprint, render_template

auth = Blueprint('auth', __name__, template_folder = 'auth_templates')

@auth.route('/')
def home():
    return render_template('index.html')


@auth.route('/fav_five')
def fav_five():
    fav_five = [{
            'name':'Pride and Prejudice',
            'year': '2005',
            'genre':'Romance/Drama'
        }, 
        {
            'name':'The Notebook',
            'year':'2004',
            'genre':'Romance/Drama'
        }, 
        {
            'name':'The Nice Guys',
            'year': '2016',
            'genre':'Action/Mystery'
        }, 
        {
            'name':'Anne of Green Gables',
            'year': '1985',
            'genre':'Drama/Costume drama'
        }, 
        {
            'name':'Lord of the Rings',
            'year': '2001',
            'genre':'Fantasy/Adventure'
        }]
    return render_template('fav_five.html', movies = fav_five)