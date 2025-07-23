# 📦 Model Setup Guide

## Overview

The Battle-Eternal AI system requires the Anything V5 model for optimal anime-style character generation. Due to the large file size (~7GB), models are not included in the repository and must be downloaded separately.

## 🔽 Downloading the Anything V5 Model

### Method 1: Hugging Face (Recommended)

1. **Install Hugging Face CLI** (if not already installed):
```bash
pip install huggingface_hub
```

2. **Download the model**:
```bash
# Create directory structure
mkdir -p models/checkpoints/anything-v5

# Download from Hugging Face
huggingface-cli download Lykon/AnythingV5_Ink --local-dir models/checkpoints/anything-v5
```

### Method 2: Manual Download

1. **Visit the model page**:
   - Go to: https://huggingface.co/Lykon/AnythingV5_Ink

2. **Download required files**:
   - `model_index.json`
   - `text_encoder/` folder
   - `tokenizer/` folder
   - `unet/` folder
   - `vae/` folder
   - `scheduler/` folder

3. **Place in correct directory**:
```
models/checkpoints/anything-v5/
├── model_index.json
├── text_encoder/
│   ├── config.json
│   ├── model.safetensors
│   └── pytorch_model.bin
├── tokenizer/
│   ├── merges.txt
│   ├── special_tokens_map.json
│   ├── tokenizer_config.json
│   └── vocab.json
├── unet/
│   ├── config.json
│   ├── diffusion_pytorch_model.bin
│   └── diffusion_pytorch_model.safetensors
├── vae/
│   ├── config.json
│   ├── diffusion_pytorch_model.bin
│   └── diffusion_pytorch_model.safetensors
└── scheduler/
    └── scheduler_config.json
```

## ✅ Verification

After downloading, verify the setup:

```bash
# Check if model files exist
python -c "
import os
model_path = 'models/checkpoints/anything-v5'
required_files = ['model_index.json', 'text_encoder', 'tokenizer', 'unet', 'vae', 'scheduler']
for file in required_files:
    path = os.path.join(model_path, file)
    if os.path.exists(path):
        print(f'✅ {file} - Found')
    else:
        print(f'❌ {file} - Missing')
"
```

## 🧪 Test Generation

Test that everything works:

```bash
# Activate virtual environment
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

# Test basic generation
python generate_anything_v5.py --battle-eternal -p "anime girl, detailed art"
```

## 🚨 Troubleshooting

### Common Issues

**"Model not found" error:**
- Ensure model is in `models/checkpoints/anything-v5/`
- Check that `model_index.json` exists
- Verify all subdirectories are present

**"Out of memory" error:**
- Reduce image resolution: `--width 256 --height 256`
- Use CPU instead of GPU (automatic if no CUDA)

**Slow download:**
- Use a download manager
- Consider using torrents if available
- Download during off-peak hours

### File Sizes

Expected file sizes for verification:

| File | Size (MB) |
|------|-----------|
| `unet/diffusion_pytorch_model.safetensors` | ~3,279 |
| `text_encoder/model.safetensors` | ~469 |
| `safety_checker/model.safetensors` | ~1,160 |
| `vae/diffusion_pytorch_model.safetensors` | ~319 |

Total: ~7GB

## 🔄 Alternative Models

If you can't download Anything V5, you can try these alternatives:

### Anything V3
```bash
huggingface-cli download Linaqruf/anything-v3.0 --local-dir models/checkpoints/anything-v3
```

### Waifu Diffusion
```bash
huggingface-cli download hakurei/waifu-diffusion --local-dir models/checkpoints/waifu-diffusion
```

**Note:** You'll need to update the model path in the generation scripts.

## 📊 Storage Requirements

Make sure you have adequate storage:

- **Minimum**: 10GB free space
- **Recommended**: 20GB+ for models, cache, and generated images

## 🔒 Legal Notice

- Ensure you comply with the model's license terms
- The Anything V5 model is for non-commercial use
- Respect the original creators' work and attributions

---

Once setup is complete, you're ready to generate Battle-Eternal characters! 🎭
