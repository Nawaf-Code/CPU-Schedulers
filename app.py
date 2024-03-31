from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template("index.html")
@app.route('/result',methods = ['POST', 'GET'])
def result():
    pnames = request.form.getlist('pname')
    btime = request.form.getlist('time')
    radio = request.form['radio1']
    total_time = 0
    dic = {}
    dic2 = {}
    order = {}
    order2 = {}
    chartval = []
    chartname = []
    charstart = [0]
    
    if radio == 's1':
        end = 0
        for k , val in zip(pnames,btime):
            #chart.update({k:end+int(val)})
            chartname.append(k)
            chartval.append(end+int(val))
            end = end+int(val) 
    elif radio == 's2':
        end = 0
        for k , val in zip(pnames,btime):
            dic.update({k:int(val)})
        order = dict(sorted(dic.items(), key=lambda item: item[1]))
        for k, val in zip(order.keys(),order.values()):
            #chart.update({k:end+val})
            chartname.append(k)
            chartval.append(end+val)
            end = end+val
    elif radio == 's3':
        end = 0
        priority = request.form.getlist('priority')
        for k , val in zip(pnames,priority):
            dic.update({k:int(val)})

        for k , val in zip(priority,btime):
            dic2.update({k:int(val)})
        order = dict(sorted(dic.items(), key=lambda item: item[1]))
        order2 = dict(sorted(dic2.items()))

        for k, val in zip(order.keys(), order2.values()):
            #chart.update({k:end+val})
            chartname.append(k)
            chartval.append(end+val)
            end = end+val
    else:
        output = request.form.to_dict()
        robin = output['robin']
        bbtime = []
        for val in btime:
            bbtime.append(int(val))
        total_time = 0    
        for i in bbtime:
            total_time=total_time+i
        i = 0
        end = 0
        while True:
            if bbtime[i] <= int(robin):
                #chart.update({pnames[i]:end+bbtime[i]})
                chartname.append(pnames[i])
                chartval.append(end+bbtime[i])
                end = end+bbtime[i]
                del pnames[i]
                del bbtime[i]
                i-=1
                if end == total_time:
                    break
            else:
                #chart.update({pnames[i]:end+int(robin)})
                chartname.append(pnames[i])
                chartval.append(end+int(robin))
                end = end+int(robin)
                bbtime[i] = bbtime[i] - int(robin)
            if i <= len(pnames)-2:
                i+=1
            else:
                i = 0
    charstart = charstart + chartval

        
            
    return render_template("result.html" ,chn = zip(chartname,charstart,chartval), chv = zip(charstart,chartval))

if __name__ == "__main__":
    app.run(debug=True,port=5999)