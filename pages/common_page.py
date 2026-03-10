from playwright.sync_api import Page, expect

class CommonPage:
    def __init__(self, page: Page):
        self.page = page
        self.voltar_para_home = page.get_by_role("link", name="Voltar para a Home")
        self.voltar_para_home_pix = page.get_by_role("button", name="Voltar para a Home")

    def assert_text(self, text):
        self.page.get_by_text(text).wait_for()
        expect(self.page.get_by_text(text)).to_be_visible()

    def assert_saldo_atual(self, saldo):
        expect(self.page.get_by_text(f"R$ {saldo}")).to_be_visible()
    
    def voltar_home(self):
        self.voltar_para_home_pix.click()
    
    def voltar_home_pix(self):
        self.voltar_para_home.click()
    