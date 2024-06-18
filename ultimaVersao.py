import os
import re
import shutil
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox

def select_folder():
    folder_selected = filedialog.askdirectory()
    return folder_selected

def rename_photos(main_folder, new_prefix):
    photo_files = sorted([f for f in os.listdir(main_folder) if f.endswith(('jpg', 'jpeg', 'png'))])
    renamed_files = []
    
    for photo in photo_files:
        match = re.search(r'\d+', photo)
        if match:
            numeric_part = match.group()
            new_name = f"{new_prefix}{numeric_part}{os.path.splitext(photo)[1]}"
            os.rename(os.path.join(main_folder, photo), os.path.join(main_folder, new_name))
            renamed_files.append(new_name)
    
    return renamed_files

def create_subfolders(main_folder, photos_per_folder):
    photo_files = sorted([f for f in os.listdir(main_folder) if f.endswith(('jpg', 'jpeg', 'png'))])
    num_photos = len(photo_files)
    
    if num_photos == 0:
        messagebox.showerror("Erro", "A pasta selecionada não contém fotos.")
        return
    
    num_subfolders = (num_photos + photos_per_folder - 1) // photos_per_folder
    
    start_idx = 0
    for i in range(num_subfolders):
        subfolder_path = os.path.join(main_folder, f'subpasta_{i+1}')
        os.makedirs(subfolder_path, exist_ok=True)
        
        end_idx = start_idx + photos_per_folder
        for photo in photo_files[start_idx:end_idx]:
            shutil.move(os.path.join(main_folder, photo), os.path.join(subfolder_path, photo))
        
        start_idx = end_idx
    
    messagebox.showinfo("Sucesso", f"Fotos divididas em {num_subfolders} subpastas.")

def move_photos_and_delete_subfolders(main_folder):
    subfolders = [f.path for f in os.scandir(main_folder) if f.is_dir()]
    
    if not subfolders:
        messagebox.showinfo("Info", "Não há subpastas na pasta selecionada.")
        return
    
    for subfolder in subfolders:
        for item in os.listdir(subfolder):
            item_path = os.path.join(subfolder, item)
            if os.path.isfile(item_path) and item.lower().endswith(('jpg', 'jpeg', 'png')):
                shutil.move(item_path, main_folder)
        
        os.rmdir(subfolder)
    
    messagebox.showinfo("Sucesso", "Fotos movidas e subpastas apagadas.")

def on_rename():
    main_folder = select_folder()
    if not main_folder:
        return
    
    new_prefix = simpledialog.askstring("Input", "Digite o novo prefixo para os arquivos de foto:")
    if not new_prefix:
        return
    
    renamed_files = rename_photos(main_folder, new_prefix)
    if renamed_files:
        messagebox.showinfo("Sucesso", f"Arquivos renomeados com o prefixo '{new_prefix}'.")
    else:
        messagebox.showerror("Erro", "Nenhuma foto encontrada na pasta selecionada.")

def on_divide():
    main_folder = select_folder()
    if not main_folder:
        return
    
    photos_per_folder = simpledialog.askinteger("Input", "Quantas fotos você deseja por subpasta?")
    if not photos_per_folder:
        return
    
    create_subfolders(main_folder, photos_per_folder)

def on_move():
    main_folder = select_folder()
    if not main_folder:
        return
    
    move_photos_and_delete_subfolders(main_folder)

def main():
    root = tk.Tk()
    root.title("Gerenciador de Fotos")
    root.geometry("400x400")
    root.configure(bg='white')

    title_label = tk.Label(root, text="Gerenciador de Fotos", bg='white', fg='black', font=('Helvetica', 18, 'bold'))
    title_label.pack(pady=20)

    button_style = {'bg': 'black', 'fg': 'white', 'font': ('Helvetica', 12, 'bold'), 'padx': 20, 'pady': 10}

    tk.Button(root, text="Renomear Fotos", command=on_rename, **button_style).pack(pady=10)
    tk.Button(root, text="Dividir Fotos em Subpastas", command=on_divide, **button_style).pack(pady=10)
    tk.Button(root, text="Remover Subpastas e Mover Fotos", command=on_move, **button_style).pack(pady=10)
    
    footer_label = tk.Label(root, text="@r.guereschi_", bg='white', fg='black', font=('Helvetica', 10))
    footer_label.pack(side=tk.BOTTOM, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
