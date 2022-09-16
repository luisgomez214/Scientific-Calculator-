from tkinter import*
import math 
import parser 
import tkinter.messagebox   #imports 

root = Tk()
root.title("Scientific Calculator")            #title for GUI 
root.resizable(width= True, height = True)     #makes it so GUI is resizable
root.geometry("800x492+460+40")                #dimensions and location of calculator 


MainFrame = Frame(root, bd=20, pady=2, relief = RIDGE)            #Frame
MainFrame.grid()
calcFrame = Frame(MainFrame, bd = 20, pady=2, relief = RIDGE) 
calcFrame.grid()                                    #creates GUI 

def cExit():               #what promtps the message when you press exit under file
  cExit = tkinter.messagebox.askyesno("Scientific Calculator", "Are you sure you wish to exit?") 
  if cExit > 0: 
    root.destroy() 
    return 

def cScientific():        #changes the menu when you press Scientific under file
  root.geometry("999x492+260+40")    
  root.resizable(width = True, height = True)   
  txtResult.delete(0,-1)     
  txtResult.delete(0,"0")
  labelDisplay = Label(calcFrame, text = "Luis' Scientific Calculator", font = ('timesnewroman', 17),padx = 9, fg = 'maroon', justify = CENTER)
  labelDisplay.grid(row = 0, column = 4, columnspan = 4, rowspan = 2) 


def cStandard():            #changes the menu when you press Standard under file
  root.geometry("460x492+460+40")
  root.resizable(width = False, height = False)
  txtResult.delete(0,-1)
  txtResult.delete(0,"0")

menubar = Menu(calcFrame)                                  #Menu

filemenu = Menu(menubar, tearoff = 0)       #creates menu tab 
menubar.add_cascade(label = "File", menu = filemenu)    #adds file to menu 
filemenu.add_command(label = "Standard", command = cStandard)         #within file, theres standard 
filemenu.add_separator()      #next line
filemenu.add_command(label = "Scientific", command = cScientific)
filemenu.add_separator()
filemenu.add_command(label = "Exit", command = cExit)



class Calc():
  def __init__(self):        
     self.total = 0
     self.current = ""
     self.input_value = True 
     self.check_sum = False 
     self.op = ""
     self.result = False 
  
  def EnterNumber(self, num):      #allows for inputs from user 
   self.result = False
   firstnum = txtResult.get()
   secondnum = str(num)
   if self.input_value:
     self.current = secondnum
     self.input_value = False 
   else:                             
     if secondnum == '.':
       if secondnum in firstnum:
         return 
       self.current = firstnum + secondnum
     self.display(self.current)

  def display(self, value):                #displays numbers on screen 
   txtResult.delete(0, END)
   txtResult.insert(0, value)

  def sumOfTotal(self):                               #keeps track of the total
   self.result = True
   self.current = float(self.current)
   if self.check_sum == True:
         self.validFunction()
   else: 
     self.total = float(txtResult.get()) 

  def validFunction(self):                         #basic math operations (code repeats)
   if self.op == "add": 
     self.total += self.current
   if self.op == "sub": 
     self.total -= self.current
   if self.op == "mult": 
     self.total *= self.current
   if self.op == "division": 
     self.total /= self.current
   if self.op == "mod": 
     self.total %= self.current
   if self.op == "squared": 
     self.total = self.current * self.current
   self.input_value = True
   self.check_sum = False
   self.display(self.total)

  def operation(self,op):                         #checks which operation will be done               
   self.current = float(self.current)
   if self.check_sum:
     self.validFunction()
   elif not self.result:
     self.total = self.current
     self.input_value = True
   self.check_sum = True
   self.op = op
   self.result = False

  def clearCal(self):                 #clears calculator
   self.result = False
   self.current = "0"
   self.display(0)
   self.input_value = True


  def allClear(self):            #clears screen
   self.clearCal 
   self.total = 0


    #different math functions that repeat throughout

  def PlusorMinusMath(self):
   self.result = False
   self.current = -(float(txtResult.get()))
   self.display(self.current)

  def cos(self):
   self.result = False
   self.current = math.cos(math.radians(float(txtResult.get())))
   self.display(self.current)


  def cosh(self):
   self.result = False
   self.current = math.cosh(math.radians(float(txtResult.get())))
   self.display(self.current)


  def tan(self):
   self.result = False
   self.current = math.tan(math.radians(float(txtResult.get())))
   self.display(self.current)


  def tanh(self):
   self.result = False
   self.current = math.tanh(math.radians(float(txtResult.get())))
   self.display(self.current)


  def sin(self):
   self.result = False
   self.current = math.sin(math.radians(float(txtResult.get())))
   self.display(self.current)


  def sinh(self):
   self.result = False
   self.current = math.sinh(math.radians(float(txtResult.get())))
   self.display(self.current)

  def log(self):
   self.result = False
   self.current = math.log(float(txtResult.get()))
   self.display(self.current)


  def exp(self):
   self.result = False
   self.current = math.exp(float(txtResult.get()))
   self.display(self.current)




  def pi(self):
   self.result = False
   self.current = math.pi
   self.display(self.current)


  def e(self):
   self.result = False
   self.current = math.e
   self.display(self.current)


  def acosh(self):
   self.result = False
   self.current = math.acosh(float(txtResult.get()))
   self.display(self.current)
  

  def asinh(self):
   self.result = False
   self.current = math.asinh(float(txtResult.get()))
   self.display(self.current)

  def sinh(self):
   self.result = False
   self.current = math.sinh(float(txtResult.get()))
   self.display(self.current)


  def expm1(self):
   self.result = False
   self.current = math.expm1(float(txtResult.get()))
   self.display(self.current)

  def lgamma(self):
   self.result = False
   self.current = math.lgamma(float(txtResult.get()))
   self.display(self.current)


  def degrees(self):
   self.result = False
   self.current = math.degrees(float(txtResult.get()))
   self.display(self.current)


  def log2(self):
   self.result = False
   self.current = math.log2(float(txtResult.get()))
   self.display(self.current)


  def log10(self):
   self.result = False
   self.current = math.log10(float(txtResult.get()))
   self.display(self.current)


  def log1p(self):
   self.result = False
   self.current = math.log1p(float(txtResult.get()))
   self.display(self.current)

  def backSpace(self):
   numLen = len(txtResult.get())
   txtResult.delete(numLen - 1, 'end')
   if numLen == 1:
     txtResult.insert(0,"0")


