from PIL import Image
import os

downloadsFolder = "C:\\Users\\WINDOWS10\\Downloads\\"
savesFolder = "C:\\Users\\WINDOWS10\\OneDrive\\Imágenes\\"


for filename in os.listdir(downloadsFolder):
    name, extension = os.path.splitext(filename)

    if extension.lower() in [".jpg", ".jpeg", ".png"]:
        full_path = os.path.join(downloadsFolder, filename)
        picture = Image.open(full_path)

        # Convertir la imagen a modo RGB si no está en ese modo
        if picture.mode != 'RGB':
            picture = picture.convert('RGB')

        # Construir el nombre del archivo comprimido
        compressed_filename = os.path.join(savesFolder, "compressed_" + name + ".jpg")

        # Guardar la imagen comprimida en formato JPEG
        picture.save(compressed_filename, optimize=True, quality=60)

        os.remove(downloadsFolder + filename)

        # Imprimir un mensaje indicando que la imagen fue comprimida y guardada
        print("Imagen comprimida y guardada:", filename)
