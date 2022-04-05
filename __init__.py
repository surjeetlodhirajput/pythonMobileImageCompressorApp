"""writer-:SurjeetLodhiRajput
   ContactInfo-Surjeetrajput433@gmail.com
   all right are reserved to the writers of this code
   //this code can be used wherever you want but the thing you need to give appreciation to the writer of this code
   //for running the program correctly please save both python files in the same folder and
   also ensure that no other file with same name is in the directory
"""
from tkinter import *
import PIL
from tkinter import filedialog
import code as cd
from tkinter.ttk import Combobox
from tkinter import messagebox
class imageCompressor:
    def __init__(self):#creatin the mainwindo and using it
        global FLAG
        try:

            self.mainwindow=Tk()
            self.mainwindow.title("Image Compressor Tool")
            self.mainwindow.geometry('400x550+300+60')
            self.mainwindow.config(bg="gray")
            self.mainwindow.resizable(False,False)

            self.top_down_Frame()
        except:
            self.back_Button()
    def top_down_Frame(self):
        self.topButton = Button(self.mainwindow, text="Compress Single Image",foreground="white",font=('times new roman',14),bd=2, command=self.topClicked, relief=RIDGE, width=28, bg="#202020",
                                height=8).place(x=56, y=70)
        self.downButton = Button(self.mainwindow, text="Compress Multiple Images",foreground="white",font=('times new roman',14), bd=2, command=self.downClicked, relief=RIDGE, width=28, bg="#202020",
                                 height=8).place(x=56, y=280)
    def clear_Widgets(self):
        list=self.mainwindow.winfo_children()
        for i in list:
            i.destroy()

    def topClicked(self):##code for when clicked on the top window
        self.clear_Widgets()
        self.singleImageFrame = Frame(self.mainwindow, bd=2, relief=RIDGE, width=300, bg="#202020",
                                height=350).place(x=56, y=70)
        self.back_Button(self.singleImageFrame)
        self.choose_single_image(self.singleImageFrame)


    def downClicked(self):#when clicked on the down window
        self.clear_Widgets()
        self.MultiImageFrame = Frame(self.mainwindow, bd=2, relief=RIDGE, width=300, bg="#202020",
                                height=350).place(x=56, y=70)
        self.back_Button(self.MultiImageFrame)
        self.choose_multiimage_image(self.MultiImageFrame)
    ###-----------------------------section  for the multiimage
    def choose_multiimage_image(self,frame_name):#function for the single image
        # variable for the combox and entries----------
        self.combo_var = StringVar()
        self.image_quality_entry_var = StringVar()
        self.single_image_entry_var = StringVar()
        ##---------------------------
        single_image_label=Label(frame_name,text="Choose Folder",font=('times new roman',13,'italic bold'),bg='#202020',foreground="white").place(x=70,y=130)
        self.single_image_entry=Entry(frame_name,textvariable=self.single_image_entry_var,font=('times new roman',13,'italic bold')).place(x=120,y=170)
        image_quality_label=Label(frame_name,text="Choose Quality",font=('times new roman',13,'italic bold'),bg='#202020',foreground="white").place(x=70,y=235)
        self.image_quality_entry=Entry(frame_name,textvariable=self.image_quality_entry_var,font=('times new roman',13,'italic bold')).place(x=120,y=280)
        browse_button = Button(frame_name, text="...", font=('times new roman', 15, 'italic bold'), bg='#202020',
                               command=self.get_folder_path,foreground="white", border=1, relief=GROOVE).place(x=310, y=165,height=30)

        quality_combobox = Combobox(frame_name,textvariable=self.combo_var, values=['Low', "Medium", 'High'], width=27, height=5)
        quality_combobox.current(0)
        quality_combobox.place(x=120, y=330)
        #button for the maintaining the submit for singla image
        single_image_submit=Button(frame_name,text="Compress",bg="#202020",border=2,foreground="white",relief=GROOVE,command=self.multiple_image_compressor)
        single_image_submit.place(x=160,y=365,width=100,height=40)
    def get_folder_path(self):
        selected_file=filedialog.askdirectory()
        self.image_quality_entry_var.set(self.combo_var.get())
        self.single_image_entry_var.set(selected_file)
    def multiple_image_compressor(self):
        if self.image_quality_entry_var.get()=="Low":
            cd.entire_directory(self.single_image_entry_var.get(),self.single_image_entry_var.get()+"/updated",500)
        elif self.image_quality_entry_var.get() == "Medium":
            cd.entire_directory(self.single_image_entry_var.get(), self.single_image_entry_var.get() + "/updated",100)
        else:
            cd.entire_directory(self.single_image_entry_var.get(), self.single_image_entry_var.get() + "/updated",2000)

    ##--------------------------------------------end for the function for the multiimage
    ##generic button for the back-----------------------------------
    def back_Button(self,frame_name):
        back=Button(frame_name,text="Back",activebackground="blue",font=('times new roman',15,'italic bold'),bg='#802020',foreground="white",border=2,relief=GROOVE,command=self.set_true_false).place(x=56,y=70)
        label=Label(frame_name,text="Compress Image",font=('times new roman',15,'italic bold'),bg='#202020',foreground="white").place(x=150,y=76)
    def set_true_false(self):#functio for setting the frame type
        self.clear_Widgets()
        self.top_down_Frame()#here we created the loop kind thing

    def choose_single_image(self,frame_name):#function for the single image
        # variable for the combox and entries----------
        self.combo_var = StringVar()
        self.image_quality_entry_var = StringVar()
        self.single_image_entry_var = StringVar()
        ##---------------------------
        single_image_label=Label(frame_name,text="Choose Image",font=('times new roman',13,'italic bold'),bg='#202020',foreground="white").place(x=70,y=130)
        self.single_image_entry=Entry(frame_name,textvariable=self.single_image_entry_var,font=('times new roman',13,'italic bold')).place(x=120,y=170)
        image_quality_label=Label(frame_name,text="Choose Quality",font=('times new roman',13,'italic bold'),bg='#202020',foreground="white").place(x=70,y=235)
        self.image_quality_entry=Entry(frame_name,textvariable=self.image_quality_entry_var,font=('times new roman',13,'italic bold')).place(x=120,y=280)
        browse_button = Button(frame_name, text="...", font=('times new roman', 15, 'italic bold'), bg='#202020',
                               command=self.get_image_path,foreground="white", border=1, relief=GROOVE).place(x=310, y=165,height=30)

        quality_combobox = Combobox(frame_name,textvariable=self.combo_var, values=['Low', "Medium", 'High'], width=27, height=5)
        quality_combobox.current(0)
        quality_combobox.place(x=120, y=330)
        #button for the maintaining the submit for singla image
        single_image_submit=Button(frame_name,text="Compress",bg="#202020",border=2,foreground="white",relief=GROOVE,command=self.single_imgae_compressor)
        single_image_submit.place(x=160,y=365,width=100,height=40)


    def get_image_path(self):
        selected_file=filedialog.askopenfilename()
        print(selected_file,self.combo_var.get())
        self.image_quality_entry_var.set(self.combo_var.get())
        self.single_image_entry_var.set(selected_file)
    def single_imgae_compressor(self):
        self.image_quality_entry_var.set(self.combo_var.get())
        if self.single_image_entry_var.get()=="":
            messagebox.showerror("Error","Please Choose The Image")
            return
        if self.image_quality_entry_var.get() not in ['Low', "Medium", 'High']:
            messagebox.showerror("Error", "Please Choose Right Option For Imgaeg Quality")
            return
        if self.single_image_entry_var.get().split('/')[-1].split('.')[-1] not in ['jpg','jpeg','png']:
            messagebox.showerror("Error", "Please Choose Right Image")
            return
        new_image_path=self.single_image_entry_var.get().split('/')
        new_i=''
        for i in range(-len(new_image_path),-1):
            new_i+=new_image_path[i]+'/'
        try:
            if self.image_quality_entry_var.get()=='Low':
                cd.resize_pic(self.single_image_entry_var.get(),new_i+self.single_image_entry_var.get().split("/")[-1].split('.')[0]+'updated.jpg',500)
            elif self.image_quality_entry_var.get()=='hight':
                cd.resize_pic(self.single_image_entry_var.get(),new_i+self.single_image_entry_var.get().split("/")[-1].split('.')[0]+'updated.jpg',2000)
            elif self.image_quality_entry_var.get()=='Medium':
                cd.resize_pic(self.single_image_entry_var.get(),new_i+self.single_image_entry_var.get().split("/")[-1].split('.')[0]+'updated.jpg',mywidth=1000)
        except:
            return
        messagebox.showinfo("Notification","Image Saved Successfully")




if __name__=="__main__":
    app=imageCompressor()
    mainloop()