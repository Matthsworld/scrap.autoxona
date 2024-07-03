from flask import render_template, redirect, url_for, flash, request
from app import app, db
from app.forms import InstantQuoteForm, BookingForm, ListingForm, LoginForm, SignupForm
from app.models import Appointment, Listing, Quote, User
from flask_login import login_user, current_user, logout_user, login_required
from flask import render_template, redirect, url_for, flash, request

@app.route('/')
def home():
    form = InstantQuoteForm()
    return render_template('home.html', form=form)

@app.route('/list-scrap', methods=['GET', 'POST'])
@login_required
def list_scrap():
    form = ListingForm()
    if form.validate_on_submit():
        listing = Listing(
            user_id=current_user.id,
            owner_name=form.owner_name.data,
            gender=form.gender.data,
            email=form.email.data,
            phone=form.phone.data,
            home_address=form.home_address.data,
            vehicle_registration=form.vehicle_registration.data,
            make=form.make.data,
            model=form.model.data,
            year=form.year.data
        )
        db.session.add(listing)
        db.session.commit()
        flash('Your scrap has been listed!', 'success')
        return redirect(url_for('home'))
    return render_template('list_scrap.html', form=form)

@app.route('/book-appointment', methods=['GET', 'POST'])
@login_required
def book_appointment():
    form = BookingForm()
    if form.validate_on_submit():
        # Handle photo uploads
        photos = []
        for photo in form.photos.data:
            photo_filename = secure_filename(photo.filename)
            photo.save(os.path.join(app.config['UPLOAD_FOLDER'], photo_filename))
            photos.append(photo_filename)
        appointment = Appointment(
            user_id=current_user.id,
            name=form.name.data,
            email=form.email.data,
            gender=form.gender.data,
            home_address=form.home_address.data,
            phone=form.phone.data,
            make=form.make.data,
            model=form.model.data,
            year=form.year.data,
            registration_number=form.registration_number.data,
            photos=','.join(photos)
        )
        db.session.add(appointment)
        db.session.commit()
        flash('Your appointment has been booked!', 'success')
        return redirect(url_for('home'))
    return render_template('book_appointment.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid email or password', 'danger')
            return redirect(url_for('login'))
        login_user(user)
        return redirect(url_for('home'))
    return render_template('login.html', form=form)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = SignupForm()
    if form.validate_on_submit():
        user = User(email=form.email.data, role='user')
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('You are now registered!', 'success')
        return redirect(url_for('login'))
    return render_template('signup.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@login_required
@app.route('/appointments')
def appointments():
    if current_user.role == 'admin':
        appointments = Appointment.query.all()
    else:
        appointments = Appointment.query.filter_by(user_id=current_user.id).all()
    return render_template('appointments.html', appointments=appointments)

@login_required
@app.route('/delete-appointment/<int:id>')
def delete_appointment(id):
    appointment = Appointment.query.get_or_404(id)
    if current_user.role == 'admin' or appointment.user_id == current_user.id:
        db.session.delete(appointment)
        db.session.commit()
        flash('Appointment deleted!', 'success')
    else:
        flash('You do not have permission to delete this appointment.', 'danger')
    return redirect(url_for('appointments'))

@login_required
@app.route('/delete-listing/<int:id>')
def delete_listing(id):
    listing = Listing.query.get_or_404(id)
    if current_user.role == 'admin' or listing.user_id == current_user.id:
        db.session.delete(listing)
        db.session.commit()
        flash('Listing deleted!', 'success')
    else:
        flash('You do not have permission to delete this listing.', 'danger')
    return redirect(url_for('listings'))

@login_required
@app.route('/mark-attended/<int:id>')
def mark_attended(id):
    appointment = Appointment.query.get_or_404(id)
    if current_user.role == 'admin':
        appointment.attended = not appointment.attended
        db.session.commit()
        flash('Appointment attendance status updated!', 'success')
    else:
        flash('You do not have permission to mark this appointment.', 'danger')
    return redirect(url_for('appointments'))

@app.route('/submit-quote', methods=['POST'])
def submit_quote():
    form = InstantQuoteForm()
    if form.validate_on_submit():
        quote = Quote(
            owner_name=form.owner_name.data,
            gender=form.gender.data,
            email=form.email.data,
            phone=form.phone.data,
            home_address=form.home_address.data,
            vehicle_registration=form.vehicle_registration.data,
            make=form.make.data,
            model=form.model.data,
            year=form.year.data
        )
        db.session.add(quote)
        db.session.commit()
        flash('Your quote request has been submitted!', 'success')
        return redirect(url_for('home'))
    return render_template('home.html', form=form)

@login_required
@app.route('/quotes')
def view_quotes():
    if current_user.role != 'admin':
        flash('You do not have permission to view this page.', 'danger')
        return redirect(url_for('home'))
    quotes = Quote.query.all()
    return render_template('view_quotes.html', quotes=quotes)

@login_required
@app.route('/respond-quote/<int:id>', methods=['GET', 'POST'])
def respond_quote(id):
    if current_user.role != 'admin':
        flash('You do not have permission to view this page.', 'danger')
        return redirect(url_for('home'))
    quote = Quote.query.get_or_404(id)
    if request.method == 'POST':
        response = request.form['response']
        quote.response = response
        db.session.commit()
        flash('Quote response has been sent!', 'success')
        return redirect(url_for('view_quotes'))
    return render_template('respond_quote.html', quote=quote)

