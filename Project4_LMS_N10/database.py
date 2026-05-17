from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

<<<<<<< HEAD:Dự án Học trực tuyến LMS/Dự án Học trực tuyến LMS/database.py
# Sử dụng %5C thay cho \ để đảm bảo URL không bị lỗi định dạng
SQLALCHEMY_DATABASE_URL = "mssql+pyodbc://DESKTOP-ICPA8AC\SQLEXPRESS/LMS_Project?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"


=======
# Đã sửa lại tên database thành LMS_Project
<<<<<<< HEAD
SQLALCHEMY_DATABASE_URL = r"mssql+pyodbc://LAPTOP-LG42FLRB\SQLEXPRESS/LMS_Project?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"
=======
SQLALCHEMY_DATABASE_URL = r"mssql+pyodbc://@DESKTOP-ICPA8AC\SQLEXPRESS/LMS_Project?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"
>>>>>>> 51ca7df891592d6706aa8a7b444c134ad2f10209
>>>>>>> 5f5ba9255d6db3b3065305313d36814e5e7b94ed:Dự án Học trực tuyến LMS/database.py

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()