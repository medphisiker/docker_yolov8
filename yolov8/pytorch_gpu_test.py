import torch

print(f'Версия PyTorch, - {torch.__version__}', )
print('Доступность устройства CUDA для вычислений, - ',
      torch.cuda.is_available())

cuda_device_num = torch.cuda.current_device()
cuda_device_name = torch.cuda.get_device_name(cuda_device_num)

print(f'Номер текущего устройство CUDA, - {cuda_device_num}')
print(f'Название текущего CUDA-устройства, - {cuda_device_name}')

print('\nТест вычислений на текущем CUDA-устройстве\n')
device = torch.device('cuda')
t1 = torch.randn(1, 2).to(device)
t2 = torch.randn(1, 2).to(device)
t3 = t1 * t2

print('Вектор t1', t1)
print('Вектор t2', t2)
print('Вектор t3 = t1 * t2', t3)
