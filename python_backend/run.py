from app import create_app


app = create_app()


if app.config.DEBUG:
    app.logger.info('DEBUG       = ' + str(app.config.DEBUG))
    app.logger.info('Environment = ' + app.config.ENV)
    app.logger.info('DBMS        = ' + app.config.SQLALCHEMY_DATABASE_URI)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
