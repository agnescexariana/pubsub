#!flask-env/bin/python
import MySQLdb		
from flask import Flask, request
import paho.mqtt.client as mqtt
import json

app = Flask(__name__)

db = MySQLdb.connect(host="127.0.0.1",
                           user = "root",
                           passwd = "",
                           db = "rumahsakit")

@app.route('/', methods=['GET'])
def index():
    cur = db.cursor()
    cur.execute('''SELECT * FROM pasien''')
    all_rows = cur.fetchall()
    data = json.dumps(all_rows)
    print data
    cur.close()
    return data

@app.route('/print_data2', methods=['GET'])
def get_pasien():
	cur = db.cursor()
	id_pasienpost = request.args.get('id_pasien')
	cur.execute('''SELECT * FROM pasien WHERE id_pasien=%s ''',(id_pasienpost,))
	data_pasien = cur.fetchone()
	data = json.dumps(data_pasien) #encode
	print "Get data =" + data	
	cur.close()
	return data

@app.route('/registrasi', methods = ['GET'])
def registrasi():
	id_pasienpost = request.args.get('id_pasien')
	nama_post = request.args.get('nama')
	gender_post = request.args.get('gender')
	agama_post = request.args.get('agama')
	tgl_post = request.args.get('BirthDate')
	bulan_post = request.args.get('BirthMonth')
	tahun_post = request.args.get('BirthYear')
	email_post = request.args.get('Email_id')
	tlp_post = request.args.get('tlp')
	alamat_post = request.args.get('alamat')
	darah_post = request.args.get('darah')
	riwayat_post = request.args.get('riwayat_penyakit')

	cur = db.cursor()
	cur.execute("""INSERT INTO pasien (id_pasien,
					nama,
					gender,
					agama, 
					BirthDate,
 					BirthMonth,
					BirthYear,
					Email_id, 
					tlp, 
					alamat,
					darah,
					riwayat_penyakit)
			values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""", (id_pasienpost, nama_post, gender_post, agama_post, tgl_post, bulan_post, tahun_post, email_post, tlp_post, alamat_post, darah_post, riwayat_post))
	db.commit() #to tell the database to save all the changes
	
	cur.execute('''SELECT * FROM pasien WHERE id_pasien=%s ''',(id_pasienpost,))
	all_rows = cur.fetchone()
	data = {"status": "insert", "datapasien": all_rows}
	client.publish("pubsub/pasien/2", payload=json.dumps(data), qos=1) #publish data into broker
	
	print ">> Data Successfully Inserted"
	cur.close()
	return "Succesfully inserted into database"


@app.route('/update', methods=['PUT'])
def update_pasien():
		cur = db.cursor()
		id_pasienpost = request.args.get('id_pasien')
		nama_post = request.args.get('nama')
		gender_post = request.args.get('gender')
		agama_post = request.args.get('agama')
		tgl_post = request.args.get('BirthDate')
		bulan_post = request.args.get('BirthMonth')
		tahun_post = request.args.get('BirthYear')
		email_post = request.args.get('Email_id')
		tlp_post = request.args.get('tlp')
		alamat_post = request.args.get('alamat')
		darah_post = request.args.get('darah')
		riwayat_post = request.args.get('riwayat_penyakit')

		if nama_post:
			cur.execute("UPDATE pasien SET nama=%s WHERE id_pasien=%s", (nama_post, id_pasienpost,))
			db.commit()
		if gender_post:
			cur.execute("UPDATE pasien SET gender=%s WHERE id_pasien=%s", (gender_post, id_pasienpost,))
			db.commit()
		if agama_post:
			cur.execute("UPDATE pasien SET agama=%s WHERE id_pasien=%s", (agama_post, id_pasienpost,))
			db.commit()
		if tgl_post:
			cur.execute("UPDATE pasien SET BirthDate=%s WHERE id_pasien=%s", (tgl_post, id_pasienpost,))
			db.commit()
		if bulan_post:
			cur.execute("UPDATE pasien SET BirthMonth=%s WHERE id_pasien=%s", (bulan_post, id_pasienpost,))
			db.commit()
		if tahun_post:
			cur.execute("UPDATE pasien SET BirthYear=%s WHERE id_pasien=%s", (nama_post, id_pasienpost,))
			db.commit()
		if email_post:
			cur.execute("UPDATE pasien SET Email_id=%s WHERE id_pasien=%s", (email_post, id_pasienpost,))
			db.commit()
		if tlp_post:
			cur.execute("UPDATE pasien SET tlp=%s WHERE id_pasien=%s", (tlp_post, id_pasienpost,))
			db.commit()
		if alamat_post:
			cur.execute("UPDATE pasien SET alamat=%s WHERE id_pasien=%s", (alamat_post, id_pasienpost,))
			db.commit()
		if darah_post:
			cur.execute("UPDATE pasien SET darah=%s WHERE id_pasien=%s", (darah_post, id_pasienpost,))
			db.commit()
		if riwayat_post:
			cur.execute("UPDATE pasien SET riwayat_penyakit=%s WHERE id_pasien=%s", (riwayat_post, id_pasienpost,))
			db.commit()

		cur.execute('''SELECT * FROM pasien WHERE id_pasien=%s ''',(id_pasienpost,))
		datapasien = cur.fetchone()
		data = {"status": "update", "datapasien": datapasien}
		client.publish("pubsub/pasien/2", payload=json.dumps(data), qos=1)
		
		print ">> Data Successfully Updated"
		cur.close()
		return "Data Successfully Updated"

		

@app.route('/delete', methods=['DELETE'])
def delete_pasien():
	cur = db.cursor()
	id_pasienpost = request.args.get('id_pasien')
	cur.execute("DELETE FROM pasien WHERE id_pasien=%s",(id_pasienpost,))
	db.commit() # Commit the change
	data = {"status": "delete", "datapasien": id_pasienpost}
	client.publish("pubsub/pasien/2", payload=json.dumps(data), qos=1)
	
	print ">> Data Successfully Deleted"
	cur.close
	return "Data Successfully Deleted"	

if __name__ == "__main__":
    client = mqtt.Client("pub1", clean_session=False)
    client.connect("127.0.0.1", 1883)
    client.publish('debug', 'server running')
    app.debug = True
    app.run()
