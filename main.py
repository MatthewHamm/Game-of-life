from tkinter import *
import numpy as np
import time

class life(object):
  def __init__(self):
    
    self.root = Tk()
    self.canvas = Canvas(self.root, width=400, height = 400)
    self.canvas.pack()
    self.animabool=False
    self.initialstate=np.zeros((40,40))#np.random.randint(2,size=(40,40))
    self.liveindex=np.where(self.initialstate==1)
    self.livelist=[]
    for  i in range(0,len(self.liveindex[0])):
      self.livelist.append(self.canvas.create_rectangle(10*self.liveindex[0][i],10*self.liveindex[1][i],9+10*self.liveindex[0][i],9+10*self.liveindex[1][i], fill='black'))
    self.canvas.pack()
    self.root.bind('<ButtonPress-1>', self.addlive)
    self.root.bind('<Key-space>', self.pause)
    self.root.after(0, self.animation)
    
    self.root.mainloop()
  def update(self):
    finalstate=np.zeros(self.initialstate.shape)
    liveindex=np.where(self.initialstate==1)
    deadindex=np.where(self.initialstate==0)
    
    
    for i in range(len(liveindex[0])):
      livecount=np.sum(self.initialstate[liveindex[0][i]-1:liveindex[0][i]+2:2,liveindex[1][i]])+np.sum(self.initialstate[liveindex[0][i],liveindex[1][i]-1:liveindex[1][i]+2:2])
      
      
      finalstate[liveindex[0][i],liveindex[1][i]]=1*(livecount==2 or livecount==3)
      
    for i in range(len(deadindex[0])):
      deadcount=np.sum(self.initialstate[deadindex[0][i]-1:deadindex[0][i]+2:2,deadindex[1][i]])+np.sum(self.initialstate[deadindex[0][i],deadindex[1][i]-1:deadindex[1][i]+2:2])
      finalstate[deadindex[0][i],deadindex[1][i]]=1*(deadcount==3)
    return finalstate
    
    

  def animation(self):
    while self.animabool:
      self.liveindex=np.where(self.initialstate==1)
      self.livelist=[]
      for i in range(0,len(self.liveindex[0])):
        self.livelist.append(self.canvas.create_rectangle(10*self.liveindex[0][i],10*self.liveindex[1][i],10+10*self.liveindex[0][i],10+10*self.liveindex[1][i], fill='black'))
      self.canvas.update()
      time.sleep(0.05)
      self.canvas.delete('all')
      
      
      self.initialstate=self.update()
      
      
      
      
  def addlive(self,event):
    
    if str(event.type) == 'ButtonPress':
      print(round((event.x-5)/10),round((event.y-5)/10))
      self.initialstate[round((event.x-5)/10),round((event.y-5)/10)]=1
      self.livelist.append(self.canvas.create_rectangle(10*round((event.x-5)/10),10*round((event.y-5)/10),10+10*round((event.x-5)/10),10+10*round((event.y-5)/10), fill='black'))
      self.canvas.update()
  def pause(self, event):
    
    self.animabool=not(self.animabool)
    self.animation()
    for i in range(0,len(self.liveindex[0])):
        self.livelist.append(self.canvas.create_rectangle(10*self.liveindex[0][i],10*self.liveindex[1][i],10+10*self.liveindex[0][i],10+10*self.liveindex[1][i], fill='black'))
    self.canvas.update()
    print('here')

    
      
  
    
      

    

life()