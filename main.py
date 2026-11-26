# One-Line Office Jokes (make.fun): write the winning one-liner to entry.txt.
import os

joke = "Our Monday meeting could've been an email, but then Karen couldn't perform her interpretive dance about Q3 synergy."

if not (1 <= len(joke) <= 199):
    raise ValueError("Joke length must be 1-199 characters")
if '\n' in joke or '\r' in joke:
    raise ValueError("Joke must be a single line")
if not joke.strip():
    raise ValueError("Joke cannot be only whitespace")

output_dir = os.environ.get('MAKEFUN_OUTPUT_DIR', '/output')
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, 'entry.txt')

with open(output_path, 'w') as f:
    f.write(joke)

print(output_path, len(joke))
