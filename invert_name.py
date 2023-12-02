import os

def modificar_nombres(ruta_directorio):
    # Iterar sobre los archivos en el directorio
    for nombre_archivo in os.listdir(ruta_directorio):
        ruta_archivo = os.path.join(ruta_directorio, nombre_archivo)      
        # Verificar si es un archivo MP3
        if nombre_archivo.endswith('.mp3'):
            nombre_archivo = nombre_archivo.replace('.mp3', '')
            # Obtener el nombre de la canción y del artista
            partes = nombre_archivo.split('-')
            if len(partes) == 2:
                cancion = partes[1].strip()
                artista = partes[0].strip()
                # Crear el nuevo nombre del archivo
                nuevo_nombre = f"{cancion} - {artista}.mp3"
                nueva_ruta = os.path.join(ruta_directorio, nuevo_nombre)
                
                # Renombrar el archivo
                os.rename(ruta_archivo, nueva_ruta)
                print(f"Archivo renombrado: {nombre_archivo} -> {nuevo_nombre}")

# Reemplaza esta ruta con la ruta real de tu directorio de música
ruta_musica = "C:\\Users\\WINDOWS10\\OneDrive\\Escritorio\\bachata"

# Llamada a la función para modificar nombres
modificar_nombres(ruta_musica)