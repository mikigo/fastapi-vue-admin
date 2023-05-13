# Import all the models, so that Base has them before being
# imported by Alembic
from fadmin.db.base_class import Base  # noqa
from fadmin.models.item import Item  # noqa
from fadmin.models.user import User  # noqa
