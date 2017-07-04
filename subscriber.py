#!flask-env/bin/python
import paho.mqtt.client as mqtt
import json, MySQLdb
import thread, time


def on_connect(client, userdata, flags, rc):
 	print("connect rc: "+str(rc))

def on_subscribe(client, userdata, mid, granted_qos):
	print("Subscribed: "+" "+str(granted_qos))

def on_message(client, userdata, message):
    print(">> Received message : " + str(message.payload))
    print(">> On topic : " + message.topic + " with QoS : " + str(message.qos))
    data = json.loads(message.payload) #parse json
    print ">> Action : " + data['status']
    
    curs=d.cursor()

	# #INSERT DATA
    if data['status'] == "insert":
    	curs.execute("INSERT into pasien VALUES %s", (data['datapasien'],))
    	d.commit()
    	curs.close()

    #DELETE DATA	
    if data['status'] == "delete":
    	id_pasienpost = data['datapasien']
    	curs.execute("DELETE FROM pasien WHERE id_pasien=%s",(id_pasienpost,))
    	d.commit() 
    	curs.close()

    # UPDATE DATA
    if data['status'] == "update":
    	row = data['datapasien']
        i = len(row)
        print i
        for i in row :
                id_pasien = row [0]
                nama = row[1]
                gender = row[2]
                agama = row[3]
                tgl = row[4]
                bulan = row[5]
                tahun = row[6]
                email = row[7]
                tlp = row[8]
                alamat = row[9]
                darah = row[10]
                riwayat = row[11]
        
        # curs = d.cursor()
        curs.execute("""UPDATE pasien SET nama=%s, 
                                            gender=%s, 
                                            agama=%s,
                                            BirthDate=%s, 
                                            BirthMonth=%s, 
                                            BirthYear=%s, 
                                            Email_id=%s, 
                                            tlp=%s, 
                                            alamat=%s, 
                                            darah=%s,
                                            riwayat_penyakit=%s 
                                            WHERE id_pasien=%s""", 
                        (nama, gender, agama, tgl, bulan, tahun, email, tlp, alamat, darah, riwayat, id_pasien,))
        d.commit()
        curs.close()


    print (">> Data Successfully Subscribed")


def on_log(client, userd, level, string):
	print(string)

def h():
    global input_client
    print "Client ID : " +str(input_client)
    client = mqtt.Client("subs"+str(input_client),clean_session=False)
    client.on_connect = on_connect
    client.connect("127.0.0.1", 1883)
    client.subscribe("pubsub/pasien/#", qos=1)
    client.on_subscribe = on_subscribe
    client.on_message = on_message
    client.loop_forever()

try:
    input_client = 0
    input_client = input("Input ID Client : ")
    namadb="rumahsakit"+str(input_client)
    d = MySQLdb.connect(host="127.0.0.1",
                                user = "root",
                                passwd = "",
                                db = ""+str(namadb))
    h()

except KeyboardInterrupt:
    print ("::Connection Closed") 
