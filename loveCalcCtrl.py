import wx
import loveCalc
import random
import sqlite3

dbconn = sqlite3.connect("E:/Random Projects/Love calc/name_db.db")



class Calculator (loveCalc.calcFrame):
    def __init__(self, parent):
        super().__init__(parent)

    def goPredict(self, event):
        maleName = self.male_text.GetValue()
        femaleName = self.female_text.GetValue()
        percentage = random.randint(1, 100)
        
        cur = dbconn.cursor()
        cur.execute('SELECT * FROM nameList WHERE maleName="%s" AND femaleName="%s"' % (maleName, femaleName))
        if (len(list(cur)) > 0):
            for row in dbconn.execute('SELECT score FROM nameList WHERE maleName="%s" AND femaleName="%s"' % (maleName, femaleName)) :
                print(row[0])
                self.result_text.SetLabel(str(row[0]) + '%')
        else:
            self.result_text.SetLabel(str(percentage) + '%')
            addQuery = f'INSERT INTO nameList (maleName, femaleName, score) VALUES ("{maleName}", "{femaleName}", "{percentage}")'
            dbconn.execute(addQuery)
            dbconn.commit()
        
        # print(maleName, femaleName, percentage)
        # self.result_text.SetLabel(str(percentage))

    # def dbCheck():



app = wx.App()
frame = Calculator(None)
frame.Show()
app.MainLoop()