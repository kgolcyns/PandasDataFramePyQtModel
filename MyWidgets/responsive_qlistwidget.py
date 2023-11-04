# responsive_qlistwidget.py
# Version = 0.1
# Subclass of qlistwidget with added signal for if has current item
from PyQt5.QtWidgets import QListWidget
from PyQt5.QtCore import pyqtSignal

def connect(signal, slot):
    signal.connect(slot)

class ResponsiveQListWidget(QListWidget):
    hasCurrentChanged = pyqtSignal(bool)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.currentItemChanged.connect(self._onCurrentItemChanged)
    
    def _onCurrentItemChanged(self, current, previous):
        """Emit hasCurrent if the change in current item is a change
        in of weather has current item or None.
        Only emited if the change is different to avoid redundant signals.
        and potential infinite loops.
        """
        if type(current) is type(previous):
            return None
        
        #if current is None:
        #    self.hasCurrentChanged.emit(False)
        #else:
        #    self.hasCurrentChanged.emit(True)
        ##TODO: test if is not None better than proper if statement
        self.hasCurrentChanged.emit(current is not None)
    
    def hasCurrent(self):
        """Returns True if the list has a current item, False if not.
        Note: this method is provided for convenience in this class,
        and for convience when initilizing to manually emit the hasCurrentChanged signal.
        since the signal is only emited when the current item changes: it can be easy to miss
        when using this class, as data has to be added to the list before connections are made
        to other widgets that listen for the hasCurrentChanged signal. otherwise if data is added
        but never removed, the signal will never be emited.
        Therefore this method can be used to emit the signal manually after data is added to the list.
        to initilize the widgets:
        
        listWidget = ResponsiveQListWidget()
        listWidget.addItems(["item1", "item2", "item3"])
        
        #...
        # connections to other widgets
        button = QPushButton("Choose")
        listWidget.hasCurrentChanged.connect(button.setEnabled)

        listWidget.hasCurrentChanged.emit(listWidget.hasCurrent())

        """
        return self.currentItem() is not None
    
    def touch(self):
        """Convience method for manually emitting currentItemChanged signal
        with the value of hasCurrent. Equivalent to:
        self.hasCurrentChanged.emit(self.hasCurrent())
        """
        self.hasCurrentChanged.emit(self.hasCurrent())

if __name__ == "__main__":
    # Test
    # TODO: Figureout how to disable deselction, so that selection always syns up with current item,
    # since many styles do not render the current item and only selected, despite the fact that
    # current item and selection are independent of each other.
    import sys
    from PyQt5.QtWidgets import *
    app = QApplication(sys.argv)
    widget = QWidget()

    listWidget = ResponsiveQListWidget()
    #listWidget.addItems(["item1", "item2", "item3"])

    buttonChoose = QPushButton("Choose")
    buttonAdd = QPushButton("Add")
    buttonRemove = QPushButton("Remove")
    buttonTouch = QPushButton("Touch")
    buttonTouch.setToolTip("Touch the list to emit hasCurrentChanged<br />listWidget.hasCurrentChanged.emit(listWidget.hasCurrent())")

    buttonSetCurrentNone = QPushButton("Set Current None")
    buttonSetCurrentNone.setToolTip("Set the current item to None reguardgless of list having items or not<br />listWidget.setCurrentItem(None)")

    labelDebuggingControls = QLabel("Debugging Controls:")
    labelDebuggingControls.setToolTip("These buttons are for testing the behavior of the list widget<br />commands and not setup or indended for how they would be used in a real application.<br>" \
                                      "ex) The remove button should mimic the same enabled behavior as the choose button in a real application, but in debugging it must always be enabled to send commands")
    # connections
    #listWidget.hasCurrentChanged.connect(buttonChoose.setEnabled)
    connect(listWidget.hasCurrentChanged, buttonChoose.setEnabled)

    connect(buttonAdd.clicked, lambda: listWidget.addItem("item"))
    connect(buttonRemove.clicked, lambda: listWidget.takeItem(listWidget.currentRow()))
    connect(buttonSetCurrentNone.clicked, lambda: listWidget.setCurrentItem(None))
    connect(buttonTouch.clicked, listWidget.touch)
    listWidget.touch() # NOTE: Comment this out to test the initilization behavior using touch button.


    # layout configuration
    layout = QVBoxLayout()
    controlsLayout = QHBoxLayout()
    controlsLayout2 = QHBoxLayout()

    layout.addWidget(listWidget)
    layout.addWidget(buttonChoose)
    layout.addWidget(labelDebuggingControls)

    controlsLayout.addWidget(buttonAdd)
    controlsLayout.addWidget(buttonRemove)

    controlsLayout2.addWidget(buttonTouch)
    controlsLayout2.addWidget(buttonSetCurrentNone)

    layout.addLayout(controlsLayout)
    layout.addLayout(controlsLayout2)

    widget.setLayout(layout)

    widget.show(); widget.raise_()
    sys.exit(app.exec_())