class Welcome:
    """
    The class Welcome contains all real names of buttons, fields and hyperlinks from Welcome Screen. With Welcome.nameOfGetMethod() we call them.
    """
    def __init__(self):
        self.welcomeWindow = "{caption='' isvisible='true' type='org.eclipse.swt.widgets.Shell'}"
        self.devicePanelProjectHyperlink = "{caption='Device Panel Project' id='devicePanelWizardLink' styletype='hyperlink' visible='true' window=" + self.welcomeWindow + "}"
        self.systemPanelProjectHyperlink = "{caption='System Panel Project' id='systemPanelWizardLink' styletype='hyperlink' visible='true' window=" + self.welcomeWindow + "}"
        self.libraryProjectHyperlink = "{caption='Library Project' id='libraryPanelWizardLink' styletype='hyperlink' visible='true' window=" + self.welcomeWindow + "}"
        self.devicePanelProjectHyperlinkLink = "{caption='Device Panel Project' container=" + self.devicePanelProjectHyperlink + " styletype='text' visible='true'}"
        self.systemPanelProjectHyperlinkLink = "{caption='System Panel Project' container=" + self.systemPanelProjectHyperlink + " styletype='text' visible='true'}"
        self.libraryProjectHyperlinkLink = "{caption='Library Project' container=" + self.libraryProjectHyperlink + " styletype='text' visible='true'}"
        self.installPackageHyperlink = "{caption='Install Package' id='installPackage' styletype='hyperlink hyperlinkWelcomeWhite' visible='true' window=" + self.welcomeWindow + "}"
        self.installPackageHyperlinkLink = "{caption='Install Package' container=" + self.welcomeWindow + " styletype='text' visible='true'}"
        self.noInstallPackageLabel = "{caption='NO INSTALLED PACKAGES' id='noInstalledPackage' styletype='scs-label-package-error scs-label-package-error' visible='true' window= " + self.welcomeWindow + "}"
        self.closeWelcome = "{caption='X' styletype='label scs-closeLabel' visible='true' window=" + self.welcomeWindow + "}"
        self.closeWelcomeLabel = "{caption='X' container=" + self.closeWelcome + " styletype='text' visible='true'}"
        self.welcomeImage = "{id='welcomeTitle' styletype='image-view' visible='true' window=" + self.welcomeWindow + "}"
        self.perspectiveComboBox = "{id='perspectiveComboBox' styletype='combo-box-base combo-box' visible='true' window=" + self.welcomeWindow + "}"
        self.recentProjectsListView = "{id='recentProjectsListView' styletype='list-view' visible='true' window=" + self.welcomeWindow + "}"
        self.welcomeCheckBox = "{caption='Always show at startup' id='alwaysShowOnStartupCheckbox' styletype='check-box white-check-box' visible='true' window=" + self.welcomeWindow + "}"
        self.recentProject = "{container=" + self.recentProjectsListView + " styletype='cell indexed-cell list-cell' visible='true'}"

    def getWelcomeWindow(self):
        """
        Usage:
        Welcome().getWelcomeWindow()
        """
        return self.welcomeWindow

    def getWelcomeLabel(self, name):
        """
        @param name [string] name of text label from welcome screan

        Usage:
        Welcome().getWelcomeLabel(name)
        """
        welcomeLabel = "{caption='" + name + "' styletype='text' visible='true' window=" + self.welcomeWindow + "}"
        return welcomeLabel

    def getRecentProjectLabel(self, name):
        """
        @param name [string] name of the project from recent project label

        Usage:
        Welcome().getRecentProjectLabel()
        """
        recentProjectLabel = "{caption='" + name + "' container=" + self.recentProjectsListView + " styletype='text' visible='true'}"
        return recentProjectLabel

    def getDevicePanelProjectHyperlinkLink(self):
        """
        Usage:
        Welcome().getDevicePanelProjectHyperlinkLink()
        """
        return self.devicePanelProjectHyperlinkLink

    def getSystemPanelProjectHyperlinkLink(self):
        """
        Usage:
        Welcome().getSystemPanelProjectHyperlinkLink()
        """
        return self.systemPanelProjectHyperlinkLink

    def getLibraryProjectHyperlinkLink(self):
        """
        Usage:
        Welcome().getLibraryProjectHyperlinkLink()
        """
        return self.libraryProjectHyperlinkLink

    def getInstallPackageHyperlink(self):
        """
        Usage:
        Welcome().getInstallPackageHyperlink()
        """
        return self.installPackageHyperlink

    def getInstallPackageHyperlinkLink(self):
        """
        Usage:
        Welcome().getInstallPackageHyperlinkLink()
        """
        return self.installPackageHyperlinkLink

    def getNoInstallPackageLabel(self):
        """
        Usage:
        Welcome().getNoInstallPackageLabel()
        """
        return self.noInstallPackageLabel

    def getCloseWelcomeLabel(self):
        """
        Usage:
        Welcome().getCloseWelcomeLabel()
        """
        return self.closeWelcomeLabel

    def getWelcomeImage(self):
        """
        Usage:
        Welcome().getWelcomeImage()
        """
        return self.welcomeImage

    def getPerspectiveComboBox(self):
        """
        Usage:
        Welcome().getPerspectiveComboBox()
        """
        return self.perspectiveComboBox

    def getWelcomeCheckBox(self):
        """
        Usage:
        Welcome().getWelcomeCheckBox()
        """
        return self.welcomeCheckBox

    def getRecentProject(self):
        """
        Usage:
        Welcome().getRecentProject()
        """
        return self.recentProject

    def getSystemHyperlink(self, name):
        """
        @param name [string] name of system that is hiperlinked on welcome screan

        Usage:
        Welcome().getSystemHyperlink(name)
        """
        systemHyperlink = "{caption='" + name + "' id='hyperlinkCfgWelcome' styletype='hyperlinkCfgWelcome' visible='true' window=" + self.welcomeWindow + "}"
        return systemHyperlink

    def getButtonFromWelcomeScrean(self, name):
        """
        @param name [string] name of the button
        @return OpenAnotherProjectButton [string] real name of Open Another Project Button

        Usage:
        Welcome().getButtonFromWelcomeScrean("OPEN ANOTHER PROJECT"))
        """

        OpenAnotherProject = "{caption='" + name + "' id='openAnotherProjectButton' styletype='button scs-button' visible='true' window=" + self.welcomeWindow + "}"
        OpenAnotherProjectButton = "{caption='" + name + "' container=" + OpenAnotherProject + " styletype='text' visible='true'}"
        return OpenAnotherProjectButton

    def getCreateNewVirtualSystemWelcomeScreen(self, name):
        """
        @param name [string] name of the virtual system type
        @return CreateNewVirtualSystemWelcomeScreen [string]

        Usage:
        Welcome().getCreateNewVirtualSystemWelcomeScreen("cdb42L42")
        """
        CreateNewVirtualSystemWelcomeScreen = "{caption='" + name + "' id='hyperlinkCfgWelcome' styletype='hyperlinkCfgWelcome' visible='true' window=" + self.welcomeWindow + "}"
        return CreateNewVirtualSystemWelcomeScreen


class MainShell:
    """
    Class MainShell contains real names of Main window SCS IDE
    """
    def __init__(self):
        self.mainWindow = "{caption='SoundClear Studio' isvisible='true' type='org.eclipse.swt.widgets.Shell'}"
        '''
        This real name doesn't exist in SCS v1.0 and newer versions.
        '''
        # self.workingPerspectiveLink = "{caption='Switch to working perspective' id='perspectiveSwitchLink' styletype='hyperlink' visible='true' window= " + self.mainWindow + "}"
        self.mainShellMenu = "{menuStyle='SWT.BAR' type='org.eclipse.swt.widgets.Menu' window=" + self.mainWindow + "}"

    def getMainWindow(self):
        """
        Usage:
        MainShell().getMainWindow()
        """
        return self.mainWindow

    def getCTab(self, name):
        """
        @param name [string] name of CTab

        Usage:
        MainShell().getCTab(name)
        """
        cTabItem = "{caption='" + name + "' parent.visible='true' type='org.eclipse.swt.custom.CTabItem' window=" + self.mainWindow + "}"
        return cTabItem

    def getWindowClose(self, name):
        """
        @param name [string] name of close (X) button

        Usage:
        MainShell().getWindowClose(name)
        """
        windowClose = "{container=" + MainShell().getCTab(name) + " type='com.froglogic.squish.swt.CTabCloseBox'}"
        return windowClose

    def getPanelTab(self, name, tooltip):
        """
        @param name [string] name of panel tab
        @param tooltip [string] tooltip name

        Usage:
        MainShell().getPanelTab("Blank.panel", "Project/Blank.panel")
        """
        tab = "{caption='" + name + "' parent.visible='true' type='org.eclipse.swt.custom.CTabItem' item.tooltiptext='" + tooltip + "'window=" + self.mainWindow + "}"
        return tab

    """
    This getter method doesn't exist in SCS v1.0 and newer versions.
    """
    # def getWorkingPerspectiveLink(self):
    #     return self.workingPerspectiveLink

    def getCLabel(self, name):
        """
        @param name [string]

        Usage:
        MainShell().getCLabel(name)
        """
        return "{caption='" + name + "' id='PerspectiveStatusLabel' styletype='label' visible='true' window=" + self.mainWindow + "}"

    def getPyFilefield(self):
        """
        Usage:
        MainShell().getPyFilefield()
        """
        return "{container=" + self.mainWindow + " isvisible='true' type='org.eclipse.swt.custom.StyledText'}"

    def getMainShellMenu(self):
        return self.mainShellMenu


class PopupListView:
    """
    Real name of pop-up list view
    """
    def __init__(self):
        self.popupCtrl = "{basetype='javafx.scene.control.PopupControl' visible='true'}"
        self.popup = "{type='javafx.stage.Popup' visible='true'}"
        self.listView = "{container=" + self.popupCtrl + " id='list-view' styletype='list-view' visible='true'}"

    def getListView(self):
        """
        Usage:
        PopupListView().getListView()
        """
        return self.listView

    def getPopupItem(self, name):
        """
        Usage:
        PopupListView().getPopupItem("Basic Headset (Full Speed)")
        """
        item = "{caption='" + name + "' container=" + self.popup + " styletype='label label-name' visible='true'}"
        return item


class WarningShell:
    """
    Class contains real names of items from warning window
    """
    def __init__(self):
        self.warning = "{caption='' isvisible='true' type='org.eclipse.swt.widgets.Shell'}"

    def getNoButton(self):
        """
        Usage:
        WarningShell().getNoButton()
        """
        button = "{caption='NO' styletype='button scs-red-button scs-button' visible='true' window=" + self.warning + "}"
        return button

    def getButton(self, name):
        """
        @param name [string] name of button

        Usage:
        WarningShell().getButton(name)
        """
        button = "{caption='" + name + "' styletype='button scs-button' visible='true' window=" + self.warning + "}"
        return button

    def getLabel(self, name):
        """
        @param name [string] name of label

        Usage:
        WarningShell().getLabel(name)
        """
        label = "{caption='" + name + "' styletype='label' visible='true' window=" + self.warning + "}"
        return label


class PreviewWarningShell:
    """
    Preview Warning window
    """
    def __init__(self):
        self.warning = "{caption='Preview Warning' isvisible='true' type='org.eclipse.swt.widgets.Shell'}"

    def getOkButton(self):
        """
        Usage:
        PreviewWarningShell().getOkButton()
        """
        button = "{caption='OK' styletype='button scs-button' visible='true' window=" + self.warning + "}"
        return button


class ConfirmShell:
    """
    Class contains real names of Confirmation message window
    """
    def __init__(self):
        self.confirmShell = "{caption='' isvisible='true' type='org.eclipse.swt.widgets.Shell'}"
        self.confirmCheckBox = "{caption='Don\\'t show again' styletype='check-box' visible='true' window=" + self.confirmShell + "}"
        self.markConfirmCheckBox = "{container=" + self.confirmCheckBox + " styletype='mark' visible='true'}"
        self.confirmWindowLeftSection = "{styletype='-scs-common-gray' visible='true' window=" + self.confirmShell + "}"
        self.confirmWindowGridPane = "{type='javafx.scene.layout.GridPane' visible='true' window=" + self.confirmShell + "}"

    def getConfirmWindow(self):
        """
        Usage:
        ConfirmShell().getConfirmWindow()
        """

        return self.confirmShell

    def getConfirmShellButton(self, name):
        """
        @param name [string] name of button from confirm shell

        Usage:
        ConfirmShell().getConfirmShellButton("OK")
        """
        self.confirmShellButton = "{caption='" + name + "' styletype='button scs-button' visible='true' window=" + self.confirmShell + "}"
        return self.confirmShellButton

    def getConfirmCheckBox(self):
        """
        Usage:
        ConfirmShell().confirmCheckBox()
        """
        return self.confirmCheckBox

    def getMarkConfirmCheckBox(self):
        """
        Usage:
        ConfirmShell().confirmCheckBox()
        """
        return self.markConfirmCheckBox

    def getConfirmWindowLeftSection(self):
        """
        Usage:
        ConfirmShell().getConfirmWindowLeftSection()
        """
        return self.confirmWindowLeftSection

    def getConfirmWindowGridPane(self):
        """
        Usage:
        ConfirmShell().getConfirmWindowGridPane()
        """
        return self.confirmWindowGridPane


class InformationShell:
    """
    Class contains real names of Information message window
    """
    def __init__(self):
        self.confirmShell = "{caption='' isvisible='true' type='org.eclipse.swt.widgets.Shell'}"
        self.checkBox = "{caption='Don\\'t show again' styletype='check-box' visible='true' window=" + self.confirmShell + "}"

    def getInformationShellDialog(self):
        return self.confirmShell

    def getInformationShellDialogMessage(self, name):
        """
        @param name [string] name of label

        Usage:
        InformationShell().getInformationShellDialogMessage(name)
        """

        label = "{caption='" + name + "' container={caption='" + name + "' styletype='label' visible='true' window=" + self.confirmShell + "} styletype='text' visible='true'}"
        return label

    def getInformationShellButton(self, name):
        """
        @param name [string] name of button from information shell

        Usage:
        InformationShell().getInformationShellButton("OK")
        """
        self.informationShellButton = "{caption='" + name + "' styletype='button scs-button' visible='true' window=" + self.confirmShell + "}"
        return self.informationShellButton

    def getInformationShellLabel(self, name):
        """
        @param name [string] name of system

        Usage:
        InformationShell().getInformationShellLabel("cdb42l42(CDB42L42_test_1)")
        """
        self.informationShellLabel = "{caption='" + "Cannot connect to system \"" + name + "\" until its status becomes AVAILABLE. Please try again later." + "' styletype='label' visible='true' window=" + self.confirmShell + "}"
        return self.informationShellLabel

    def getCheckBox(self):
        return self.checkBox

    def getTitleLabel(self, title):
        titleLabel = "{caption?='*" + title + "*' styletype='label scs-DialogTitleLabel' visible='true' window=" + self.confirmShell + "}"
        return titleLabel


class ErrorShell:
    """
    Class contains real names of Error window
    """
    def __init__(self):
        self.errorShell = "{caption='' isvisible='true' type='org.eclipse.swt.widgets.Shell'}"

    def getErrorShell(self):
        return self.errorShell

    def getErrorShellButton(self, name):
        """
        @param name [string] name of button from error shell

        Usage:
        ErrorShell().getErrorShellButton("OK")
        """
        errorShellButton = "{caption='" + name + "' styletype='button scs-button' visible='true' window=" + self.errorShell + "}"
        return errorShellButton

    def getErrorShellLabel(self, name="Project build has encountered an error."):
        """
        Usage:
        ErrorShell().getErrorShellLabel("name of label")
        """
        errorShellLabel = "{caption='" + name + "' styletype='label' visible='true' window=" + self.errorShell + "}"
        return errorShellLabel

    def getErrorShellLabelText(self, text):
        """
        Usage:
        ErrorShell().getErrorShellLabelText("name of label")
        """
        errorShellLabel = "{caption='" + text + "' id='dialogContetLabel' styletype='label' visible='true' window=" + self.errorShell + "}"
        errorShellLabelText = "{caption='" + text + "' container=" + errorShellLabel + " styletype='text' visible='true'}"
        return errorShellLabelText

    def getTitleLabel(self, title):
        titleLabel = "{caption?='*" + title + "*' styletype='label scs-DialogTitleLabel' visible='true' window=" + self.errorShell + "}"
        return titleLabel


class BSPConfirmShell:
    """
    Confirmation message window for BSP
    """
    def __init__(self):
        self.confirmShell = "{caption='Support Package Installer' isvisible='true' type='org.eclipse.swt.widgets.Shell'}"
        self.bspLabelscs = "{caption='PACKAGES INSTALLED' styletype='label scs-welcomeTitle' visible='true' window=" + self.confirmShell + "}"

    def getConfirmShellButton(self, name):
        """
        Usage:
        BSPConfirmShell().getConfirmShellButton()
        """
        self.confirmShellButton = "{caption='" + name + "' styletype='button scs-button' visible='true' window=" + self.confirmShell + "}"
        return self.confirmShellButton

    def getBSPSLabelSCSWelcomeTitle(self):
        """
        Usage:
        BSPConfirmShell().getBSPSLabelSCSWelcomeTitle()
        """
        return self.bspLabelscs

    def getBSPCongfirmShellLabel(self, name):
        """
        @param [string] name labels caption
        Usage:
        BSPConfirmShell().getConfirmShellButton()
        """
        return "{caption='" + name + "' styletype='label' visible='true' window=" + self.confirmShell + "}"


class BSPUninstallShell:
    """
    Uninstall message window for BSP
    """
    def __init__(self):
        self.uninstallShell = "{caption='Support Package Uninstaller' isvisible='true' type='org.eclipse.swt.widgets.Shell'}"

    def getUninstallShellButton(self, name):
        """
        Usage:
        BSPUninstallShell().getUninstallShellButton("OK")
        """
        self.uninstallShellButton = "{caption='" + name + "' id='dialogButton' styletype='button scs-button' visible='true' window=" + self.uninstallShell + "}"
        return self.uninstallShellButton


