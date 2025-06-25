
from ogma_core_v1_1 import OgmaSymbol

def run_ogma_tests():
    print("Running Ogma v1.1 Basic Tests...")

    # Test 1: Overflow from 4-bit to 8-bit
    overflow_symbol = OgmaSymbol(18).expand_to(8)
    print("Test: Overflow 4-bit to 8-bit =>", overflow_symbol)

    # Test 2: Symbolic fallback for unresolved large value
    fallback_symbol = OgmaSymbol(999999999999999999999).reduce_to_symbolic_64bit()
    print("Test: Symbolic Fallback =>", fallback_symbol)

    # Test 3: Presumed intent for unavailable feature (LED)
    led_symbol = OgmaSymbol(0).presume_intent("white", "blue")
    print("Test: LED Substitution (Blue → White) =>", led_symbol)

if __name__ == "__main__":
    run_ogma_tests()
