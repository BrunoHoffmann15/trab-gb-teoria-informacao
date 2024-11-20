

class Hamming:
  def __init__(self):
    self.codeword = ""
    self.hamming_code = ""
    self.error = False
    self.error_position = 0

  def encode(self, codeword):
    pass

  def validate(self, hamming_code):
    pass

  def decode(self, hamming_code):
    if not self.validate(hamming_code):
      return "Código inválido"
    
    bits = [int(bit) for bit in hamming_code]
    
    p1 = bits[0] ^ bits[2] ^ bits[4] ^ bits[6] # XOR dos bits 0, 2, 4 e 6
    p2 = bits[1] ^ bits[2] ^ bits[5] ^ bits[6] # XOR dos bits 1, 2, 5 e 6
    p3 = bits[3] ^ bits[4] ^ bits[5] ^ bits[6] # XOR dos bits 3, 4, 5 e 6
    error_position = p1 + p2 * 2 + p3 * 4
    if error_position > 0:
      self.error = True
      self.error_position = error_position
      bits[error_position - 1] ^= 1 # Inverte o bit com erro
    return "".join([str(bit) for bit in bits[2:]]) # Remove os bits de paridade e retorna a mensagem original