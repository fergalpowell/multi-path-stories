from flask import Flask
from flask import render_template, redirect, request

app = Flask(__name__)

story_dict = {
    "story1": {
        "sentence": "Once upon a time",
        "path_1": None,
        "path_2": None,
        "path_3": None,
        "path_4": None,
    }
}


def get_story_sentence(story_id):
    if story_id is not None:
        story = story_dict.get(story_id)
        return story['sentence']


def add_story(sentence):
    new_id = len(story_dict) + 1
    new_story_id = "story" + str(new_id)
    story_dict[new_story_id] = {
        "sentence": sentence,
        "path_1": None,
        "path_2": None,
        "path_3": None,
        "path_4": None,
    }
    return new_story_id


def update_story(current_story_id, new_story_id, path):
    cur_story = story_dict.get(current_story_id)
    cur_story["path_" + str(path)] = new_story_id


@app.route('/')
def index():
    return redirect("/story/story1")


@app.route('/story/<story_id>')
def display_story(story_id):
    story = story_dict.get(story_id)
    path_1_sentence = get_story_sentence(story['path_1'])
    path_2_sentence = get_story_sentence(story['path_2'])
    path_3_sentence = get_story_sentence(story['path_3'])
    path_4_sentence = get_story_sentence(story['path_4'])
    return render_template('index.html', sentence=story["sentence"], path1=story['path_1'],
                           path2=story['path_2'], path3=story['path_3'], path4=story['path_4'],
                           path1_sentence=path_1_sentence, path2_sentence=path_2_sentence,
                           path3_sentence=path_3_sentence, path4_sentence=path_4_sentence,
                           current_story_id=story_id, story=story)


@app.route('/create_story', methods=['POST'])
def create_story():
    new_story_id = add_story(request.form['sentence'])
    update_story(request.form['current_story_id'], new_story_id, request.form['path'])
    print(story_dict)
    return redirect('story/' + request.form['current_story_id'])


if __name__ == '__main__':
    app.run()
