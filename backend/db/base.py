# Import all the models, so that Base has them before being
# imported by Alembic
from backend.db.base_class import Base  # noqa
from backend.models.item import Item  # noqa
from backend.models.user import User  # noqa
