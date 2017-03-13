from flask import Flask, render_template, request, redirect
from bokeh.plotting import figure
from bokeh.embed import components 
import quandl
import pandas as pd
from bokeh.models import Range1d


from bokeh.models import HoverTool, BoxSelectTool

app = Flask(__name__)

quandl.ApiConfig.api_key = "1VdR4_VUTyzaeDNjy77S"

TOOLS = 'box_zoom,box_select,crosshair,resize,reset'


@app.route('/index',methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    else:
		#request was a POST
		ticker = request.form['stock']
		plot_type = request.form['type']
		try:
			data = quandl.get("WIKI/"+ticker,collapse="daily")
		except:
			print 'error in getting ticker info for ticker ' + ticker
			print 'check symbol and try again'
			
		plot = figure(tools=TOOLS,title=ticker + ' from Quandle WIKI set',x_axis_label='date',y_axis_label='price ($)',x_axis_type='datetime')

		plot.line(data.index,data[plot_type],line_width=3)


		script, div = components(plot)

		return render_template('index.html', script=script, div=div)




if __name__ == '__main__':
  app.run(port=33507)
