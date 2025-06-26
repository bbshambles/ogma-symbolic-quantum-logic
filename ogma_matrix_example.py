
# ogma_matrix_example.py
# Demonstration: Ogma Symbolic Matrix with Complex Numbers — No Collapse

class OgmaSymbol:
    def __init__(self, real, imag=0, label="⌀"):
        self.real = real
        self.imag = imag
        self.label = label

    def __str__(self):
        return f"{self.label}({self.real} + {self.imag}i)"

    def __add__(self, other):
        return OgmaSymbol(
            self.real + other.real,
            self.imag + other.imag,
            label=f"({self.label}+{other.label})"
        )

    def __mul__(self, other):
        if isinstance(other, OgmaSymbol):
            return OgmaSymbol(
                self.real * other.real - self.imag * other.imag,
                self.real * other.imag + self.imag * other.real,
                label=f"{self.label}*{other.label}"
            )
        elif isinstance(other, (int, float)):
            return OgmaSymbol(
                self.real * other,
                self.imag * other,
                label=f"{other}*{self.label}"
            )

# Define symbolic matrix A (2x2)
A = [
    [OgmaSymbol(1, 2, "α"), OgmaSymbol(0, 1, "β")],
    [OgmaSymbol(-1, 1, "γ"), OgmaSymbol(2, 0, "δ")]
]

# Define symbolic vector X (2x1)
X = [
    OgmaSymbol(3, 1, "x₁"),
    OgmaSymbol(1, -1, "x₂")
]

# Perform symbolic matrix multiplication
Y = []
for i in range(2):
    y = A[i][0] * X[0] + A[i][1] * X[1]
    Y.append(y)

# Print results symbolically
print("Ogma Symbolic Matrix Equation Result:")
for i, y in enumerate(Y):
    print(f"y{i+1} =", y)
