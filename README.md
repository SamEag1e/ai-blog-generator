# ai-blog-generator

Generate SEO-friendly blog posts using OpenAI (or mocked data) and schedule daily generations with ease. Supports Dockerized or manual execution.

---

## ⚙️ Setup

Before anything, create a `.env` file at the root:

```env
DEBUG=True
MOCK_DATA=False
SEO_DATA_API_KEY=your-seo-data-api-key
OPEN_AI_API_KEY=your-open-ai-api-key
```

> **Note:** Not all keys are used yet — this is intentional. It shows flexibility for future extensions (e.g., SEO_DATA_API_KEY).

---

## 🚀 1. Run with Docker (recommended)

```bash
docker compose up --build -d
```

- API: [http://localhost:5000](http://localhost:5000)
- Daily blog post saved at: `./generated/YYYY-MM-DD.json`

The scheduler runs inside a container, hitting the `/generate?keyword=...` endpoint once every 24 hours:

```bash
KEYWORD="wireless earbuds"
```

You’ll find generated posts inside the `generated/` folder (auto-mounted from the container).

---

## 🐧 3. Manual Run (Linux/macOS)

### Step 1 — Set up environment

```bash
cd path/to/project
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Step 2 — Start the API

```bash
python src/app.py
```

### Step 3 — Trigger generation (using included script)

```bash
bash scripts/generate_daily.sh
```

Or set up a crontab:

```bash
crontab -e
```

Add:

```cron
0 9 * * * /absolute/path/to/your/project/scripts/generate_daily.sh
```

---

## 🪟 2. Manual Run (Windows)

### Step 1 — Set up environment

```powershell
cd path\to\project
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### Step 2 — Start the API

```powershell
python src\app.py
```

### Step 3 — Trigger generation (using included script)

```powershell
powershell -ExecutionPolicy Bypass -File scripts\generate_daily.ps1
```

---

## 📂 Folder Structure

```
project-root/
├── src/
│   ├── app.py
│   ├── config/
│   │   └── cfg.py
│   └── core/
│       ├── ai_generator.py
│       ├── seo_fetcher.py
│       └── utils.py
├── scripts/
│   ├── generate_daily.sh
│   └── generate_daily.ps1
├── generated/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── .env
```

---

## ✅ Summary

| Mode    | Server       | Scheduler         | Notes               |
| ------- | ------------ | ----------------- | ------------------- |
| Docker  | Yes (`web`)  | Yes (`scheduler`) | Cleanest experience |
| Windows | Yes (manual) | PowerShell        | Manual trigger      |
| Linux   | Yes (manual) | Crontab or shell  | Ideal for local dev |
