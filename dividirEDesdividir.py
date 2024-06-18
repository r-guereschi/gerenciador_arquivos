# import tkinter as tk
# from tkinter import filedialog, simpledialog, messagebox
# import os
# import shutil

# def select_folder():
#     folder_selected = filedialog.askdirectory()
#     return folder_selected

# def create_subfolders(main_folder, photos_per_folder):
#     photo_files = sorted([f for f in os.listdir(main_folder) if f.endswith(('jpg', 'jpeg', 'png'))])
#     num_photos = len(photo_files)
    
#     if num_photos == 0:
#         messagebox.showerror("Erro", "A pasta selecionada não contém fotos.")
#         return
    
#     num_subfolders = (num_photos + photos_per_folder - 1) // photos_per_folder  # Calcula o número de subpastas necessárias
    
#     start_idx = 0
#     for i in range(num_subfolders):
#         subfolder_path = os.path.join(main_folder, f'subpasta_{i+1}')
#         os.makedirs(subfolder_path, exist_ok=True)
        
#         end_idx = start_idx + photos_per_folder
#         for photo in photo_files[start_idx:end_idx]:
#             shutil.move(os.path.join(main_folder, photo), os.path.join(subfolder_path, photo))
        
#         start_idx = end_idx
    
#     messagebox.showinfo("Sucesso", f"Fotos divididas em {num_subfolders} subpastas.")

# def move_photos_and_delete_subfolders(main_folder):
#     subfolders = [f.path for f in os.scandir(main_folder) if f.is_dir()]
    
#     if not subfolders:
#         messagebox.showinfo("Info", "Não há subpastas na pasta selecionada.")
#         return
    
#     for subfolder in subfolders:
#         for item in os.listdir(subfolder):
#             item_path = os.path.join(subfolder, item)
#             if os.path.isfile(item_path) and item.lower().endswith(('jpg', 'jpeg', 'png')):
#                 shutil.move(item_path, main_folder)
        
#         # Apagar a subpasta vazia
#         os.rmdir(subfolder)
    
#     messagebox.showinfo("Sucesso", "Fotos movidas e subpastas apagadas.")

# def main():
#     def on_submit():
#         action = action_var.get()
#         main_folder = select_folder()
#         if not main_folder:
#             return
        
#         if action == 'dividir':
#             photos_per_folder = simpledialog.askinteger("Input", "Quantas fotos você deseja por subpasta?")
#             if not photos_per_folder:
#                 return
#             create_subfolders(main_folder, photos_per_folder)
#         elif action == 'remover':
#             move_photos_and_delete_subfolders(main_folder)
#         else:
#             messagebox.showerror("Erro", "Ação desconhecida. Por favor, selecione uma ação válida.")

#     root = tk.Tk()
#     root.title("Escolha a Ação")
    
#     action_var = tk.StringVar(value="dividir")

#     tk.Label(root, text="Escolha a Ação:").pack()

#     tk.Radiobutton(root, text="Dividir Fotos em Subpastas", variable=action_var, value="dividir").pack(anchor="w")
#     tk.Radiobutton(root, text="Remover Subpastas e Mover Fotos", variable=action_var, value="remover").pack(anchor="w")

#     tk.Button(root, text="Submit", command=on_submit).pack()

#     root.mainloop()

# if __name__ == "__main__":
#     main()
