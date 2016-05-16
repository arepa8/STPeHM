import os
from flask import Flask, render_template, request, redirect
from app.models import db
from werkzeug.routing import Rule

# Flask application and config
app = Flask(__name__, static_url_path='')
app.secret_key = 'development key'
app.config.from_object('config')
db.init_app(app)


#Middleware to serve the static files
from werkzeug import SharedDataMiddleware
import os
app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {
  '/': os.path.join(os.path.dirname(__file__), 'templates', app.config['DEFAULT_TPL'])
})

from app import views