

# from schemas.img_schemas import cut_change_schemas,change_img_schemas
from config.db import engine
from models.index import cut_change, change_img
from fastapi.responses import FileResponse
import os  # ,cv2, uuid, pixellib

import jwt
from datetime import datetime, timedelta
from functools import wraps

# import matplotlib.pyplot as plt
from sqlalchemy import desc
from pixellib.tune_bg import alter_bg
from rembg import remove

# from random import randint
import random
import base64
import io
import PIL.Image
from PIL import Image
from io import BytesIO
from pydantic import BaseModel
from starlette.responses import StreamingResponse
from fastapi import Depends, FastAPI, Header, Request, Body, File, UploadFile
import requests
import shutil
import random
import string
import json
from flask_cors import CORS
from fastapi.middleware.cors import CORSMiddleware

from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask_cors import CORS, cross_origin
from flask_login import (
    LoginManager,
    UserMixin,
    login_user,
    login_required,
    logout_user,
    current_user,
)


# ______SONPIPI______
from pickle import FALSE
from tkinter import TRUE
import mysql.connector
import smtplib
import hashlib
import requests
import threading
import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth
from getpass import getpass
import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# from bs4 import BeautifulSoup
from flask import Flask, request, jsonify, session
from flask_session import Session

FLASKapp = Flask(__name__)
# apiFLASK = Api(app)

login_manager = LoginManager()
login_manager.init_app(FLASKapp)

cors = CORS(FLASKapp)
FLASKapp.config["CORS_HEADERS"] = "Content-Type"

IMAGEDIR = "images/"
IMAGEDIR_OUT = "images/out_put/"
YOUR_SECRET_KEY = "keysecret"

FLASKapp.config["SESSION_PERMANENT"] = False
FLASKapp.config["SESSION_TYPE"] = "filesystem"
Session(FLASKapp)


config = {
    "user": "root",
    "password": "18112002aD@",
    "host": "localhost",
    "port": 3306,
    "database": "fakelocation",
}
# cred = firebase_admin.credentials.Certificate('fir-sigup-b773e-firebase-adminsdk-anunx-0416c5a276.json')
# cred = firebase_admin.credentials.Certificate('fir-sigup-b773e-firebase-adminsdk-anunx-f6abbb59a1.json')
cred = firebase_admin.credentials.Certificate(
    "fakelocation1-c0453-firebase-adminsdk-aug09-56c714bd51.json"
)

firebase_admin.initialize_app(cred)


@FLASKapp.route("/login", methods=["POST"])
def loginAccount():
    email = request.form.get("email")
    password = request.form.get("password")
    try:
        connection = mysql.connector.connect(**config)
        mycursor = connection.cursor()

        # Kiểm tra thông tin email và mật khẩu trong cơ sở dữ liệu
        sql = "SELECT * FROM user WHERE email = %s AND password = %s"
        val = (email, password)
        mycursor.execute(sql, val)
        user_info = mycursor.fetchone()

        if user_info:
            user = {
                "id_user": user_info[0],
                "email": user_info[1],
                "full_name": user_info[2],
                "user_name": user_info[3],
                "link_avatar": user_info[4],
                "ip_register": user_info[5],
                "device_register": user_info[6],
            }

            token_payload = {
                "user_id": user["id_user"],
                "exp": datetime.datetime.utcnow() + datetime.timedelta(days=1)  # Thời gian hết hạn của token
            }
            token = jwt.encode(token_payload, YOUR_SECRET_KEY, algorithm="HS256")

            return {"ketqua": "Đăng nhập thành công!", "user": user, "token": token}
        else:
            return {"ketqua": "Email hoặc mật khẩu không đúng."}

    except Exception as e:
        return {"ketqua": "Lỗi khi kết nối đến cơ sở dữ liệu."}

@FLASKapp.route("/profile/change_avatar", methods=["PUT"])
def change_avatar():
    # Lấy token từ tiêu đề Authorization
    auth_header = request.headers.get("Authorization")

    id_user = request.form.get("id_user")
    link_avatar = request.form.get("link_avatar")

    if auth_header:
        try:
            # Tách phần "Bearer" ra khỏi token
            token = auth_header.split(" ")[1]
            # Giải mã token sử dụng secret key để lấy thông tin user_id
            token_payload = jwt.decode(token, YOUR_SECRET_KEY, algorithms=["HS256"])
            user_id = token_payload["user_id"]
            # Kiểm tra thông tin user_id và thực hiện thay đổi link_avatar
            # ...
            connection = mysql.connector.connect(**config)
            mycursor = connection.cursor()

            # Update the link_avatar for the user with the given id_user
            sql = "UPDATE user SET link_avatar = %s WHERE id_user = %s"
            val = (link_avatar, id_user)
            mycursor.execute(sql, val)
            connection.commit()
            mycursor.close()
            connection.close()

            return {"ketqua": "Avatar updated successfully!"}
        except jwt.ExpiredSignatureError:
            return {"ketqua": "Token đã hết hạn, vui lòng đăng nhập lại."}
        except jwt.InvalidTokenError:
            return {"ketqua": "Token không hợp lệ, vui lòng đăng nhập lại."}
    else:
        return {"ketqua": "Vui lòng cung cấp token trong tiêu đề Authorization."}


if __name__ == "__main__":
    FLASKapp.run(host="0.0.0.0", port=3003)



