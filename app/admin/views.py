from flask import abort, flash, redirect, render_template, url_for
from flask_login import current_user, login_required

from . import admin
from .forms import NoticiaFormulario, FuncionarioFormulario
from .. import db
from ..models import Noticia, Funcionario


def check_admin():
    """
    Prevent non-admins from accessing the page
    """
    if not current_user.is_admin:
        abort(403)


# Department Views


@admin.route('/noticias', methods=['GET', 'POST'])
@login_required
def listar_noticias():
    """
    Lista todas as noticias
    """
    #check_admin()

    noticias = Noticia.query.all()

    return render_template('admin/noticias/noticias.html',
                           noticias=noticias, title="Noticias")


@admin.route('/noticias/add', methods=['GET', 'POST'])
@login_required
def add_noticias():
    """
    Add a department to the database
    """
    #check_admin()

    add_noticia = True

    form = NoticiaFormulario()
    if form.validate_on_submit():
        noticia = Noticia(titulo=form.titulo.data,
                                caminho_imagem=form.caminho_imagem.data,
                                texto=form.texto.data)
        try:
            # add department to the database
            db.session.add(noticia)
            db.session.commit()
            flash('Voce adicionou uma nova noticia com sucesso.')
        except:
            # in case department name already exists
            flash('Error: noticia ja existe')

        # redirect to departments page
        return redirect(url_for('admin.listar_noticias'))

    # load department template
    return render_template('admin/noticias/noticia.html', action="Add",
                           add_noticia=add_noticia, form=form,
                           title="Adicionar noticia")


@admin.route('/noticias/editar/<int:id>', methods=['GET', 'POST'])
@login_required
def editar_noticia(id):
    """
    Edit a department
    """
    #check_admin()

    add_noticia = False

    noticia = Noticia.query.get_or_404(id)
    form = NoticiaFormulario(obj=noticia)
    if form.validate_on_submit():
        noticia.titulo = form.titulo.data
        noticia.caminho_imagem = form.caminho_imagem.data
        noticia.texto = form.texto.data
        db.session.commit()
        flash('Voce editou a noticia com sucesso.')

        # redirect to the departments page
        return redirect(url_for('admin.listar_noticias'))

    form.caminho_imagem.data = noticia.caminho_imagem
    form.titulo.data = noticia.titulo
    return render_template('admin/noticias/noticia.html', action="Edit",
                           add_noticia=add_noticia, form=form,
                           noticia=noticia, title="Editar noticia")


@admin.route('/noticias/apagar/<int:id>', methods=['GET', 'POST'])
@login_required
def deletar_noticia(id):
    """
    Delete a department from the database
    """
    #check_admin()

    noticia = Noticia.query.get_or_404(id)
    db.session.delete(noticia)
    db.session.commit()
    flash('Noticia apagada com sucesso.')

    # redirect to the departments page
    return redirect(url_for('admin.listar_noticias'))

    return render_template(title="Apagar Noticia")


"""
VIEWS PARA FUNCIONARIOS
"""

@admin.route('/funcionarios', methods=['GET', 'POST'])
@login_required
def listar_funcionarios():
    """
    Lista todos os funcionarios
    """
    check_admin()

    funcionarios = Funcionario.query.all()

    return render_template('admin/funcionarios/funcionarios.html',
                           funcionarios=funcionarios, title="Funcionarios")


@admin.route('/funcionarios/editar/<int:id>', methods=['GET', 'POST'])
@login_required
def editar_funcionario(id):
    """
    Editar um funcionario
    """
    check_admin()

    add_noticia = False

    funcionario = Funcionario.query.get_or_404(id)
    form = FuncionarioFormulario(obj=funcionario)
    if form.validate_on_submit():
        funcionario.email = form.email.data
        funcionario.usuario = form.usuario.data
        funcionario.primeiro_nome = form.primeiro_nome.data
        funcionario.ultimo_nome = form.ultimo_nome.data
        db.session.commit()
        flash('Voce alterou dados do funcionario com sucesso.')

        # redirect to the departments page
        return redirect(url_for('admin.listar_funcionarios'))

    form.email.data = funcionario.email
    form.usuario.data = funcionario.usuario
    form.primeiro_nome.data = funcionario.primeiro_nome
    form.ultimo_nome.data = funcionario.ultimo_nome
    return render_template('admin/funcionarios/funcionario.html', action="Edit",
                           add_noticia=add_noticia, form=form,
                           funcionario=funcionario, title="Editar funcionario")


@admin.route('/funcionarios/apagar/<int:id>', methods=['GET', 'POST'])
@login_required
def deletar_funcionario(id):
    """
    Apagar um funcionario do banco de dados
    """
    check_admin()

    funcionario = Funcionario.query.get_or_404(id)
    db.session.delete(funcionario)
    db.session.commit()
    flash('Funcionario apagado com sucesso.')

    # redirect to the departments page
    return redirect(url_for('admin.listar_funcionarios'))

    return render_template(title="Apagar funcionario")