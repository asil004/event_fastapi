from starlette_admin.contrib.sqla import Admin, ModelView

from database import engine
from main import router
from models import Users, Events, Items, EventDetail, UsersEvents

# Create admin
admin = Admin(engine, title="Example: SQLAlchemy", base_url='/admin')

# Add view
admin.add_view(ModelView(Users))
admin.add_view(ModelView(Events))
admin.add_view(ModelView(Items))
admin.add_view(ModelView(EventDetail))
admin.add_view(ModelView(UsersEvents))

# Mount admin to your app
admin.mount_to(router)
