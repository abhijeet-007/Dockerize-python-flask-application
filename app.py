from flask import Flask, jsonify, request, render_template, redirect, url_for, flash
from datetime import date

app = Flask(__name__)
app.secret_key = 'flask-docker-secret'

todos = {}
next_id = 1

posts = {}
next_post_id = 1

# ── Todos UI ───────────────────────────────────────────────

@app.route('/todos')
def todos_page():
    return render_template('todos.html', todos=list(todos.values()))

@app.route('/todos/new', methods=['POST'])
def add_todo():
    global next_id
    title = request.form.get('title', '').strip()
    if not title:
        flash('Title is required.', 'error')
        return redirect(url_for('todos_page'))
    todos[next_id] = {'id': next_id, 'title': title, 'done': False}
    next_id += 1
    flash('Todo added!')
    return redirect(url_for('todos_page'))

@app.route('/todos/<int:todo_id>/delete', methods=['POST'])
def delete_todo(todo_id):
    todos.pop(todo_id, None)
    flash('Todo deleted.')
    return redirect(url_for('todos_page'))

# ── Todos JSON API ─────────────────────────────────────────

@app.route('/api/todos', methods=['GET'])
def get_todos():
    return jsonify(list(todos.values()))

@app.route('/api/todos', methods=['POST'])
def create_todo():
    global next_id
    data = request.get_json()
    if not data or 'title' not in data:
        return jsonify({'error': 'title is required'}), 400
    todo = {'id': next_id, 'title': data['title'], 'done': False}
    todos[next_id] = todo
    next_id += 1
    return jsonify(todo), 201

@app.route('/api/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    if todo_id not in todos:
        return jsonify({'error': 'not found'}), 404
    data = request.get_json()
    if 'title' in data:
        todos[todo_id]['title'] = data['title']
    if 'done' in data:
        todos[todo_id]['done'] = data['done']
    return jsonify(todos[todo_id])

# ── Blog ───────────────────────────────────────────────────

@app.route('/blog')
def blog_page():
    return render_template('blog.html', posts=list(posts.values()))

@app.route('/blog', methods=['POST'])
def create_post():
    global next_post_id
    title = request.form.get('title', '').strip()
    body = request.form.get('body', '').strip()
    if not title or not body:
        flash('Title and body are required.', 'error')
        return redirect(url_for('blog_page'))
    posts[next_post_id] = {'id': next_post_id, 'title': title, 'body': body, 'date': str(date.today())}
    next_post_id += 1
    flash('Post published!')
    return redirect(url_for('blog_page'))

@app.route('/blog/<int:post_id>')
def view_post(post_id):
    if post_id not in posts:
        flash('Post not found.', 'error')
        return redirect(url_for('blog_page'))
    return render_template('post.html', post=posts[post_id])

# ── Home ───────────────────────────────────────────────────

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
