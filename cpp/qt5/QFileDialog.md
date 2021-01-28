 1. [`QFileDialog` restrict for the users only the respective path](https://forum.qt.io/topic/76690/qfiledialog-restrict-for-the-users-only-the-respective-path)
    
    Two solution:
    
    ```        
    void dirchanged(QString dir)
    {
         if (dir out of scope)
             m_Fdialog->setDirectory("<last/valid/dir/> or <your/specific/DIR/path>");
    }
    
    QFileDialog dialog(this);
    connect(&dialog, &QFileDialog::directoryEntered, this, &dirChanged);
    ```
