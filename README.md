

# Ogma: Symbolic Quantum Logic

**Ogma** is a symbolic computation paradigm designed to extend classical logic by embracing ambiguity, failure, and imagination.  
It blends complex number theory, quantum analogs, and symbolic logic to allow machines to continue reasoning even when traditional logic fails.

---

## 🧠 What Is Ogma?

Traditional logic treats 0 and 1 as distinct, complete truths.  
**Ogma proposes** that during processing, these truths exist in a state of symbolic uncertainty — just like quantum superposition.  
- In Ogma, **`0` may be interpreted as `-1`**, a placeholder for unresolved logic
- **Complex numbers** (like `x + iy`) represent ideas that haven't fully collapsed into an answer yet
- Collapse occurs **not when calculated**, but when **context requires a resolution**

The idea comes from the poetic intuition:  
> "Between 1 and 0 lies a hush... a shimmer just out of sight."

![Ogma Collapse Diagram](diagrams/A_ogma_symbolic_collapse.png)

This approach lets logic become fluid — errors become symbolic states, ambiguity becomes useful, and reasoning can persist even with incomplete information.

---

## 🔹 Version 1.0 (Stable)

This introduces Ogma's foundational logic:
- Complex numbers to represent logical states
- `OgmaSymbol(real, imag)` captures unresolved meaning
- Symbolic representation of values and error labels

### 🧮 Key Concepts
- Logical fault is not failure — it's **processing in flight**
- `imaginary` parts encode symbolic deviation from numeric reality
- Symbolic logic is **descriptive** — not deterministic

---

## 🔁 Version 1.1 (Experimental)

Ogma v1.1 adds **fallback mechanics and recovery logic** that simulate a symbolic quantum state machine.

### 🔧 New Features:
- `expand_to(bits)` – Symbolically grow values to prevent bit overflow
- `reduce_to_symbolic_64bit()` – Represent invalid large values symbolically
- `presume_intent(actual, requested)` – Substitute unavailable operations with symbolic approximations
- Labels and context tagging for developer clarity

---

## 🧪 Running Tests

Explore symbolic recovery and approximation by running:

```bash
python ogma_tests_v1_1.py
```

---

## 📂 Branches

- `main` – Stable release with minimal symbolic engine
- `v1.1` – Symbolic fallback, approximation, and error tolerance logic

---

## 🔍 Why Ogma?

Modern computing relies on **strict logic** that fails hard when unexpected input or conditions arise.  
Ogma **absorbs and repurposes failure** into new symbolic states that:
- Avoid crashes
- Provide fallback interpretations
- Allow AI to explore logic “between” conventional binaries

This system is ideal for:
- Embedded systems with limited fail tolerance  
- Symbolic machine learning  
- Creative AI environments  
- Exploratory error-immune programming

---

## 🧠 Authored by
**Cian Monerawela + ChatGPT**  
“Between human imagination and AI logic lies the symbolic field.”

---

## 🛡️ License
MIT – Free to use with attribution.
