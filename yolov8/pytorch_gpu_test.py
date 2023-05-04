import torch

print('Версия PyTorch', torch.__version__)
print('Доступность устройства CUDA для вычислений', torch.cuda.is_available())
print('Текущее устройство CUDA', torch.cuda.current_device())
print('Название текущего CUDA-устройства', torch.cuda.get_device_name(0))

print('Тест вычислений на текущем CUDA-устройстве')
device = torch.device('cuda')
t1 = torch.randn(1, 2).to(device)
t2 = torch.randn(1, 2).to(device)
t3 = t1 * t2

print('Вектор t1', t1)
print('Вектор t2', t2)
print('Вектор t3 = t1 * t2', t3)