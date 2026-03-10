def test_005_pix_acima_do_limite(common_page, login_page, home_page, pix_page) -> None:
    login_page.login("user1", "pass1")
    home_page.acessar_menu("Fazer Pix")
    pix_page.fazer_pix("999.999.999-99", "3001,00")
    common_page.assert_text("O valor do Pix não pode ultrapassar R$ 3.000,00. Tente novamente.")
    common_page.voltar_home_pix()
    common_page.assert_saldo_atual("5.000,00")

                                  
