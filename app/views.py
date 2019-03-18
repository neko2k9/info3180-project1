"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app, db
import os, datetime
from flask import render_template, request, redirect, url_for, flash, session, abort, send_from_directory
from werkzeug.utils import secure_filename
from app.forms import ProfileForm
from app.models import UserProfile


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')

@app.route("/profile",methods=["GET","POST"])
def profile():
    form=ProfileForm()
    if request.method=="POST" and form.validate_on_submit():
        firstname=form.firstname.data
        lastname=form.lastname.data
        gender=form.gender.data
        email=form.email.data
        location=form.location.data
        biography=form.bio.data
        print (biography)
        now=str(datetime.date.today())
        
        image=request.files['photo']
        if allowed_file(image.filename):
            filename=secure_filename(image.filename)
            image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        else:
            flash('Incorrect File Format','danger')
            return redirect(url_for('profile'))
        
        user=UserProfile(firstname,lastname,gender,email,location,biography,filename,now)
        db.session.add(user)
        db.session.commit()
        flash('File Saved','success')
        return redirect(url_for('profiles'))
    return render_template("profile.html", form=form)
    
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_UPLOADS']


def get_uploaded_images():
    rootdir = os.getcwd()
    print (rootdir)
    img = []
    for subdir, dirs, files in os.walk(rootdir + '/app/static/uploads'):
        for file in files:
            img.append(os.path.join(subdir, file).split('/')[-1])
    return img

@app.route('/profiles/')
def profiles():
    imagenames = get_uploaded_images()
    users = UserProfile.query.all()
    return render_template("profiles.html", users=users, imagenames=imagenames)


@app.route("/profiles/<id>")
def user_profile(id):
    user = UserProfile.query.filter_by(id=id).first()
    imagenames= get_uploaded_images()
    return render_template('viewprofile.html', user=user, imagenames=imagenames)

###
# The functions below should be applicable to all Flask apps.
###


@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
