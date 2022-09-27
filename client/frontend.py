import sys
import os
import components

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from server import database
from server import routes

print(components.component)
print(database.database)
print(routes.routes)
