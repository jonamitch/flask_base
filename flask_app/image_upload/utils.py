import os
import imghdr
from flask import current_app


def upload_file(file, filename):
    file_location = os.path.join(current_app.root_path,
                                 current_app.config['STATIC_UPLOAD_FOLDER'],
                                 filename)
    file.save(file_location)
    return


def delete_file(display_filename):
    directory, filename = get_directory_and_filename(display_filename)
    file_location = os.path.join(current_app.root_path,
                             current_app.config['STATIC_UPLOAD_FOLDER'],
                             filename)
    if os.path.exists(file_location):
        os.remove(file_location)
        return
    raise FileNotFoundError


def get_directory_and_filename(display_filename):
    return current_app.config['STATIC_UPLOAD_FOLDER'], display_filename


def list_upload_files():
    directory = os.path.join(current_app.root_path, current_app.config['STATIC_UPLOAD_FOLDER'])
    return os.listdir(directory)


def validate_image(stream):
    header = stream.read(512)
    stream.seek(0)
    format = imghdr.what(None, header)
    if not format:
        return None
    return '.' + (format if format != 'jpeg' else 'jpg')

