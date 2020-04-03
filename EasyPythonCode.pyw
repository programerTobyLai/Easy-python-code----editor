import sys,win32api,os,subprocess,json,webbrowser,qdarkstyle
from pykeyboard import PyKeyboard
from PyQt5.QtPrintSupport import QPrinter,QPrintDialog
from PyQt5 import QtCore,QtGui,uic,Qt,Qsci
import PyQt5.sip
from PyQt5.QtWidgets import *
# from python_highlighter import PythonHighlighter
# from try_for_console import Console
from codeEdit import CodeEditor
import GUIs.replacedlg as replacedlg
import PyQt5_stylesheets
import mail.send
# import qtawesome as qta
codeeditstyle="""background-color: rgb(24, 74, 191);
border:5px solid rgb(17, 120, 255);
color: rgb(255, 255, 255);"""
os.chdir(os.path.split(sys.argv[0])[0])
country = QtCore.QLocale.system().country()

if country in (QtCore.QLocale.China, QtCore.QLocale.HongKong, QtCore.QLocale.Taiwan):
	if country==QtCore.QLocale.China:
		with open('GUIs/QSS/zh-cn.qss','r',encoding='utf-8')as zh_cnQSSimport:
			TextStyle=zh_cnQSSimport.read()
	else:
		with open('GUIs/QSS/zh-tw.qss','r',encoding='utf-8')as zh_twQSSimport:
			TextStyle=zh_twQSSimport.read()
else:
	TextStyle=''
winStyle="""

"""
Replacer=uic.loadUiType("GUIs/replace.ui")[0]
class replacec(QDialog,Replacer):
	"""docstring for replace"""
	def __init__(self, parent=None):
		QMainWindow.__init__(self,parent)

		self.setupUi(self)
		self.cancel.clicked.connect(self.reject)
		self.show()
		
		

class_py=uic.loadUiType("GUIs/code.ui")[0]
# toolboxUI=uic.loadUiType("toolbox/bxToolbox.ui")[0]
# class app2(QMainWindow,toolboxUI):
# 	def __init__(self,parent=None):
# 		QMainWindow.__init__(self,parent)



