from ResuableLibrary.reusablecodes import  reusable

News_tab = "(//*[@class='SiteMenuTab_TEMPO_SITE---nav_label'])[1]"
Task_tab = "(//*[@class='SiteMenuTab_TEMPO_SITE---nav_label'])[2]"
Records_tab = "(//*[@class='SiteMenuTab_TEMPO_SITE---nav_label'])[3]"
Reports_tab = "(//*[@class='SiteMenuTab_TEMPO_SITE---nav_label'])[4]"
Actions_tab = "(//*[@class='SiteMenuTab_TEMPO_SITE---nav_label'])[5]"


class homepage():

    def __init__(self, driver):
        self.driver = driver
        self.sharedfunction = reusable(driver)



    def clickActionTab(self):
        self.sharedfunction.clickobj(Actions_tab)