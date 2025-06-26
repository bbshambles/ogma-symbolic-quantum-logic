# Ogma Symbolic Field Constants
OGMA_SYMBOLIC_FIELD_MIN = -100
OGMA_SYMBOLIC_FIELD_MAX = 100

def map_to_ogma_symbolic_field(value):
    """
    Clamp value into the symbolic range of –100 to +100.
    Prevents symbolic overflow or failure.
    """
    if value < OGMA_SYMBOLIC_FIELD_MIN:
        return OGMA_SYMBOLIC_FIELD_MIN
    elif value > OGMA_SYMBOLIC_FIELD_MAX:
        return OGMA_SYMBOLIC_FIELD_MAX
    return value
  
# Example test
inputs = [-200, -75, 0, 75, 200]
mapped = [map_to_ogma_symbolic_field(i) for i in inputs]
print(mapped)  # Output: [-100, -75, 0, 75, 100]
