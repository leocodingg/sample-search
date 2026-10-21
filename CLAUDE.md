# sample-search — context for AI assistants

## What this is
Local text-to-sample search: type a plain-English description ("dusty jazz piano, 90 BPM") and get the closest-matching audio samples from my own library. Runs fully local and private.

Built as a learning/portfolio project for engineering roles at AI/infra startups. Depth over breadth: I need to be able to defend every line and design tradeoff.

## How it works
1. CLAP (`laion/clap-htsat-unfused`, Hugging Face) turns each audio file into a 512-number embedding.
2. A text query is embedded by the same model into the same space.
3. Cosine similarity ranks the samples against the query.
4. Later: embeddings stored in Postgres + pgvector; FastAPI API; background workers for indexing.

## Roadmap
1. **Core**: CLAP search over ~10 samples in one script (`search.py`). ← current
2. **API**: FastAPI wrapper.
3. **Queue**: background workers to index large libraries.
4. **Storage + search**: Postgres + pgvector.
5. **Ship**: Docker, deploy, monitoring.
6. Optional: stem separation (Demucs), then search per stem.

## Current status (Week 1)
- Done: venv setup, model loads, `librosa.load(..., sr=48000)` works.
- Next: processor → `model.get_audio_features` inside `torch.no_grad()`, print embedding shape; then text embedding, normalize, cosine similarity, ranked output, query from `sys.argv`.
- Open question: CLAP only sees ~10 s (processor randomly crops longer files). How to handle full-length loops/tracks?

## Environment
- Python 3.12, venv in `.venv/` (not committed). Install: `pip install -r requirements.txt`.
- I work on both Windows (PowerShell) and macOS. Give commands for the one I'm on.
- `samples/` is gitignored (my own audio); each machine has its own copy.

## Rules for helping me
- Don't write the project for me. Explain, give the smallest hint that unblocks me, and review my code.
- If you give code, I retype it and must be able to explain every line, so explain it.
- Reviews cover: bugs, edge cases, Python idioms I'm getting wrong (I come from C++/Java), and design tradeoffs.
- Keep responses short and direct. No praise padding. If I'm wrong, say so and why.


