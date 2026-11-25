# Raptor public preview

A work-in-progress Telegram freelance marketplace side project.

Raptor is a Telegram Mini App for clients to find freelancers, discuss work, and agree on project terms. The project is in development and has not launched publicly.

This repository contains selected parts of the codebase: catalog and portfolio templates, a profile form template, interface styles, Telegram theme handling, a skill catalog, and display-name helpers.

The main project uses Python 3.12, Django 5.2, Django REST Framework, Django Channels, HTML templates, JavaScript, CSS, and the Telegram WebApp SDK. Its production configuration targets PostgreSQL and Redis.

The base templates here are presentation-only replacements. Styles are extracted from the original templates. Application routes, models, authentication, payment processing, transaction verification, workers, and deployment configuration are omitted. Template links and forms require the omitted application; this is not a complete runnable app.

`requirements.txt` lists the dependency needed by the published Python helpers and templates, not the dependencies of the full project.
