import os
from flask import Flask, render_template, request
from .values import context


def create_app(tc=None):
    app = Flask(__name__, instance_relative_config=True)

    if tc is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(tc)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # jinja custom filters

    # routes and pages
    @app.route('/')
    def app_route_home():
        context['title'] = 'Página inicial'
        return render_template('views/pages/home.html', context=context)

    @app.route('/gallery', methods=['GET'])
    def app_route_gallery():
        requested = request.args.get('u')
        if requested == None:
            requested = 'all'

        image = []

        if requested == 'all':
            for item in context['pics'].keys():
                for value in context['pics'][item]:
                    image.append(value)
        else:
            image = context['pics'][requested]

        context['imgs'] = image
        context['title'] = 'Galeria'
        return render_template('views/pages/gallery.html', context=context)

    @app.route('/about')
    def app_route_about():
        context['title'] = 'Sobre'
        return render_template('views/pages/about.html', context=context)

    @app.route('/contact')
    def app_route_contact():
        context['title'] = 'Contato'
        return render_template('views/pages/home.html', context=context)

    # errors

    # redirects

    return app
