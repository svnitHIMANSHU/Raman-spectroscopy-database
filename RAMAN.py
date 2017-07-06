import wx
import sqlite3
import itertools
import matplotlib.pyplot as plt
import re 
import os 

class MyFrame(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, -1, "My Frame", size=(3000, 3000))
        self.p = wx.Panel(self,-1)
        button=wx.Button(self.p,label="OK",pos=(800, 400), size = (50,50))
        self.Bind(wx.EVT_BUTTON, self.newwindow, button)


    def newwindow(self, event):
        secondWindow = Example(parent=self.p)
        secondWindow.Show()

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
        txt = "Periodic Table"
        font = wx.Font(18, wx.ROMAN, wx.ITALIC, wx.NORMAL)
        lbl.SetFont(font)
	lbl.SetLabel(txt)
	bs.Add(lbl,0,wx.ALIGN_CENTER)
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
                   
        self.search_btn=wx.Button(self.p,-1,"Search!")
        self.search_btn.Bind(wx.EVT_BUTTON, self.OnSearch, self.search_btn)
        bs.Add(self.search_btn,0,wx.ALIGN_CENTER)
        
        self.plot_btn=wx.Button(self.p,-1,"Plot!")
        self.Bind(wx.EVT_BUTTON, self.OnPlot, self.plot_btn)
        bs.Add(self.plot_btn,0,wx.ALIGN_CENTER)
        
        self.reset_btn=wx.Button(self.p,-1,"Reset!")
        self.reset_btn.Bind(wx.EVT_BUTTON, self.OnReset, self.reset_btn)
        bs.Add(self.reset_btn,0,wx.ALIGN_LEFT)
        
        #self.addnew_btn=wx.Button(self.p,-1,"Add New!")
        #self.addnew_btn.Bind(wx.EVT_BUTTON, self.OnAddNew, self.addnew_btn)
        #bs.Add(self.addnew_btn,0,wx.ALIGN_LEFT)

        self.total_btn=wx.Button(self.p,-1,"Total Molecule!")
        self.total_btn.Bind(wx.EVT_BUTTON, self.OnTotal, self.total_btn)
        bs.Add(self.total_btn,0,wx.ALIGN_RIGHT)
        
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
        plt.show()

    def OnTotal(self, event):
        cursor= self.conn.execute("SELECT count(*) FROM MOLECULE")
        total = cursor.fetchall()
        print total

app = wx.App(False)
frame = MyFrame()
frame.Show(True)
app.MainLoop()
