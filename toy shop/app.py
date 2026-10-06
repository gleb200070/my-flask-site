from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")

def home():

    toys = [

        {

            "name": "Гибкий дракон",

            "price": 304,

            "image": "toy3.png",

            "Avito": "https://www.avito.ru/moskva/kollektsionirovanie/gibkiy_drakon_3d-pechat_8456888513"

        },

        {

            "name": "Веселые котята",

            "price": 256,

            "image": "toy2.png",

            "Avito": "https://www.avito.ru/moskva/tovary_dlya_detey_i_igrushki/2_gibkih_kotenka-3d_pechat_igrushka_podarok_8358333701"

        },

        {

            "name": "Милый скат",

            "price": 273,

            "image": "toy1.png",

            "Avito": "https://www.avito.ru/moskva/kollektsionirovanie/gibkaya_igrushka_skat_3d-pechat_siniy_tsvet_8453643915?utm_campaign=native&utm_medium=item_page_ios&utm_source=soc_sharing"

        }

    ]

    return render_template("index.html", toys=toys)

app.run(debug=True)