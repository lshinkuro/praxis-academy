from flask import Flask
import json

app = Flask(__name__)

with open('./file.json') as f:
    file=json.loads(f.read())
    i = 0
class User:
    def __init__(self,name,kelas,jeniskelamin,umur):
        self.name =name
        self.kelas = kelas
        self.jeniskelamin =jeniskelamin
        self.umur =umur

    def get_current_user():
        return User(
            file[i][("nama")],
            file[i][("kelas")],
            file[i][("jenis kelamin")],
            file[i][("umur")])

@app.route("/me")
def me_api():

    user = User.get_current_user()
    return {
        "username": user.name,
        "kelas": user.kelas,
        "jenis kelamin":user.jeniskelamin,
        "umur":user.umur
        
    }
if __name__=="__main__":
    app.run(debug=True)
