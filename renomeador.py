import os
import re
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox

def rename_photos():
    # Criar janela principal oculta
    root = tk.Tk()
    root.withdraw()
    
    # Pedir a pasta ao usuário
    folder = filedialog.askdirectory(title="Selecione a pasta com as fotos")
    if not folder:
        messagebox.showerror("Erro", "Nenhuma pasta selecionada!")
        return
    
    # Pedir o prefixo ao usuário
    new_prefix = simpledialog.askstring("Novo Prefixo", "Digite o novo prefixo para os arquivos:")
    if not new_prefix:
        messagebox.showerror("Erro", "Nenhum prefixo fornecido!")
        return
    
    # Regex para identificar o padrão dos arquivos (_GA_0000, etc.)
    pattern = re.compile(r"^(.*?)(\d{4})$")
    
    renamed_count = 0
    
    # Percorrer os arquivos na pasta
    for filename in os.listdir(folder):
        name, ext = os.path.splitext(filename)  # Separar nome e extensão
        match = pattern.match(name)
        
        if match:
            number = match.group(2)  # Pega os 4 dígitos finais
            new_name = f"{new_prefix}{number}{ext}"  # Novo nome
            old_path = os.path.join(folder, filename)
            new_path = os.path.join(folder, new_name)
            
            try:
                os.rename(old_path, new_path)
                renamed_count += 1
            except Exception as e:
                messagebox.showwarning("Erro ao renomear", f"Não foi possível renomear {filename}: {e}")
    
    messagebox.showinfo("Concluído", f"{renamed_count} arquivos foram renomeados com sucesso!")

if __name__ == "__main__":
    rename_photos()