#below is code for the font and the cosmetics of the calculator
added_value = Calc()
txtResult = Entry(calcFrame, font =('timesnewroman', 16, 'bold') , bg = 'maroon', bd = 30, width = 26, justify = RIGHT)
txtResult .grid(row = 0, column = 0, columnspan = 4, pady = 1)
txtResult.insert(0,"0")

#below is code for buttons 
numberButtons = "789456123" #order matters
i = 0 
btn = []
for j in range(2,5):
    for q in range(3):
        btn.append(Button(calcFrame, width = 6, height = 2, font = ('timesnewroman', 16, 'bold'),bd = 4,text = numberButtons[i])) #buttons' cosmetics
        btn[i].grid(row = j, column = q, pady =1) #location of button 
        btn[i]["command"] = lambda x = numberButtons[i]: added_value.EnterNumber(x)
        i += 1 

btn0 = Button(calcFrame, text = "0", width = 6, height = 2, font = ('timesnewroman', 16, 'bold'), bd = 4, command = lambda: added_value.EnterNumber(0)).grid(row = 5, column = 0, pady = 1)     #uses code from above to set value to the buttons of the operations. also the cosmetics of the buttons (repeats throughout)
btnDiv = Button(calcFrame, text = "/", width = 6, height = 2, font = ('timesnewroman', 16, 'bold'), bd = 4, command = lambda: added_value.operation("division")).grid(row = 5, column = 3, pady = 1)
btnMul = Button(calcFrame, text = "*", width = 6, height = 2, font = ('timesnewroman', 16, 'bold'), bd = 4,  command = lambda: added_value.operation("mult")).grid(row = 4, column = 3, pady = 1)
btnSub = Button(calcFrame, text = "-", width = 6, height = 2, font = ('timesnewroman', 16, 'bold'), bd = 4,  command = lambda: added_value.operation("sub")).grid(row = 3, column = 3, pady = 1)
btnPeriod = Button(calcFrame, text = ".", width = 6, height = 2, font = ('timesnewroman', 16, 'bold'), bd = 4,  command = lambda: added_value.EnterNumber(".")).grid(row = 5, column = 1, pady = 1)
btnAdd = Button(calcFrame, text = "+", width = 6, height = 2, font = ('timesnewroman', 16, 'bold'), bd = 4,  command = lambda: added_value.operation("add")).grid(row = 2, column = 3, pady = 1)
btnPlusorMinus = Button(calcFrame, text = "+/-", width = 6, height = 2, font = ('timesnewroman', 16, 'bold'), bd = 4, command = added_value.PlusorMinusMath).grid(row = 1, column = 3, pady = 1)
btnBackSpace = Button(calcFrame, text = "<--", width = 6, height = 2, font = ('timesnewroman', 16, 'bold'), bd = 4,  command = added_value.backSpace).grid(row = 1, column = 0, pady = 1)
btnClearEntry = Button(calcFrame, text = "CE", width = 6, height = 2, font = ('timesnewroman', 16, 'bold'), bd = 4, command = added_value.clearCal).grid(row = 1, column = 1, pady = 1)
btnClear = Button(calcFrame, text = "C", width = 6, height = 2, font = ('timesnewroman', 16, 'bold'), bd = 4,  command = added_value.allClear).grid(row = 1, column = 2, pady = 1)
btnEqual = Button(calcFrame, text = "=", width = 6, height = 2, font = ('timesnewroman', 16, 'bold'), bd = 4,  command = added_value.sumOfTotal).grid(row = 5, column = 2, pady = 1)


