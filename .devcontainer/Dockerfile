# образ для контейнера
FROM nvcr.io/nvidia/tensorrt:22.08-py3

# отключаем интерактивные вопросы при установке пакетов
# при создании docker-контейнера
ARG DEBIAN_FRONTEND=noninteractive

# установим opencv-python
# для этого нам понадобится ее зависимость libgl1
# см. https://stackoverflow.com/a/68666500
RUN apt-get update && apt-get install -y python3-opencv
RUN pip install opencv-python==4.6.0.66

# Установим PyTorch 1.12 и Cuda 1.13
RUN pip install torch==1.12.0+cu113 torchvision==0.13.0+cu113 \
    torchaudio==0.12.0 --extra-index-url https://download.pytorch.org/whl/cu113

# Установим ultralytics yolov8
RUN pip install ultralytics==8.0.99

# Зависимости для экспорта yolov8 в ONNX
RUN pip install onnx==1.14.0 onnxsim==0.4.28 install onnxruntime-gpu==1.14.1 \
    rich==13.3.5 flatbuffers==23.5.9 sympy==1.12 coloredlogs==15.0.1  \
    humanfriendly==10.0 markdown_it_py==2.2.0 mpmath==1.3.0 mdurl==0.1.2

# установим kernel для Jupyter Notebook
RUN pip install ipykernel==6.23.0

# чистим систему от лишнего
RUN apt-get clean && apt-get autoremove

# папка для подключения репозитория с кодом
WORKDIR /workspace