# PandasDataFrameModel.py
# Pandas QAbstract Item Model wrapper
# for pandas data frame, with extras to implement
from PyQt5.QtCore import QAbstractTableModel, Qt #, pyqtSignal
import pandas as pd


class PandasDataFrameModel(QAbstractTableModel):
    """Qt Model for Pandas Data Frame base implimentation for viewing data"""
    def __init__(self, dataFrame=None):
        super().__init__()
        if dataFrame is None:
            #self._data = pd.DataFrame()
            self.setDataFrame(pd.DataFrame())
        else:
            #self._data = dataFrame
            self.setDataFrame(dataFrame)
    
    def dataFrame(self):
        return self._data
    
    def setDataFrame(self, dataFrame):
        self._data = dataFrame
        self.layoutChanged.emit()
    
    def clear(self):
        self.setDataFrame(pd.DataFrame())
        self.layoutChanged.emit()
    
    def rowCount(self, index):
        """
        Return the number of rows in the model
        rowCount(self, index: QModelIndex) -> self._data.shape[0]
        """
        return self._data.shape[0]
    
    def columnCount(self, index):
        """
        Return the number of columns in the model
        columnCount(self, index: QModelIndex) -> self._data.shape[1]
        """
        return self._data.shape[1]
    
    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self._dataDisplayRole(index, role)
        
        # general purpose roles (default implementation returns None)
        if role == Qt.DecorationRole:
            return self._dataDecorationRole(index, role)
        
        if role == Qt.EditRole:
            return self._dataEditRole(index, role)
        
        if role == Qt.ToolTipRole:
            return self._dataToolTipRole(index, role)
        
        if role == Qt.StatusTipRole:
            return self._dataStatusTipRole(index, role)
        
        if role == Qt.WhatsThisRole:
            return self._dataWhatsThisRole(index, role)
        
        if role == Qt.SizeHintRole:
            return self._dataSizeHintRole(index, role)
        
        # Roles Describing the appearance and meta data (with associated types)
        if role == Qt.FontRole:
            return self._dataFontRole(index, role)
        
        if role == Qt.TextAlignmentRole:
            return self._dataTextAlignmentRole(index, role)
        
        if role == Qt.BackgroundRole:
            return self._dataBackgroundRole(index, role)
        
        if role == Qt.BackgroundColorRole:
            return self._dataBackgroundColorRole(index, role)
        
        if role == Qt.ForegroundRole:
            return self._dataForegroundRole(index, role)
        
        if role == Qt.TextColorRole:
            return self._dataTextColorRole(index, role)
        
        if role == Qt.CheckStateRole:
            return self._dataCheckStateRole(index, role)
        
        if role == Qt.InitialSortOrderRole:
            return self._dataInitialSortOrderRole(index, role)
        
        # Accessibility roles:
        if role == Qt.AccessibleTextRole:
            return self._dataAccessibleTextRole(index, role)
        
        if role == Qt.AccessibleDescriptionRole:
            return self._dataAccessibleDescriptionRole(index, role)
        
        # User roles:
        if role >= Qt.UserRole:
            return self._dataUserRole(index, role)
        
    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole:
            return self._headerDataDisplayRole(section, orientation, role)
        
        # general purpose roles (default implementation returns None)
        if role == Qt.DecorationRole:
            return self._headerDataDecorationRole(section, orientation, role)
        
        if role == Qt.EditRole:
            return self._headerDataEditRole(section, orientation, role)
        
        if role == Qt.ToolTipRole:
            return self._headerDataToolTipRole(section, orientation, role)
        
        if role == Qt.StatusTipRole:
            return self._headerDataStatusTipRole(section, orientation, role)
        
        if role == Qt.WhatsThisRole:
            return self._headerDataWhatsThisRole(section, orientation, role)
        
        if role == Qt.SizeHintRole:
            return self._headerDataSizeHintRole(section, orientation, role)
        
        # Roles Describing the appearance and meta data (with associated types)
        if role == Qt.FontRole:
            return self._headerDataFontRole(section, orientation, role)
        
        if role == Qt.TextAlignmentRole:
            return self._headerDataTextAlignmentRole(section, orientation, role)
        
        if role == Qt.BackgroundRole:
            return self._headerDataBackgroundRole(section, orientation, role)
        
        if role == Qt.BackgroundColorRole:
            return self._headerDataBackgroundColorRole(section, orientation, role)
        
        if role == Qt.ForegroundRole:
            return self._headerDataForegroundRole(section, orientation, role)
        
        if role == Qt.TextColorRole:
            return self._headerDataTextColorRole(section, orientation, role)
        
        if role == Qt.CheckStateRole:
            return self._headerDataCheckStateRole(section, orientation, role)
        
        if role == Qt.InitialSortOrderRole:
            return self._headerDataInitialSortOrderRole(section, orientation, role)
        
        # Accessibility roles:
        if role == Qt.AccessibleTextRole:
            return self._headerDataAccessibleTextRole(section, orientation, role)
        
        if role == Qt.AccessibleDescriptionRole:
            return self._headerDataAccessibleDescriptionRole(section, orientation, role)
        
        # User roles:
        if role >= Qt.UserRole:
            return self._headerDataUserRole(section, orientation, role)
    
    
    '''Implementations of Item Data Roles'''
    ##### Data Mapper function #####
    def _dataRoleMapping_(self, role):
        """Alternative method for this
        TODO: To Test Later for performance"""
        ItemDataRoles = {
                         Qt.DisplayRole : self._dataDisplayRole,
                      Qt.DecorationRole : self._dataDecorationRole,
                            Qt.EditRole : self._dataEditRole,
                         Qt.ToolTipRole : self._dataToolTipRole,
                       Qt.StatusTipRole : self._dataStatusTipRole,
                       Qt.WhatsThisRole : self._dataWhatsThisRole,
                        Qt.SizeHintRole : self._dataSizeHintRole,
            
                             Qt.FontRole : self._dataFontRole,
                    Qt.TextAlignmentRole : self._dataTextAlignmentRole,
                       Qt.BackgroundRole : self._dataBackgroundRole,
                  Qt.BackgroundColorRole : self._dataBackgroundColorRole,
                       Qt.ForegroundRole : self._dataForegroundRole,
                        Qt.TextColorRole : self._dataTextColorRole,
                       Qt.CheckStateRole : self._dataCheckStateRole,
                 Qt.InitialSortOrderRole : self._dataInitialSortOrderRole,
            
                   Qt.AccessibleTextRole : self._dataAccessibleTextRole,
            Qt.AccessibleDescriptionRole : self._dataAccessibleDescriptionRole,
            
                             Qt.UserRole : self._dataUserRole,
        }
        if role >= Qt.UserRole:
            return self._dataUserRole
        else:
            return ItemDataRoles.get(role, None)

    
    def _dataDisplayRole(self, index, role):
        """
        Default implementation in data(...) under Qt.DisplayRole
        called inside data(...) if role == Qt.DisplayRole
        Can reimplement this method if needed
        returns str(self._data.iloc[index.row(), index.column()])
        """
        return str(self._data.iloc[index.row(), index.column()])
    
    def _dataDecorationRole(self, index, role):
        """
        Default implementation in data(...) under Qt.DecorationRole
        called inside data(...) if role == Qt.DecorationRole
        Can reimplement this method if needed
        
        returns QColor, QIcon, or QPixmap
        """
        return None
    def _dataEditRole(self, index, role):
        """
        Default implementation in data(...) under Qt.EditRole
        called inside data(...) if role == Qt.EditRole
        Can reimplement this method if needed
        
        returns str
        """
        return None
    def _dataToolTipRole(self, index, role):
        """
        Default implementation in data(...) under Qt.ToolTipRole
        called inside data(...) if role == Qt.ToolTipRole
        Can reimplement this method if needed
        
        returns str
        """
        return None
        #TODO: probably too anoyting to display tool tip for data (that isnt header),
        #      but tooltip might be useful for displaying row and column associated with data
        #row = index.row(); col = index.column()
        #value = self._data.iloc[row, col]
        #return str('iloc[{0}, {1}]= {2}'.format(row, col, value))
        
    def _dataStatusTipRole(self, index, role):
        """
        Default implementation in data(...) under Qt.StatusTipRole
        called inside data(...) if role == Qt.StatusTipRole
        Can reimplement this method if needed
        
        returns str
        """
        row = index.row(); col = index.column()
        value = self._data.iloc[row, col]
        return str('iloc[{0}, {1}]= {2}'.format(row, col, value))
    
    def _dataWhatsThisRole(self, index, role):
        """
        Default implementation in data(...) under Qt.WhatsThisRole
        called inside data(...) if role == Qt.WhatsThisRole
        Can reimplement this method if needed
        
        returns str
        """
        return None
    def _dataSizeHintRole(self, index, role):
        """
        Default implementation in data(...) under Qt.SizeHintRole
        called inside data(...) if role == Qt.SizeHintRole
        Can reimplement this method if needed
        
        returns QSizeHintRole
        """
        return None

    # Roles describing appearance and meta data (with associated types)
    def _dataFontRole(self, index, role):
        """
        Default implementation in data(...) under Qt.FontRole
        called inside data(...) if role == Qt.FontRole
        Can reimplement this method if needed
        
        returns QFont
        """
        return None
    def _dataTextAlignmentRole(self, index, role):
        """
        Default implementation in data(...) under Qt.TextAlignmentRole
        called inside data(...) if role == Qt.TextAlignmentRole
        Can reimplement this method if needed
        
        returns Qt.AlignmentFlag
        """
        return None
    def _dataBackgroundRole(self, index, role):
        """
        Default implementation in data(...) under Qt.BackgroundRole
        called inside data(...) if role == Qt.BackgroundRole
        Can reimplement this method if needed
        
        returns QBrush
        """
        return None
    def _dataBackgroundColorRole(self, index, role):
        """
        Default implementation in data(...) under Qt.BackgroundColorRole
        called inside data(...) if role == Qt.BackgroundColorRole
        Can reimplement this method if needed
        
        Note: This role is obsolete. Use BackgroundRole instead.
        returns None
        """
        return None
    def _dataForegroundRole(self, index, role):
        """
        Default implementation in data(...) under Qt.ForegroundRole
        called inside data(...) if role == Qt.ForegroundRole
        Can reimplement this method if needed
        
        returns QBrush
        """
        return None
    def _dataTextColorRole(self, index, role):
        """
        Default implementation in data(...) under Qt.TextColorRole
        called inside data(...) if role == Qt.TextColorRole
        Can reimplement this method if needed
        
        Note: This role is obsolete. Use ForegroundRole instead.
        returns None
        """
        return None
    def _dataCheckStateRole(self, index, role):
        """
        Default implementation in data(...) under Qt.CheckStateRole
        called inside data(...) if role == Qt.CheckStateRole
        Can reimplement this method if needed
        
        returns Qt.CheckState
        """
        return None
    def _dataInitialSortOrderRole(self, index, role):
        """
        Default implementation in data(...) under Qt.InitialSortOrderRole
        called inside data(...) if role == Qt.InitialSortOrderRole
        Can reimplement this method if needed
        
        returns Qt.SortOrder
        """
        return None
    
    # Accessibility roles:
    def _dataAccessibleTextRole(self, index, role):
        """
        Default implementation in data(...) under Qt.AccessibleTextRole
        called inside data(...) if role == Qt.AccessibleTextRole
        Can reimplement this method if needed
        
        returns str
        """
        return None
    def _dataAccessibleDescriptionRole(self, index, role):
        """
        Default implementation in data(...) under Qt.AccessibleDescriptionRole
        called inside data(...) if role == Qt.AccessibleDescriptionRole
        Can reimplement this method if needed
        
        returns str
        """
        return None
    
    # User roles:
    def _dataUserRole(self, index, role):
        """
        Default implementation in data(...) under Qt.UserRole
        called inside data(...) if role >= Qt.UserRole
        Qt.UserRole = 256 (0x0100)
        Can reimplement this method if needed
        
        returns up to user what to return 
        """
        return None
    
    
    '''Implementation of headerData methods'''
    def _headerDataDisplayRole(self, section, orientation, role):
        """
        Default implementation in headerData(...) under Qt.DisplayRole
        called inside headerData(...) if role == Qt.DisplayRole
        Can reimplement this method if needed
        -Returns str(self._data.columns[section]) if orientation == Qt.Horizontal
        -Returns str(self._data.index[section]) if orientation == Qt.Vertical
        
        returns str(self._data.columns[section])
        """
        if orientation == Qt.Horizontal:
            return str(self._data.columns[section])
        
        if orientation == Qt.Vertical:
            return str(self._data.index[section])
    
    def _headerDataDecorationRole(self, section, orientation, role):
        """
        Default implementation in headerData(...) under Qt.DecorationRole
        called inside headerData(...) if role == Qt.DecorationRole
        Can reimplement this method if needed
        
        returns None
        """
        return None
    def _headerDataEditRole(self, section, orientation, role):
        """
        Default implementation in headerData(...) under Qt.EditRole
        called inside headerData(...) if role == Qt.EditRole
        Can reimplement this method if needed
        
        returns None
        """
        return None
    def _headerDataToolTipRole(self, section, orientation, role):
        """
        Default implementation in headerData(...) under Qt.ToolTipRole
        called inside headerData(...) if role == Qt.ToolTipRole
        Can reimplement this method if needed
        -Returns str(self._data.columns[section]) if orientation == Qt.Horizontal
        -Returns str(self._data.index[section]) if orientation == Qt.Vertical
        
        returns str
        """
        if orientation == Qt.Horizontal:
            return str(self._data.columns[section])
        
        if orientation == Qt.Vertical:
            return str(self._data.index[section])
    
    def _headerDataStatusTipRole(self, section, orientation, role):
        """
        Default implementation in headerData(...) under Qt.StatusTipRole
        called inside headerData(...) if role == Qt.StatusTipRole
        Can reimplement this method if needed
        
        returns str
        """
        return None
    def _headerDataWhatsThisRole(self, section, orientation, role):
        """
        Default implementation in headerData(...) under Qt.WhatsThisRole
        called inside headerData(...) if role == Qt.WhatsThisRole
        Can reimplement this method if needed
        
        returns str
        """
        return None
    def _headerDataSizeHintRole(self, section, orientation, role):
        """
        Default implementation in headerData(...) under Qt.SizeHintRole
        called inside headerData(...) if role == Qt.SizeHintRole
        Can reimplement this method if needed
        
        returns QSizeHintRole
        """
        return None
    def _headerDataFontRole(self, section, orientation, role):
        """
        Default implementation in headerData(...) under Qt.FontRole
        called inside headerData(...) if role == Qt.FontRole
        Can reimplement this method if needed
        
        returns QFont
        """
        return None
    def _headerDataTextAlignmentRole(self, section, orientation, role):
        """
        Default implementation in headerData(...) under Qt.TextAlignmentRole
        called inside headerData(...) if role == Qt.TextAlignmentRole
        Can reimplement this method if needed
        
        returns Qt.AlignmentFlag
        """
        return None
    def _headerDataBackgroundRole(self, section, orientation, role):
        """
        Default implementation in headerData(...) under Qt.BackgroundRole
        called inside headerData(...) if role == Qt.BackgroundRole
        Can reimplement this method if needed
        
        returns QBrush
        """
        return None
    def _headerDataBackgroundColorRole(self, section, orientation, role):
        """
        Default implementation in headerData(...) under Qt.BackgroundColorRole
        called inside headerData(...) if role == Qt.BackgroundColorRole
        Can reimplement this method if needed
        
        Note: This role is obsolete. Use BackgroundRole instead.
        returns None
        """
        return None
    def _headerDataForegroundRole(self, section, orientation, role):
        """
        Default implementation in headerData(...) under Qt.ForegroundRole
        called inside headerData(...) if role == Qt.ForegroundRole
        Can reimplement this method if needed
        
        returns QBrush
        """
        return None
    def _headerDataTextColorRole(self, section, orientation, role):
        """
        Default implementation in headerData(...) under Qt.TextColorRole
        called inside headerData(...) if role == Qt.TextColorRole
        Can reimplement this method if needed
        
        Note: This role is obsolete. Use ForegroundRole instead.
        returns None
        """
        return None
    def _headerDataCheckStateRole(self, section, orientation, role):
        """
        Default implementation in headerData(...) under Qt.CheckStateRole
        called inside headerData(...) if role == Qt.CheckStateRole
        Can reimplement this method if needed
        
        returns Qt.CheckState
        """
        return None
    def _headerDataInitialSortOrderRole(self, section, orientation, role):
        """
        Default implementation in headerData(...) under Qt.InitialSortOrderRole
        called inside headerData(...) if role == Qt.InitialSortOrderRole
        Can reimplement this method if needed
        
        returns Qt.SortOrder
        """
        return None
    def _headerDataAccessibleTextRole(self, section, orientation, role):
        """
        Default implementation in headerData(...) under Qt.AccessibleTextRole
        called inside headerData(...) if role == Qt.AccessibleTextRole
        Can reimplement this method if needed
        
        returns str
        """
        return None
    def _headerDataAccessibleDescriptionRole(self, section, orientation, role):
        """
        Default implementation in headerData(...) under Qt.AccessibleDescriptionRole
        called inside headerData(...) if role == Qt.AccessibleDescriptionRole
        Can reimplement this method if needed
        
        returns str
        """
        return None
    def _headerDataUserRole(self, section, orientation, role):
        """
        Default implementation in headerData(...) under Qt.UserRole
        called inside headerData(...) if role >= Qt.UserRole
        Qt.UserRole = 256 (0x0100)
        Can reimplement this method if needed
        
        returns up to user what to return 
        """
        return None


