#!/usr/bin/env python3
"""
Battle-Eternal LoRA Training Data Generator

This script generates diverse training images for each Battle-Eternal character
to be used for LoRA training. It creates variations in pose, expression, 
outfit, and lighting to ensure good training data diversity.
"""

import argparse
import os
import torch
from diffusers import StableDiffusionPipeline
from datetime import datetime
import random
import json

# Character-specific prompt templates
CHARACTER_TEMPLATES = {
    "alexander": {
        "base": "anime style Alexander, blonde messy hair, blue eyes, glasses, red hoodie",
        "variations": [
            # Poses and expressions
            "confident smile, looking at viewer",
            "serious expression, side profile",
            "determined look, clenched fist",
            "surprised expression, wide eyes",
            "thinking pose, hand on chin",
            "pointing forward, dynamic pose",
            "arms crossed, confident stance",
            "looking up, hopeful expression",
            "smirking, arrogant look",
            "concerned expression, frowning",
            
            # Different outfits/contexts
            "school uniform, indoor setting",
            "casual clothes, outdoor scene",
            "winter coat, snowy background",
            "summer clothes, bright lighting",
            "formal attire, elegant pose",
            
            # Magical/battle contexts
            "glowing magical aura around him",
            "holding magical cards in hand",
            "surrounded by floating spell effects",
            "casting a spell, dramatic lighting",
            "in battle stance, energy effects",
            
            # Camera angles
            "full body shot, standing pose",
            "upper body portrait, detailed face",
            "close-up face shot, detailed eyes",
            "three quarter view, slight angle",
            "from below angle, heroic pose"
        ]
    },
    
    "demarcus": {
        "base": "anime style DeMarcus, dark-skinned bald male, technomancer",
        "variations": [
            # Expressions and poses
            "arrogant smirk, looking down",
            "concentrated expression, coding",
            "evil grin, glowing eyes",
            "serious face, determined look",
            "laughing maniacally, crazy eyes",
            "confident pose, arms crossed",
            "typing on laptop, focused",
            "pointing at screen, explaining",
            "leaning back in chair, smug",
            "standing pose, intimidating",
            
            # Tech contexts
            "surrounded by multiple monitors",
            "laptop open, code on screen",
            "holographic displays around him",
            "cyberpunk office environment",
            "server room background, blue lights",
            
            # Magic/tech fusion
            "laptop with magical energy emanating",
            "runic code flowing from computer",
            "red dragon energy behind him",
            "shadow and fire constructs around",
            "mystical tech laboratory setting",
            "digital magic spell effects",
            "technomancy ritual, glowing symbols",
            
            # Camera angles
            "full body in tech environment",
            "upper body at computer desk",
            "close-up portrait, intense eyes",
            "from side, profile view",
            "dramatic low angle, imposing"
        ]
    }
}

# Lighting and quality modifiers
QUALITY_MODIFIERS = [
    "detailed art, high quality",
    "masterpiece, detailed digital art",
    "professional illustration, detailed",
    "high resolution, sharp details",
    "detailed anime art style",
    "studio lighting, high quality",
    "dramatic lighting, detailed art",
    "soft lighting, detailed illustration"
]

NEGATIVE_PROMPTS = [
    "lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry, artist name",
    "ugly, duplicate, morbid, mutilated, out of frame, extra fingers, mutated hands, poorly drawn hands, poorly drawn face, mutation, deformed, blurry, bad anatomy, bad proportions, extra limbs, cloned face, disfigured, gross proportions, malformed limbs",
    "multiple people, crowd, group, extra person, background characters, text, watermark, signature, artist name, low quality, blurry"
]

def setup_pipeline():
    """Initialize the Anything V5 pipeline"""
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"💻 Using device: {device}")
    
    model_path = "models/checkpoints/anything-v5"
    
    if not os.path.exists(model_path):
        print(f"❌ Error: Anything V5 model not found at {model_path}")
        return None
    
    print("📦 Loading Anything V5 model for training data generation...")
    pipe = StableDiffusionPipeline.from_pretrained(
        model_path,
        torch_dtype=torch.float16 if device == "cuda" else torch.float32,
        safety_checker=None,
        requires_safety_checker=False,
        local_files_only=True
    )
    pipe = pipe.to(device)
    
    # Memory optimizations
    if device == "cuda":
        pipe.enable_memory_efficient_attention()
        pipe.enable_vae_slicing()
    
    print("✅ Pipeline ready for training data generation!")
    return pipe

def generate_character_prompt(character, variation_index):
    """Generate a complete prompt for a character variation"""
    if character not in CHARACTER_TEMPLATES:
        raise ValueError(f"Unknown character: {character}")
    
    template = CHARACTER_TEMPLATES[character]
    base = template["base"]
    variations = template["variations"]
    
    # Cycle through variations
    variation = variations[variation_index % len(variations)]
    quality = random.choice(QUALITY_MODIFIERS)
    
    full_prompt = f"{base}, {variation}, {quality}"
    return full_prompt

