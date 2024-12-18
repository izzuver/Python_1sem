import math
class Vector():
  def __init__ (self, x , y, z):
      self.x = x
      self.y = y
      self.z = z


  def summ(self, second):
        return Vector(self.x + second.x, self.y + second.y, self.z + second.z)

  def minus(self, second):
        return Vector(self.x - second.x, self.y - second.y, self.z - second.z)

  def abs(self):
      return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

  def sc_product(self, second):
        return self.x * second.x + self.y * second.y + self.z * second.z

  def mult(self, number):
      return self.x * number + self.y * number + self.z * number