# Import all the models, so that Base has them before being
# imported by Alembic
from apps.db.base_class import Base  # noqa
from apps.models.item import Item  # noqa
from apps.models.user import User  # noqa