class UninstallPackagesShell:
    """
    Uninstall package shell
    """
    def __init__(self):
        self.unistallPackageShell = "{caption='Uninstall Packages' isvisible='true' type='org.eclipse.swt.widgets.Shell'}"
        self.listView = "{styletype='list-view' visible='true' window=" + self.unistallPackageShell + "}"

    def getUninstallBSPCheckBox(self, bsp):
        """
        @param [string] bsp type
        @return unistall bsp check box real name
        Usage:
        UninstallPackagesShell().getUninstallBSPCheckBox("CDB42L42")
        """
        cell = "{container=" + self.listView + " styletype='cell indexed-cell list-cell' visible='true' item.pkg.bspcreationinfo.supportpackagename='" + bsp + " BSP'}"
        checkBox = "{caption='' container=" + cell + " styletype='check-box' visible='true'}"
        return checkBox

    def getButton(self, name):
        """
        @param name [string] button name
        @return Uninstall Packages Shell button
        Usage:
        UninstallPackagesShell().getButton("OK")
        """
        button = "{caption='" + name + "' id='dialogButton' styletype='button scs-button' visible='true' window=" + self.unistallPackageShell + "}"
        return button


class PackageUninstallSuccessful:
    """
    Package Uninstall Successful window
    """
    def __init__(self):
        self.packageUninstallSuccessful = "{caption='Package Uninstall Successful' isvisible='true' type='org.eclipse.swt.widgets.Shell'}"

    def getButton(self, name):
        """
        @param name [string] button name
        @return Package Uninstall Successful button
        Usage:
        PackageUninstallSuccessful().getButton("OK")
        """
        button = "{caption='" + name + "' id='dialogButton' styletype='button scs-button' visible='true' window=" + self.packageUninstallSuccessful + "}"
        return button


class Directory:
    """
    Class contains all real names from System Directory window. withh Directory().getNameOfItem() we call specific item.
    """
    def __init__(self):
        self.CTabItem = "{caption='Navigator' parent.visible='true' type='org.eclipse.swt.custom.CTabItem' window=" + MainShell().getMainWindow() + "}"
        self.systemDirectoryTree = "{container=" + self.CTabItem + " styletype='tree-view' visible='true'}"
        self.discoveredSystems = "{caption='Discovered systems' container=" + self.systemDirectoryTree + " styletype='cell indexed-cell tree-cell' visible='true'}"
        self.registerMap = "{caption='Register maps' container=" + self.systemDirectoryTree + " styletype='cell indexed-cell tree-cell' visible='true'}"
        self.toolItem = "{firstItemText='Navigator' isvisible='true' type='org.eclipse.swt.widgets.ToolBar' window=" + MainShell().getMainWindow() + "}"
        self.floatableView = "{caption='Navigator' id='directoryButton' styletype='button scs-top-toolbar-button' visible='true' window=" + MainShell().getMainWindow() + "}"
        self.CTabFolder = "{firstTabCaption='Navigator' isvisible='true' type='org.eclipse.swt.custom.CTabFolder' window=" + MainShell().getMainWindow() + "}"
        self.toolBar = "{container=" + self.CTabFolder + " firstItemText='Minimize' isvisible='true' type='org.eclipse.swt.widgets.ToolBar'}"
        self.floatableToolBar = "{container=" + self.CTabFolder + " firstItemText='Restore' isvisible='true' type='org.eclipse.swt.widgets.ToolBar'}"
        self.myProjects = "{caption='My Projects' container=" + self.systemDirectoryTree + " styletype='text' visible='true'}"
        self.myProjectsTab = "{caption='My Projects' container=" + self.systemDirectoryTree + " styletype='cell indexed-cell tree-cell' visible='true'}"
        self.contextMenu = "{type='com.cirrus.scs.ide.systemdirectory.ui.controls.SystemDirectoryContextMenu' visible='true'}"
        self.textFieldSearch = "{container=" + self.CTabItem + " styletype='text-input text-field scs-text-field-filter' visible='true'}"
        self.expandCollapseArrow = "{container=" + self.myProjectsTab + " styletype='arrow' visible='true'}"
        self.comboCheckBoxSearch = "{container=" + self.CTabItem + " styletype='scs-combo-box-search' visible='true'}"
        self.comboCheckBoxFilter = "{container=" + self.comboCheckBoxSearch + " styletype='combo-box-base combo-box' visible='true'}"
        self.saveAll = "{caption='Save all' id='saveAllButton' styletype='button scs-top-toolbar-button' visible='true' window=" + MainShell().getMainWindow() + "}"
        self.scrollBar = "{container=" + self.systemDirectoryTree + " styletype='scroll-bar' visible='true'}"
        self.topToolbarHBox = "{id='leftTopToolbarHBox' type='javafx.scene.layout.HBox' visible='true' window=" + MainShell().getMainWindow() + "}"
        self.floatableViewImage = "{container=" + self.floatableView + " styletype='image-view' visible='true'}"
        self.saveAllImage = "{container=" + self.saveAll + " styletype='image-view' visible='true'}"
        self.directoryClose = "{container=" + self.CTabItem + " type='com.froglogic.squish.swt.CTabCloseBox'}"
        self.overviewPanelTab = "{caption='Overview' parent.visible='true' type='org.eclipse.swt.custom.CTabItem' window=" + MainShell().getMainWindow() + "}"
        self.closeOverviewPanelTab = "{container=" + self.overviewPanelTab + " type='com.froglogic.squish.swt.CTabCloseBox'}"
        self.textFieldSearchContextMenu = "{type='com.cirrus.scs.ide.ui.javafx.controls.SCSContextMenu' visible='true'}"
        self.configurePerspectiveButton = "{caption='' id='configureButton' styletype='button scs-top-toolbar-button' visible='true' window=" + MainShell().getMainWindow() + "}"
        self.panelDevPerspectiveButton = "{caption='' id='panelDevelopmentButton' styletype='button scs-top-toolbar-button' visible='true' window=" + MainShell().getMainWindow() + "}"

    def getCTabItem(self):
        """
        Usage:
        Directory().getCTabItem()
        """
        return self.CTabItem

    def getCTabFolder(self):
        """
        Usage:
        Directory().getCTabFolder()
        """
        return self.CTabFolder

    def getSystemDirectoryTree(self):
        """
        Usage:
        Directory().getSystemDirectoryTree()
        """
        return self.systemDirectoryTree

    def getDiscoveredSystems(self):
        """
        Usage:
        Directory().getDiscoveredSystems()
        """
        return self.discoveredSystems

    def getBoardName(self, name):
        '''
        This method returns full board name using board nickname

        @param name [string] board nickname
        @return  full board name = CirrusLink + part of MAC address + nickname

        Usage:
        Directory().getBoardName(boardName)
        '''
        snooze(0.5)
        rnBoardName = "{caption?='*" + name + "*' container=" + self.systemDirectoryTree + " styletype='cell indexed-cell tree-cell' visible='true'}"
        boardName = name
        try:
            boardName = waitForObject(rnBoardName).text
            return boardName
        except LookupError:
            test.fail("FAIL", "Board with name " + boardName + " does not exist in Directory")
            return None

    def getBoardOrSystem(self, boardOrSysName):
        '''
        This method returns board or simulated system real name

        @param boardOrSysName: board or simulated name
        @return: board or simulated system real name

        Usage:
        Directory().getBoardOrSystem(boardName)
        '''
        name = "{caption?='*" + boardOrSysName + "*' container=" + self.systemDirectoryTree + " styletype='cell indexed-cell tree-cell' visible='true'}"
        return name

    def getDevice(self, name):
        """
        @param name [string] name of device

        Usage:
        Directory().getDevice(name)
        """
        if name != "CS46L41":
            device = "{caption='" + name + "' container=" + self.systemDirectoryTree + " styletype='cell indexed-cell tree-cell' item.treeitemtype='REGISTERMAP' visible='true'}"
        else:
            device = "{caption='" + name + "' container=" + self.systemDirectoryTree + " styletype='cell indexed-cell tree-cell' item.treeitemtype='DEVICE' visible='true'}"
        return device

    def getRegisterMap(self):
        """
        Usage:
        Directory().getRegisterMap()
        """
        return self.registerMap

    def getFloatableView(self):
        """
        Usage:
        Directory().getFloatableView()
        """
        return self.floatableView

    def getToolBar(self, option):
        """
        @param option [string] option

        Usage:
        Directory().getToolBar("Restore")
        """
        if option == 'Restore':
            cTab2 = "{firstTabCaption='Navigator' isvisible='true' type='org.eclipse.swt.custom.CTabFolder' window=" + MainShell().getMainWindow() + "}"
            return "{caption='Restore' container=" + cTab2 + " type='org.eclipse.swt.widgets.ToolItem'}"
        return "{caption='" + option + "' container=" + self.toolBar + " type='org.eclipse.swt.widgets.ToolItem'}"

    def FloatableToolBar(self, option):
        """
        @param option [string]

        Usage:
        Directory().FloatableToolBar(option)
        """
        return "{caption='" + option + "' container=" + self.floatableToolBar + " type='org.eclipse.swt.widgets.ToolItem'}"

    def getMyProjectsCell(self):
        """
        Usage:
        Directory().getMyProjectsCell()
        """
        return self.myProjectsTab

    def getMyProjects(self):
        """
        Usage:
        Directory().getMyProjects()
        """
        return self.myProjects

    def getProjectName(self, name):
        """
        @param name [string] name of project

        Usage:
        Directory().getProjectName(projectName)
        """
        projectName = "{caption?='*" + name + "*' container=" + self.systemDirectoryTree + " styletype='text' visible='true'}"
        return projectName

    def getContextMenu(self, context=None):
        """
        @param contex [string] default None(return real name of contex manu)

        Usage:
        Directory().getContextMenu()
        Directory().getContextMenu("Add New")
        Directory().getContextMenu("Add Existing")

        """
        if context == None:
            return self.contextMenu
        elif context == "Add New":
            return "{caption='Add New' type='javafx.scene.control.ContextMenu' visible='true'}"
        elif context == "Add Existing":
            return "{caption='Add Existing' type='javafx.scene.control.ContextMenu' visible='true'}"
        elif context == "Open Project(s)":
            return "{caption='Open Project(s)' type='javafx.scene.control.ContextMenu' visible='true'}"

    def getLabelFromUpdateFirmwareShell(self, labelName):
        """
        @param labelName [string] name of the label from contex menu

        Usage:
        Directory().getLabelFromContexMenu("Save registers state")
        """
        contexMenu = "{type='com.cirrus.scs.ide.systemdirectory.ui.controls.SystemDirectoryContextMenu' visible='true'}"
        label = "{caption='" + labelName + "' container=" + contexMenu + " styletype='label' visible='true'}"
        return label

    def getSearchTextField(self):
        """
        Usage:
        Directory().getSearchTextField()
        """
        return "{container=" + self.textFieldSearch + " type='javafx.scene.layout.Pane' visible='true'}"

    def getExpandAllButton(self):
        """
        Usage:
        Directory().getExpandAllButton()
        """
        return "{caption='' container=" + self.CTabItem + " styletype='button scs-navigator-buttons scs-expand-all-button' visible='true'}"

    def getCollapseAllButton(self):
        """
        Usage:
        Directory().getCollapseAllButton()
        """
        return "{caption='' container=" + self.CTabItem + " styletype='button scs-navigator-buttons scs-collapse-all-button' visible='true'}"

    def getExpandCollapseArrow(self):
        """
        Usage:
        Directory().getExpandCollapseArrow()
        """
        return self.expandCollapseArrow

    def getComboCheckBoxSearch(self):
        """
        Usage:
        Directory().getComboCheckBoxSearch()
        """
        return self.comboCheckBoxSearch

    def getComboCheckBoxText(self):
        """
        Usage:
        Directory().getComboCheckBoxText()
        """
        rName = "{caption?='*""*' container=" + self.comboCheckBoxFilter + " styletype='cell indexed-cell list-cell' visible='true'}"
        return rName

    def getFilterCheckBox(self, name):
        """
        @param name [string] name of filter check box

        Usage:
        Directory().getFilterCheckBox()
        """
        checkBox = "{caption='" + name + "' container=" + PopupListView().getListView() + " styletype='cell indexed-cell list-cell check-box-list-cell' visible='true'}"
        mark = "{container=" + checkBox + " styletype='mark' visible='true'}"
        return mark

    def getLinkButton(self, name):
        """
        @param name [string] name of button

        Usage:
        Directory().getLinkButton()
        """
        return "{caption='' container=" + Directory().getBoardOrSystem(name) + " styletype='button' visible='true'}"

    def getSaveAll(self):
        """
        Usage:
        Directory().getSaveAll()
        """
        return self.saveAll

    def getScrollBar(self):
        """
        Usage:
        Directory().getScrollBar()
        """
        return self.scrollBar

    def getFileName(self, path):
        """
        @param path [string] path to file

        Usage:
        Directory().getFileName("testing1/Blank.panel")
        """

        list = path.split("/")
        num = len(list)
        name = list[num - 1]

        return "{caption='" + name + "' item.resource.fullpath='" + "/" + path + "' container=" + self.systemDirectoryTree + " styletype='cell indexed-cell tree-cell' visible='true'}"

    def getDirectoryTreeItem(self, name, styletype="text"):
        """
        @param name [string] name of item from directory tree

        Usage:
        Directory().getDirectoryTreeItem(name)
        """
        directoryTreeItem = "{caption='" + name + "' container=" + self.systemDirectoryTree + " styletype='cell indexed-cell tree-cell' visible='true'}"
        directoryTreeItemLabel = "{caption='" + name + "' container=" + directoryTreeItem + "  styletype='text' visible='true'}"
        if styletype == "text":
            return directoryTreeItemLabel
        else:
            return directoryTreeItem

    def getTopToolbarHBox(self):
        """"
        Usage:
        Directory().getTopToolbarHBox()
        """
        return self.topToolbarHBox

    def getFloatableViewImage(self):
        """
        Usage:
        Directory().getFloatableViewImage()
        """
        return self.floatableViewImage

    def getSaveAllImage(self):
        """
        Usage:
        Directory().getSaveAllImage()
        """
        return self.saveAllImage

    def getDirectoryClose(self):
        """
        Usage:
        Directory().getSaveAllImage()
        """
        return self.directoryClose

    def getOverviewPanelTab(self):
        """
        Usage:
        Directory().getOverviewPanelTab()
        """
        return self.overviewPanelTab

    def getCloseOverviewPanelTab(self):
        """
        Usage:
        Directory().getCTabItem()
        """
        return self.closeOverviewPanelTab

    def getTextFieldSearchContextMenu(self):
        """
        Usage:
        Directory().getTextFieldSearchContextMenu()
        """
        return self.textFieldSearchContextMenu

    def getConfigurePerspectiveButton(self):
        """
        Usage:
        Directory().getConfigurePerspectiveButton()
        """
        return self.configurePerspectiveButton

    def getPanelDevPerspectiveButton(self):
        """
        Usage:
        Directory().getPanelDevPerspectiveButton()
        """
        return self.panelDevPerspectiveButton

    def getTreeViewItem(self, name):
        """
        Used for finding objects with consideration to its hierarchy inside Directory.
        Parent of object will be its visual parent from Directory, unlike result of Directory().getDirectoryTreeItem(name).
        @param name [string] Name of object from Directory
        Usage:
        Directory().getTreeViewItem("Gray_System")
        Directory().getTreeViewItem("Overview")
        """
        itemFromTree = "{caption='" + name + "' container=" + self.systemDirectoryTree + " type='com.froglogic.squish.jfx.TreeItemProxy'}"
        return itemFromTree
    
    def getSystemItem(self,name):
        """
        Usage:
        Directory().getSystemItem(name)
        """
        systemItem = "{container={caption='" + name + "' container=" + self.systemDirectoryTree + " styletype='cell indexed-cell tree-cell' visible='true'} styletype='arrow' visible='true'}"
        return systemItem

class OpenProject:
    def __init__(self):
        self.openProjectWindow = "{caption='Open project(s)' isvisible='true' type='org.eclipse.swt.widgets.Shell'}"
        self.projectPathButton = "{caption='' styletype='button scs-browse-button' visible='true' window=" + self.openProjectWindow + "}"
        self.listView = "{styletype='list-view scs-listview-dialog' visible='true' window=" + self.openProjectWindow + "}"
        self.openButton = "{caption='Open' id='dialogButton' styletype='button scs-button' visible='true' window=" + self.openProjectWindow + "}"
        self.openProjectTextField = "{styletype='text-input text-field' visible='true' window=" + self.openProjectWindow + "}"

    def getOpenProjectTextField(self):
        """
        Usage:
        OpenProject().getOpenProjectTextField()
        """
        return self.openProjectTextField

    def getOpenProjectWindow(self):
        """
        Usage:
        OpenProject().getOpenProjectWindow()
        """
        return self.openProjectWindow

    def getProjectPathButton(self):
        """
        Usage:
        OpenProject().getProjectPathButton()
        """
        return self.projectPathButton

    def getProjectNameAndPath(self, nameAndPath):
        """
        @param nameAndPath [string] name of project

        Usage:
        OpenProject().getProjectNameAndPath()
        """
        namePath = "{caption?='" + nameAndPath + " (*" + "' container=" + self.listView + " styletype='cell indexed-cell list-cell check-box-list-cell' visible='true'}"
        return namePath

    def getProjectCheckBox(self, name):
        return "{caption='' container=" + OpenProject().getProjectNameAndPath(name) + " styletype='check-box' visible='true'}"

    def getOpenProjectCheckBox(self, nameAndPath):
        """
        @param nameAndPath [string] name of project

        Usage:
        OpenProject().getOpenProjectCheckBox()
        """
        checkBox = "{caption='' container=" + OpenProject().getProjectNameAndPath(nameAndPath) + " styletype='check-box' visible='true'}"
        mark = "{container=" + checkBox + " styletype='mark' visible='true'}"
        return mark

    def getOpenButton(self):
        """
        Usage:
        OpenProject().getOpenButton()
        """
        return self.openButton

    def getSelectDeselectButton(self, name):
        """
        This method returns the real name of Select All or Deselect All button.
        @param name: name of buton (could be 'Select All' or 'Deselect All')
        usage example:
        OpenProject().getSelectDeselectButton("Select All")
        OpenProject().getSelectDeselectButton("Deselect All")
        """
        return "{caption='" + name + "' id='selectDeselectButton' styletype='button scs-button' visible='true' window=" + self.openProjectWindow + "}"

    def closeOpenProjectDialog(self):
        return "{caption='X' styletype='label scs-closeLabel' visible='true' window=" + self.openProjectWindow + "}"
        # {caption='X' container=':Open project(s).X_label scs-closeLabel' styletype='text' visible='true'}

    def getProgressBar(self):
        """
        This method returns the real name of progress bar.
        usage example:
        OpenProject().getProgressBar()
        """
        barContainer = "{id='openProjectsProgressBar' styletype='progress-bar' visible='true' window=" + self.openProjectWindow + "}"
        return "{container=" + barContainer + " styletype='track' visible='true'}"

    def getStopButton(self):
        """
        This method returns the real name of Stop button.
        usage example:
        OpenProject().getStopButton()
        """
        return "{caption='Stop' styletype='button scs-button' visible='true' window=" + self.openProjectWindow + "}"


