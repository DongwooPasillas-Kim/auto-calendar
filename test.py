import tkinter as tk
import string
from tkinter.filedialog import askopenfile, asksaveasfilename

window = tk.Tk()
frm_ent1 = tk.LabelFrame(master=window, width=30, text="Events", relief=tk.GROOVE, borderwidth=2, padx=10,pady=10)
frm_ent2 = tk.LabelFrame(master=window, width=5, text="Min. Day(s)", relief=tk.GROOVE, borderwidth=2, padx=10,pady=10)
frm_ent3 = tk.LabelFrame(master=window, width=5, text="Max. Day(s)", relief=tk.GROOVE, borderwidth=2, padx=10,pady=10)
frm_chk2 = tk.LabelFrame(master=window, text="Bound", relief=tk.GROOVE, borderwidth=2, padx=10,pady=9)
frm_chk1 = tk.LabelFrame(master=window, text="Exact", relief=tk.GROOVE, borderwidth=2, padx=10,pady=9)
frm_btn = tk.Frame(master=window, width=40, padx=10,pady=15)

frm_ent1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True, padx=10, pady=10)
frm_ent2.pack(fill=tk.BOTH, side=tk.LEFT, padx=10, pady=10)
frm_ent3.pack(fill=tk.BOTH, side=tk.LEFT, padx=10, pady=10)
frm_chk1.pack(fill=tk.BOTH, side=tk.LEFT, padx=10, pady=10)
frm_chk2.pack(fill=tk.BOTH, side=tk.LEFT, padx=10, pady=10)
frm_btn.pack(fill=tk.BOTH, side=tk.LEFT)

# 여기 밑에는.. 엔트리 리스트 5개 만들어 놓고 버튼 누르면 행을 추가해주는 건데,
# 이벤트 명 / 기간(2열?) / 체크박스(붙어야하는 일정?) / 체크박스(고정 기간) 으로 5열로 관리 필요할 듯
# add(): 버튼 눌러서 조건 행 더하기

preset_ent = string.ascii_uppercase
entlist = [[],[],[],[],[]]
val_ent = []
count = 0 # To keep track of inserted entries

print(type(preset_ent[0]))

for i in range(0,5):
    entlist[0].append(tk.Entry(master=frm_ent1))
    entlist[1].append(tk.Entry(master=frm_ent2,width=5))
    entlist[2].append(tk.Entry(master=frm_ent3,width=5))
    entlist[3].append(tk.Checkbutton(master=frm_chk1))
    entlist[4].append(tk.Checkbutton(master=frm_chk2))
    # entlist[-1].grid(row=idx,column=0,padx=5,pady=2)
    for j in range(3):
        entlist[j][-1].pack(pady=3,fill=tk.BOTH)
    for j in range(3,5):
        if (i!=4)|(j!=4):
            entlist[j][-1].pack(fill=tk.BOTH)

    entlist[0][-1].insert(index=0, string=preset_ent[count%len(preset_ent)]+'. ')
    count +=1

def add():
    global count
    # MAX_NUM = 4 # Maximum number of entries
    # if count <= MAX_NUM:
    entlist[0].append(tk.Entry(master=frm_ent1)) # Create and append to list
    entlist[1].append(tk.Entry(master=frm_ent2, width=5))
    entlist[2].append(tk.Entry(master=frm_ent3, width=5))
    entlist[3].append(tk.Checkbutton(master=frm_chk1))
    entlist[4].append(tk.Checkbutton(master=frm_chk2))
    # entlist[-1].grid(row=count,column=0,padx=5,pady=2) # Place the just created widget
    for i in range(3):
        entlist[i][-1].pack(pady=3,fill=tk.BOTH)
    for i in range(3,5):
        entlist[i][-1].pack(fill=tk.BOTH)
    entlist[0][-1].insert(index=0, string=preset_ent[count%len(preset_ent)]+'. ')
    count += 1

def delete():
    global count
    # MAX_NUM = 4 # Maximum number of entries
    # if count <= MAX_NUM:
    if len(entlist[0])!=0:
        for i in range(5):
            entlist[i][-1].destroy()
            entlist[i].pop()
        count -= 1
    
def save():
    # global val_entry
    if len(val_ent) != 0:
        val_ent.clear()
    for entry in entlist[0]:  
        val_ent.append(entry.get())
    print(val_ent)

btn_addent = tk.Button(frm_btn, text='Add Cond.', command=add).pack(pady=5, fill='x') # A button to call the function
btn_deleteent = tk.Button(frm_btn, text='Delete Cond.', command=delete).pack(pady=5, fill='x')
btn_save = tk.Button(frm_btn, text='Save Cond.', command=save).pack(pady=5, fill='x')


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