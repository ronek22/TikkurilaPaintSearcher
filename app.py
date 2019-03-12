from flask import Flask, render_template, request, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from script.script import search_for_colors
from wtforms import IntegerField, validators, SubmitField
from wtforms.widgets import html5
from wtforms.validators import NumberRange
import os
import logging

app = Flask(__name__)
app.secret_key = 'dev'
bootstrap = Bootstrap(app)

class ColourForm(FlaskForm):
    r = IntegerField("R", widget=html5.NumberInput(min=0, max=255), validators=[validators.NumberRange(min=0, max=255, message="0-255")])
    g = IntegerField("G", widget=html5.NumberInput(min=0, max=255), validators=[validators.NumberRange(min=0, max=255, message="0-255")])
    b = IntegerField("B", widget=html5.NumberInput(min=0, max=255), validators=[validators.NumberRange(min=0, max=255, message="0-255")])
    submit = SubmitField("Szukaj")


@app.route('/', methods=['GET', 'POST'])
def index():
    form = ColourForm()
    if form.validate_on_submit():
        flash("Color submited")
        app.logger.info(form.r.data)
        color = (form.r.data, form.g.data, form.b.data)
        content = search_for_colors(form.r.data, form.g.data, form.b.data)
        content = [(c.index, tuple(c.rgb['py/seq']), c.url) for c in content]
        print(content)
        return render_template("index.html", form=form, content=content, color=color)
    return render_template("index.html", form=form, content=None)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)