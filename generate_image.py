import torch
from diffusers import StableDiffusionPipeline
import os
import argparse
from datetime import datetime

def setup_pipeline():
    """Initialize the Stable Diffusion pipeline"""
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"💻 Using device: {device}")
    
    print("📦 Loading Stable Diffusion model (this may take a while on first run)...")
    pipe = StableDiffusionPipeline.from_pretrained(
        "runwayml/stable-diffusion-v1-5",
        torch_dtype=torch.float16 if device == "cuda" else torch.float32,
        safety_checker=None,
        requires_safety_checker=False
    )
    pipe = pipe.to(device)
    
    # Memory optimizations
    if device == "cuda":
        pipe.enable_memory_efficient_attention()
        pipe.enable_vae_slicing()  # Reduce memory usage
    
    print("✅ Model loaded and ready!")
    return pipe

def generate_image(pipe, prompt, negative_prompt="", steps=20, guidance=7.5, width=512, height=512, seed=None):
    """Generate an image from a text prompt"""
    
    if seed is not None:
        torch.manual_seed(seed)
    
    print(f"🎨 Generating image...")
    print(f"   Prompt: {prompt}")
    if negative_prompt:
        print(f"   Negative prompt: {negative_prompt}")
    print(f"   Steps: {steps}, Guidance: {guidance}, Size: {width}x{height}")
    
    with torch.no_grad():
        result = pipe(
            prompt,
            negative_prompt=negative_prompt if negative_prompt else None,
            num_inference_steps=steps,
            guidance_scale=guidance,
            height=height,
            width=width,
            generator=torch.Generator().manual_seed(seed) if seed else None
        )
    
    return result.images[0]

def main():
    parser = argparse.ArgumentParser(description='Generate images with Stable Diffusion')
    parser.add_argument('--prompt', '-p', type=str, help='Text prompt for image generation')
    parser.add_argument('--negative', '-n', type=str, default='', help='Negative prompt')
    parser.add_argument('--steps', '-s', type=int, default=20, help='Number of inference steps')
    parser.add_argument('--guidance', '-g', type=float, default=7.5, help='Guidance scale')
    parser.add_argument('--width', '-w', type=int, default=512, help='Image width')
    parser.add_argument('--height', type=int, default=512, help='Image height')
    parser.add_argument('--seed', type=int, help='Random seed for reproducible results')
    parser.add_argument('--interactive', '-i', action='store_true', help='Interactive mode')
    
    args = parser.parse_args()
    
    # Setup the pipeline
    pipe = setup_pipeline()
    
    # Create output directory
    os.makedirs("output", exist_ok=True)
    
    if args.interactive or not args.prompt:
        # Interactive mode
        print("\n🎭 Welcome to Interactive Stable Diffusion!")
        print("Type your prompts and press Enter. Type 'quit' to exit.")
        print("You can also use commands like: --steps 30 --guidance 8.0")
        
        while True:
            try:
                user_input = input("\n🖼️  Enter your prompt: ").strip()
                
                if user_input.lower() in ['quit', 'exit', 'q']:
                    print("👋 Goodbye!")
                    break
                
                if not user_input:
                    continue
                
                # Generate timestamp for filename
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                
                # Generate image
                image = generate_image(
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
                filename = f"output/generated_{timestamp}.png"
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
        
        image = generate_image(
            pipe,
            args.prompt,
            negative_prompt=args.negative,
            steps=args.steps,
            guidance=args.guidance,
            width=args.width,
            height=args.height,
            seed=args.seed
        )
        
        filename = f"output/generated_{timestamp}.png"
        image.save(filename)
        print(f"💾 Image saved: {filename}")

if __name__ == "__main__":
    main()
