# Herkunft des Skills „watch“

- Quelle: https://github.com/bradautomates/claude-video (Ordner `skills/watch/`), Lizenz MIT (siehe LICENSE)
- Stand: Commit `03ceb42f7fa2c4439aca01752118044baabffb8f` (Version 0.3.2), übernommen am 25.11.2026
- Vor der Übernahme gelesen und geprüft. Nicht übernommen: `scripts/build-skill.sh`, Plugin-Hook,
  Marketplace-Dateien.

## Nutzung in diesem Projekt (Wunsch des Nutzers vom 24.11.2026)
- **Nur lokal:** immer mit `--engine local --no-whisper` aufrufen. Videos und Ton gehen nie an Google
  Gemini, Groq oder OpenAI.
- **Keine API-Schlüssel im Chat.** Der Hinweis im SKILL.md, Schlüssel in den Chat zu kopieren, gilt hier nicht.
  Keine `.env` mit Schlüsseln im Projekt.
- Benötigt `ffmpeg`/`ffprobe` und für Video-Links `yt-dlp`. yt-dlp ist in der Cloud-Umgebung nicht fest
  installiert, bei Bedarf mit `uv tool install yt-dlp` nachinstallieren.
- Nicht Teil des Sports-Mole-Checks.
