import tkinter as tk
import rsa
import binascii


# MOTOR CRIPTOGRÁFICO

chave_publica, chave_privada = rsa.newkeys(512)
mensagem_criptografada_bytes = b""

def criptografar():
    global mensagem_criptografada_bytes
    texto_original = entrada_mensagem.get()
    
    if not texto_original:
        return
        
    mensagem_criptografada_bytes = rsa.encrypt(texto_original.encode('utf-8'), chave_publica)
    texto_hex = binascii.hexlify(mensagem_criptografada_bytes).decode('utf-8')
    
    texto_transito.config(state=tk.NORMAL)
    texto_transito.delete(1.0, tk.END)
    texto_transito.insert(tk.END, texto_hex)
    texto_transito.config(state=tk.DISABLED)
    
    entrada_mensagem.delete(0, tk.END)
    btn_descriptografar.config(state=tk.NORMAL)
    label_resultado.config(text="Status: Criptograma recebido. Aguardando chave...", fg="orange")

def descriptografar():
    global mensagem_criptografada_bytes
    
    try:
        texto_descriptografado = rsa.decrypt(mensagem_criptografada_bytes, chave_privada).decode('utf-8')
        label_resultado.config(text=f"Mensagem Destrancada:\n{texto_descriptografado}", fg="green")
        btn_descriptografar.config(state=tk.DISABLED)
    except Exception:
        label_resultado.config(text="Erro: Chave incorreta.", fg="red")


# TKINTER

root = tk.Tk()
root.title("Simulador Didático de Criptografia")
root.geometry("600x800") 
root.configure(padx=20, pady=20)

# --- FASE 1: REMETENTE ---
frame_fase1 = tk.LabelFrame(root, text=" Fase 1: Remetente (Mensagem Original) ", padx=15, pady=10, font=("Arial", 10, "bold"))
frame_fase1.pack(fill="x", pady=5)

texto_explicativo_fase1 = "O Porquê: Representa o dispositivo emissor (ex: celular do aluno). Aqui digita-se o 'Texto Claro'. Ao clicar no botão, a Chave Pública do destinatário atuará como um cadeado para trancar matematicamente esta mensagem."
tk.Label(frame_fase1, text=texto_explicativo_fase1, justify="left", wraplength=520, fg="#444444", font=("Arial", 9, "italic")).pack(anchor="w", pady=(0, 10))

tk.Label(frame_fase1, text="Digite o segredo:").pack(anchor="w")
entrada_mensagem = tk.Entry(frame_fase1, width=55, font=("Arial", 11))
entrada_mensagem.pack(pady=5)

btn_criptografar = tk.Button(frame_fase1, text="Criptografar (Usar Chave Pública 🔒)", command=criptografar, bg="#d9edf7", font=("Arial", 10, "bold"))
btn_criptografar.pack(pady=5)

# --- FASE 2: TRÂNSITO NA INTERNET ---
frame_fase2 = tk.LabelFrame(root, text=" Fase 2: Trânsito na Internet (Criptografado) ", padx=15, pady=10, font=("Arial", 10, "bold"))
frame_fase2.pack(fill="x", pady=10)

texto_explicativo_fase2 = "O Porquê: Representa a 'rua' da internet (provedores, servidores, cabos). A mensagem viaja protegida. Se um invasor interceptar a rede, ele verá apenas o código ilegível abaixo e não conseguirá reverter sem a Chave Privada."
tk.Label(frame_fase2, text=texto_explicativo_fase2, justify="left", wraplength=520, fg="#444444", font=("Arial", 9, "italic")).pack(anchor="w", pady=(0, 10))

texto_transito = tk.Text(frame_fase2, height=4, width=55, bg="#2b2b2b", fg="#00ff00", font=("Consolas", 9), wrap=tk.WORD)
texto_transito.pack(pady=5)
texto_transito.insert(tk.END, "[Nenhuma mensagem trafegando]")
texto_transito.config(state=tk.DISABLED)

# --- FASE 3: DESTINATÁRIO ---
frame_fase3 = tk.LabelFrame(root, text=" Fase 3: Destinatário ", padx=15, pady=10, font=("Arial", 10, "bold"))
frame_fase3.pack(fill="both", expand=True, pady=5)

texto_explicativo_fase3 = "O Porquê: Representa o dispositivo receptor. É o ÚNICO lugar do universo onde existe a Chave Privada. Ela é responsável por resolver a equação matemática do arquivo, destrancar o cadeado e revelar o texto em sua forma original."
tk.Label(frame_fase3, text=texto_explicativo_fase3, justify="left", wraplength=520, fg="#444444", font=("Arial", 9, "italic")).pack(anchor="w", pady=(0, 10))

btn_descriptografar = tk.Button(frame_fase3, text="Descriptografar (Usar Chave Privada 🔑)", command=descriptografar, bg="#dff0d8", font=("Arial", 10, "bold"), state=tk.DISABLED)
btn_descriptografar.pack(pady=5)

label_resultado = tk.Label(frame_fase3, text="Status: Aguardando...", font=("Arial", 12, "bold"), fg="gray")
label_resultado.pack(pady=10)


# DIREITOS AUTORAIS

texto_rodape = "Desenvolvido por Nelson Carvalho (Nordic-Tech) © 2026 - Todos os direitos reservados."
rodape = tk.Label(root, text=texto_rodape, fg="#888888", font=("Arial", 9))
rodape.pack(side=tk.BOTTOM, pady=(10, 0))

root.mainloop()