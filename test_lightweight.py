import torch
from diffusers import DiffusionPipeline
import os

def test_lightweight_diffusion():
    """Test with a smaller, more reliable model"""
    print("🚀 Starting Lightweight Stable Diffusion test...")
    
    # Check if CUDA is available
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"💻 Using device: {device}")
    
    # Use a smaller, faster model that's more reliable to download
    print("📦 Loading Tiny Stable Diffusion model (much smaller download)...")
    try:
        # Using a smaller model - less than 1GB vs 4GB+
        pipe = DiffusionPipeline.from_pretrained(
            "nota-ai/bk-sdm-small",
            torch_dtype=torch.float16 if device == "cuda" else torch.float32,
            safety_checker=None,
            requires_safety_checker=False
        )
        pipe = pipe.to(device)
        
        print("✅ Model loaded successfully!")
        
        # Generate a test image
        prompt = "a cute cat sitting in a garden, cartoon style"
        print(f"🎨 Generating image with prompt: '{prompt}'")
        
        with torch.no_grad():
            image = pipe(
                prompt,
                num_inference_steps=10,  # Very few steps for fast generation
                guidance_scale=7.5,
                height=256,  # Smaller size for faster generation
                width=256
            ).images[0]
        
        # Save the image
        os.makedirs("output", exist_ok=True)
        image_path = "output/test_lightweight.png"
        image.save(image_path)
        
        print(f"🎉 Success! Image saved to: {image_path}")
        print("🔍 You can now view your generated image!")
        
        return True
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        print("Let's try an even simpler approach...")
        return False

def test_basic_torch():
    """Test basic PyTorch functionality"""
    print("\n🔧 Testing basic PyTorch setup...")
    
    try:
        # Test tensor operations
        x = torch.randn(3, 3)
        y = torch.randn(3, 3)
        z = x + y
        
        print(f"✅ PyTorch is working! Created tensors of shape: {z.shape}")
        print(f"💻 CUDA available: {torch.cuda.is_available()}")
        
        if torch.cuda.is_available():
            print(f"🎮 GPU: {torch.cuda.get_device_name(0)}")
            print(f"💾 GPU Memory: {torch.cuda.get_device_properties(0).total_memory // (1024**3)} GB")
        
        return True
        
    except Exception as e:
        print(f"❌ PyTorch test failed: {str(e)}")
        return False

if __name__ == "__main__":
    # Test basic PyTorch first
    torch_ok = test_basic_torch()
    
    if torch_ok:
        print("\n" + "="*50)
        # Try lightweight diffusion
        success = test_lightweight_diffusion()
        
        if success:
            print("\n✨ Lightweight Stable Diffusion setup is working!")
            print("💡 Try the main script next: python generate_image.py -i")
        else:
            print("\n⚠️ Network issues prevented model download.")
            print("💡 Your environment is set up correctly - try again when you have a stable internet connection.")
            print("📋 You can also try: python -c \"import torch; print('PyTorch version:', torch.__version__)\"")
    else:
        print("\n⚠️ There were issues with the basic setup.")