class app(QMainWindow,class_py):
	def __init__(self,parent=None):
		QMainWindow.__init__(self,parent)
		self.setupUi(self)
		self.edit=CodeEditor()
		self.edit.setEdgeColumn(self.width())
		# self.test()
		try:
			with open('lang/zh-cn/zh-cn.json',encoding='utf-8')as jsondat:
				list_widget_lang=json.load(jsondat)
		except:
			print('启动语言包失败')
		else:
			for x in list_widget_lang:
				try:
					exec(f'self.{x}.setText("{list_widget_lang[x]}")')

				except AttributeError:
					exec(f'self.{x}.setTitle("{list_widget_lang[x]}")')
				except Exception as e:
					print(f'翻译控件{x}为"{list_widget_lang[x]}"时出错，错误信息：{e}')

		if len(sys.argv)==2:
			try:
				with open(sys.argv[1],"r",encoding='utf-8')as fp:
					a = fp.read()
				self.edit.setPlainText(a)
				self.file=True
				self.filename=sys.argv[1]
				self.setWindowTitle('Easy Python Code beta - '+self.filename)
			except:
				QMessageBox.critical(self,'Error','无法打开此文件！',QMessageBox.Close)
		
		
		
		
		 
		self.layout.addWidget(self.edit)
		#self.actionPrint.setIcon(qta.icon('mdi.printer', scale_factor = 1.3, color="skyblue"))
		self.setWindowIcon(QtGui.QIcon('./GUIs/images/icons/Icon.png'))
		self.actionRun.setIcon(QtGui.QIcon('./GUIs/images/toolbar/run.png'))
		# self.actionReplace.setIcon(qta.icon('mdi.find-replace', scale_factor = 1.3, color=QtGui.QColor(0,200,0)))
		# self.actionClosetoolbar.setIcon(qta.icon('mdi.progress-close', scale_factor = 1.3, color="red"))

		# self.actionOpen.setIcon(qta.icon('ei.folder-open', scale_factor = 1.3, color='skyblue'))
		# self.actionNew.setIcon(qta.icon('ei.file-new', scale_factor = 1.3, color="skyblue"))
		# self.actionSave.setIcon(qta.icon('fa.save',scale_factor=1.3,color='skyblue'))
		# self.actionFull.setIcon(qta.icon('mdi.fullscreen',scale_factor=1.5,color='skyblue'))
		# self.actionNormal.setIcon(qta.icon('mdi.fullscreen-exit',scale_factor=1.5,color='skyblue'))
		# self.actiontbopen.setIcon(qta.icon('mdi.tools',scale_factor=1.4,color='skyblue'))
		# self.actionCmd.setIcon(qta.icon('fa.terminal',scale_factor=1.4,color='skyblue'))
		self.actionnew_window.triggered.connect(lambda:win32api.ShellExecute(0, 'open', sys.argv[0], '','',1) )

		#self.lighter2=PythonHighlighter(self.edit.document())
		self.actionNew.triggered.connect(self.new)
		self.actionSave.triggered.connect(self.save)
		self.actionOpen.triggered.connect(self.open)
		self.actionCmd.triggered.connect(self.cmd)
		self.actionRun.triggered.connect(self.run)
		self.actionReplace.triggered.connect(self.replace)
		#self.actionView_tools.triggered.connect(self.showtool)
		# self.actionPrint.triggered.connect(self.print)
		self.actionClosetoolbar.triggered.connect(self.closetb)
		self.actiontbopen.triggered.connect(self.showtb)
		self.actionAbout.triggered.connect(self.about)
		self.actionPypi.triggered.connect(self.jumpToPypiWeb)
		self.actionPython.triggered.connect(self.jumpToPythonWeb)
		self.actionMail.triggered.connect(self.send_email)
		self.skyblue.triggered.connect(self.cskyblue)
		self.actionQdark.triggered.connect(self.cdark)
		#self.actionQdark.triggered.connect(self.qd)
		self.actionDarkO.triggered.connect(self.cdarkOrange)
		self.actionlight.triggered.connect(self.light)
		self.actionPB.triggered.connect(self.cpinkblue)
		self.actionInstall_pack.triggered.connect(self.install)
		self.actionShell.triggered.connect(self.showShell)
		self.qds=qdarkstyle.load_stylesheet_pyqt5()
		try:
			with open('GUIs/setting.json','r',encoding='utf-8')as fp:
				self.whenClose=json.load(fp)
				if self.whenClose['toolbar_show']==False:
					self.Toolbox.close()
				if self.whenClose['kind']=='skyblue':
					self.cskyblue()
				elif self.whenClose['kind']=='dark':
					self.cdark()
				elif self.whenClose['kind']=='darkOrange':
					self.cdarkOrange()
				elif self.whenClose['kind']=='pinkblue':
					self.cpinkblue()
				elif self.whenClose['kind']=='light':
					self.light()
				else:
					self.setStyleSheet(self.qds)
		except:
			with open('GUIs/setting.json','w',encoding='utf-8')as fp2:
				json.dump({},fp2)
				self.whenClose={}
				self.cskyblue()
				self.whenClose['toolbar_show']=True
		
		self.filename=None
		self.file=False

	def save(self):
		try:
			a=False
			if self.file==False:
				self.filename=QFileDialog.getSaveFileName(self,
										"save file",
										"C:/",
										"Python Files (*.py *.pyw)\nText Files (*.txt)\nOthers (*.*)")[0]

				if self.filename:
					f = self.edit.text()
					with open(self.filename,"w",encoding='utf-8')as fp:
						fp.write(f)
					self.statusbar.showMessage('已保存！',2000)
					self.file=True
					self.setWindowTitle('Easy Python Code beta - '+self.filename)
					a=True

				else:
					a=False
			else:
				f = self.edit.text()
				p = open(self.filename,"w",encoding='utf-8')
				p.write(f)
				p.close()
				self.statusbar.showMessage('已保存！',2000)
				self.file=True
				
				self.setWindowTitle('Easy Python Code beta - '+self.filename)
				a=True
			return a

		except Exception as e:
			QMessageBox.critical(self,'Error','无法保存此文件！'+str(e))

	
			

		
	def open(self):
		try:
			openfile = str(QFileDialog.getOpenFileName(self,
					"open file", 'C:/',
					"Python Files (*.py *.pyw)\nText Files (*.txt)\nOthers (*.*)")[0])
			print(openfile)
			if openfile != '':
				
				with open(openfile,"r",encoding='utf-8')as fp:
					a = fp.read()
				self.edit.setText(a)
				self.file=True
				self.filename=openfile
				self.setWindowTitle('Easy Python Code beta - '+self.filename)
		except:
			QMessageBox.critical(self,'Error','无法打开此文件！',QMessageBox.Close)

	def new(self):
		c=(QMessageBox.warning(self,'新建','是否保存您未保存的更改？     ',QMessageBox.Yes|QMessageBox.No|QMessageBox.Cancel,QMessageBox.Cancel))
		if c==QMessageBox.Yes:
			self.save()
			self.file=False
			self.filename='new.py'
			self.setWindowTitle('Easy Python Code beta - '+self.filename+'*')
			self.edit.clear()
		elif c==c==QMessageBox.No:
			self.edit.clear()
			self.file=False

	def cmd(self):
		win32api.ShellExecute(0, 'open', 'cmd.exe', '','',1)

	def install(self):
		a=os.getcwd()
		win32api.ShellExecute(0, 'open', a+'/bin/install_package.exe', '','',1)


	def run(self):
		if self.save():
			a=os.getcwd()
			win32api.ShellExecute(0, 'open', a+'/bin/runPython.exe', f'"{self.filename}"','',1)
			# k = PyKeyboard()
			# k.type_string('Hello, World!')
			# k.tap_key(k.enter_key)
		#QtGui.QApplication.processEvents()
		# self.entered=False
		# self.outputlist.clear()
		# if self.save():
		# 	cmd='python "'+self.filename+'"'
		# 	path=os.path.split(self.filename)
		# 	p = subprocess.Popen(cmd,stdout=subprocess.PIPE, stderr=subprocess.PIPE,stdin=subprocess.PIPE)#,env=path[0]
		# 	print(p.communicate(input=b'hi'))
			# output = p.stdout.readlines()
			# errout = p.stderr.readlines()
			# #user_input=p.stdin.readlines()
			# for x in output:
			# 	self.outputlist.append('<p>'+x.strip().decode('utf-8')+'</p>')
			# for y in errout:
			# 	self.outputlist.append('<p style="color: red;">'+y.strip().decode('utf-8')+'</p>')

	def showtool(self):
		self.showtUi=app2(self)
		self.showtUi.setupUi(self.showtUi)
		self.showtUi.show()	

	def send_email(self):
		self.mailwindow=mail.send.window(parent=self,style=self.whenClose['kind'])
		self.mailwindow.setupUi(self.mailwindow)
		
		self.mailwindow.setWindowIcon(QtGui.QIcon('./GUIs/images/icons/Icon.png'))
		self.mailwindow.send_btn.clicked.connect(self.mailwindow.send)
		self.mailwindow.text.setPlainText(self.edit.toPlainText())
		self.mailwindow.show()	

	# def print(self):
	# 	printer = QPrinter()
	# 	result = QPrintDialog(printer, self)
	# 	if result.exec_():
	# 		doc = self.edit.document()
	# 		print(doc)
	# 		doc.print_(printer)		

	def replace(self):
		self.replacer=replacec(parent=self)
		self.replacer.replace.clicked.connect(self.replacing)
		self.replacer.show()
	def jumpToPythonWeb(self):
		webbrowser.open('https://python.org/')

	def jumpToPypiWeb(self):
		webbrowser.open('https://pypi.org/')

	def replacing(self):
		if self.replacer.r1.text():
			a=self.edit.toPlainText().replace(self.replacer.r1.text(),self.replacer.r2.text())
			self.edit.setPlainText(a)
			if a==self.edit.toPlainText():
				QMessageBox.information(self,"",f'你替换"{self.replacer.r1.text()}"没有变化')

	def closetb(self):
		self.whenClose['toolbar_show']=False
		self.Toolbox.close()

	def showtb(self):
		self.whenClose['toolbar_show']=True
		self.Toolbox.show()

	def closeEvent(self, event):
		"""
		重写closeEvent方法，实现窗体关闭时执行一些代码
		:param event: close()触发的事件
		:return: None
		"""
		with open('GUIs/setting.json','w')as fp:
			json.dump(self.whenClose,fp)

		if self.file != True:
			reply = QMessageBox.question(self,
											  '未保存',
											  "是否保存您未保存的更改并关闭？",
											  QMessageBox.Save | QMessageBox.Abort | QMessageBox.Cancel,
											  QMessageBox.Cancel)
			if reply == QMessageBox.Save:
				self.save()
				event.accept()
			elif reply == QMessageBox.Abort:
				event.accept()
			else:
				event.ignore()

	def about(self):
		QMessageBox.about(self,'关于Easy Python Code','''Easy Python Code<br>版本:测试版(beta)''')

	def cpinkblue(self):
		(0.8)
		self.whenClose['kind']='pinkblue'
		self.edit.h=QtGui.QColor(Qt.Qt.yellow)
		#self.edit.highlightCurrentLine()
		self.setStyleSheet('')
		self.setStyleSheet('background-color: pink;')
		self.menubar.setStyleSheet('background-color:pink')
		self.edit.setStyleSheet('color: black;background-color: pink;border-radius:15px;border-color: white;')
		self.Toolbox.setStyleSheet('background-color: pink')
		self.setStyleSheet('background-color: pink;QMainWindow,QMenu,QAction{background-color: pink;color: black;}QMenuBar::item {background: transparent;}')
	def cdark(self):
		self.whenClose['kind']='dark'
		try:
			self.edit.h=QtGui.QColor(Qt.Qt.blue)
			#self.edit.highlightCurrentLine()
			self.setStyleSheet(PyQt5_stylesheets.load_stylesheet_pyqt5(style="style_Dark"))
			self.Toolbox.setStyleSheet(PyQt5_stylesheets.load_stylesheet_pyqt5(style="style_Dark"))
			self.menubar.setStyleSheet(PyQt5_stylesheets.load_stylesheet_pyqt5(style="style_Dark"))
			self.edit.setStyleSheet(PyQt5_stylesheets.load_stylesheet_pyqt5(style="style_Dark"))
		except Exception as E:
			print(E)
	def cskyblue(self):
		(0.8)
		self.whenClose['kind']='skyblue'
		self.edit.h=QtGui.QColor(Qt.Qt.yellow)
		#self.edit.highlightCurrentLine()
		self.setStyleSheet('')
		self.menubar.setStyleSheet('')
		self.edit.setStyleSheet('color: black;background-color: skyblue')
		self.Toolbox.setStyleSheet('background-color: skyblue')
		self.setStyleSheet('background-color: skyblue;QMainWindow,QMenu,QAction{background-color: skyblue;color: black;}QMenuBar::item {background: transparent;}')
	
	def cdarkOrange(self):
		(0.84)
		self.whenClose['kind']='darkOrange'
		# with open('GUIs/style/darkorange','r')as style:
		# 	stylesheet=style.read()
		try:
			self.edit.h=QtGui.QColor(4,0,4)
			self.setStyleSheet(PyQt5_stylesheets.load_stylesheet_pyqt5(style="style_DarkOrange"))
			self.Toolbox.setStyleSheet(PyQt5_stylesheets.load_stylesheet_pyqt5(style="style_DarkOrange"))
			self.menubar.setStyleSheet(PyQt5_stylesheets.load_stylesheet_pyqt5(style="style_DarkOrange"))
			self.edit.setStyleSheet(PyQt5_stylesheets.load_stylesheet_pyqt5(style="style_DarkOrange"))
		except:
			pass

	def qd(self):
		(0.91)
		self.whenClose['kind']='qtdarkstyle'
		self.edit.h=QtGui.QColor(4,0,4)
		#self.edit.highlightCurrentLine()
		self.setStyleSheet('')
		self.setStyleSheet(self.qds)
		self.edit.setStyleSheet(self.qds)
		self.Toolbox.setStyleSheet(self.qds)

	def light(self):
		(0.82)
		self.whenClose['kind']='light'
		self.setStyleSheet('')
		self.edit.setStyleSheet('')
		self.menubar.setStyleSheet('')
		self.edit.setStyleSheet('color:black')
		self.edit.h=QtGui.QColor(Qt.Qt.yellow)
		#self.edit.highlightCurrentLine()
		self.Toolbox.setStyleSheet('')

	def showShell(self):
		a=os.getcwd()
		subprocess.Popen(a+'/bin/shell.bat')

Appx=QApplication(sys.argv)
App=app()
Appx.setStyleSheet(TextStyle)
translator = QtCore.QTranslator()
translator.load('lang/qt_zh_CN.qm')
Appx.installTranslator(translator)
App.show()
Appx.exec_()