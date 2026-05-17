
from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, Text, DateTime, Date, NVARCHAR, Numeric
from database import Base
from sqlalchemy.ext.declarative import declarative_base
import datetime
                
Base = declarative_base()
# ==========================================
# 1. NGƯỜI DÙNG & HỆ THỐNG
# ==========================================
class User(Base):
<<<<<<< HEAD:Dự án Học trực tuyến LMS/Dự án Học trực tuyến LMS/models.py
    __tablename__ = "g10users"
=======
<<<<<<< HEAD
    __tablename__ = "g10users"
=======
    __tablename__ = "users"
>>>>>>> 51ca7df891592d6706aa8a7b444c134ad2f10209
>>>>>>> 5f5ba9255d6db3b3065305313d36814e5e7b94ed:Dự án Học trực tuyến LMS/models.py
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String(50), nullable=False)
    password = Column(String(255), nullable=False)
    role = Column(String(50))
    is_active = Column(Boolean, default=True)

class Notification(Base):
<<<<<<< HEAD:Dự án Học trực tuyến LMS/Dự án Học trực tuyến LMS/models.py
    __tablename__ = "g10notifications"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('g10users.id'), nullable=False)
=======
<<<<<<< HEAD
    __tablename__ = "g10notifications"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('g10users.id'), nullable=False)
=======
    __tablename__ = "notifications"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
>>>>>>> 51ca7df891592d6706aa8a7b444c134ad2f10209
>>>>>>> 5f5ba9255d6db3b3065305313d36814e5e7b94ed:Dự án Học trực tuyến LMS/models.py
    title = Column(String(255), nullable=False)
    message = Column(String(500), nullable=False)
    is_read = Column(Boolean, default=False)

# ==========================================
# 2. KHÓA HỌC & BÀI HỌC
# ==========================================
class Category(Base):
<<<<<<< HEAD:Dự án Học trực tuyến LMS/Dự án Học trực tuyến LMS/models.py
    __tablename__ = "g10categories"
=======
<<<<<<< HEAD
    __tablename__ = "g10categories"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    parent_id = Column(Integer, ForeignKey('g10categories.id'), nullable=True)

class Course(Base):
    __tablename__ = "g10courses"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    category_id = Column(Integer, ForeignKey('g10categories.id'), nullable=False)
    instructor_id = Column(Integer, ForeignKey('g10users.id'), nullable=False)
    title = Column(String(255), nullable=False)
    price = Column(Numeric(18, 2), nullable=False) 
    status = Column(String(50))

class Section(Base):
    __tablename__ = "g10sections"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    course_id = Column(Integer, ForeignKey('g10courses.id'), nullable=False)
=======
    __tablename__ = "categories"
>>>>>>> 5f5ba9255d6db3b3065305313d36814e5e7b94ed:Dự án Học trực tuyến LMS/models.py
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    parent_id = Column(Integer, ForeignKey('g10categories.id'), nullable=True)

class Course(Base):
    __tablename__ = "g10courses"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    category_id = Column(Integer, ForeignKey('g10categories.id'), nullable=False)
    instructor_id = Column(Integer, ForeignKey('g10users.id'), nullable=False)
    title = Column(String(255), nullable=False)
    price = Column(Numeric(18, 2), nullable=False) 
    status = Column(String(50))

class Section(Base):
    __tablename__ = "g10sections"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
<<<<<<< HEAD:Dự án Học trực tuyến LMS/Dự án Học trực tuyến LMS/models.py
    course_id = Column(Integer, ForeignKey('g10courses.id'), nullable=False)
=======
    course_id = Column(Integer, ForeignKey('courses.id'), nullable=False)
>>>>>>> 51ca7df891592d6706aa8a7b444c134ad2f10209
>>>>>>> 5f5ba9255d6db3b3065305313d36814e5e7b94ed:Dự án Học trực tuyến LMS/models.py
    title = Column(String(255), nullable=False)
    order_index = Column(Integer, nullable=False)

class Lesson(Base):
<<<<<<< HEAD:Dự án Học trực tuyến LMS/Dự án Học trực tuyến LMS/models.py
    __tablename__ = "g10lessons"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    section_id = Column(Integer, ForeignKey('g10sections.id'), nullable=False)
=======
<<<<<<< HEAD
    __tablename__ = "g10lessons"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    section_id = Column(Integer, ForeignKey('g10sections.id'), nullable=False)
=======
    __tablename__ = "lessons"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    section_id = Column(Integer, ForeignKey('sections.id'), nullable=False)
>>>>>>> 51ca7df891592d6706aa8a7b444c134ad2f10209
>>>>>>> 5f5ba9255d6db3b3065305313d36814e5e7b94ed:Dự án Học trực tuyến LMS/models.py
    lesson_type = Column(String(50))
    url_content = Column(String(500))

