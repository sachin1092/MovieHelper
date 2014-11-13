#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os

# import sip
import sys
# sip.setapi('QString', 2)
# sip.setapi('QVariant', 2)

from PyQt4.QtCore import *
from PyQt4.QtGui import *

class droppableLabel(QLabel):
    fileDropped = pyqtSignal(list)

    def __init__(self, type, parent=None):
        super(droppableLabel, self).__init__(parent)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls:
            event.accept()

        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls:
            event.setDropAction(Qt.CopyAction)
            event.accept()

        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasUrls:
            event.setDropAction(Qt.CopyAction)
            event.accept()
            links = []
            for url in event.mimeData().urls():
                links.append(str(url.toLocalFile()))

            self.fileDropped.emit(links)

        else:
            event.ignore()

class droppableWidget(QWidget):
    def __init__(self, parent=None):
        super(droppableWidget, self).__init__(parent)

        self.setWindowTitle("Movie Helper")

        self.setStyleSheet("QWidget{background-color: #fff;\n"
"color: rgb(0, 0, 0);\n"
"border: 1px;\n"
"border-radius: 2px;}\n")

        self.label = droppableLabel(self)
        self.label.fileDropped.connect(self.on_label_fileDropped)
        self.label.setText(QApplication.translate("QWidget", "Drop a folder\n"
"or\n"
"Click button to select a folder.", None, QApplication.UnicodeUTF8))
        # self.label.setMinimumSize(QSize(40, 100))
        self.label.setMinimumSize(QSize(450, 450))
        self.label.setMaximumSize(QSize(450, 450))
        font = QFont()
        font.setFamily("Roboto")
        font.setPointSize(18)
        font.setWeight(75)
        font.setItalic(True)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAcceptDrops(True)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("\n"
"    background: rgb(63, 81, 181); \n"
"    border-radius: 225px;\n"
"    color:#fff\n"
"")


        self.label.setAlignment(Qt.AlignCenter)

        self.folderButton = QPushButton(self)
        self.folderButton.setObjectName("folderButton")
        self.folderButton.setMinimumHeight(50)
        self.folderButton.setText(QApplication.translate("QWidget", "Select Folder", None, QApplication.UnicodeUTF8))

        self.folderButton.setStyleSheet("QPushButton{\n"
"border: 1px;\n"
"border-radius: 2px;\n"
"border-color: #000;\n"
"background-color:#fff;\n"
"font: 9pt \"Roboto\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color:#e0e0e0;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: #9e9e9e;\n"
"}")

        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.addWidget(self.label)
        self.verticalLayout.addWidget(self.folderButton)
        self.verticalLayout.setMargin(10)

        self.folderButton.clicked.connect(self.fbuttonclicked)

    def fbuttonclicked(self):
        file = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.on_label_fileDropped([file])
        print file
        print type(file)

    @pyqtSlot(list)
    def on_label_fileDropped(self, fileNames):
        droppedFiles = [    fileName
                            for fileName in fileNames
                            if os.path.exists(fileName)
                            ]

        if droppedFiles:
            keyModifiers = QApplication.keyboardModifiers()
            if keyModifiers == Qt.ShiftModifier:
                print "SHIFT"
                formatter = "\n"                

            elif keyModifiers == Qt.ControlModifier:
                print "CTRL"
                formatter = ","

            else:
                print "NONE"
                formatter = "|"

            self.label.setText(formatter.join(droppedFiles))
            self.newWindow(list(set(self.get_files(fileNames))))

    def get_files(self, roots):
        # rv = {}
        rv = []
        for root in roots:
            for cwd, folders, files in os.walk(root):
                for fname in files:
                    # os.path.splitext splits a filename into a tuple like so:
                    # (file_path, extension)
                    if os.path.splitext(fname)[1] in self.extensions:
                        # key = filename, value = directory of file
                        rv.append(fname)

        if len(rv) == 0:
            for root in roots:
                if os.path.splitext(root)[1] in self.extensions:
                    rv.append(root.split("/")[-1])
        return rv
    extensions = [".3g2", ".3gp", ".asf", ".asx", ".avi", ".flv", ".m4v", ".mov", ".mp4", ".mpg", ".rm", ".swf", ".vob", ".wmv", ".aepx", ".ale", ".avp", ".avs", ".bdm", ".bik", ".bin", ".bsf", ".camproj", ".cpi", ".dash", ".divx", ".dmsm", ".dream", ".dvdmedia", ".dvr-ms", ".dzm", ".dzp", ".edl", ".f4v", ".fbr", ".fcproject", ".hdmov", ".imovieproj", ".ism", ".ismv", ".m2p", ".mkv", ".mod", ".moi", ".mpeg", ".mts", ".mxf", ".ogv", ".otrkey", ".pds", ".prproj", ".psh", ".r3d", ".rcproject", ".rmvb", ".scm", ".smil", ".snagproj", ".sqz", ".stx", ".swi", ".tix", ".trp", ".ts", ".veg", ".vf", ".vro", ".webm", ".wlmp", ".wtv", ".xvid", ".yuv", ".3gp2", ".3gpp", ".3p2", ".890", ".aaf", ".aec", ".aep", ".aetx", ".ajp", ".amc", ".amv", ".amx", ".arcut", ".arf", ".avb", ".avchd", ".avv", ".axm", ".bdmv", ".bdt3", ".bmc", ".bmk", ".camrec", ".ced", ".cine", ".cip", ".clpi", ".cmmp", ".cmmtpl", ".cmproj", ".cmrec", ".cst", ".d2v", ".d3v", ".dat", ".dce", ".dck", ".dcr", ".dcr", ".dir", ".dmsd", ".dmsd3d", ".dmss", ".dmx", ".dpa", ".dpg", ".dv", ".dv-avi", ".dvr", ".dvx", ".dxr", ".dzt", ".evo", ".eye", ".eyetv", ".ezt", ".f4p", ".fbz", ".fcp", ".ffm", ".flc", ".flh", ".fli", ".fpdx", ".ftc", ".gcs", ".gfp", ".gifv", ".gts", ".hdv", ".hkm", ".ifo", ".imovieproject", ".ircp", ".ismc", ".ivr", ".izz", ".izzy", ".jss", ".jts", ".jtv", ".kdenlive", ".lrv", ".m1pg", ".m21", ".m21", ".m2t", ".m2ts", ".m2v", ".mani", ".mgv", ".mj2", ".mjp", ".mk3d", ".mnv", ".mp21", ".mp21", ".mpgindex", ".mpl", ".mpls", ".mproj", ".mpv", ".mqv", ".msdvd", ".mse", ".mswmm", ".mtv", ".mvd", ".mve", ".mvp", ".mvp", ".mvy", ".mxv", ".ncor", ".nsv", ".nuv", ".nvc", ".ogm", ".ogx", ".pac", ".pgi", ".photoshow", ".piv", ".plproj", ".pmf", ".ppj", ".prel", ".pro", ".prtl", ".pxv", ".qtl", ".qtz", ".rcd", ".rdb", ".rec", ".rmd", ".rmp", ".rms", ".roq", ".rsx", ".rum", ".rv", ".rvid", ".rvl", ".sbk", ".scc", ".screenflow", ".sdv", ".sedprj", ".seq", ".sfvidcap", ".siv", ".smi", ".smi", ".smk", ".stl", ".svi", ".swt", ".tda3mt", ".thp", ".tivo", ".tod", ".tp", ".tp0", ".tpd", ".tpr", ".trec", ".tsp", ".ttxt", ".tvlayer", ".tvs", ".tvshow", ".usf", ".usm", ".vbc", ".vc1", ".vcpf", ".vcv", ".vdo", ".vdr", ".vep", ".vfz", ".vgz", ".viewlet", ".vlab", ".vp6", ".vp7", ".vpj", ".vsp", ".wcp", ".wmd", ".wmmp", ".wmx", ".wp3", ".wpl", ".wve", ".wvx", ".xej", ".xel", ".xesc", ".xfl", ".xlmv", ".y4m", ".zm1", ".zm2", ".zm3", ".zmv", ".264", ".3gpp2", ".3mm", ".60d", ".aet", ".anx", ".avc", ".avd", ".avs", ".awlive", ".axv", ".bdt2", ".bnp", ".box", ".bs4", ".bu", ".bvr", ".byu", ".camv", ".clk", ".cx3", ".dav", ".ddat", ".dif", ".dlx", ".dmb", ".dmsm3d", ".dnc", ".dv4", ".f4f", ".fbr", ".ffd", ".flx", ".gvp", ".h264", ".inp", ".int", ".irf", ".iva", ".ivf", ".jmv", ".k3g", ".ktn", ".lrec", ".lsx", ".lvix", ".m1v", ".m2a", ".m4u", ".meta", ".mjpg", ".modd", ".moff", ".moov", ".movie", ".mp2v", ".mp4.infovid", ".mp4v", ".mpe", ".mpl", ".mpsub", ".mvc", ".mvex", ".mys", ".osp", ".par", ".playlist", ".pns", ".pro4dvd", ".pro5dvd", ".proqc", ".pssd", ".pva", ".pvr", ".qt", ".qtch", ".qtindex", ".qtm", ".rp", ".rts", ".sbt", ".scn", ".sfd", ".sml", ".smv", ".spl", ".str", ".tdt", ".tid", ".tvrecording", ".vcr", ".vem", ".vft", ".vfw", ".vid", ".video", ".vix", ".vs4", ".vse", ".w32", ".wm", ".wot", ".xmv", ".yog", ".787", ".am", ".anim", ".aqt", ".bix", ".cel", ".cvc", ".db2", ".dsy", ".gl", ".gom", ".grasp", ".gvi", ".ismclip", ".ivs", ".kmv", ".lsf", ".m15", ".m4e", ".m75", ".mmv", ".mob", ".mpeg1", ".mpeg4", ".mpf", ".mpg2", ".mpv2", ".msh", ".mvb", ".nut", ".orv", ".pjs", ".pmv", ".psb", ".rmd", ".rmv", ".rts", ".scm", ".sec", ".ssf", ".ssm", ".tdx", ".vdx", ".viv", ".vivo", ".vp3", ".zeg"]

    def newWindow(self, names):
        self.hide()
        import main
        self.form2 = main.MainWindow(files=names)
        self.form2.show()



# class MainWindow(QMainWindow, mainGui.Ui_mainWindow):
#
#     def __init__(self, parent=None):
#         super(MainWindow, self).__init__(parent)
#         self.setupUi(self)


# def startDialog():
#     app = QApplication(sys.argv)
#     main = droppableWidget()
#     main.show()
#     # app.exec_()
#     sys.exit(app.exec_())

app = QApplication(sys.argv)
main = droppableWidget()
main.show()
sys.exit(app.exec_())
# app.exec_()




