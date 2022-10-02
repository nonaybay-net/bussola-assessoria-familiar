import os
from app.debug_log import log_msg
from flask import Flask, render_template, request, send_from_directory
from flask_minify import Minify
from random import shuffle

from app.utilities import create_hash_w_time, jinja_escape_hash, jinja_random_list
from .values import context
from hashlib import md5


os.system('clear')
log_msg('hashing static url')
static_url_path = '/{}'.format(create_hash_w_time('static'))


log_msg('init of create_app function')
def create_app(tc=None):
    log_msg('creating the instance of app')
    app = Flask(__name__, instance_relative_config=True, static_url_path=static_url_path)
    log_msg('telling to flask to minify')
    Minify(app=app)
    log_msg('removing whitespaces on jinja')
    app.jinja_env.trim_blocks = True
    app.jinja_env.lstrip_blocks = True

    log_msg('checking config')
    if tc is None:
        log_msg('test_config is None')
        app.config.from_pyfile('config.py', silent=True)
    else:
        log_msg('test_config is something')
        app.config.from_mapping(tc)

    try:
        log_msg('trying to create the instance path')
        os.makedirs(app.instance_path)
    except OSError:
        log_msg('instance path created')
        pass

    log_msg('creating jinja filters')
    # jinja-filters
    @app.template_filter('random_list')
    def filter_random_list(sequence, repeats=1):
        return jinja_random_list(sequence, repeats)


    @app.template_filter('escape_hash')
    def filter_escape_hash(shift):
        return jinja_escape_hash(shift)

    # end of jinja-filters


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

    @app.template_filter('ha')
    def filter_ha(entry):
        a = entry
        a = str(a)
        a = md5(a.encode()).hexdigest()

        return a

    log_msg('jinja filters has been created')

    # routes and pages
    log_msg('ROUTES AND PAGES')
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

    @app.route('/gallery/ibiuna')
    def app_route_gallery_p1():
        image = []
        for val in context['pics']['ibiuna']:
            image.append(val)

        context['title'] = 'Ibiúna | Galeria'
        context['imgs'] = image
        context['u'] = 'ibiuna'

        return render_template('views/pages/gallery.show.html', context=context)

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
    @app.errorhandler(404)
    def app_route_error_404(error):
        context['title'] = 'Página não encontrada'
        return render_template('404.html', context=context)

    # routes from static
    @app.route('/sitemap.xml')
    def serving_static():
        return send_from_directory(app.static_folder, request.path[1:])

    return app