class OpenLibraryProject:
    def __init__(self):
        self.mainShell = "{caption='Open library project(s)' isvisible='true' type='org.eclipse.swt.widgets.Shell'}"
        self.projectPathButton = "{caption='' styletype='button scs-browse-button' visible='true' window=" + self.mainShell + "}"
        self.listView = "{styletype='list-view scs-listview-dialog' visible='true' window=" + self.mainShell + "}"
        self.openButton = "{caption='Open' id='dialogButton' styletype='button scs-button' visible='true' window=" + self.mainShell + "}"
        self.openProjectTextField = "{styletype='text-input text-field' visible='true' window=" + self.mainShell + "}"

    def getMainShell(self):
        """
        Usage:
        OpenLibraryProject().getMainShell()
        """
        return self.mainShell

    def getLibraryProjectPathButton(self):
        """
        Usage:
        OpenLibraryProject().getLibraryProjectPathButton()
        """
        return self.projectPathButton

    def getLibraryProjectNameAndPath(self, nameAndPath):
        """
        @param nameAndPath [string] name of project

        Usage:
        OpenProject().getLibraryProjectNameAndPath()
        """
        namePath = "{caption?='" + nameAndPath + " (*" + "' container=" + self.listView + " styletype='cell indexed-cell list-cell check-box-list-cell' visible='true'}"
        return namePath

    def getOpenLibraryProjectCheckBox(self, nameAndPath):
        """
        @param nameAndPath [string] name of project

        Usage:
        OpenProject().getOpenProjectCheckBox()
        """
        checkBox = "{caption='' container=" + OpenLibraryProject().getLibraryProjectNameAndPath(nameAndPath) + " styletype='check-box' visible='true'}"
        mark = "{container=" + checkBox + " styletype='mark' visible='true'}"
        return mark

    def getLibraryProjectCheckBox(self, name):
        return "{caption='' container=" + OpenLibraryProject().getLibraryProjectNameAndPath(name) + " styletype='check-box' visible='true'}"

    def getButton(self, name):
        return "{caption='" + name + "' styletype='button scs-button' visible='true' window=':Open library project(s)_Shell'}"

    def closeOpenLibraryProjectDialog(self):
        return "{caption='X' styletype='label scs-closeLabel' visible='true' window=" + self.mainShell + "}"
        # {caption='X' container=':Open project(s).X_label scs-closeLabel' styletype='text' visible='true'}


class LinkProject:
    """
    Class conteins real names of items from LinkProject window
    """
    def __init__(self):
        self.mainShell = "{caption='Link project with a system' isvisible='true' type='org.eclipse.swt.widgets.Shell'}"
        self.systemComboBox = "{styletype='combo-box-base combo-box' visible='true' window=" + self.mainShell + "}"

    def getMainShell(self):
        """
        Usage:
        LinkProject(name).getMainShell()
        """
        return self.mainShell

    def getComboBox(self):
        """
        Usage:
        LinkProject(name).getComboBox()
        """
        return self.systemComboBox

    def getOkButton(self, name):
        """
        @param name [string] name of button (example OK)

        Usage:
        LinkProject(name).getOkButton("OK")
        """
        return "{caption='" + name + "' id='dialogButton' styletype='button scs-button' visible='true' window=" + self.mainShell + "}"


class AddSystemStage:
    """
    Class contains all real names from Window for adding a system
    """
    def __init__(self):
        self.addSystem = "{caption='Add System' isvisible='true' type='org.eclipse.swt.widgets.Shell'}"
        self.addSysOkButton = "{caption='OK' styletype='button scs-button' visible='true' window=" + self.addSystem + "}"
        self.addSysTextField = "{styletype='text-input text-field' visible='true' window=" + self.addSystem + "}"
        self.addcomboBox = "{id='simulatedSystemCombo' styletype='combo-box-base combo-box' visible='true' window=" + self.addSystem + "}"
        self.addSysLoadButton = "{caption='Load' styletype='button scs-button' visible='true' window=" + self.addSystem + "}"
        self.commStateLabel = "{caption='Communication state: ' container=" + self.addSystem + " styletype='text' visible='true'}"
        self.addSystemBackground = "{styletype='scs-commonDialogBackground scs-dialogRoot' visible='true' window=" + self.addSystem + "}"

    def getAddSystem(self):
        """
        Usage:
        AddSystemStage().getAddSystem()
        """

        return self.addSystem

    def getAddSysOkButton(self):
        """
        Usage:
        AddSystemStage().getAddSysOkButton()
        """
        return self.addSysOkButton

    def getAddSysTextField(self):
        """
        Usage:
        AddSystemStage().getAddSysTextField()
        """
        return self.addSysTextField

    def getAddComboBox(self):
        """
        Usage:
        AddSystemStage().getAddComboBox()
        """
        return self.addcomboBox

    def getAddSysLoadButton(self):
        """
        Usage:
        AddSystemStage().getAddSysLoadButton()
        """
        return self.addSysLoadButton

    def getCommStateLabel(self):
        """
        Usage:
        AddSystemStage().getCommStateLabel()
        """
        return self.commStateLabel

    def getCommStateNameLabel(self, name):
        """
        @param name [string] name of the Communication state (NORMAL/BROKEN)
        Usage:
        AddSystemStage().getCommStateNameLabel(name)
        """
        commState = "{caption='" + name + "' styletype='label' visible='true' window=" + self.addSystem + "}"
        return commState

    def getAddComboBoxItem(self, item):
        """
        @param name [string] add combo box item text
        Usage:
        AddSystemStage().getAddComboBoxItem("CS42L42 Customer Demonstration Board")
        """
        rnSystem = "{caption?='" + "*" + item + "*" + "' container = " + self.addcomboBox + " styletype='text' visible='true'}"
        return rnSystem

    def getAddSystemBackground(self):
        """
        Usage:
        AddSystemStage().getAddSystemBackground()
        """
        return self.addSystemBackground


class History:
    """
    Class contains real names of all items from window for History
    """
    def __init__(self, sysOrDevName=""):
        self.CTabItem = "{caption?='History:*" + sysOrDevName + "*' parent.visible='true' type='org.eclipse.swt.custom.CTabItem' window=" + MainShell().getMainWindow() + "}"
        self.table = "{container=" + self.CTabItem + " id='historyTableView' styletype='table-view scs-history-table' visible='true'}"
        self.newHistoryView = "{caption='New History View' isvisible='true' type='org.eclipse.swt.widgets.Shell'}"
        self.historyButtonBar = "{styletype='button-bar' visible='true' window=" + self.newHistoryView + "}"
        self.historyOkButton = "{caption='OK' styletype='button scs-button' visible='true' window=" + self.newHistoryView + "}"
        self.closeLabel = "{caption='X' styletype='label scs-closeLabel' visible='true' window=" + self.newHistoryView + "}"
        self.historyDropDown = "{styletype='combo-box-base combo-box' visible='true' window=" + self.newHistoryView + "}"
        self.historyClickDD = "{container=" + self.historyDropDown + " id='arrow-button' styletype='arrow-button' visible='true'}"
        self.historySelectList = "{container=" + self.historyDropDown + " id='list-view' styletype='list-view' visible='true'}"
        self.historyClose = "{container=" + self.CTabItem + "  type='com.froglogic.squish.swt.CTabCloseBox'}"
        self.historyToolBar = "{window=" + MainShell().getMainWindow() + " firstItemText='Clear' isvisible='true' type='org.eclipse.swt.widgets.ToolBar'}"
        self.historyImport = "{caption='' container=" + self.CTabItem + " styletype='button scs-import-history-button' visible='true'}"
        self.historyExport = "{caption='' container=" + self.CTabItem + " styletype='button scs-export-history-button' visible='true'}"
        self.historyExportImage = "{container= " + self.historyExport + " styletype='image-view' visible='true'}"
        self.historyClear = "{caption='' container=" + self.CTabItem + " styletype='button scs-clear-history-button' visible='true'}"
        self.historyCTabFolder = "{firstTabCaption='Properties' isvisible='true' type='org.eclipse.swt.custom.CTabFolder' window=" + MainShell().getMainWindow() + "}"
        self.historyCornerToolBar = "{container= " + self.historyCTabFolder + " firstItemText='Minimize' isvisible='true' type='org.eclipse.swt.widgets.ToolBar'}"
        self.maximizeWindow = "{caption='Maximize' container=" + self.historyCornerToolBar + "  type='org.eclipse.swt.widgets.ToolItem'}"
        self.emptyTableLabel = "{caption='No content in table' container= " + self.table + " styletype='label' visible='true'}"
        self.toolbar = "{container=" + self.historyCTabFolder + " firstItemText='Clear' isvisible='true' type='org.eclipse.swt.widgets.ToolBar'}"
        #combo boxes
        self.filterComboCheckBox = "{container=" + self.CTabItem + " type='com.cirrus.scs.ide.ui.javafx.controls.ComboCheckBox' visible='true' everythingchecked='All Operations, Status and Devices'}"
        self.filterDropDown = "{container=" + self.filterComboCheckBox + " styletype='combo-box-base combo-box' visible='true'}"
        self.columnsComboCheckBox = "{container=" + self.CTabItem + " type='com.cirrus.scs.ide.ui.javafx.controls.ComboCheckBox' visible='true' everythingchecked='All History Table Columns'}"
        self.columnsDropDown = "{container=" + self.columnsComboCheckBox + " styletype='combo-box-base combo-box' visible='true'}"
        #search
        self.historySearch = "{container=" + self.CTabItem + " styletype='text-input text-field scs-text-field-search' visible='true'}"
        self.historyTableRowCell = "{container=" + self.table + " styletype='cell indexed-cell table-row-cell' visible='true'}"

    def getHistoryWindow(self):
        """
        Usage:
        History().getHistoryWindow()
        """
        return self.CTabItem

    def getExportButton(self):
        """
        Usage:
        History().getExportButton()
        """
        return self.exportButton

    def getImportButton(self):
        """
        Usage:
        History().getImportButton()
        """
        return self.importButton

    def getCTabItem(self):
        """
        Usage:
        History().getCTabItem()
        """
        return self.CTabItem

    def getTable(self):
        """
        Usage:
        History().getTable()
        """
        return self.table

    def getNewHistoryView(self):
        """
        Usage:
        History().getNewHistoryView()
        """
        return self.newHistoryView

    def getHistoryButtonBar(self):
        """
        Usage:
        History().getHistoryButtonBar()
        """
        return self.historyButtonBar

    def getHistoryOkButton(self):
        """
        Usage:
        History().getHistoryOkButton()
        """
        return self.historyOkButton

    def getHistoryCloseLabel(self):
        """
        Usage:
        History().getHistoryCloseLabel()
        """
        return self.closeLabel

    def getHistoryDropDown(self):
        """
        Usage:
        History().getHistoryDropDown()
        """
        return self.historyDropDown

    def getHistoryClickDD(self):
        """
        Usage:
        History().getHistoryClickDD()
        """
        return self.historyClickDD

    def getHistorySelectList(self):
        """
        Usage:
        History().getHistorySelectList()
        """
        return self.historySelectList

    def getHistoryListItem(self, deviceOrSysName):
        """
        @param deviceOrSysName [string] name of device or system

        Usage:
        History().getHistoryListItem("System_1")
        """
        item = "{caption?='" + "*" + deviceOrSysName + "*" + "' styletype='text' visible='true' container=" + self.newHistoryView + "}"
        return item

    def getHistoryTabName(self, testBoardName):
        '''
        This method checks the name of a History tab
        @param testBoardName [string] name of test board

        Usage:
        History().getHistoryTabName(bordName)
        '''
        historyTab = "{caption?='History:" + "*" + testBoardName + "*" + "' parent.visible='true' type='org.eclipse.swt.custom.CTabItem' window=" + MainShell().getMainWindow() + "}"
        try:
            waitForObject(historyTab)
            test.passes("Window " + testBoardName + " exists")
        except LookupError:
            test.fail("FAIL", testBoardName + " doesn't exist")
        return historyTab

    def getHistoryClose(self):
        """
        Usage:
        History().getHistoryClose()
        """
        return self.historyClose

    def getHistoryImport(self):
        """
        Usage:
        History().getHistoryImport()
        """
        return self.historyImport

    def getHistoryExport(self):
        """
        Usage:
        History().getHistoryExport()
        """
        return self.historyExport

    def getHistoryExportImage(self):
        """
        Usage:
        History().getHistoryExportImage()
        """
        return self.historyExportImage

    def getHistoryClear(self):
        """
        Usage:
        History().getHistoryClear()
        """
        return self.historyClear

    def getHistoryCTabFolder(self):
        """
        Usage:
        History().getHistoryCTabFolder()
        """
        return self.historyCTabFolder

    def getHistoryCornerToolBar(self):
        """
        Usage:
        History().getHistoryCornerToolBar()
        """
        return self.historyCornerToolBar

    def getMaximizeWindow(self):
        """
        Usage:
        History().getMaximizeWindow()
        """
        return self.maximizeWindow

    def getEmptyTableLabel(self):
        """
        Usage:
        History().getEmptyTableLabel()
        """
        return self.emptyTableLabel

    def getHistoryCell(self, row, column):
        """
        @param row [string] index of row
        @param column [string] name of column

        Usage:
        History().getHistoryCell(row, column)
        """
        if column == "Operation":
            cell = "{column='" + column + "' container=" + self.table + " row='" + row + "' styletype='cell indexed-cell table-cell table-column scs-table-view-firstColumn' visible='true'}"
        else:
            cell = "{column='" + column + "' container=" + self.table + " row='" + row + "' styletype='cell indexed-cell table-cell table-column' visible='true'}"
        return cell

    def getFilterDropDown(self):
        """
        Usage:
        History().getFilterDropDown()
        """
        return self.filterDropDown

    def getColumnsComboCheckBox(self):
        """
        Usage:
        History().getColumnsComboCheckBox()
        """
        return self.columnsComboCheckBox

    def getColumnsDropDown(self):
        """
        Usage:
        History().getColumnsDropDown()
        """
        return self.columnsDropDown

    def getCheckBox(self, name):
        """
        @param name [string] name of check box

        Usage:
        History().getCheckBox(name)
        """
        checkBoxList = "{caption='" + name + "' container=" + PopupListView().getListView() + " styletype='cell indexed-cell list-cell check-box-list-cell' visible='true'}"
        checkBox = "{caption='' container=" + checkBoxList + " styletype='check-box' visible='true'}"
        mark = "{container=" + checkBox + " styletype='mark' visible='true'}"
        return mark

    def getHistoryDropDownName(self):
        """
        Usage:
        History().getHistoryDropDownName()
        """
        dropDownName = "{caption?='*""*' container=" + self.filterDropDown + " styletype='cell indexed-cell list-cell' visible='true'}"
        name = ""
        try:
            name = waitForObject(dropDownName).text
            return name
        except LookupError:
            test.fail("FAIL", name + " does not exist")

    def getHistoryColumsDropDownName(self):
        """
        Usage:
        History().getHistoryColumsDropDownName()
        """
        dropDownName = "{caption?='*""*' container=" + self.columnsDropDown + " styletype='cell indexed-cell list-cell' visible='true'}"
        name = ""
        try:
            name = waitForObject(dropDownName).text
            return name
        except LookupError:
            test.fail("FAIL", name + " does not exist")

    def getHistoryRow(self, row):
        """
        @param row [string] index of row

        Usage:
        History().getHistoryRow(row)
        """
        historyRow = "{caption='TableRow" + str(row) + "' container=" + self.table + " type='com.froglogic.squish.jfx.TableRowProxy'}"
        return historyRow

    def getHistorySearch(self):
        """
        Usage:
        History().getHistorySearch()
        """
        return self.historySearch

    def getHistoryTableColumn(self, name):
        """
        @param name [string] name of table column

        Usage:
        History().getHistoryTableColumn(name)
        """
        tableColumn = "{caption='" + name + "' container=" + self.table + " styletype='label' visible='true'}"
        return tableColumn

    def getHistoryTableRowCell(self):
        """
        Usage:
        History().getHistoryTableRowCell()
        """
        return self.historyTableRowCell


class HistoryDialog:
    """
    Class contains all real names of history dialog
    """
    def __init__(self):
        self.historyDialogShell = "{caption='' isvisible='true' type='org.eclipse.swt.widgets.Shell'}"
        self.infoLabel = "{caption='Information' styletype='label scs-DialogTitleLabel' visible='true' window=" + self.historyDialogShell + "}"
        self.OKButton = "{caption='OK' styletype='button scs-button' visible='true' window=" + self.historyDialogShell + "}"

    def getInfoLabel(self):
        """
        Usage:
        HistoryDialog().getInfoLabel()
        """
        return self.infoLabel

    def getOKButton(self):
        """
        Usage:
        HistoryDialog().getOKButton()
        """
        return self.OKButton


