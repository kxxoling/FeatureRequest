===============
Feature Request
===============

A sample app built with Vue.js and Flask with a lot of plugins
to satisfy the demand of `IntuitiveWebSolutions/EngineeringMidLevel <https://github.com/IntuitiveWebSolutions/EngineeringMidLevel>`__.


Installation
============

Assume you already have node.js, npm, python and pip installed.

Install frontend app requirements::

    npm install

Install backend app requirements::

    pip install -r requirements/dev.pip


Start a dev server
==================

Start node server::

    npm run dev

Start Flask app::

    python manage.py runserver

Then open `127.0.0.1:8080 <http://127.0.0.1:8080/>`__ in your browser.

Otherwise you could run `npm run build` to compile the frontend to statics
and start the Flask app alone. Then you can open `127.0.0.1:5000 <http://127.0.0.1:5000/>`__
in browser.
