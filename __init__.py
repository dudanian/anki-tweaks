from anki.hooks import addHook
from aqt import mw
from aqt.qt import QAction

from .tweaks import replaceDivs

# replace divs
def bulkReplaceDivs(nids):
    mw.checkpoint("Replace <div> with <br>")
    mw.progress.start()
    for nid in nids:
        replaceDivs(mw.col.getNote(nid))

    mw.progress.finish()
    mw.reset()

def onReplaceDivs(browser):
    bulkReplaceDivs(browser.selectedNotes())


# menu stuff
def setupMenu(browser):
    menu = browser.form.menubar.addMenu("&Tweaks")

    a = QAction("Replace <div> with <br>", browser)
    a.triggered.connect(lambda: onReplaceDivs(browser))
    menu.addAction(a)

addHook("browser.setupMenus", setupMenu)
