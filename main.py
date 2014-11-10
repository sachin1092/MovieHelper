#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import operator
import time
import json
import os

from PySide.QtCore import *
from PySide.QtGui import *

import mainGui
import movielookup


class MainWindow(QMainWindow, mainGui.Ui_mainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.table_view = self.tvEverything
        self.table_model = self.MyTableModel(self, (), self.header)
        self.table_view.setModel(self.table_model)
        self.table_view.horizontalHeader().setResizeMode(QHeaderView.Stretch)
        self.table_view.setSortingEnabled(True)
        self.backButton.clicked.connect(self.anotherFolder)
        self.backButton.setText("Close")
        self.startThread()

    def anotherFolder(self):
        sys.exit(0)

    def allDone(self):
        self.progressBar.hide()

    def startThread(self):
        self.workerThread = WorkerThread(files.pop())
        self.connect(self.workerThread, SIGNAL("threadDone(QString)"), self.doThing, Qt.DirectConnection)
        self.connect(self.workerThread, SIGNAL("allDone()"), self.allDone, Qt.DirectConnection)
        self.workerThread.start()

    def doThing(self, text):
        jsonvalues = json.loads(text)
        mtup = (jsonvalues["Title"], jsonvalues["imdbRating"], jsonvalues["Released"], jsonvalues["Runtime"],
                jsonvalues["Genre"])
        self.table_model.updateTableData(mtup)
        self.startThread()

    class MyTableModel(QAbstractTableModel):
        def __init__(self, parent, mylist, header, *args):
            QAbstractTableModel.__init__(self, parent, *args)
            self.mylist = mylist
            self.header = header

        def updateTableData(self, tup):
            self.emit(SIGNAL("layoutAboutToBeChanged()"))
            self.mylist.append(tup)
            self.mylist = list(set(self.mylist))
            self.emit(SIGNAL("layoutChanged()"))


        def rowCount(self, parent):
            return len(self.mylist)

        def columnCount(self, parent):
            return len(self.mylist[0])

        def data(self, index, role):
            if not index.isValid():
                return None
            elif role != Qt.DisplayRole:
                return None
            return self.mylist[index.row()][index.column()]

        def headerData(self, col, orientation, role):
            if orientation == Qt.Horizontal and role == Qt.DisplayRole:
                return self.header[col]
            return None

        def sort(self, col, order):
            """sort table by given column number col"""
            print "col", col
            self.emit(SIGNAL("layoutAboutToBeChanged()"))
            if col == 2:
                self.mylist = sorted(self.mylist, key=lambda tup: time.mktime(
                    time.strptime(tup[2].split()[0] + " " + tup[2].split()[1] + " " + getYear(tup[2].split()[2]),
                                  "%d %b %y")))
            elif col == 3:
                self.mylist = sorted(self.mylist, key=lambda tup: getDuration(tup[3]))
            else:
                self.mylist = sorted(self.mylist,
                                     key=operator.itemgetter(col))

            if order == Qt.DescendingOrder:
                self.mylist.reverse()
            self.emit(SIGNAL("layoutChanged()"))


    header = [' Title ', ' Rating ', ' Released ', ' Runtime ', ' Genre ']


def getDuration(text):
    if text == "N/A":
        return 0
    return int(text.split()[0])


class WorkerThread(QThread):
    def __init__(self, text, parent=None):
        super(WorkerThread, self).__init__(parent)
        self.name = text

    def run(self):
        for i in self.name:
            print i
            print type(i)
            response = movielookup.finder(i)
            print response
            self.emit(SIGNAL("threadDone(QString)"), response)
        self.emit(SIGNAL("allDone()"))


files = []

def get_files(roots):
    # rv = {}
    rv = []
    for root in roots:
        for cwd, folders, files in os.walk(root):
            for fname in files:
                # os.path.splitext splits a filename into a tuple like so:
                # (file_path, extension)
                if os.path.splitext(fname)[1] in extensions:
                    # key = filename, value = directory of file
                    # rv[fname] = cwd
                    rv.append(fname)

    if len(rv) == 0:
        for root in roots:
            if os.path.splitext(root)[1] in extensions:
                rv.append(root.split("/")[-1])
    return rv


extensions = [".3g2", ".3gp", ".asf", ".asx", ".avi", ".flv", ".m4v", ".mov", ".mp4", ".mpg", ".rm", ".swf", ".vob",
              ".wmv", ".aepx", ".ale", ".avp", ".avs", ".bdm", ".bik", ".bin", ".bsf", ".camproj", ".cpi", ".dash",
              ".divx", ".dmsm", ".dream", ".dvdmedia", ".dvr-ms", ".dzm", ".dzp", ".edl", ".f4v", ".fbr", ".fcproject",
              ".hdmov", ".imovieproj", ".ism", ".ismv", ".m2p", ".mkv", ".mod", ".moi", ".mpeg", ".mts", ".mxf", ".ogv",
              ".otrkey", ".pds", ".prproj", ".psh", ".r3d", ".rcproject", ".rmvb", ".scm", ".smil", ".snagproj", ".sqz",
              ".stx", ".swi", ".tix", ".trp", ".ts", ".veg", ".vf", ".vro", ".webm", ".wlmp", ".wtv", ".xvid", ".yuv",
              ".3gp2", ".3gpp", ".3p2", ".890", ".aaf", ".aec", ".aep", ".aetx", ".ajp", ".amc", ".amv", ".amx",
              ".arcut", ".arf", ".avb", ".avchd", ".avv", ".axm", ".bdmv", ".bdt3", ".bmc", ".bmk", ".camrec", ".ced",
              ".cine", ".cip", ".clpi", ".cmmp", ".cmmtpl", ".cmproj", ".cmrec", ".cst", ".d2v", ".d3v", ".dat", ".dce",
              ".dck", ".dcr", ".dcr", ".dir", ".dmsd", ".dmsd3d", ".dmss", ".dmx", ".dpa", ".dpg", ".dv", ".dv-avi",
              ".dvr", ".dvx", ".dxr", ".dzt", ".evo", ".eye", ".eyetv", ".ezt", ".f4p", ".fbz", ".fcp", ".ffm", ".flc",
              ".flh", ".fli", ".fpdx", ".ftc", ".gcs", ".gfp", ".gifv", ".gts", ".hdv", ".hkm", ".ifo",
              ".imovieproject", ".ircp", ".ismc", ".ivr", ".izz", ".izzy", ".jss", ".jts", ".jtv", ".kdenlive", ".lrv",
              ".m1pg", ".m21", ".m21", ".m2t", ".m2ts", ".m2v", ".mani", ".mgv", ".mj2", ".mjp", ".mk3d", ".mnv",
              ".mp21", ".mp21", ".mpgindex", ".mpl", ".mpls", ".mproj", ".mpv", ".mqv", ".msdvd", ".mse", ".mswmm",
              ".mtv", ".mvd", ".mve", ".mvp", ".mvp", ".mvy", ".mxv", ".ncor", ".nsv", ".nuv", ".nvc", ".ogm", ".ogx",
              ".pac", ".pgi", ".photoshow", ".piv", ".plproj", ".pmf", ".ppj", ".prel", ".pro", ".prtl", ".pxv", ".qtl",
              ".qtz", ".rcd", ".rdb", ".rec", ".rmd", ".rmp", ".rms", ".roq", ".rsx", ".rum", ".rv", ".rvid", ".rvl",
              ".sbk", ".scc", ".screenflow", ".sdv", ".sedprj", ".seq", ".sfvidcap", ".siv", ".smi", ".smi", ".smk",
              ".stl", ".svi", ".swt", ".tda3mt", ".thp", ".tivo", ".tod", ".tp", ".tp0", ".tpd", ".tpr", ".trec",
              ".tsp", ".ttxt", ".tvlayer", ".tvs", ".tvshow", ".usf", ".usm", ".vbc", ".vc1", ".vcpf", ".vcv", ".vdo",
              ".vdr", ".vep", ".vfz", ".vgz", ".viewlet", ".vlab", ".vp6", ".vp7", ".vpj", ".vsp", ".wcp", ".wmd",
              ".wmmp", ".wmx", ".wp3", ".wpl", ".wve", ".wvx", ".xej", ".xel", ".xesc", ".xfl", ".xlmv", ".y4m", ".zm1",
              ".zm2", ".zm3", ".zmv", ".264", ".3gpp2", ".3mm", ".60d", ".aet", ".anx", ".avc", ".avd", ".avs",
              ".awlive", ".axv", ".bdt2", ".bnp", ".box", ".bs4", ".bu", ".bvr", ".byu", ".camv", ".clk", ".cx3",
              ".dav", ".ddat", ".dif", ".dlx", ".dmb", ".dmsm3d", ".dnc", ".dv4", ".f4f", ".fbr", ".ffd", ".flx",
              ".gvp", ".h264", ".inp", ".int", ".irf", ".iva", ".ivf", ".jmv", ".k3g", ".ktn", ".lrec", ".lsx", ".lvix",
              ".m1v", ".m2a", ".m4u", ".meta", ".mjpg", ".modd", ".moff", ".moov", ".movie", ".mp2v", ".mp4.infovid",
              ".mp4v", ".mpe", ".mpl", ".mpsub", ".mvc", ".mvex", ".mys", ".osp", ".par", ".playlist", ".pns",
              ".pro4dvd", ".pro5dvd", ".proqc", ".pssd", ".pva", ".pvr", ".qt", ".qtch", ".qtindex", ".qtm", ".rp",
              ".rts", ".sbt", ".scn", ".sfd", ".sml", ".smv", ".spl", ".str", ".tdt", ".tid", ".tvrecording", ".vcr",
              ".vem", ".vft", ".vfw", ".vid", ".video", ".vix", ".vs4", ".vse", ".w32", ".wm", ".wot", ".xmv", ".yog",
              ".787", ".am", ".anim", ".aqt", ".bix", ".cel", ".cvc", ".db2", ".dsy", ".gl", ".gom", ".grasp", ".gvi",
              ".ismclip", ".ivs", ".kmv", ".lsf", ".m15", ".m4e", ".m75", ".mmv", ".mob", ".mpeg1", ".mpeg4", ".mpf",
              ".mpg2", ".mpv2", ".msh", ".mvb", ".nut", ".orv", ".pjs", ".pmv", ".psb", ".rmd", ".rmv", ".rts", ".scm",
              ".sec", ".ssf", ".ssm", ".tdx", ".vdx", ".viv", ".vivo", ".vp3", ".zeg"]


def getYear(text):
    return text[-2] + text[-1]


def startMain(names, app):
    # app = QApplication(sys.argv)
    print names
    files.append(names)
    form1 = MainWindow()
    form1.show()
    app.exec_()