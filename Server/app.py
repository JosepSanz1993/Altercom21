#Llibreries del framework flask
from flask import Flask
from flask import render_template, request, redirect, url_for, session
from db.db import User_MB_Management
from crud import crud
from userspace import userspace
from check_dni import check
from hash import toHash
from datetime import timedelta

#instancies de classes
space = userspace()
c_crud = crud()
cur = User_MB_Management()
check_dni = check()
hash = toHash()

# App principal
app = Flask(__name__,template_folder='template')

@app.before_request
def make_session_permanent():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=10)
    
@app.route('/')
def home():
    return render_template('index.html') 

@app.route('/client')
def client():
    if session['Rol'] == 'Client':
        enterprise = space.Select_buisness(_name,hash.get_Hash(_password))
        dni = space.Select_Dni(_name,hash.get_Hash(_password))
        d_data = space.Select_Backup(dni)
        return render_template('client.html',title=enterprise,data=d_data)
    else:
        return redirect(url_for('Log_Out'))
    
@app.route('/admin')
def admin():
    if session['Rol'] == 'Admin':
        manage = c_crud.All_Users()
        return render_template('admin.html',data =manage)
    else:
        return redirect(url_for('Log_Out'))

@app.route('/acceso-login', methods = ["GET","POST"])
def login():
    if request.method == 'POST' and 'txtName' in request.form and 'txtPassword' in request.form:
        global _name,_password
        _name = request.form['txtName']
        _password = request.form['txtPassword']
        account = cur.Select_User_Login('Alta_Users',_name,hash.get_Hash(_password))
        if account:
            session['logueado'] = True
            session['id'] = account[0]
            session['Rol'] = account[3]
            if session['Rol'] == "Admin":
                return redirect(url_for('admin'))
            
            elif session['Rol'] == "Client":
                return redirect(url_for('client'))
        else:
            return render_template('index.html',mensaje="Usuari O Contrasenya incorrecta")

@app.route('/storage', methods=['Post'])
def adduser():
    dni = request.form['dni']
    name = request.form['name']
    rol = request.form['rol']
    password = request.form['password']
    empresa = request.form['empresa']
    if dni and name and rol and password and empresa:
        if check_dni.check_dni(dni):
            c_crud.Create_Users(dni,name,rol,hash.get_Hash(password),empresa)
        else:
            manage = c_crud.All_Users()
            return render_template('admin.html' ,data=manage,mensaje="DNI no valid o repetit")
    return redirect(url_for('admin'))

@app.route('/delete/<string:dni>')
def delete(dni):
    if c_crud.Check_Rol(dni)=='Client' and space.Count_Backup_table(dni)>=0:
        space.Delete_Backup_Table(dni)
        c_crud.Delete_Users(dni)
    else:
        c_crud.Delete_Users(dni)
    return redirect(url_for('admin'))

@app.route('/edit/<string:id>', methods=['POST'])
def edit(id):
    name = request.form['name']
    password = request.form['password']
    empresa = request.form['empresa']
    if name and password and empresa:
        c_crud.Edit_Users(id,name,hash.get_Hash(password),empresa)
    return redirect(url_for('admin'))

@app.route('/logout')
def Log_Out():
    session.clear()
    return render_template('index.html')

@app.route('/TimeOff')
def TimeOff():
    session.clear()
    return render_template('index.html')


if __name__ == '__main__':
   app.secret_key = "key"
   app.run(debug=True, host='0.0.0.0', port=5000, threaded=True)

