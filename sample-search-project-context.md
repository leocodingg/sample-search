# Project Context: Getting Hired at AI/Infra Startups via Project-Based Learning

## Who I am
- Leo, junior CS student at NYU Tandon (transferred from another school).
- Prior internships: PersonifyAI and Turing. ML research background.
- Music producer — I have my own sample library.
- Come from C++/Java (OOP course CS-UY 2124). Now writing Python; syntax/idiom transfer mistakes are a recurring issue.
- Doing interview prep through the NeetCode 150 (currently around Arrays/Hashing and Two Pointers; have also covered heaps, DP, graphs, monotonic stack).
- Targeting Summer 2027 engineering internships, and new-grad roles after that.

## Where this started
I saw a TikTok showing Lightspeed-backed companies named to Redpoint's InfraRed 100 (2026). The video framed them as "upside" tech sales jobs. I am NOT interested in sales — I want to be hired as an **engineer** at companies like these.

Companies on the list: Anthropic, Arctic Wolf, Chainguard, ClickHouse, Cyera, Databricks, Docker, ElevenLabs, Emergent, Eon, Exa, Fireworks AI, Glean, Grafana Labs, Inferact, Judgment Labs, Mistral AI, Nexthop AI, Patronus AI, Raindrop, Reactor, ScaleOps, Semgrep, Sphinx, Stripe, Supabase, Temporal.

What they have in common: mostly infra/AI-tooling startups selling to developers. They hire people who already understand their product and its users.

## Strategy to become a strong candidate (engineering)
1. **Contribute to their open source.** ClickHouse, Supabase, Temporal, Grafana, Semgrep, Docker, Chainguard have public repos. Merged PRs are the strongest signal, and their engineers review them (doubles as networking). Biggest lever — almost no students do this seriously.
2. **Build one deep project on their kind of stack.** Depth over breadth. Must be able to explain every design tradeoff.
3. **Use my ML research.** Anthropic, Mistral, Fireworks, Patronus, Judgment Labs, ElevenLabs value it. Make it public: paper, writeup, or reproducible repo.
4. **Get referrals.** NYU alumni at these companies; short, specific messages ("I fixed X in your repo, I'm interested in Y team"). Cold apps to hot startups mostly get filtered.
5. **Clear the interview bar.** LeetCode mediums fluently + system design basics. Infra companies often use practical coding rounds — practice building small working systems under time pressure.
6. **Write publicly.** Blog posts explaining technical things I did signal depth.

## Timeline reality check
- Not too late as a junior: ~1.5 years before graduation, AI tooling is new for everyone, startups hire on rolling basis (often spring), and new-grad 2028 is the bigger prize.
- Big tech Summer 2027 recruiting is happening now (fall 2026) — apply to those in parallel with the long-term work.
- Using AI to write code doesn't make me good; understanding what it generates does. These companies test reasoning about systems without AI.
- Locking in means: learn fundamentals (systems, databases, networking, concurrency) with AI as a tutor, not a crutch; build one real project I can defend line by line; keep grades steady this semester.

## How I want to learn
Project-based learning. I write the code myself; AI explains, hints, and reviews.

## Project choice and reasoning
- Chose an audio + ML project because it fits my music production, my ML background, and ElevenLabs directly, while forcing me through the infra skills the rest of the list cares about.
- Considered my other idea, **Lapse** (peer accountability app, Next.js/Supabase/Tailwind, PRD drafted) — solid product app, but teaches less of the infra depth these companies screen for.
- Originally considered a stem separation service. Dropped it as the core: it's mostly someone else's model (Demucs) in a wrapper, and it already exists (Moises, LALAL.AI).
- **On novelty:** for a hiring project, novelty matters less than depth — "did this person build something hard, make real engineering decisions, and understand them?" A twist still makes it more memorable. Similar-sample search exists (Splice, Cosmos), but those search their own catalogs, not mine.

## THE PROJECT: Local text-to-sample search
**One line:** describe a sound in plain English and find it in my own sample library.

Example: type "dusty jazz piano, 90 BPM" → get the closest matching samples from folders on my computer. Runs fully local and private (a real selling point for producers with unreleased music).

### How it works
1. An ML model (CLAP — audio-text embedding model) converts each audio file into an embedding: a list of numbers capturing what it sounds like.
2. Embeddings are stored in a database built for similarity search (Postgres + pgvector).
3. A text description is converted into an embedding by the same model; the database returns the closest audio.
4. A web API and a background job queue handle the slow parts (indexing thousands of samples).

### Roadmap (each layer teaches a core skill)
1. **Core** — CLAP search over a handful of samples in one Python script. *ML inference, audio basics.*
2. **API** — wrap it in FastAPI. *HTTP, async, API design.*
3. **Queue** — background workers to index large libraries. *Concurrency, distributed systems (Temporal/Docker territory).*
4. **Storage + search** — Postgres + pgvector, indexing. *Databases, vector search (Supabase/ClickHouse territory).*
5. **Ship** — containerize, deploy, add monitoring. *Docker, deployment, observability (Grafana territory).*
6. **Optional later** — stem separation (Demucs), then search my library for samples similar to each stem.

Other twist ideas considered: sample source detection (identify which samples/loops a beat used — hard but interesting).

What it proves to employers: ML inference, databases and vector search, APIs, concurrency, deployment — all in one project demoable in 30 seconds.

## Week 1
**Goal:** get CLAP running on 10 of my own samples and print which one best matches a typed text description.

**Setup (boilerplate, OK to copy):**
```bash
mkdir sample-search && cd sample-search
python3 -m venv .venv
source .venv/bin/activate
pip install torch transformers librosa numpy
```
Put 10 varied samples (drums, piano, vocal chop, bass, etc.) in a `samples/` folder.

**Write `search.py` myself. It should:**
1. Load `ClapModel` and `ClapProcessor` from Hugging Face, model `laion/clap-htsat-unfused`.
2. Loop over files in `samples/`, load each with `librosa.load`.
3. Embed each clip with `model.get_audio_features`.
4. Take a text query from the command line, embed it with `model.get_text_features`.
5. Compute cosine similarity between the text embedding and each audio embedding.
6. Print samples ranked best to worst.

**Gotchas:**
- CLAP expects audio at 48 kHz — use `sr=48000` in `librosa.load`.
- Wrap inference in `with torch.no_grad():`.
- Normalize embeddings before comparing.
- Java habit check: no main class; use `if __name__ == "__main__":` and `sys.argv`.

Also to do this week: create the repo with a README stating the goal.

## Rules for how Claude should help me in this project
- Don't write the project for me. Explain, give the smallest hint that unblocks me, and review my code.
- If you give me code, I retype it and must be able to explain every line.
- Reviews should cover: bugs, edge cases, Python idioms I'm getting wrong (C++/Java transfer), and design tradeoffs.
- Keep responses short and direct. No praise padding. If I'm wrong, say so and why.
- Keep grades steady this semester — the project doesn't replace them.
