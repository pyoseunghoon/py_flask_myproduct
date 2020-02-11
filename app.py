from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.
app = Flask(__name__)

## URL 별로 함수명이 같거나,
## route('/') 등의 주소가 같으면 안됩니다.

@app.route('/')
def home():
    return render_template('myproductpage.html')

@app.route('/api/info', methods=['POST'])
def test_post():
    name_receive = request.form['name_give']
    count_receive = request.form['count_give']
    phonenumber_receive = request.form['phonenumber_give']
    address_receive = request.form['address_give']

    all_info = list(db.order_info.find({}))
    total_count = len(all_info)
    rank_receive = total_count + 1

    doc = {
        'rank': rank_receive,
        'name': name_receive,
        'count': int(count_receive),
        'address': address_receive,
        'phonenumber':phonenumber_receive
    }
    db.order_info.insert_one(doc)
    return jsonify({'result':'success'})

@app.route('/api/listing', methods=['GET'])
def test_get():
    all_info = list(db.order_info.find({},{'_id':0}))
    return jsonify({'result':'success', 'orders':all_info})

if __name__ == '__main__':
    app.run('0.0.0.0',port=5000,debug=True)