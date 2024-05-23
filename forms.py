
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField,TextField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from agrotech.models import *
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms import SelectField
from wtforms.fields.html5 import DateField
from wtforms import validators, ValidationError


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login') 

class Staffreg(FlaskForm):
    
    fname = StringField('First Name', validators=[DataRequired(), Length(min=1, max=400)])
    sname = StringField('Second Name', validators=[DataRequired(), Length(min=1, max=400)])
    address = StringField('Address', validators=[DataRequired(), Length(min=1, max=400)])
    gender = StringField('Gender', validators=[DataRequired(), Length(min=3, max=10)])
    phone = StringField('Phone Number', validators=[DataRequired(), Length(min=1, max=400)])
    district = StringField('District', validators=[DataRequired(), Length(min=1, max=400)])
    position = StringField('Position')
    email = StringField('Email id', validators=[DataRequired(), Length(min=1, max=400)])
    password = StringField('Password', validators=[DataRequired(), Length(min=1, max=400)])
    pic = FileField('Uploard your photo', validators=[DataRequired(),FileAllowed(['jpg', 'png','jpeg'])])
    submit = SubmitField('Save')

class Regshm(FlaskForm):
    
    name = StringField('Name', validators=[DataRequired(), Length(min=1, max=400)])
    address = StringField('Address', validators=[DataRequired(), Length(min=1, max=400)])
    gender = StringField('Gender', validators=[DataRequired(), Length(min=3, max=10)])
    dob = StringField('Date of birth', validators=[DataRequired(), Length(min=1, max=400)])
    phone = StringField('Phone Number', validators=[DataRequired(), Length(min=1, max=400)])
    email = StringField('Email id', validators=[DataRequired(), Length(min=1, max=400)])
    block = StringField('Block', validators=[DataRequired(), Length(min=1, max=400)])
    panchayath = StringField('Panchayath', validators=[DataRequired(), Length(min=1, max=400)])
    village = StringField('Village', validators=[DataRequired(), Length(min=1, max=400)])
    bank = StringField('bank', validators=[DataRequired(), Length(min=1, max=400)])
    accountnum = StringField('Account number', validators=[DataRequired(), Length(min=1, max=400)])
    area = StringField('Total Area', validators=[DataRequired(), Length(min=1, max=400)])
    cropname = StringField('Crop name', validators=[DataRequired(), Length(min=1, max=400)])
    img = FileField('Uploard the photo of crop', validators=[DataRequired(),FileAllowed(['jpg', 'png','jpeg'])])
    submit = SubmitField('Save')

class Farmer_regist(FlaskForm):
    
    name = StringField('Name', validators=[DataRequired(), Length(min=1, max=400)])
    address = StringField('Address', validators=[DataRequired(), Length(min=1, max=400)])
    gender = StringField('Gender', validators=[DataRequired(), Length(min=3, max=10)])
    dob = StringField('Date of birth', validators=[DataRequired(), Length(min=1, max=400)])
    phone = StringField('Phone Number', validators=[DataRequired(), Length(min=1, max=400)])
    email = StringField('Email id', validators=[DataRequired(), Length(min=1, max=400)])
    block = StringField('Block', validators=[DataRequired(), Length(min=1, max=400)])
    panchayath = StringField('Panchayath', validators=[DataRequired(), Length(min=1, max=400)])
    village = StringField('Village', validators=[DataRequired(), Length(min=1, max=400)])
    bank = StringField('bank', validators=[DataRequired(), Length(min=1, max=400)])
    accountnum = StringField('Account number', validators=[DataRequired(), Length(min=1, max=400)])
    aadharnum = StringField('Aadhar number', validators=[DataRequired(), Length(min=1, max=400)])
    rationnum = StringField('Ration card number', validators=[DataRequired(), Length(min=1, max=400)])
    area = StringField('Total Area', validators=[DataRequired(), Length(min=1, max=400)])
    img = FileField('Uploard the photo of Aadharcard', validators=[DataRequired(),FileAllowed(['jpg', 'png','jpeg'])])
    submit = SubmitField('Save')

class Anfarmerreg(FlaskForm):
    
    name = StringField('Name', validators=[DataRequired(), Length(min=1, max=400)])
    address = StringField('Address', validators=[DataRequired(), Length(min=1, max=400)])
    gender = StringField('Gender', validators=[DataRequired(), Length(min=3, max=10)])
    dob = StringField('Date of birth', validators=[DataRequired(), Length(min=1, max=400)])
    phone = StringField('Phone Number', validators=[DataRequired(), Length(min=1, max=400)])
    email = StringField('Email id', validators=[DataRequired(), Length(min=1, max=400)])
    block = StringField('Block', validators=[DataRequired(), Length(min=1, max=400)])
    panchayath = StringField('Panchayath', validators=[DataRequired(), Length(min=1, max=400)])
    village = StringField('Village', validators=[DataRequired(), Length(min=1, max=400)])
    bank = StringField('bank', validators=[DataRequired(), Length(min=1, max=400)])
    accountnum = StringField('Account number', validators=[DataRequired(), Length(min=1, max=400)])
    aadharnum = StringField('Account number', validators=[DataRequired(), Length(min=1, max=400)])
    rationnum = StringField('Account number', validators=[DataRequired(), Length(min=1, max=400)])
    area = StringField('Total Area', validators=[DataRequired(), Length(min=1, max=400)])
    img = FileField('Uploard the photo of Aadharcard', validators=[DataRequired(),FileAllowed(['jpg', 'png','jpeg'])])
    submit = SubmitField('Save')


