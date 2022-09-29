import time
import tkinter as tk
from tkinter import messagebox

class HashTable:
    def __init__(self): #initialized values
        self.nf  = 2                              
        self.pos = 0   
        self.t0=0
        self.t1=0                          


    def put(self,tempkey): 
      hashvalue1 = self.hashfn1(tempkey,len(self.positions1)) #to get hash key1/value
      hashvalue2 = self.hashfn2(tempkey,len(self.positions2)) #to get hash key2/value
      currenthkey = hashvalue1 #for swapping between hash value of key 1 or 2
      htable = self.positions1 #for swapping between position hashtable
      for i in range (self.size): #to check for duplicate of key
            if tempkey == self.positions1[i]:
              self.nf=0
              self.pos = i
              break
              
            elif tempkey == self.positions2[i]:
              self.nf = 1
              self.pos = i
              break

            else:
              self.nf = 2      

      if self.nf == 2:
        exit= 0
        collide= 0
        while exit == 0 and collide != 5:
        # no collision
            if htable[currenthkey] == None:
                htable[currenthkey] = tempkey
                print("Hashtable1:")
                print(self.positions1)
                print("Hashtable2:")
                print(self.positions2)
                print("")
                exit = 1

            else:
                collide += 1
                print(collide)
                htable[currenthkey],tempkey = tempkey,htable[currenthkey] #replace and store temporary
                print("Hashtable1:")
                print(self.positions1)
                print("Hashtable2:")
                print(self.positions2)
                print("")
                #handling the collided key
                if currenthkey == hashvalue1: #if currently at Hashtable1
                    hashvalue1 = self.hashfn1(tempkey, len(self.positions1)) #create hash key1 based on tempkey
                    hashvalue2 = self.hashfn2(tempkey,len(self.positions2)) #create hash key1 based on tempkey
                    currenthkey = hashvalue2
                    htable = self.positions2
            
          
                elif currenthkey == hashvalue2: #if currently at Hashtable2
                    hashvalue1 = self.hashfn1(tempkey, len(self.positions1)) #create hash key1 based on tempkey
                    hashvalue2 = self.hashfn2(tempkey,len(self.positions2)) #create hash key1 based on tempkey
                    currenthkey = hashvalue1
                    htable = self.positions1

        if collide==5:
            self.rehash(tempkey)

    def rehash(self,key):
        self.positions1.append(None)
        self.positions2.append(None)
        print(self.positions1)
        print(self.positions2)
        self.size+=1
        self.put(key)

    def hashfn1(self,key,size):
         return key%size

    def hashfn2(self,key,size):
         return (key//size)%size


    def search(self,key):#function search 
            self.nf = 0 
            self.pos = 0
            i = 0
            for i in range (self.size):
                if key == self.positions1[i]:#to check if key at table 1
                    print("Your index number in Hashtable1 is ",i)
                    self.nf = 0
                    self.pos = i
                    break
              
                elif key == self.positions2[i]:#to check if key at table 2
                    print("Your index number in Hash Table 2 is ",i)
                    self.nf = 1
                    self.pos = i
                    break

                else:
                    self.nf = 2
                

    def delete(self,key):#function delete
        self.search(key)
        if self.nf == 0:#if key in table 1
            self.positions1[self.pos]=None
            print("Your new hastable1 is",self.positions1)
        elif self.nf ==1:#if key in table 2
            self.positions2[self.pos]=None
            print("Your new hastable2 is",self.positions2)

    def getsize(self,sz):
        self.size=sz
        self.setTable()

    def setTable(self):
        self.positions1 = [None] * self.size
        self.positions2= [None] * self.size
        print(self.positions1)
        print(self.positions2)

    def time_set(self):
        self.t0= time.time()
        
    def time_end(self):
        self.t1 = time.time() - self.t0
        


def MainTable(size):

    H = HashTable()
    H.getsize(size)

    def get_key():
        key = int(ent_enkey.get())
        H.put(key)
        for j in range(H.size):
            #index1
            frm = tk.Frame(master=frame4,relief=tk.RAISED,borderwidth=1)
            frm.grid(row=1, column=j+1, padx=5, pady=5)
            label = tk.Label(master=frm, text=f"{j}")
            label.pack(padx=5, pady=5)
            #table1
            frm1 = tk.Frame(master=frame4, relief=tk.SUNKEN, borderwidth=1)
            frm1.grid(row=2, column=j+1) 
            label1 = tk.Label(master=frm1, text=f"{H.positions1[j]}", width = 4 , height = 1)
            label1.pack(padx=5, pady=5)
            #index2
            frm1 = tk.Frame(master=frame5,relief=tk.RAISED,borderwidth=1)
            frm1.grid(row=1, column=j+1, padx=5, pady=5)
            label1 = tk.Label(master=frm1, text=f"{j}")
            label1.pack(padx=5, pady=5)
            #table2
            frm2 = tk.Frame(master=frame5, relief=tk.SUNKEN, borderwidth=1)
            frm2.grid(row=2, column=j+1) 
            label2 = tk.Label(master=frm2, text=f"{H.positions2[j]}", width = 4 , height = 1)
            label2.pack(padx=5, pady=5)



    def search_key():
        key = ent_sckey.get()

        if key:
            key = int(key)
            H.search(key)
            if H.nf==0:
                messagebox.showinfo('Message','Your index number in Hashtable1 is {}'.format(H.pos))
            elif H.nf==1:
                messagebox.showinfo('Message','Your index number in Hashtable2 is {}'.format(H.pos))
            elif H.nf==2:
                messagebox.showinfo('Message','Not found')
        else:
            messagebox.showinfo('Message','No Input!')

    def delete_key():
        key = int(ent_delkey.get())
        H.delete(key)

        for j in range(size):
            #index1
            frm = tk.Frame(master=frame4,relief=tk.RAISED,borderwidth=1)
            frm.grid(row=1, column=j+1, padx=5, pady=5)
            label = tk.Label(master=frm, text=f"{j}")
            label.pack(padx=5, pady=5)
            #table1
            frm1 = tk.Frame(master=frame4, relief=tk.SUNKEN, borderwidth=1)
            frm1.grid(row=2, column=j+1) 
            label1 = tk.Label(master=frm1, text=f"{H.positions1[j]}", width = 4 , height = 1)
            label1.pack(padx=5, pady=5)
            #index2
            frm1 = tk.Frame(master=frame5,relief=tk.RAISED,borderwidth=1)
            frm1.grid(row=1, column=j+1, padx=5, pady=5)
            label1 = tk.Label(master=frm1, text=f"{j}")
            label1.pack(padx=5, pady=5)
            #table2
            frm2 = tk.Frame(master=frame5, relief=tk.SUNKEN, borderwidth=1)
            frm2.grid(row=2, column=j+1) 
            label2 = tk.Label(master=frm2, text=f"{H.positions2[j]}", width = 4 , height = 1)
            label2.pack(padx=5, pady=5)

    menu2=tk.Tk()
    frame4=tk.Frame(master=menu2)
    frame4.grid(row=0,column=0)

    lbl_tbl1=tk.Label(master=frame4, text='Hash Table 1', fg='black',font=80)
    lbl_tbl1.grid(row=0,column=0)
    #Hashtable 1 grid here
    lbl_index=tk.Label(master=frame4,text='Index',relief=tk.SUNKEN)
    lbl_index.grid(row=1,column=0)

    for j in range(H.size):
        frm = tk.Frame(master=frame4,relief=tk.RAISED,borderwidth=1)
        frm.grid(row=1, column=j+1, padx=5, pady=5)
        label = tk.Label(master=frm, text=f"{j}")
        label.pack(padx=5, pady=5)

    lbl_key=tk.Label(master=frame4, text='Key', relief=tk.SUNKEN)
    lbl_key.grid(row=2,column=0)

    for j in range(H.size):
        frm1 = tk.Frame(master=frame4, relief=tk.RAISED, borderwidth=1)
        frm1.grid(row=2, column=j+1) 
        label1 = tk.Label(master=frm1, text=f"{H.positions1[j]}")
        label1.pack(padx=5, pady=5)

    
    frame5=tk.Frame(master=menu2)
    frame5.grid(row=1,column=0)
    lbl_tbl2=tk.Label(master=frame5, text='Hash Table 2', fg='black',font=80)
    lbl_tbl2.grid(row=0,column=0)
    #Hashtable 2 grid here
    lbl_index1=tk.Label(master=frame5,text='Index',relief=tk.SUNKEN)
    lbl_index1.grid(row=1,column=0)

    for j in range(H.size):
        frm1 = tk.Frame(master=frame5,relief=tk.RAISED,borderwidth=1)
        frm1.grid(row=1, column=j+1, padx=5, pady=5)
        label1 = tk.Label(master=frm1, text=f"{j}")
        label1.pack(padx=5, pady=5)

    lbl_key1=tk.Label(master=frame5, text='Key', relief=tk.SUNKEN)
    lbl_key1.grid(row=2,column=0)

    for j in range(H.size):
        frm2 = tk.Frame(master=frame5, relief=tk.RAISED, borderwidth=1)
        frm2.grid(row=2, column=j+1) 
        label2 = tk.Label(master=frm2, text=f"{H.positions2[j]}")
        label2.pack(padx=5, pady=5)


    frame6=tk.Frame(master=menu2)
    frame6.grid(row=2,column=0)


    lbl_enkey=tk.Label(master=frame6, text='Enter key:')
    lbl_enkey.grid(row=0,column=0)
    ent_enkey=tk.Entry(master=frame6,width=30)
    ent_enkey.grid(row=0,column=1)
    btn_enkey=tk.Button(master=frame6,text='Enter',command = get_key)
    btn_enkey.grid(row=0,column=2)


    lbl_sckey=tk.Label(master=frame6, text='Search key:')
    lbl_sckey.grid(row=1,column=0)
    ent_sckey=tk.Entry(master=frame6,width=30)
    ent_sckey.grid(row=1,column=1)
    btn_sckey=tk.Button(master=frame6,text='Enter', command = search_key)
    btn_sckey.grid(row=1,column=2)


    lbl_delkey=tk.Label(master=frame6, text='Delete key:')
    lbl_delkey.grid(row=2,column=0)
    ent_delkey=tk.Entry(master=frame6,width=30)
    ent_delkey.grid(row=2,column=1)
    btn_delkey=tk.Button(master=frame6,text='Enter', command = delete_key)
    btn_delkey.grid(row=2,column=2)


    menu2.mainloop()



def EnterSizeWindow(event):

    def size_entry(event):
    
        size = ent_size_input.get()
        
        if size:

            size = int(size)
            MainTable(size)

        else:
            messagebox.showinfo('Message','No Input!')

    menu1=tk.Tk()

    frame2=tk.Frame(master=menu1)
    frame2.grid(row=0,column=0)

    lbl_size=tk.Label(master=frame2, text='Enter table size', fg='black',font=80)
    lbl_size.grid(row=0,column=0)

    frame3=tk.Frame(master=menu1)
    frame3.grid(row=1,column=0)

    ent_size_input=tk.Entry(master=frame3)
    ent_size_input.grid(row=0,column=0)

    Enter=tk.Button(master=frame3, text="Enter", width=10, height=2)
    Enter.grid(row=0, column=1)
    Enter.bind("<Button-1>",size_entry)


    menu1.mainloop()






def main():


    window= tk.Tk()
    T=HashTable()
    frame1=tk.Frame(master=window,bd=10)
    frame1.grid(row=0,column=0)
    intro1=tk.Label(master=frame1, text='Welcome to Cuckoo Hashing', fg='black',font=80)
    intro1.grid(row=0,column=0)

    frame2=tk.Frame(master=window,bd=5)
    frame2.grid(row=1,column=0)
    start=tk.Button(master=frame2, text="Start", width=10, height=5, command=lambda:T.time_set)
    start.grid(row=0, column=0)
    start.bind("<Button-1>",EnterSizeWindow)


    window.mainloop()

if __name__ == '__main__':
	main()
