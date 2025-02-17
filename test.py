import os
import fitz  # PyMuPDF
from PIL import Image

def pdf_to_jpg(folder_path):
    # Проверяем, существует ли папка
    if not os.path.exists(folder_path):
        print(f"Папка '{folder_path}' не найдена.")
        return

    # Проходим по всем файлам в папке
    for file_name in os.listdir(folder_path):
        # Проверяем, является ли файл PDF
        if file_name.lower().endswith('.pdf'):
            pdf_path = os.path.join(folder_path, file_name)
            jpg_path = os.path.join(folder_path, file_name.replace('.pdf', '.jpg'))

            try:
                # Открываем PDF
                pdf_document = fitz.open(pdf_path)
                # Получаем первую страницу
                page = pdf_document[0]
                # Конвертируем страницу в изображение
                pix = page.get_pixmap()
                # Сохраняем изображение как JPG
                img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
                img.save(jpg_path, "JPEG")
                print(f"Сохранено: {jpg_path}")
                pdf_document.close()
            except Exception as e:
                print(f"Ошибка при обработке файла {pdf_path}: {e}")

# Укажите путь к папке
folder_path = r"D:\BooksConvert"
pdf_to_jpg(folder_path)