class Machinaries(FlaskForm):
    
    name = StringField('Name', validators=[DataRequired(), Length(min=1, max=400)])
    address = StringField('Address', validators=[DataRequired(), Length(min=1, max=400)])
    gender = StringField('Gender', validators=[DataRequired(), Length(min=3, max=10)])
    dob = StringField('Date of birth', validators=[DataRequired(), Length(min=1, max=400)])
    phone = StringField('Phone Number', validators=[DataRequired(), Length(min=1, max=400)])
    email = StringField('Email id', validators=[DataRequired(), Length(min=1, max=400)])
    block = StringField('Block', validators=[DataRequired(), Length(min=1, max=400)])
    panchayath = StringField('Panchayath', validators=[DataRequired(), Length(min=1, max=400)])
    village = StringField('Village', validators=[DataRequired(), Length(min=1, max=400)])
    bank = StringField('bank', validators=[DataRequired(), Length(min=1, max=400)])
    accountnum = StringField('Account number', validators=[DataRequired(), Length(min=1, max=400)])
    aadharnum = StringField('Aadhar number', validators=[DataRequired(), Length(min=1, max=400)])
    rationnum = StringField('Rationcard number', validators=[DataRequired(), Length(min=1, max=400)])
    area = StringField('Total Area', validators=[DataRequired(), Length(min=1, max=400)])
    machines = StringField('Machinaries')
    img = FileField('Uploard the photo of Aadharcard', validators=[DataRequired(),FileAllowed(['jpg', 'png','jpeg'])])
    submit = SubmitField('Save')

class Fertilizers(FlaskForm):
    
    name = StringField('Name', validators=[DataRequired(), Length(min=1, max=400)])
    address = StringField('Address', validators=[DataRequired(), Length(min=1, max=400)])
    gender = StringField('Gender', validators=[DataRequired(), Length(min=3, max=10)])
    dob = StringField('Date of birth', validators=[DataRequired(), Length(min=1, max=400)])
    phone = StringField('Phone Number', validators=[DataRequired(), Length(min=1, max=400)])
    email = StringField('Email id', validators=[DataRequired(), Length(min=1, max=400)])
    block = StringField('Block', validators=[DataRequired(), Length(min=1, max=400)])
    panchayath = StringField('Panchayath', validators=[DataRequired(), Length(min=1, max=400)])
    village = StringField('Village', validators=[DataRequired(), Length(min=1, max=400)])
    bank = StringField('bank', validators=[DataRequired(), Length(min=1, max=400)])
    accountnum = StringField('Account number', validators=[DataRequired(), Length(min=1, max=400)])
    aadharnum = StringField('Aadhar number', validators=[DataRequired(), Length(min=1, max=400)])
    rationnum = StringField('Rationcard number', validators=[DataRequired(), Length(min=1, max=400)])
    category = StringField('Category of fertilizers', validators=[DataRequired(), Length(min=1, max=400)])
    farmerid = StringField('Farmer Id')
    img = FileField('Uploard the photo of Aadharcard', validators=[DataRequired(),FileAllowed(['jpg', 'png','jpeg'])])
    submit = SubmitField('Save')


class Cows(FlaskForm):
    
    name = StringField('Name', validators=[DataRequired(), Length(min=1, max=400)])
    address = StringField('Address', validators=[DataRequired(), Length(min=1, max=400)])
    gender = StringField('Gender', validators=[DataRequired(), Length(min=3, max=10)])
    dob = StringField('Date of birth', validators=[DataRequired(), Length(min=1, max=400)])
    phone = StringField('Phone Number', validators=[DataRequired(), Length(min=1, max=400)])
    email = StringField('Email id', validators=[DataRequired(), Length(min=1, max=400)])
    block = StringField('Block', validators=[DataRequired(), Length(min=1, max=400)])
    panchayath = StringField('Panchayath', validators=[DataRequired(), Length(min=1, max=400)])
    village = StringField('Village', validators=[DataRequired(), Length(min=1, max=400)])
    bank = StringField('bank', validators=[DataRequired(), Length(min=1, max=400)])
    accountnum = StringField('Account number', validators=[DataRequired(), Length(min=1, max=400)])
    aadharnum = StringField('Aadhar number', validators=[DataRequired(), Length(min=1, max=400)])
    rationnum = StringField('Rationcard number', validators=[DataRequired(), Length(min=1, max=400)])
    cowsnum = StringField('Number of cows', validators=[DataRequired(), Length(min=1, max=400)])
    ctype = StringField('Type of cows', validators=[DataRequired(), Length(min=1, max=400)])
    category = StringField('Category of Subsidy', validators=[DataRequired(), Length(min=1, max=400)])
    farmerid = StringField('Farmer Id')
    img = FileField('Uploard the copy of Aadharcard', validators=[DataRequired(),FileAllowed(['jpg', 'png','jpeg'])])
    submit = SubmitField('Save')

