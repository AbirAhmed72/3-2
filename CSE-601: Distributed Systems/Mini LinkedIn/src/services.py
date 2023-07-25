from typing import List, Optional
from sqlalchemy.orm import Session
from sqlalchemy.sql.sqltypes import Integer
import models, schemas
from jose import JWTError, jwt #JSON Web Token
from datetime import datetime, time, timedelta
import random
from passlib.hash import bcrypt
SECRET_KEY = 'e2c6a3bc1aad22372e102e8f9f657bccd65676aef94587815b9d4d2c4960a650'
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp" : expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
def create_hashed_password(password: str):
    return bcrypt.hash(password)
def verify_hashed_password(password: str, password_hashed: str):
    return bcrypt.verify(password, password_hashed)
def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = create_hashed_password(user.password)
    db_user = models.User(
        # username = user.username,
        username = user.username,
        password_hashed = hashed_password,
        # is_active = True
    )
    print(db_user)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    delattr(db_user, "password_hashed")
    return db_user
def get_user_by_username(db: Session, username: str):
    print("Checking existing users")
    return db.query(models.User).filter(models.User.username == username).first()

def get_all_users(db: Session):
    return db.query(models.User).all()

def get_user_by_id(db: Session, id: int):
    print("Checking existing users")
    return db.query(models.User).filter(models.User.id == id).first()

def make_post(db: Session, current_username: str, post_text, image_url: Optional[str] = None):
    db_post = models.Post(
        post_text = post_text,
        image_url = image_url,
        created_at = datetime.utcnow(),
        username = current_username
    )
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post
 
# def make_appointment(db:Session, current_user_id:int, doctor_id: int, data: schemas.ConsultationData):
#     appointment = models.Consultation(
#         user_id = current_user_id,
#         patient_name = get_user_by_id(db, current_user_id).name,
#         doctor_id = doctor_id,
#         required_doctor = data.required_doctor,
#         symptoms = str(data.perceived_symptoms),
#         predicted_disease = data.predicted_disease,
#         status = False,
#         appointment_datetime=data.appointment_datetime
#     )
#     db.add(appointment)
#     db.commit()
#     db.refresh(appointment)
#     # print(db.query(models.Consultation).filter(models.Consultation.user_id == current_user_id).first())
#     return db.query(models.Consultation).filter(models.Consultation.user_id == current_user_id).first()
# def get_specialized_doctors_list(db: Session, doctor_specialization: str, skip: int = 0, limit: int = 10) -> List[schemas.DoctorData]:
#     doctors = db.query(models.Doctors).filter(models.Doctors.specialization == doctor_specialization, models.Doctors.is_approved == True).offset(skip).limit(limit).all()
#     specialized_doctors = []
#     for doctor in doctors:
#         specialized_doctors.append(
#             schemas.DoctorData(
#                 id=doctor.id,
#                 username=doctor.username,
#                 name=doctor.name,
#                 specialization=doctor.specialization,
#                 approval=doctor.is_approved
#             )
#         )
#     return specialized_doctors
# def get_doctor_by_username(db: Session, username: str):
#     return db.query(models.Doctors).filter(models.Doctors.username == username).first()
# def get_doctor_by_id(db: Session, id: int):
#     return db.query(models.Doctors).filter(models.Doctors.id == id).first()
# def get_appointment(db: Session, appointment_id: int):
#     return db.query(models.Consultation).filter(models.Consultation.appointment_id == appointment_id).first()
# def get_appointment_by_user_id(db: Session, user_id: int):
#     return db.query(models.Consultation).filter(models.Consultation.user_id == user_id).first()
