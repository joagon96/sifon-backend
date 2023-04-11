from flask import Flask, jsonify, request, copy_current_request_context, make_response, session
import datetime
import jwt
# from cypherEX import cypherEX
from functools import wraps
import sqlite3

#secretSessionKey = cypherEX()
#sessionKey = secretSessionKey.cypheration('Test')
sessionKey = 'Test'
# Design to called by external Classes

"""
WORKFLOW
---------------------------------

FRONT               BACKEND

Login   --------->    getToken
Action  -api-sec->    decodeToken
User    <---------    sendUser

---------------------------------
"""


def require_api_token(func):
    @wraps(func)
    def decorator(*args, **kwargs):
        token = None
        if 'api-sec' not in request.headers:
            return make_response("Access denied")
        else:
            token = request.headers['api-sec']
            if token:
                data = jwt.decode(token, sessionKey)
                # Here maybe can filter the user using the owner ID
                userCurrent = data['owner']  # filter by query
                with sqlite3.connect("sifono_db.db") as con:
                    c = con.cursor()
                    c.execute("SELECT * FROM Usuario WHERE id=?",(userCurrent,))
                    userCurrent = c.fetchone()
                con.commit()
                con.close()
            else:
                userCurrent = None
                return jsonify({'Error': 'Token is Invalid'})
        return func(userCurrent, *args, **kwargs)
    return decorator

class AuthBraska(object):
    def encode(self, userID):
        """
        Generate the encode token
        :return: string
        """
        try:
            pay = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=300),
                'owner': userID
            }
            token =  jwt.encode(pay, sessionKey, algorithm='HS256')
            return token
        except:
            return make_response(jsonify({'msg': 'Error in the encode token, please try again.'}), 403)
        return 0

    def decode(self, token):
        """
        Decode the auth token
        :return: integer|string
        """
        try:
            pay = jwt.decode(token, sessionKey)
            return pay['owner']
        except jwt.ExpiredSignatureError:
            return 'Signature expired.'
        except jwt.InvalidTokenError:
            return 'Invalid token.'
        return 0
