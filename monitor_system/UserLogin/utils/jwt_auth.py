"""
生成jwt token
"""
import jwt
import datetime
from django.conf import settings
from rest_framework.authentication import BaseAuthentication
from jwt import exceptions
from rest_framework.exceptions import AuthenticationFailed
from loguru import logger


def create_token(payload,timeout=60*60*24):
    salt = settings.SECRET_KEY

    headers = {
        'typ': 'jwt',
        'alg': 'HS256'
    }

    payload["exp"] = datetime.datetime.utcnow() + datetime.timedelta(minutes=timeout)
    token = jwt.encode(payload=payload,key=salt,algorithm="HS256",headers=headers).decode('utf-8')

    return token

class JwtQueryParamsAuthentication(BaseAuthentication):

    def authenticate(self, request):
        # logger.debug(request.method)
        # logger.debug(request.META.get("HTTP_AUTHORIZATION"))
        # logger.debug(request.query_params)
        # 获取token并判断token的合理性
        # token = request.META.get("HTTP_AUTHORIZATION")
        # logger.debug(request.META.get("HTTP_TOKEN"))
        token = request.META.get("HTTP_TOKEN")
        # logger.debug(token)
        salt = settings.SECRET_KEY
        payload = None
        msg = None
        try:
            payload = jwt.decode(token,salt,True)
        except exceptions.ExpiredSignatureError:

            raise AuthenticationFailed({
                'code': 3,
                'data': None,
                'msg': "token已失效"
            })
        except jwt.DecodeError:

            raise AuthenticationFailed({
                'code': 3,
                'data': None,
                'msg': "token认证失败"
            })
        except jwt.InvalidTokenError:
            raise AuthenticationFailed({
                'code': 3,
                'data': None,
                'msg': "非法的token"
            })

        return (payload,token)

