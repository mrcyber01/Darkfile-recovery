import time
import sys

# Função para exibir o aviso de segurança
def exibir_aviso():
    print("\n** ATENÇÃO: UTILIZAÇÃO DE FERRAMENTA - DARKFILE RECOVERY **")
    print("\nVocê está prestes a utilizar **DarkFile Recovery**, uma ferramenta de recuperação avançada de arquivos.")
    time.sleep(2)
    print("\nAVISOS IMPORTANTES:")
    print("\n1. **Não interrompa o processo:** Durante o uso da ferramenta, nunca desconecte o cabo de alimentação ou cabo USB de seu dispositivo. Isso pode resultar em danos permanentes aos dados e até danificar o sistema operacional.")
    time.sleep(4)
    print("\n2. **Utilização de dispositivos adequados:** Se você estiver utilizando um dispositivo móvel, recomendamos o uso de um adaptador OTG para garantir que a ferramenta funcione corretamente.")
    time.sleep(4)
    print("\n3. **Risco de corrupção de dados:** Não garantimos 100% de sucesso em todos os casos. Dependendo da integridade dos dados ou da complexidade da recuperação, alguns arquivos podem não ser recuperados corretamente.")
    time.sleep(4)
    print("\n4. **Responsabilidade do usuário:** A utilização da **DarkFile Recovery** é de total responsabilidade do usuário. Recomendamos que faça backups regulares de seus dados antes de utilizar qualquer ferramenta de recuperação.")
    time.sleep(4)
    print("\n5. **Uso restrito:** A ferramenta foi desenvolvida para uso pessoal e não é recomendada para redes corporativas. O uso inadequado pode comprometer dados sensíveis.")
    time.sleep(4)

    print("\n**Atenção:**")
    print("\nDevido à alta demanda e à complexidade das operações realizadas, a ferramenta agora é paga.")
    print("\nO valor é de **R$ 150** para liberar a ferramenta completa e garantir o acesso imediato a todas as funcionalidades.")
    print("\nPara efetuar o pagamento, entre em contato conosco no Telegram. Aceitamos qualquer tipo de pagamento: Ethereum, Bitcoin, Pix, Dólar ou Euro.")
    print("\nNosso suporte está disponível 24 horas por dia. Envie uma mensagem para nosso Telegram para receber os detalhes de pagamento e iniciar o processo.")
    print("\nTelegram: @brunooliv123")
    print("\nApós o pagamento, enviaremos a liberação imediata da ferramenta.")
    
    # Novo aviso sobre o tempo de recuperação
    print("\n**Importante:** Dependendo do tamanho e da quantidade de arquivos no seu dispositivo, o processo de recuperação pode levar algumas horas ou até um dia inteiro para ser concluído. Esteja ciente de que quanto maior o volume de dados, maior o tempo de processamento.")

# Função para exibir o menu de opções
def exibir_menu():
    print("\n** Bem-vindo à DarkFile Recovery **")
    print("\nEscolha uma das opções abaixo para continuar:")
    print("1 - Criar Arquivos")
    print("2 - Excluir Arquivos")
    print("3 - Recuperar Arquivos")

    opcao = input("\nDigite o número da opção: ")
    
    if opcao not in ['1', '2', '3']:
        print("\nOpção inválida! Por favor, selecione uma opção válida.")
        return

    # Quando o usuário escolhe uma opção, mostramos as informações sobre o pagamento e o suporte.
    print("\n** Atenção: Pagamento necessário para liberar a ferramenta **")
    print("\nPara continuar, você precisa realizar um pagamento de R$ 150.")
    print("\nApós o pagamento, entre em contato conosco pelo nosso canal no Telegram para liberar o acesso.")
    print("\n** Link para pagamento:**")
    print("Entre em contato conosco no Telegram para que possamos enviar as instruções de pagamento.")
    print("\nAceitamos as seguintes formas de pagamento:")
    print("- Ethereum")
    print("- Bitcoin")
    print("- Pix")
    print("- Dólar")
    print("- Euro")

    print("\nNosso suporte está disponível 24 horas por dia no Telegram.")
    print("\nEntre em contato com a nossa equipe ou com um dos nossos colegas de trabalho através do Telegram: @brunooliv123")

    # Não é necessário pressionar ENTER, apenas instruímos a entrar em contato via Telegram
    print("\nEntre em contato com a nossa equipe no Telegram para continuar o processo.")

# Função principal
def main():
    exibir_aviso()

    while True:
        exibir_menu()
        continuar = input("\nDeseja realizar outra ação? (s/n): ").lower()
        if continuar != 's':
            print("\nObrigado por usar a DarkFile Recovery! Tenha um bom dia!")
            break

if __name__ == "__main__":
    main()
