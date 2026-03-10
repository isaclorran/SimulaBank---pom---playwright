from playwright.sync_api import Page, expect

class HomePage:
    def __init__(self, page: Page):
        self.page = page
    
    def acessar_menu(self, menu):
        self.page.get_by_text(menu).click()
    

        
