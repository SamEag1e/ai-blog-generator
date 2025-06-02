# ai-blog-generator-interview-samad-taghinejad

Backend Interview

- This line was a little ambiguous: "A module (ai_generator.py) that calls OpenAI with a structured prompt to generate a blog post draft (HTML or Markdown), replacing {{AFF_LINK_n}} placeholders with dummy URLs."
- I went with this:
  “The AI response includes affiliate placeholders like {{AFF_LINK_1}}, which the backend replaces with dummy URLs like https://dummyurl.com/a1.”

- If you're on Windows, you’d use the Task Scheduler to run the PowerShell script daily.
- open PowerShell as Administrator if permission issues pop up
- powershell -ExecutionPolicy Bypass -File .\scripts\generate_daily.ps1

- linux
- crontab -e
- 0 9 \* \* \* /absolute/path/to/your/project/scripts/generate_daily.sh
- bash scripts/generate_daily.sh
