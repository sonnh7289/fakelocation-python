from sqlalchemy import create_engine, MetaData
from sqlalchemy import URL

# create_engine('mysql+pymysql://<username>:<password>@<host>/<dbname>')
# echo=True

url_object = URL.create(
    "mysql+pymysql",
    username="root",
    password="18112002aD@",  # plain (unescaped) text admi
    host="localhost",
    port="3306",
    database="fakelocation",
)

engine = create_engine(url_object, pool_recycle=3600)
# engine = create_engine('mysql+pymysql://root@localhost:3306/api_img',echo=True)
meta = MetaData()
