#!/usr/bin/env python3

# =====================================================
#                  Author The-Repo-Club
# =====================================================

import sys
import getpass
import os
import shutil
import subprocess
import Functions as fn
from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtWidgets import *

class ShutdownMenu(QDialog):
    # CANCEL - LOGOUT - SUSPEND - RESTART - SHUTDOWN- HIBERNATE- LOCK
    cancel_button = None
    logout_button = None
    suspend_button = None
    restart_button = None
    shutdown_button = None
    hibernate_button = None
    lock_button = None

    def __init__(self):
        super().__init__()
        if not fn.os.path.isdir(fn.home + "/.config/qt-logout"):
            fn.os.mkdir(fn.home + "/.config/qt-logout")

        if not fn.os.path.isfile(fn.home + "/.config/qt-logout/settings.conf"):
            shutil.copy(fn.root_config, fn.home + "/.config/qt-logout/settings.conf")

        fn.get_config(self, fn.config)
        self.icon_size = int(self.icon_size)
        self.icon_font_size = str(self.icon_font_size)
        self.title_font_size = str(self.title_font_size)
        self.icon_font_weight = str(self.icon_font_weight)
        self.title_font_weight = str(self.title_font_weight)
        self.opacity = str(self.opacity)
        self.buttons = str(self.buttons)
        self.init_ui()

    def init_ui(self):
        vbox = QVBoxLayout()
        self.setWindowTitle("Shutdown menu")

        self.text = QLabel("Hello, " + getpass.getuser() + "! What would you like to do?")
        self.text.setStyleSheet("QLabel {background-color:transparent;font-size: "+self.title_font_size+"pt;font-weight: "+self.title_font_weight+";border: none;color : white;}")

        hbox = QGridLayout()

        self.cancel_button = QToolButton()
        self.cancel_button.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.cancel_button.setIcon(QIcon.fromTheme("go-home"))
        self.cancel_button.setIconSize(QSize(self.icon_size, self.icon_size))
        self.cancel_button.setToolTip("Exit Application")
        self.cancel_button.setText("Exit Application")
        self.cancel_button.setStyleSheet("QToolButton {background-color:transparent;font-size: "+self.icon_font_size+"pt;font-weight: "+self.icon_font_weight+";border: none;color : white;}")
        self.cancel_button.setShortcut("ctrl+q")
        self.cancel_button.clicked.connect(self.cancel)

        self.logout_button = QToolButton()
        self.logout_button.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.logout_button.setIcon(QIcon.fromTheme("system-log-out"))
        self.logout_button.setIconSize(QSize(self.icon_size, self.icon_size))
        self.logout_button.setToolTip("Logout")
        self.logout_button.setText("Logout")
        self.logout_button.setStyleSheet("QToolButton {background-color:transparent;font-size: "+self.icon_font_size+"pt;font-weight: "+self.icon_font_weight+";border: none;color : white;}")
        self.logout_button.setShortcut("ctrl+e")
        self.logout_button.clicked.connect(self.logout)

        self.suspend_button = QToolButton()
        self.suspend_button.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.suspend_button.setIcon(QIcon.fromTheme("system-suspend"))
        self.suspend_button.setIconSize(QSize(self.icon_size, self.icon_size))
        self.suspend_button.setToolTip("Suspend")
        self.suspend_button.setText("Suspend")
        self.suspend_button.setStyleSheet("QToolButton {background-color:transparent;font-size: "+self.icon_font_size+"pt;font-weight: "+self.icon_font_weight+";border: none;color : white;}")
        self.suspend_button.setShortcut("ctrl+s")
        self.suspend_button.clicked.connect(self.suspend)

        self.restart_button = QToolButton()
        self.restart_button.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.restart_button.setIcon(QIcon.fromTheme("system-reboot"))
        self.restart_button.setIconSize(QSize(self.icon_size, self.icon_size))
        self.restart_button.setToolTip("Reboot")
        self.restart_button.setText("Restart")
        self.restart_button.setStyleSheet("QToolButton {background-color:transparent;font-size: "+self.icon_font_size+"pt;font-weight: "+self.icon_font_weight+";border: none;color : white;}")
        self.restart_button.setShortcut("ctrl+r")
        self.restart_button.clicked.connect(self.restart)

        self.shutdown_button = QToolButton()
        self.shutdown_button.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.shutdown_button.setIcon(QIcon.fromTheme("system-shutdown"))
        self.shutdown_button.setIconSize(QSize(self.icon_size, self.icon_size))
        self.shutdown_button.setToolTip("Shutdown")
        self.shutdown_button.setText("Shutdown")
        self.shutdown_button.setStyleSheet("QToolButton {background-color:transparent;font-size: "+self.icon_font_size+"pt;font-weight: "+self.icon_font_weight+";border: none;color : white;}")
        self.shutdown_button.setShortcut("ctrl+p")
        self.shutdown_button.clicked.connect(self.shutdown)

        self.hibernate_button = QToolButton()
        self.hibernate_button.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.hibernate_button.setIcon(QIcon.fromTheme("system-suspend-hibernate"))
        self.hibernate_button.setIconSize(QSize(self.icon_size, self.icon_size))
        self.hibernate_button.setToolTip("Hibernate")
        self.hibernate_button.setText("Hibernate")
        self.hibernate_button.setStyleSheet("QToolButton {background-color:transparent;font-size: "+self.icon_font_size+"pt;font-weight: "+self.icon_font_weight+";border: none;color : white;}")
        self.hibernate_button.setShortcut("ctrl+p")
        self.hibernate_button.clicked.connect(self.hibernate)

        self.lock_button = QToolButton()
        self.lock_button.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.lock_button.setIcon(QIcon.fromTheme("system-lock-screen"))
        self.lock_button.setIconSize(QSize(self.icon_size, self.icon_size))
        self.lock_button.setToolTip("Lock-Screen")
        self.lock_button.setText("Lock-Screen")
        self.lock_button.setStyleSheet("QToolButton {background-color:transparent;font-size: "+self.icon_font_size+"pt;font-weight: "+self.icon_font_weight+";border: none;color : white;}")
        self.lock_button.setShortcut("ctrl+p")
        self.lock_button.clicked.connect(self.lock)

        vbox.addWidget(self.text)
        if 'cancel' in self.buttons:
            hbox.addWidget(self.cancel_button,1,0, Qt.AlignTop)
        if 'logout' in self.buttons:
            hbox.addWidget(self.logout_button,1,1, Qt.AlignTop)
        if 'suspend' in self.buttons:
            hbox.addWidget(self.suspend_button,1,2, Qt.AlignTop)
        if 'restart' in self.buttons:
            hbox.addWidget(self.restart_button,1,3, Qt.AlignTop)
        if 'shutdown' in self.buttons:
            hbox.addWidget(self.shutdown_button,1,4, Qt.AlignTop)
        if 'hibernate' in self.buttons:
            hbox.addWidget(self.hibernate_button,1,5, Qt.AlignTop)
        if 'lock' in self.buttons:
            hbox.addWidget(self.lock_button,1,6, Qt.AlignTop)
        vbox.addLayout(hbox)

        vbox.setAlignment(Qt.AlignCenter)
        vbox.setSpacing(75)

        base = QWidget()
        base.setObjectName("base")
        base.setLayout(vbox)

        baseLyt = QVBoxLayout()
        baseLyt.addWidget(base)
        baseLyt.setContentsMargins(QMargins())
        self.setLayout(baseLyt)

        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setStyleSheet("QWidget {background-color: rgba(0,0,0,"+self.opacity+");}")

    def cancel(self):
        self.disable_buttons()
        self.close()

    def logout(self):
        self.disable_buttons()
        logout_systemctl()
        self.close()

    def suspend(self):
        out = subprocess.run(["sh", "-c", "cat /proc/1/comm"], shell=False, stdout=subprocess.PIPE)
        system = out.stdout.decode().split("=")[0].strip()

        self.disable_buttons()
        suspend_systemctl(system)
        self.close()

    def restart(self):
        out = subprocess.run(["sh", "-c", "cat /proc/1/comm"], shell=False, stdout=subprocess.PIPE)
        system = out.stdout.decode().split("=")[0].strip()

        self.disable_buttons()
        reboot_systemctl(system)
        self.close()

    def shutdown(self):
        out = subprocess.run(["sh", "-c", "cat /proc/1/comm"], shell=False, stdout=subprocess.PIPE)
        system = out.stdout.decode().split("=")[0].strip()

        self.disable_buttons()
        shutdown_systemctl(system)
        self.close()

    def hibernate(self):
        out = subprocess.run(["sh", "-c", "cat /proc/1/comm"], shell=False, stdout=subprocess.PIPE)
        system = out.stdout.decode().split("=")[0].strip()

        self.disable_buttons()
        hibernate_systemctl(system)
        self.close()

    def lock(self):
        self.disable_buttons()
        lock_systemctl(self.cmd_lock)
        self.close()

    def disable_buttons(self):
        self.cancel_button.setEnabled(False)
        self.logout_button.setEnabled(False)
        self.suspend_button.setEnabled(False)
        self.restart_button.setEnabled(False)
        self.shutdown_button.setEnabled(False)
        self.hibernate_button.setEnabled(False)
        self.lock_button.setEnabled(False)


