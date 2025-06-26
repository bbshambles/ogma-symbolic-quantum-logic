import math

class OgmaSymbol:
    def __init__(self, real, imag=0, label=None):
        self.value = complex(real, imag)
        self.label = label or "⌀"

    def collapse(self):
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

    def __str__(self):
        return f"Ogma({self.value.real} + {self.value.imag}i → {self.collapse()})"

    def __repr__(self):
        return str(self)

class OgmaWave(OgmaSymbol):
    def __init__(self, real, imag=0, label=None, amplitude=1.0, frequency=1.0, phase=0.0):
        super().__init__(real, imag, label)
        self.amplitude = amplitude
        self.frequency = frequency
        self.phase = phase

    def get_wave_value(self, time):
        return self.amplitude * math.sin(self.frequency * time + self.phase)

    def __add__(self, other):
        if isinstance(other, OgmaWave):
            combined_symbol = super().__add__(other)
            new_amplitude = self.amplitude + other.amplitude
            new_frequency = max(self.frequency, other.frequency)
            new_phase = self.phase + other.phase

            return OgmaWave(
                combined_symbol.value.real, combined_symbol.value.imag,
                label=combined_symbol.label,
                amplitude=new_amplitude, frequency=new_frequency, phase=new_phase
            )
        else:
            return super().__add__(other)

    def __str__(self):
        return f"OgmaWave({self.value.real} + {self.value.imag}i | A:{self.amplitude}, F:{self.frequency}, P:{self.phase} → {self.collapse()})"

# Example usage
if __name__ == "__main__":
    wave_a = OgmaWave(2, 1, amplitude=1.5, frequency=2.0, phase=0.0)
    wave_b = OgmaWave(1, 0.5, amplitude=2.0, frequency=1.5, phase=math.pi / 4)

    t = 0.5
    print("Wave A:", wave_a)
    print("Wave A value at t=0.5:", wave_a.get_wave_value(t))
    print("Wave B:", wave_b)
    print("Wave B value at t=0.5:", wave_b.get_wave_value(t))

    combined = wave_a + wave_b
    print("\nCombined Wave:", combined)
    print("Combined Wave value at t=0.5:", combined.get_wave_value(t))

    def __init__(self, real, imag=0, label=None, amplitude=1.0, frequency=1.0, phase=0.0):
        super().__init__(real, imag, label)
        self.amplitude = amplitude
        self.frequency = frequency
        self.phase = phase

    def get_wave_value(self, time):
        return self.amplitude * math.sin(self.frequency * time + self.phase)

    def __add__(self, other):
        if isinstance(other, OgmaWave):
            combined_symbol = super().__add__(other)
            new_amplitude = self.amplitude + other.amplitude
            new_frequency = max(self.frequency, other.frequency)
            new_phase = self.phase + other.phase

            return OgmaWave(
                combined_symbol.value.real, combined_symbol.value.imag,
                label=combined_symbol.label,
                amplitude=new_amplitude, frequency=new_frequency, phase=new_phase
            )
        else:
            return super().__add__(other)

    def __str__(self):
        return f"OgmaWave({self.value.real} + {self.value.imag}i | A:{self.amplitude}, F:{self.frequency}, P:{self.phase} → {self.collapse()})"

# Test case for OgmaWave
if __name__ == "__main__":
    wave_x = OgmaWave(1, amplitude=2.0, frequency=5.0, phase=math.pi/4)
    wave_y = OgmaWave(0, 0.5, label="Ψ", amplitude=1.5, frequency=3.0, phase=math.pi/2)

    print("Wave X value at t=0.1:", wave_x.get_wave_value(0.1))
    print("Wave Y value at t=0.1:", wave_y.get_wave_value(0.1))

    superposition_wave = wave_x + wave_y
    print("\nSuperposition Wave:", superposition_wave)
    print("Superposition Wave Collapsed:", superposition_wave.collapse())
    print("Superposition Wave value at t=0.1:", superposition_wave.get_wave_value(0.1))
