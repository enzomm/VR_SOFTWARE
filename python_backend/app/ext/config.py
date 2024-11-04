from dynaconf import FlaskDynaconf


def load_extensions(app):
    app.config.load_extensions("EXTENSIONS")


def init_app(app):
    FlaskDynaconf(app, envvar_prefix="VR_SOFTWARE", settings_files=["settings.toml", ".secrets.toml"])
