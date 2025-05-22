from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models.auth import login_required
from app.models.courses import get_all_courses, get_course_by_id, add_new_course, update_course, delete_course
from app.models.testimonials import get_all_testimonials, get_testimonial_by_id, add_new_testimonial, update_testimonial, delete_testimonial
from app.models.contacts import get_lead_sources, get_lead_details

bp = Blueprint('admin', __name__, url_prefix='/admin')

@bp.route('/')
@login_required
def dashboard():
    return render_template('admin/dashboard.html')

# Rotas para cursos
@bp.route('/cursos')
@login_required
def courses():
    courses = get_all_courses()
    return render_template('admin/courses.html', courses=courses)

@bp.route('/cursos/novo', methods=['GET', 'POST'])
@login_required
def add_course():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        image = request.form['image']
        link = request.form['link']
        
        add_new_course(title, description, image, link)
        
        flash('Curso adicionado com sucesso!', 'success')
        return redirect(url_for('admin.courses'))
        
    return render_template('admin/course_form.html')

@bp.route('/cursos/editar/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_course(id):
    course = get_course_by_id(id)
    
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        image = request.form['image']
        link = request.form['link']
        
        update_course(id, title, description, image, link)
        
        flash('Curso atualizado com sucesso!', 'success')
        return redirect(url_for('admin.courses'))
        
    return render_template('admin/course_form.html', course=course)

@bp.route('/cursos/excluir/<int:id>')
@login_required
def delete_course_route(id):
    delete_course(id)
    
    flash('Curso excluído com sucesso!', 'success')
    return redirect(url_for('admin.courses'))

# Rotas para depoimentos
@bp.route('/depoimentos')
@login_required
def testimonials():
    testimonials = get_all_testimonials()
    return render_template('admin/testimonials.html', testimonials=testimonials)

@bp.route('/depoimentos/novo', methods=['GET', 'POST'])
@login_required
def add_testimonial():
    if request.method == 'POST':
        name = request.form['name']
        text = request.form['text']
        
        add_new_testimonial(name, text)
        
        flash('Depoimento adicionado com sucesso!', 'success')
        return redirect(url_for('admin.testimonials'))
        
    return render_template('admin/testimonial_form.html')

@bp.route('/depoimentos/editar/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_testimonial(id):
    testimonial = get_testimonial_by_id(id)
    
    if request.method == 'POST':
        name = request.form['name']
        text = request.form['text']
        
        update_testimonial(id, name, text)
        
        flash('Depoimento atualizado com sucesso!', 'success')
        return redirect(url_for('admin.testimonials'))
        
    return render_template('admin/testimonial_form.html', testimonial=testimonial)

@bp.route('/depoimentos/excluir/<int:id>')
@login_required
def delete_testimonial_route(id):
    delete_testimonial(id)
    
    flash('Depoimento excluído com sucesso!', 'success')
    return redirect(url_for('admin.testimonials'))

# Rotas para relatórios
@bp.route('/reports')
@login_required
def reports():
    sources = get_lead_sources()
    leads = get_lead_details()
    
    return render_template('admin/reports.html', sources=sources, leads=leads) 