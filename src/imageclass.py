import numpy as np
import cv2
import os




class ImageToLMS:
    def __init__(self, image_path):
        self.image_path = image_path

        # sRGB (linear) → XYZ (D65)
        self.MsRGB = np.array([
            [0.4124564, 0.3575761, 0.1804375],
            [0.2126729, 0.7151522, 0.0721750],
            [0.0193339, 0.1191920, 0.9503041]
        ])

        # XYZ → LMS (Hunt–Pointer–Estevez)
        self.MHPE = np.array([
            [ 0.4002,  0.7075, -0.0807],
            [-0.2263,  1.1653,  0.0457],
            [ 0.0,     0.0,     0.9182]
        ])

        # Combined linear RGB → LMS
        self.Trgb2lms = self.MHPE @ self.MsRGB

    # --- sRGB gamma decoding ---
    def linearize_srgb(self, img):
        img = img / 255.0

        mask = img <= 0.04045
        img_linear = np.zeros_like(img)

        img_linear[mask] = img[mask] / 12.92
        img_linear[~mask] = ((img[~mask] + 0.055) / 1.055) ** 2.4

        return img_linear

    # --- main conversion ---
    def get_lms_activations(self):
        # Load image (BGR → RGB)
        img = cv2.imread(self.image_path, cv2.IMREAD_COLOR)
        if img is None:
            raise ValueError("Could not load image")

        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # Convert to linear RGB
        img_linear = self.linearize_srgb(img.astype(np.float32))

        # Reshape to 3 × N
        H, W, _ = img_linear.shape
        pixels = img_linear.reshape(-1, 3).T   # shape (3, N)

        # Convert to LMS
        lms = self.Trgb2lms @ pixels            # shape (3, N)

        # Reshape back to image
        lms_image = lms.T.reshape(H, W, 3)

        return lms_image
