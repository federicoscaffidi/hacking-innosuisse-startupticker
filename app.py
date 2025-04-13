from flask import Flask, render_template, request, jsonify
from model_backend2 import run_model

app = Flask(__name__)

# 🔁 Memoria temporanea
history_list = []
current_index = -1

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    global history_list, current_index
    query = request.form.get('query')
    analysis = run_model(query)

    item = {
        "query": query,
        "analysis": analysis
    }

    history_list.append(item)
    current_index = len(history_list) - 1

    return jsonify({
        **item,
        "has_prev": current_index > 0,
        "has_next": False
    })

@app.route('/history/prev')
def prev():
    global current_index, history_list
    if current_index > 0:
        current_index -= 1

    item = history_list[current_index] if history_list else {}
    return jsonify({
        **item,
        "has_prev": current_index > 0,
        "has_next": current_index < len(history_list) - 1
    })

@app.route('/history/next')
def next():
    global current_index, history_list
    if current_index < len(history_list) - 1:
        current_index += 1

    item = history_list[current_index] if history_list else {}
    return jsonify({
        **item,
        "has_prev": current_index > 0,
        "has_next": current_index < len(history_list) - 1
    })

if __name__ == '__main__':
    app.run(debug=True)