import wx
import sqlite3
import itertools
import matplotlib.pyplot as plt
import re 
import os 


class Example(wx.Frame):
 
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(1000,800))
        self.inter_list = list()
        self.plot_list = list()

 
        self.InitUI()
        self.Layout()
        self.Centre()
        self.Show()
 
    def InitUI(self):
 
        self.p = wx.Panel(self)        
        bs = wx.BoxSizer(wx.VERTICAL)
        lbl=wx.StaticText(self.p,-1,style=wx.ALIGN_CENTER)
        txt = "Welcome to Raman Spectroscopy Database"
        font = wx.Font(18, wx.ROMAN, wx.ITALIC, wx.NORMAL)
        lbl.SetFont(font)
	lbl.SetLabel(txt)
	bs.Add(lbl,0,wx.ALIGN_CENTER)
        #lbl2=wx.StaticText(self.p,-1,style=wx.ALIGN_CENTER)
        #txt2 = "Periodic Table"
       # font2 = wx.Font(18, wx.ROMAN, wx.ITALIC, wx.NORMAL)
       # lbl2.SetFont(font2)
	#lbl2.SetLabel(txt2)
	#bs.Add(lbl2,0,wx.ALIGN_CENTER)
        self.text = wx.TextCtrl(self.p,size = (50,30),style = wx.TE_MULTILINE |wx.TE_CENTER)
        bs.Add(self.text, 1, wx.EXPAND)
        self.list = wx.ListCtrl(self.p,size = (50,30),style = wx.LC_REPORT)
        self.list.InsertColumn(0, 'MOLECULE NUMBER',wx.LIST_FORMAT_CENTER, width = 170) 
        self.list.InsertColumn(1, 'MOLECULE', wx.LIST_FORMAT_CENTER, 200) 
        self.list.InsertColumn(2, 'FACILITY & REFERENCES', wx.LIST_FORMAT_CENTER, 350)
        self.list.InsertColumn(3, 'DATA', wx.LIST_FORMAT_CENTER, 300)
        bs.Add(self.list, 1, wx.EXPAND)
        
        gs = wx.GridSizer(10, 18, 5, 5)
        bs.Add(gs, 1, wx.EXPAND)

        self.conn = sqlite3.connect('RAMAN.db')
        for row_id in range(1,11):
           for col_id in range(1,19):
             #print row_id,col_id
             cursor= self.conn.execute("SELECT * FROM ELEMENT where ROW_NO==%d AND COLUMN_NO==%d"%(row_id,col_id))
             if(cursor==None):
                gs.Add(wx.StaticText(self.p,-1,''))
             else:
                elements = cursor.fetchall()
                if(elements==None or len(elements)==0):
                   gs.Add(wx.StaticText(self.p,-1,''))
                else:
                   #print elements[0]
                   btn = wx.Button(self.p, -1,str(elements[0][1]), (10,20))                              
                   btn.Bind(wx.EVT_BUTTON, self.OnClick, btn)
                   gs.Add(btn, -1, wx.EXPAND)
                   
        self.search_btn=wx.Button(self.p,-1,"Search")
        self.search_btn.Bind(wx.EVT_BUTTON, self.OnSearch, self.search_btn)
        bs.Add(self.search_btn,0,wx.ALIGN_CENTER)

        self.reset_btn=wx.Button(self.p,-1,"Reset")
        self.reset_btn.Bind(wx.EVT_BUTTON, self.OnReset, self.reset_btn)
        bs.Add(self.reset_btn,0,wx.ALIGN_CENTER)
        
        self.plot_btn=wx.Button(self.p,-1,"Plot")
        self.Bind(wx.EVT_BUTTON, self.OnPlot, self.plot_btn)
        bs.Add(self.plot_btn,0,wx.ALIGN_LEFT)
        

        
        self.addnew_btn=wx.Button(self.p,-1,"Add New")
        self.addnew_btn.Bind(wx.EVT_BUTTON, self.OnAddNew, self.addnew_btn)
        bs.Add(self.addnew_btn,0,wx.ALIGN_LEFT)

        self.delete_btn=wx.Button(self.p,-1,"Delete")
        self.delete_btn.Bind(wx.EVT_BUTTON, self.OnDelete, self.delete_btn)
        bs.Add(self.delete_btn,0,wx.ALIGN_RIGHT)
        
        self.credit_btn=wx.Button(self.p,-1,"Credits")
        self.credit_btn.Bind(wx.EVT_BUTTON, self.OnCredit, self.credit_btn)
        bs.Add(self.credit_btn,0,wx.ALIGN_RIGHT)
        
        self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.get_selected_item, self.list)
        
        
        self.p.SetSizer(bs)
        
         
    def OnClick(self, event):                                       
        name = event.GetEventObject().GetLabelText()
        cursor= self.conn.execute("SELECT * FROM ELEMENT where SYMBOL==?", (name,))
        elements = cursor.fetchall()
        #print elements
        cursor= self.conn.execute("SELECT ATOMIC_NUMBER FROM ELEMENT where SYMBOL = ?", (name,))
        numbers = cursor.fetchone()[0]
        atomicnumber = numbers
        cursor= self.conn.execute("SELECT MOL_NUMBER FROM LINK where ELEMENT_NUMBER = ?", (atomicnumber,))
        mnumbers = cursor.fetchall()
        #print mnumbers
        mnum_list = []
        for i in mnumbers:
             mnum_list.append(i[0])
        #print mnum_list
        self.inter_list.append(mnum_list)
        #print self.inter_list
        self.molecule_list=list(set.intersection(*map(set,self.inter_list)))
        #print self.molecule_list
        self.text.AppendText(str(elements[0][1]))
        self.text.AppendText("\n")
               
    def OnSearch(self, event):        
        placeholder = '?'
        placeholders = ','.join(placeholder for unused in self.molecule_list)
        query = 'SELECT * FROM MOLECULE WHERE MOL_NUMBER IN (%s)' % placeholders
        cursor = self.conn.execute(query, self.molecule_list)
        final = cursor.fetchall()

        no_of_elements=len(self.inter_list)

        #print final         
        for j in final:
            mol_no=j[0]
            cursor= self.conn.execute('SELECT * FROM LINK WHERE MOL_NUMBER = %d' % mol_no)
            mnumbers = cursor.fetchall()
            if(len(mnumbers)==no_of_elements):
               self.list.Append((j[0],j[1],j[2],j[3]))                            

    def OnReset(self, event):                                   
        self.list.DeleteAllItems()
        self.molecule_list = []
        self.inter_list = []
        self.text.Clear()
        
    def get_selected_item(self, event):
        self.plot_list = list()  
	self.to_delete = event.GetIndex()
        self.plot_list.append(event.GetText())
        #print self.plot_list
        
    def OnPlot(self, event):
        cursor= self.conn.execute("SELECT FILE_NAME FROM MOLECULE where MOL_NUMBER==?", (self.plot_list[0],))
        files = cursor.fetchall()
        #print files[0][0]
        tf = open(files[0][0],'r+')
	d = tf.readlines()
	tf.seek(0)
	for line in d:
    	     s=re.search(r'[a-zA-Z]',line)
             if s:
       	         tf.write('#'+line)
    	     else:
                 tf.write(line)
        tf.truncate()
        tf.close()
        plt.plotfile(str(files[0][0]), delimiter=' ',comments = '#', cols=(0, 1), 
                   names=('Raman Shift ($\mathregular{Cm^{-1}}$)', 'Intensity (arb. units)'), ) 
        plt.title('Raman Spectra of {}'.format(files[0][0]))
        plt.show()

    def OnDelete(self,event):
        cursor= self.conn.execute("DELETE FROM MOLECULE WHERE MOL_NUMBER==?", (self.plot_list[0],))
	print self.to_delete
	#print self.list.GetIndex()
        delet = self.list.DeleteItem(self.to_delete)
        self.conn.commit()
        print delet

    def OnCredit(self,event):
        wx.MessageBox("  BARC \n  Himanshu Pareek, SVNIT Surat")


    def OnAddNew(self,event):
        dlg = GetData(parent = self.p) 
        dlg.ShowModal()
        dlg.Destroy()
           

