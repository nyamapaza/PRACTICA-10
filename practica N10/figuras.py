import numpy as np

class Superficie3D:
    def __init__(self, x_range=None, y_range=None):
        if x_range is not None and y_range is not None:
            self.x_range = x_range
            self.y_range = y_range
            self.x, self.y = np.meshgrid(np.linspace(x_range[0], x_range[1], 100), 
                                         np.linspace(y_range[0], y_range[1], 100))

    def generar_datos(self):
        raise NotImplementedError("Este método debe ser implementado por las subclases")

class Plano(Superficie3D):
    def __init__(self, x_range, y_range, pendiente):
        super().__init__(x_range, y_range)
        self.pendiente = pendiente

    def generar_datos(self):
        z = self.pendiente * self.x
        return self.x, self.y, z

class Paraboloide(Superficie3D):
    def __init__(self, x_range, y_range, coef):
        super().__init__(x_range, y_range)
        self.coef = coef

    def generar_datos(self):
        z = self.coef * (self.x**2 + self.y**2)
        return self.x, self.y, z

class Sinusoide(Superficie3D):
    def __init__(self, x_range, y_range, frecuencia):
        super().__init__(x_range, y_range)
        self.frecuencia = frecuencia

    def generar_datos(self):
        z = np.sin(self.frecuencia * np.sqrt(self.x**2 + self.y**2))
        return self.x, self.y, z

class Hiperboloide(Superficie3D):
    def __init__(self, x_range, y_range, a, b, c):
        super().__init__(x_range, y_range)
        self.a = a
        self.b = b
        self.c = c

    def generar_datos(self):
        z = np.sqrt((self.x**2 / self.a**2) - (self.y**2 / self.b**2) + self.c)
        return self.x, self.y, z

class Conica(Superficie3D):
    def __init__(self, x_range, y_range, a, b):
        super().__init__(x_range, y_range)
        self.a = a
        self.b = b

    def generar_datos(self):
        z = self.a * self.x + self.b * self.y
        return self.x, self.y, z

class Toroide(Superficie3D):
    def __init__(self, x_range, y_range, R, r):
        super().__init__(x_range, y_range)
        self.R = R
        self.r = r

    def generar_datos(self):
        z = (self.R - np.sqrt(self.x**2 + self.y**2))**2 + self.r**2
        return self.x, self.y, z

class Cubo(Superficie3D):
    def __init__(self, lado):
        self.lado = lado

    def generar_datos(self):
        x = [0, self.lado, self.lado, 0, 0, 0, self.lado, self.lado, 0, 0, self.lado, self.lado, self.lado, self.lado, 0, 0]
        y = [0, 0, self.lado, self.lado, 0, 0, 0, self.lado, self.lado, 0, 0, self.lado, self.lado, 0, 0, self.lado]
        z = [0, 0, 0, 0, 0, self.lado, self.lado, self.lado, self.lado, self.lado, self.lado, self.lado, 0, 0, 0, self.lado]
        return np.array(x), np.array(y), np.array(z)

class Piramide(Superficie3D):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def generar_datos(self):
        x = [0, self.base, self.base, 0, 0, self.base/2]
        y = [0, 0, self.base, self.base, 0, self.base/2]
        z = [0, 0, 0, 0, self.altura, 0]
        return np.array(x), np.array(y), np.array(z)

class Cilindro(Superficie3D):
    def __init__(self, radio, altura):
        self.radio = radio
        self.altura = altura

    def generar_datos(self):
        theta = np.linspace(0, 2*np.pi, 100)
        x = self.radio * np.cos(theta)
        y = self.radio * np.sin(theta)
        z = np.concatenate([np.zeros_like(theta), np.full_like(theta, self.altura)])
        x = np.concatenate([x, x])
        y = np.concatenate([y, y])
        return x, y, z
