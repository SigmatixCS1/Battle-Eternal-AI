# 🎭 Battle-Eternal AI - Anime Character Generation System

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Stable Diffusion](https://img.shields.io/badge/Stable%20Diffusion-Anything%20V5-green.svg)]()

A complete AI-powered image generation system designed specifically for the **Battle-Eternal** light novel project. Generate consistent, high-quality anime-style character artwork using advanced Stable Diffusion models.

## ✨ Features

- 🎨 **Anime-Style Generation** - Specialized for high-quality anime/light novel artwork
- 👤 **Character Consistency** - Optimized prompts for Battle-Eternal characters
- 🔌 **Offline Capable** - Works completely offline once models are downloaded
- 🎛️ **ComfyUI Integration** - Advanced workflow support and node-based editing
- 🏷️ **LoRA Training Ready** - Prepare and train custom character models
- ⚡ **Battle-Eternal Optimized** - Pre-configured settings for best results
- 🎯 **Multiple Characters** - Alexander, DeMarcus, and expanding cast

## 🚀 Quick Start

### Prerequisites
- **Python** 3.8 or higher
- **RAM** 8GB minimum (16GB+ recommended)
- **Storage** 10GB+ free space for models
- **OS** Windows, Linux, or macOS

### Installation

1. **Clone the repository:**
```bash
git clone https://github.com/yourusername/battle-eternal-ai.git
cd battle-eternal-ai
```

2. **Create and activate virtual environment:**
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/macOS
source venv/bin/activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Download Models:**
- Download the Anything V5 model
- Place in `models/checkpoints/anything-v5/`
- See [Model Setup Guide](docs/MODEL_SETUP.md)

### 🎨 Generate Your First Image

```bash
# Generate Alexander (protagonist)
python generate_anything_v5.py --battle-eternal -p "Alexander, confident pose, magical aura"

# Generate DeMarcus (technomancer)
python generate_anything_v5.py --battle-eternal -p "DeMarcus, technomancer, laptop with magical energy"

# Interactive mode with examples
python generate_anything_v5.py -i
```

## 👥 Battle-Eternal Characters

### 🦸 Alexander - The Protagonist
- **Appearance**: Blonde messy hair, blue eyes, glasses
- **Outfit**: Red and gray hoodie
- **Personality**: Confident, determined
- **Powers**: Magical card summoning

### 🧙 DeMarcus - The Technomancer  
- **Appearance**: Dark-skinned, bald, intense eyes
- **Style**: Cyberpunk-fantasy fusion
- **Personality**: Arrogant, brilliant
- **Powers**: Technology-magic fusion

*More characters coming soon!*

## 📚 Documentation

| Document | Description |
|----------|-------------|
| [**Usage Guide**](USAGE_ANYTHING_V5.md) | Complete usage instructions and examples |
| [**LoRA Training**](LORA_TRAINING_GUIDE.md) | Train custom character models |
| [**Contributing**](CONTRIBUTING.md) | How to contribute to the project |

## 🛠️ Advanced Features

### 🎯 LoRA Character Training
Train custom models for perfect character consistency:
```bash
python generate_training_data.py --character alexander --count 25
# Follow LORA_TRAINING_GUIDE.md for complete process
```

### 🏷️ Logo Generation
Generate Battle-Eternal branding assets:
```bash
.\generate_logo_variations.bat
```

### 🎛️ ComfyUI Workflows
Advanced node-based image generation and editing.

## 📁 Project Structure

```
battle-eternal-ai/
├── 📁 comfyui/                 # ComfyUI installation
├── 📁 models/                  # AI models (not in repo)
│   └── checkpoints/
│       └── anything-v5/
├── 📁 output/                  # Generated images
├── 📁 training_data/           # LoRA training data
├── 📁 workflows/               # ComfyUI workflows
├── 🐍 generate_anything_v5.py  # Main generation script
├── 🐍 generate_training_data.py# LoRA training data gen
├── 📋 requirements.txt         # Python dependencies
├── 📖 README.md               # This file
└── 📖 USAGE_ANYTHING_V5.md    # Detailed usage guide
```

## 💡 Usage Examples

### Character Generation
```bash
# Alexander variants
python generate_anything_v5.py --battle-eternal -p "Alexander portrait, confident smile"
python generate_anything_v5.py --battle-eternal -p "Alexander casting spell, magical cards"
python generate_anything_v5.py --battle-eternal -p "Alexander full body, heroic pose"

# DeMarcus variants
python generate_anything_v5.py --battle-eternal -p "DeMarcus technomancer, coding magic"
python generate_anything_v5.py --battle-eternal -p "DeMarcus arrogant smirk, glowing laptop"
```

### Logo and Branding
```bash
# Generate logo variations
.\generate_logo_variations.bat

# Custom logo prompts
python generate_anything_v5.py -p "BATTLE ETERNAL logo, cyan glow, dark background"
```

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

### Quick Contribute
1. 🍴 Fork the repository
2. 🌿 Create feature branch (`git checkout -b feature/amazing-feature`)
3. ✅ Commit changes (`git commit -m 'Add amazing feature'`)
4. 📤 Push to branch (`git push origin feature/amazing-feature`)
5. 🔃 Open a Pull Request

## 📊 System Requirements

| Component | Minimum | Recommended |
|-----------|---------|-------------|
| **RAM** | 8GB | 16GB+ |
| **Storage** | 10GB | 20GB+ |
| **GPU** | None (CPU) | NVIDIA GTX 1060+ |
| **Python** | 3.8 | 3.9+ |

## 🐛 Troubleshooting

### Common Issues

**Out of Memory:**
```bash
# Reduce image size
python generate_anything_v5.py -p "prompt" --width 256 --height 256
```

**Model Not Found:**
Ensure Anything V5 model is in `models/checkpoints/anything-v5/`

**Slow Generation:**
- CPU generation takes 5-10 minutes per image
- GPU highly recommended for faster generation

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Anything V5** model creators for the amazing anime generation capability
- **ComfyUI** team for the powerful workflow system
- **Diffusers** library for Stable Diffusion integration
- **Battle-Eternal** community for inspiration and feedback

## 📞 Support

- 📖 [Documentation](docs/)
- 🐛 [Issue Tracker](https://github.com/yourusername/battle-eternal-ai/issues)
- 💬 [Discussions](https://github.com/yourusername/battle-eternal-ai/discussions)

---

**Made with ❤️ for the Battle-Eternal light novel project**

⭐ **Star this repo if you find it useful!** ⭐
