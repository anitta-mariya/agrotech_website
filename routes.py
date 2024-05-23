import os
from flask import Flask,render_template,redirect,request,abort,url_for,flash
from agrotech import app,db,crypt
from agrotech.forms import LoginForm,Staffreg,Prodadd,Eventadd,Rentmachine,Notice,Fertilizers,Booknow,Booknowmac,Booknow_training,An_pension,Pmk_an,Anfarmerreg,Formloan,Cows,Goats,Hens,Regshm,Loan_animals,Add_magazine,Electricity_conn,Farmer_regist,Crore_one,Crop_insur,Machinaries,Livestockm,Pension_reg,Polyhouse_reg,Prmkisan,Addcart,Calamity_reg,Soilhealth,Pmfasal,Trainingcent,Soiltest,Bamboor
from agrotech.models import *
from flask import Markup
from random import randint
from datetime import date
from PIL import Image
from datetime import datetime
from flask_login import login_user, current_user, logout_user, login_required



@app.route('/adminlog',methods=['POST','GET'])
def adminlog():
    if current_user.is_authenticated:
        logout_user()
        return redirect('/')                                           
    form = LoginForm()
    if form.validate_on_submit():
        far = Login.query.filter_by(email=form.email.data,usertype='far').first()
        animalfar = Login.query.filter_by(email=form.email.data,usertype='animalfar').first()
        staff = Login.query.filter_by(email=form.email.data,usertype='staff').first()
        admin = Login.query.filter_by(email=form.email.data, usertype='admin').first()
        

        if far and far.password== form.password.data:
            login_user(far, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect('/f_layout')

        if animalfar and animalfar.password== form.password.data:
            login_user(animalfar, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect('/an_layout')
            
        if staff and staff.password== form.password.data:
            login_user(staff, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect('/s_layout')
            

        if admin and admin.password == form.password.data:
            login_user(admin, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect('/ad_layout')
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')      
    return render_template('adminlog.html',title='Login', form=form)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/new')
def new():
    return render_template('new.html')


@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/start')
def start():
    return render_template('start.html')


@app.route('/training_add',methods=['POST','GET'])
def training_add():
    form=Trainingcent()
    view="default.jpg"
    if form.validate_on_submit():
        print(view)
        gallery = Addtraining(name=form.name.data,address=form.address.data,programer=form.programer.data,contact=form.contact.data,date=form.date.data,time=form.time.data,topic=form.topic.data)
        db.session.add(gallery)
        db.session.commit()
        print(gallery)
        flash('image added')
        return redirect('/training_add')
    return render_template('training_add.html',form=form)

@app.route('/booking_train',methods=['POST','GET'])
def booking_train():
    form=Booking()
    view="default.jpg"
    if form.validate_on_submit():
        print(view)
        gallery = Booking_train(name=form.name.data,address=form.address.data,contact=form.contact.data,topic=form.topic.data,date=form.date.data,time=form.time.data)
        db.session.add(gallery)
        db.session.commit()
        print(gallery)
        flash('image added')
        return redirect('/booking_train')
    return render_template('booking_train.html',form=form)



@app.route('/training_cen')
def training_cen():
    return render_template('training_cen.html')



@app.route('/gallery')
def gallery():
    return render_template('gallery.html')



@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/contact',methods=['POST','GET'])
def contact():
    if request.method=='POST':
        fname=request.form['name']
        emailid=request.form['email']
        phone=request.form['number']
        msg=request.form['message']
    

    try:
        contact=Contact(name=fname,email=emailid,phone=phone,message=msg)
        db.session.add(contact)
        db.session.commit()
        message=Markup("*****successfully inserted*****")
        flash(message)
        return redirect('/contact')
    except Exception as e:
        print(e)
    return render_template('contact.html')



@app.route('/layout')
def layout():
    return render_template('layout.html')

@app.route('/anlayout')
def anlayout():
    return render_template('anlayout.html')

@app.route("/logout")
def logout():
    logout_user()
    return redirect('/adminlog')

@app.route('/regstaff',methods=['POST','GET'])
def regstaff():
    Pap = Regstaff.query.all()
    form=Staffreg()
    view="default.jpg"
    if form.validate_on_submit():
        if form.pic.data:
            pic_file = save_picture(form.pic.data)
            view = pic_file
        print(view)
        gallery = Regstaff(fname=form.fname.data,sname=form.sname.data,address=form.address.data,gender=form.gender.data,phone=form.phone.data,district=form.district.data,position=form.position.data,email=form.email.data,password=form.password.data,img=view)
        a=Login(email=form.email.data,password=form.password.data,usertype='staff')
        db.session.add(gallery)
        db.session.add(a)
        db.session.commit()
        print(gallery)
        flash('image added')
        return redirect('/regstaff')
    return render_template('regstaff.html',form=form,Pap=Pap)

@app.route('/regfarmer',methods=['POST','GET'])
def regfarmer():
   if request.method=='POST':
        name=request.form['name']
        address=request.form['address']
        gender=request.form['gender']
        email=request.form['email']
        phone=request.form['phone']
        password=request.form['password']
        
   try:
        regfarmer=Regfarmer(name=name,address=address,gender=gender,email=email,phone=phone,password=password)
        a=Login(email=email,password=password,usertype='far')
        db.session.add(regfarmer)
        db.session.add(a)
        db.session.commit()
        message=Markup("*****successfully inserted*****")
        flash(message)
        return redirect('/adminlog')
   except Exception as e:
        print(e)
   return render_template('regfarmer.html')

@app.route('/animalsect_reg',methods=['POST','GET'])
def animalsect_reg():
   if request.method=='POST':
        name=request.form['name']
        address=request.form['address']
        gender=request.form['gender']
        email=request.form['email']
        phone=request.form['phone']
        password=request.form['password']
        
   try:
        animalsect_reg=Animalfarmer(name=name,address=address,gender=gender,email=email,phone=phone,password=password)
        a=Login(email=email,password=password,usertype='animalfar')
        db.session.add(animalsect_reg)
        db.session.add(a)
        db.session.commit()
        message=Markup("*****successfully inserted*****")
        flash(message)
        return redirect('/adminlog')
   except Exception as e:
        print(e)
   return render_template('animalsect_reg.html')


@app.route('/regstaffdele/<int:id>')
def regstaffdele(id):
    upcus = Regstaff.query.get_or_404(id)
    try:
        db.session.delete(upcus)
        db.session.commit()
        return redirect('/regstaff')
    except:
        return 'NOT committed'

@app.route('/adm_calamitydele/<int:id>')
def adm_calamitydele(id):
    upcus = Calamity.query.get_or_404(id)
    try:
        db.session.delete(upcus)
        db.session.commit()
        return redirect('/adview_calamity')
    except:
        return 'NOT committed'

@app.route('/adm_bamboodele/<int:id>')
def adm_bamboodele(id):
    upcus = Bamboo_reg.query.get_or_404(id)
    try:
        db.session.delete(upcus)
        db.session.commit()
        return redirect('/adview_bamboo')
    except:
        return 'NOT committed'

@app.route('/adm_cowdele/<int:id>')
def adm_cowdele(id):
    upcus = Cowdairy.query.get_or_404(id)
    try:
        db.session.delete(upcus)
        db.session.commit()
        return redirect('/adview_cow')
    except:
        return 'NOT committed'

@app.route('/adm_electdele/<int:id>')
def adm_electdele(id):
    upcus = Electricity.query.get_or_404(id)
    try:
        db.session.delete(upcus)
        db.session.commit()
        return redirect('/adview_elect')
    except:
        return 'NOT committed'

@app.route('/adm_farmerregdele/<int:id>')
def adm_farmerregdele(id):
    upcus = Farmerreg.query.get_or_404(id)
    try:
        db.session.delete(upcus)
        db.session.commit()
        return redirect('/adview_farmerreg')
    except:
        return 'NOT committed'

@app.route('/adm_farmerregandele/<int:id>')
def adm_farmerregandele(id):
    upcus = An_farmerreg.query.get_or_404(id)
    try:
        db.session.delete(upcus)
        db.session.commit()
        return redirect('/adview_farmerregan')
    except:
        return 'NOT committed'


@app.route('/adm_fasaldele/<int:id>')
def adm_fasaldele(id):
    upcus = Pm_fasal.query.get_or_404(id)
    try:
        db.session.delete(upcus)
        db.session.commit()
        return redirect('/adview_fasal')
    except:
        return 'NOT committed'

@app.route('/adm_fertidele/<int:id>')
def adm_fertidele(id):
    upcus = Fertiliz.query.get_or_404(id)
    try:
        db.session.delete(upcus)
        db.session.commit()
        return redirect('/adview_ferti')
    except:
        return 'NOT committed'


@app.route('/adm_goatgdele/<int:id>')
def adm_goatdele(id):
    upcus = Goatfarm.query.get_or_404(id)
    try:
        db.session.delete(upcus)
        db.session.commit()
        return redirect('/adview_goat')
    except:
        return 'NOT committed'


@app.route('/adm_hendele/<int:id>')
def adm_hendele(id):
    upcus = Hfarm.query.get_or_404(id)
    try:
        db.session.delete(upcus)
        db.session.commit()
        return redirect('/adview_hen')
    except:
        return 'NOT committed'


@app.route('/adm_livestockdele/<int:id>')
def adm_livestockdele(id):
    upcus = Livestock.query.get_or_404(id)
    try:
        db.session.delete(upcus)
        db.session.commit()
        return redirect('/adview_livestock')
    except:
        return 'NOT committed'
    

@app.route('/adm_loanagridele/<int:id>')
def adm_loanagridele(id):
    upcus = Loanform.query.get_or_404(id)
    try:
        db.session.delete(upcus)
        db.session.commit()
        return redirect('/adview_loanagri')
    except:
        return 'NOT committed'    


@app.route('/adm_loananimaldele/<int:id>')
def adm_loananimaldele(id):
    upcus = loananimal.query.get_or_404(id)
    try:
        db.session.delete(upcus)
        db.session.commit()
        return redirect('/adview_loananimal')
    except:
        return 'NOT committed'


@app.route('/adm_machinedele/<int:id>')
def adm_machinedele(id):
    upcus = Machines.query.get_or_404(id)
    try:
        db.session.delete(upcus)
        db.session.commit()
        return redirect('/adview_machine')
    except:
        return 'NOT committed'  


@app.route('/adm_onecroredele/<int:id>')
def adm_onecroredele(id):
    upcus = One_crore.query.get_or_404(id)
    try:
        db.session.delete(upcus)
        db.session.commit()
        return redirect('/adview_onecrore')
    except:
        return 'NOT committed'  

@app.route('/adm_pensiondele/<int:id>')
def adm_pensiondele(id):
    upcus = Pension.query.get_or_404(id)
    try:
        db.session.delete(upcus)
        db.session.commit()
        return redirect('/adview_pension')
    except:
        return 'NOT committed'

@app.route('/adm_pensionandele/<int:id>')
def adm_pensionandele(id):
    upcus = Pension_an.query.get_or_404(id)
    try:
        db.session.delete(upcus)
        db.session.commit()
        return redirect('/adview_pensionan')
    except:
        return 'NOT committed'

@app.route('/adm_pmkdele/<int:id>')
def adm_pmkdele(id):
    upcus = Pmkisan.query.get_or_404(id)
    try:
        db.session.delete(upcus)
        db.session.commit()
        return redirect('/adview_pmk')
    except:
        return 'NOT committed'      

@app.route('/adm_pmkandele/<int:id>')
def adm_pmkandele(id):
    upcus = An_pmk.query.get_or_404(id)
    try:
        db.session.delete(upcus)
        db.session.commit()
        return redirect('/adview_pmkan')
    except:
        return 'NOT committed'

@app.route('/adm_polyhousedele/<int:id>')
def adm_polyhousedele(id):
    upcus = Polyhouse.query.get_or_404(id)
    try:
        db.session.delete(upcus)
        db.session.commit()
        return redirect('/adview_polyhouse')
    except:
        return 'NOT committed'  


@app.route('/adm_shmdele/<int:id>')
def adm_shmdele(id):
    upcus = Shmreg.query.get_or_404(id)
    try:
        db.session.delete(upcus)
        db.session.commit()
        return redirect('/adview_shm')
    except:
        return 'NOT committed'


@app.route('/adm_soildele/<int:id>')
def adm_soildele(id):
    upcus = Soil_health.query.get_or_404(id)
    try:
        db.session.delete(upcus)
        db.session.commit()
        return redirect('/adview_soilhealth')
    except:
        return 'NOT committed'

@app.route('/shmreeg',methods=['POST','GET'])
def shmreeg():
    form=Regshm()
    view="default.jpg"
    if form.validate_on_submit():
        if form.img.data:
            pic_file = save_picture(form.img.data)
            view = pic_file
        print(view)
        gallery = Shmreg(name=form.name.data,address=form.address.data,gender=form.gender.data,dob=form.dob.data,phone=form.phone.data,email=form.email.data,block=form.block.data,panchayath=form.panchayath.data,village=form.village.data,bank=form.bank.data,accountnum=form.accountnum.data,area=form.area.data,cropname=form.cropname.data,img=view)
        db.session.add(gallery)
        db.session.commit()
        print(gallery)
        flash('image added')
        return redirect('/shmreeg')
    return render_template('shmreeg.html',form=form)


@app.route('/soilt_booknow',methods=['POST','GET'])
def soilt_booknow():
    form=Booknow()
    view="default.jpg"
    if form.validate_on_submit():
        print(view)
        gallery = Soilbooknow(name=form.name.data,address=form.address.data,phone=form.phone.data,email=form.email.data,block=form.block.data,panchayath=form.panchayath.data,aadhar=form.aadhar.data)
        db.session.add(gallery)
        db.session.commit()
        print(gallery)
        flash('image added')
        return redirect('/view_soiltest')
    return render_template('soilt_booknow.html',form=form)

@app.route('/mac_booknow',methods=['POST','GET'])
def mac_booknow():
    form=Booknow()
    view="default.jpg"
    if form.validate_on_submit():
        print(view)
        gallery = Machinebooknow(name=form.name.data,address=form.address.data,phone=form.phone.data,email=form.email.data,block=form.block.data,panchayath=form.panchayath.data,aadhar=form.aadhar.data)
        db.session.add(gallery)
        db.session.commit()
        print(gallery)
        flash('image added')
        return redirect('/mac_booknow')
    return render_template('mac_booknow.html',form=form)


@app.route('/booknow_training',methods=['POST','GET'])
def booknow_training():
    form=Booknow_training()
    view="default.jpg"
    if form.validate_on_submit():
        print(view)
        gallery = Trainingbooking(name=form.name.data,address=form.address.data,phone=form.phone.data,email=form.email.data,block=form.block.data,panchayath=form.panchayath.data,aadhar=form.aadhar.data)
        db.session.add(gallery)
        db.session.commit()
        print(gallery)
        flash('image added')
        return redirect('/booknow_training')
    return render_template('booknow_training.html',form=form)

@app.route('/booknow_training_an',methods=['POST','GET'])
def booknow_training_an():
    form=Booknow_training()
    view="default.jpg"
    if form.validate_on_submit():
        print(view)
        gallery = Trainingbooking(name=form.name.data,address=form.address.data,phone=form.phone.data,email=form.email.data,block=form.block.data,panchayath=form.panchayath.data,aadhar=form.aadhar.data)
        db.session.add(gallery)
        db.session.commit()
        print(gallery)
        flash('image added')
        return redirect('/booknow_training_an')
    return render_template('booknow_training_an.html',form=form)



@app.route('/farmerreg',methods=['POST','GET'])
def farmerreg():
    form=Farmer_regist()
    view="default.jpg"
    if form.validate_on_submit():
        if form.img.data:
            pic_file = save_picture(form.img.data)
            view = pic_file
        print(view)
        gallery = Farmerreg(name=form.name.data,address=form.address.data,gender=form.gender.data,dob=form.dob.data,phone=form.phone.data,email=form.email.data,block=form.block.data,panchayath=form.panchayath.data,village=form.village.data,bank=form.bank.data,accountnum=form.accountnum.data,aadharnum=form.aadharnum.data,rationnum=form.rationnum.data,area=form.area.data,img=view)
        db.session.add(gallery)
        db.session.commit()
        print(gallery)
        flash('image added')
        return redirect('/farmerreg')
    return render_template('farmerreg.html',form=form)

@app.route('/farmerreg_an',methods=['POST','GET'])
def farmerreg_an():
    form=Anfarmerreg()
    view="default.jpg"
    if form.validate_on_submit():
        if form.img.data:
            pic_file = save_picture(form.img.data)
            view = pic_file
        print(view)
        gallery = An_farmerreg(name=form.name.data,address=form.address.data,gender=form.gender.data,dob=form.dob.data,phone=form.phone.data,email=form.email.data,block=form.block.data,panchayath=form.panchayath.data,village=form.village.data,bank=form.bank.data,accountnum=form.accountnum.data,aadharnum=form.aadharnum.data,rationnum=form.rationnum.data,area=form.area.data,img=view)
        db.session.add(gallery)
        db.session.commit()
        print(gallery)
        flash('image added')
        return redirect('/farmerreg_an')
    return render_template('farmerreg_an.html',form=form)


@app.route('/machines',methods=['POST','GET'])
def machines():
    form=Machinaries()
    view="default.jpg"
    if form.validate_on_submit():
        if form.img.data:
            pic_file = save_picture(form.img.data)
            view = pic_file
        print(view)
        gallery = Machines(name=form.name.data,address=form.address.data,gender=form.gender.data,dob=form.dob.data,phone=form.phone.data,email=form.email.data,block=form.block.data,panchayath=form.panchayath.data,village=form.village.data,bank=form.bank.data,accountnum=form.accountnum.data,aadharnum=form.aadharnum.data,rationnum=form.rationnum.data,area=form.area.data,machines=form.machines.data,img=view)
        db.session.add(gallery)
        db.session.commit()
        print(gallery)
        flash('image added')
        return redirect('/machines')
    return render_template('machines.html',form=form)

@app.route('/fertilizers',methods=['POST','GET'])
def fertilizers():
    form=Fertilizers()
    view="default.jpg"
    if form.validate_on_submit():
        if form.img.data:
            pic_file = save_picture(form.img.data)
            view = pic_file
        print(view)
        gallery = Fertiliz(name=form.name.data,address=form.address.data,gender=form.gender.data,dob=form.dob.data,phone=form.phone.data,email=form.email.data,block=form.block.data,panchayath=form.panchayath.data,village=form.village.data,bank=form.bank.data,accountnum=form.accountnum.data,aadharnum=form.aadharnum.data,rationnum=form.rationnum.data,category=form.category.data,farmerid=form.farmerid.data,img=view)
        db.session.add(gallery)
        db.session.commit()
        print(gallery)
        flash('image added')
        return redirect('/fertilizers')
    return render_template('fertilizers.html',form=form)

@app.route('/cow',methods=['POST','GET'])
def cow():
    form=Cows()
    view="default.jpg"
    if form.validate_on_submit():
        if form.img.data:
            pic_file = save_picture(form.img.data)
            view = pic_file
        print(view)
        gallery = Cowdairy(name=form.name.data,address=form.address.data,gender=form.gender.data,dob=form.dob.data,phone=form.phone.data,email=form.email.data,block=form.block.data,panchayath=form.panchayath.data,village=form.village.data,bank=form.bank.data,accountnum=form.accountnum.data,aadharnum=form.aadharnum.data,rationnum=form.rationnum.data,cowsnum=form.cowsnum.data,ctype=form.ctype.data,category=form.category.data,farmerid=form.farmerid.data,img=view)
        db.session.add(gallery)
        db.session.commit()
        print(gallery)
        flash('image added')
        return redirect('/cow')
    return render_template('cow.html',form=form)

@app.route('/goat',methods=['POST','GET'])
def goat():
    form=Goats()
    view="default.jpg"
    if form.validate_on_submit():
        if form.img.data:
            pic_file = save_picture(form.img.data)
            view = pic_file
        print(view)
        gallery = Goatfarm(name=form.name.data,address=form.address.data,gender=form.gender.data,dob=form.dob.data,phone=form.phone.data,email=form.email.data,block=form.block.data,panchayath=form.panchayath.data,village=form.village.data,bank=form.bank.data,accountnum=form.accountnum.data,aadharnum=form.aadharnum.data,rationnum=form.rationnum.data,goatnum=form.goatnum.data,gtype=form.gtype.data,category=form.category.data,farmerid=form.farmerid.data,img=view)
        db.session.add(gallery)
        db.session.commit()
        print(gallery)
        flash('image added')
        return redirect('/goat')
    return render_template('goat.html',form=form)

@app.route('/hen',methods=['POST','GET'])
def hen():
    form=Hens()
    view="default.jpg"
    if form.validate_on_submit():
        if form.img.data:
            pic_file = save_picture(form.img.data)
            view = pic_file
        print(view)
        gallery = Hfarm(name=form.name.data,address=form.address.data,gender=form.gender.data,dob=form.dob.data,phone=form.phone.data,email=form.email.data,block=form.block.data,panchayath=form.panchayath.data,village=form.village.data,bank=form.bank.data,accountnum=form.accountnum.data,aadharnum=form.aadharnum.data,rationnum=form.rationnum.data,num=form.num.data,htype=form.htype.data,category=form.category.data,farmerid=form.farmerid.data,img=view)
        db.session.add(gallery)
        db.session.commit()
        print(gallery)
        flash('image added')
        return redirect('/hen')
    return render_template('hen.html',form=form)





@app.route('/polyhouse',methods=['POST','GET'])
def polyhouse():
    form=Polyhouse_reg()
    view="default.jpg"
    if form.validate_on_submit():
        if form.img.data:
            pic_file = save_picture(form.img.data)
            view = pic_file
        print(view)
        gallery = Polyhouse(name=form.name.data,address=form.address.data,gender=form.gender.data,dob=form.dob.data,phone=form.phone.data,email=form.email.data,block=form.block.data,panchayath=form.panchayath.data,village=form.village.data,bank=form.bank.data,accountnum=form.accountnum.data,aadharnum=form.aadharnum.data,rationnum=form.rationnum.data,area=form.area.data,spented=form.spented.data,img=view)
        db.session.add(gallery)
        db.session.commit()
        print(gallery)
        flash('image added')
        return redirect('/polyhouse')
    return render_template('polyhouse.html',form=form)

@app.route('/electricity',methods=['POST','GET'])
def electricity():
    form=Electricity_conn()
    view="default.jpg"
    if form.validate_on_submit():
        if form.img.data:
            pic_file = save_picture(form.img.data)
            view = pic_file
        print(view)
        gallery = Electricity(name=form.name.data,address=form.address.data,gender=form.gender.data,dob=form.dob.data,phone=form.phone.data,email=form.email.data,block=form.block.data,panchayath=form.panchayath.data,village=form.village.data,bank=form.bank.data,accountnum=form.accountnum.data,aadharnum=form.aadharnum.data,connid=form.connid.data,spented=form.spented.data,img=view)
        db.session.add(gallery)
        db.session.commit()
        print(gallery)
        flash('image added')
        return redirect('/electricity')
    return render_template('electricity.html',form=form)





@app.route('/livestock',methods=['POST','GET'])
def livestock():
    form=Livestockm()
    view="default.jpg"
    if form.validate_on_submit():
        if form.img.data:
            pic_file = save_picture(form.img.data)
            view = pic_file
        print(view)
        gallery = Livestock(name=form.name.data,address=form.address.data,gender=form.gender.data,dob=form.dob.data,phone=form.phone.data,email=form.email.data,block=form.block.data,panchayath=form.panchayath.data,village=form.village.data,bank=form.bank.data,accountnum=form.accountnum.data,aadharnum=form.aadharnum.data,rationnum=form.rationnum.data,animaltype=form.animaltype.data,animalnum=form.animalnum.data,img=view)
        db.session.add(gallery)
        db.session.commit()
        print(gallery)
        flash('image added')
        return redirect('/livestock')
    return render_template('livestock.html',form=form)

@app.route('/cropinsur',methods=['POST','GET'])
def cropinsur():
    form=Crop_insur()
    view="default.jpg"
    if form.validate_on_submit():
        if form.img.data:
            pic_file = save_picture(form.img.data)
            view = pic_file
        print(view)
        gallery = Insurcrop(name=form.name.data,address=form.address.data,gender=form.gender.data,dob=form.dob.data,phone=form.phone.data,email=form.email.data,block=form.block.data,panchayath=form.panchayath.data,village=form.village.data,aadharnum=form.aadharnum.data,bank=form.bank.data,accountnum=form.accountnum.data,area=form.area.data,cropname=form.cropname.data,farmerid=form.farmerid.data,img=view)
        db.session.add(gallery)
        db.session.commit()
        print(gallery)
        flash('image added')
        return redirect('/cropinsur')
    return render_template('cropinsur.html',form=form)

@app.route('/calamity',methods=['POST','GET'])
def calamity():
    form=Calamity_reg()
    view="default.jpg"
    if form.validate_on_submit():
        if form.img.data:
            pic_file = save_picture(form.img.data)
            view = pic_file
        print(view)
        gallery = Calamity(name=form.name.data,farmerid=form.farmerid.data,address=form.address.data,gender=form.gender.data,dob=form.dob.data,phone=form.phone.data,email=form.email.data,block=form.block.data,panchayath=form.panchayath.data,village=form.village.data,aadharnum=form.aadharnum.data,bank=form.bank.data,accountnum=form.accountnum.data,area=form.area.data,cropname=form.cropname.data,img=view)
        db.session.add(gallery)
        db.session.commit()
        print(gallery)
        flash('image added')
        return redirect('/calamity')
    return render_template('calamity.html',form=form)



@app.route('/soil_test',methods=['POST','GET'])
def soil_test():
    form=Soiltest()
    view="default.jpg"
    if form.validate_on_submit():
        print(view)
        gallery = Addsoiltest(name=form.name.data,address=form.address.data,contact=form.contact.data,day=form.day.data,time=form.time.data)
        db.session.add(gallery)
        db.session.commit()
        print(gallery)
        flash('image added')
        return redirect('/soil_test')
    return render_template('soil_test.html',form=form)


@app.route('/mac_rentview')
def mac_rentview():
    Pap = Machine_rent.query.all()
    return render_template('mac_rentview.html',Pap=Pap)

@app.route('/vtraining_cen')
def vtraining_cen():
    Pap = Addtraining.query.all()
    return render_template('vtraining_cen.html',Pap=Pap)

@app.route('/vtraining_an')
def vtraining_an():
    Pap = Addtraining.query.all()
    return render_template('vtraining_an.html',Pap=Pap)

@app.route('/view_soiltest')
def view_soiltest():
    Pap = Addsoiltest.query.all()
    return render_template('view_soiltest.html',Pap=Pap)

@app.route('/view_notification')
def view_notification():
    Pap = Addnotice.query.all()
    return render_template('view_notification.html',Pap=Pap)

@app.route('/view_notice')
def view_notice():
    Pap = Addnotice.query.all()
    return render_template('view_notice.html',Pap=Pap)

@app.route('/magazine_view')
def magazine_view():
    Pap = Magazine.query.all()
    return render_template('magazine_view.html',Pap=Pap)

@app.route('/magazine_anview')
def magazine_anview():
    Pap = Magazine.query.all()
    return render_template('magazine_anview.html',Pap=Pap)



@app.route('/view_agriprod')
def view_agriprod():
    Pap = Addprod.query.all()
    return render_template('view_agriprod.html',Pap=Pap)


@app.route('/soil_health',methods=['POST','GET'])
def soil_health():
    form=Soilhealth()
    view="default.jpg"
    if form.validate_on_submit():
        if form.img.data:
            pic_file = save_picture(form.img.data)
            view = pic_file
        print(view)
        gallery = Soil_health(name=form.name.data,address=form.address.data,gender=form.gender.data,dob=form.dob.data,phone=form.phone.data,email=form.email.data,block=form.block.data,panchayath=form.panchayath.data,village=form.village.data,bank=form.bank.data,accountnum=form.accountnum.data,area=form.area.data,cropname=form.cropname.data,img=view)
        db.session.add(gallery)
        db.session.commit()
        print(gallery)
        flash('image added')
        return redirect('/soil_health')
    return render_template('soil_health.html',form=form)


@app.route('/cart',methods=['POST','GET'])
def cart():
    form=Addcart()
    view="default.jpg"
    if form.validate_on_submit():
        if form.img.data:
            pic_file = save_picture(form.img.data)
            view = pic_file
        print(view)
        gallery = Cart(bcode=form.bcode.data,bname=form.bname.data,author=form.author.data,publication=form.publication.data,pub_year=form.pub_year.data,price=form.price.data,img=view)
        db.session.add(gallery)
        db.session.commit()
        print(gallery)
        flash('image added')
        return redirect('/cart')
    return render_template('cart.html',form=form)


@app.route('/view_shm')
def view_shm():
    Pap = Shmreg.query.all()
    return render_template('view_shm.html',Pap=Pap)

@app.route('/view_soiltbooking')
def view_soiltbooking():
    Pap = Soilbooknow.query.all()
    return render_template('view_soiltbooking.html',Pap=Pap)


@app.route('/view_trainingbooking')
def view_trainingbooking():
    Pap = Trainingbooking.query.all()
    return render_template('view_trainingbooking.html',Pap=Pap)

@app.route('/view_farmerreg')
def view_farmerreg():
    Pap = Farmerreg.query.all()
    return render_template('view_farmerreg.html',Pap=Pap)

@app.route('/view_insur')
def view_insur():
    Pap = Insurcrop.query.all()
    return render_template('view_insur.html',Pap=Pap)

@app.route('/view_machrent')
def view_machrent():
    Pap = Machine_rent.query.all()
    return render_template('view_machrent.html',Pap=Pap)

@app.route('/view_fameran')
def view_fameran():
    Pap = An_farmerreg.query.all()
    return render_template('view_fameran.html',Pap=Pap)


@app.route('/view_polyhouse')
def view_polyhouse():
    Pap = Polyhouse.query.all()
    return render_template('view_polyhouse.html',Pap=Pap)


@app.route('/view_prod')
def view_prod():
    Pap = Addprod.query.all()
    return render_template('view_prod.html',Pap=Pap)

@app.route('/view_product')
def view_product():
    Pap = Addprod.query.all()
    return render_template('view_product.html',Pap=Pap)

@app.route('/view_elect')
def view_elect():
    Pap = Electricity.query.all()
    return render_template('view_elect.html',Pap=Pap)


@app.route('/view_livestock')
def view_livestock():
    Pap = Livestock.query.all()
    return render_template('view_livestock.html',Pap=Pap)


@app.route('/view_loanagri')
def view_loanagri():
    Pap = Loanform.query.all()
    return render_template('view_loanagri.html',Pap=Pap)

@app.route('/view_loananimal')
def view_loananimal():
    Pap = Loananimal.query.all()
    return render_template('view_loananimal.html',Pap=Pap)


@app.route('/view_soilhealth')
def view_soilhealth():
    Pap = Soil_health.query.all()
    return render_template('view_soilhealth.html',Pap=Pap)

@app.route('/view_machine')
def view_machine():
    Pap = Machines.query.all()
    return render_template('view_machine.html',Pap=Pap)

@app.route('/view_cow')
def view_cow():
    Pap = Cowdairy.query.all()
    return render_template('view_cow.html',Pap=Pap)

@app.route('/view_goat')
def view_goat():
    Pap = Goatfarm.query.all()
    return render_template('view_goat.html',Pap=Pap)

@app.route('/view_hen')
def view_hen():
    Pap = Hfarm.query.all()
    return render_template('view_hen.html',Pap=Pap)


@app.route('/adview_elect')
def adview_elect():
    Pap = Electricity.query.filter_by(verify="verify").all()
    return render_template('adview_elect.html',Pap=Pap)

@app.route('/adview_machine')
def adview_machine():
    Pap = Machines.query.filter_by(verify="verify").all()
    return render_template('adview_machine.html',Pap=Pap)

@app.route('/adview_cow')
def adview_cow():
    Pap = Cowdairy.query.filter_by(verify="verify").all()
    return render_template('adview_cow.html',Pap=Pap)

@app.route('/adview_goat')
def adview_goat():
    Pap = Goatfarm.query.filter_by(verify="verify").all()
    return render_template('adview_goat.html',Pap=Pap)

@app.route('/adview_hen')
def adview_hen():
    Pap = Hfarm.query.filter_by(verify="verify").all()
    return render_template('adview_hen.html',Pap=Pap)


@app.route('/adview_ferti')
def adview_ferti():
    Pap = Fertiliz.query.filter_by(verify="verify").all()
    return render_template('adview_ferti.html',Pap=Pap)

@app.route('/adview_calamity')
def adview_calamity():
    Pap = Calamity.query.filter_by(verify="verify").all()
    return render_template('adview_calamity.html',Pap=Pap)


@app.route('/adview_shm')
def adview_shm():
    Pap = Shmreg.query.filter_by(verify="verify").all()
    return render_template('adview_shm.html',Pap=Pap)


@app.route('/adview_loananimal')
def adview_loananimal():
    Pap = Loananimal.query.filter_by(verify="verify").all()
    return render_template('adview_loananimal.html',Pap=Pap)


@app.route('/adview_farmerreg')
def adview_farmerreg():
    Pap = Farmerreg.query.filter_by(verify="verify").all()
    return render_template('adview_farmerreg.html',Pap=Pap)

@app.route('/adview_farmerregan')
def adview_farmerregan():
    Pap = An_farmerreg.query.filter_by(verify="verify").all()
    return render_template('adview_farmerregan.html',Pap=Pap)

@app.route('/adview_polyhouse')
def adview_polyhouse():
    Pap = Polyhouse.query.filter_by(verify="verify").all()
    return render_template('adview_polyhouse.html',Pap=Pap)

@app.route('/adview_pensionan')
def adview_pensionan():
    Pap = Pension_an.query.filter_by(verify="verify").all()
    return render_template('adview_pensionan.html',Pap=Pap)

@app.route('/adview_pension')
def adview_pension():
    Pap = Pension.query.filter_by(verify="verify").all()
    return render_template('adview_pension.html',Pap=Pap)

@app.route('/adview_pmk')
def adview_pmk():
    Pap = Pmkisan.query.filter_by(verify="verify").all()
    return render_template('adview_pmk.html',Pap=Pap)

@app.route('/adview_pmkan')
def adview_pmkan():
    Pap = An_pmk.query.filter_by(verify="verify").all()
    return render_template('adview_pmkan.html',Pap=Pap)


@app.route('/adview_bamboo')
def adview_bamboo():
    Pap = Bamboo_reg.query.filter_by(verify="verify").all()
    return render_template('adview_bamboo.html',Pap=Pap)

@app.route('/adview_loanagri')
def adview_loanagri():
    Pap = Loanform.query.filter_by(verify="verify").all()
    return render_template('adview_loanagri.html',Pap=Pap)

@app.route('/adview_livestock')
def adview_livestock():
    Pap = Livestock.query.filter_by(verify="verify").all()
    return render_template('adview_livestock.html',Pap=Pap)

@app.route('/adview_fasal')
def adview_fasal():
    Pap = Pm_fasal.query.filter_by(verify="verify").all()
    return render_template('adview_fasal.html',Pap=Pap)

@app.route('/adview_soilhealth')
def adview_soilhealth():
    Pap = Soil_health.query.filter_by(verify="verify").all()
    return render_template('adview_soilhealth.html',Pap=Pap)


@app.route('/view_calamity')
def view_calamity():
    Pap = Calamity.query.all()
    return render_template('view_calamity.html',Pap=Pap)

@app.route('/view_bookingmac')
def view_bookingmac():
    Pap = Machinebooknow.query.all()
    return render_template('view_bookingmac.html',Pap=Pap)

@app.route('/view_pmk')
def view_pmk():
    Pap = Pmkisan.query.all()
    return render_template('view_pmk.html',Pap=Pap)

@app.route('/view_pmkan')
def view_pmkan():
    Pap = An_pmk.query.all()
    return render_template('view_pmkan.html',Pap=Pap)

@app.route('/view_pension')
def view_pension():
    Pap = Pension.query.all()
    return render_template('view_pension.html',Pap=Pap)

@app.route('/view_pensionan')
def view_pensionan():
    Pap = Pension_an.query.all()
    return render_template('view_pensionan.html',Pap=Pap)

@app.route('/view_fasal')
def view_fasal():
    Pap = Pm_fasal.query.all()
    return render_template('view_fasal.html',Pap=Pap)

@app.route('/view_bamboo')
def view_bamboo():
    Pap = Bamboo_reg.query.all()
    return render_template('view_bamboo.html',Pap=Pap)

@app.route('/view_ferti')
def view_ferti():
    Pap = Fertiliz.query.all()
    return render_template('view_ferti.html',Pap=Pap)

@app.route('/view_feedback')
def view_feedback():
    Pap = Addfeed.query.all()
    return render_template('view_feedback.html',Pap=Pap)


@app.route('/appr_soil/<int:id>',methods=['GET','POST'])
def appr_soil(id):
    a=Soil_health.query.get_or_404(id)
    if request.method == 'POST':
        a.name = request.form['name']
        a.email = request.form['email']
        a.status= request.form['status']
        try:
            db.session.commit()
            return redirect('/adview_soilhealth')
        except Exception as e:
            
            print(e)

    return render_template('appr_soil.html',a=a)

@app.route('/appr_soiltbook/<int:id>',methods=['GET','POST'])
def appr_soiltbook(id):
    a=Soilbooknow.query.get_or_404(id)
    if request.method == 'POST':
        a.name = request.form['name']
        a.address = request.form['address']
        a.email = request.form['email']
        a.status= request.form['status']
        try:
            db.session.commit()
            return redirect('/view_soiltbooking')
        except Exception as e:
            
            print(e)

    return render_template('appr_soiltbook.html',a=a)

@app.route('/appr_trainbook/<int:id>',methods=['GET','POST'])
def appr_trainbook(id):
    a=Trainingbooking.query.get_or_404(id)
    if request.method == 'POST':
        a.name = request.form['name']
        a.address = request.form['address']
        a.email = request.form['email']
        a.status= request.form['status']
        try:
            db.session.commit()
            return redirect('/view_trainingbooking')
        except Exception as e:
            
            print(e)

    return render_template('appr_trainbook.html',a=a)



@app.route('/soiltest_booking/<int:id>',methods=['GET','POST'])
def soiltest_booking(id):
    a=Addsoiltest.query.get_or_404(id)
    if request.method == 'POST':
        a.name = request.form['name']
        a.day = request.form['day']
        a.time = request.form['time']
        try:
            db.session.commit()
            return redirect('/soilt_booknow')
        except Exception as e:
            
            print(e)

    return render_template('soiltest_booking.html',a=a)


@app.route('/macrent_booking/<int:id>',methods=['GET','POST'])
def macrent_booking(id):
    a=Machine_rent.query.get_or_404(id)
    if request.method == 'POST':
        a.productname = request.form['productname']
        a.brant = request.form['brant']
        a.rentrupee = request.form['rentrupee']
        try:
            db.session.commit()
            return redirect('/mac_booknow')
        except Exception as e:
            
            print(e)

    return render_template('macrent_booking.html',a=a)


@app.route('/booking_trainingclass/<int:id>',methods=['GET','POST'])
def booking_trainingclass(id):
    a=Addtraining.query.get_or_404(id)
    if request.method == 'POST':
        a.name = request.form['name']
        a.date = request.form['date']
        a.time = request.form['time']
        a.topic = request.form['topic']
        try:
            db.session.commit()
            return redirect('/booknow_training')
        except Exception as e:
            
            print(e)

    return render_template('booking_trainingclass.html',a=a)

@app.route('/booking_trainingclass_an/<int:id>',methods=['GET','POST'])
def booking_trainingclass_an(id):
    a=Addtraining.query.get_or_404(id)
    if request.method == 'POST':
        a.name = request.form['name']
        a.date = request.form['date']
        a.time = request.form['time']
        a.topic = request.form['topic']
        try:
            db.session.commit()
            return redirect('/booknow_training_an')
        except Exception as e:
            
            print(e)

    return render_template('booking_trainingclass_an.html',a=a)



@app.route('/appr_calamity/<int:id>',methods=['GET','POST'])
def appr_calamity(id):
    a=Calamity.query.get_or_404(id)
    if request.method == 'POST':
        a.name = request.form['name']
        a.email = request.form['email']
        a.status= request.form['status']
        try:
            db.session.commit()
            return redirect('/adview_calamity')
        except Exception as e:
            
            print(e)

    return render_template('appr_calamity.html',a=a)

@app.route('/appr_onecrore/<int:id>',methods=['GET','POST'])
def appr_onecrore(id):
    a=One_crore.query.get_or_404(id)
    if request.method == 'POST':
        a.name = request.form['name']
        a.email = request.form['email']
        a.status= request.form['status']
        try:
            db.session.commit()
            return redirect('/adview_onecrore')
        except Exception as e:
            
            print(e)

    return render_template('appr_onecrore.html',a=a)


@app.route('/appr_pmk/<int:id>',methods=['GET','POST'])
def appr_pmk(id):
    a=Pmkisan.query.get_or_404(id)
    if request.method == 'POST':
        a.name = request.form['name']
        a.email = request.form['email']
        a.status= request.form['status']
        try:
            db.session.commit()
            return redirect('/adview_pmk')
        except Exception as e:
            
            print(e)

    return render_template('appr_pmk.html',a=a)

@app.route('/appr_pmkan/<int:id>',methods=['GET','POST'])
def appr_pmkan(id):
    a=An_pmk.query.get_or_404(id)
    if request.method == 'POST':
        a.name = request.form['name']
        a.email = request.form['email']
        a.status= request.form['status']
        try:
            db.session.commit()
            return redirect('/adview_pmkan')
        except Exception as e:
            
            print(e)

    return render_template('appr_pmkan.html',a=a)

@app.route('/appr_pensionan/<int:id>',methods=['GET','POST'])
def appr_pensionan(id):
    a=Pension_an.query.get_or_404(id)
    if request.method == 'POST':
        a.name = request.form['name']
        a.email = request.form['email']
        a.status= request.form['status']
        try:
            db.session.commit()
            return redirect('/adview_pensionan')
        except Exception as e:
            
            print(e)

    return render_template('appr_pensionan.html',a=a)

@app.route('/appr_pension/<int:id>',methods=['GET','POST'])
def appr_pension(id):
    a=Pension.query.get_or_404(id)
    if request.method == 'POST':
        a.name = request.form['name']
        a.email = request.form['email']
        a.status= request.form['status']
        try:
            db.session.commit()
            return redirect('/adview_pension')
        except Exception as e:
            
            print(e)

    return render_template('appr_pension.html',a=a)


@app.route('/appr_elect/<int:id>',methods=['GET','POST'])
def appr_elect(id):
    a=Electricity.query.get_or_404(id)
    if request.method == 'POST':
        a.name = request.form['name']
        a.email = request.form['email']
        a.status= request.form['status']
        try:
            db.session.commit()
            return redirect('/adview_elect')
        except Exception as e:
            
            print(e)

    return render_template('appr_elect.html',a=a)


@app.route('/appr_cow/<int:id>',methods=['GET','POST'])
def appr_cow(id):
    a=Cowdairy.query.get_or_404(id)
    if request.method == 'POST':
        a.name = request.form['name']
        a.email = request.form['email']
        a.status= request.form['status']
        try:
            db.session.commit()
            return redirect('/adview_cow')
        except Exception as e:
            
            print(e)

    return render_template('appr_cow.html',a=a)

@app.route('/appr_goat/<int:id>',methods=['GET','POST'])
def appr_goat(id):
    a=Goatfarm.query.get_or_404(id)
    if request.method == 'POST':
        a.name = request.form['name']
        a.email = request.form['email']
        a.status= request.form['status']
        try:
            db.session.commit()
            return redirect('/adview_goat')
        except Exception as e:
            
            print(e)

    return render_template('appr_goat.html',a=a)

@app.route('/appr_hen/<int:id>',methods=['GET','POST'])
def appr_hen(id):
    a=Hfarm.query.get_or_404(id)
    if request.method == 'POST':
        a.name = request.form['name']
        a.email = request.form['email']
        a.status= request.form['status']
        try:
            db.session.commit()
            return redirect('/adview_hen')
        except Exception as e:
            
            print(e)

    return render_template('appr_hen.html',a=a)


@app.route('/appr_ferti/<int:id>',methods=['GET','POST'])
def appr_ferti(id):
    a=Fertiliz.query.get_or_404(id)
    if request.method == 'POST':
        a.name = request.form['name']
        a.email = request.form['email']
        a.status= request.form['status']
        try:
            db.session.commit()
            return redirect('/adview_ferti')
        except Exception as e:
            
            print(e)

    return render_template('appr_ferti.html',a=a)


@app.route('/appr_shm/<int:id>',methods=['GET','POST'])
def appr_shm(id):
    a=Shmreg.query.get_or_404(id)
    if request.method == 'POST':
        a.name = request.form['name']
        a.email = request.form['email']
        a.status= request.form['status']
        try:
            db.session.commit()
            return redirect('/adview_shm')
        except Exception as e:
            
            print(e)

    return render_template('appr_shm.html',a=a)
    

@app.route('/appr_machine/<int:id>',methods=['GET','POST'])
def appr_machine(id):
    a=Machines.query.get_or_404(id)
    if request.method == 'POST':
        a.name = request.form['name']
        a.email = request.form['email']
        a.status= request.form['status']
        try:
            db.session.commit()
            return redirect('/adview_machine')
        except Exception as e:
            
            print(e)

    return render_template('appr_machine.html',a=a)


@app.route('/appr_farmerreg/<int:id>',methods=['GET','POST'])
def appr_farmerreg(id):
    a=Farmerreg.query.get_or_404(id)
    if request.method == 'POST':
        a.name = request.form['name']
        a.email = request.form['email']
        a.status= request.form['status']
        try:
            db.session.commit()
            return redirect('/adview_farmerreg')
        except Exception as e:
            
            print(e)

    return render_template('appr_farmerreg.html',a=a)



@app.route('/appr_farmerregan/<int:id>',methods=['GET','POST'])
def appr_farmerregan(id):
    a=An_farmerreg.query.get_or_404(id)
    if request.method == 'POST':
        a.name = request.form['name']
        a.email = request.form['email']
        a.status= request.form['status']
        try:
            db.session.commit()
            return redirect('/adview_farmerregan')
        except Exception as e:
            
            print(e)

    return render_template('appr_farmerregan.html',a=a)



@app.route('/appr_polyhouse/<int:id>',methods=['GET','POST'])
def appr_polyhouse(id):
    a=Polyhouse.query.get_or_404(id)
    if request.method == 'POST':
        a.name = request.form['name']
        a.email = request.form['email']
        a.status= request.form['status']
        try:
            db.session.commit()
            return redirect('/adview_polyhouse')
        except Exception as e:
            
            print(e)

    return render_template('appr_polyhouse.html',a=a)

@app.route('/appr_livestock/<int:id>',methods=['GET','POST'])
def appr_livestock(id):
    a=Livestock.query.get_or_404(id)
    if request.method == 'POST':
        a.name = request.form['name']
        a.email = request.form['email']
        a.status= request.form['status']
        try:
            db.session.commit()
            return redirect('/adview_livestock')
        except Exception as e:
            
            print(e)

    return render_template('appr_livestock.html',a=a)

@app.route('/appr_loanagri/<int:id>',methods=['GET','POST'])
def appr_loanagri(id):
    a=Loanform.query.get_or_404(id)
    if request.method == 'POST':
        a.name = request.form['name']
        a.email = request.form['email']
        a.status= request.form['status']
        try:
            db.session.commit()
            return redirect('/adview_loanagri')
        except Exception as e:
            
            print(e)

    return render_template('appr_loanagri.html',a=a)

@app.route('/appr_loananimal/<int:id>',methods=['GET','POST'])
def appr_loananimal(id):
    a=Loananimal.query.get_or_404(id)
    if request.method == 'POST':
        a.name = request.form['name']
        a.email = request.form['email']
        a.status= request.form['status']
        try:
            db.session.commit()
            return redirect('/adview_loananimal')
        except Exception as e:
            
            print(e)

    return render_template('appr_loananimal.html',a=a)




@app.route('/appr_bamboo/<int:id>',methods=['GET','POST'])
def appr_bamboo(id):
    a=Bamboo_reg.query.get_or_404(id)
    if request.method == 'POST':
        a.name = request.form['name']
        a.email = request.form['email']
        a.status= request.form['status']
        try:
            db.session.commit()
            return redirect('/adview_bamboo')
        except Exception as e:
            
            print(e)

    return render_template('appr_bamboo.html',a=a)

@app.route('/appr_fasal/<int:id>',methods=['GET','POST'])
def appr_fasal(id):
    a=Pm_fasal.query.get_or_404(id)
    if request.method == 'POST':
        a.name = request.form['name']
        a.email = request.form['email']
        a.status= request.form['status']
        try:
            db.session.commit()
            return redirect('/adview_fasal')
        except Exception as e:
            
            print(e)

    return render_template('appr_fasal.html',a=a)

@app.route('/varify_shm/<int:id>',methods=['GET','POST'])
def varify_shm(id):
    a=Shmreg.query.get_or_404(id)
    if request.method == 'POST':
        a.name = request.form['name']
        a.email = request.form['email']
        a.verify= request.form['verify']
        try:
            db.session.commit()
            return redirect('/view_shm')
        except Exception as e:
            
            print(e)

    return render_template('varify_shm.html',a=a)


@app.route('/varify_insur/<int:id>',methods=['GET','POST'])
def varify_insur(id):
    a=Insurcrop.query.get_or_404(id)
    if request.method == 'POST':
        a.name = request.form['name']
        a.email = request.form['email']
        a.verify= request.form['verify']
        try:
            db.session.commit()
            return redirect('/view_insur')
        except Exception as e:
            
            print(e)

    return render_template('varify_insur.html',a=a)



@app.route('/varify_pensionan/<int:id>',methods=['GET','POST'])
def varify_pensionan(id):
    a= Pension_an.query.get_or_404(id)
    if request.method == 'POST':
        a.name = request.form['name']
        a.email = request.form['email']
        a.verify= request.form['verify']
        try:
            db.session.commit()
            return redirect('/view_pensionan')
        except Exception as e:
            
            print(e)

    return render_template('varify_pensionan.html',a=a)

@app.route('/varify_pension/<int:id>',methods=['GET','POST'])
def varify_pension(id):
    a= Pension.query.get_or_404(id)
    if request.method == 'POST':
        a.name = request.form['name']
        a.email = request.form['email']
        a.verify= request.form['verify']
        try:
            db.session.commit()
            return redirect('/view_pension')
        except Exception as e:
            
            print(e)

    return render_template('varify_pension.html',a=a)


@app.route('/varify_onecrore/<int:id>',methods=['GET','POST'])
def varify_onecrore(id):
    a=One_crore.query.get_or_404(id)
    if request.method == 'POST':
        a.name = request.form['name']
        a.email = request.form['email']
        a.verify= request.form['verify']
        try:
            db.session.commit()
            return redirect('/view_onecrore')
        except Exception as e:
            
            print(e)

    return render_template('varify_onecrore.html',a=a)


@app.route('/varify_pmk/<int:id>',methods=['GET','POST'])
def varify_pmk(id):
    a=Pmkisan.query.get_or_404(id)
    if request.method == 'POST':
        a.name = request.form['name']
        a.email = request.form['email']
        a.verify= request.form['verify']
        try:
            db.session.commit()
            return redirect('/view_pmk')
        except Exception as e:
            
            print(e)

    return render_template('varify_pmk.html',a=a)


@app.route('/varify_pmkan/<int:id>',methods=['GET','POST'])
def varify_pmkan(id):
    a=An_pmk.query.get_or_404(id)
    if request.method == 'POST':
        a.name = request.form['name']
        a.email = request.form['email']
        a.verify= request.form['verify']
        try:
            db.session.commit()
            return redirect('/view_pmkan')
        except Exception as e:
            
            print(e)

    return render_template('varify_pmkan.html',a=a)


@app.route('/varify_hen/<int:id>',methods=['GET','POST'])
def varify_hen(id):
    a=Hfarm.query.get_or_404(id)
    if request.method == 'POST':
        a.name = request.form['name']
        a.email = request.form['email']
        a.verify= request.form['verify']
        try:
            db.session.commit()
            return redirect('/view_hen')
        except Exception as e:
            
            print(e)

    return render_template('varify_hen.html',a=a)



@app.route('/varify_cow/<int:id>',methods=['GET','POST'])
def varify_cow(id):
    a=Cowdairy.query.get_or_404(id)
    if request.method == 'POST':
        a.name = request.form['name']
        a.email = request.form['email']
        a.verify= request.form['verify']
        try:
            db.session.commit()
            return redirect('/view_cow')
        except Exception as e:
            
            print(e)

    return render_template('varify_cow.html',a=a)

@app.route('/varify_goat/<int:id>',methods=['GET','POST'])
def varify_goat(id):
    a=Goatfarm.query.get_or_404(id)
    if request.method == 'POST':
        a.name = request.form['name']
        a.email = request.form['email']
        a.verify= request.form['verify']
        try:
            db.session.commit()
            return redirect('/view_goat')
        except Exception as e:
            
            print(e)

    return render_template('varify_goat.html',a=a)


@app.route('/varify_ferti/<int:id>',methods=['GET','POST'])
def varify_ferti(id):
    a=Fertiliz.query.get_or_404(id)
    if request.method == 'POST':
        a.name = request.form['name']
        a.email = request.form['email']
        a.verify= request.form['verify']
        try:
            db.session.commit()
            return redirect('/view_ferti')
        except Exception as e:
            
            print(e)

    return render_template('varify_ferti.html',a=a)


@app.route('/varify_machine/<int:id>',methods=['GET','POST'])
def varify_machine(id):
    a=Machines.query.get_or_404(id)
    if request.method == 'POST':
        a.name = request.form['name']
        a.email = request.form['email']
        a.verify= request.form['verify']
        try:
            db.session.commit()
            return redirect('/view_machine')
        except Exception as e:
            
            print(e)

    return render_template('varify_machine.html',a=a)


@app.route('/varify_farmerreg/<int:id>',methods=['GET','POST'])
def varify_farmerreg(id):
    a=Farmerreg.query.get_or_404(id)
    if request.method == 'POST':
        a.name = request.form['name']
        a.email = request.form['email']
        a.verify= request.form['verify']
        try:
            db.session.commit()
            return redirect('/view_farmerreg')
        except Exception as e:
            
            print(e)

    return render_template('varify_farmerreg.html',a=a)

@app.route('/verify_farmeran/<int:id>',methods=['GET','POST'])
def verify_farmeran(id):
    a=An_farmerreg.query.get_or_404(id)
    if request.method == 'POST':
        a.name = request.form['name']
        a.email = request.form['email']
        a.verify= request.form['verify']
        try:
            db.session.commit()
            return redirect('/view_fameran')
        except Exception as e:
            
            print(e)

    return render_template('verify_farmeran.html',a=a)

@app.route('/verify_calamity/<int:id>',methods=['GET','POST'])
def verify_calamity(id):
    a=Calamity.query.get_or_404(id)
    if request.method == 'POST':
        a.name = request.form['name']
        a.email = request.form['email']
        a.verify= request.form['verify']
        try:
            db.session.commit()
            return redirect('/view_calamity')
        except Exception as e:
            
            print(e)

    return render_template('verify_calamity.html',a=a)




@app.route('/varify_polyhouse/<int:id>',methods=['GET','POST'])
def varify_polyhouse(id):
    a=Polyhouse.query.get_or_404(id)
    if request.method == 'POST':
        a.name = request.form['name']
        a.email = request.form['email']
        a.verify= request.form['verify']
        try:
            db.session.commit()
            return redirect('/view_polyhouse')
        except Exception as e:
            
            print(e)

    return render_template('varify_polyhouse.html',a=a)

@app.route('/varify_elect/<int:id>',methods=['GET','POST'])
def varify_elect(id):
    a=Electricity.query.get_or_404(id)
    if request.method == 'POST':
        a.name = request.form['name']
        a.email = request.form['email']
        a.verify= request.form['verify']
        try:
            db.session.commit()
            return redirect('/view_elect')
        except Exception as e:
            
            print(e)

    return render_template('varify_elect.html',a=a)




@app.route('/varify_livestock/<int:id>',methods=['GET','POST'])
def varify_livestock(id):
    a=Livestock.query.get_or_404(id)
    if request.method == 'POST':
        a.name = request.form['name']
        a.email = request.form['email']
        a.verify= request.form['verify']
        try:
            db.session.commit()
            return redirect('/view_livestock')
        except Exception as e:
            
            print(e)

    return render_template('varify_livestock.html',a=a)



@app.route('/varify_loanagri/<int:id>',methods=['GET','POST'])
def varify_loanagri(id):
    a=Loanform.query.get_or_404(id)
    if request.method == 'POST':
        a.name = request.form['name']
        a.email = request.form['email']
        a.verify= request.form['verify']
        try:
            db.session.commit()
            return redirect('/view_loanagri')
        except Exception as e:
            
            print(e)

    return render_template('varify_loanagri.html',a=a)

@app.route('/varify_loananimal/<int:id>',methods=['GET','POST'])
def varify_loananimal(id):
    a=Loananimal.query.get_or_404(id)
    if request.method == 'POST':
        a.name = request.form['name']
        a.email = request.form['email']
        a.verify= request.form['verify']
        try:
            db.session.commit()
            return redirect('/view_loananimal')
        except Exception as e:
            
            print(e)

    return render_template('varify_loananimal.html',a=a)


@app.route('/varify_fasal/<int:id>',methods=['GET','POST'])
def varify_fasal(id):
    a=Pm_fasal.query.get_or_404(id)
    if request.method == 'POST':
        a.name = request.form['name']
        a.email = request.form['email']
        a.verify= request.form['verify']
        try:
            db.session.commit()
            return redirect('/view_fasal')
        except Exception as e:
            
            print(e)

    return render_template('varify_fasal.html',a=a)

@app.route('/varify_bamboo/<int:id>',methods=['GET','POST'])
def varify_bamboo(id):
    a=Bamboo_reg.query.get_or_404(id)
    if request.method == 'POST':
        a.name = request.form['name']
        a.email = request.form['email']
        a.verify= request.form['verify']
        try:
            db.session.commit()
            return redirect('/view_bamboo')
        except Exception as e:
            
            print(e)

    return render_template('varify_bamboo.html',a=a)

@app.route('/verify_soilhealth/<int:id>',methods=['GET','POST'])
def verify_soilhealth(id):
    a=Soil_health.query.get_or_404(id)
    if request.method == 'POST':
        a.name = request.form['name']
        a.email = request.form['email']
        a.verify= request.form['verify']
        try:
            db.session.commit()
            return redirect('/view_soilhealth')
        except Exception as e:
            
            print(e)

    return render_template('verify_soilhealth.html',a=a)

@app.route('/view_shmdele/<int:id>')
def view_shmdele(id):
    upcus = Shmreg.query.get_or_404(id)
    try:
        db.session.delete(upcus)
        db.session.commit()
        return redirect('/view_shm')
    except:
        return 'NOT committed'

@app.route('/view_insurdele/<int:id>')
def view_insurdele(id):
    upcus = Insurcrop.query.get_or_404(id)
    try:
        db.session.delete(upcus)
        db.session.commit()
        return redirect('/view_insur')
    except:
        return 'NOT committed'


@app.route('/view_calamitydele/<int:id>')
def view_calamitydele(id):
    upcus = Calamity.query.get_or_404(id)
    try:
        db.session.delete(upcus)
        db.session.commit()
        return redirect('/view_calamity')
    except:
        return 'NOT committed'

@app.route('/view_pmkdele/<int:id>')
def view_pmkdele(id):
    upcus = Pmkisan.query.get_or_404(id)
    try:
        db.session.delete(upcus)
        db.session.commit()
        return redirect('/view_pmk')
    except:
        return 'NOT committed'

@app.route('/appr_trainbookdele/<int:id>')
def appr_trainbookdele(id):
    upcus = Trainingbooking.query.get_or_404(id)
    try:
        db.session.delete(upcus)
        db.session.commit()
        return redirect('/view_trainingbooking')
    except:
        return 'NOT committed'

@app.route('/appr_soiltbookingdele/<int:id>')
def appr_soiltbookingdele(id):
    upcus = Soilbooknow.query.get_or_404(id)
    try:
        db.session.delete(upcus)
        db.session.commit()
        return redirect('/view_soiltbooking')
    except:
        return 'NOT committed'


@app.route('/view_pmkandele/<int:id>')
def view_pmkandele(id):
    upcus = An_pmk.query.get_or_404(id)
    try:
        db.session.delete(upcus)
        db.session.commit()
        return redirect('/view_pmkan')
    except:
        return 'NOT committed'

@app.route('/view_goatdele/<int:id>')
def view_goatdele(id):
    upcus = Goatfarm.query.get_or_404(id)
    try:
        db.session.delete(upcus)
        db.session.commit()
        return redirect('/view_goat')
    except:
        return 'NOT committed'

@app.route('/view_hendele/<int:id>')
def view_hendele(id):
    upcus = Hfarm.query.get_or_404(id)
    try:
        db.session.delete(upcus)
        db.session.commit()
        return redirect('/view_hen')
    except:
        return 'NOT committed'



@app.route('/view_cowdele/<int:id>')
def view_cowdele(id):
    upcus = Cowdairy.query.get_or_404(id)
    try:
        db.session.delete(upcus)
        db.session.commit()
        return redirect('/view_cow')
    except:
        return 'NOT committed'

@app.route('/view_fertidele/<int:id>')
def view_fertidele(id):
    upcus = Fertiliz.query.get_or_404(id)
    try:
        db.session.delete(upcus)
        db.session.commit()
        return redirect('/view_ferti')
    except:
        return 'NOT committed'

@app.route('/view_feeddele/<int:id>')
def view_feeddele(id):
    upcus = Addfeed.query.get_or_404(id)
    try:
        db.session.delete(upcus)
        db.session.commit()
        return redirect('/view_feedback')
    except:
        return 'NOT committed'


@app.route('/view_pensionandele/<int:id>')
def view_pensionandele(id):
    upcus = Pension_an.query.get_or_404(id)
    try:
        db.session.delete(upcus)
        db.session.commit()
        return redirect('/view_pensionan')
    except:
        return 'NOT committed'

@app.route('/view_pensiondele/<int:id>')
def view_pensiondele(id):
    upcus = Pension.query.get_or_404(id)
    try:
        db.session.delete(upcus)
        db.session.commit()
        return redirect('/view_pension')
    except:
        return 'NOT committed'

@app.route('/view_machinedele/<int:id>')
def view_machinedele(id):
    upcus = Machines.query.get_or_404(id)
    try:
        db.session.delete(upcus)
        db.session.commit()
        return redirect('/view_machine')
    except:
        return 'NOT committed'

@app.route('/view_electdele/<int:id>')
def view_electdele(id):
    upcus = Electricity.query.get_or_404(id)
    try:
        db.session.delete(upcus)
        db.session.commit()
        return redirect('/view_elect')
    except:
        return 'NOT committed'


@app.route('/view_loanagridele/<int:id>')
def view_loanagridele(id):
    upcus = Loanform.query.get_or_404(id)
    try:
        db.session.delete(upcus)
        db.session.commit()
        return redirect('/view_loanagri')
    except:
        return 'NOT committed'


@app.route('/view_loananimaldele/<int:id>')
def view_loananimaldele(id):
    upcus = Loananimal.query.get_or_404(id)
    try:
        db.session.delete(upcus)
        db.session.commit()
        return redirect('/view_loananimal')
    except:
        return 'NOT committed'

@app.route('/view_farmerregdele/<int:id>')
def view_farmerregdele(id):
    upcus = Farmerreg.query.get_or_404(id)
    try:
        db.session.delete(upcus)
        db.session.commit()
        return redirect('/view_farmerreg')
    except:
        return 'NOT committed'

@app.route('/view_farmerandele/<int:id>')
def view_farmerandele(id):
    upcus = An_farmerreg.query.get_or_404(id)
    try:
        db.session.delete(upcus)
        db.session.commit()
        return redirect('/view_fameran')
    except:
        return 'NOT committed'



@app.route('/view_polyhousedele/<int:id>')
def view_polyhousedele(id):
    upcus = Polyhouse.query.get_or_404(id)
    try:
        db.session.delete(upcus)
        db.session.commit()
        return redirect('/view_polyhouse')
    except:
        return 'NOT committed'



@app.route('/view_livestockdele/<int:id>')
def view_livestockdele(id):
    upcus = Livestock.query.get_or_404(id)
    try:
        db.session.delete(upcus)
        db.session.commit()
        return redirect('/view_livestock')
    except:
        return 'NOT committed'

@app.route('/view_fasaldele/<int:id>')
def view_pmkmaandele(id):
    upcus = Pmk_manndhany.query.get_or_404(id)
    try:
        db.session.delete(upcus)
        db.session.commit()
        return redirect('/view_pmkmaan')
    except:
        return 'NOT committed'

@app.route('/view_bamboodele/<int:id>')
def view_bamboodele(id):
    upcus = Bamboo_reg.query.get_or_404(id)
    try:
        db.session.delete(upcus)
        db.session.commit()
        return redirect('/view_bamboo')
    except:
        return 'NOT committed'

@app.route('/view_soildele/<int:id>')
def view_soildele(id):
    upcus = Soil_health.query.get_or_404(id)
    try:
        db.session.delete(upcus)
        db.session.commit()
        return redirect('/view_soilhelth')
    except:
        return 'NOT committed'

    
@app.route('/one_crore',methods=['POST','GET'])
def one_crore():
    form=Crore_one()
    view="default.jpg"
    if form.validate_on_submit():
        if form.img.data:
            pic_file = save_picture(form.img.data)
            view = pic_file
        print(view)
        gallery = One_crore(name=form.name.data,address=form.address.data,gender=form.gender.data,dob=form.dob.data,phone=form.phone.data,email=form.email.data,block=form.block.data,panchayath=form.panchayath.data,village=form.village.data,aadharnum=form.aadharnum.data,area=form.area.data,cropname=form.cropname.data,cropnum=form.cropnum.data,img=view)
        db.session.add(gallery)
        db.session.commit()
        print(gallery)
        flash('image added')
        return redirect('/one_crore')
    return render_template('one_crore.html',form=form)

@app.route('/bamboo',methods=['POST','GET'])
def bamboo():
    form=Bamboor()
    view="default.jpg"
    if form.validate_on_submit():
        if form.img.data:
            pic_file = save_picture(form.img.data)
            view = pic_file
        print(view)
        gallery =Bamboo_reg(name=form.name.data,address=form.address.data,gender=form.gender.data,dob=form.dob.data,phone=form.phone.data,email=form.email.data,block=form.block.data,panchayath=form.panchayath.data,village=form.village.data,aadharnum=form.aadharnum.data,area=form.area.data,img=view)
        db.session.add(gallery)
        db.session.commit()
        print(gallery)
        flash('image added')
        return redirect('/bamboo')
    return render_template('bamboo.html',form=form)





@app.route('/view_onecrore')
def view_onecrore():
    Pap = One_crore.query.all()
    return render_template('view_onecrore.html',Pap=Pap)

@app.route('/view_onecroredele/<int:id>')
def view_onecroredele(id):
    upcus = One_crore.query.get_or_404(id)
    try:
        db.session.delete(upcus)
        db.session.commit()
        return redirect('/view_onecrore')
    except:
        return 'NOT committed'

@app.route('/adview_onecrore')
def adview_onecrore():
    Pap = One_crore.query.filter_by(verify="verify").all()
    return render_template('adview_onecrore.html',Pap=Pap)

@app.route('/pmkisan',methods=['POST','GET'])
def pmkisan():
    form=Prmkisan()
    view="default.jpg"
    if form.validate_on_submit():
        if form.img.data:
            pic_file = save_picture(form.img.data)
            view = pic_file
        print(view)
        gallery = Pmkisan(name=form.name.data,address=form.address.data,gender=form.gender.data,dob=form.dob.data,phone=form.phone.data,email=form.email.data,block=form.block.data,panchayath=form.panchayath.data,village=form.village.data,bank=form.bank.data,accountnum=form.accountnum.data,aadharnum=form.aadharnum.data,img=view)
        db.session.add(gallery)
        db.session.commit()
        print(gallery)
        flash('image added')
        return redirect('/pmkisan')
    return render_template('pmkisan.html',form=form)

@app.route('/pmk_an',methods=['POST','GET'])
def pmk_an():
    form=Pmk_an()
    view="default.jpg"
    if form.validate_on_submit():
        if form.img.data:
            pic_file = save_picture(form.img.data)
            view = pic_file
        print(view)
        gallery = An_pmk(name=form.name.data,address=form.address.data,gender=form.gender.data,dob=form.dob.data,phone=form.phone.data,email=form.email.data,block=form.block.data,panchayath=form.panchayath.data,village=form.village.data,bank=form.bank.data,accountnum=form.accountnum.data,aadharnum=form.aadharnum.data,img=view)
        db.session.add(gallery)
        db.session.commit()
        print(gallery)
        flash('image added')
        return redirect('/pmk_an')
    return render_template('pmk_an.html',form=form)


@app.route('/pension',methods=['POST','GET'])
def pension():
    form=Pension_reg()
    view="default.jpg"
    if form.validate_on_submit():
        if form.img.data:
            pic_file = save_picture(form.img.data)
            view = pic_file
        print(view)
        gallery = Pension(name=form.name.data,farmerid=form.farmerid.data,address=form.address.data,gender=form.gender.data,dob=form.dob.data,phone=form.phone.data,email=form.email.data,block=form.block.data,panchayath=form.panchayath.data,village=form.village.data,bank=form.bank.data,accountnum=form.accountnum.data,aadharnum=form.aadharnum.data,img=view)
        db.session.add(gallery)
        db.session.commit()
        print(gallery)
        flash('image added')
        return redirect('/pension')
    return render_template('pension.html',form=form)    

@app.route('/pension_an',methods=['POST','GET'])
def pension_an():
    form=An_pension()
    view="default.jpg"
    if form.validate_on_submit():
        if form.img.data:
            pic_file = save_picture(form.img.data)
            view = pic_file
        print(view)
        gallery = Pension_an(name=form.name.data,farmerid=form.farmerid.data,address=form.address.data,gender=form.gender.data,dob=form.dob.data,phone=form.phone.data,email=form.email.data,block=form.block.data,panchayath=form.panchayath.data,village=form.village.data,bank=form.bank.data,accountnum=form.accountnum.data,aadharnum=form.aadharnum.data,img=view)
        db.session.add(gallery)
        db.session.commit()
        print(gallery)
        flash('image added')
        return redirect('/pension_an')
    return render_template('pension_an.html',form=form)    


@app.route('/pmfasal',methods=['POST','GET'])
def pmfasal():
    form=Pmfasal()
    view="default.jpg"
    if form.validate_on_submit():
        if form.img.data:
            pic_file = save_picture(form.img.data)
            view = pic_file
        print(view)
        gallery = Pm_fasal(name=form.name.data,address=form.address.data,gender=form.gender.data,dob=form.dob.data,phone=form.phone.data,email=form.email.data,block=form.block.data,panchayath=form.panchayath.data,village=form.village.data,bank=form.bank.data,accountnum=form.accountnum.data,aadharnum=form.aadharnum.data,img=view)
        db.session.add(gallery)
        db.session.commit()
        print(gallery)
        flash('image added')
        return redirect('/pmfasal')
    return render_template('pmfasal.html',form=form)


@app.route('/adlayout')
def adlayout():
    return render_template('adlayout.html')


@app.route('/ad_layout')
def ad_layout():
    return render_template('ad_layout.html')

@app.route('/slayout')
def slayout():
    return render_template('slayout.html')

@app.route('/flayout')
def flayout():
    return render_template('flayout.html')

@app.route('/f_layout')
def f_layout():
    return render_template('f_layout.html')

@app.route('/s_layout')
def s_layout():
    return render_template('s_layout.html')

@app.route('/an_layout')
def an_layout():
    return render_template('an_layout.html')

@app.route('/common')
def common():
    return render_template('common.html')

@app.route('/common_agri')
def common_agri():
    return render_template('common_agri.html')

@app.route('/com_live')
def com_live():
    return render_template('com_live.html')

@app.route('/com_cow')
def com_cow():
    return render_template('com_cow.html')

@app.route('/com_goat')
def com_goat():
    return render_template('com_goat.html')

@app.route('/com_hen')
def com_hen():
    return render_template('com_hen.html')

@app.route('/com_loanz')
def com_loanz():
    return render_template('com_loanz.html')

@app.route('/com_soilh')
def com_soilh():
    return render_template('com_soilh.html')

@app.route('/com_loan')
def com_loan():
    return render_template('com_loan.html')


@app.route('/com_shm')
def com_sshm():
    return render_template('com_shm.html')

@app.route('/com_pension')
def com_pension():
    return render_template('com_pension.html')

@app.route('/com_calamity')
def com_calamity():
    return render_template('com_calamity.html')

@app.route('/com_onecrore')
def com_onecrore():
    return render_template('com_onecrore.html')

@app.route('/com_poly')
def com_poly():
    return render_template('com_poly.html')

@app.route('/com_elect')
def com_elect():
    return render_template('com_elect.html')

@app.route('/com_mac')
def com_mac():
    return render_template('com_mac.html')

@app.route('/com_ferti')
def com_ferti():
    return render_template('com_ferti.html')

@app.route('/com_cropins')
def com_cropins():
    return render_template('com_cropins.html')

@app.route('/com_pmk')
def com_pmk():
    return render_template('com_pmk.html')

@app.route('/addfeed',methods=['POST','GET'])
def addfeed():
   if request.method=='POST':
        fname=request.form['fname']
        lname=request.form['lname']
        email=request.form['email']
        phone=request.form['phone']
        message=request.form['message']
   try:
        addfeed=Addfeed(fname=fname,lname=lname,email=email,phone=phone,message=message)
        db.session.add(addfeed)
        db.session.commit()
        message=Markup("*****successfully inserted*****")
        flash(message)
        return redirect('/addfeed')
   except Exception as e:
        print(e)
   return render_template('addfeed.html')

@app.route('/add_feed',methods=['POST','GET'])
def add_feed():
   if request.method=='POST':
        fname=request.form['fname']
        lname=request.form['lname']
        email=request.form['email']
        phone=request.form['phone']
        message=request.form['message']
   try:
        addfeed=Addfeed(fname=fname,lname=lname,email=email,phone=phone,message=message)
        db.session.add(addfeed)
        db.session.commit()
        message=Markup("*****successfully inserted*****")
        flash(message)
        return redirect('/add_feed')
   except Exception as e:
        print(e)
   return render_template('add_feed.html')


@app.route('/add_notification',methods=['POST','GET'])
def add_notification():
    form=Notice()
    view="default.jpg"
    if form.validate_on_submit():
        print(view)
        gallery = Addnotice(subject=form.subject.data,details=form.details.data,date=form.date.data,contactnum=form.contactnum.data,email=form.email.data)
        db.session.add(gallery)
        db.session.commit()
        print(gallery)
        flash('image added')
        return redirect('/add_notification')
    return render_template('add_notification.html',form=form)


@app.route('/regforms_far')
def regforms_far():
    return render_template('regforms_far.html')


@app.route('/farmerview')
def farmerview():
    Pap = Regfarmer.query.all()
    return render_template('farmerview.html',Pap=Pap)

@app.route('/animalfar_view')
def animalfar_view():
    Pap = Animalfarmer.query.all()
    return render_template('animalfar_view.html',Pap=Pap)
 
@app.route('/sfarmerview')
def sfarmerview():
    Pap = Regfarmer.query.all()
    return render_template('sfarmerview.html',Pap=Pap)

@app.route('/sfarmerviewdele/<int:id>')
def sfarmerviewdele(id):
    upcus = Regfarmer.query.get_or_404(id)
    try:
        db.session.delete(upcus)
        db.session.commit()
        return redirect('/sfarmerview')
    except:
        return 'NOT committed'
 
@app.route('/farmerviewdele/<int:id>')
def farmerviewdele(id):
    upcus = Regfarmer.query.get_or_404(id)
    try:
        db.session.delete(upcus)
        db.session.commit()
        return redirect('/farmerview')
    except:
        return 'NOT committed'

        
@app.route('/app_farmer/<int:id>',methods=['GET','POST'])
def app_farmer(id):
    a=Regfarmer.query.get_or_404(id)
    if request.method == 'POST':
        a.name = request.form['name']
        a.email = request.form['email']
        a.status= request.form['status']
        password=a.password
        pb = Login(email=a.email,usertype='Farmer',password=password)
        print('pb')
        try:
            db.session.add(pb)
            db.session.commit()
            return redirect('/sfarmerview')
        except Exception as e:
            
            print(e)

    return render_template('app_farmer.html',a=a)
 
 

  



@app.route('/far_feedback')
def far_feedback():
    return render_template('far_feedback.html')

@app.route('/tableview')
def tableview():
    return render_template('tableview.html')

@app.route('/faraddprod')
def faraddprod():
    return render_template('faraddprod.html')


@app.route('/addprod',methods=['POST','GET'])
def addprod():
    Pap = Addprod.query.all()
    form=Prodadd()
    view="default.jpg"
    if form.validate_on_submit():
        if form.pic.data:
            pic_file = save_picture(form.pic.data)
            view = pic_file
        print(view)
        gallery = Addprod(productname=form.productname.data,productcat=form.productcat.data,features=form.features.data,price=form.price.data,contactnum=form.contactnum.data,img=view)
        db.session.add(gallery)
        db.session.commit()
        print(gallery)
        flash('image added')
        return redirect('/addprod')
    return render_template('addprod.html',form=form,Pap=Pap)

@app.route('/machine_rent',methods=['POST','GET'])
def machine_rent():
    Pap = Machine_rent.query.all()
    form=Rentmachine()
    view="default.jpg"
    if form.validate_on_submit():
        if form.pic.data:
            pic_file = save_picture(form.pic.data)
            view = pic_file
        print(view)
        gallery = Machine_rent(productname=form.productname.data,brant=form.brant.data,rentrupee=form.rentrupee.data,features=form.features.data,contactnum=form.contactnum.data,img=view)
        db.session.add(gallery)
        db.session.commit()
        print(gallery)
        flash('image added')
        return redirect('/machine_rent')
    return render_template('machine_rent.html',form=form,Pap=Pap)

@app.route('/magazine_add',methods=['POST','GET'])
def magazine_add():
    Pap = Magazine.query.all()
    form=Add_magazine()
    view="default.jpg"
    if form.validate_on_submit():
        if form.pic.data:
            pic_file = save_picture(form.pic.data)
            view = pic_file
        print(view)
        gallery = Magazine(name=form.name.data,author=form.author.data,publisher=form.publisher.data,features=form.features.data,rupees=form.rupees.data,img=view)
        db.session.add(gallery)
        db.session.commit()
        print(gallery)
        flash('image added')
        return redirect('/magazine_add')
    return render_template('magazine_add.html',form=form,Pap=Pap)



@app.route('/addevent',methods=['POST','GET'])
def addevent():
    Pap = Addevent.query.all()
    form=Eventadd()
    view="default.jpg"
    if form.validate_on_submit():
        if form.pic.data:
            pic_file = save_picture(form.pic.data)
            view = pic_file
        print(view)
        gallery = Addevent(eventname=form.eventname.data,description=form.description.data,date=form.time.data,time=form.time.data,place=form.place.data,contactnum=form.contactnum.data,img=view)
        db.session.add(gallery)
        db.session.commit()
        print(gallery)
        flash('image added')
        return redirect('/addevent')
    return render_template('addevent.html',form=form,Pap=Pap)

@app.route('/loan_form',methods=['POST','GET'])
def loan_form():
    form=Formloan()
    view="default.jpg"
    if form.validate_on_submit():
        if form.img.data:
            pic_file = save_picture(form.img.data)
            view = pic_file
        print(view)
        gallery = Loanform(name=form.name.data,address=form.address.data,gender=form.gender.data,dob=form.dob.data,phone=form.phone.data,email=form.email.data,block=form.block.data,panchayath=form.panchayath.data,village=form.village.data,bank=form.bank.data,accountnum=form.accountnum.data,aadharnum=form.aadharnum.data,rationnum=form.rationnum.data,area=form.area.data,projtopic=form.projtopic.data,projdisc=form.projdisc.data,img=view)
        db.session.add(gallery)
        db.session.commit()
        print(gallery)
        flash('image added')
        return redirect('/loan_form')
    return render_template('loan_form.html',form=form)

@app.route('/loan_animal',methods=['POST','GET'])
def loan_animal():
    form=Loan_animals()
    view="default.jpg"
    if form.validate_on_submit():
        if form.img.data:
            pic_file = save_picture(form.img.data)
            view = pic_file
        print(view)
        gallery = Loananimal(name=form.name.data,address=form.address.data,gender=form.gender.data,dob=form.dob.data,phone=form.phone.data,email=form.email.data,block=form.block.data,panchayath=form.panchayath.data,village=form.village.data,bank=form.bank.data,accountnum=form.accountnum.data,aadharnum=form.aadharnum.data,rationnum=form.rationnum.data,area=form.area.data,projtopic=form.projtopic.data,projdisc=form.projdisc.data,img=view)
        db.session.add(gallery)
        db.session.commit()
        print(gallery)
        flash('image added')
        return redirect('/loan_animal')
    return render_template('loan_animal.html',form=form)


@app.route('/viewproduct')
def viewproduct():
    Pap = Addprod.query.all()
    return render_template('viewproduct.html',Pap=Pap)

@app.route('/viewfarmerproduct')
def viewfarmerproduct():
    Pap = Addprod.query.all()
    return render_template('viewfarmerproduct.html',Pap=Pap)

@app.route('/f_view_loanform')
def f_view_loanform():
    Pap = Loanform.query.all()
    return render_template('f_view_loanform.html',Pap=Pap)

@app.route('/viewevent')
def viewevent():
    Pap = Addevent.query.all()
    return render_template('viewevent.html',Pap=Pap)


@app.route('/viewfarmerevent')
def viewfarmerevent():
    Pap = Addevent.query.all()
    return render_template('viewfarmerevent.html',Pap=Pap)



@app.route('/addproddele/<int:id>')
def addproddele(id):
    upcus = Addprod.query.get_or_404(id)
    try:
        db.session.delete(upcus)
        db.session.commit()
        return redirect('/addprod')
    except:
        return 'NOT committed'


def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

def save_picture(form_picture):
    random_hex = random_with_N_digits(14)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = str(random_hex) + f_ext
    picture_path = os.path.join(app.root_path, 'static/pics', picture_fn)
    
    output_size = (500, 500)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_fn

