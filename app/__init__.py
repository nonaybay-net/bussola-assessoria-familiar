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
        return render_template('views/pages/home.html')

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

        return render_template('views/pages/gallery.html', context=context)

    @app.route('/about')
    def app_route_about():
        return render_template('views/pages/home.html')

    @app.route('/contact')
    def app_route_contact():
        return render_template('views/pages/home.html')

    # errors

    # redirects

    return app
