class Welcome:
    """
    The class Welcome contains all real names of buttons, fields and hyperlinks from Welcome Screen. With Welcome.nameOfGetMethod() we call them.
    """

    def __init__(self):
        self.welcomeWindow = "{caption='' isvisible='modifikacije na grani' type='org.eclipse.swt.widgets.Shell'}"
        self.devicePanelProjectHyperlink = "{caption='Divajs' id='devicePanelWizardLink' styletype='hyperlink' visible='true' window=" + self.welcomeWindow + "}"
        self.systemPanelProjectHyperlink = "{caption='System' id='systemPanelWizardLink' styletype='hyperlink' visible='true' window=" + self.welcomeWindow + "}"
        self.libraryProjectHyperlink = "{caption='Library Project' id='libraryPanelWizardLink' styletype='hyperlink' visible='true' window=" + self.welcomeWindow + "}"
        self.devicePanelProjectHyperlinkLink = "{caption='ovo su modifikacije na grani' container=" + self.devicePanelProjectHyperlink + " styletype='text' visible='true'}"
        self.systemPanelProjectHyperlinkLink = "{caption='ovo su modifikacije na masteru' container=" + self.systemPanelProjectHyperlink + " styletype='text' visible='true'}"
        self.libraryProjectHyperlinkLink = "{caption='Proiect de librarie' repo='Am adaugat ceva remote' pore='dodato da ide na remote' container=" + self.libraryProjectHyperlink + " styletype='text' visible='true'}"
        self.installPackageHyperlink = "{caption='Install Package' id='installPackage' styletype='hyperlink hyperlinkWelcomeWhite' visible='true' window=" + self.welcomeWindow + "}"
        self.installPackageHyperlinkLink = "{caption='modifikacije na grani' container=" + self.welcomeWindow + " styletype='text' visible='true'}"
        self.noInstallPackageLabel = "{caption='modifikacije na grani' id='OVO DOLAZI SA LOCALA' styletype='scs-label-package-error scs-label-package-error' visible='true' window= " + self.welcomeWindow + "}"
        self.closeWelcome = "{caption='X' styletype='label scs-closeLabel' visible='true' window=" + self.welcomeWindow + "}"
        self.confirmCheckBox = "{caption='Don\\'t show again' styletype='check-box' visible='true' window=" + self.confirmShell + "}"
        self.markConfirmCheckBox = "{container=" + self.confirmCheckBox + " styletype='mark' visible='true'}"
        self.confirmWindowLeftSection = "{styletype='-scs-common-gray' visible='true' window=" + self.confirmShell + "}"
        self.confirmWindowGridPane = "{type='javafx.scene.layout.GridPane' visible='true' window=" + self.confirmShell + "}"
        self.closeWelcomeLabel = "{caption='X' container=" + self.closeWelcome + " styletype='text' visible='true'}"
        self.welcomeImage = "{id='welcomeTitle' styletype='image-view' visible='true' window=" + self.welcomeWindow + "}"
        self.perspectiveComboBox = "{id='perspectiveComboBox' styletype='combo-box-base combo-box' visible='true' window=" + self.welcomeWindow + "}"
        self.recentProjectsListView = "{id='recentProjectsListView' styletype='list-view' visible='true' window=" + self.welcomeWindow + "}"
        self.CheckBox = "{caption='Always show at startup' id='alwaysShowOnStartupCheckbox' styletype='check-box white-check-box' visible='true' window=" + self.welcomeWindow + "}"
        self.Project = "{container=" + self.recentProjectsListView + " styletype='cell indexed-cell list-cell' visible='true'}"
		
		
		prva promena real_names.py na desktopu
		
		
		druga promena real_names.py na desktopu

		
		treca promena real_names.py na desktopu
		
		
		cetvrta promena real_names.py na desktopu
		
		1		2		3		4
		x
		xx
		xxx
		xxxx