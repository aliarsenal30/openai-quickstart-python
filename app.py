import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        user = request.form["user"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(user),
            temperature=0.75,
            max_tokens = 4000,
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(user):
    return """Write an essay with paragraphs about {}
Names:""".format(
        user.capitalize()
    )
#new change