# ==========================================
# 3. THI CỬ & TRẮC NGHIỆM
# ==========================================
class Quiz(Base):
<<<<<<< HEAD:Dự án Học trực tuyến LMS/Dự án Học trực tuyến LMS/models.py
    __tablename__ = "g10quizzes"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))  
    time_limit = Column(Integer)
    difficulty = Column(String(20))
    pass_score = Column(Integer, default=50)

class Question(Base):
    __tablename__ = "g10questions"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    quiz_id = Column(Integer, ForeignKey('g10quizzes.id'), nullable=False)
=======
<<<<<<< HEAD
    __tablename__ = "g10quizzes"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    course_id = Column(Integer, ForeignKey('g10courses.id'), nullable=False)
=======
    __tablename__ = "quizzes"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    course_id = Column(Integer, ForeignKey('courses.id'), nullable=False)
>>>>>>> 51ca7df891592d6706aa8a7b444c134ad2f10209
    time_limit = Column(Integer, nullable=False)
    pass_score = Column(Float, nullable=False)

class Question(Base):
<<<<<<< HEAD
    __tablename__ = "g10questions"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    quiz_id = Column(Integer, ForeignKey('g10quizzes.id'), nullable=False)
=======
    __tablename__ = "questions"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    quiz_id = Column(Integer, ForeignKey('quizzes.id'), nullable=False)
>>>>>>> 51ca7df891592d6706aa8a7b444c134ad2f10209
>>>>>>> 5f5ba9255d6db3b3065305313d36814e5e7b94ed:Dự án Học trực tuyến LMS/models.py
    content = Column(String(500), nullable=False)
    point = Column(Float, nullable=False)

class Option(Base):
<<<<<<< HEAD:Dự án Học trực tuyến LMS/Dự án Học trực tuyến LMS/models.py
    __tablename__ = "g10options"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    question_id = Column(Integer, ForeignKey('g10questions.id'), nullable=False)
=======
<<<<<<< HEAD
    __tablename__ = "g10options"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    question_id = Column(Integer, ForeignKey('g10questions.id'), nullable=False)
=======
    __tablename__ = "options"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    question_id = Column(Integer, ForeignKey('questions.id'), nullable=False)
>>>>>>> 51ca7df891592d6706aa8a7b444c134ad2f10209
>>>>>>> 5f5ba9255d6db3b3065305313d36814e5e7b94ed:Dự án Học trực tuyến LMS/models.py
    option_text = Column(String(255), nullable=False)
    is_correct = Column(Boolean, nullable=False)

# ==========================================
# 4. TIẾN ĐỘ & KẾT QUẢ
# ==========================================
class Enrollment(Base):
<<<<<<< HEAD:Dự án Học trực tuyến LMS/Dự án Học trực tuyến LMS/models.py
    __tablename__ = "g10enrollments"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('g10users.id'), nullable=False)
    course_id = Column(Integer, ForeignKey('g10courses.id'), nullable=False)
=======
<<<<<<< HEAD
    __tablename__ = "g10enrollments"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('g10users.id'), nullable=False)
    course_id = Column(Integer, ForeignKey('g10courses.id'), nullable=False)
=======
    __tablename__ = "enrollments"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    course_id = Column(Integer, ForeignKey('courses.id'), nullable=False)
>>>>>>> 51ca7df891592d6706aa8a7b444c134ad2f10209
>>>>>>> 5f5ba9255d6db3b3065305313d36814e5e7b94ed:Dự án Học trực tuyến LMS/models.py
    enrolled_at = Column(DateTime, default=datetime.datetime.now)
    status = Column(String(50))

class CourseProgress(Base):
<<<<<<< HEAD:Dự án Học trực tuyến LMS/Dự án Học trực tuyến LMS/models.py
    __tablename__ = "g10course_progress"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('g10users.id'), nullable=False)
    lesson_id = Column(Integer, ForeignKey('g10lessons.id'), nullable=False)
=======
<<<<<<< HEAD
    __tablename__ = "g10course_progress"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('g10users.id'), nullable=False)
    lesson_id = Column(Integer, ForeignKey('g10lessons.id'), nullable=False)
=======
    __tablename__ = "course_progress"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    lesson_id = Column(Integer, ForeignKey('lessons.id'), nullable=False)
>>>>>>> 51ca7df891592d6706aa8a7b444c134ad2f10209
>>>>>>> 5f5ba9255d6db3b3065305313d36814e5e7b94ed:Dự án Học trực tuyến LMS/models.py
    is_completed = Column(Boolean, default=False)
    completed_at = Column(DateTime)

class QuizResult(Base):
<<<<<<< HEAD:Dự án Học trực tuyến LMS/Dự án Học trực tuyến LMS/models.py
    __tablename__ = "g10quiz_results"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('g10users.id'), nullable=False)
    quiz_id = Column(Integer, ForeignKey('g10quizzes.id'), nullable=False)
=======
<<<<<<< HEAD
    __tablename__ = "g10quiz_results"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('g10users.id'), nullable=False)
    quiz_id = Column(Integer, ForeignKey('g10quizzes.id'), nullable=False)