def generate_training_images(pipe, character, count, output_dir, seed_base=None):
    """Generate training images for a character"""
    
    # Create character directory
    char_dir = os.path.join(output_dir, character)
    os.makedirs(char_dir, exist_ok=True)
    
    print(f"🎨 Generating {count} training images for {character}")
    print(f"📁 Output directory: {char_dir}")
    
    # Generate metadata file
    metadata = {
        "character": character,
        "model": "anything-v5",
        "generation_date": datetime.now().isoformat(),
        "total_images": count,
        "images": []
    }
    
    successful_generations = 0
    
    for i in range(count):
        try:
            # Generate prompt
            prompt = generate_character_prompt(character, i)
            negative_prompt = random.choice(NEGATIVE_PROMPTS)
            
            # Set seed for reproducibility if provided
            if seed_base:
                seed = seed_base + i
                torch.manual_seed(seed)
                generator = torch.Generator().manual_seed(seed)
            else:
                seed = random.randint(0, 999999)
                generator = torch.Generator().manual_seed(seed)
            
            print(f"  🖼️  Generating image {i+1}/{count}: {prompt[:60]}...")
            
            # Generate image
            with torch.no_grad():
                result = pipe(
                    prompt,
                    negative_prompt=negative_prompt,
                    num_inference_steps=25,  # Faster for training data
                    guidance_scale=8.0,
                    height=512,
                    width=512,
                    generator=generator
                )
            
            # Save image
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"{character}_{i+1:03d}_{timestamp}.png"
            image_path = os.path.join(char_dir, filename)
            result.images[0].save(image_path)
            
            # Save caption file
            caption_path = os.path.join(char_dir, f"{character}_{i+1:03d}_{timestamp}.txt")
            with open(caption_path, 'w', encoding='utf-8') as f:
                # Create training-friendly caption
                training_caption = f"{character}, " + prompt.replace("anime style ", "").replace(f"{character}, ", "")
                f.write(training_caption)
            
            # Add to metadata
            metadata["images"].append({
                "filename": filename,
                "caption_file": os.path.basename(caption_path),
                "prompt": prompt,
                "negative_prompt": negative_prompt,
                "seed": seed,
                "variation_index": i
            })
            
            successful_generations += 1
            print(f"    ✅ Saved: {filename}")
            
        except Exception as e:
            print(f"    ❌ Error generating image {i+1}: {e}")
            continue
    
    # Save metadata
    metadata_path = os.path.join(char_dir, "training_metadata.json")
    with open(metadata_path, 'w', encoding='utf-8') as f:
        json.dump(metadata, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Generated {successful_generations}/{count} training images for {character}")
    print(f"📄 Metadata saved: {metadata_path}")
    
    return successful_generations

def main():
    parser = argparse.ArgumentParser(description='Generate training data for Battle-Eternal character LoRAs')
    parser.add_argument('--character', '-c', type=str, required=True,
                        choices=['alexander', 'demarcus'], 
                        help='Character to generate training data for')
    parser.add_argument('--count', '-n', type=int, default=25,
                        help='Number of training images to generate')
    parser.add_argument('--output_dir', '-o', type=str, default='training_data',
                        help='Output directory for training images')
    parser.add_argument('--seed_base', '-s', type=int, help='Base seed for reproducible generation')
    parser.add_argument('--all', action='store_true', help='Generate for all characters')
    
    args = parser.parse_args()
    
    # Setup pipeline
    pipe = setup_pipeline()
    if pipe is None:
        return
    
    # Create output directory
    os.makedirs(args.output_dir, exist_ok=True)
    
    if args.all:
        # Generate for all characters
        characters = ['alexander', 'demarcus']
        total_generated = 0
        
        for char in characters:
            print(f"\n🎭 Starting generation for {char}")
            generated = generate_training_images(
                pipe, char, args.count, args.output_dir, args.seed_base
            )
            total_generated += generated
        
        print(f"\n🎉 Total training images generated: {total_generated}")
        
    else:
        # Generate for single character
        print(f"\n🎭 Starting generation for {args.character}")
        generated = generate_training_images(
            pipe, args.character, args.count, args.output_dir, args.seed_base
        )
        print(f"\n🎉 Training images generated: {generated}")
    
    print("\n📚 Next steps:")
    print("1. Review generated images and remove any poor quality ones")
    print("2. Edit caption files if needed for better training")
    print("3. Use the images and captions for LoRA training")
    print("4. Check the training guide: LORA_TRAINING_GUIDE.md")

if __name__ == "__main__":
    main()
