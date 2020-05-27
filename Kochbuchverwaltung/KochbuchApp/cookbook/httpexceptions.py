
from starlette.applications import Starlette
from starlette.responses import HTMLResponse


HTML_400_PAGE = '<h1>400 BAD REQUEST'
HTML_401_PAGE = '<h1>401 UNAUTHORIZED'
HTML_402_PAGE = '<h1>402 PAYMENT REQUIRED</h1>'
HTML_403_PAGE = '<h1>403 FORBIDDEN</h2>'
HTML_404_PAGE = '<h1>404 NOT FOUND</h1>'
HTML_500_PAGE = '<h1>500 INTERNAL SERVER ERROR</h1>'


async def bad_request(request, exc):
    return HTMLResponse(content=HTML_400_PAGE, status_code=exc.status_code)

async def unauthorized(request, exc):
    return HTMLResponse(content=HTML_401_PAGE, status_code=exc.status_code)

async def payment_required(request, exc):
    return HTMLResponse(content=HTML_402_PAGE, status_code=exc.status_code)

async def forbidden(request, exc):
    return HTMLResponse(content=HTML_403_PAGE, status_code=exc.status_code)

async def not_found(request, exc):
    return HTMLResponse(content=HTML_404_PAGE, status_code=exc.status_code)

async def internal_server_error(request, exc):
    return HTMLResponse(content=HTML_500_PAGE, status_code=exc.status_code)


exception_handlers = {
    400: bad_request,
    401: unauthorized,
    402: payment_required,
    403: forbidden,
    404: not_found,
    500: internal_server_error
}
