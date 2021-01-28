 1. [`QFileDialog` restrict for the users only the respective path](https://forum.qt.io/topic/76690/qfiledialog-restrict-for-the-users-only-the-respective-path)
    
    Two solution:
    
    ```
    connect(m_Fdialog,SIGNAL(currentChanged(QString)),SLOT(dirchanged(QString)));
    
    void Dialog::dirchanged(QString dir)
    {
         m_Fdialog->setDirectory("<your specific DIR path>");
    }
    ```
    
    Or:
    
    ```
    QFileDialog dialog(this);
    connect(&dialog, SIGNAL(directoryEntered(const QString &)), this, SLOT(onFileDialogDirectoryChanged(const QString &)));
    ```