btnSin = Button(calcFrame, text = "sin", width = 6, height = 2, font = ('timesnewroman', 16, 'bold'), bd = 4,  command = added_value.sin).grid(row = 1, column = 4, padx = 5 , pady = 1)
btnTan = Button(calcFrame, text = "tan", width = 6, height = 2, font = ('timesnewroman', 16, 'bold'), bd = 4,  command = added_value.tan).grid(row = 1, column = 5, padx = 5 , pady = 1)
btnCos = Button(calcFrame, text = "cos", width = 6, height = 2, font = ('timesnewroman', 16, 'bold'), bd = 4,  command = added_value.cos).grid(row = 1, column = 6, padx = 5 , pady = 1)
btnPi = Button(calcFrame, text = "π", width = 6, height = 2, font = ('timesnewroman', 16, 'bold'), bd = 4,  command = added_value.pi).grid(row = 1, column = 7, padx = 5 , pady = 1)
btnSinh = Button(calcFrame, text = "sinh", width = 6, height = 2, font = ('timesnewroman', 16, 'bold'), bd = 4,  command = added_value.sinh).grid(row = 2, column = 4, padx = 5 , pady = 1)
btnTanh = Button(calcFrame, text = "tanh", width = 6, height = 2, font = ('timesnewroman', 16, 'bold'), bd = 4,  command = added_value.tanh).grid(row = 2, column = 5, padx = 5 , pady = 1)
btnCosh = Button(calcFrame, text = "cosh", width = 6, height = 2, font = ('timesnewroman', 16, 'bold'), bd = 4,  command = added_value.cosh).grid(row = 2, column = 6, padx = 5 , pady = 1)
btnAsinh = Button(calcFrame, text = "asinh", width = 6, height = 2, font = ('timesnewroman', 16, 'bold'), bd = 4, command = added_value.asinh).grid(row = 4, column = 4, padx = 5 , pady = 1)
btnacosh = Button(calcFrame, text = "bcoshh", width = 6, height = 2, font = ('timesnewroman', 16, 'bold'), bd = 4, command = added_value.acosh).grid(row = 4, column = 5, padx = 5 , pady = 1)
btnDec = Button(calcFrame, text = "dec", width = 6, height = 2, font = ('timesnewroman', 16, 'bold'), bd = 4, command = added_value.degrees).grid(row = 4, column = 6, padx = 5 , pady = 1)
btnLog2 = Button(calcFrame, text = "log2", width = 6, height = 2, font = ('timesnewroman', 16, 'bold'), bd = 4,  command = added_value.log2).grid(row = 4, column = 7, padx = 5 , pady = 1)
btnLgamma = Button(calcFrame, text = "lgamma", width = 6, height = 2, font = ('timesnewroman', 16, 'bold'), bd = 4,  command = added_value.lgamma).grid(row = 5, column = 4, padx = 5 , pady = 1)
btnexpm1 = Button(calcFrame, text = "expm1", width = 6, height = 2, font = ('timesnewroman', 16, 'bold'), bd = 4,  command = added_value.expm1).grid(row = 5, column = 5, padx = 5 , pady = 1)
btnLog1p = Button(calcFrame, text = "log1p", width = 6, height = 2, font = ('timesnewroman', 16, 'bold'), bd = 4,  command = added_value.log1p).grid(row = 5, column = 6, padx = 5 , pady = 1)
btnLog10 = Button(calcFrame, text = "log10", width = 6, height = 2, font = ('timesnewroman', 16, 'bold'), bd = 4,  command = added_value.log10).grid(row = 5, column = 7, padx = 5 , pady = 1)

btnsquared = Button(calcFrame, text = "^2", width = 6, height = 2, font = ('timesnewroman', 16, 'bold'), bd = 4,  command = lambda: added_value.operation("squared")).grid(row = 2, column = 7, padx = 5 , pady = 1)
btnE = Button(calcFrame, text = "e", width = 6, height = 2, font = ('timesnewroman', 16, 'bold'), bd = 4,  command = added_value.e).grid(row = 3, column = 4, padx = 5 , pady = 1)
btnMod = Button(calcFrame, text = "mod", width = 6, height = 2, font = ('timesnewroman', 16, 'bold'), bd = 4,  command = lambda: added_value.operation("mod")).grid(row = 3, column = 5, padx = 5 , pady = 1)
btnExp = Button(calcFrame, text = "exp", width = 6, height = 2, font = ('timesnewroman', 16, 'bold'), bd = 4, command = added_value.exp).grid(row = 3, column = 6, padx = 5 , pady = 1)
btnLog = Button(calcFrame, text = "log", width = 6, height = 2, font = ('timesnewroman', 16, 'bold'), bd = 4, command = added_value.log).grid(row = 3, column = 7, padx = 5 , pady = 1)




root.config(menu = menubar)
root.mainloop()
