import os
import random
import json
from flask import Flask, redirect, url_for, send_file, render_template, send_from_directory, jsonify
from markupsafe import escape

import website.errorPage as errorPage
import website.filesMoment as filesmoment

app = Flask(__name__)

HYPERLINK = '<a href="{}">{}</a>'

data = open(f"{os.getcwd()}/website/static/arts.json")
arts = json.load(data)

# Some fixes will be here
def deskFIXED(texr):
    if "\n" in texr:
        texr = texr.replace("\n",'<br>')
    elif "<br>" in texr:
        texr = texr.replace("<br>","<br>")
    elif '"' in texr:
        texr = texr.replace('"',"")
    return texr

imgExt = [
    "gif",
    "png",
    "apng",
    "jpg",
    "jpeg"
]

def ranLow():
    listssss = [
        f"Only {len(arts.keys())} media was added.",
        "You can click on content to see full size image/video"
    ]
    thicc = random.choice(listssss)
    return thicc

def ranImg(): 
    random_key = random.choice(list(arts.keys()))
    random_data = arts[random_key]
    results = dict();
    results['url'] = random_key
    results['width'] = random_data['width']
    results['height'] = random_data['height']
    results['author'] = random_data['author']
    if random_data['desc'] == "None":
        results['desc'] = f"Content made by {results['author']}"
        results['author'] = ""
    else:
        results['desc'] = random_data['desc']
    file_extension = os.path.splitext(random_key)[1]
    file_extension = file_extension[1:]
    results['type'] = file_extension
    return results

@app.route('/')
def index():
    fuck = ranImg()
    print(fuck['type'])
    fileFormat = None
    if fuck['type'] in imgExt:
        return render_template('index.html',  
        fanartDesc=deskFIXED(fuck['desc']), 
        fanartAuthor= fuck['author'],
        fanartURL=f"{fuck['url']}", 
        fanartWidth = fuck['width'] / 2,
        fanartHeight = fuck['height'] / 2,
        counter = ranLow())
    elif "mov" or "MOV" or "mp4" in fuck['type']:
        # match fuck['type']: #vercel don't support 3.10 yet
        #     case "mov":
        #         fileFormat = "mov"
        #     case "mp4":
        #         fileFormat = "mp4"
        #     case "MOV":
        #         fileFormat = "MOV"
        if fuck['type'] == "mov":
            fileFormat = "mov"
        elif fuck['type'] == "mp4":
            fileFormat = "mp4"
        else:
            pass
        return render_template('indexvideos.html',  
        fanartDesc=deskFIXED(fuck['desc']), 
        fanartAuthor= fuck['author'],
        fanartURL=f"{fuck['url']}", 
        fanartWidth = fuck['width'] / 1.5,
        fanartHeight = fuck['height'] / 1.5,
        fileFormat = fileFormat,
        counter = len(arts.keys()))
    else:
        return 404


errorPage.extendApplication(app)
filesmoment.extendApplication(app)

if __name__ == "__main__":
    app.run(port=25190)