class BitControl:
    """
    Class contains all real names of BitControl Window
    """
    def __init__(self):
        self.bitControl = "{caption='Bit Control' parent.visible='true' type='org.eclipse.swt.custom.CTabItem' window=" + MainShell().getMainWindow() + "}"
        self.toggleButton = "{styletype='toggle-button' visible='true' window=" + self.bitControl + "}"
        self.bitControlToggle = "{caption='TOGGLE'  container=" + self.toggleButton + " styletype='text' visible='true'}"
        self.bitControlClose = "{container=" + self.bitControl + " type='com.froglogic.squish.swt.CTabCloseBox'}"

    def getBitControl(self):
        """
        Usage:
        BitControl().getBitControl()
        """
        return self.bitControl

    def getToggleButton(self):
        """
        Usage:
        BitControl().getToggleButton()
        """
        return self.toggleButton

    def getBitControlToggle(self):
        """
        Usage:
        BitControl().getBitControlToggle()
        """
        return self.bitControlToggle

    def getBitControlClose(self):
        """
        Usage:
        BitControl().getBitControlClose()
        """
        return self.bitControlClose


class ErrorMessage:
    """
    Class contains all real names of Error message window
    """
    def __init__(self):
        self.errorStage = "{basetype='javafx.stage.Stage' caption='Error' visible='true'}"
        self.twoSimSysSameName = "{caption='A system already exists with the given name, system names must be unique.' styletype='label content' visible='true' window=" + self.errorStage + "}"
        self.noSysTypeError = "{caption='You must select a system.' styletype='label content' visible='true' window=" + self.errorStage + "}"
        self.noSysNameError = "{caption='You must give the system a name.' styletype='label content' visible='true' window=" + self.errorStage + "}"
        self.emptyXMLError = "{caption?='file is empty*' styletype='label content' visible='true' window=" + self.errorStage + "}"
        self.invalidXMLError = "{caption?='invalid file format:*' styletype='label content' visible='true' window=" + self.errorStage + "}"
        self.errorStageOkButtonBar = "{styletype='button-bar' visible='true' window=" + self.errorStage + "}"
        self.errorStageOkButton = "{caption='OK' container=" + self.errorStageOkButtonBar + " styletype='button' visible='true'}"

    def getErrorStage(self):
        """
        Usage:
        ErrorMessage().getErrorStage()
        """
        return self.errorStage

    def getTwoSimSysSameName(self):
        """
        Usage:
        ErrorMessage().getTwoSimSysSameName()
        """
        return self.twoSimSysSameName

    def getNoSysTypeError(self):
        """
        Usage:
        ErrorMessage().getNoSysTypeError()
        """
        return self.noSysTypeError

    def getNoSysNameError(self):
        """
        Usage:
        ErrorMessage().getNoSysNameError()
        """
        return self.noSysNameError

    def getEmptyXMLError(self):
        """
        Usage:
        ErrorMessage().getEmptyXMLError()
        """
        return self.emptyXMLError

    def getInvalidXMLError(self):
        """
        Usage:
        ErrorMessage().getInvalidXMLError()
        """
        testMachine = platform.system()
        errWin = "{caption?='invalid file format:*' styletype='label content' visible='true' window=" + self.errorStage + "}"
        errMAC = "{caption?='error during deserialisation:*' styletype='label content' visible='true' window=" + self.errorStage + "}"
        if "Windows" in testMachine:
            return errWin
        elif "Linux" in testMachine:
            sys.exit("Linux!")
        elif "Darwin":
            return errMAC
        else:
            sys.exit("OS not found")

    def getErrorStageOkButton(self):
        """
        Usage:
        ErrorMessage().getErrorStageOkButton()
        """
        return self.errorStageOkButton


class RegisterMap:
    """
    Class contains all real names of RegisterMap Window
    """
    def __init__(self, moduleName):
        self.CTabItem = "{caption='" + moduleName + "' parent.visible='true' type='org.eclipse.swt.custom.CTabItem' window=" + MainShell().getMainWindow() + "}"
        self.bitFieldTable = "{container=" + self.CTabItem + " id='bitfieldTable' styletype='table-view' visible='true'}"
        self.registerTable = "{container=" + self.CTabItem + " id='registerTable' styletype='table-view' visible='true'}"
        self.pageComboBox = "{container=" + self.CTabItem + " id='pageSelectComboBox' styletype='combo-box-widget' visible='true'}"
        self.pagelistView = "{container=" + self.pageComboBox + " id='list-view' styletype='list-view' visible='true'}"
        self.pageDropDown = "{container=" + self.pageComboBox + " id='arrow-button' styletype='arrow-button' visible='true'}"
        self.formatComboBox = "{container=" + self.CTabItem + " id='formatComboBox' styletype='combo-box-widget' visible='true'}"
        self.formatDropDown = "{container=" + self.formatComboBox + " id='arrow-button' styletype='arrow-button' visible='true'}"
        self.popupCtrl = "{type='javafx.stage.Popup' visible='true'}"
        self.comboBoxListView = "{container=" + self.popupCtrl + " id='list-view' styletype='list-view' visible='true'}"
        self.comboBoxWidget = "{container=" + self.CTabItem + " id='pageSelectComboBox' styletype='combo-box-widget' visible='true'}"
        self.comboBoxLabel = "{caption?='*' container=" + self.comboBoxWidget + " styletype='label label-name' visible='true'}"
        self.CTabCloseBox = "{container=" + self.CTabItem + " type='com.froglogic.squish.swt.CTabCloseBox'}"
        self.refreshPage = "{caption='' container=" + self.CTabItem + " id='refreshPage' styletype='button scs-refresh-button' visible='true'}"
        self.refreshRegister = "{caption='' container=" + self.CTabItem + " id='refreshRegister' styletype='button scs-refresh-button' visible='true'}"
        self.search = "{container=" + self.CTabItem + " id='searchRegistersTextField' styletype='text-input text-field scs-text-field-filter' visible='true'}"
        self.scrollPane = "{container=" + self.CTabItem + " id='repmapScrollPane' styletype='scroll-pane' visible='true'}"
        self.bitfieldTableValueColumn = "{container=" + self.bitFieldTable + " styletype='vbox-regmap' visible='true'}"

    def getCTabItem(self):
        """
        Usage:
        RegisterMap(moduleName).getCTabItem()
        """
        return self.CTabItem

    def getRegisterCellArea(self, column, row, container):
        """
        @param column [string] name of column
        @param row [string] index of row
        @param container [string] name of container that contains cell

        Usage:
        RegisterMap(moduleName).getRegisterCellArea()
        """
        RegisterCellArea = "{column='" + column + "' container=" + container + " id='registerTableValueColumn' row='" + row + "' styletype='cell indexed-cell table-cell table-column table-view-lastColumn' visible='true'}"
        return RegisterCellArea

    def getCTabCloseBox(self):
        """
        Usage:
        RegisterMap(moduleName).getCTabCloseBox()
        """
        return self.CTabCloseBox

    def getRegisterTable(self):
        """
        Usage:
        RegisterMap(moduleName).getRegisterTable()
        """
        return self.registerTable

    def getRegisterTableRow(self, currentRow):
        """
        @param currentRow [string] index of row

        Usage:
        RegisterMap(moduleName).getRegisterTableRow()
        """
        row = "{caption='TableRow" + currentRow + "' container=" + self.registerTable + " type='com.froglogic.squish.jfx.TableRowProxy'}"
        return row

    def getRegisterFromRegTable(self, name):
        """
        @param name [string] name of registar from table

        Usage:
        RegisterMap(moduleName).getRegisterFromRegTable(name)
        """
        registerFromRegTable = "{caption='" + name + "' container=" + self.registerTable + " type='com.froglogic.squish.jfx.TableCellProxy'}"
        return registerFromRegTable

    def getRegisterFromBitFieldTable(self, name):
        """
        @param name [string] name of registar bit field table

        Usage:
        RegisterMap(moduleName).getRegisterFromBitFieldTable(name)
        """
        registerFromBitFieldTable = "{caption='" + name + "' container=" + self.bitFieldTable + " type='com.froglogic.squish.jfx.TableCellProxy'}"
        return registerFromBitFieldTable

    def getBitFieldTable(self):
        """
        Usage:
        RegisterMap(moduleName).getBitFieldTable()
        """
        return self.bitFieldTable

    def getPopUpCtrl(self):
        """
        Usage:
        RegisterMap(moduleName).getPopUpCtrl()
        """
        return self.popUpCtrl

    def getComboBoxItem(self, name):
        """
        @param name [string] name of combo box item

        Usage:
        RegisterMap().getComboBoxItem("0x01")
        RegisterMap().getComboBoxItem("dec")
        """
        comboBoxItem = "{caption='" + name + "' container=" + self.popupCtrl + " styletype='label label-name' visible='true'}"
        return comboBoxItem

    def getComboListMember(self, itemName):
        """
        @param itemName [string] name of item from combo list

        Usage:
        RegisterMap(moduleName).getComboListMember(name)
        """
        comboListMemberCell = "{caption?='" + "*" + itemName + "*" + "' container=" + self.comboBoxListView + " styletype='cell indexed-cell list-cell' visible='true'}"
        comboListMember = "{caption?='" + "*" + itemName + "*" + "' container=" + comboListMemberCell + " styletype='text' visible='true'}"
        return comboListMember

    def getPageComboBox(self):
        """
        Usage:
        RegisterMap(moduleName).getPageComboBox()
        """
        return self.pageComboBox

    def getPagelistView(self):
        """
        Usage:
        RegisterMap(moduleName).getPagelistView()
        """
        return self.pagelistView

    def getComboBoxWidget(self):
        """
        Usage:
        RegisterMap(moduleName).getComboBoxWidget()
        """
        return self.comboBoxWidget

    def getComboBoxLabel(self):
        """
        Usage:
        RegisterMap(moduleName).getComboBoxLabel()
        """
        return self.comboBoxLabel

    def getPageDropDown(self):
        """
        Usage:
        RegisterMap(moduleName).getPageDropDown()
        """
        return self.pageDropDown

    def getRegisters(self, pageNumber):
        """
        @param pageNumber [string] page number

        Usage:
        RegisterMap(moduleName).getRegisters(number)
        """
        registers = "{caption='" + pageNumber + "' container=" + self.pageComboBox + " styletype='cell indexed-cell list-cell' visible='true'}"
        return registers

    def getFormatComboBox(self):
        """
        Usage:
        RegisterMap(moduleName).getFormatComboBox()
        """
        return self.formatComboBox

    def getFormatDropDown(self):
        """
        Usage:
        RegisterMap(moduleName).getFormatDropDown()
        """
        return self.formatDropDown

    def getPageLabel(self, value):
        """
        @param value [string] value of page label

        Usage:
        RegisterMap(moduleName).getPageLabel()
        """
        pageLabel = "{caption='Page " + value + ": Page " + value + "' container=" + self.CTabItem + " id='pageName' styletype='label' visible='true'}"
        return str(findObject(pageLabel).text)

    def getRegisterMapLabel(self):
        """
        Usage:
        RegisterMap(moduleName).getRegisterMapLabel()
        """
        return self.registerMapLabel

    def getRefreshPage(self):
        """
        Usage:
        RegisterMap(moduleName).getRefreshPage()
        """
        return self.refreshPage

    def getRefreshRegister(self):
        """
        Usage:
        RegisterMap(moduleName).getRefreshRegister()
        """
        return self.refreshRegister

    def getSearch(self):
        """
        Usage:
        RegisterMap(moduleName).getSearch()
        """
        return self.search

    def getSortLabel(self, name):
        """
        Usage:
        RegisterMapObj.getSortLabel("Name")
        RegisterMapObj.getSortLabel("Page")
        RegisterMapObj.getSortLabel("Address")
        """
        labelContainer = "{caption='" + name + "' container=" + self.registerTable + " styletype='label' visible='true'}"
        return "{caption='" + name + "' container=" + labelContainer + " styletype='text' visible='true'}"

    def getBitFieldSortLabel(self, name):
        """
        Usage:
        RegisterMapObj.getSortLabel("Name")
        RegisterMapObj.getSortLabel("Page")
        RegisterMapObj.getSortLabel("Address")
        """
        labelContainer = "{caption='" + name + "' container=" + self.bitFieldTable + " styletype='label' visible='true'}"
        return "{caption='" + name + "' container=" + labelContainer + " styletype='text' visible='true'}"

    def getScrollPane(self):
        """
        Usage:
        RegisterMapObj.getScrollPane()
        """
        return self.scrollPane

    def getRadioButton(self, regmapObj, registerName, bitFieldName, radioButtonCaption):
        """
        @param regmapObj [object] RegisterMap class object
        @param registerName [string] name of register
        @param bitFieldName [string] name of bit field
        @param radioButtonCaption [string] name of the radio button
        @returns radioButtonDot real name
        Usage:
        RegisterMapObj = RegisterMap("cs42l42 (CS42L42)")
        RegisterMapObj.getRadioButton(RegisterMapObj, "Freeze Control", "FREEZE", "Volume-control and power-down register changes take effect immediately")
        """
        InputActions.mouseClickOnItem(regmapObj.getRegisterFromRegTable(registerName))
        row = str(findObject(regmapObj.getRegisterFromBitFieldTable(bitFieldName)).cell.parent.index)
        bitFieldTableCell = "{column='Value' container=" + self.bitFieldTable + " id='bitfieldTableValueColumn' row='" + row + "' styletype='cell indexed-cell table-cell table-column scs-table-view-lastColumn' visible='true'}"
        radioButton = "{caption='" + radioButtonCaption + "' container=" + bitFieldTableCell + " styletype='radio-button' visible='true'}"
        radioButtonDot = "{container=" + radioButton + " styletype='dot' visible='true'}"
        return radioButtonDot

    def getBitfieldCellArea(self, column, row):
        """
        @param column [string] name of column
        @param row [string] index of row
        @param container [string] name of container that contains cell

        Usage:
        RegisterMapObj.getBitfieldCellArea("Value", "0")
        """
        BitFieldCellArea = "{column='" + column + "' container=" + self.bitFieldTable + " id='bitfieldTableValueColumn' row='" + row + "' styletype='cell indexed-cell table-cell table-column scs-table-view-lastColumn' visible='true'}"
        return BitFieldCellArea

    def getSlider(self, container):
        """
        Usage:
        RegisterMapObj.getSlider(RegisterMapObj.getBitfieldCellArea("Value", "0"))
        """
        slider = "{container=" + container + " styletype='slider slider-min-value' visible='true'}"
        return "{container=" + slider + " styletype='thumb' visible='true'}"

    def getBitfieldTableValueColumn(self):
        """
        Usage:
        RegisterMap(moduleName).getBitfieldTableValueColumn()
        """
        return self.bitfieldTableValueColumn


class ErrorLog:
    """
    Class contains all real names from error log Window
    """
    def __init__(self):
        self.errorLogTab = "{caption='Error Log View' parent.visible='true' type='org.eclipse.swt.custom.CTabItem' window=" + MainShell().getMainWindow() + "}"
        self.errorLogTree = "{container=" + self.errorLogTab + " isvisible='true' type='org.eclipse.swt.widgets.Tree'}"
        self.errorLogViewTab = "{caption='Error Log View' parent.visible='true' type='org.eclipse.swt.custom.CTabItem' window=" + MainShell().getMainWindow() + "}"
        self.errorLogViewTree = "{container=" + self.errorLogViewTab + " styletype='root tree-table-view' visible='true'}"
        self.errorLogViewCell = "{container=" + self.errorLogViewTree + " styletype='cell indexed-cell tree-table-row-cell' visible='true'}"
        self.errorLogViewMessage = "{caption?='*' container=" + self.errorLogViewCell + " styletype='cell indexed-cell tree-table-cell table-column' visible='true'}"
        self.errorLogTableView = "{container=" + self.errorLogTab + " id='logTableView' styletype='root tree-table-view' visible='true'}"
        self.CTabFolder = "{firstTabCaption='Error Log View' isvisible='true' type='org.eclipse.swt.custom.CTabFolder' window=" + MainShell().getMainWindow() + "}"
        self.toolBarMinimize = "{container=" + self.CTabFolder + " firstItemText='Minimize' isvisible='true' type='org.eclipse.swt.widgets.ToolBar'}"
        self.SCSToolBar = "{firstItemText='&Restore' isvisible='true' type='org.eclipse.swt.widgets.ToolBar' window=" + MainShell().getMainWindow() + "}"
        self.toolBarRestore = "{container=" + self.CTabFolder + " firstItemText='Restore' isvisible='true' type='org.eclipse.swt.widgets.ToolBar'}"
        self.restoreToolItem = "{caption='Restore' container=" + self.toolBarRestore + " type='org.eclipse.swt.widgets.ToolItem'}"
        self.toolItem = "{caption='Error Log View' container=" + self.SCSToolBar + " type='org.eclipse.swt.widgets.ToolItem'}"

    def getErrorLogTab(self):
        """
        Usage:
        ErrorLog().getErrorLogTab()
        """
        return self.errorLogTab

    def getErrorLogTree(self):
        """
        Usage:
        ErrorLog().getErrorLogTree()
        """
        return self.errorLogTree

    def getErrorLogViewTab(self):
        """
        Usage:
        ErrorLog().getErrorLogViewTab()
        """
        return self.errorLogViewTab

    def getErrorLogViewTree(self):
        """
        Usage:
        ErrorLog().getErrorLogViewTree()
        """
        return self.errorLogViewTree

    def getErrorLogViewCell(self):
        """
        Usage:
        ErrorLog().getErrorLogViewCell()
        """
        return self.errorLogViewCell

    def getErrorLogViewMessage(self):
        """
        Usage:
        ErrorLog().getErrorLogViewMessage()
        """
        return self.errorLogViewMessage

    def getErrorLogViewColumnText(self, text):
        """
        @param text [string] text from message column

        Usage:
        ErrorLog().getErrorLogViewColumnText("Project build has encountered an error")
        """
        self.columnText = "{caption?='" + "*" + text + "*" + "' container=" + self.errorLogTableView + " styletype='cell indexed-cell tree-table-cell table-column' visible='true'}"
        return self.columnText

    def getMinimizeOrMaximize(self, type):
        """
        Usage:
        ErrorLog().getMinimize("Minimize")
        ErrorLog().getMinimize("Maximize")
        ErrorLog().getMinimize("Restore")
        """
        self.minimizeOrMaximize = "{caption='" + type + "' container=" + self.toolBarMinimize + " type='org.eclipse.swt.widgets.ToolItem'}"
        return self.minimizeOrMaximize

    def getCTabFolder(self):
        """
        Usage:
        ErrorLog().getErrorLogViewMessage()
        """
        return self.CTabFolder

    def getToolItem(self):
        """
        Usage:
        ErrorLog().getErrorLogViewMessage()
        """
        return self.toolItem

    def getRestoreToolItem(self):
        """
        Usage:
        ErrorLog().getErrorLogViewMessage()
        """
        return self.restoreToolItem

    def getErrorLogTableView(self):
        """
        Usage:
        ErrorLog().getErrorLogTableView()
        """
        return self.errorLogTableView


