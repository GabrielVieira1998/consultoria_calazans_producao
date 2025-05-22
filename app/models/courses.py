from app.models.database import get_db

def get_all_courses():
    conn = get_db()
    courses = conn.execute('SELECT * FROM courses').fetchall()
    return courses

def get_course_by_id(id):
    conn = get_db()
    course = conn.execute('SELECT * FROM courses WHERE id = ?', (id,)).fetchone()
    return course

def add_new_course(title, description, image, link):
    conn = get_db()
    conn.execute(
        'INSERT INTO courses (title, description, image, link) VALUES (?, ?, ?, ?)',
        (title, description, image, link)
    )
    conn.commit()
    
def update_course(id, title, description, image, link):
    conn = get_db()
    conn.execute(
        'UPDATE courses SET title = ?, description = ?, image = ?, link = ? WHERE id = ?',
        (title, description, image, link, id)
    )
    conn.commit()
    
def delete_course(id):
    conn = get_db()
    conn.execute('DELETE FROM courses WHERE id = ?', (id,))
    conn.commit() 