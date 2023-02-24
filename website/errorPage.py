from flask import Flask, redirect, url_for, send_file, render_template, send_from_directory, jsonify

def extendApplication(app):

    @app.errorhandler(404)
    def page_not_found(e):
        return """
        <html>
        <head>
        <title>404 error page</title>
        </head>
        <body>
        <h1 align="center"> 404 error </h1>
        </body>
        </html>
        """, 404

    @app.errorhandler(500)
    def page_fucked(e):
        return render_template("500.html", fuckedError=f"{e}")