from flask import Blueprint, abort, render_template


static_view = Blueprint('static_view',
                        __name__,
                        url_prefix='',
                        template_folder='dist',
                        static_folder='dist/')


@static_view.route('/')
def index():
    return static_view.send_static_file('index.html')
