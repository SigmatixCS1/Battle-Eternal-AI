import torch
from diffusers import StableDiffusionPipeline
import os

def test_stable_diffusion():
    """Test basic Stable Diffusion functionality"""
    print("🚀 Starting Stable Diffusion test...")
    
    # Check if CUDA is available
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"💻 Using device: {device}")
    
    # Load the model (using a smaller, faster model for testing)
    print("📦 Loading Stable Diffusion model...")
    try:
        # Using runwayml/stable-diffusion-v1-5 as it's well-supported
        pipe = StableDiffusionPipeline.from_pretrained(
            "runwayml/stable-diffusion-v1-5",
            torch_dtype=torch.float16 if device == "cuda" else torch.float32,
            safety_checker=None,  # Disable for faster loading
            requires_safety_checker=False
        )
        pipe = pipe.to(device)
        
        # Optimize for memory usage
        if device == "cuda":
            pipe.enable_memory_efficient_attention()
        
        print("✅ Model loaded successfully!")
        
        # Generate a test image
        prompt = "a majestic lion in a mystical forest, digital art, high quality"
        print(f"🎨 Generating image with prompt: '{prompt}'")
        
        with torch.no_grad():
            image = pipe(
                prompt,
                num_inference_steps=20,  # Fewer steps for faster generation
                guidance_scale=7.5,
                height=512,
                width=512
            ).images[0]
        
        # Save the image
        os.makedirs("output", exist_ok=True)
        image_path = "output/test_image.png"
        image.save(image_path)
        
        print(f"🎉 Success! Image saved to: {image_path}")
        print("🔍 You can now view your generated image!")
        
        return True
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return False

if __name__ == "__main__":
    success = test_stable_diffusion()
    if success:
        print("\n✨ Stable Diffusion setup is working correctly!")
    else:
        print("\n⚠️ There were issues with the setup. Check the error messages above.")
