# Открытие изображения
def open_image(file_path):
    try:
        image = Image.open(file_path)
        return image
    except IOError:
        print("Не удалось открыть изображение")
        return None

# Изменение размера изображения
def resize_image(image, size):
    try:
        resized_image = image.resize(size)
        return resized_image
    except ValueError:
        print("Ошибка при изменении размера изображения")
        return None

# Сохранение изображения
def save_image(image, file_path):
    try:
        image.save(file_path)
        print("Изображение сохранено")
    except IOError:
        print("Не удалось сохранить изображение")

# Открытие видеофайла
def open_video(file_path):
    try:
        cap = cv2.VideoCapture(file_path)
        return cap
    except:
        print("Не удалось открыть видеофайл")
        return None

# Чтение и отображение кадра из видео
def read_frame(cap):
    ret, frame = cap.read()
    if ret:
        cv2.imshow("Video", frame)
        return frame
    else:
        return None

# Закрытие видеофайла
def close_video(cap):
    cap.release()
    cv2.destroyAllWindows()