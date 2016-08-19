
from flask import Blueprint, render_template

error_handler = Blueprint('error_handler', __name__)


@error_handler.app_errorhandler(404)
def handle_404(error):
    return render_template('errors/404.html'), 404


@error_handler.app_errorhandler(500)
def handle_500(error):
    return render_template('errors/500.html')
