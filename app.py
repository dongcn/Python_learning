from flask import Flask, render_template, abort

app = Flask(__name__)

# ---------- 模拟数据库的数据（写死在内存里） ----------
posts_data = [
    {"id": 1, "title": "Flask 入门踩坑记", "content": "今天终于把 Flask 跑起来了，缩进太重要了！"},
    {"id": 2, "title": "部署到 PythonAnywhere", "content": "只要改对 WSGI 路径，其实很简单。"},
    {"id": 3, "title": "为什么要写个人博客", "content": "为了沉淀知识，打造自己的技术名片。"}
]

# ---------- 路由（页面地址） ----------

@app.route('/')
def index():
    # 把文章列表传给主页模板
    return render_template('index.html', posts=posts_data)

@app.route('/about')
def about():
    # 关于页面很简单，不需要传数据
    return render_template('about.html')

@app.route('/post/<int:post_id>')
def post(post_id):
    # 根据 id 查找文章
    # 使用生成器表达式查找，找不到返回 None
    p = next((p for p in posts_data if p['id'] == post_id), None)
    if p is None:
        # 如果用户输入了不存在的 id（比如 /post/999），返回 404 页面
        abort(404)
    return render_template('post.html', post=p)

# ---------- 启动 ----------
if __name__ == '__main__':
    app.run(debug=True)