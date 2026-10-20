import os
import shutil
import subprocess
import tempfile

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
base_dir = r"C:\Users\Admin\.gemini\antigravity-ide\scratch\backend_repo"
assets_dir = os.path.join(base_dir, "assets")
temp_dir = tempfile.gettempdir()

jobs = [
    {
        "html": os.path.join(assets_dir, "step4.html"),
        "temp_png": os.path.join(temp_dir, "erd_step4_initial.png"),
        "dest_png": os.path.join(assets_dir, "erd_step4_initial.png"),
        "width": 1540,
        "height": 1150
    },
    {
        "html": os.path.join(assets_dir, "step5.html"),
        "temp_png": os.path.join(temp_dir, "erd_step5_normalized.png"),
        "dest_png": os.path.join(assets_dir, "erd_step5_normalized.png"),
        "width": 1540,
        "height": 1150
    },
    {
        "html": os.path.join(assets_dir, "schema.html"),
        "temp_png": os.path.join(temp_dir, "relational_schema.png"),
        "dest_png": os.path.join(assets_dir, "relational_schema.png"),
        "width": 1540,
        "height": 1180
    }
]

for job in jobs:
    file_url = "file:///" + job["html"].replace("\\", "/")
    cmd = [
        chrome_path,
        "--headless=new",
        "--no-sandbox",
        "--disable-gpu",
        f"--window-size={job['width']},{job['height']}",
        f"--screenshot={job['temp_png']}",
        file_url
    ]
    print(f"Rendering {job['html']} -> {job['dest_png']}...")
    res = subprocess.run(cmd, capture_output=True, text=True)
    if os.path.exists(job["temp_png"]):
        shutil.copy2(job["temp_png"], job["dest_png"])
        print(f"Successfully created {job['dest_png']} ({os.path.getsize(job['dest_png'])} bytes)")
    else:
        print(f"Error rendering: {res.stderr}")

print("All diagrams rendered successfully!")
