import numpy as np

def calculate(list):
  """
  Calcula a média, variância, desvio padrão, máximo, mínimo e soma
  de uma lista de 9 dígitos em uma matriz 3x3.


  Raises:
    ValueError: Se a lista de entrada não contiver exatamente 9 números.
  """
  if len(list) != 9:
    raise ValueError("Array must have nine numbers.")

  # Converte a lista numa matriz NumPy 3x3
  matrix = np.array(list).reshape(3, 3)

  # Calcula as estatísticas e as organiza no formato do dicionário
  # Esta linha e as seguintes devem estar no mesmo nível do 'if' acima
  calculations = {
      'mean': [matrix.mean(axis=0).tolist(), matrix.mean(axis=1).tolist(), matrix.mean()],
      'variance': [matrix.var(axis=0).tolist(), matrix.var(axis=1).tolist(), matrix.var()],
      'standard deviation': [matrix.std(axis=0).tolist(), matrix.std(axis=1).tolist(), matrix.std()],
      'max': [matrix.max(axis=0).tolist(), matrix.max(axis=1).tolist(), matrix.max()],
      'min': [matrix.min(axis=0).tolist(), matrix.min(axis=1).tolist(), matrix.min()],
      'sum': [matrix.sum(axis=0).tolist(), matrix.sum(axis=1).tolist(), matrix.sum()]
  }

  return calculations
    