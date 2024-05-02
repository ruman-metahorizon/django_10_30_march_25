## Create a superuser
`
python manage.py createsuperuser
`

### Add following code to boards/admin.py
`
from .models import Board

admin.site.register(Board)
`

Created a new board through /admin pannel in browser.