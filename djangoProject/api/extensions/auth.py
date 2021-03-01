from django.conf import settings
from rest_framework.authentication import BaseAuthentication
import jwt
from jwt import exceptions
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.views import Response
"""
认证登陆
"""
class JwtQueryParamsAuthentication(BaseAuthentication):

    def authenticate(self, request):

        # 获取token并判断token的合理性
        token = request.META.get("HTTP_AUTHORIZATION")

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