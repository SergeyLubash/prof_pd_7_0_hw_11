from flask import Flask, render_template, views
from utils import load_candidates, sort_by_id, sort_by_name, sort_by_skill

app = Flask(__name__)
candidates_list = load_candidates('candidates.json')


@app.route('/')
def listen():
    return render_template('list.html', user=candidates_list)


@app.route('/candidates/<int:candidate_id>')
def single(candidate_id):
    candidate_id = sort_by_id(candidate_id)
    return render_template('single.html', candidat=candidate_id)


@app.route('/search/<candidate_name>')
def search(candidate_name):
    candidates = sort_by_name(candidate_name)
    return render_template('search.html', candidates=candidates, candidates_len=len(candidates))


@app.route('/skills/<skill>')
def skills(skill):
    candidates = sort_by_skill(skill)
    return render_template('skill.html', candidates=candidates, candidates_len=len(candidates), skill=skill)


app.run()
