#!/usr/bin/env python3
"""
Image optimization script for MkDocs build process.
Optimizes images in the docs/images directory to reduce file sizes.
"""

import os
import sys
from PIL import Image
from pathlib import Path

def optimize_image(image_path):
    """Optimize a single image file."""
    try:
        with Image.open(image_path) as img:
            # Convert to RGB if necessary (for JPEG optimization)
            if img.mode in ('RGBA', 'LA', 'P'):
                # Create white background for transparent images
                background = Image.new('RGB', img.size, (255, 255, 255))
                if img.mode == 'P':
                    img = img.convert('RGBA')
                background.paste(img, mask=img.split()[-1] if img.mode == 'RGBA' else None)
                img = background
            
            # Determine format and optimization settings
            file_ext = image_path.suffix.lower()
            
            if file_ext in ['.jpg', '.jpeg']:
                img.save(image_path, 'JPEG', optimize=True, quality=85, progressive=True)
            elif file_ext == '.png':
                img.save(image_path, 'PNG', optimize=True, compress_level=9)
            elif file_ext == '.webp':
                img.save(image_path, 'WEBP', quality=85, method=6)
            else:
                print(f"Skipping unsupported format: {image_path}")
                return False
                
            print(f"✓ Optimized: {image_path}")
            return True
            
    except Exception as e:
        print(f"✗ Failed to optimize {image_path}: {e}")
        return False

def main():
    """Main function to optimize all images in docs/images directory."""
    images_dir = Path("docs/images")
    
    if not images_dir.exists():
        print("No docs/images directory found. Creating it...")
        images_dir.mkdir(parents=True, exist_ok=True)
        print("Created docs/images directory. No images to optimize.")
        return
    
    # Supported image formats
    image_extensions = {'.jpg', '.jpeg', '.png', '.webp'}
    
    # Find all image files in docs/images directory
    image_files = []
    for ext in image_extensions:
        image_files.extend(images_dir.rglob(f"*{ext}"))
        image_files.extend(images_dir.rglob(f"*{ext.upper()}"))
    
    if not image_files:
        print("No image files found in docs/images directory.")
        return
    
    print(f"Found {len(image_files)} image files to optimize in docs/images/...")
    
    # Optimize each image
    optimized_count = 0
    for image_path in image_files:
        if optimize_image(image_path):
            optimized_count += 1
    
    print(f"\nOptimization complete: {optimized_count}/{len(image_files)} images optimized.")

if __name__ == "__main__":
    main() 