class Preferences:
    """
    Class contains all real names from Preferences window
    """
    def __init__(self):
        self.preferencesShell = "{caption='Preferences' isvisible='true' type='org.eclipse.swt.widgets.Shell'}"
        self.preferencesTree = "{styletype='tree-view' visible='true' window=" + self.preferencesShell + "}"
        self.preferencesTreeItems = "{caption='' container=" + self.preferencesTree + " type='com.froglogic.squish.jfx.TreeItemProxy'}"
        self.themeComboBox = "{styletype='combo-box-base combo-box' visible='true' window=" + self.preferencesShell + "}"
        self.preferencesTextBoxLabel = "{caption='Number of Rolling Log Files' isvisible='true' type='org.eclipse.swt.widgets.Label' window=" + self.preferencesShell + "}"
        self.preferencesTextBox = "{isvisible='true' leftWidget=" + self.preferencesTextBoxLabel + " type='org.eclipse.swt.widgets.Text' window=" + self.preferencesShell + "}"
        self.preferencesDebugLogging = "{caption='Log Debug Events' isvisible='true' type='org.eclipse.swt.widgets.Button' window=" + self.preferencesShell + "}"
        self.historyTextBox = "{styletype='text-input text-field scs-preferences-text-field' visible='true' window=" + self.preferencesShell + "}"
        self.historyPane = "{container=" + self.historyTextBox + " type='javafx.scene.layout.Pane' visible='true'}"
        self.filterSystemsComboBoxSearch = "{styletype='scs-combo-box-search' visible='true' window=" + self.preferencesShell + "}"
        self.filterSystemsComboBox = "{container=" + self.filterSystemsComboBoxSearch + " styletype='combo-box-base combo-box' visible='true'}"
        self.filterSystemsComboBoxText = "{caption?='*""*' container=" + self.filterSystemsComboBox + " styletype='cell indexed-cell list-cell' visible='true'}"
        self.loggingDebugLevelComboBox = "{styletype='combo-box-base combo-box' visible='true' window=" + self.preferencesShell + "}"
        self.loggingDebugLevelComboBoxText = "{caption='Info' container=" + self.loggingDebugLevelComboBox + " styletype='cell indexed-cell list-cell' visible='true'}"
        self.loggingLogToFileCheckBox = "{caption='Log to file' styletype='check-box' visible='true' window=" + self.preferencesShell + "}"
        self.maximumLogFileSizeLabel = "{caption='Maximum log file size in MB ' id='down-padding' styletype='label' visible='true' window=" + self.preferencesShell + "}"
        self.textFiltar = "{styletype='text-input text-field scs-text-field-filter' visible='true' window=" + self.preferencesShell + "}"
        self.closePreferences = "{caption='X' styletype='label scs-closeLabel' visible='true' window=" + self.preferencesShell + "}"

    def getPreferencesShell(self):
        """
        Usage:
        Preferences().getPreferencesShell()
        """
        return self.preferencesShell

    def getPreferencesTree(self):
        """
        Usage:
        Preferences().getPreferencesTree()
        """
        return self.preferencesTree

    def getTreeItem(self, name):
        """
        @param name [string] name of tree item

        Usage:
        Preferences().getTreeItem(name)
        """
        item = "{caption='" + name + "' container=" + self.preferencesTree + " styletype='cell indexed-cell tree-cell' visible='true'}"
        return item

    def getThemeComboBox(self):
        """
        Usage:
        Preferences().getThemeComboBox()
        """
        return self.themeComboBox

    def getThemeItem(self, name):
        """
        @param name [string] name of them

        Usage:
        Preferences().getThemeItem(name)
        """
        themeItem = "{caption='" + name + "' container=" + self.themeComboBox + " styletype='cell indexed-cell list-cell' visible='true'}"
        return themeItem

    def getTextBox(self):
        """
        Usage:
        Preferences().getTextBox()
        """
        return self.preferencesTextBox

    def getButton(self, name):
        """
        @param name [string] name of the button

        Usage:
        Preferences().getButton(name)
        """
        if name == "Cancel":
            preferencesButton = "{caption='Cancel' id='dialogButton' styletype='button scs-button' visible='true' window=" + self.preferencesShell + "}"
        else:
            preferencesButton = "{caption='" + name + "' id='dialogButton' styletype='button scs-button' visible='true' window=" + self.preferencesShell + "}"
        return preferencesButton

    def getDebugLogging(self):
        """
        Usage:
        Preferences().getDebugLogging()
        """
        return self.preferencesDebugLogging

    def getHistoryPane(self):
        """
        Usage:
        Preferences().getHistoryPane()
        """
        return self.historyPane

    def getFilterSystemsComboBoxSearch(self):
        """
        Usage:
        Preferences().getFilterSystemsComboBoxSearch()
        """
        return self.filterSystemsComboBoxSearch

    def getFilterSystemsComboBoxText(self):
        """
        Usage:
        Preferences().getFilterSystemsComboBoxText()
        """
        return self.filterSystemsComboBoxText

    def getGeneralCheckBox(self, name):
        """
        @param name [string] name of general check box

        Usage:
        Preferences().getGeneralCheckBox(name)
        """
        checkBox = "{caption='" + name + "' styletype='check-box' visible='true' window=" + self.preferencesShell + "}"
        return checkBox

    def getLabel(self, tab):
        """
        @param tab [string] name of label in current tab
        Usage:
        Preferences().getLabel("Appearance")
        """
        appearanceLabel = "{caption='" + tab + "' container=" + self.preferencesTree + " styletype='cell indexed-cell tree-cell' visible='true'}"
        return appearanceLabel

    def getLoggingDebugLevelComboBoxText(self):
        """
        Usage:
        Preferences().getLoggingDebugLevelComboBoxText()
        """
        return self.loggingDebugLevelComboBoxText

    def getLoggingLogToFileCheckBox(self):
        """
        Usage:
        Preferences().getLoggingLogToFileCheckBox()
        """
        return self.loggingLogToFileCheckBox

    def getMaximumLogFileSizeLabel(self):
        """
        Usage:
        Preferences().getMaximumLogFileSizeLabel()
        """
        label = "{caption='Maximum log file size in MB ' container=" + self.maximumLogFileSizeLabel + " styletype='text' visible='true'}"
        return label

    def getCheckBox(self, name):
        """
        Usage:
        Preferences().getCheckBox("Log to file")
        """
        return "{container=" + Preferences().getGeneralCheckBox(name) + " styletype='mark' visible='true'}"

    def getTextFiltar(self):
        """
        Usage:
        Preferences().getTextFiltar()
        """
        return self.textFiltar

    def getPreferencesTreeItems(self):
        """
        Usage:
        Preferences().getPreferencesTreeItems()
        """
        return self.preferencesTreeItems

    def getClosePreferences(self):
        """
        Usage:
        Preferences().getClosePreferences()
        """
        return self.closePreferences

    def getPrefTextField(self):
        """
        Usage:
        Preferences().getPrefTextField()
        """
        return self.historyTextBox


class NewDeviceProjectShell:
    """
    Class conteins all real names from Device Panel Project Window
    """
    def __init__(self):
        self.newDeviceProjectShell = "{caption='New device project' isvisible='true' type='org.eclipse.swt.widgets.Shell'}"
        self.availableSystemsListView = "{id='listViewAvailableSystems' styletype='list-view scs-listview-dialog' visible='true' window= " + self.newDeviceProjectShell + "}"
        self.virtualSystemsListView = "{id='listViewVirtualSystems' styletype='list-view scs-listview-dialog' visible='true' window= " + self.newDeviceProjectShell + "}"
        self.devicesListView = "{id='listViewDevices' styletype='list-view scs-listview-dialog' visible='true' window= " + self.newDeviceProjectShell + "}"
        self.templatesTreeView = "{id='treeViewTemplates' styletype='tree-view scs-tree-view-dialog scs-border-nobottom' visible='true' window= " + self.newDeviceProjectShell + "}"
        self.projectNameTextBox = "{id='txtNewProjectName' styletype='text-input text-field scs-white-borded' visible='true' window= " + self.newDeviceProjectShell + "}"
        self.projectLocationTextBox = "{id='txtDirectory' styletype='text-input text-field scs-white-borded' visible='true' window= " + self.newDeviceProjectShell + "}"

    def getNewDeviceShell(self):
        """
        Usage:
        NewDeviceProjectShell().getNewDeviceShell()
        """
        return self.newDeviceProjectShell

    def getVirtualSystem(self, name):
        """
        @param name [string] name of virtual system

        Usage:
        NewDeviceProjectShell().getVirtualSystem("System1")
        """
        virtualSystem = "{caption='" + name + "' container=" + self.virtualSystemsListView + " styletype='label' visible='true'}"
        return virtualSystem

    def getButton(self, name):
        """
        @param name [string] name of the button

        Usage:
        NewDeviceProjectShell().getButton()
        """
        button = "{caption='" + name + "' styletype='button scs-button' visible='true' window=" + self.newDeviceProjectShell + "}"
        return button

    def getTemplatesTreeView(self):
        """
        Usage:
        NewDeviceProjectShell().getTemplatesTreeView()
        """
        return self.templatesTreeView

    def getTemplate(self, name):
        """
        @param name [string] name of template
        Usage:
        NewDeviceProjectShell().getTemplate(template)

        """
        template = "{caption='" + name + "' container=" + self.templatesTreeView + " styletype='cell indexed-cell tree-cell' visible='true'}"
        return template

    def getDevice(self, name):
        """
        @param name [string] name od device

        Usage:
        NewDeviceProjectShell().getDevice(name)
        """
        device = "{caption='" + name + "' container=" + self.devicesListView + " styletype='cell indexed-cell list-cell' visible='true'}"
        return device

    def getProjectNameTextBox(self):
        """
        Usage:
        NewDeviceProjectShell().getProjectNameTextBox()
        """
        return self.projectNameTextBox

    def getProjectLocationTextBox(self):
        """
        Usage:
        NewDeviceProjectShell().getProjectLocationTextBox()
        """
        return self.projectLocationTextBox

    def getAvailableSystem(self, name):
        """
        @param name [string] name of available ststem

        Usage:
        NewDeviceProjectShell().getAvailableSystem("system1")
        """
        availableSystem = "{caption?='*" + name + "*' container=" + self.availableSystemsListView + " styletype='label' visible='true'}"
        return availableSystem

    def getVirtualSystemsListView(self):
        """
        Usage:
        NewDeviceProjectShell().getVirtualSystemsListView()
        """
        return self.virtualSystemsListView

    def getAvailableSystemCheckBox(self, name):
        """
        This method returns the real name of the check-box object from NewDeviceProjectShell().
        @param name: Local   - returns the name of Local check-box
                     Network - returns the name of Network check-box

        Usage:
        NewDeviceProjectShell().getAvailableSystemCheckBox(name)
        """
        if name is "Local":
            return "{caption='" + name + "' id='localCheckBox' styletype='check-box' visible='true' window=" + self.newDeviceProjectShell + "}"
        else:
            return "{caption='" + name + "' id='networkCheckBox' styletype='check-box' visible='true' window=" + self.newDeviceProjectShell + "}"

    def getCloseDialogBox(self):
        """
        This method retruns the real name of X mark to close the NEW DEVICE PROJECT dialog.
        Usage:
        NewDeviceProjectShell().getCloseDialogBox()
        """
        closeContainer = "{caption='X' styletype='label scs-closeLabel' visible='true' window=" + self.newDeviceProjectShell + "}"
        return "{caption='X' container=" + closeContainer + " styletype='text' visible='true'}"


class NewSystemProjectShell:
    """
    Class contains all real names of System Panel Project Window
    """
    def __init__(self):
        self.newSystemProjectShell = "{caption='New system project' isvisible='true' type='org.eclipse.swt.widgets.Shell'}"
        self.availableSystemsListView = "{id='listViewAvailableSystems' styletype='list-view scs-listview-dialog' visible='true' window= " + self.newSystemProjectShell + "}"
        self.virtualSystemsListView = "{id='listViewVirtualSystems' styletype='list-view scs-listview-dialog' visible='true' window= " + self.newSystemProjectShell + "}"
        self.devicesListView = "{id='listViewDevices' styletype='list-view scs-listview-dialog scs-non-selectable-list-view-dialog' visible='true' window= " + self.newSystemProjectShell + "}"
        self.projectNameTextBox = "{id='txtNewProjectName' styletype='text-input text-field scs-white-borded' visible='true' window= " + self.newSystemProjectShell + "}"
        self.closeNewSystemProjectWindow = "{caption='X' styletype='label scs-closeLabel' visible='true' window='" + self.newSystemProjectShell + "'}"

    def getNewSystemShell(self):
        """
        Usage:
        NewSystemProjectShell().getNewSystemShell()
        """
        return self.newSystemProjectShell

    def getVirtualSystem(self, name):
        """
        @param name [string] name of system

        Usage:
        NewSystemProjectShell().getVirtualSystem("system1")
        """
        virtualSystem = "{caption='" + name + "' container=" + self.virtualSystemsListView + " styletype='label' visible='true'}"
        return virtualSystem

    def getButton(self, name):
        """
        @param name [string] name of button

        Usage:
        NewSystemProjectShell().getButton("OK")
        """
        button = "{caption='" + name + "' styletype='button scs-button' visible='true' window=" + self.newSystemProjectShell + "}"
        return button

    def getDevice(self, name):
        """
        @param name [string] name of device

        Usage:
        NewSystemProjectShell().getDevice(name)
        """
        device = "{caption='" + name + "' container=" + self.devicesListView + " styletype='cell indexed-cell list-cell' visible='true'}"
        return device

    def getProjectNameTextBox(self):
        """
        Usage:
        NewSystemProjectShell().getProjectNameTextBox()
        """
        return self.projectNameTextBox

    def getAvailableSystem(self, name):
        """
        @param name [string] name of system

        Usage:
        NewSystemProjectShell().getAvailableSystem("system1")
        """
        availableSystem = "{caption='" + name + "' container=" + self.availableSystemsListView + " styletype='label' visible='true'}"
        return availableSystem

    def getCloseNewSystemProjectWindow(self):
        """
        Usage:
        NewSystemProjectShell().getCloseNewSystemProjectWindow()
        """
        closeButton = "{caption='X' styletype='label scs-closeLabel' visible='true' window=" + self.newSystemProjectShell + "}"
        return closeButton


class NewLibraryProjectShell:
    """
    Class contains all real names for New Library Project shell.
    """
    def __init__(self):
        self.mainShell = "{caption='New library project' isvisible='true' type='org.eclipse.swt.widgets.Shell'}"

    def getMainShell(self):
        return self.mainShell

    def getProjectNameTextPane(self):
        """
        Usage:
        NewLibraryProjectShell().getProjectNameTextPane()
        """
        container = "{id='txtNewProjectName' styletype='text-input text-field scs-white-borded' visible='true' window=" + self.mainShell + "}"
        return "{container=" + container + " type='javafx.scene.layout.Pane' visible='true'}"

    def getDirectoryTextPane(self):
        """
        Usage:
        NewLibraryProjectShell().getDirectoryTextPane()
        """
        container = "{id='txtDirectory' styletype='text-input text-field scs-white-borded' visible='true' window=" + self.mainShell + "}"
        return "{container=" + container + " type='javafx.scene.layout.Pane' visible='true'}"

    def getWarningLabel(self):
        """
        This is getter for real name of the warning label from New Library Project Shell.

        Usage:
        NewLibraryProjectShell().getWarningLabel()
        """
        container = "{basetype='javafx.scene.layout.StackPane' occurrence='1' visible='true' window=" + self.mainShell + "}"
        try:
            text = str(waitForObject(container).children)
        except:
            test.fail("FAIL", "Can't find object '" + container + "'.")

        warningText = re.split("'", text)
        return "{caption='" + warningText[1] + "' styletype='scs-error-label' visible='true' window=" + self.mainShell + "}"

    def getCloseShell(self):
        """
        Usage:
        NewLibraryProjectShell().getCloseShell()
        """
        return "{caption='X' styletype='label scs-closeLabel' visible='true' window=" + self.mainShell + "}"

    def getButton(self, name):
        """
        Usage:
        NewLibraryProjectShell().getButton("Done")
        """
        return "{caption='" + name + "' id='dialogButton' styletype='button scs-button' visible='true' window=" + self.mainShell + "}"


class ConfirmationShell:
    """
    Class contains all real names from confirmation shell
    """
    def __init__(self):
        self.mainShell = "{caption='' isvisible='true' type='org.eclipse.swt.widgets.Shell'}"
        self.checkbox = "{caption='Delete project contents on disk (cannot be undone)' styletype='check-box check-box' visible='true' window=" + self.mainShell + "}"

    def getMainShell(self):
        """
        Usage:
        ConfirmationShell().getMainShell()
        """
        return self.mainShell

    def getCheckbox(self):
        """
        Usage:
        ConfirmationShell().getCheckbox()
        """
        return self.checkbox

    def getButton(self, buttonName):
        """
        @param buttonName [string] name of button

        Usage:
        ConfirmationShell().getButton("OK")
        """
        return "{caption='" + buttonName + "' styletype='button scs-button' visible='true' window=" + self.mainShell + "}"