class Goats(FlaskForm):
    
    name = StringField('Name', validators=[DataRequired(), Length(min=1, max=400)])
    address = StringField('Address', validators=[DataRequired(), Length(min=1, max=400)])
    gender = StringField('Gender', validators=[DataRequired(), Length(min=3, max=10)])
    dob = StringField('Date of birth', validators=[DataRequired(), Length(min=1, max=400)])
    phone = StringField('Phone Number', validators=[DataRequired(), Length(min=1, max=400)])
    email = StringField('Email id', validators=[DataRequired(), Length(min=1, max=400)])
    block = StringField('Block', validators=[DataRequired(), Length(min=1, max=400)])
    panchayath = StringField('Panchayath', validators=[DataRequired(), Length(min=1, max=400)])
    village = StringField('Village', validators=[DataRequired(), Length(min=1, max=400)])
    bank = StringField('bank', validators=[DataRequired(), Length(min=1, max=400)])
    accountnum = StringField('Account number', validators=[DataRequired(), Length(min=1, max=400)])
    aadharnum = StringField('Aadhar number', validators=[DataRequired(), Length(min=1, max=400)])
    rationnum = StringField('Rationcard number', validators=[DataRequired(), Length(min=1, max=400)])
    goatnum = StringField('Number of goats', validators=[DataRequired(), Length(min=1, max=400)])
    gtype = StringField('Type of goats', validators=[DataRequired(), Length(min=1, max=400)])
    category = StringField('Category of Subsidy', validators=[DataRequired(), Length(min=1, max=400)])
    farmerid = StringField('Farmer Id')
    img = FileField('Uploard the copy of Aadharcard', validators=[DataRequired(),FileAllowed(['jpg', 'png','jpeg'])])
    submit = SubmitField('Save')

class Hens(FlaskForm):
    
    name = StringField('Name', validators=[DataRequired(), Length(min=1, max=400)])
    address = StringField('Address', validators=[DataRequired(), Length(min=1, max=400)])
    gender = StringField('Gender', validators=[DataRequired(), Length(min=3, max=10)])
    dob = StringField('Date of birth', validators=[DataRequired(), Length(min=1, max=400)])
    phone = StringField('Phone Number', validators=[DataRequired(), Length(min=1, max=400)])
    email = StringField('Email id', validators=[DataRequired(), Length(min=1, max=400)])
    block = StringField('Block', validators=[DataRequired(), Length(min=1, max=400)])
    panchayath = StringField('Panchayath', validators=[DataRequired(), Length(min=1, max=400)])
    village = StringField('Village', validators=[DataRequired(), Length(min=1, max=400)])
    bank = StringField('bank', validators=[DataRequired(), Length(min=1, max=400)])
    accountnum = StringField('Account number', validators=[DataRequired(), Length(min=1, max=400)])
    aadharnum = StringField('Aadhar number', validators=[DataRequired(), Length(min=1, max=400)])
    rationnum = StringField('Rationcard number', validators=[DataRequired(), Length(min=1, max=400)])
    num = StringField('Number of Item', validators=[DataRequired(), Length(min=1, max=400)])
    htype = StringField('Type of ITem', validators=[DataRequired(), Length(min=1, max=400)])
    category = StringField('Category of Subsidy', validators=[DataRequired(), Length(min=1, max=400)])
    farmerid = StringField('Farmer Id')
    img = FileField('Uploard the copy of Aadharcard', validators=[DataRequired(),FileAllowed(['jpg', 'png','jpeg'])])
    submit = SubmitField('Save')



class Crop_insur(FlaskForm):
    
    name = StringField('Name', validators=[DataRequired(), Length(min=1, max=400)])
    address = StringField('Address', validators=[DataRequired(), Length(min=1, max=400)])
    gender = StringField('Gender', validators=[DataRequired(), Length(min=3, max=10)])
    dob = StringField('Date of birth', validators=[DataRequired(), Length(min=1, max=400)])
    phone = StringField('Phone Number', validators=[DataRequired(), Length(min=1, max=400)])
    email = StringField('Email id', validators=[DataRequired(), Length(min=1, max=400)])
    block = StringField('Block', validators=[DataRequired(), Length(min=1, max=400)])
    panchayath = StringField('Panchayath', validators=[DataRequired(), Length(min=1, max=400)])
    village = StringField('Village', validators=[DataRequired(), Length(min=1, max=400)])
    aadharnum = StringField('Aadhar Number', validators=[DataRequired(), Length(min=1, max=400)])
    bank = StringField('bank', validators=[DataRequired(), Length(min=1, max=400)])
    accountnum = StringField('Account number', validators=[DataRequired(), Length(min=1, max=400)])
    area = StringField('Total Area', validators=[DataRequired(), Length(min=1, max=400)])
    cropname = StringField('Crop name', validators=[DataRequired(), Length(min=1, max=400)])
    farmerid = StringField('Farmerid number', validators=[DataRequired(), Length(min=1, max=400)])
    img = FileField('Uploard the photo of crop', validators=[DataRequired(),FileAllowed(['jpg', 'png','jpeg'])])
    submit = SubmitField('Save')

class Calamity_reg(FlaskForm):
    
    name = StringField('Name', validators=[DataRequired(), Length(min=1, max=400)])
    farmerid = StringField('Farmerid number', validators=[DataRequired(), Length(min=1, max=400)])
    address = StringField('Address', validators=[DataRequired(), Length(min=1, max=400)])
    gender = StringField('Gender', validators=[DataRequired(), Length(min=3, max=10)])
    dob = StringField('Date of birth', validators=[DataRequired(), Length(min=1, max=400)])
    phone = StringField('Phone Number', validators=[DataRequired(), Length(min=1, max=400)])
    email = StringField('Email id', validators=[DataRequired(), Length(min=1, max=400)])
    block = StringField('Block', validators=[DataRequired(), Length(min=1, max=400)])
    panchayath = StringField('Panchayath', validators=[DataRequired(), Length(min=1, max=400)])
    village = StringField('Village', validators=[DataRequired(), Length(min=1, max=400)])
    aadharnum = StringField('Aadhar Number', validators=[DataRequired(), Length(min=1, max=400)])
    bank = StringField('bank', validators=[DataRequired(), Length(min=1, max=400)])
    accountnum = StringField('Account number', validators=[DataRequired(), Length(min=1, max=400)])
    area = StringField('Total Area', validators=[DataRequired(), Length(min=1, max=400)])
    cropname = StringField('Crop name', validators=[DataRequired(), Length(min=1, max=400)])
    img = FileField('Uploard the photo of distroyed crop', validators=[DataRequired(),FileAllowed(['jpg', 'png','jpeg'])])
    submit = SubmitField('Save')



