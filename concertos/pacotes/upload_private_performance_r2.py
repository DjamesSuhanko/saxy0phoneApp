#!/usr/bin/env python3
import hashlib, subprocess
from pathlib import Path
p = Path(__file__).resolve().with_name("private_performance.zip")
expected = "083dbb2d109e934826e0d89b575a9c5e5056b268f5e62701a63317f277a079e5"
if hashlib.sha256(p.read_bytes()).hexdigest() != expected:
    raise SystemExit("SHA-256 divergente: upload cancelado.")
subprocess.run(["wrangler", "r2", "object", "put", "saxy0phone-paid-packages/private_performance.zip", f"--file={p}", "--remote", "--content-type=application/zip"], check=True)
print("Upload concluído.")
