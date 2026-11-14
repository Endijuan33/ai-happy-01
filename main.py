import os
import shutil

# Entry image: two small white robots exchanging yellow daisies with each
# other at golden sunset, both beaming with joy — mutual joy, not one
# robot giving while the other only receives. The image is palette
# quantized to 256 colors so the 1024x1024 PNG stays under the 1 MiB cap.
# The program only copies the committed image bytes, so both runs write
# exactly the same file.
OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(OUT, exist_ok=True)
shutil.copyfile(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png"),
    os.path.join(OUT, "entry.png"),
)