class Soilhealth(FlaskForm):
    
    name = StringField('Name', validators=[DataRequired(), Length(min=1, max=400)])
    address = StringField('Address', validators=[DataRequired(), Length(min=1, max=400)])
    gender = StringField('Gender', validators=[DataRequired(), Length(min=3, max=10)])
    dob = StringField('Date of birth', validators=[DataRequired(), Length(min=1, max=400)])
    phone = StringField('Phone Number', validators=[DataRequired(), Length(min=1, max=400)])
    email = StringField('Email id', validators=[DataRequired(), Length(min=1, max=400)])
    block = StringField('Block', validators=[DataRequired(), Length(min=1, max=400)])
    panchayath = StringField('Panchayath', validators=[DataRequired(), Length(min=1, max=400)])
    village = StringField('Village', validators=[DataRequired(), Length(min=1, max=400)])
    bank = StringField('bank', validators=[DataRequired(), Length(min=1, max=400)])
    accountnum = StringField('Account number', validators=[DataRequired(), Length(min=1, max=400)])
    area = StringField('Total Area', validators=[DataRequired(), Length(min=1, max=400)])
    cropname = StringField('Crop name', validators=[DataRequired(), Length(min=1, max=400)])
    img = FileField('Uploard the photo of Aadhar', validators=[DataRequired(),FileAllowed(['jpg', 'png','jpeg'])])
    submit = SubmitField('Save')

class Addcart(FlaskForm):
    
    bcode = StringField('Code of Book', validators=[DataRequired(), Length(min=1, max=400)])
    bname = StringField('Name of book', validators=[DataRequired(), Length(min=1, max=400)])
    author = StringField('Name of author', validators=[DataRequired(), Length(min=3, max=10)])
    publication = StringField('Name of publication', validators=[DataRequired(), Length(min=1, max=400)])
    pub_year = StringField('Year of published', validators=[DataRequired(), Length(min=1, max=400)])
    price = StringField('price', validators=[DataRequired(), Length(min=1, max=400)])
    img = FileField('Upload image of product', validators=[DataRequired(),FileAllowed(['jpg', 'png','jpeg'])])
    submit = SubmitField('Save')

class Add_magazine(FlaskForm):
    
    name = StringField('Name of book', validators=[DataRequired(), Length(min=1, max=400)])
    author = StringField('Name of author', validators=[DataRequired(), Length(min=3, max=400)])
    publisher = StringField('Name of publication', validators=[DataRequired(), Length(min=1, max=400)])
    features = StringField('Highlights of Book', validators=[DataRequired(), Length(min=1, max=400)])
    rupees = StringField('price of Book', validators=[DataRequired(), Length(min=1, max=400)])
    pic = FileField('Upload image of Book', validators=[DataRequired(),FileAllowed(['jpg', 'png','jpeg'])])
    submit = SubmitField('Save')

class Trainingcent(FlaskForm):
    
    name = StringField('Name of Center', validators=[DataRequired(), Length(min=1, max=400)])
    address = StringField('Address of Center', validators=[DataRequired(), Length(min=1, max=400)])
    programer = StringField('Name of Programer', validators=[DataRequired(), Length(min=1, max=400)])
    contact = StringField('Contact', validators=[DataRequired(), Length(min=1, max=400)])
    date = StringField('Date of program', validators=[DataRequired(), Length(min=3, max=10)])
    time = StringField('time', validators=[DataRequired(), Length(min=1, max=400)])
    topic = StringField('topic of program', validators=[DataRequired(), Length(min=1, max=400)])
    submit = SubmitField('Save')

class Booknow(FlaskForm):
    
    name = StringField('Name of Applicant', validators=[DataRequired(), Length(min=1, max=400)])
    address = StringField('Address of Applicant', validators=[DataRequired(), Length(min=1, max=400)])
    phone = StringField('Contactr', validators=[DataRequired(), Length(min=1, max=400)])
    email = StringField('Email id', validators=[DataRequired(), Length(min=1, max=400)])
    block = StringField('Name of the Block', validators=[DataRequired(), Length(min=3, max=400)])
    panchayath = StringField('Name of Panchayath', validators=[DataRequired(), Length(min=1, max=400)])
    aadhar = StringField('Aadhar number', validators=[DataRequired(), Length(min=1, max=400)])
    submit = SubmitField('Submit')

class Booknowmac(FlaskForm):
    
    name = StringField('Name of Applicant', validators=[DataRequired(), Length(min=1, max=400)])
    address = StringField('Address of Applicant', validators=[DataRequired(), Length(min=1, max=400)])
    phone = StringField('Contactr', validators=[DataRequired(), Length(min=1, max=400)])
    email = StringField('Email id', validators=[DataRequired(), Length(min=1, max=400)])
    block = StringField('Name of the Block', validators=[DataRequired(), Length(min=3, max=400)])
    panchayath = StringField('Name of Panchayath', validators=[DataRequired(), Length(min=1, max=400)])
    aadhar = StringField('Aadhar number', validators=[DataRequired(), Length(min=1, max=400)])
    submit = SubmitField('Submit')

