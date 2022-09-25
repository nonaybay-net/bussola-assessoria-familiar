import os
from flask import Flask, render_template, request, send_from_directory
from random import shuffle
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
    @app.template_filter('randlist')
    def filter_randlist(seq, re=5):
        r = list(seq)

        if (re >= 0):
            shuffle(r)

            return filter_randlist(r, (re - 1))
        elif (re == 0):
            return r
        else:
            return seq

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

    @app.route('/comming-soon')
    def app_route_update():
        context['title'] = 'Atualizações Futuras'
        return render_template('views/pages/updates.html', context=context)

    # errors

    # redirects

    # routes from static
    @app.route('/sitemap.xml')
    def serving_static():
        return send_from_directory(app.static_folder, request.path[1:])

    return app
