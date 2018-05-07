# gui.py

import config_editor
import os
import pdf_creator
import wx

from parsers import parse_json, parse_xml

wildcard = ("XML (*.xml)|*.xml|"
            "JSON (*.json)|*.json|"
            "All files (*.*)|*.*")


class PDFPanel(wx.Panel):
    """
    Panel container for holding the PDF generation
    widgets
    """

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.main_sizer = wx.BoxSizer(wx.VERTICAL)
        self.std_paths = wx.StandardPaths.Get()

        self.data_file = wx.TextCtrl(self, style=wx.TE_READONLY)
        data_file_btn = wx.Button(self, label='Data File')
        data_file_btn.Bind(wx.EVT_BUTTON, self.get_data_file)
        self.layout(self.data_file, data_file_btn)

        self.output_path = wx.TextCtrl(self, style=wx.TE_READONLY)
        output_btn = wx.Button(self, label='Output Folder')
        output_btn.Bind(wx.EVT_BUTTON, self.get_output_path)
        self.layout(self.output_path, output_btn)

        generate_btn = wx.Button(self, label='Generate PDF')
        generate_btn.Bind(wx.EVT_BUTTON, self.generate_pdf)
        self.main_sizer.Add(generate_btn, 0, wx.ALL|wx.CENTER, 5)

        self.SetSizer(self.main_sizer)

    def layout(self, txt, btn):
        """
        Layout the text control and related button
        """
        hsizer = wx.BoxSizer(wx.HORIZONTAL)
        hsizer.Add(txt, 1, wx.ALL, 5)
        hsizer.Add(btn, 0, wx.ALL, 5)
        self.main_sizer.Add(hsizer, 0, wx.EXPAND)


    def get_data_file(self, event):
        """
        Get the data file path
        """
        dlg = wx.FileDialog(
            self, message='Choose a data file',
            defaultDir=self.std_paths.GetDocumentsDir(),
            defaultFile="",
            wildcard=wildcard,
            style=wx.FD_OPEN | wx.FD_MULTIPLE | wx.FD_CHANGE_DIR
        )
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            self.data_file.SetValue(path)
            dlg.Destroy()

    def get_output_path(self, event):
        """
        Get the output folder
        """
        dlg = wx.FileDialog(
            self, message="Save file",
            defaultDir=self.std_paths.GetDocumentsDir(),
            defaultFile="",
            wildcard="PDF (*.pdf)|*.pdf",
            style=wx.FD_SAVE
            )
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            name, ext = os.path.splitext(path)
            if not ext:
                path += '.pdf'
            self.output_path.SetValue(path)
        dlg.Destroy()

    def generate_pdf(self, event):
        """
        Create the PDF
        """
        supported_ext_types = ['.json', '.xml']

        data_file = self.data_file.GetValue()
        output_path = self.output_path.GetValue()
        _, ext = os.path.splitext(data_file)

        if not data_file:
            self.show_error_msg('A data file is required')
            return

        if ext not in supported_ext_types:
            msg = 'PDF Creator only accepts the following file types: {}'
            self.show_error_msg(msg.format(supported_ext_types))
            return

        if not output_path:
            self.show_error_msg('You must choose an output folder')
            return

        if ext == '.xml':
            data = parse_xml(data_file)
        elif ext == '.json':
            data = parse_json(data_file)

        eob = pdf_creator.EOB(data,
                              pdf_file=output_path)
        eob.save()

        dlg = wx.MessageDialog(
            parent=None,
            message='PDF saved to {}'.format(self.output_path.GetValue()),
            caption='PDF Saved',
            style=wx.OK|wx.ICON_INFORMATION
        )
        dlg.ShowModal()
        dlg.Destroy()

    def show_error_msg(self, msg):
        """
        Display an error message
        """
        dlg = wx.MessageDialog(parent=None,
                               message=msg,
                               caption='Error',
                               style=wx.OK|wx.ICON_ERROR)
        dlg.ShowModal()
        dlg.Destroy()


class PDFFrame(wx.Frame):
    """
    The top level container for the panel and menu
    """

    def __init__(self):
        wx.Frame.__init__(self, None, title='PDF Creator')
        panel = PDFPanel(self)
        self.create_menu()
        self.Show()

    def create_menu(self):
        """
        Create the menu
        """
        menubar = wx.MenuBar()

        file_menu = wx.Menu()
        exit_menu_item = file_menu.Append(
            wx.NewId(), 'Exit', 'Exit the application')
        menubar.Append(file_menu, '&File')
        self.Bind(wx.EVT_MENU, self.on_exit, exit_menu_item)

        edit_menu = wx.Menu()
        config_menu_item = edit_menu.Append(
            wx.NewId(),'Config', 'Edit config')
        menubar.Append(edit_menu, '&Edit')
        self.Bind(wx.EVT_MENU, self.on_edit_config, config_menu_item)

        self.SetMenuBar(menubar)

    def on_edit_config(self, event):
        """
        Edit the configuration
        """
        dlg = config_editor.ConfigDialog()
        dlg.ShowModal()
        dlg.Destroy()

    def on_exit(self, event):
        """
        Close the application
        """
        self.Close()


if __name__ == '__main__':
    app = wx.App(False)
    frame = PDFFrame()
    app.MainLoop()