class Booknow_training(FlaskForm):
    
    name = StringField('Name of Applicant', validators=[DataRequired(), Length(min=1, max=400)])
    address = StringField('Address of Applicant', validators=[DataRequired(), Length(min=1, max=400)])
    phone = StringField('Contactr', validators=[DataRequired(), Length(min=1, max=400)])
    email = StringField('Email id', validators=[DataRequired(), Length(min=1, max=400)])
    block = StringField('Name of the Block', validators=[DataRequired(), Length(min=3, max=400)])
    panchayath = StringField('Name of Panchayath', validators=[DataRequired(), Length(min=1, max=400)])
    aadhar = StringField('Aadhar number', validators=[DataRequired(), Length(min=1, max=400)])
    submit = SubmitField('Submit')

class Soiltest(FlaskForm):
    
    name = StringField('Name of Center', validators=[DataRequired(), Length(min=1, max=400)])
    address = StringField('Address of Center', validators=[DataRequired(), Length(min=1, max=400)])
    contact = StringField('Contact', validators=[DataRequired(), Length(min=1, max=400)])
    day = StringField('Date', validators=[DataRequired(), Length(min=1, max=400)])
    time = StringField('time', validators=[DataRequired(), Length(min=1, max=400)])
    submit = SubmitField('Save')

class Notice(FlaskForm):
    
    subject = StringField('Subject', validators=[DataRequired(), Length(min=1, max=400)])
    details = StringField('Details', validators=[DataRequired(), Length(min=1, max=400)])
    date = StringField('Expired Date', validators=[DataRequired(), Length(min=1, max=400)])
    contactnum = StringField('Contact number', validators=[DataRequired(), Length(min=1, max=400)])
    email = StringField('Email Id', validators=[DataRequired(), Length(min=1, max=400)])
    submit = SubmitField('Save')

class Prmkisan(FlaskForm):
    
    name = StringField('Name', validators=[DataRequired(), Length(min=1, max=400)])
    address = StringField('Address', validators=[DataRequired(), Length(min=1, max=400)])
    gender = StringField('Gender', validators=[DataRequired(), Length(min=3, max=10)])
    dob = StringField('Date of birth', validators=[DataRequired(), Length(min=1, max=400)])
    phone = StringField('Phone Number', validators=[DataRequired(), Length(min=1, max=400)])
    email = StringField('Email id', validators=[DataRequired(), Length(min=1, max=400)])
    block = StringField('Block', validators=[DataRequired(), Length(min=1, max=400)])
    panchayath = StringField('Panchayath', validators=[DataRequired(), Length(min=1, max=400)])
    village = StringField('Village', validators=[DataRequired(), Length(min=1, max=400)])
    bank = StringField('bank', validators=[DataRequired(), Length(min=1, max=400)])
    accountnum = StringField('Account number', validators=[DataRequired(), Length(min=1, max=400)])
    aadharnum = StringField('Aadhar Number', validators=[DataRequired(), Length(min=1, max=400)])
    img = FileField('Uploard the photo of Aadhar', validators=[DataRequired(),FileAllowed(['jpg', 'png','jpeg'])])
    submit = SubmitField('Save')

class Pmk_an(FlaskForm):
    
    name = StringField('Name', validators=[DataRequired(), Length(min=1, max=400)])
    address = StringField('Address', validators=[DataRequired(), Length(min=1, max=400)])
    gender = StringField('Gender', validators=[DataRequired(), Length(min=3, max=10)])
    dob = StringField('Date of birth', validators=[DataRequired(), Length(min=1, max=400)])
    phone = StringField('Phone Number', validators=[DataRequired(), Length(min=1, max=400)])
    email = StringField('Email id', validators=[DataRequired(), Length(min=1, max=400)])
    block = StringField('Block', validators=[DataRequired(), Length(min=1, max=400)])
    panchayath = StringField('Panchayath', validators=[DataRequired(), Length(min=1, max=400)])
    village = StringField('Village', validators=[DataRequired(), Length(min=1, max=400)])
    bank = StringField('bank', validators=[DataRequired(), Length(min=1, max=400)])
    accountnum = StringField('Account number', validators=[DataRequired(), Length(min=1, max=400)])
    aadharnum = StringField('Aadhar Number', validators=[DataRequired(), Length(min=1, max=400)])
    img = FileField('Uploard the photo of Aadhar', validators=[DataRequired(),FileAllowed(['jpg', 'png','jpeg'])])
    submit = SubmitField('Save')


class Pension_reg(FlaskForm):
    
    name = StringField('Name', validators=[DataRequired(), Length(min=1, max=400)])
    farmerid = StringField('Farmer registration id', validators=[DataRequired(), Length(min=1, max=400)])
    address = StringField('Address', validators=[DataRequired(), Length(min=1, max=400)])
    gender = StringField('Gender', validators=[DataRequired(), Length(min=3, max=10)])
    dob = StringField('Date of birth', validators=[DataRequired(), Length(min=1, max=400)])
    phone = StringField('Phone Number', validators=[DataRequired(), Length(min=1, max=400)])
    email = StringField('Email id', validators=[DataRequired(), Length(min=1, max=400)])
    block = StringField('Block', validators=[DataRequired(), Length(min=1, max=400)])
    panchayath = StringField('Panchayath', validators=[DataRequired(), Length(min=1, max=400)])
    village = StringField('Village', validators=[DataRequired(), Length(min=1, max=400)])
    bank = StringField('bank', validators=[DataRequired(), Length(min=1, max=400)])
    accountnum = StringField('Account number', validators=[DataRequired(), Length(min=1, max=400)])
    aadharnum = StringField('Aadhar Number', validators=[DataRequired(), Length(min=1, max=400)])
    img = FileField('Uploard the photo of Aadhar', validators=[DataRequired(),FileAllowed(['jpg', 'png','jpeg'])])
    submit = SubmitField('Save')

