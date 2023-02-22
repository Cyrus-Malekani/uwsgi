from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/octa_db'

def get_mongo_client():
    mongo_uri = app.config['MONGO_URI']
    client = MongoClient(mongo_uri)
    return client


@app.route('/')
def index():
    videos = ['brag.mp4','tvny.mp4','9.HIV_103 15sec.mp4', '12.HIV15EP02TON.mp4', 'singingbee.mp4', '3.diagnos_x_klar.mp4', 'Podcast_13.mp4', '2.cross_promo_2_klar.mp4',
             '25.Serie_A_klar.mp4','Podcast_12.mp4','Podcast_14.mp4','Podcast_11.mp4','6.film_v4_lor.mp4','27.Talladega_Nights_klar.mp4','23.my_super_ex-girlfriend.mp4',
             '21.lady_in_the_water.mp4','29.the_devil_wears_prada.mp4','Shaping.mp4','31.trailer Copy 30sec.mp4','22.movies_in_march.mp4','10.HIV_103 30sec.mp4']
    return render_template('index.html', videos=videos)


@app.route('/music')
def music():
    video = ['music/Chimar_nr_2.mp4']
    return render_template('music.html', video=video)


if __name__ == '__main__':
    app.run('0.0.0.0')
