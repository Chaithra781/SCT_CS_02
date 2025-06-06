# 🖼️ Image Encryption Tool Using Pixel Manipulation

This Python-based tool performs simple image encryption using pixel-level transformations. It supports basic operations such as:

- 🔄 Swapping pixel values randomly
- ➕ Applying mathematical operations (e.g., brightness shift)

---

## ⚙️ Features

- Load and process image files (`.jpg`, `.png`, etc.)
- Encrypt image by:
  - Random pixel swaps (not reversible in simple mode)
  - Brightness shifting (add/subtract values from RGB channels)
- Save encrypted and decrypted images
- Reversible decryption for math-based encryption

---

## 📦 Requirements

- Python 3.x
- [Pillow](https://pypi.org/project/Pillow/)
- [NumPy](https://pypi.org/project/numpy/)

Install dependencies:

```bash
pip install pillow numpy
