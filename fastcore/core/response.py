from fastapi.responses import JSONResponse


class JSONBuildResponse:

    """
   
    Выдаёт Уже готовый json
   
    ---

    Разберём пример использования.
    ```py

    @app.get('/')
    async def info():
        return JSONBuildResponse(
            error=0,
            message=f'Информация'
        )
    ```

    В этом случае, error, это статус код задачи, 0 всё окей, ошибок в процессе выполнения задачи небыло, 1, ошибка процессе выполнения задачи.
   
    """

    def __init__(
        self, 
        error: int = 0, 
        message: str = 'Успех!', 
        **kwargs
    ) -> None:
        self.error = error
        self.message = message
        self.data = kwargs

    def json(
        self
    ):
        return JSONResponse(
            content={
                "error": self.error,
                "message": self.message,
                "data": self.data
            }
        )