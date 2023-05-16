from aiohttp.web import RouteTableDef, json_response, Response
from app.business.service.book.BookService import BookService

bookroutes = RouteTableDef()

@bookroutes.get('/book/catalogs')
async def get_all_available_books_catalog(request):
    pass

@bookroutes.get('/book/catalogs/{id}')
async def get_catalogs_books_by_id(request):
    pass

