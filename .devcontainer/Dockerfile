# образ для контейнера
FROM nvcr.io/nvidia/tensorrt:23.03-py3

# отключаем интерактивные вопросы при установке пакетов
# при создании docker-контейнера
ARG DEBIAN_FRONTEND=noninteractive

# обновляем список пакетов
RUN apt-get update

# Установим PyTorch 1.12 и Cuda 1.13
RUN pip install torch==1.12.0+cu113 torchvision==0.13.0+cu113 torchaudio==0.12.0 --extra-index-url https://download.pytorch.org/whl/cu113

# Установим ultralytics yolov8
RUN pip install ultralytics

# установим opencv-python
# для этого нам понадобится ее зависимость libgl1
# см. https://stackoverflow.com/a/68666500
RUN apt-get update && apt-get install -y python3-opencv
RUN pip install opencv-python==4.6.0.66

# установим kernel для Jupyter Notebook
RUN pip install ipykernel

# чистим систему от лишнего
RUN apt-get clean && apt-get autoremove

# папка для подключения репозитория с кодом
WORKDIR /workspace