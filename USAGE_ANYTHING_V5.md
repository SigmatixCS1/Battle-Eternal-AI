# Anything V5 Model - Usage Guide

## 🎨 **Battle-Eternal Style Generation**

The Anything V5 model is specifically optimized for high-quality anime/light novel style illustrations, perfect for the Battle-Eternal universe.

## 🚀 **Quick Start**

### Battle-Eternal Optimized Generation
```bash
python generate_anything_v5.py --battle-eternal -p "your prompt here"
```

This automatically uses optimal settings:
- **Steps**: 30 (high quality)
- **Guidance**: 8.5 (strong prompt adherence)
- **Size**: 512x768 (portrait format)
- **Enhanced negative prompts** for better anime quality

### Interactive Mode
```bash
python generate_anything_v5.py -i
```

Features:
- Built-in Battle-Eternal example prompts
- Style tips and suggestions
- Continuous generation session

## 💡 **Battle-Eternal Prompt Tips**

### Character Generation
```
"anime style portrait of [CHARACTER], [HAIR COLOR] hair, [EYE COLOR] eyes, [CLOTHING], [POSE], detailed art, high quality"
```

### Example for Alexander:
```
"anime style portrait of Alexander, blonde messy hair, blue eyes, glasses, red and gray hoodie, confident pose, magical cards floating around, mystical blue aura, detailed digital art"
```

### Magical Scenes
```
"magical battle scene, anime characters, spell effects, dynamic poses, detailed illustration, dramatic lighting"
```

## ⚙️ **Advanced Options**

### Custom Settings
```bash
python generate_anything_v5.py -p "prompt" -s 25 -g 7.5 --width 512 --height 768 --seed 42
```

### Parameters
- `-s, --steps`: Generation steps (20-30 recommended)
- `-g, --guidance`: Guidance scale (7.5-9.0 for anime)
- `--width/height`: Image dimensions
- `--seed`: For reproducible results
- `-n, --negative`: Custom negative prompts

## 🎯 **Best Practices**

1. **Always include "anime style"** in your prompts
2. **Use "detailed, high quality"** for better results  
3. **Add lighting descriptions**: "dramatic lighting", "soft light"
4. **Specify pose and composition**: "portrait", "full body", "dynamic pose"
5. **Include magical elements**: "glowing aura", "magical particles"

## 📊 **Model Specifications**

- **Model**: Anything V5 (Anime-optimized Stable Diffusion)
- **Size**: ~7GB total download
- **Optimal Settings**: 25-30 steps, guidance 8.0-8.5
- **Best Resolution**: 512x768 (portrait) or 768x512 (landscape)

## 🔧 **Troubleshooting**

### Memory Issues
- Reduce image size: `--width 256 --height 256`
- Lower steps: `-s 15`

### Quality Issues
- Increase steps: `-s 30`
- Adjust guidance: `-g 8.5`
- Check negative prompts

### Loading Errors
- Ensure model downloaded correctly in `models/checkpoints/anything-v5/`
- Check disk space (7GB+ required)

---

**Happy generating!** 🎨✨
