# Battle-Eternal AI Art Workflow

🎨 **Professional AI Art Generation for Battle-Eternal Universe**

A comprehensive workflow combining Stable Diffusion and ComfyUI for creating high-quality anime/light novel-style illustrations that maintain the distinctive Battle-Eternal art style.

## ✨ Key Features

- **Custom Style Workflow**: ComfyUI node-based interface for precise control
- **Battle-Eternal Optimized**: Specialized for anime/light novel art style
- **Model Management**: Organized structure for checkpoints, LoRAs, and ControlNet
- **Workflow Templates**: Reusable workflows for consistent results
- **GitHub Ready**: Version-controlled setup for collaboration

## 🚀 Setup Complete!

Your environment is now set up with:
- ✅ Python 3.13.5 virtual environment
- ✅ PyTorch for deep learning
- ✅ Hugging Face Diffusers library
- ✅ Stable Diffusion v1.5 support

## 📁 Project Structure

```
battle-eternal-ai/
├── venv/                    # Virtual environment
├── output/                  # Generated images will be saved here
├── comfyui/                 # ComfyUI installation
│   ├── models/
│   ├── custom_nodes/
│   └── ComfyUI.py
├── models/                  # Custom model directory
│   ├── checkpoints/         # Anime-specific model checkpoints
│   ├── loras/              # Battle-Eternal character LoRAs
│   └── controlnet/         # ControlNet models
├── workflows/               # ComfyUI workflow templates
├── test_stable_diffusion.py # Test script to verify setup
├── generate_image.py        # Main image generation script
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

## 🧪 Testing Your Setup

Run the test script to verify everything is working:

```powershell
python test_stable_diffusion.py
```

This will:
1. Check if CUDA/GPU acceleration is available
2. Download the Stable Diffusion model (first run only)
3. Generate a test image
4. Save it to the `output/` folder

## 🎨 Generating Images

### 🌟 NEW: Battle-Eternal Style with Anything V5

**Quick Battle-Eternal Generation:**
```powershell
python generate_anything_v5.py -p "anime style portrait of Alexander, blonde hair, blue eyes, glasses, red hoodie, magical cards floating" --battle-eternal
```

**Interactive Mode with Battle-Eternal Examples:**
```powershell
python generate_anything_v5.py -i
```

### Original Stable Diffusion v1.5

**Quick Generation:**
```powershell
python generate_image.py -p "a beautiful sunset over mountains, oil painting style"
```

**Interactive Mode:**
```powershell
python generate_image.py -i
```

**Advanced Options:**
```powershell
python generate_image.py -p "cyberpunk cityscape" -n "blurry, low quality" -s 30 -g 8.0 --seed 42
```

Parameters:
- `-p, --prompt`: Text description of what you want to generate
- `-n, --negative`: What you DON'T want in the image
- `-s, --steps`: Number of generation steps (more = higher quality, slower)
- `-g, --guidance`: How closely to follow the prompt (7.5 is good default)
- `--width, --height`: Image dimensions (512x512 recommended)
- `--seed`: Random seed for reproducible results
- `-i, --interactive`: Interactive mode for multiple generations

## 💡 Tips for Better Images

### Good Prompts
- Be specific and descriptive
- Include style keywords: "digital art", "oil painting", "photorealistic"
- Add quality terms: "high quality", "detailed", "sharp"
- Specify lighting: "soft lighting", "dramatic shadows"

### Negative Prompts
Use negative prompts to avoid unwanted elements:
- "blurry, low quality, pixelated"
- "extra limbs, deformed"
- "text, watermark"

### Example Prompts
```
"a majestic dragon flying over a medieval castle, fantasy art, detailed, dramatic lighting"

"portrait of a wise old wizard, long beard, magical staff, digital art, high quality"

"futuristic city at night, neon lights, cyberpunk, detailed architecture, atmospheric"
```

## 🔧 Troubleshooting

### Memory Issues
- Reduce image size: `--width 256 --height 256`
- Use fewer steps: `-s 10`
- Close other applications

### Slow Generation
- First run downloads the model (~4GB) - this is normal
- CPU generation is slower than GPU
- Fewer steps generate faster but lower quality images

### Model Loading Errors
- Check internet connection for first-time model download
- Ensure you have enough disk space (~5GB free recommended)

## 🎯 Next Steps

1. **Test the setup**: Run `python test_stable_diffusion.py`
2. **Generate your first custom image**: Use `python generate_image.py -i`
3. **Experiment with different prompts and settings**
4. **Check the `output/` folder for your generated images**

## 🖥️ Hardware Notes

- **CPU Mode**: Works on any computer, but slower generation
- **GPU Mode**: Requires NVIDIA GPU with CUDA support for faster generation
- **RAM**: Minimum 8GB recommended, 16GB+ for optimal performance

Your setup is ready to create amazing AI-generated images! 🎨✨