def logout_systemctl():
    desktop = os.environ["DESKTOP_SESSION"]

    print("Your desktop is " + desktop)
    if desktop in ("herbstluftwm", "/usr/share/xsessions/herbstluftwm"):
        os.system( "herbstclient quit")
    elif desktop in ("bspwm", "/usr/share/xsessions/bspwm"):
        os.system("pkill bspwm")
    elif desktop in ("jwm", "/usr/share/xsessions/jwm"):
        os.system("pkill jwm")
    elif desktop in ("openbox", "/usr/share/xsessions/openbox"):
        os.system("pkill openbox")
    elif desktop in ("awesome", "/usr/share/xsessions/awesome"):
        os.system("pkill awesome")
    elif desktop in ("qtile", "/usr/share/xsessions/qtile"):
        os.system("pkill qtile")
    elif desktop in ("xmonad", "/usr/share/xsessions/xmonad"):
        os.system("pkill xmonad")
    elif desktop in ("dwm", "/usr/share/xsessions/dwm"):
        os.system("pkill dwm")
    elif desktop in ("instawm", "/usr/share/xsessions/instawm"):
        os.system("pkill instawm")
    elif desktop in ("instantwm", "/usr/share/xsessions/instantwm"):
        os.system("pkill instantwm")
    elif desktop in ("i3", "/usr/share/xsessions/i3"):
        os.system("pkill i3")
    elif desktop in ("i3-with-shmlog", "/usr/share/xsessions/i3-with-shmlog"):
        os.system("pkill i3-with-shmlog")
    elif desktop in ("lxqt", "/usr/share/xsessions/lxqt"):
        os.system("pkill lxqt")
    elif desktop in ("spectrwm", "/usr/share/xsessions/spectrwm"):
        os.system("pkill spectrwm")
    elif desktop in ("xfce", "/usr/share/xsessions/xfce"):
        os.system("pkill xfce")
    elif desktop in ("sway", "/usr/bin/sway"):
        os.system("pkill sway")

    return None

