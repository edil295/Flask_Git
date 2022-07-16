from flask import render_template, url_for, redirect, request, flash
from . import models, db, forms


def index():
    record = models.Transactons.query.all()
    return render_template('index.html', record=record)


def add_transaction():
    form = forms.TransactionForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            position = models.Transactons(
                period=request.form.get('period'),
                value=request.form.get('value'),
                status=request.form.get('status'),
                unit=request.form.get('unit'),
                subject=request.form.get('subject'))
            db.session.add(position)
            db.session.commit()
            flash('Вы успешно добавили транзакцию', category='success')
            return redirect(url_for('index'))
        elif form.errors:
            for errors in form.errors.values():
                for error in errors:
                    flash(error, category='danger')
    return render_template('add_position.html', form=form)