class AddPanelShell:
    """
    Class contains all real names from add panel shell
    """
    def __init__(self):
        self.addPanelShell = "{caption='New Panel' isvisible='true' type='org.eclipse.swt.widgets.Shell'}"
        self.testFieldName = "{styletype='text-input text-field' visible='true' window=" + self.addPanelShell + "}"
        # {container=':Add panel..._text-input text-field' type='javafx.scene.layout.Pane' visible='true'}
        self.comboBoxTemp = "{id='newPanelComboBox' styletype='combo-box-base combo-box' visible='true' window=" + self.addPanelShell + "}"

    def getPanelShell(self):
        """
        Usage:
        AddPanelShell().getPanelShell()
        """
        return self.addPanelShell

    def getTestFieldName(self):
        """
        Usage:
        AddPanelShell().getTestFieldName()
        """
        return self.testFieldName

    def getcomboBoxTemp(self):
        """
        Usage:
        AddPanelShell().getcomboBoxTemp()
        """
        return self.comboBoxTemp

    def getOkButton(self, buttonName):
        """
        @param buttonName [string] name of the button

        Usage:
        AddPanelShell().getOkButton("OK")
        """
        rnButton = "{caption?='" + "*" + buttonName + "*" + "' id='dialogButton' styletype='button scs-button' visible='true' window=" + self.addPanelShell + "}"
        return rnButton

    def getProjectName(self, name):
        """
        This getter returns the real name of the Project cell in Add New Panel shell.
        @param name [string] name of the project

        Usage:
        AddPanelShell().getProjectName("project1")
        """
        treeViewDialog = "{styletype='tree-view scs-tree-view-dialog' visible='true' window=" + self.addPanelShell + "}"
        return "{caption='" + name + "' container=" + treeViewDialog + " styletype='cell indexed-cell tree-cell' visible='true'}"

    def getProjectPath(self, path, panelName):
        """
        This getter returns the real name of Path label inside Add New Panel shell.
        @param path [string] path of the project
        @param panelName [string] name of panel

        Usage:
        panel = "panel"
        projectPath = SuiteGlobals.getSCSProjectPath(project1)
        AddPanelShell().getProjectPath(projectPath, panel)
        """
        if "Windows" in SuiteGlobals.testMachine:
            caption = "Path: "
            list = path.split("\\")
        elif "Darwin" in SuiteGlobals.testMachine:
            caption = "Path: /"
            list = path.split("/")
        else:
            test.fail("FAIL", "OS not found")

        for item in list:
            caption = caption + item + os.sep + os.sep
        caption = caption + panelName + ".panel"
        return "{caption='" + caption + "' styletype='label scs-commonDialogBackground' visible='true' window=" + self.addPanelShell + "}"


class AddReferencedPanelShell:
    """
    """
    def __init__(self):
        self.mainShell = "{caption='Add new referenced library panel' isvisible='true' type='org.eclipse.swt.widgets.Shell'}"
        self.popupControl = "{basetype='javafx.scene.control.PopupControl' visible='true'}"
        self.listView = "{styletype='list-view scs-listview-dialog' visible='true' window=" + self.mainShell + "}"

    def getLibraryComboBox(self):
        return "{styletype='combo-box-base combo-box' visible='true' window=" + self.mainShell + "}"

    def getLibraryFromComboBox(self):
        return "{container=" + self.popupControl + " id='list-view' styletype='list-view' visible='true'}"

    def getLibraryPanel(self, name):
        return "{caption='" + name + "' container=" + self.listView + " styletype='cell indexed-cell list-cell' visible='true'}"

    def getTextField(self):
        return "{styletype='text-input text-field' visible='true' window=" + self.mainShell + "}"

    def getButton(self, name):
        return "{caption='" + name + "' id='dialogButton' styletype='button scs-button' visible='true' window=" + self.mainShell + "}"


class AddFolderShell:
    """
    Class contains all real names of Add Folder Shell
    """
    def __init__(self):
        self.addFolderShell = "{caption='New Folder' isvisible='true' type='org.eclipse.swt.widgets.Shell'}"
        self.textField = "{styletype='text-input text-field' visible='true' window=" + self.addFolderShell + "}"
        self.textInput = "{container=" + self.textField + " type='javafx.scene.layout.Pane' visible='true'}"

    def getFolderShell(self):
        """
        Usage:
        AddFolderShell().getFolderShel()
        """
        return self.addFolderShell

    def getTextField(self):
        """
        Usage:
        AddFolderShell().getTextField()
        """
        return self.textInput

    def getOkButton(self, buttonName):
        """
        @param buttonName [string] name of button

        Usage:
        AddFolderShell().getOkButton("OK")
        """
        rnButton = "{caption?='" + "*" + buttonName + "*" + "' id='dialogButton' styletype='button scs-button' visible='true' window=" + self.addFolderShell + "}"
        return rnButton

    def getRealNameOfErrorMesage(self):
        """
        Usage:
        AddFolderShell().getRealNameOfErrorMesage()
        """
        realName = "{caption?='" + "*" + "already exists" + "*" + "' styletype='scs-error-label' visible='true' window=" + self.addFolderShell + "}"
        return realName


class AddFileShell:
    """
    Class contains all real names from Add File Shell
    """
    def __init__(self):
        self.addFileShell = "{caption='New Python script' isvisible='true' type='org.eclipse.swt.widgets.Shell'}"
        self.textField = "{styletype='text-input text-field' visible='true' window=" + self.addFileShell + "}"
        self.textInput = "{container=" + self.textField + " type='javafx.scene.layout.Pane' visible='true'}"

    def getFileShell(self):
        """
        Usage:
        AddFileShell().getFileShell()
        """
        return self.addFileShell

    def getTextField(self):
        """
        Usage:
        AddFileShell().getTextField()
        """
        return self.textInput

    def getOkButton(self, buttonName):
        """
        @param buttonName [string] name of the button

        Usage:
        AddFileShell().getOkButton("OK")
        """
        rnButton = "{caption?='" + "*" + buttonName + "*" + "' id='dialogButton' styletype='button scs-button' visible='true' window=" + self.addFileShell + "}"
        return rnButton


class RenameShell:
    """
    Class contains all real names of Rename Shell
    """
    def __init__(self):
        self.renameShell = "{caption='Rename' isvisible='true' type='org.eclipse.swt.widgets.Shell'}"
        self.textField = "{styletype='text-input text-field' visible='true' window=" + self.renameShell + "}"
        self.textInput = "{container=" + self.textField + " type='javafx.scene.layout.Pane' visible='true'}"
        self.messageContainer = "{basetype='javafx.scene.layout.StackPane' visible='true' window=" + self.renameShell + "}"
        self.closeButtonLabel = "{caption='X' styletype='label scs-closeLabel' visible='true' window=" + self.renameShell + "}"
        self.closeButton = "{caption='X' container='" + self.closeButtonLabel + "' styletype='text' visible='true'}"

    def getRenameShell(self):
        """
        Usage:
        RenameShell().getRenameShell()
        """
        return self.renameShell

    def getTextField(self):
        """
        Usage:
        RenameShell().getTextField()
        """
        return self.textInput

    def getOkButton(self, buttonName):
        """
        @param buttonName [string] name of button

        Usage:
        RenameShell().getOkButton("OK")
        """
        rnButton = "{caption?='" + "*" + buttonName + "*" + "' id='dialogButton' styletype='button scs-button' visible='true' window=" + self.renameShell + "}"
        return rnButton

    def getCloseButton(self):
        """
        Usage:
        RenameShell().getCloseButton()
        """
        return self.closeButton

    def getRealNameOfErrorMesage(self):
        """
        Usage:
        RenameShell().getRealNameOfErrorMesage()
        """
        realName = "{caption?='" + "*" + "already exists" + "*" + "' styletype='scs-error-label' visible='true' window=" + self.renameShell + "}"
        return realName


class NameAlreadyExistShell:
    """
    Class Conteins all real names from Name Already Exist Shell
    """
    def __init__(self, name):
        """
        @param name [string] name of shell, it could be - File name already exists
                                                        - Folder name already exists
        """
        self.mainShell = "{caption='" + name + "' isvisible='true' type='org.eclipse.swt.widgets.Shell'}"

    def getMainShell(self):
        """
        Usage:
        NameAlreadyExistShell(name).getMainShell()
        """
        return self.mainShell

    def getRadioButton(self, name):
        """
        @param name [string] if it's a file:  - Overwrite existing file
                                                 - Rename copied file
                                if it'a a folder - Overwrite existing folder
                                                 - Rename copied folder

        Usage:
        NameAlreadyExistShell(name).getRadioButton("OK")
        """
        radioButton = "{caption='" + name + "' styletype='radio-button' visible='true' window=" + self.mainShell + "}"
        return "{container=" + radioButton + " styletype='dot' visible='true'}"

    def getTextField(self):
        """
        Usage:
        NameAlreadyExistShell(name).getTextField()
        """
        return "{styletype='text-input text-field' visible='true' window=" + self.mainShell + "}"

    def getButton(self, name):
        """
        @param name [string] name of button

        Usage:
        NameAlreadyExistShell(name).getButton("OK")
        """
        rName = "{caption='" + name + "' id='dialogButton' styletype='button scs-button' visible='true' window=" + self.mainShell + "}"
        return rName

    def getWarningLabel(self, label):
        """
        @param label: [string] label full name

        Usage:
        NameAlreadyExistShell(Rename copied file).getWarningLabel("Error: File name already exist.")
        """
        return "{caption='" + label + "' styletype='scs-error-label' visible='true' window=" + self.mainShell + "}"


class AddExistingFileShell:
    """
    Class contains all real names from add existing File shell
    """
    def __init__(self):
        self.addExistingFileShell = "{caption='Add existing file' isvisible='true' type='org.eclipse.swt.widgets.Shell'}"
        self.textField = "{styletype='text-input text-field' visible='true' window=" + self.addExistingFileShell + "}"
        self.textInput = "{container=" + self.textField + " type='javafx.scene.layout.Pane' visible='true'}"

    def getFileShell(self):
        """
        Usage:
        AddExistingFileShell().getFileShell()
        """
        return self.addExistingFileShell

    def getTextField(self):
        """
        Usage:
        AddExistingFileShell().getTextField()
        """
        return self.textInput

    def getOkButton(self, buttonName):
        """
        @param buttonName [string] name of button

        Usage:
        AddExistingFileShell().getOkButton("OK")
        """
        rnButton = "{caption?='" + "*" + buttonName + "*" + "' id='dialogButton' styletype='button scs-button' visible='true' window=" + self.addExistingFileShell + "}"
        return rnButton

    def getRadioButton(self, name):
        """
        @param name [string] - Copy into the project
                                - Link to existing

        Usage:
        AddExistingFileShell().()
        """
        radioButton = "{caption='" + name + "' styletype='radio-button' visible='true' window=" + self.addExistingFileShell + "}"
        return "{container=" + radioButton + " styletype='dot' visible='true'}"


class AddExistingFolderShell:
    """
    Class contains all real names from Add Existing Folder Shell
    """
    def __init__(self):
        self.addExistingFolderShell = "{caption='Add existing folder' isvisible='true' type='org.eclipse.swt.widgets.Shell'}"
        self.textField = "{styletype='text-input text-field' visible='true' window=" + self.addExistingFolderShell + "}"
        self.textInput = "{container=" + self.textField + " type='javafx.scene.layout.Pane' visible='true'}"

    def getFolderShell(self):
        """
        Usage:
        AddExistingFolderShell().getFolderShell()
        """
        return self.addExistingFolderShell

    def getTextField(self):
        """
        Usage:
        AddExistingFolderShell().getTextField()
        """
        return self.textInput

    def getOkButton(self, buttonName):
        """
        @param butonName [string] name of button

        Usage:
        AddExistingFolderShell().getOkButton("OK")
        """
        rnButton = "{caption?='" + "*" + buttonName + "*" + "' id='dialogButton' styletype='button scs-button' visible='true' window=" + self.addExistingFolderShell + "}"
        return rnButton

    def getRadioButton(self, name):
        """
        @param name [string] - Copy into the project
                            - Link to existing

        Usage:
        AddExistingFolderShell().getRadioButton("Copy")
        """
        radioButton = "{caption='" + name + "' styletype='radio-button' visible='true' window=" + self.addExistingFolderShell + "}"
        return "{container=" + radioButton + " styletype='dot' visible='true'}"


