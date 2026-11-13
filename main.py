import os
import shutil

# Entry image: a small robot shyly offering a daisy to a taller robot at
# sunset. The program only copies the committed image bytes, so both runs
# write exactly the same file.
OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(OUT, exist_ok=True)
shutil.copyfile(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png"),
    os.path.join(OUT, "entry.png"),
)
