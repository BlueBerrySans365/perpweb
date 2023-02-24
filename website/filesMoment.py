from flask import Flask, redirect, url_for, send_file, render_template, send_from_directory, jsonify

def extendApplication(app):

    @app.route('/assets/<path:filename>')
    def websiteStaticAssetsHandler(filename):
        return send_from_directory('website/static', filename)


    # @app.route('/PERPUUE/<path:filename>')
    # def perpue(filename):
    #     if not discord.authorized:
    #         return redirect("/")
    #     guilds = discord.fetch_guilds()
    #     user = discord.fetch_user()
    #     guildsw = [g.id for g in guilds]
    #     if prepSrvID in guildsw:
    #         return send_from_directory('website/ProjectYEEEE', filename)
    #     else:
    #         return redirect("/")