class PanelEditor:
    """
    Class contains all real names of Penel editor
    """
    def __init__(self, name, tooltip=None):
        if tooltip == None:
            self.cTabItem = "{caption?='" + "*" + name + "' parent.visible='true' type='org.eclipse.swt.custom.CTabItem' window=" + MainShell().getMainWindow() + "}"
        else:
            self.cTabItem = "{caption?='" + "*" + name + "' parent.visible='true' type='org.eclipse.swt.custom.CTabItem' window=" + MainShell().getMainWindow() + " item.tooltiptext?='*" + tooltip + "*'}"
        self.preview = "{caption='PREVIEW' container=" + self.cTabItem + " id='previewLink' styletype='hyperlink' visible='true'}"
        self.root = "{container=" + self.cTabItem + " styletype='root scs-part' visible='true'}"
        self.rootWithoutSCSPart = "{container=" + self.cTabItem + " styletype='root' visible='true'}"
        self.sceneLayoutPane = "{container=" + self.cTabItem + " type='javafx.scene.layout.Pane' visible='true'}"
        self.panelClose = "{container=" + self.cTabItem + " type='com.froglogic.squish.swt.CTabCloseBox'}"
        self.group = "{container=" + self.cTabItem + " id='0' type='javafx.scene.Group' visible='true'}"

    def getTabItem(self):
        """
        Usage:
        PanelEditor(name).getTabItem()
        """
        return self.cTabItem

    def getPreview(self):
        """
        Usage:
        PanelEditor(name).getPreview()
        """
        return self.preview

    def getRoot(self):
        """
        Usage:
        PanelEditor(name).getRoot()
        """
        return self.root

    def getRootWithoutSCSPart(self):
        """
        Usage:
        PanelEditor(name).getRootWithoutSCSPart()
        """
        return self.rootWithoutSCSPart

    def getWidget(self, widget, widget_control_ID=None):
        """
        @param widget [string] name of widget
        @param widget_control_ID [string] defoult None

        Usage:
        panel = "Blank.panel"
        widget = "Button"
        widget_ID = "button_0"

        PanelEditor(panel).getWidget(widget, widget_ID)
        """
        splitString = widget.split(" ")
        mergeString = "".join(splitString) + "Widget"

        if widget_control_ID != None:
            return "{container=" + self.cTabItem + " visible='true' type='com.cirrus.scs.ide.paneleditor.ui.widget." + mergeString + "' model.name='" + widget_control_ID + "'}"
        else:
            return "{container=" + self.cTabItem + " type='com.cirrus.scs.ide.paneleditor.ui.widget." + mergeString + "' visible='true'}"

    def getGroup(self):
        """
        Usage:
        PanelEditor(name).getGroup()
        """
        return self.group

    def getBlockBorderPane(self, borderID=None):
        """
        Usage:
        PanelEditor(name).getBlockBorderPane(160)
        PanelEditor(name).getBlockBorderPane()
        """
        if borderID == None:
            borderPane = "{container=" + self.group + " type='javafx.scene.layout.BorderPane' visible='true'}"
        else:
            borderPane = "{container=" + self.group + " id='" + borderID + "' type='javafx.scene.layout.BorderPane' visible='true'}"
        return borderPane

    def getBlockName(self, borderID, name):
        """
        @param borderID [int] border pane ID
        @param name [string] border pane label name
        Usage:
        PanelEditor(name).getBlockName(1, "EVENTS")
        PanelEditor(name).getBlockName(2, "ACTIONS")
        """
        borderPane = "{container=" + self.group + " id='" + str(borderID) + "' type='javafx.scene.layout.BorderPane' visible='true'}"
        label = "{caption='" + name + "' container=" + borderPane + " styletype='label' visible='true'}"
        return label

    def getLayoutPane(self):
        """
        Usage:
        PanelEditor(name).getLayoutPane()
        """
        return self.sceneLayoutPane

    def getAlignLeft(self):
        """
        Usage:
        PanelEditor(name).getAlignLeft()
        """
        return "{caption='' container=" + self.cTabItem + " styletype='button scs-toolbar-button scs-toolbar-button-align-left' visible='true'}"

    def getAlignCenterVertical(self):
        """
        Usage:
        PanelEditor(name).getAlignCenterVertical()
        """
        return "{caption='' container=" + self.cTabItem + " styletype='button scs-toolbar-button scs-toolbar-button-center-vertical' visible='true'}"

    def getAlignRight(self):
        """
        Usage:
        PanelEditor(name).getAlignRight()
        """
        return "{caption='' container=" + self.cTabItem + " styletype='button scs-toolbar-button scs-toolbar-button-align-right' visible='true'}"

    def getAlignTop(self):
        """
        Usage:
        PanelEditor(name).getAlignTop()
        """
        return "{caption='' container=" + self.cTabItem + " styletype='button scs-toolbar-button scs-toolbar-button-align-top' visible='true'}"

    def getAlignCenterHorizontal(self):
        """
        Usage:
        PanelEditor(name).getAlignCenterHorizontal()
        """
        return "{caption='' container=" + self.cTabItem + " styletype='button scs-toolbar-button scs-toolbar-button-center-horizontal' visible='true'}"

    def getAlignBottom(self):
        """
        Usage:
        PanelEditor(name).getAlignBottom()
        """
        return "{caption='' container=" + self.cTabItem + " styletype='button scs-toolbar-button scs-toolbar-button-align-bottom' visible='true'}"

    def getAlignBringToFront(self):
        """
        Usage:
        PanelEditor(name).getAlignBringToFront()
        """
        return "{caption='' container=" + self.cTabItem + " styletype='button scs-toolbar-button scs-toolbar-button-bring-to-front' visible='true'}"

    def getAlignSendToBack(self):
        """
        Usage:
        PanelEditor(name).getAlignSendToBack()
        """
        return "{caption='' container=" + self.cTabItem + " styletype='button scs-toolbar-button scs-toolbar-button-send-to-back' visible='true'}"

    def getAlignHorizontalSpacing(self):
        """
        Usage:
        PanelEditor(name).getAlignHorizontalSpacing()
        """
        return "{caption='' container=" + self.cTabItem + " styletype='button scs-toolbar-button scs-toolbar-button-horizontal-spacing' visible='true'}"

    def getAlignVerticalSpacing(self):
        """
        Usage:
        PanelEditor(name).getAlignVerticalSpacing()
        """
        return "{caption='' container=" + self.cTabItem + " styletype='button scs-toolbar-button scs-toolbar-button-vertical-spacing' visible='true'}"

    def getPanelClose(self):
        """
        Usage:
        PanelEditor(name).getPanelClose()
        """
        return self.panelClose

    def getContainer(self, container, container_control_ID=None):
        """
        @param container [string] name of container
        @param container_control_ID [string] default None
        @return container real name

        Usage:
        panel = "Blank.panel"

        PanelEditor(panel).getWidget("Blank Container")
        PanelEditor(panel).getContainer("Diagram Image", "diagram_image_1")
        """
        if container_control_ID == None:
            if container == "Blank Container":
                rnContainer = "{container=" + self.cTabItem + " styletype='blank-container scs-border-dotted' visible='true'}"
            elif container == "One Column Container":
                rnContainer = "{container=" + self.cTabItem + " styletype='one-col-container scs-border-dotted' visible='true'}"
            elif container == "Diagram Image":
                rnContainer = "{container=" + self.cTabItem + " styletype='diagram-container' visible='true'}"
            return rnContainer
        else:
            if container == "Blank Container":
                rnContainer = "{container=" + self.cTabItem + " visible='true' styletype='blank-container scs-border-dotted' model.name='" + container_control_ID + "'}"
            elif container == "One Column Container":
                rnContainer = "{container=" + self.cTabItem + " visible='true' styletype='one-col-container scs-border-dotted' model.name='" + container_control_ID + "'}"
            elif container == "Diagram Image":
                rnContainer = "{container=" + self.cTabItem + " visible='true' styletype='diagram-container' model.name='" + container_control_ID + "'}"
            return rnContainer

    def getBorderPaneOrConnectionID(self, type, number):
        """
        @param [string] type of object on panel - can be BorderPane or Connection
        @param number [int] ordinal number of border pane or connection which is added to the panel
        @return border pane or connection id

        Usage:
        panel = "DMC.bdf"

        PanelEditor(panel).getBorderPaneOrConnectionID("BorderPane", 1)
        PanelEditor(panel).getBorderPaneOrConnectionID("BorderPane", 3)
        PanelEditor(panel).getBorderPaneOrConnectionID("Connection", 1)
        PanelEditor(panel).getBorderPaneOrConnectionID("Connection", 2)
        """
        list = []
        children = ""
        try:
            children = str(waitForObject(self.group).children)
        except LookupError:
                test.fail("FAIL", "Object or propery does not exist")
        list = children.split(',')
        IDs = []
        for i in list:
            if type + "[id=" in i:
                IDs.append(re.sub(r'\D', '', i))
        try:
            ID = IDs[number - 1]
        except:
            test.fail("FAIL", "Number is not correct")
        return ID

    def getConnection(self, ID):
        """
        @param ID [int] id of connection

        Usage:
        panel = "DMC.bdf"

        PanelEditor(panel).getConnection(23)
        PanelEditor(panel).getConnection(156)
        """
        connection = "{container=" + self.cTabItem + " id='" + str(ID) + "' type='org.eclipse.gef4.fx.nodes.Connection' visible='true'}"
        return connection

    def getLastAddedBorderPane(self):
        """
        @return last added border pane real name

        Usage:
        panel = "DMC.bdf"

        PanelEditor(panel).getLastAddedBorderPane()
        """
        borderPaneList = []
        try:
            borderPaneList = str(waitForObject(self.group).children)
        except LookupError:
                test.fail("FAIL", "Object or propery does not exist")
        borderPanes = borderPaneList.split(',')
        borderIDs = []
        for i in borderPanes:
            if "BorderPane[id=" in i:
                borderIDs.append(re.sub(r'\D', '', i))
        lastAddedBorderPaneId = borderIDs[len(borderIDs) - 1]
        lastAddedBorderPane = "{container=" + self.cTabItem + " id='" + str(lastAddedBorderPaneId) + "' type='javafx.scene.layout.BorderPane' visible='true'}"
        return lastAddedBorderPane

    def getBorderPaneFromBorderPane(self, parentBorderPane, side, borderPaneNumber):
        """
        @param parentBorderPane [string] parent border pane
        @param side [string] side of borderPane in parent borderPane - can be top, bottom, right or left
        @param borderPaneNumber [int] ordinal number of port from one side of block - for example: if there is 4 ports portNumber can be 1, 2, 3 or 4
        @return border pane real name

        Usage:
        panel = "DMC.bdf"
        parentBorderPane = PanelEditor(panel).getLastAddedBorderPane()

        PanelEditor(panel).getBorderPaneFromBorderPane(parentBorderPane, "left", 1)
        PanelEditor(panel).getBorderPaneFromBorderPane(parentBorderPane, "left", 2)
        PanelEditor(panel).getBorderPaneFromBorderPane(parentBorderPane, "right", 1)
        """
        if side == "top":
            try:
                borderPaneList = str(waitForObject(parentBorderPane).top.children)
            except LookupError:
                test.fail("FAIL", "Object or propery does not exist")
        elif side == "bottom":
            try:
                borderPaneList = str(waitForObject(parentBorderPane).bottom.children)
            except LookupError:
                test.fail("FAIL", "Object or propery does not exist")
        elif side == "right":
            try:
                borderPaneList = str(waitForObject(parentBorderPane).right.children)
            except LookupError:
                test.fail("FAIL", "Object or propery does not exist")
        elif side == "left":
            try:
                borderPaneList = str(waitForObject(parentBorderPane).left.children)
            except LookupError:
                test.fail("FAIL", "Object or propery does not exist")
        else:
            test.fail("FAIL", "Wrong second parameter")
        borderPanes = borderPaneList.split()
        borderPaneIDs = []
        for i in borderPanes:
            if "id=" in i:
                borderPaneIDs.append(re.sub(r'\D', '', i))
        borderPane = "{container=" + parentBorderPane + " id='" + str(borderPaneIDs[borderPaneNumber - 1]) + "' type='javafx.scene.layout.BorderPane' visible='true'}"
        return borderPane

    def getPort(self, borderPane, side, portNumber):
        """
        @param borderPane - real name of border pane
        @param side [string] side of port - can be top, bottom, right or left
        @param portNumber [int] ordinal number of port from one side of block - for example: if there is 4 ports portNumber can be 1, 2, 3 or 4
        @return port real name

        Usage:
        panel = "DMC.bdf"
        borderPane = PanelEditor(panel).getLastAddedBorderPane()

        PanelEditor(panel).getPort(borderPane, "right", 1)
        PanelEditor(panel).getPort(borderPane, "left", 2)
        """
        if side == "top":
            try:
                portList = str(waitForObject(borderPane).top.children)
            except LookupError:
                test.fail("FAIL", "Object or propery does not exist")
        elif side == "bottom":
            try:
                portList = str(waitForObject(borderPane).bottom.children)
            except LookupError:
                test.fail("FAIL", "Object or propery does not exist")
        elif side == "right":
            try:
                portList = str(waitForObject(borderPane).right.children)
            except LookupError:
                test.fail("FAIL", "Object or propery does not exist")
        elif side == "left":
            try:
                portList = str(waitForObject(borderPane).left.children)
            except LookupError:
                test.fail("FAIL", "Object or propery does not exist")
        else:
            test.fail("FAIL", "Wrong second parameter")
        ports = portList.split()
        portIDs = []
        for i in ports:
            if "id=" in i:
                portIDs.append(re.sub(r'\D', '', i))
        port = "{container=" + borderPane + " id='" + str(portIDs[portNumber - 1]) + "' type='javafx.scene.shape.SVGPath' visible='true'}"
        return port

    def getVBoxPort(self, name, side):
        """
        @param name [string] name of block/widget
        @param side [string] side of port - can be left or right
        @return port real name

        Usage:
        panel = "Event Handling.bdf"

        PanelEditor(panel).getVBoxPort("GPI", "right")
        PanelEditor(panel).getVBoxPort("GPI", "left")
        """
        borderPane = "{container=" + self.cTabItem + " type='javafx.scene.layout.BorderPane' visible='true' center.children?='*" + name + "*'}"
        portSide = ""
        if side == "right":
            try:
                portSide = str(waitForObject(borderPane).right)
            except LookupError:
                test.fail("FAIL", "Object or propery does not exist")
        elif side == "left":
            try:
                portSide = str(waitForObject(borderPane).left)
            except LookupError:
                test.fail("FAIL", "Object or propery does not exist")
        else:
            test.fail("FAIL", "Wrong second parameter")
        port = "{container=" + borderPane + " type='javafx.scene.shape.SVGPath' visible='true' parent='" + portSide + "'}"
        return port

    def getHelpText(self, name):
        """
        @param name [string] text

        Usage:
        panel = "DMC.bdf"
        PanelEditor(panel).getHelpText("Drop items from the palette window here then use your mouse or touchpad to draw connecting wires")
        """
        helpText = "{caption='" + name + "' container=" + self.cTabItem + " styletype='help-text' visible='true'}"
        return helpText

    def getStackPane(self, borderPane):
        """
        @param borderPane real name of borderPane which is parent of stack pane we need
        @return stackPane real name of stack pane

        Usage:
        panel = "DMC.bdf"
        PanelEditor(panel).getStackPane(BorderPane0)
        """
        stackPane = "{container=" + borderPane + " type='javafx.scene.layout.StackPane' visible='true'}"
        return stackPane


class PanelRuntime:
    """
    Class contains all real names of PanelRuntime
    """
    def __init__(self, name):
        self.cTabItem = "{caption='" + name + "' parent.visible='true' type='org.eclipse.swt.custom.CTabItem' window=" + MainShell().getMainWindow() + "}"
        self.buttonWidget = "{container=" + self.cTabItem + " styletype='button-widget' visible='true'}"
        self.dialWidget = "{container=" + self.cTabItem + " styletype='dial-widget' visible='true'}"
        self.sliderWidget = "{container=" + self.cTabItem + " styletype='slider-widget' visible='true'}"
        self.sliderWidgetTextBox = "{container=" + self.sliderWidget + " styletype='numeric-field-widget slider-numeric-field' visible='true'}"
        self.runtimePanel = "{container=" + self.cTabItem + " styletype='scs-runtime-panel' visible='true'}"

    def getCTabitem(self):
        """
        PanelRuntime(name).getCTabitem()
        """
        return self.cTabItem

    def getDialWidget(self):
        """
        Usage:
        PanelRuntime(name).getDialWidget()
        """
        return self.dialWidget

    def getSliderWidzet(self):
        """
        Usage:
        PanelRuntime(name).etSliderWidzet()
        """
        return self.sliderWidget

    def getSliderWidzetTextBox(self):
        """
        Usage:
        PanelRuntime(name).getSliderWidzetTextBox()
        """
        return self.sliderWidgetTextBox

    def getButtonWidget(self):
        """
        Usage:
        panel = "Blank.panel"

        PanelRuntime("Blank").getButtonWidget()
        or
        PanelRuntime(panel.split(".")[0]).getButtonWidget()
        """
        return self.buttonWidget

    def getContainer(self, container, container_control_ID=None):
        """
        @param container [string] name of container
        @param container_control_ID [string] default None
        @return container real name

        Usage:
        panel = "Blank.panel"

        PanelRuntime(name).getContainer("One Column Container", "one_column_container_1")
        """
        if container_control_ID == None:
            if container == "Blank Container":
                rnContainer = "{container=" + self.cTabItem + " styletype='blank-container scs-border-solid' visible='true'}"
            elif container == "One Column Container":
                rnContainer = "{container=" + self.cTabItem + " styletype='one-col-container scs-border-solid' visible='true'}"
            elif container == "Diagram Image":
                rnContainer = "{container=" + self.cTabItem + " styletype='diagram-container' visible='true'}"
            return rnContainer
        else:
            if container == "Blank Container":
                rnContainer = "{container=" + self.cTabItem + " styletype='blank-container scs-border-solid' model.name='" + container_control_ID + "' visible='true'}"
            elif container == "One Column Container":
                rnContainer = "{container=" + self.cTabItem + " styletype='one-col-container scs-border-solid' model.name='" + container_control_ID + "' visible='true'}"
            elif container == "Diagram Image":
                rnContainer = "{container=" + self.cTabItem + " styletype='diagram-container' model.name='" + container_control_ID + "' visible='true'}"

            return rnContainer

    def getRuntimePanel(self):
        """
        Usage:
        PanelRuntime(name).getRuntimePanel()
        """
        return self.runtimePanel

    def getBorderPane(self, ID):
        """
        @param [integer] border pane ID

        Usage:
        PanelRuntime(name).getBorderPane(15)
        PanelRuntime(name).getBorderPane(256)
        PanelRuntime(name).getBorderPane(4500)
        """
        self.borderPane = "{container=" + self.cTabItem + " id='" + str(ID) + "' type='javafx.scene.layout.BorderPane' visible='true'}"
        return self.borderPane


class Palette:
    """
    Class contains all real names from palette
    """
    def __init__(self):
        self.cTabItem = "{caption='Palette' parent.visible='true' type='org.eclipse.swt.custom.CTabItem' window=" + MainShell().getMainWindow() + "}"
        self.tableView = "{container=" + self.cTabItem + " id='paletteTableView' styletype='table-view' visible='true'}"
        self.textFieldFilter = "{container=" + self.cTabItem + " styletype='text-input text-field scs-text-field-filter' visible='true'}"
        self.paletteCombobox = "{container=" + self.cTabItem + " styletype='combo-box-base combo-box scs-combo-box-search' visible='true'}"

    def getCTabItem(self):
        """
        Usage:
        Palette().getCTabItem()
        """
        return self.cTabItem

    def getTableView(self):
        """
        Usage:
        Palette().getTableView()
        """
        return self.tableView

    def getWidget(self, name):
        """
        @param name [string] name of widget

        Usage:
        Palette().getWidget(name)
        """
        obj = waitForObject(self.tableView)
        widgetCounter = 0
        while widgetCounter <= obj.items.length:
            temp = "{caption='TableRow" + str(widgetCounter) + "' container=" + self.tableView + " type='com.froglogic.squish.jfx.TableRowProxy'}"
            snooze(0.3)
            if not "indexed-cell table-row-cell" in str(findObject(temp).cell):
                mouseClick(findObject(temp), 5, 5, 0, Button.Button1)
                snooze(1)
            elif name in str(waitForObject(temp).cell.childrenunmodifiable):
                return temp
            else:
                widgetCounter += 1
        return False

    def getWidgetFromPalette(self, name):
        """
        @param name [string] name of wigdet

        Usage:
        Palette().getWidgetFromPalette(name)
        """
        return "{caption='" + name + "' container={caption='" + name + "' column?='?*' container=" + self.tableView + " row?='?*' styletype='cell indexed-cell table-cell table-column' visible='true'} styletype='text' visible='true'}"

    def getTextFieldFilter(self):
        """
        Usage:
        Palette().getTextFieldFilter()
        """
        return self.textFieldFilter

    def getPaletteCombobox(self):
        """
        Usage:
        Palette().getPaletteCombobox()
        """
        return self.paletteCombobox

    def getTableViewItem(self, column, row):
        """
        @param name [int] column of TableView
        @param name [int] row of TableView

        Usage:
        Palette().getTableViewItem(column,row)
        """
        tableViewItem = "{column='" + str(column) + "' container=" + self.tableView + " id='paletteItem' row='" + str(row) + "' styletype='cell indexed-cell table-cell table-column' visible='true'}"
        return tableViewItem

    def getTableViewItemChild(self, column, row):
        tableViewItemChild = "{container=" + Palette().getTableViewItem(column, row) + " type='javafx.scene.shape.SVGPath' visible='true'}"
        return tableViewItemChild

    def getPaletteComboBoxItem(self, name):
        """
        @param name [string] Name of Palette Combobox item

        Usage:
        Palette().getPaletteComboBoxItem(name)
        """
        paletteComboboxItem = "{caption='" + name + "' container=" + PopupListView().getListView() + " styletype='cell indexed-cell list-cell' visible='true'}"

        return paletteComboboxItem

    def getMissingBlock(self, index):
        """
        @param index [int]: index of column

        Usage:
        Palette().getMissingBlock(index)
        """
        missingBlock = "{caption='MISSING BLOCK' column='" + str(index) + "' container=" + self.tableView + " id='paletteError' styletype='cell indexed-cell table-cell table-column' visible='true'}"
        return missingBlock


class BlockProperties:
    """
    Class contains all real names from Block Properties tab
    """
    def __init__(self):
        self.cTabItem = "{caption='Block Properties' parent.visible='true' type='org.eclipse.swt.custom.CTabItem' window=" + MainShell().getMainWindow() + "}"
        self.tableView = "{container=" + self.cTabItem + " id='propertiesTableView' styletype='root table-view' visible='true'}"
        self.lockedCheckBox = "{caption='' container=" + self.cTabItem + " id='Locked' styletype='check-box' visible='true'}"

    def getLockedCheckBox(self):
        """
        Usage:
        BlockProperties.getLockedCheckBox()
        """
        return self.lockedCheckBox

    def getTableViewCellByPosition(self, column, row):
        """
        @param column [int] column of the Block Properties table
        @param row [int] row of the Block Properties table

        Usage:
        blockPropertiesObj = BlockProperties()
        blockPropertiesObj.getTableViewCellByPosition(column, row)
        """
        tableViewCell = "{column='" + str(column) + "' container=" + self.tableView + " row='" + str(row) + "' styletype='cell indexed-cell table-cell table-column' visible='true'}"
        return tableViewCell

    def getTableViewCellCombobox(self, column, row):
        """
        @param column [int] column of the Block Properties table
        @param row [int] row of the Block Properties table

        Usage:
        blockPropertiesObj = BlockProperties()
        blockPropertiesObj.getTableViewCellCombobox(column, row)
        """
        tableViewCell = "{column='" + str(column) + "' container=" + self.tableView + " row='" + str(row) + "' styletype='cell indexed-cell table-cell table-column' visible='true'}"
        tableViewCellCombobox = "{container=" + tableViewCell + "  styletype='combo-box-base combo-box' visible='true'}"
        return tableViewCellCombobox