class An_pension(FlaskForm):
    
    name = StringField('Name', validators=[DataRequired(), Length(min=1, max=400)])
    farmerid = StringField('Farmer registration id', validators=[DataRequired(), Length(min=1, max=400)])
    address = StringField('Address', validators=[DataRequired(), Length(min=1, max=400)])
    gender = StringField('Gender', validators=[DataRequired(), Length(min=3, max=10)])
    dob = StringField('Date of birth', validators=[DataRequired(), Length(min=1, max=400)])
    phone = StringField('Phone Number', validators=[DataRequired(), Length(min=1, max=400)])
    email = StringField('Email id', validators=[DataRequired(), Length(min=1, max=400)])
    block = StringField('Block', validators=[DataRequired(), Length(min=1, max=400)])
    panchayath = StringField('Panchayath', validators=[DataRequired(), Length(min=1, max=400)])
    village = StringField('Village', validators=[DataRequired(), Length(min=1, max=400)])
    bank = StringField('bank', validators=[DataRequired(), Length(min=1, max=400)])
    accountnum = StringField('Account number', validators=[DataRequired(), Length(min=1, max=400)])
    aadharnum = StringField('Aadhar Number', validators=[DataRequired(), Length(min=1, max=400)])
    img = FileField('Uploard the photo of Aadhar', validators=[DataRequired(),FileAllowed(['jpg', 'png','jpeg'])])
    submit = SubmitField('Save')


class Pmfasal(FlaskForm):
    
    name = StringField('Name', validators=[DataRequired(), Length(min=1, max=400)])
    address = StringField('Address', validators=[DataRequired(), Length(min=1, max=400)])
    gender = StringField('Gender', validators=[DataRequired(), Length(min=3, max=10)])
    dob = StringField('Date of birth', validators=[DataRequired(), Length(min=1, max=400)])
    phone = StringField('Phone Number', validators=[DataRequired(), Length(min=1, max=400)])
    email = StringField('Email id', validators=[DataRequired(), Length(min=1, max=400)])
    block = StringField('Block', validators=[DataRequired(), Length(min=1, max=400)])
    panchayath = StringField('Panchayath', validators=[DataRequired(), Length(min=1, max=400)])
    village = StringField('Village', validators=[DataRequired(), Length(min=1, max=400)])
    bank = StringField('bank', validators=[DataRequired(), Length(min=1, max=400)])
    accountnum = StringField('Account number', validators=[DataRequired(), Length(min=1, max=400)])
    aadharnum = StringField('Aadhar Number', validators=[DataRequired(), Length(min=1, max=400)])
    img = FileField('Uploard the photo of Aadhar', validators=[DataRequired(),FileAllowed(['jpg', 'png','jpeg'])])
    submit = SubmitField('Save')

class Polyhouse_reg(FlaskForm):
    
    name = StringField('Name', validators=[DataRequired(), Length(min=1, max=400)])
    address = StringField('Address', validators=[DataRequired(), Length(min=1, max=400)])
    gender = StringField('Gender', validators=[DataRequired(), Length(min=3, max=10)])
    dob = StringField('Date of birth', validators=[DataRequired(), Length(min=1, max=400)])
    phone = StringField('Phone Number', validators=[DataRequired(), Length(min=1, max=400)])
    email = StringField('Email id', validators=[DataRequired(), Length(min=1, max=400)])
    block = StringField('Block', validators=[DataRequired(), Length(min=1, max=400)])
    panchayath = StringField('Panchayath', validators=[DataRequired(), Length(min=1, max=400)])
    village = StringField('Village', validators=[DataRequired(), Length(min=1, max=400)])
    bank = StringField('bank', validators=[DataRequired(), Length(min=1, max=400)])
    accountnum = StringField('Account number', validators=[DataRequired(), Length(min=1, max=400)])
    aadharnum = StringField('Aadhar Number', validators=[DataRequired(), Length(min=1, max=400)])
    rationnum = StringField('Ration Card Number', validators=[DataRequired(), Length(min=1, max=400)])
    area = StringField('Total Area for Polyhouse ', validators=[DataRequired(), Length(min=1, max=400)])
    spented = StringField('Total Amount Spented for Polyhouse', validators=[DataRequired(), Length(min=1, max=400)])
    img = FileField('Upload the photo of Polyhouse', validators=[DataRequired(),FileAllowed(['jpg', 'png','jpeg'])])
    submit = SubmitField('Save')

