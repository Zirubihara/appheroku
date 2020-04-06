from flask import Flask, render_template # render_template pozwala nam na wyswietlanie
#pliku html

#from flask import *

#z paczki flask zaimportuj Flaska

app = Flask(__name__)
#app - nazwa obiektu Flask
#gracz1 = GraczKoszykowki(....)


#@ - adnotacja
#app - nazwa naszej aplikacji
#.route - metoda route
@app.route("/")
def index():                    #tworzymy funkcje index
    return render_template("index.html")            #sprawia ze wyswietli nam sie napis witaj

#www.przykladowastrona.pl/kontakt
@app.route("/kontakt")
def kontakt():
    return render_template("kontakt.html")


if __name__ == '__main__':      #konstrukcja warunkowa
    app.run()






#mamy dwa rodzaje stron internetowych 1) statyczne 2)Dynamiczne
#HTML, CSS - statyczne
#Python, HTML, CSS - dynamiczne

#Flask, Django