class GetData(wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, wx.ID_ANY, "Name Input", size= (650,220))
        self.p = wx.Panel(self,wx.ID_ANY)

        self.lblmol = wx.StaticText(self.p, label="Molecule", pos=(20,20))
        self.molecule = wx.TextCtrl(self.p, value="", pos=(110,20), size=(500,-1))
        self.lblfr = wx.StaticText(self.p, label="Facility", pos=(20,60))
        self.facility = wx.TextCtrl(self.p, value="", pos=(110,60), size=(500,-1))
        self.lbldt = wx.StaticText(self.p, label="Data", pos=(20,100))
        self.data = wx.TextCtrl(self.p, value="", pos=(110,100), size=(500,-1))
        self.lblelem = wx.StaticText(self.p, label = "Elements", pos = (20,140))
        self.elements = wx.TextCtrl(self.p, value="", pos=(110,140), size=(500,-1))
        self.saveButton =wx.Button(self.p, label="Save", pos=(110,160))
        self.closeButton =wx.Button(self.p, label="Cancel", pos=(210,160))
        self.saveButton.Bind(wx.EVT_BUTTON, self.SaveConnString)
        self.closeButton.Bind(wx.EVT_BUTTON, self.OnQuit)
        self.Bind(wx.EVT_CLOSE, self.OnQuit)
        self.Show()

    def OnQuit(self, event):
        self.result_name = None
        self.Destroy()

    def SaveConnString(self, event):
	self.conn = sqlite3.connect('RAMAN.db')
        result_molecule = self.molecule.GetValue()
        result_facility = self.facility.GetValue()
        result_data = self.data.GetValue()
        result_elements = self.elements.GetValue()

 	cursora = self.conn.execute("SELECT * FROM LINK")
        maxmola = cursora.fetchall()
	#print maxmola

        cursor= self.conn.execute("SELECT MAX(MOL_NUMBER) FROM MOLECULE")
        maxmol = cursor.fetchall()
        #print maxmol[0][0]
	#print result_facility
	cursor = self.conn.execute("INSERT INTO MOLECULE( MOL_NUMBER , MOL_NAME , MOL_FORMULA , FILE_NAME) VALUES(? , ? , ? , ?)" , (maxmol[0][0] +1 , result_molecule , result_facility , result_data))
	self.conn.commit()
	element_array = result_elements.split(",") 
	for element in element_array: 
		element_id = self.conn.execute("SELECT * FROM ELEMENT WHERE SYMBOL == ?", [element])
		ele = element_id.fetchall()[0][0]
                cursor= self.conn.execute("SELECT MAX(ID) FROM LINK")
        	maxid = cursor.fetchall()
        	#print maxid[0][0]
		cursor = self.conn.execute("INSERT INTO LINK(ID , ELEMENT_NUMBER , MOL_NUMBER ) VALUES(? , ? , ?)" , (maxid[0][0] +1 , ele, maxmol[0][0] + 1))
		self.conn.commit()
        self.Destroy()
      
       		
app = wx.App(False)
Example(None, title = 'Raman Spectroscopy Database')
app.MainLoop() 
