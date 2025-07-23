@echo off
echo Battle-Eternal Logo Generator
echo ============================
echo.
echo Choose a logo variation:
echo 1. Basic Logo
echo 2. Character + Logo (Alexander)
echo 3. Gaming UI Logo
echo 4. Neon Sign Logo
echo 5. Custom prompt
echo.
set /p choice="Enter your choice (1-5): "

if "%choice%"=="1" (
    venv\Scripts\python.exe generate_anything_v5.py --battle-eternal --width 768 --height 512 -p "3D text logo BATTLE ETERNAL, bright cyan blue glowing letters, futuristic font, dark gradient background, neon glow effect, metallic finish, professional gaming logo, high contrast, detailed 3D rendering"
)
if "%choice%"=="2" (
    venv\Scripts\python.exe generate_anything_v5.py --battle-eternal -p "anime style Alexander with BATTLE ETERNAL logo backdrop, blonde hair, glasses, red hoodie, magical cards, cyan blue mystical energy, detailed art, logo prominently displayed"
)
if "%choice%"=="3" (
    venv\Scripts\python.exe generate_anything_v5.py --battle-eternal --width 768 --height 512 -p "gaming UI interface featuring BATTLE ETERNAL logo, glowing cyan text, dark HUD elements, futuristic design, anime art style, professional game interface"
)
if "%choice%"=="4" (
    venv\Scripts\python.exe generate_anything_v5.py --battle-eternal --width 768 --height 512 -p "BATTLE ETERNAL neon sign, bright cyan blue lights, dark urban background, futuristic atmosphere, glowing letters, night scene"
)
if "%choice%"=="5" (
    set /p custom_prompt="Enter your custom prompt: "
    venv\Scripts\python.exe generate_anything_v5.py --battle-eternal -p "%custom_prompt%"
)

echo.
echo Generation complete! Check the output folder for your image.
pause
