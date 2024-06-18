# import tkinter as tk
# from tkinter import filedialog, simpledialog, messagebox
# import os
# import re

# def select_folder():
#     folder_selected = filedialog.askdirectory()
#     return folder_selected

# def rename_photos(main_folder, new_prefix):
#     photo_files = sorted([f for f in os.listdir(main_folder) if f.endswith(('jpg', 'jpeg', 'png'))])
#     renamed_files = []
    
#     for photo in photo_files:
#         match = re.search(r'\d+', photo)
#         if match:
#             numeric_part = match.group()
#             new_name = f"{new_prefix}{numeric_part}{os.path.splitext(photo)[1]}"
#             os.rename(os.path.join(main_folder, photo), os.path.join(main_folder, new_name))
#             renamed_files.append(new_name)
    
#     return renamed_files

# def main():
#     root = tk.Tk()
#     root.withdraw()  # Esconde a janela principal do Tkinter
    
#     main_folder = select_folder()
#     if not main_folder:
#         messagebox.showerror("Erro", "Nenhuma pasta selecionada.")
#         return
    
#     new_prefix = simpledialog.askstring("Input", "Digite o novo prefixo para os arquivos de foto:")
#     if not new_prefix:
#         messagebox.showerror("Erro", "Nenhum prefixo fornecido.")
#         return
    
#     renamed_files = rename_photos(main_folder, new_prefix)
#     if renamed_files:
#         messagebox.showinfo("Sucesso", f"Arquivos renomeados com o prefixo '{new_prefix}'.")
#     else:
#         messagebox.showerror("Erro", "Nenhuma foto encontrada na pasta selecionada.")

# if __name__ == "__main__":
#     main()