class WidgetProperties:

    def __init__(self, name):
        self.ControlID = [1, 0]
        self.cTabItem = "{caption='" + name + " Properties' parent.visible='true' type='org.eclipse.swt.custom.CTabItem' window=" + MainShell().getMainWindow() + "}"
        self.tableView = "{container=" + self.cTabItem + " id='propertiesTableView' styletype='root table-view' visible='true'}"

    def getWidgetPropertiesTab(self):
        """
        Usage:
        WidgetProperties(name).getWidgetPropertiesTab()
        """
        return self.cTabItem

    def getTableViewCellByPosition(self, column, row):
        """
        @param column [int] column of the Widget properties table
        @param row [int] row of the Widget properties table
        Usage:
        WidgetProperties(name).getTableViewCellByPosition(column, row)
        """
        tableViewCell = "{column='" + str(column) + "' container=" + self.tableView + " row='" + str(row) + "' styletype='cell indexed-cell table-cell table-column' visible='true'}"
        return tableViewCell

    def getTableViewCellItem(self, tableViewCell):
        """
        @param tableViewCell [string] real name of the tableViewCell
        Usage:
        WidgetProperties(name).getTableViewCellItem(tableViewCell)
        """
        tableViewCellItem = "{caption='' container=" + tableViewCell + " styletype='button scs-browse-button' visible='true'}"
        return tableViewCellItem

    def getTableViewCellTextFiled(self, tableViewCell):
        textField = "{container=" + tableViewCell + " styletype='text-input text-field' visible='true'}"
        return textField

    def getControlID(self):
        """
        Usage:
        WidgetProperties(name).getControlID()
        """
        return "{container={column='" + str(self.ControlID[0]) + "' container=" + self.tableView + " row='" + str(self.ControlID[1]) + "' styletype='cell indexed-cell table-cell table-column' visible='true'} id='ControlID' styletype='text-input text-field' visible='true'}"

    def getTextField(self, id):
        """
        Usage:
        WidgetProperties(name).getTextField("Field")
        """
        propertyTable = "{container=" + self.cTabItem + " id='propertiesTableView' styletype='root table-view' visible='true'}"
        if id in ["Field", "Size", "Style"]:
            fieldTextContainer = "{container=" + propertyTable + " id='" + id + "' styletype='combo-box-base combo-box' visible='true'}"
        else:
            fieldTextContainer = "{container=" + propertyTable + " id='" + id + "' styletype='text-input text-field' visible='true'}"
        return "{container=" + fieldTextContainer + " type='javafx.scene.layout.Pane' visible='true'}"


class BoardFirmwareUpdateShell:
    """
    Class contains all real names from Board Firmware Update Shell
    There are a few shells/dialogs: - Board Firmware Update
                                    - Checking firmware version...
                                    - Update complete
    """
    def __init__(self, name):
        self.mainShell = "{caption='" + name + "' isvisible='true' type='org.eclipse.swt.widgets.Shell'}"
        self.listView = "{styletype='list-view' visible='true' window=" + self.mainShell + "}"

    def getMainShell(self):
        """
        Usage:
        BoardFirmwareUpdateShell(name).getMainShell()
        """
        return self.mainShell

    def getBoard(self, name):
        """
        @param name [string] name of board

        Usage:
        BoardFirmwareUpdateShell(name).getBoard(name)
        """
        return "{caption='" + name + "' container=" + self.listView + " styletype='cell indexed-cell list-cell' visible='true'}"

    def getRedButton(self, name):
        """
        @param name [string] name of button

        Usage:
        BoardFirmwareUpdateShell(name).getRedButton(name)
        """
        return "{caption='" + name + "' id='dialogButton' styletype='button scs-button scs-red-button' visible='true' window=" + self.mainShell + "}"

    def getButton(self, name):
        """
        @param name [string] name of button

        Usage:
        BoardFirmwareUpdateShell(name).getButton(name)
        """
        return "{caption='" + name + "' id='dialogButton' styletype='button scs-button' visible='true' window=" + self.mainShell + "}"

    def getOKButton(self):
        """
        Usage:
        BoardFirmwareUpdateShell(name).getOKButton()
        """
        return "{caption='OK' styletype='button scs-button' visible='true' window=" + self.mainShell + "}"

    def getLabel(self, labelName):
        """
        Usage:
        BoardFirmwareUpdateShell(name).getLabel(labelName)
        """
        label = "{caption='" + labelName + "' styletype='label' visible='true' window=" + self.mainShell + "}"
        return label


class HelpAboutShell:
    """
    Class contains all real names from Help->About Shell
    """
    def __init__(self):
        self.aboutSCS = "{caption='About SoundClear Studio' isvisible='true' type='org.eclipse.swt.widgets.Shell'}"
        self.ScsAndBspVersion = "{caption?='SoundClear Studio:*' styletype='label' visible='true' window=" + self.aboutSCS + "}"
        self.closeAboutSCS = "{caption='X' styletype='label scs-closeLabel' visible='true' window=" + self.aboutSCS + "}"

    def getAboutSCS(self):
        """
        Usage:
        HelpAboutShell().getAboutSCS()
        """

        return self.aboutSCS

    def getVersionShell(self):
        """
        Usage:
        HelpAboutShell().getVersionShell()
        """
        return self.ScsAndBspVersion

    def getCloseAboutSCS(self):
        """
        Usage:
        HelpAboutShell().getCloseAboutSCS()
        """
        return self.closeAboutSCS


class SaveResourceShell:
    """Class contains all real names from Save Resource Shell"""
    def __init__(self):
        self.saveResourcesShell = "{caption='Save resources' isvisible='true' type='org.eclipse.swt.widgets.Shell'}"
        self.saveResourcesShellWindow = "{styletype='root scs-commonDialogDark' visible='true' window=" + self.saveResourcesShell + "}"
        self.closeLabel = "{caption='X' styletype='label scs-closeLabel' visible='true' window=" + self.saveResourcesShell + "}"
        self.closeButon = "{caption='X' container=" + self.closeLabel + " styletype='text' visible='true'}"
        self.dialogBackground = "{styletype='scs-commonDialogBackground scs-dialogRoot' visible='true' window=" + self.saveResourcesShell + "}"
        self.listview = "{styletype='list-view scs-listview-dialog' visible='true' window=" + self.saveResourcesShell + "}"

    def getSaveResourcesShell(self):
        """
        Usage:
        SaveResourceShell().getSaveResourcesShell()
        """
        return self.saveResourcesShell

    def getCloseButton(self):
        """
        Usage:
        SaveResourceShell().getCloseButton()
        """
        return self.closeButon

    def getSelectDeselectButton(self, buttonName):
        """
        @param buttonName [string] name of the button to click

        Usage:
        SaveResourceShell().getSelectDeselectButton("Deselect All")
        SaveResourceShell().getSelectDeselectButton("Select All")
        """
        buttonContainer = "{caption='" + buttonName + "' id='selectDeselectButton' styletype='button scs-button' visible='true' window=" + self.saveResourcesShell + "}"
        button = "{caption='" + buttonName + "' container=" + buttonContainer + " styletype='text' visible='true'}"
        return button

    def getButton(self, buttonName):
        """
        @param buttonName [string] name of the button to click

        Usage:
        SaveResourceShell().getButton("OK")
        """
        buttonContainer = "{caption='" + buttonName + "' id='dialogButton' styletype='button scs-button' visible='true' window=" + self.saveResourcesShell + "}"
        button = "{caption='" + buttonName + "' container=" + buttonContainer + " styletype='text' visible='true'}"
        return button

    def getfileFromList(self, nameOfFile):
        """
        @param nameOfFile [string] name of file from list

        Usage:
        SaveResourceShell().getfileFromList("Blank.panel")
        """
        listItemContainer = "{caption='" + nameOfFile + "' container=" + self.listview + " styletype='cell indexed-cell list-cell check-box-list-cell' visible='true'}"
        listItem = "{caption='" + nameOfFile + "' container=" + listItemContainer + " styletype='text' visible='true'}"
        return listItem

    def getChackBoxFromListItem(self, nameOfFile):
        """
        @param nameOfFile [string] name of file that is in list view

        Usage:
        SaveResourceShell().getChackBoxFromListItem("Blank.panel")
        """
        listItemContainer = "{caption='" + nameOfFile + "' container=" + self.listview + " styletype='cell indexed-cell list-cell check-box-list-cell' visible='true'}"
        checkBox = "{caption='' container=" + listItemContainer + " styletype='check-box' visible='true'}"
        return checkBox


class Problems:
    """
    Class contains all real names from Problems
    """
    def __init__(self):
        self.cTabItem = "{caption='Problems' parent.visible='true' type='org.eclipse.swt.custom.CTabItem' window=" + MainShell().getMainWindow() + "}"
        self.closeProblems = "{container=" + self.cTabItem + " type='com.froglogic.squish.swt.CTabCloseBox'}"
        self.tableView = "{container=" + self.cTabItem + " id='problemsTreeTableView' styletype='tree-table-view' visible='true'}"
        self.contextMenuCopy = "{type='com.cirrus.scs.ide.ui.javafx.controls.SCSContextMenu' visible='true'}"
        self.comboBoxSearch = "{container=" + self.cTabItem + " styletype='scs-combo-box-search' visible='true'}"
        self.comboBox = "{container=" + self.comboBoxSearch + " styletype='combo-box-base combo-box' visible='true'}"
        self.popupControl = "{basetype='javafx.scene.control.PopupControl' visible='true'}"
        self.listView = "{container=" + self.popupControl + " id='list-view' styletype='list-view' visible='true'}"
        self.noProblems = "{caption='No problems' container=" + self.tableView + " styletype='label' visible='true'}"
        self.placeholder = "{container=" + self.tableView + " styletype='placeholder' visible='true'}"

    def getCTabItem(self):
        """
        Usage:
        Problems().getCTabItem()
        """
        return self.cTabItem

    def closeProblems(self):
        """
        Usage:
        Problems().closeProblems()
        """
        return self.cTabItem

    def getProblemsRow(self, number):
        """
        Usage:
        Problems().getProblemsRow()
        """
        problemsRow = "{container=" + self.tableView + "  styletype='cell indexed-cell tree-table-row-cell' visible='true' index ='" + number + "'}"
        return problemsRow

    def getProblemsFromRow(self, column, index):
        """
        @param column: [string] ("DESCRIPTION", "FILE", "PATH")
        @param index: [string] row number (index)

        Usage:
        Problems().getProblemsFromRow("DESCRIPTION", "1")
        """
        problemsFromRow = "{tablecolumn.text='" + column + "' container={container=" + self.tableView + " styletype='cell indexed-cell tree-table-row-cell' visible='true' index='" + index + "'} styletype='cell indexed-cell tree-table-cell table-column' visible='true'}"
        return problemsFromRow

    def getNoProblemsLabel(self):
        """
        Usage:
        Problems().getNoProblemsLabel()
        """
        return "{caption='No problems' container=" + self.tableView + " styletype='label' visible='true'}"

    def getContextMenuCopy(self):
        """
        Usage:
        Problems().getContextMenuCopy()
        """
        return self.contextMenuCopy

    def getComboBoxItem(self, item):
        """
        Usage:
        Problems().getComboBoxItem("Error")
        """
        rnItem = "{caption='" + item + "' container=" + self.listView + " styletype='cell indexed-cell list-cell check-box-list-cell' visible='true'}"
        return rnItem

    def getComboBoxSearch(self):
        """
        Usage:
        Problems().getComboBoxSearch()
        """
        return self.comboBoxSearch

    def getPopupControl(self):
        """
        Usage:
        Problems().getPopupControl()
        """
        return self.popupControl

    def getTableView(self):
        """
        Usage:
        Problems().getTableView()
        """
        return self.tableView

    def getNoProblems(self):
        """
        Usage:
        Problems().getNoProblems()
        """
        return self.noProblems

    def getPlaceholder(self):
        """
        Usage:
        Problems().getPlaceholder()
        """
        return self.placeholder


class Properties:
    """
    Class contains all real names from Problems
    """
    def __init__(self, name):
        """
        This consturctor has parameter name which represents the name of properties tab.
        @param name [string] name of the properties tab (e.g. "Device Properties")

        Usage:
        Properties("Device Properties").getTableView()
        """
        self.cTabItem = "{caption='" + name + "' parent.visible='true' type='org.eclipse.swt.custom.CTabItem' window=" + MainShell().getMainWindow() + "}"

    def getcTabItem(self):
        """
        Usage:
        Properties("Properties").getcTabItem()
        """
        return self.cTabItem

    def getTableView(self):
        """
        This getter returs the real name of properties table.

        Usage:
        Properties("Device Properties").getTableView()
        """
        return "{container=" + self.cTabItem + " id='propertiesTableView' styletype='root table-view' visible='true'}"

    def getField(self, fieldName):
        """
        This getter returns the real name of the cell from the 1st column (not zero column).

        Usage:
        Properties("Device Properties").getField("Path")
        """
        return "{container=" + self.getTableView() + " id='" + fieldName + "' styletype='text-input text-field' visible='true'}"


class ScriptEditor:
    """
    Class contains all real names from script editor window
    """

    def __init__(self, name):
        self.cTabItem = "{caption?='" + name + "' parent.visible='true' type='org.eclipse.swt.custom.CTabItem' window=" + MainShell().getMainWindow() + "}"
        self.styledText = "{container=" + self.cTabItem + " isvisible='true' type='org.eclipse.swt.custom.StyledText'}"

    def getScriptEditor(self):
        """
        Return real name of Script Editor window

        Usage:
        script = "test_script.py"
        ScriptEditor(script).getScriptEditor()
        """
        return self.styledText


class ScriptingConsole:
    """
    Class containsreal names for Scripting Console window
    """

    def __init__(self):
        self.cTabItem = "{caption='Scripting Console' parent.visible='true' type='org.eclipse.swt.custom.CTabItem' window=" + MainShell().getMainWindow() + "}"
        self.textArea = "{container=" + self.cTabItem + " styletype='root text-input text-area' visible='true'}"
        self.text = "{container=" + self.textArea + " styletype='text' visible='true'}"

    def getCTabItem(self):
        """
        Usage:
        ScriptingConsole().getCTabItem()
        """
        return self.cTabItem

    def getConsoleOutput(self):
        """
        Return output from console

        Usage:
        ScriptingConsole().getConsoleOutput()
        """
        return self.text

    def getConsoleArea(self):
        """
        Return real name from console area

        Usage:
        ScriptingConsole().getConsoleArea()
        """
        return self.textArea


class SaveRegisersStateShell:
    """Class contains all real names from Save Regisers State Shell"""
    def __init__(self):
        self.saveRegiserState = "{caption='Save Regisers State' isvisible='true' type='org.eclipse.swt.widgets.Shell'}"

    def getSaveButton(self):
        """
        Usage:
        SaveRegisersStateShell().getSaveButton()
        """
        return "{caption='Save' id='dialogButton' styletype='button scs-button' visible='true' window=" + self.saveRegiserState + "}"


class ContextMenuShell:
    """Class contains all real names from context menu shell."""

    def __init__(self):
        self.mainShell = "{type='com.cirrus.scs.ide.ui.javafx.controls.SCSContextMenu' visible='true'}"

    def getMainShell(self):
        return self.mainShell

    def getContextLabel(self, name):
        """
        This getter returns the real name of label from context menu shell.
        Usage:
        ContextMenuShell().getContextLabel("Copy")
        """
        return "{caption='" + name + "' container=" + self.mainShell + " styletype='label' visible='true'}"


class NewPluginProjectShell:
    """
    Class contains all real names of Plugin Panel Project Window
    """
    def __init__(self):
        self.newPluginProjectShell = "{caption='New Plugin Project' isvisible='true' type='org.eclipse.swt.widgets.Shell'}"
        self.projectNameTextBox = "{id='txtNewProjectName' styletype='text-input text-field scs-white-borded' visible='true' window=" + self.newPluginProjectShell + "}"
        self.projectDirectoryBox = "{id='txtDirectory' styletype='text-input text-field scs-white-borded' visible='true' window=" + self.newPluginProjectShell + "}"
        self.projectVersionBox = "{id='txtProjectVersion' styletype='text-input text-field scs-white-borded' visible='true' window=" + self.newPluginProjectShell + "}"
        self.listViewSys = "{id='listViewSystems' styletype='list-view scs-listview-dialog' visible='true' window=" + self.newPluginProjectShell + "}"
        self.listViewDev = "{id='listViewDevices' styletype='list-view scs-listview-dialog' visible='true' window=" + self.newPluginProjectShell + "}"

    def getNewPluginProject(self):
        """
        Usage:
        NewPluginProjectShell().getNewPluginProject()
        """
        return self.newPluginProjectShell

    def getProjectNameTextBox(self):
        """
        Usage:
        NewPluginProjectShell().getProjectNameTextBox()
        """
        return self.projectNameTextBox
    
    def getProjectVersionBox(self):
        """
        Usage:
        NewPluginProjectShell().getProjectVersionBox()
        """
        return self.projectVersionBox
    
    def getProjectPluginLvl(self, name):
        """
        Usage:
        NewPluginProjectShell().getProjectPluginLvl(name)
        """
        projectPluginLvl = "{caption='" + name + "' styletype='radio-button' visible='true' window=" + self.newPluginProjectShell + "}"
        return projectPluginLvl

    def getSupportedSys(self, name):
        """
        Usage:
        NewPluginProjectShell().getSupportedSys(name)
        """
        supportedSys = "{caption='" + name + "' container=" + self.listViewSys + " styletype='cell indexed-cell list-cell' visible='true'}"
        return supportedSys

    def getSupportedDev(self, name):
        """
        Usage:
        NewPluginProjectShell().getSupportedDev(name)
        """
        supportedDev = "{container={caption='' container={caption='" + name + "' container=" + self.listViewDev + " styletype='cell indexed-cell list-cell check-box-list-cell' visible='true'} styletype='check-box' visible='true'} styletype='mark' visible='true'}"
        return supportedDev

    def getProjectDirectoryBox(self):
        """
        Usage:
        NewPluginProjectShell().getProjectDirectoryBox()
        """
        return self.projectDirectoryBox

    def getButton(self, name):
        """
        @param name [string] name of the button

        Usage:
        NewPluginProjectShell().getButton()
        """
        button = "{caption='" + name + "' styletype='button scs-button' visible='true' window=" + self.newPluginProjectShell + "}"
        return button

    def getPluginProjectField(self, name):
        """
        Usage:
        NewPluginProjectShell().getPluginProjectField(name)
        """
        projectField = "{caption='" + name + "' container={container=" + Directory().getCTabItem() + " styletype='tree-view' visible='true'} styletype='cell indexed-cell tree-cell' visible='true'}"
        return projectField
