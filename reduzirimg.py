from PIL import Image
import os
import shutil

# Diretório raiz onde as pastas com as imagens estão localizadas
root_directory = 'E:\\imgrodobens'

# Diretório raiz para salvar as imagens reduzidas mantendo a estrutura
output_root_directory = 'E:\\novasimg'

# Percorre todas as pastas dentro do diretório raiz
for folder_name in os.listdir(root_directory):
    folder_path = os.path.join(root_directory, folder_name)
    
    # Verifica se o item na pasta é realmente uma pasta
    if os.path.isdir(folder_path):
        # Cria um diretório correspondente no diretório de saída
        output_folder_path = os.path.join(output_root_directory, folder_name)
        os.makedirs(output_folder_path, exist_ok=True)
        
        # Percorre todas as imagens dentro da pasta
        for image_file in os.listdir(folder_path):
            # Verifica se o arquivo é uma imagem suportada (por extensão)
            if image_file.lower().endswith(('.png', '.jpg', '.jpeg')):
                # Abre a imagem usando PIL
                img_path = os.path.join(folder_path, image_file)
                img = Image.open(img_path)

                # Obtém as dimensões da imagem original
                original_width, original_height = img.size

                # Calcula a altura do corte em 10% da altura original
                cut_height = int(original_height * 0.1)

                # Define as coordenadas para o corte
                left = 0
                upper = cut_height
                right = original_width
                lower = original_height - cut_height

                # Corta a imagem
                cropped_img = img.crop((left, upper, right, lower))

                # Salva a imagem cortada no diretório de saída
                output_path = os.path.join(output_folder_path, image_file)
                cropped_img.save(output_path)

                print(f'Imagem {image_file} cortada em 10% na parte superior e inferior e salva como {output_path}')
for folder_name in os.listdir(root_directory):
    folder_path = os.path.join(root_directory, folder_name)
    
    # Verifica se o item na pasta é realmente uma pasta
    if os.path.isdir(folder_path):
        # Cria um diretório correspondente no diretório de saída
        output_folder_path = os.path.join(output_root_directory, folder_name)
        os.makedirs(output_folder_path, exist_ok=True)
        
        # Percorre todos os arquivos dentro da pasta
        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)
            output_file_path = os.path.join(output_folder_path, "laudo_14.pdf")

            # Verifica se o arquivo é um PDF
            if file_name.lower().endswith('.pdf'):
                # Move o arquivo para o diretório de saída com o novo nome
                shutil.copy(file_path, output_file_path)
                print(f'Arquivo {file_name} movido para {output_file_path}')

print('Processo concluído.')
print('Processo concluído.')