from flask import Flask, render_template, request, redirect, session
import pymysql
import os

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "taskmanager123")

# ---------------- DATABASE CONNECTION ----------------
def get_db_connection():
    return pymysql.connect(
        host=os.environ.get("MYSQLHOST"),
        user=os.environ.get("MYSQLUSER"),
        password=os.environ.get("MYSQLPASSWORD"),
        database=os.environ.get("MYSQLDATABASE"),
        port=int(os.environ.get("MYSQLPORT")),
        cursorclass=pymysql.cursors.DictCursor
    )

# ---------------- HOME ----------------
@app.route('/')
def home():
    return redirect('/login')

# ---------------- REGISTER ----------------
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        db = get_db_connection()
        cur = db.cursor()

        cur.execute("""
            INSERT INTO users(name,email,password,role)
            VALUES(%s,%s,%s,%s)
        """, (name, email, password, "member"))

        db.commit()
        db.close()

        return redirect('/login')

    return render_template('register.html')

# ---------------- LOGIN ----------------
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        db = get_db_connection()
        cur = db.cursor()

        cur.execute("""
            SELECT * FROM users
            WHERE email=%s AND password=%s
        """, (email, password))

        user = cur.fetchone()
        db.close()

        if user:
            session['user_id'] = user['id']
            session['name'] = user['name']
            return redirect('/dashboard')

        return "❌ Invalid Login"

    return render_template('login.html')

# ---------------- DASHBOARD ----------------
@app.route('/dashboard')
def dashboard():

    if 'user_id' not in session:
        return redirect('/login')

    db = get_db_connection()
    cur = db.cursor()

    cur.execute("""
        SELECT * FROM tasks
        WHERE user_id=%s
    """, (session['user_id'],))

    tasks = cur.fetchall()

    db.close()

    return render_template(
        'dashboard.html',
        tasks=tasks,
        name=session['name']
    )

# ---------------- ADD TASK ----------------
@app.route('/add_task', methods=['POST'])
def add_task():

    title = request.form['title']

    db = get_db_connection()
    cur = db.cursor()

    cur.execute("""
        INSERT INTO tasks(title,status,user_id)
        VALUES(%s,%s,%s)
    """, (title, "Pending", session['user_id']))

    db.commit()
    db.close()

    return redirect('/dashboard')

# ---------------- COMPLETE TASK ----------------
@app.route('/complete_task/<int:id>')
def complete_task(id):

    db = get_db_connection()
    cur = db.cursor()

    cur.execute("""
        UPDATE tasks
        SET status='Completed'
        WHERE id=%s
    """, (id,))

    db.commit()
    db.close()

    return redirect('/dashboard')

# ---------------- DELETE TASK ----------------
@app.route('/delete_task/<int:id>')
def delete_task(id):

    db = get_db_connection()
    cur = db.cursor()

    cur.execute("""
        DELETE FROM tasks
        WHERE id=%s
    """, (id,))

    db.commit()
    db.close()

    return redirect('/dashboard')

# ---------------- LOGOUT ----------------
@app.route('/logout')
def logout():

    session.clear()

    return redirect('/login')

# ---------------- RUN ----------------
if __name__ == "__main__":
    app.run()