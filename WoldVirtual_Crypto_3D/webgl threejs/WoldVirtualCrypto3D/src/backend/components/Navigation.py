from flask import Blueprint, render_template

# Create a Blueprint for navigation
navigation_bp = Blueprint('navigation', __name__)

@navigation_bp.route('/home')
def home():
    return render_template('home.html')

@navigation_bp.route('/metaverse')
def metaverse():
    return render_template('metaverse.html')

@navigation_bp.route('/profile')
def profile():
    return render_template('profile.html')