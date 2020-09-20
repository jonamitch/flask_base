from datetime import datetime
from .home import *
from .users import *
from .edit_profile import *


@bp.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()