if __name__ == '__main__':
    # Testing model
    import sys
    import traceback
    import numpy as np
    from PyQt5.QtWidgets import *
    
    class Tester(QMainWindow):
        def __init__(self, parent=None):
            super().__init__(parent)
            self.setWindowTitle("Pandas DataFrame Model Tester")
            status = self.statusBar()
            self.testbuttonA = QPushButton("Test A")
            self.testbuttonB = QPushButton("Test B")
            self.testbuttonC = QPushButton("Test C")
            self.testbuttonClear = QPushButton("Clear")
            
            self.testbuttonA.clicked.connect(self.testA)
            self.testbuttonB.clicked.connect(self.testB)
            self.testbuttonC.clicked.connect(self.testC)
            self.testbuttonClear.clicked.connect(self.clear)
            
            self.model = PandasDataFrameModel()
            self.view = QTableView()
            self.view.setModel(self.model)
            
            # Config layouts
            self.layout = QVBoxLayout()
            self.layoutButtons = QHBoxLayout()
            
            # Test buttons layed out horizontally 
            # will be nested in overall layout
            self.layoutButtons.addWidget(self.testbuttonA)
            self.layoutButtons.addWidget(self.testbuttonB)
            self.layoutButtons.addWidget(self.testbuttonC)
            
            # set overall vertical layout
            self.layout.addWidget(self.view)
            self.layout.addLayout(self.layoutButtons)
            self.layout.addWidget(self.testbuttonClear)
            
            # set layout
            self.widget = QWidget()
            self.widget.setLayout(self.layout)
            self.setCentralWidget(self.widget)
        
        def testA(self):
            self.model.setDataFrame(pd.DataFrame(np.random.randint(0,100,size=(100, 4)), columns=list('ABCD')))
        
        def testB(self):
            self.model.setDataFrame(pd.DataFrame(np.random.randint(0,100,size=(100, 4)), columns=list('ABCD')))
        
        def testC(self):
            self.model.setDataFrame(pd.DataFrame(np.random.randint(0,100,size=(100, 4)), columns=list('ABCD')))
        
        def clear(self):
            self.model.clear()
        
        def excepthook(self, cls, err, tb):
            title = str(cls.__name__)
            TB = "".join(list(traceback.format_tb(tb)))
            body = "<b>"+str(cls.__name__)+"</b>: "+str(err)+"\n\n"+TB
            print(body)
            r = QMessageBox.critical(self, title, body, QMessageBox.Ok)
            
    app = QApplication(sys.argv)
    win = Tester()
    win.show()
    win.raise_()
    sys.excepthook = win.excepthook
    app.exec_()