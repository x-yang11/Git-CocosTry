from pyh import *
def tablecss(self,table = None,width='90%'):
	table.attributes['cellSpacing'] = 1;
	table.attributes['cellPadding'] = 1;
	table.attributes['border'] = 1;
	table.attributes['borderColor'] = '#666666';
	table.attributes['width'] = width;
 #set colum title bgcolor 
def tr_title_css(self,tr = None):
	tr.attributes['bgcolor'] = '#CCCC00';

#get summary info
def gentask_html():
	
	page = PyH("MyPage")
	#page.addCSS('myStylesheet1.css', 'myStylesheet2.css')
	#page.addJS('myJavascript1.js', 'myJavascript2.js')

	#<h1 align="center">MyTitle1</h1>
	page <<h1('MyTitle1',align='center')

	#<div align="center" id="myDiv1"><p id="myp1">my paragraph1</p>
	#</div>
	page << div(align='center',id='myDiv1') << p('my paragraph1',id='myp1')

	#<div id="myDiv2"><h2>title2 in div2<p>paragraph under title2</p>
	#</h2>
	#</div>
	mydiv2 = page << div(id='myDiv2')
	mydiv2 <<h2('title2 in div2') << p('paragraph under title2')

	#<div align="right" id="myDiv3"><p>paragraph in mydiv3</p>
	#</div>
	mydiv3 = page << div(id='myDiv3')
	mydiv3.attributes['align'] = 'right'
	mydiv3 << p('paragraph in mydiv3')

	#<table border="1" id="mytable1"><tr id="headline"><td>Head1<td>Head2</td>
	#</td>
	#</tr>
	#<tr id="line1"><td>r1,c1<td>r1,c2</td>
	#</td>
	#</tr>
	#<tr id="line2"><td>r2,c1<td>r2,c2</td>
	#</td>
	#</tr>
	#</table>
	table1 = page << table(border='1',id='mytable1')
	headtr = table1 << tr(id='headline')
	headtr << td('Head1') << td('Head2')

	tr1 = table1 << tr(id='line1')
	tr1 << td('r1,c1') <<td('r1,c2')

	tr2 = table1 << tr(id='line2')
	tr2 << td('r2,c1') <<td('r2,c2')
	page.printOut("mypage.html")

if __name__ == '__main__':
	gentask_html()