import json
import cv2

img = cv2.imread(f"{input('Introduce el nombre del archivo: ')}.png",3)
def reorderRGB(img_array):
    lista = []
    for i in range(16):
        for j in range(16):
            img_array[i][j][0], img_array[i][j][2] = img_array[i][j][2], img_array[i][j][0]
            lista.append(img_array[i][j])

    njson = {
        "array":lista
    }
    with open("img.json","w") as file:
        json.dump(njson, file)

njson = {"array":img.tolist()}
reorderRGB(njson["array"])
print("\narchivo img.json creado")
