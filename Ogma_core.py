
# ogma_core.py
# Ogma Symbolic Quantum Logic Engine
# Created by Cian Monerawela + ChatGPT (OpenAI)

import cmath

class OgmaSymbol:
    def __init__(self, real, imag=0, label=None):
        self.value = complex(real, imag)
        self.label = label or "⌀"

    def collapse(self):
        # Collapse symbolic state: if imaginary, resolve to label
        if self.value.imag != 0:
            return self.label
        return round(self.value.real, 5)

    def __add__(self, other):
        if isinstance(other, OgmaSymbol):
            return OgmaSymbol(
                self.value.real + other.value.real,
                self.value.imag + other.value.imag,
                label=self.label if self.label == other.label else "⊗"
            )
        else:
            return OgmaSymbol(self.value.real + other, self.value.imag, self.label)

    def __sub__(self, other):
        if isinstance(other, OgmaSymbol):
            return OgmaSymbol(
                self.value.real - other.value.real,
                self.value.imag - other.value.imag,
                label=self.label if self.label == other.label else "⊗"
            )
        else:
            return OgmaSymbol(self.value.real - other, self.value.imag, self.label)

    def __str__(self):
        return f"Ogma({self.value.real} + {self.value.imag}i → {self.collapse()})"

    def __repr__(self):
        return str(self)

# Test case
if __name__ == "__main__":
    a = OgmaSymbol(5)
    b = OgmaSymbol(3, 1, label="∑")  # symbolic component
    c = a + b
    print("Symbolic Sum:", c)
    print("Collapsed:", c.collapse())
