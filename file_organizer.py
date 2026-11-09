from pathlib import Path
import shutil
folder = Path(__file__).parent / "test_files"
pdf_count = 0
jpg_count = 0
txt_count = 0 
zip_count = 0
exe_count = 0
other_count = 0
total_count = 0

print("Python ищет папку здесь:")
print(folder)

if folder.exists():
    documents = folder / "Documents"
    documents.mkdir(exist_ok = True)
    images = folder / "Images"
    images.mkdir(exist_ok = True)
    archives = folder / "Archives"
    archives.mkdir(exist_ok = True)
    files = list(folder.iterdir())
    applications = folder / "Applications"
    applications.mkdir(exist_ok = True)
    others = folder / "Others"
    others.mkdir(exist_ok = True)

    print("Найденные файлы")
    for file in files:
        if file.is_file():
            
            if file.suffix == ".pdf":
                pdf_count += 1 
            elif file.suffix == ".txt":
                txt_count += 1
            elif file.suffix in [".jpg", ".png", ".jpeg", ".webp"]:
                jpg_count += 1  
            elif file.suffix == ".zip":
                zip_count += 1
            elif file.suffix == ".exe":
                exe_count += 1
            else:
                other_count += 1


            if file.suffix in[ ".pdf", ".txt"]:
                shutil.move(file, documents)

            elif file.suffix in [".jpg",".png", ".jpeg" , ".webp"]:
                shutil.move(file, images)

            elif file.suffix == ".zip":
                shutil.move(file, archives)

            elif file.suffix == ".exe":
                shutil.move(file,applications)
            else:
                shutil.move(file,others)


            print("Название", file.name)
            print("Расширение", file.suffix)
            print("-------------")
    total_count = pdf_count + jpg_count + txt_count + zip_count + exe_count + other_count
    print("===================")
    print("        ОТЧЕТ")
    print("===================")
    print("pdf Файлов" , pdf_count)
    print('jpg Файлов', jpg_count)
    print("txt Файлов" , txt_count)
    print('zip Файлов', zip_count)
    print('exe Файлов', exe_count)
    print("другие файлы", other_count)  
    print("Всего обработано файлов", total_count)
else:
    print("Папка не найдена")
