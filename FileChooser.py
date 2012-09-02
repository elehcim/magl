#!/bin/python
# -*- coding: utf-8 -*-
#
# Genera la appendice di un documento latex da file Matlab
#
# UI adapted from 
# http://python-gtk-3-tutorial.readthedocs.org/en/latest/dialogs.html
from gi.repository import Gtk
import string
import os

class FileChooserWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="FileChooser Example")
    
        self.list_of_files=[]
        self.default_output_tex_file='matlab_appendix.tex'
        
        # #codice per caricare il file .ui
        # self.builder = Gtk.Builder()
        # self.builder.add_from_file(path_to_file)
        # # Carichiamo i pezzi con cui dobbiamo interagire
        # # all' interno dell' oggetto !
        # self.counter_label = self.builder.get_object("counter_label")

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,spacing=6)
        self.add(box)

        button1 = Gtk.Button("Choose Files")
        button1.connect("clicked", self.on_file_clicked)
        box.add(button1)

        button2 = Gtk.Button("Choose Folder")
        button2.connect("clicked", self.on_folder_clicked)
        box.add(button2)

        button3 = Gtk.Button("Write on output file")
        button3.connect("clicked",self.chiedi_conferma)
        box.add(button3)

        self.entry = Gtk.Entry()
        self.entry.set_text(self.default_output_tex_file)
        box.add(self.entry)

        hbox = Gtk.Box(spacing=6)
        box.pack_start(hbox, True, True, 0)
        self.list_label = Gtk.Label(self.list_of_files)
        hbox.add(self.list_label)

    def chiedi_conferma(self, widget):
        # prendi l'ultima versione della stringa entry
        self.output_tex_file=self.entry.get_text()
        # FIXME: dare un comando del tipo salva in...
        # capisce dove sta il file dello script
        #   pwd = os.path.dirname(__file__)
        # capisce dov'è la directory corrente
        pwd = os.getcwd()

        dialog = Gtk.MessageDialog(None,
        Gtk.DialogFlags.MODAL, 
        Gtk.MessageType.QUESTION,
        Gtk.ButtonsType.YES_NO,
        "Sto per scrivere l'appendice Matlab")
        dialog.format_secondary_markup(
            "Sto per scrivere il file:\n\t{0}\nnel percorso\n\t{1}\nSei sicuro?"
            .format(self.output_tex_file,pwd))
        #dialog.set_title("Scrittura appendice file Matlab")
        if dialog.run() == Gtk.ResponseType.YES:
        # Gestisco il caso OK
            print 'sto per scrivere'
            write_on_tex_file(self.list_of_files,self.output_tex_file)
            print 'ho scritto!'
        else:
        # Gestico il caso cancel
            pass
        
        # Faccio sparire il dialogo
        dialog.destroy()

    def on_file_clicked(self, widget):
        dialog = Gtk.FileChooserDialog("Please choose some file", self,
            Gtk.FileChooserAction.OPEN,
            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
             Gtk.STOCK_OPEN, Gtk.ResponseType.OK))

        dialog.set_select_multiple(True)
        
        self.add_filters(dialog)

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            #print "Open clicked"
            #print "File selected: " + dialog.get_filename()
            self.list_of_files+=(dialog.get_filenames())
            filenames=''
            for k in crop_pathnames(self.list_of_files):
                filenames+=k+'\n'
            self.list_label.set_text(filenames)
            print self.list_of_files
        elif response == Gtk.ResponseType.CANCEL:
            print "Cancel clicked"

        dialog.destroy()

    def add_filters(self, dialog):
        filter_text = Gtk.FileFilter()
        filter_text.set_name("Text files")
        filter_text.add_mime_type("text/plain")
        dialog.add_filter(filter_text)

        filter_py = Gtk.FileFilter()
        filter_py.set_name("Python files")
        filter_py.add_mime_type("text/x-python")
        dialog.add_filter(filter_py)

        filter_any = Gtk.FileFilter()
        filter_any.set_name("Any files")
        filter_any.add_pattern("*")
        dialog.add_filter(filter_any)

    def on_folder_clicked(self, widget):
        dialog = Gtk.FileChooserDialog("Please choose a folder", self,
            Gtk.FileChooserAction.SELECT_FOLDER,
            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
             "Select", Gtk.ResponseType.OK))
        dialog.set_default_size(800, 400)

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            print "Select clicked"
            print "Folder selected: " + dialog.get_filename()
        elif response == Gtk.ResponseType.CANCEL:
            print "Cancel clicked"

        dialog.destroy()

# Funzioni caratteristiche
def crop_pathnames(path_list, sep='michele'):
    b=[]
    for j in path_list: b.append(string.split(j,sep)[1])
    return b

def write_header(tex_file):
    out=open(tex_file,'w')
    header=(
'''\chapter{Matlab Code}
\label{chptr:Matlab}
\lstset{language=matlab,
basicstyle=\\fontfamily{pcr}\\footnotesize,
numberstyle=\\tiny,
commentstyle=\color{blue}\itshape,
stringstyle=\color{red},
showstringspaces=false,
tabsize=3,
numbers=left}\n\n'''
)
    out.write(header)
    out.close()

def write_section(m_file,tex_file):
    input_file=open(m_file,'r')
    output_file=open(tex_file,'a')
    #nome_m_file=string.split(m_file,'/')[-1]
    nome_m_file=string.split(os.path.splitext(m_file)[0],'/')[-1]
    header=('\section{%s}\n\label{sec:%s}\n' % (nome_m_file,nome_m_file))
    body=input_file.read()
    output_file.write(header)
    output_file.write(body+'\n')
    input_file.close()
    output_file.close()

def write_on_tex_file(list_of_m_files,tex_file):
        write_header(tex_file)
        for m_file in list_of_m_files:
            write_section(m_file,tex_file)

# Esegui il programma
win = FileChooserWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()