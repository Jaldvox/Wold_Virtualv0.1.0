from flask import render_template

def Layout(page_title, content):
    return render_template('layout.html', title=page_title, content=content)