def suspend_systemctl(system):
    if system == 'init':
        os.system("loginctl suspend")

    if system == 'systemd':
        os.system("systemctl suspend")

    if system == 'runit':
        os.system("loginctl suspend")


def reboot_systemctl(system):
    if system == 'init':
        os.system("loginctl reboot")

    if system == 'systemd':
        os.system("systemctl reboot")

    if system == 'runit':
        os.system("loginctl reboot")

def shutdown_systemctl(system):
    if system == 'init':
        os.system("loginctl poweroff")

    if system == 'systemd':
        os.system("systemctl poweroff")

    if system == 'runit':
        os.system("loginctl poweroff")

def hibernate_systemctl(system):
    if system == 'init':
        os.system("loginctl hibernate")

    if system == 'systemd':
        os.system("systemctl hibernate")

    if system == 'runit':
        os.system("loginctl hibernate")

def lock_systemctl(command):
    os.system(command)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        app = QApplication(sys.argv)
        Gui = ShutdownMenu()
        Gui.showFullScreen()
        sys.exit(app.exec())
    else:
        out = subprocess.run(["sh", "-c", "cat /proc/1/comm"], shell=False, stdout=subprocess.PIPE)
        system = out.stdout.decode().split("=")[0].strip()

        if sys.argv[1] == "logout":
            logout_systemctl()
        elif sys.argv[1] == "suspend":
            suspend_systemctl(system)
        elif sys.argv[1] == "reboot":
            reboot_systemctl(system)
        elif sys.argv[1] == "shutdown":
            shutdown_systemctl(system)
        elif sys.argv[1] == "hibernate":
            hibernate_systemctl(system)
        elif sys.argv[1] == "lock":
            lock_systemctl('multimonitorlock -l -- --timestr="%H:%M"')
