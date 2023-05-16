import os
import sys
from dotenv import load_dotenv
load_dotenv()

path = os.environ["FILE_PATH"]
sys.path.append(path)

from app.api.controller.BookController import bookroutes

def setup_routes(app):
    app.add_routes(bookroutes)

