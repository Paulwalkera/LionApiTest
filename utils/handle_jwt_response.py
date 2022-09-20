# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2021/6/2 21:20 
    
  @File : handle_jwt_response.py
   
-------------------------------------------------
"""


def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'user_id': user.id,
        'username': user.username,
        'token': token
    }
