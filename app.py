import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
from config import open_api_key
openai.api_key = open_api_key


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        prompt = request.form["question"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=0.9,
            max_tokens=150,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.6,
            stop=[" Human:", " AI:"]
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)