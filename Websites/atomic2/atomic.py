from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
  return render_template('PAGINA PRINCIPALA.html')

@app.route("/about")
def about():
  return render_template('INFO - CONTACT.html', title='CONTACT - INFO')

@app.route("/baschet")
def baschet():
  return render_template('BASCHET.html', title='BASCHET')

@app.route("/volei")
def volei():
  return render_template('VOLEI.html', title='VOLEI')


# PT BASCHET ----------------------------------->

@app.route("/baschet_poze")
def baschet_poze():
  return render_template('baschet_poze.html', title='BASCHET - POZE')

# SUBDIVIZIUNI BASCHET POZE -------->

@app.route("/cs_atomic_viitorul")
def cs_atomic_viitorul():
  return render_template('cs_atomic_viitorul.html', title='POZE | ATOMIC BLAJ - VIITORUL DEVA')

@app.route("/baschet_poze_malembach_2018")
def baschet_poze_malembach_2018():
  return render_template('baschet_poze_malembach_2018.html', title='POZE | CUPA MALEMBACH BASCHET SEBES - 2018')

@app.route("/blaj_sebes")
def blaj_sebes():
  return render_template('2004_2005_blaj_sebes.html', title='POZE | ATOMIC BLAJ - MALEMBACH SEBES')

@app.route("/blaj_sebes_2006_2008")
def blaj_sebes_2006_2008():
  return render_template('blaj_sebes_2006_2008.html', title='POZE | ATOMIC BLAJ - MALEMBACH SEBES')

@app.route("/atomic_viitorul_deva")
def atomic_viitorul_deva():
  return render_template('atomic_viitorul_deva.html', title='POZE | ATOMIC BLAJ - VIITORUL DEVA')

# <---

@app.route("/baschet_membrii")
def baschet_membrii():
  return render_template('baschet_membrii.html', title='BASCHET - MEMBRII')

@app.route("/baschet_noutati")
def baschet_noutati():
  return render_template('baschet_noutati.html', title='BASCHET - NOUTATI')

# -----------> BACK <------------- #  !!!

@app.route("/inapoi")
def inapoi():
  return render_template('inapoi.html', title='INAPOI')

# PT VOLEI -------------------------------------->

@app.route("/volei_poze")
def volei_poze():
  return render_template('volei_poze.html', title='VOLEI - POZE')

# SUBDIVIZIUNI VOLEI POZE ----------->

@app.route("/volei_poze_one")
def volei_poze_one():
  return render_template('volei_poze_one.html', title='VOLEI - POZE')

@app.route("/volei_poze_two")
def volei_poze_two():
  return render_template('volei_poze_two.html', title='VOLEI - POZE')

@app.route("/volei_poze_tree")
def volei_poze_tree():
  return render_template('volei_poze_tree.html', title='VOLEI - POZE')

@app.route("/volei_poze_four")
def volei_poze_four():
  return render_template('volei_poze_four.html', title='VOLEI - POZE')

# <----

@app.route("/volei_membrii")
def volei_membrii():
  return render_template('volei_membrii.html', title='VOLEI - MEMBRII')

@app.route("/volei_noutati")
def volei_noutati():
  return render_template('volei_noutati.html', title='VOLEI - NOUTATI')




# ----------------------------------------------------------- #
  
if __name__ == "__main__": # TREBE PT A RULA DIRECT...
  app.run(debug = True)
