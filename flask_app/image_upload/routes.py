import os
from flask import request, send_from_directory, render_template, current_app, abort, flash, redirect, url_for
from flask_login import login_required
from flask_app.image_upload import bp
from flask_app.image_upload.forms import EmptyForm
from flask_app.image_upload.utils import upload_file, list_upload_files, get_directory_and_filename, delete_file, \
    validate_image
from werkzeug.utils import secure_filename


@bp.route('/upload-photo', methods=['POST'])
@login_required
def upload_blog_photo():
    """
    Upload Blog Photo
    """
    for image_file in request.files.getlist('file'):
        filename = secure_filename(image_file.filename)
        if filename != '':
            file_ext = os.path.splitext(filename)[1]
            if (file_ext.lower() not in current_app.config['UPLOAD_EXTENSIONS'] or
                    file_ext.lower() != validate_image(image_file.stream).lower()):
                abort(400)
            upload_file(image_file, filename)
    flash('Your image(s) were uploaded successfully')
    return redirect(request.referrer)


@bp.route("/download-photo/<display_filename>", methods=['GET'])
@login_required
def download_photo(display_filename):
    directory, filename = get_directory_and_filename(display_filename)
    return send_from_directory(directory, filename, as_attachment=True)


@bp.route("/photos/<display_filename>", methods=['GET'])
def get_photo(display_filename):
    directory, filename = get_directory_and_filename(display_filename)
    return send_from_directory(directory, filename)


@bp.route("/delete-photo/<display_filename>", methods=['POST'])
@login_required
def delete_photo(display_filename):
    form = EmptyForm()
    if form.validate_on_submit():
        try:
            delete_file(display_filename)
            flash('The image(s) was successfully deleted')
        except FileNotFoundError:
            flash('The image(s) could not be found')
        return redirect(request.referrer)
    else:
        return redirect(url_for('index'))


@bp.route("/images")
@login_required
def images():
    form = EmptyForm()
    contents = list_upload_files()
    return render_template('image_upload/image_storage.html', contents=contents, form=form)
