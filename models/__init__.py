"""
Initialices the package
"""
from os import getenv

stora_type = getenv("HOME_TYPE_STORAGE")

if stora_type == "db":
    from models.engine.dbStorage import DbStorage
    storage = DbStorage()
else:
    from models.engine.jStorage import JStorage
    storage = JStorage()

storage.reload()
