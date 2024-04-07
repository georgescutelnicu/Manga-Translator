from PIL import Image, ImageDraw, ImageFont
import numpy as np
import textwrap
import cv2


def add_text(image, text, font_path, bubble_contour):
    """
    Add text inside a speech bubble contour.

    Args:
        image (numpy.ndarray): Processed bubble image (cv2 format - BGR).
        text (str): Text to be placed inside the speech bubble.
        font_path (str): Font path.
        bubble_contour (numpy.ndarray): Contour of the detected speech bubble.

    Returns:
        numpy.ndarray: Image with text placed inside the speech bubble.
    """
    pil_image = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(pil_image)

    x, y, w, h = cv2.boundingRect(bubble_contour)

    wrapped_text = textwrap.fill(text, width=int(w * 0.1), break_long_words=True)

    line_height = 12
    font_size = 10
    font = ImageFont.truetype(font_path, size=font_size)

    lines = wrapped_text.split('\n')
    total_text_height = (len(lines)) * line_height

    if total_text_height > h:
        font_size *= (h / total_text_height)
        line_height = 10
        total_text_height = (len(lines)) * line_height

    # Vertical centering
    text_y = y + (h - total_text_height) // 2

    for line in lines:
        text_length = draw.textlength(line, font=font)

        # Horizontal centering
        text_x = x + (w - text_length) // 2

        draw.text((text_x, text_y), line, font=font, fill=(0, 0, 0))

        text_y += line_height

    image[:, :, :] = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)

    return image
