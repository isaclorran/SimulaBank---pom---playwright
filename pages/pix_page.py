from playwright.sync_api import Page, expect

class PixPage:
    def __init__(self, page: Page):
        self.page = page
        self.chave_pix = page.get_by_role("textbox", name="Chave Pix:")
        self.valor_pix = page.get_by_role("textbox", name="Valor:")
        self.enviar_pix_button = page.get_by_role("button", name="Enviar Pix")
        self.voltar_para_home = page.get_by_role("button", name="Voltar para a Home")
    
    def fazer_pix(self, chave, valor):
        self.chave_pix.wait_for()
        self.chave_pix.fill(chave)
        self.valor_pix.fill(valor)
        self.enviar_pix_button.click()

    def assert_pix_realizado(self):
        #expect(self.page.get_by_text("Transação realizada com sucesso")).to_be_visible()
        expect(self.page.get_by_text("A transação foi concluída com sucesso. Você pode voltar para a página principal e continuar suas operações.")).to_be_visible()

  
    