class Electricity_conn(FlaskForm):
    
    name = StringField('Name', validators=[DataRequired(), Length(min=1, max=400)])
    address = StringField('Address', validators=[DataRequired(), Length(min=1, max=400)])
    gender = StringField('Gender', validators=[DataRequired(), Length(min=3, max=10)])
    dob = StringField('Date of birth', validators=[DataRequired(), Length(min=1, max=400)])
    phone = StringField('Phone Number', validators=[DataRequired(), Length(min=1, max=400)])
    email = StringField('Email id', validators=[DataRequired(), Length(min=1, max=400)])
    block = StringField('Block', validators=[DataRequired(), Length(min=1, max=400)])
    panchayath = StringField('Panchayath', validators=[DataRequired(), Length(min=1, max=400)])
    village = StringField('Village', validators=[DataRequired(), Length(min=1, max=400)])
    bank = StringField('bank', validators=[DataRequired(), Length(min=1, max=400)])
    accountnum = StringField('Account number', validators=[DataRequired(), Length(min=1, max=400)])
    aadharnum = StringField('Aadhar Number', validators=[DataRequired(), Length(min=1, max=400)])
    connid = StringField('Electricity Connection Id ', validators=[DataRequired(), Length(min=1, max=400)])
    spented = StringField('Total Amount Spented for Connection ', validators=[DataRequired(), Length(min=1, max=400)])
    img = FileField('Upload the photo of Aadhar', validators=[DataRequired(),FileAllowed(['jpg', 'png','jpeg'])])
    submit = SubmitField('Save')

class Livestockm(FlaskForm):
    
    name = StringField('Name', validators=[DataRequired(), Length(min=1, max=400)])
    address = StringField('Address', validators=[DataRequired(), Length(min=1, max=400)])
    gender = StringField('Gender', validators=[DataRequired(), Length(min=3, max=10)])
    dob = StringField('Date of birth', validators=[DataRequired(), Length(min=1, max=400)])
    phone = StringField('Phone Number', validators=[DataRequired(), Length(min=1, max=400)])
    email = StringField('Email id', validators=[DataRequired(), Length(min=1, max=400)])
    block = StringField('Block', validators=[DataRequired(), Length(min=1, max=400)])
    panchayath = StringField('Panchayath', validators=[DataRequired(), Length(min=1, max=400)])
    village = StringField('Village', validators=[DataRequired(), Length(min=1, max=400)])
    bank = StringField('bank', validators=[DataRequired(), Length(min=1, max=400)])
    accountnum = StringField('Account number', validators=[DataRequired(), Length(min=1, max=400)])
    aadharnum = StringField('Aadhar Number', validators=[DataRequired(), Length(min=1, max=400)])
    rationnum = StringField('Ration Card Number', validators=[DataRequired(), Length(min=1, max=400)])
    animaltype = StringField('Type of animal', validators=[DataRequired(), Length(min=1, max=400)])
    animalnum = StringField('Number of animal', validators=[DataRequired(), Length(min=1, max=400)])
    img = FileField('Uploard the photo of Animalfarm', validators=[DataRequired(),FileAllowed(['jpg', 'png','jpeg'])])
    submit = SubmitField('Save')


class Crore_one(FlaskForm):
    
    name = StringField('Name', validators=[DataRequired(), Length(min=1, max=400)])
    address = StringField('Address', validators=[DataRequired(), Length(min=1, max=400)])
    gender = StringField('Gender', validators=[DataRequired(), Length(min=3, max=10)])
    dob = StringField('Date of birth', validators=[DataRequired(), Length(min=1, max=400)])
    phone = StringField('Phone Number', validators=[DataRequired(), Length(min=1, max=400)])
    email = StringField('Email id', validators=[DataRequired(), Length(min=1, max=400)])
    block = StringField('Block', validators=[DataRequired(), Length(min=1, max=400)])
    panchayath = StringField('Panchayath', validators=[DataRequired(), Length(min=1, max=400)])
    village = StringField('Village', validators=[DataRequired(), Length(min=1, max=400)])
    aadharnum = StringField('Aadhar number', validators=[DataRequired(), Length(min=1, max=400)])
    area = StringField('Total Area', validators=[DataRequired(), Length(min=1, max=400)])
    cropname = StringField('Plant name', validators=[DataRequired(), Length(min=1, max=400)])
    cropnum = StringField('Number of plants for plant', validators=[DataRequired(), Length(min=1, max=400)])
    img = FileField('Uploard the photo of Aadhar', validators=[DataRequired(),FileAllowed(['jpg', 'png','jpeg'])])
    submit = SubmitField('Save')


class Bamboor(FlaskForm):
    
    name = StringField('Name', validators=[DataRequired(), Length(min=1, max=400)])
    address = StringField('Address', validators=[DataRequired(), Length(min=1, max=400)])
    gender = StringField('Gender', validators=[DataRequired(), Length(min=3, max=10)])
    dob = StringField('Date of birth', validators=[DataRequired(), Length(min=1, max=400)])
    phone = StringField('Phone Number', validators=[DataRequired(), Length(min=1, max=400)])
    email = StringField('Email id', validators=[DataRequired(), Length(min=1, max=400)])
    block = StringField('Block', validators=[DataRequired(), Length(min=1, max=400)])
    panchayath = StringField('Panchayath', validators=[DataRequired(), Length(min=1, max=400)])
    village = StringField('Village', validators=[DataRequired(), Length(min=1, max=400)])
    aadharnum = StringField('Aadhar number', validators=[DataRequired(), Length(min=1, max=400)])
    area = StringField('Total Area', validators=[DataRequired(), Length(min=1, max=400)])
    img = FileField('Uploard the photo of Aadhar', validators=[DataRequired(),FileAllowed(['jpg', 'png','jpeg'])])
    submit = SubmitField('Save')


