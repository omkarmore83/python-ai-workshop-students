# Python and AI Workshop — Student Pack

A 90-minute beginner workshop for learners who have used Pandas.

**No API key is needed.** The supplied chatbot runs offline by default. Install the dependencies before the session; installation needs internet access.

## Download and start

1. [Download the student pack as a ZIP](https://github.com/omkarmore83/python-ai-workshop-students/archive/refs/heads/main.zip).
2. Extract the ZIP completely. Do not open notebooks inside the ZIP.
3. Open the extracted `python-ai-workshop-students-main` folder in VS Code.
4. Follow **[Setup.md](Setup.md)** to install dependencies and select your notebook kernel.
5. Start with **[01_statistics_regression.ipynb](notebooks/01_statistics_regression.ipynb)**, then **[02_llm_tool_agent.ipynb](notebooks/02_llm_tool_agent.ipynb)**.

GitHub shows notebook previews, but does not execute them. Download the complete folder so imports and data paths keep working.

If you already use Git, you can clone instead:

```bash
git clone https://github.com/omkarmore83/python-ai-workshop-students.git
cd python-ai-workshop-students
```

## What you will do

| Part | Activity |
|---|---|
| Data and regression | Inspect a synthetic dataset, fit a line, and explain a held-out prediction |
| Tool-using chatbot | Trace a validated Python tool call, then add and test a FAQ topic |
| Teach-back | Explain which work belongs to the data, model, and Python application |

The core statistics path is **S1, S2, S4–S7**; S3 distributions is optional. In the chatbot notebook, follow **A1–A5**, including the guided **A4b** contact exercise. Live API and interactive cells are optional and disabled by default.

## Files

- `Setup.md`: student setup, notebook controls, session instructions, and troubleshooting.
- `Exercises.md`: classroom activities and homework.
- `notebooks/`: two notebooks with saved outputs for reference.
- `src/agent.py`: offline chatbot and optional live API adapter.
- `src/test_offline.py`: installation and offline behavior check.
- `data/study_hours.csv`: synthetic teaching data, not real student information.
- `requirements.txt`: dependencies for Python 3.11 or 3.12.
- `Architecture.md` and `Architecture.svg`: teaching diagrams for tracing a tool-call cycle in E6.

The offline chatbot is scripted keyword matching, **not an LLM**. The optional live path uses an API model. This is a notebook-based teaching demo; you do not need to build or host an application.

This student pack intentionally excludes the instructor guide, presentation, and answer key. Keep API keys and personal information out of notebooks, screenshots, and GitHub uploads.
