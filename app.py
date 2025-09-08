from flask import Flask, render_template, request

app = Flask(__name__)

# Hlavní stránka s formulářem
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        jmeno = request.form.get("jmeno")
        email = request.form.get("email")
        zprava = request.form.get("zprava")
        # Zde můžeš uložit data do databáze nebo poslat e-mail
        return f"<h2>Děkujeme, {jmeno}! Vaše zpráva byla přijata.</h2>"
    return render_template("form.html")  # form.html uložený v templates/

if __name__ == "__main__":
    app.run(debug=True)
