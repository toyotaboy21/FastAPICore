# JWT 
#
# Труебуется для шифрования/дешифрования str. 
#
#
# Reques6e 2024


import jwt


class JWT:
    def __init__(self, secret: str) -> None:
        self.secret = secret

    async def crypted(self, payload: dict, algorithm: str) -> str:
        """
        Пример использования
        
        import asyncio
        from fastcore.core.jwts import JWT

        jwt = JWT(secret='test')

        async def main():
            await jwt.crypted({'test': 'test'}, algorithm='HS256'
        """

        return jwt.encode(payload=payload, key=self.secret, algorithm=algorithm)

    async def encrypted(self) -> None:
        pass

if __name__ == '__main__':
    import asyncio
    jwt_instance = JWT(secret='test')

    result = asyncio.run(jwt_instance.crypted({'test': 'test'}, algorithm='HS256'))
    print(result)
