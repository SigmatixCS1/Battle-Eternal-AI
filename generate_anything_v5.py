import torch
from diffusers import StableDiffusionPipeline
import os
import argparse
from datetime import datetime

def setup_anything_v5_pipeline():
    """Initialize the Anything V5 pipeline for anime-style generation"""
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"💻 Using device: {device}")
    
    model_path = "models/checkpoints/anything-v5"
    
    if not os.path.exists(model_path):
        print(f"❌ Error: Anything V5 model not found at {model_path}")
        print("Please make sure you've downloaded the model first.")
        return None
    
    print("📦 Loading Anything V5 model for anime-style generation...")
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
        pipe.enable_vae_slicing()  # Reduce memory usage
    
    print("✅ Anything V5 model loaded and ready for Battle-Eternal style generation!")
    return pipe

def generate_battle_eternal_image(pipe, prompt, negative_prompt="", steps=25, guidance=8.0, width=512, height=768, seed=None):
    """Generate a Battle-Eternal style image using Anything V5"""
    
    # Enhanced negative prompt for better anime quality
    enhanced_negative = "lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry, artist name"
    if negative_prompt:
        enhanced_negative = f"{negative_prompt}, {enhanced_negative}"
    
    if seed is not None:
        torch.manual_seed(seed)
    
    print(f"🎨 Generating Battle-Eternal style image...")
    print(f"   Prompt: {prompt}")
    print(f"   Negative prompt: {enhanced_negative}")
    print(f"   Steps: {steps}, Guidance: {guidance}, Size: {width}x{height}")
    
    with torch.no_grad():
        result = pipe(
            prompt,
            negative_prompt=enhanced_negative,
            num_inference_steps=steps,
            guidance_scale=guidance,
            height=height,
            width=width,
            generator=torch.Generator().manual_seed(seed) if seed else None
        )
    
    return result.images[0]

def main():
    parser = argparse.ArgumentParser(description='Generate Battle-Eternal style images with Anything V5')
    parser.add_argument('--prompt', '-p', type=str, help='Text prompt for image generation')
    parser.add_argument('--negative', '-n', type=str, default='', help='Negative prompt')
    parser.add_argument('--steps', '-s', type=int, default=25, help='Number of inference steps')
    parser.add_argument('--guidance', '-g', type=float, default=8.0, help='Guidance scale')
    parser.add_argument('--width', '-w', type=int, default=512, help='Image width')
    parser.add_argument('--height', type=int, default=768, help='Image height')
    parser.add_argument('--seed', type=int, help='Random seed for reproducible results')
    parser.add_argument('--interactive', '-i', action='store_true', help='Interactive mode')
    parser.add_argument('--battle-eternal', '-be', action='store_true', help='Use Battle-Eternal optimized settings')
    
    args = parser.parse_args()
    
    # Setup the Anything V5 pipeline
    pipe = setup_anything_v5_pipeline()
    if pipe is None:
        return
    
    # Battle-Eternal optimized settings
    if args.battle_eternal:
        args.steps = 30
        args.guidance = 8.5
        args.width = 512
        args.height = 768
        print("🎭 Using Battle-Eternal optimized settings!")
    
    # Create output directory
    os.makedirs("output", exist_ok=True)
    
    if args.interactive or not args.prompt:
        # Interactive mode with Battle-Eternal examples
        print("\n🎭 Welcome to Battle-Eternal AI Art Generation with Anything V5!")
        print("Perfect for anime/light novel style illustrations")
        print("Type your prompts and press Enter. Type 'quit' to exit.")
        print("\n💡 Battle-Eternal Style Tips:")
        print("- Use 'anime style, detailed' for consistent results")
        print("- Add 'dramatic lighting, high quality' for better scenes")
        print("- Try 'magical aura, floating particles' for mystical effects")
        
        # Example prompts for Battle-Eternal
        examples = [
            "anime style portrait of Alexander, blonde hair, blue eyes, glasses, red hoodie, magical cards floating around, dramatic lighting",
            "beautiful anime girl with long hair, magical powers, glowing eyes, fantasy outfit, detailed art",
            "anime boy warrior, sword in hand, mystical background, high quality digital art",
            "magical battle scene, anime characters, spell effects, dynamic poses, detailed illustration"
        ]
        
        print("\n🎨 Example prompts for Battle-Eternal:")
        for i, example in enumerate(examples, 1):
            print(f"{i}. {example}")
        print()
        
        while True:
            try:
                user_input = input("\n🖼️  Enter your prompt (or 'examples' to see suggestions): ").strip()
                
                if user_input.lower() in ['quit', 'exit', 'q']:
                    print("👋 Goodbye!")
                    break
                
                if user_input.lower() == 'examples':
                    for i, example in enumerate(examples, 1):
                        print(f"{i}. {example}")
                    continue
                
                if not user_input:
                    continue
                
                # Generate timestamp for filename
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                
                # Generate image
                image = generate_battle_eternal_image(
                    pipe, 
                    user_input,
                    negative_prompt=args.negative,
                    steps=args.steps,
                    guidance=args.guidance,
                    width=args.width,
                    height=args.height,
                    seed=args.seed
                )
                
                # Save image
                filename = f"output/battle_eternal_anything_v5_{timestamp}.png"
                image.save(filename)
                print(f"💾 Image saved: {filename}")
                
            except KeyboardInterrupt:
                print("\n👋 Goodbye!")
                break
            except Exception as e:
                print(f"❌ Error: {e}")
    
    else:
        # Single generation mode
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        image = generate_battle_eternal_image(
            pipe,
            args.prompt,
            negative_prompt=args.negative,
            steps=args.steps,
            guidance=args.guidance,
            width=args.width,
            height=args.height,
            seed=args.seed
        )
        
        filename = f"output/battle_eternal_anything_v5_{timestamp}.png"
        image.save(filename)
        print(f"💾 Image saved: {filename}")

if __name__ == "__main__":
    main()
