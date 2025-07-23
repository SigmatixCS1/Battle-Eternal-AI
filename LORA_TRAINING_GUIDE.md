# 🎭 Battle-Eternal Character LoRA Training Guide

## 🎯 Overview

Training custom LoRA (Low-Rank Adaptation) models for your Battle-Eternal characters will give you:
- **Consistent character appearance** across generations
- **Better prompt control** for specific characters
- **Character-specific style adaptation**
- **Reduced prompt length** (just use character name triggers)

## 📋 Prerequisites

### System Requirements
- **RAM**: 16GB+ recommended (8GB minimum)
- **VRAM**: 6GB+ for GPU training (CPU training possible but slow)
- **Storage**: 5GB+ free space for training data and models
- **Time**: 2-8 hours per character depending on hardware

### Software Requirements
✅ Already installed in your system:
- Python 3.8+
- PyTorch
- Diffusers
- ComfyUI (with training nodes)
- Accelerate

## 🗂️ Training Data Preparation

### 1. Image Collection Strategy

For each Battle-Eternal character, you need **15-30 high-quality images**:

#### **Alexander (Protagonist)**
```
📁 training_data/alexander/
├── alexander_portrait_001.jpg    # Close-up, clear face
├── alexander_full_body_002.jpg   # Full body shot
├── alexander_casual_003.jpg      # Different outfit
├── alexander_action_004.jpg      # Dynamic pose
├── alexander_side_005.jpg        # Profile view
└── ... (15-30 total images)
```

#### **DeMarcus (Technomancer)**
```
📁 training_data/demarcus/
├── demarcus_tech_001.jpg         # With laptop/tech
├── demarcus_portrait_002.jpg     # Clear face
├── demarcus_magic_003.jpg        # Casting spells
├── demarcus_confident_004.jpg    # Arrogant expression
└── ... (15-30 total images)
```

### 2. Image Quality Guidelines

**✅ Good Training Images:**
- **Resolution**: 512x512 minimum (768x768 preferred)
- **Quality**: High detail, sharp, good lighting
- **Variety**: Different poses, expressions, angles
- **Consistency**: Same character, recognizable features
- **Clean**: No watermarks, text overlays

**❌ Avoid:**
- Blurry or low-resolution images
- Multiple characters in same image
- Heavy shadows or poor lighting
- Extreme distortions or filters

### 3. Caption Files

Create `.txt` files for each image with descriptive captions:

```
# alexander_portrait_001.txt
alexander, anime boy, blonde messy hair, blue eyes, glasses, red hoodie, confident smile, portrait, detailed art

# demarcus_tech_001.txt
demarcus, anime man, dark skin, bald, glowing eyes, laptop computer, technomancer, cyberpunk style, detailed art
```

## 🛠️ Training Methods

### Method 1: ComfyUI Training Nodes (Recommended)

Your ComfyUI installation includes training nodes. Here's the workflow:

1. **Load Training Data**
2. **Setup LoRA Parameters** 
3. **Configure Training Settings**
4. **Start Training Process**

### Method 2: Kohya Scripts (Advanced)

For more control, you can use dedicated training scripts.

### Method 3: Diffusers Training (Alternative)

Using the built-in diffusers training utilities.

## 🚀 Step-by-Step Training Process

### Step 1: Prepare Training Environment

```bash
# Activate your virtual environment
C:\Users\Sigma\battle-eternal-ai\venv\Scripts\activate

# Install additional training dependencies if needed
pip install accelerate wandb tensorboard
```

### Step 2: Organize Training Data

```bash
# Create directory structure
mkdir training_data
mkdir training_data\alexander
mkdir training_data\demarcus
mkdir output\loras
```

### Step 3: Generate Training Images

Use your existing Anything V5 pipeline to create consistent training data:

```python
# Generate multiple variations of Alexander
python generate_training_data.py --character alexander --count 25
python generate_training_data.py --character demarcus --count 25
```

### Step 4: Configure Training Parameters

**Recommended Settings for Battle-Eternal Characters:**

```yaml
# training_config.yaml
base_model: "models/checkpoints/anything-v5"
output_dir: "output/loras"
resolution: 512
train_batch_size: 1
learning_rate: 1e-4
max_train_steps: 1000
checkpointing_steps: 100
validation_steps: 50
mixed_precision: "fp16"
gradient_accumulation_steps: 1
```

