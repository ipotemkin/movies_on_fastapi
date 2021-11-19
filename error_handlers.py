from errors import NoContentError, NotFoundError, DatabaseError, BadRequestError


def reg_error_handlers(app):

    @app.errorhandler(404)
    @app.errorhandler(NotFoundError)
    def not_found_error(error):
        return "Not Found", 404

    @app.errorhandler(NoContentError)
    def no_content_error(error):
        return "No Content", 204

    @app.errorhandler(DatabaseError)
    def no_content_error(error):
        return "Database Error", 400

    @app.errorhandler(BadRequestError)
    def no_content_error(error):
        return "Bad Request", 400
