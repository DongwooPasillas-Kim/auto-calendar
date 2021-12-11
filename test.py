import tkinter as tk
import string
from tkinter.constants import BOTH, E, N

window = tk.Tk()
frm_ent = tk.Frame(master=window, relief=tk.GROOVE, borderwidth=2, width=200, height=100, padx=10,pady=20)
frm_btn = tk.Frame(master=window, width=30, padx=10,pady=20)
frm_ent.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
frm_btn.pack(fill=tk.BOTH, side=tk.LEFT)

# 여기 밑에는.. 엔트리 리스트 5개 만들어 놓고 버튼 누르면 행을 추가해주는 건데,
# 이벤트 명 / 기간(2열?) / 체크박스(붙어야하는 일정?) / 체크박스(고정 기간) 으로 5열로 관리 필요할 듯
# add(): 버튼 눌러서 조건 행 더하기

preset_ent = string.ascii_uppercase
entlist = []
val_ent = []
count = 0 # To keep track of inserted entries

print(type(preset_ent[0]))

for idx in range(0,5):
    entlist.append(tk.Entry(master=frm_ent))
    # entlist[-1].grid(row=idx,column=0,padx=5,pady=2)
    entlist[-1].pack(fill=tk.BOTH)
    entlist[-1].insert(index=0, string=preset_ent[count%len(preset_ent)]+'. ')
    count +=1

def add():
    global count
    # MAX_NUM = 4 # Maximum number of entries
    # if count <= MAX_NUM:
    entlist.append(tk.Entry(master=frm_ent)) # Create and append to list
    # entlist[-1].grid(row=count,column=0,padx=5,pady=2) # Place the just created widget
    entlist[-1].pack(fill=tk.BOTH)
    entlist[-1].insert(index=0, string=preset_ent[count%len(preset_ent)]+'. ')
    count += 1

def delete():
    global count
    # MAX_NUM = 4 # Maximum number of entries
    # if count <= MAX_NUM:
    if len(entlist)!=0:
        entlist[-1].destroy()
        entlist.pop()
        count -= 1
    
def save():
    # global val_entry
    if len(val_ent) != 0:
        val_ent.clear()
    for entry in entlist:  
        val_ent.append(entry.get())
    print(val_ent)

btn_addent = tk.Button(frm_btn, text='Add Cond', command=add).pack() # A button to call the function
btn_deleteent = tk.Button(frm_btn, text='Delete Cond', command=delete).pack()
btn_save = tk.Button(frm_btn, text='Save Cond', command=save).pack()


# eventname = []
# ent_eventname1 = tk.Entry(width=50)
# ent_eventname2 = tk.Entry(width=50)
# ent_eventname3 = tk.Entry(width=50)
# ent_eventname4 = tk.Entry(width=50)
# ent_eventname5 = tk.Entry(width=50)
# btn_condition = tk.Button(text="condition")


# ent_eventname1.pack()
# btn_condition.pack()

window.mainloop()