### Step 5: Start Training

```bash
# Train Alexander LoRA
python train_lora.py \
  --character "alexander" \
  --training_data "training_data/alexander" \
  --output_name "battle_eternal_alexander_v1" \
  --steps 1000

# Train DeMarcus LoRA  
python train_lora.py \
  --character "demarcus" \
  --training_data "training_data/demarcus" \
  --output_name "battle_eternal_demarcus_v1" \
  --steps 1000
```

## ⚙️ Advanced Training Configuration

### Learning Rate Scheduling
- **Start**: 1e-4
- **Warmup**: 10% of total steps
- **Decay**: Cosine annealing

### Data Augmentation
- **Random crops**: 10%
- **Horizontal flips**: 50% (careful with text/asymmetric features)
- **Color jitter**: Slight variations

### LoRA Rank Settings
- **Rank**: 32-128 (higher = more detailed, larger file)
- **Alpha**: 32 (good starting point)
- **Dropout**: 0.1

## 🎮 Using Trained LoRAs

### In Generate Script

```python
# Modified generate_anything_v5.py
from diffusers import StableDiffusionPipeline
import torch

pipe = StableDiffusionPipeline.from_pretrained("models/checkpoints/anything-v5")

# Load LoRA
pipe.load_lora_weights("output/loras/battle_eternal_alexander_v1.safetensors")

# Simple prompt with character trigger
prompt = "alexander, confident pose, magical aura"
image = pipe(prompt).images[0]
```

### In ComfyUI

1. Load your LoRA file using "Load LoRA" node
2. Connect to your model chain
3. Use simple trigger words in prompts

### Trigger Words

**Alexander LoRA triggers:**
- `alexander` - Basic character
- `alexander portrait` - Close-up shots  
- `alexander full body` - Full body shots
- `alexander magic` - With magical elements

**DeMarcus LoRA triggers:**
- `demarcus` - Basic character
- `demarcus technomancer` - With tech elements
- `demarcus confident` - Arrogant expression
- `demarcus coding` - At computer/laptop

## 📊 Training Monitoring

### Loss Tracking
- **Target Loss**: < 0.1 for good convergence
- **Validation Loss**: Should decrease steadily
- **Overfitting Signs**: Validation loss increases while training loss decreases

### Quality Checkpoints
Generate test images every 100 steps:
```bash
# Test prompts
"alexander, anime portrait, detailed art"
"demarcus, technomancer, glowing laptop, anime art style"
```

## 🚨 Troubleshooting

### Common Issues

**1. Out of Memory (OOM)**
```bash
# Solutions:
--train_batch_size 1
--gradient_accumulation_steps 2
--resolution 256
--mixed_precision fp16
```

**2. Poor Character Consistency**
- Increase training steps (1500-2000)
- Add more diverse training images
- Check caption quality

**3. Overfitting**
- Reduce learning rate
- Add more training data
- Increase dropout

**4. Slow Training**
```bash
# Enable optimizations
--use_8bit_adam
--gradient_checkpointing
--mixed_precision bf16
```

## 📈 Expected Timeline

### CPU Training (Your Setup)
- **Alexander**: ~6-8 hours (1000 steps)
- **DeMarcus**: ~6-8 hours (1000 steps)
- **Both characters**: ~12-16 hours total

### With GPU (Future upgrade)
- **Per character**: ~1-2 hours
- **Both characters**: ~2-4 hours total

## 🎯 Success Metrics

Your LoRA is ready when:
- ✅ Character appears consistently with just trigger word
- ✅ Facial features match your character design
- ✅ Style remains consistent with Battle-Eternal aesthetic
- ✅ Works with various poses and expressions
- ✅ File size reasonable (< 500MB)

## 🔄 Iterative Improvement

1. **Version 1**: Basic character recognition
2. **Version 2**: Add outfit variations
3. **Version 3**: Include magical/special abilities
4. **Version 4**: Perfect consistency and style

## 📚 Next Steps

After successful LoRA training:
1. **Character Expansion**: Train more Battle-Eternal characters
2. **Style LoRAs**: Train specific art styles
3. **Concept LoRAs**: Train magical effects, environments
4. **Merging**: Combine multiple LoRAs for complex scenes

---

**Training your Battle-Eternal LoRAs will give you incredible control over character generation!** 🎭✨
