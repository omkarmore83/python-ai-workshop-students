# Student setup and session guide

## Before the session

Allow 20–30 minutes. You need:

- Python **3.11 or 3.12**.
- VS Code with Microsoft's **Python** and **Jupyter** extensions, or a browser for JupyterLab.
- Internet access to download this pack and install dependencies.

You do not need Git, an API account, an API key, or paid model access. Use the offline defaults.

Extract the complete ZIP first. Keep `notebooks`, `src`, and `data` together. In VS Code, choose **File > Open Folder** and open the extracted project folder. Then choose **Terminal > New Terminal**. The terminal should start in the folder containing `requirements.txt`.

## 1. Create your environment

### macOS or Linux

Check your Python:

```bash
python3 --version
```

If it is 3.11 or 3.12, run:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m ipykernel install --user --name python-ai-workshop --display-name "Python AI Workshop"
```

If your default Python is another version, install Python 3.12 from [python.org](https://www.python.org/downloads/) and use `python3.12 -m venv .venv` for the first command. Use a separate environment rather than installing into an Anaconda base environment.

### Windows PowerShell

Install Python 3.12 from [python.org](https://www.python.org/downloads/) if needed. Then run:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m ipykernel install --user --name python-ai-workshop --display-name "Python AI Workshop"
```

If Python 3.11 is installed instead, use `py -3.11` in the first command. Calling the environment's Python directly avoids PowerShell activation-policy issues.

## 2. Check the installation

From the project root, run the command for your system:

macOS/Linux, with the environment activated:

```bash
python src/test_offline.py
```

Windows PowerShell:

```powershell
.\.venv\Scripts\python.exe src\test_offline.py
```

Expected: both notebook names print `PASS`, and the final line is `Offline checks passed`. This executes the offline examples, checks the guided exercise in isolation, and regenerates the synthetic CSV. It does not require credentials, contact an API, or overwrite your notebook outputs.

## 3. Run in VS Code

1. Open `notebooks/01_statistics_regression.ipynb`.
2. Click **Select Kernel** at the top right. Choose **Python AI Workshop**. If it is not listed, choose **Python Environments** and select this folder's `.venv/bin/python` on Mac/Linux or `.venv\Scripts\python.exe` on Windows.
3. Use **Restart Kernel**, then **Run All** for your pre-session check. Charts and tables should appear below the cells.
4. Open `notebooks/02_llm_tool_agent.ipynb` and choose the same kernel.
5. For the first run, keep `MODE = 'offline'`, `RUN_EXTENSION = False`, and `RUN_CHAT = False`. Run all cells. The contact exercise and live request should say they are skipped or ready; this is expected.

Run one selected cell with **Shift+Enter**. Cells must run in order because later cells use variables created earlier. Save your work with **Cmd+S** on Mac or **Ctrl+S** on Windows/Linux.

## Or use JupyterLab in a browser

From the project root:

macOS/Linux:

```bash
source .venv/bin/activate
python -m jupyterlab --notebook-dir=notebooks
```

Windows PowerShell:

```powershell
.\.venv\Scripts\python.exe -m jupyterlab --notebook-dir=notebooks
```

Open the local browser address printed in the terminal. Do not share its access token. Select the **Python AI Workshop** kernel, open a notebook, and choose **Run > Restart Kernel and Run All Cells** for the first check.

Keep the terminal open while working. Stop Jupyter with **Ctrl+C** in that terminal when finished. To edit `src/agent.py` for the exercise, open the extracted project folder in VS Code or another text editor.

## During the session

Follow the instructor rather than running ahead:

| Minutes | Notebook activity |
|---|---|
| 0–15 | S1, S2, then S4; skip optional S3 |
| 15–40 | S5–S7; change the prediction input to eight hours |
| 40–50 | Discussion: numeric predictions, tokens, and tools |
| 50–67 | A1–A4; read the tool trace |
| 67–75 | A4b; add and test your contact topic |
| 75–80 | A5; inspect boundary checks |
| 80–90 | Architecture discussion, recap, and homework |

### Contact exercise: why restarting matters

In `src/agent.py`, add this entry inside `FAQ`, before the existing `"schedule"` entry:

```python
"contact": "Contact training@example.com for this fictional workshop.",
```

Save the file. Restart the chatbot notebook's kernel, then rerun A1–A4 in offline mode. In A4b, change `RUN_EXTENSION = False` to `RUN_EXTENSION = True` and run the cell. Expected: a contact tool trace and `Contact extension passed`.

Python caches imported modules: saving the source file alone does not reload it. The address is fictional. You changed the tool's data and the derived schema, not model weights.

Keep `RUN_EXTENSION = False` until you have added the topic. Leave `RUN_CHAT = False` unless you deliberately want the optional cell to wait for typed questions.

## Return another day

Reopen the folder and choose the same notebook kernel. No reinstall is needed. If using a terminal on Mac/Linux, activate the environment again with `source .venv/bin/activate`. On Windows, continue using `.\.venv\Scripts\python.exe`.

## Troubleshooting

| Problem | What to do |
|---|---|
| `python3` or `py` not found | Install Python 3.12; reopen the terminal |
| `ModuleNotFoundError` | Select the workshop kernel and install requirements using that environment's Python |
| Kernel does not appear | Rerun the kernel registration command, then reload VS Code |
| Cannot import `agent` or find the CSV | Extract the full project, preserve the folder structure, and open notebooks from `notebooks` |
| Contact check fails | Check the dictionary entry, save `src/agent.py`, restart the kernel, and rerun A1–A4 |
| Cell waits for input | Interrupt the kernel and set `RUN_CHAT = False` |
| Notebook shows old results | Restart the kernel and run cells in order |
| Live API error | Return to `MODE = 'offline'`; live mode is not required |
| Installation fails before class | Save the error text for the instructor; use the supplied notebook outputs or pair with a classmate |

To check the selected interpreter, run this in a notebook cell:

```python
import sys
print(sys.executable)
```

It should point to the extracted project's `.venv` environment.

## Optional live API path

Live mode is not needed for this session. It requires an OpenAI API account with quota, access to a tool-capable model, and the environment variables `OPENAI_API_KEY` and `OPENAI_MODEL` configured **before** launching Jupyter. Calls can incur charges. A ChatGPT subscription is not API credit.

Ask the instructor before enabling live mode. Never put credentials into source files, notebooks, screenshots, or GitHub issues. This pack does not automatically load `.env` files.
