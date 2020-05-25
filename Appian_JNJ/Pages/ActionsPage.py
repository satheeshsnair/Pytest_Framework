from ResuableLibrary.reusablecodes import reusable

submitorder = "//a[contains(text(),'3PI Submit Order Request')]"


class actionspage():

    def __init__(self,driver):
        self.driver = driver
        self.sharedfunction = reusable(driver)

    def select_sumitorder(self):
        self.sharedfunction.clickobj(submitorder)