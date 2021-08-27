# app/home/views.py

from flask import abort, render_template,jsonify
from flask_login import current_user, login_required
from ..models import Noticia
from . import home

@home.route('/')
def homepage():
    """
    Render the homepage template on the / route
    """
    

    noticias = Noticia.query.all()
    return render_template('home/index.html', title="Home",noticias=noticias)


@home.route('/home')
@login_required
def dashboard():
    """
    Render the dashboard template on the /dashboard route
    """
    
    noticias = Noticia.query.all()
    return render_template('home/dashboard.html', title="Home", noticias=noticias)


# add admin dashboard view
@home.route('/admin/dashboard')
@login_required
def admin_dashboard():
    # prevent non-admins from accessing the page
    if not current_user.is_admin:
        abort(403)
   
    noticias = Noticia.query.all()
    return render_template('home/index.html', title="Home", noticias=noticias)

@home.route('/pag_noticia/<int:id>')
def pag_noticia(id):
    noticia = Noticia.query.get_or_404(id)
    return render_template('home/pag_noticia.html', title=noticia.titulo, noticia=noticia)