=======
    __tablename__ = "quiz_results"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    quiz_id = Column(Integer, ForeignKey('quizzes.id'), nullable=False)
>>>>>>> 51ca7df891592d6706aa8a7b444c134ad2f10209
>>>>>>> 5f5ba9255d6db3b3065305313d36814e5e7b94ed:Dự án Học trực tuyến LMS/models.py
    total_score = Column(Float, nullable=False)
    status = Column(String(50))
    attempt_count = Column(Integer)

# ==========================================
# 5. TÀI CHÍNH & TƯƠNG TÁC
# ==========================================
class Payment(Base):
<<<<<<< HEAD:Dự án Học trực tuyến LMS/Dự án Học trực tuyến LMS/models.py
    __tablename__ = "g10payments"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('g10users.id'), nullable=False)
    course_id = Column(Integer, ForeignKey('g10courses.id'), nullable=False)
    amount = Column(Numeric(18, 2), nullable=False) 
    payment_method = Column(String(100), nullable=False)
=======
<<<<<<< HEAD
    __tablename__ = "g10payments"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('g10users.id'), nullable=False)
    course_id = Column(Integer, ForeignKey('g10courses.id'), nullable=False)
    amount = Column(Numeric(18, 2), nullable=False) 
=======
    __tablename__ = "payments"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    course_id = Column(Integer, ForeignKey('courses.id'), nullable=False)
    amount = Column(Numeric(18, 2), nullable=False) # Đã đổi thành Numeric cho khớp Decimal
>>>>>>> 51ca7df891592d6706aa8a7b444c134ad2f10209
    payment_method = Column(String(100))
>>>>>>> 5f5ba9255d6db3b3065305313d36814e5e7b94ed:Dự án Học trực tuyến LMS/models.py
    transaction_id = Column(String(100), nullable=False)
   

class Coupon(Base):
<<<<<<< HEAD:Dự án Học trực tuyến LMS/Dự án Học trực tuyến LMS/models.py
    __tablename__ = "g10coupons"
=======
<<<<<<< HEAD
    __tablename__ = "g10coupons"
=======
    __tablename__ = "coupons"
>>>>>>> 51ca7df891592d6706aa8a7b444c134ad2f10209
>>>>>>> 5f5ba9255d6db3b3065305313d36814e5e7b94ed:Dự án Học trực tuyến LMS/models.py
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    code = Column(String(50), nullable=False)
    discount_val = Column(Integer, nullable=False)
    expiry_date = Column(DateTime, nullable=False)
    usage_limit = Column(Integer, nullable=False)

class Review(Base):
<<<<<<< HEAD:Dự án Học trực tuyến LMS/Dự án Học trực tuyến LMS/models.py
    __tablename__ = "g10reviews"
=======
<<<<<<< HEAD
    __tablename__ = "g10reviews"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    course_id = Column(Integer, ForeignKey('g10courses.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('g10users.id'), nullable=False)
    rating = Column(Integer)
    comment = Column(String(500))
    created_at = Column(DateTime)


class Lesson(Base):
    __tablename__ = "lessons"
    id = Column(Integer, primary_key=True)
    course_id = Column(Integer)
    title = Column(String)
    video_url = Column(String)

class Assignment(Base):
    __tablename__ = "assignments"
    id = Column(Integer, primary_key=True)
    lesson_id = Column(Integer)
    question = Column(String)
    answer = Column(String)

class Attendance(Base):
    __tablename__ = "attendance"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    course_id = Column(Integer)
    status = Column(Boolean)
=======
    __tablename__ = "reviews"
>>>>>>> 5f5ba9255d6db3b3065305313d36814e5e7b94ed:Dự án Học trực tuyến LMS/models.py
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    course_id = Column(Integer, ForeignKey('g10courses.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('g10users.id'), nullable=False)
    rating = Column(Integer)
    comment = Column(String(500))
    created_at = Column(DateTime)
<<<<<<< HEAD:Dự án Học trực tuyến LMS/Dự án Học trực tuyến LMS/models.py



class Assignment(Base):
    __tablename__ = "g10assignments"
    id = Column(Integer, primary_key=True)
    lesson_id = Column(Integer)
    question = Column(String)
    answer = Column(String)

class Attendance(Base):
    __tablename__ = "g10attendance"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    course_id = Column(Integer)
    status = Column(Boolean)
class Event(Base):
    __tablename__ = 'g10events'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(NVARCHAR(255), nullable=False)
    event_date = Column(Date, nullable=False)
    status = Column(NVARCHAR(50), nullable=False)

class Order(Base):
    __tablename__ = "g10orders"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_name = Column(String(100), nullable=False)
    course_title = Column(String(255), nullable=False)
    price = Column(Integer, nullable=False)
    status = Column(String(50), default="Đang xác nhận")
=======
>>>>>>> 51ca7df891592d6706aa8a7b444c134ad2f10209
>>>>>>> 5f5ba9255d6db3b3065305313d36814e5e7b94ed:Dự án Học trực tuyến LMS/models.py
