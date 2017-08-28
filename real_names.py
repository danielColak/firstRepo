class Welcome:
    """
    The class Welcome contains all real names of buttons, fields and hyperlinks from Welcome Screen. With Welcome.nameOfGetMethod() we call them.
    """
    def __init__(self):
        self.welcomeWindow = "{caption='' isvisible='true' type='org.eclipse.swt.widgets.Shell'}"
        self.devicePanelProjectHyperlink = "{caption='Divajs' id='devicePanelWizardLink' styletype='hyperlink' visible='true' window=" + self.welcomeWindow + "}"
        self.systemPanelProjectHyperlink = "{caption='System' id='systemPanelWizardLink' styletype='hyperlink' visible='true' window=" + self.welcomeWindow + "}"
        self.libraryProjectHyperlink = "{caption='Library Project' id='libraryPanelWizardLink' styletype='hyperlink' visible='true' window=" + self.welcomeWindow + "}"
        self.devicePanelProjectHyperlinkLink = "{caption='Device Panel Project' container=" + self.devicePanelProjectHyperlink + " styletype='text' visible='true'}"
        self.systemPanelProjectHyperlinkLink = "{caption='System Panel Project' container=" + self.systemPanelProjectHyperlink + " styletype='text' visible='true'}"
        self.libraryProjectHyperlinkLink = "{caption='Library Project' container=" + self.libraryProjectHyperlink + " styletype='text' visible='true'}"
        self.installPackageHyperlink = "{caption='Install Package' id='installPackage' styletype='hyperlink hyperlinkWelcomeWhite' visible='true' window=" + self.welcomeWindow + "}"
        self.installPackageHyperlinkLink = "{caption='Install Package' container=" + self.welcomeWindow + " styletype='text' visible='true'}"
        self.noInstallPackageLabel = "{caption='NO INSTALLED PACKAGES' id='noInstalledPackage' styletype='scs-label-package-error scs-label-package-error' visible='true' window= " + self.welcomeWindow + "}"
        self.closeWelcome = "{caption='X' styletype='label scs-closeLabel' visible='true' window=" + self.welcomeWindow + "}"
        self.confirmShell = "{caption='' isvisible='true' type='org.eclipse.swt.widgets.Shell'}"
        self.confirmCheckBox = "{caption='Don\\'t show again' styletype='check-box' visible='true' window=" + self.confirmShell + "}"
        self.markConfirmCheckBox = "{container=" + self.confirmCheckBox + " styletype='mark' visible='true'}"
        self.confirmWindowLeftSection = "{styletype='-scs-common-gray' visible='true' window=" + self.confirmShell + "}"
        self.confirmWindowGridPane = "{type='javafx.scene.layout.GridPane' visible='true' window=" + self.confirmShell + "}"
        self.closeWelcomeLabel = "{caption='X' container=" + self.closeWelcome + " styletype='text' visible='true'}"
        self.welcomeImage = "{id='welcomeTitle' styletype='image-view' visible='true' window=" + self.welcomeWindow + "}"
        self.perspectiveComboBox = "{id='perspectiveComboBox' styletype='combo-box-base combo-box' visible='true' window=" + self.welcomeWindow + "}"
        self.recentProjectsListView = "{id='recentProjectsListView' styletype='list-view' visible='true' window=" + self.welcomeWindow + "}"
        self.welcomeCheckBox = "{caption='Always show at startup' id='alwaysShowOnStartupCheckbox' styletype='check-box white-check-box' visible='true' window=" + self.welcomeWindow + "}"
        self.recentProject = "{container=" + self.recentProjectsListView + " styletype='cell indexed-cell list-cell' visible='true'}"
