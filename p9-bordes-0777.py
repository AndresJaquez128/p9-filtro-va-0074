#Para lhombres el ejemplo 2 ( del 1 al 30 )  y/o  el ejemplo 3 (31 al 60)
#COCODRILO IMAGEN 31
# JAQUEZ CAMACHO JOEL ANDRES 0074 
import cv2

# Cargar imagen

imagen = cv2.imread("C:\IA_Gpo3H\VA_0074\p9-filtro-va-0074\Original-cocodrilo1-0074.jpg")
# Comprobar imagen
if imagen is None:
    print("Error: no se pudo cargar la imagen.")
    exit()

# Convertir a escala de grises
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Convertir a imagen binaria mediante umbral
_, binaria = cv2.threshold(
    gris,
    127,
    255,
    cv2.THRESH_BINARY
)

# Detectar contornos
contornos, jerarquia = cv2.findContours(
    binaria,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

# Dibujar los contornos
resultado = imagen.copy()

cv2.drawContours(
    resultado,
    contornos,
    -1,
    (0, 255, 0),
    2
)

# Mostrar resultados
cv2.imshow("Imagen original 0074", imagen)
cv2.imshow("Imagen binaria0074 ", binaria)
cv2.imshow("Contornos detectados0 0074", resultado)

# Guardar resultado
cv2.imwrite(
    "../resultados/ejemplo2_contornos.jpg",
    resultado
)

print("Cantidad de contornos encontrados:", len(contornos))
print("Resultado guardado en resultados/ejemplo2_contornos.jpg")

# Esperar
cv2.waitKey(0)

# Cerrar ventanas
cv2.destroyAllWindows()
print("PROGRAMA REALIZADO POR JAQUEZ ANDRES 0074")