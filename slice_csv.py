def dividir_arquivo(caminho_arquivo, tamanho_parte):
    try:
        with open(caminho_arquivo, 'rb') as arquivo:
            contador_parte = 1
            while True:
                parte = arquivo.read(tamanho_parte)
                if not parte:
                    break
                nome_parte = f"{caminho_arquivo}_parte_{contador_parte}"
                with open(nome_parte, 'wb') as arquivo_parte:
                    arquivo_parte.write(parte)
                print(f"Parte {contador_parte} salva como '{nome_parte}'")
                contador_parte += 1
        print("Divisão concluída com sucesso.")
    except FileNotFoundError:
        print("Erro: Arquivo não encontrado.")
    except Exception as e:
        print(f"Erro: {e}")
 
# Exemplo de uso
caminho_arquivo = 'ratings.csv'  # Substitua pelo caminho do arquivo original
tamanho_parte = 100 * 1024 * 1024  # Tamanho em bytes (1 MB neste exemplo)
 
dividir_arquivo(caminho_arquivo, tamanho_parte)