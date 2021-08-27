# app/auth/views.py

from flask import flash, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user

from . import auth
from .forms import LoginForm, RegistrationForm
from .. import db
from ..models import Funcionario


@auth.route('/registro', methods=['GET', 'POST'])
def register():
    """
    Handle requests to the /register route
    Add an employee to the database through the registration form
    """
    form = RegistrationForm()
    if form.validate_on_submit():
        funcionario = Funcionario(email=form.email.data,
                            usuario=form.usuario.data,
                            primeiro_nome=form.primeiro_nome.data,
                            ultimo_nome=form.ultimo_nome.data,
                            password=form.senha.data)

        # add employee to the database
        db.session.add(funcionario)
        db.session.commit()
        flash('Voce foi registrado com sucesso! Voce pode logar agora.')

        # redirect to the login page
        return redirect(url_for('auth.login'))

    # load registration template
    return render_template('auth/register.html', form=form, title='Cadastro')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    """
    Handle requests to the /login route
    Log an employee in through the login form
    """
    form = LoginForm()
    if form.validate_on_submit():

        # check whether employee exists in the database and whether
        # the password entered matches the password in the database
        funcionario = Funcionario.query.filter_by(email=form.email.data).first()
        if funcionario is not None and funcionario.verify_password(form.senha.data):
            # log employee in
            login_user(funcionario)

            # redirect to the dashboard page after login
            if funcionario.is_admin:
                return redirect(url_for('home.admin_dashboard'))
            else:
                return redirect(url_for('home.dashboard'))

        # when login details are incorrect
        else:
            flash('Email ou senha invalidos.')

    # load login template
    return render_template('auth/login.html', form=form, title='Login')


@auth.route('/logout')
@login_required
def logout():
    """
    Handle requests to the /logout route
    Log an employee out through the logout link
    """
    logout_user()
    flash('Voce deslogou com sucesso.')

    # redirect to the login page
    return redirect(url_for('auth.login'))