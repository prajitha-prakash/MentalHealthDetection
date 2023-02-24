from flask import Flask, render_template, request, redirect
from DBConnection import Db

app = Flask(__name__)


@app.route('/', methods=['get', 'post'])
def hello_world():
    if request.method=="POST":
        username=request.form['t1']
        password=request.form['t2']
        db=Db()
        res=db.selectOne("SELECT * FROM login WHERE username='"+username+"' AND PASSWORD='"+password+"'")
        if res is None:
            return "<script>alert('Invalid details');window.location='/';</script>"
        else:
            type=res['usertype']
            if type=="admin":
                return redirect("/admin_home")
            else:
                return "<script>alert('Unauthorised user');window.location='/';</script>"
    return render_template("login.html")


@app.route("/admin_home")
def admin_home():
    return render_template("admin/admin_home.html")


@app.route("/admin_psychiatrist_approval")
def admin_psychiatrist_approval():
    db=Db()
    res=db.select("SELECT * FROM `psychiatrist`, login WHERE `psychiatrist`.psychiatrist_id=login.login_id AND login.usertype='pending'")
    return render_template("admin/psychiatrist_approval.html", data=res)

@app.route("/approve_psych/<pid>")
def approve_psych(pid):
    db=Db()
    db.update("update login set usertype='pyschiatrist' where login_id='"+pid+"'")
    return redirect("/admin_psychiatrist_approval")
@app.route("/reject_psych/<pid>")
def reject_psych(pid):
    db=Db()
    db.update("update login set usertype='rejected' where login_id='"+pid+"'")
    return redirect("/admin_psychiatrist_approval")



@app.route("/admin_approved_psychiatrist")
def admin_approved_psychiatrist():
    db=Db()
    res=db.select("SELECT * FROM `psychiatrist`, login WHERE `psychiatrist`.psychiatrist_id=login.login_id AND login.usertype='pyschiatrist'")
    return render_template("admin/approved_psychiatrist.html", data=res)


@app.route("/admin_rejected_psychiatrist")
def admin_rejected_psychiatrist():
    db=Db()
    res=db.select("SELECT * FROM `psychiatrist`, login WHERE `psychiatrist`.psychiatrist_id=login.login_id AND login.usertype='rejected'")
    return render_template("admin/rejected_psychiatrist.html", data=res)



@app.route("/admin_view_users")
def admin_view_users():
    db=Db()
    res=db.select("SELECT * FROM user")
    print(res)
    return render_template("admin/view_users.html", data=res)

@app.route("/admin_view_complaints")
def admin_view_complaints():
    db=Db()
    res=db.select("SELECT * FROM complaint, USER WHERE user.user_id=complaint.user_id ORDER BY complaint.cid DESC")
    return render_template("admin/view_complaints.html", data=res)


@app.route("/send_reply/<cid>", methods=['get', 'post'])
def send_reply(cid):
    if request.method=="POST":
        reply=request.form['t1']
        db=Db()
        db.update("UPDATE complaint set reply='"+reply+"' WHERE cid='"+cid+"'")
        return redirect("/admin_view_complaints")
    else:
        return render_template("admin/send_reply.html")

@app.route("/change_password", methods=['get', 'post'])
def change_password():
    if request.method=="POST":
        psw=request.form['t1']
        db=Db()
        db.update("update login set password='"+psw+"' where usertype='admin'")
        return "<script>alert('Password changed');window.location='/';</script>"
    return render_template("admin/change_password.html")





import time
##################              psychiatrist
@app.route("/psych_reg", methods=['get','post'])
def psych_reg():
    if request.method=="POST":
        name=request.form['t1']
        email=request.form['t2']
        phn=request.form['t3']
        qual=request.form['t4']
        exp=request.form['t5']
        image=request.files['f1']
        dt=time.strftime("%Y%m%d_%H%M%S")
        image.save(r"C:\Users\USER\PycharmProjects\mental_health\static\pic\\" + dt + ".jpg")
        path="/static/pic/" + dt +".jpg"
        psw=request.form['t6']
        db=Db()
        lid=db.insert("INSERT INTO login(username, PASSWORD, usertype) VALUES('"+email+"', '"+psw+"', 'pending')")
        db.insert("INSERT INTO `psychiatrist` values('"+str(lid)+"', '"+name+"', '"+email+"', '"+phn+"' ,'"+qual+"' , '"+exp+"', '"+path+"')")
        return "<script>alert('Registered successfully');window.location='/';</script>"
    else:
        return render_template("pysh_reg.html")


if __name__ == '__main__':
    app.run()
