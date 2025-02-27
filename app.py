from flask import Flask, render_template, request
import defuzzyfication as df
import inference as inf
import fuzzyfication as fz


def status(pm25:float, pm10:float,mq2:float) -> dict:
    pm25,pm10,mq2 = float(pm25),float(pm10),float(mq2)
    pic = {
        "pm25":str,
        "pm10":str,
        "mq2":str
    }
    if (pm25>0 and pm25<= 10):
        pic['pm25'] = "bersih"
    elif (pm25 > 10 and pm25<= 20 ):
        pic['pm25'] = "sedikit_bersih"
    elif (pm25 > 20 and pm25<= 35):
        pic['pm25'] = "sedikit_kotor"
    elif (pm25 > 35):
        pic['pm25'] = "kotor"
    
    if (pm10 > 0 and pm10 <= 22):
        pic['pm10'] = "bersih"
    elif (pm10 > 22 and pm10 <= 41):
        pic['pm10'] = "sedikit_bersih"
    elif (pm10 > 41 and pm10 <= 75):
        pic['pm10'] = "sedikit_kotor"
    elif (pm10 > 75):
        pic['pm10'] = "kotor"
        
    if (mq2 > 0 and mq2<=300):
        pic['mq2'] = "aman"
    elif (mq2 > 300 and mq2<=600):
        pic['mq2'] = "peringatan"
    elif (mq2 > 600):
        pic['mq2'] = "bahaya"
        
    return pic

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    return render_template("input.html")

@app.route("/result",methods=['GET','POST'])
def fuzzy():
    pm25_value = request.form.get("pm25")
    pm10_value = request.form.get("pm10")
    mq2_value = request.form.get("mq2")
    pic = status(pm25_value,pm10_value,mq2_value)
    data_pm25 = fz.fuzzy_PM25(pm25_value)
    data_pm10 = fz.fuzzy_PM10(pm10_value)
    data_mq2 = fz.fuzzy_MQ2(mq2_value)
    data = inf.rule(data_pm25,data_pm10,data_mq2)
    result = df.crisp(data)
    formated_result = "{:,.2f}".format(result)
    return render_template("result.html",
                           pm25_value = pm25_value,
                           pm10_value = pm10_value,
                           mq2_value = mq2_value,
                           pm25_status = pic['pm25'],
                           pm10_status = pic['pm10'],
                           mq2_status = pic['mq2'],
                           result = result,
                           formated_result = formated_result)

if __name__ == "__main__":
    app.run(debug=True)