class Prodadd(FlaskForm):
    
    productname = StringField('Product Name', validators=[DataRequired(), Length(min=1, max=400)])
    productcat = StringField('Product Category', validators=[DataRequired(), Length(min=1, max=400)])
    features = StringField('Features', validators=[DataRequired(), Length(min=1, max=400)])
    price = StringField('Price', validators=[DataRequired(), Length(min=1, max=100)])
    contactnum = StringField('Contact Number', validators=[DataRequired(), Length(min=1, max=10)])
    pic = FileField('Uploard your photo', validators=[DataRequired(),FileAllowed(['jpg', 'png','jpeg'])])
    submit = SubmitField('Save')

class Rentmachine(FlaskForm):
    
    productname = StringField('Name of Machine', validators=[DataRequired(), Length(min=1, max=400)])
    brant = StringField('Brant of Machine', validators=[DataRequired(), Length(min=1, max=400)])
    rentrupee = StringField('Rent Amount', validators=[DataRequired(), Length(min=1, max=100)])
    features = StringField('Features', validators=[DataRequired(), Length(min=1, max=400)]) 
    contactnum = StringField('Contact Number', validators=[DataRequired(), Length(min=1, max=10)])
    pic = FileField('Uploard your photo', validators=[DataRequired(),FileAllowed(['jpg', 'png','jpeg'])])
    submit = SubmitField('Save')

class Eventadd(FlaskForm):
    
    eventname = StringField('Event Name', validators=[DataRequired(), Length(min=1, max=400)])
    description = StringField('Description', validators=[DataRequired(), Length(min=1, max=400)])
    date = StringField('Date', validators=[DataRequired(), Length(min=1, max=400)])
    time = StringField('Time', validators=[DataRequired(), Length(min=1, max=100)])
    place = StringField('Place', validators=[DataRequired(), Length(min=1, max=100)])
    contactnum = StringField('Contact Number', validators=[DataRequired(), Length(min=1, max=10)])
    pic = FileField('Uploard  photo', validators=[DataRequired(),FileAllowed(['jpg', 'png','jpeg'])])
    submit = SubmitField('Save')

class Formloan(FlaskForm):
    
    name = StringField('Name', validators=[DataRequired(), Length(min=1, max=400)])
    address = StringField('Address', validators=[DataRequired(), Length(min=1, max=400)])
    gender = StringField('Gender', validators=[DataRequired(), Length(min=3, max=10)])
    dob = StringField('Date of birth', validators=[DataRequired(), Length(min=1, max=400)])
    phone = StringField('Phone Number', validators=[DataRequired(), Length(min=1, max=400)])
    email = StringField('Email id', validators=[DataRequired(), Length(min=1, max=400)])
    block = StringField('Block', validators=[DataRequired(), Length(min=1, max=400)])
    panchayath = StringField('Panchayath', validators=[DataRequired(), Length(min=1, max=400)])
    village = StringField('Village', validators=[DataRequired(), Length(min=1, max=400)])
    bank = StringField('bank', validators=[DataRequired(), Length(min=1, max=400)])
    accountnum = StringField('Account number', validators=[DataRequired(), Length(min=1, max=400)])
    aadharnum = StringField('Aadhar Number', validators=[DataRequired(), Length(min=1, max=400)])
    rationnum = StringField('Ration Card Number', validators=[DataRequired(), Length(min=1, max=400)])
    area = StringField('Total area of field', validators=[DataRequired(), Length(min=1, max=400)])
    projtopic = StringField('Name of Project', validators=[DataRequired(), Length(min=1, max=400)])
    projdisc = StringField('Discription about your Project', validators=[DataRequired(), Length(min=1, max=400)])
    img = FileField('Uploard the photo of Aadhar', validators=[DataRequired(),FileAllowed(['jpg', 'png','jpeg'])])
    submit = SubmitField('Save')


class Loan_animals(FlaskForm):
    
    name = StringField('Name', validators=[DataRequired(), Length(min=1, max=400)])
    address = StringField('Address', validators=[DataRequired(), Length(min=1, max=400)])
    gender = StringField('Gender', validators=[DataRequired(), Length(min=3, max=10)])
    dob = StringField('Date of birth', validators=[DataRequired(), Length(min=1, max=400)])
    phone = StringField('Phone Number', validators=[DataRequired(), Length(min=1, max=400)])
    email = StringField('Email id', validators=[DataRequired(), Length(min=1, max=400)])
    block = StringField('Block', validators=[DataRequired(), Length(min=1, max=400)])
    panchayath = StringField('Panchayath', validators=[DataRequired(), Length(min=1, max=400)])
    village = StringField('Village', validators=[DataRequired(), Length(min=1, max=400)])
    bank = StringField('bank', validators=[DataRequired(), Length(min=1, max=400)])
    accountnum = StringField('Account number', validators=[DataRequired(), Length(min=1, max=400)])
    aadharnum = StringField('Aadhar Number', validators=[DataRequired(), Length(min=1, max=400)])
    rationnum = StringField('Ration Card Number', validators=[DataRequired(), Length(min=1, max=400)])
    area = StringField('Total area of field', validators=[DataRequired(), Length(min=1, max=400)])
    projtopic = StringField('Name of Project', validators=[DataRequired(), Length(min=1, max=400)])
    projdisc = StringField('Discription about your Project', validators=[DataRequired(), Length(min=1, max=400)])
    img = FileField('Uploard the photo of Aadhar', validators=[DataRequired(),FileAllowed(['jpg', 'png','jpeg'])])
    submit = SubmitField('Save')
