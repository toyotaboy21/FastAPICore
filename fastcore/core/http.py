from fastapi import Request, FastAPI
from fastapi.responses import JSONResponse
from fastcore.core.response import JSONBuildResponse

class FastCoreExceptionHandlers:
    """
    Пример использования

    ```py
    from fastapi import FastAPI
    from fastcore.http import FastCoreExceptionHandlers

    api = FastAPI(
        title='By Reques6e',
        version='0.1.0',
        redoc_url=None,
        description='Example code'
    )

    FastCoreExceptionHandlers(api)

    ```
    """

    def __init__(self, app: FastAPI):
        self.app = app
        self.register_handlers()

    def register_handlers(self):
        @self.app.exception_handler(404)
        async def custom_404_handler(request: Request, exc):
            return JSONResponse(
                content=JSONBuildResponse(
                    error=1,
                    message="Страница не найдена"
                ).json()
            )

        @self.app.exception_handler(403)
        async def custom_403_handler(request: Request, exc):
            return JSONResponse(
                content=JSONBuildResponse(
                    error=1,
                    message="У вас нет доступа к этой странице"
                ).json()
            )
        
        @self.app.exception_handler(401)
        async def custom_401_handler(request: Request, exc):
            return JSONResponse(
                content=JSONBuildResponse(
                    error=1,
                    message="Требуется авторизация"
                ).json()
            )

        @self.app.exception_handler(500)
        async def custom_500_handler(request: Request, exc):
            return JSONResponse(
                content=JSONBuildResponse(
                    error=1,
                    message="На сервере произошла ошибка"
                ).json()
            )