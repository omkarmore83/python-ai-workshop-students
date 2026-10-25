"""Run from package root: python src/test_offline.py"""
import json
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from agent import Chatbot, dispatch, FAQ, TOOLS
root = Path(__file__).resolve().parents[1]
import os
os.chdir(root / "notebooks")
for name in ["01_statistics_regression.ipynb", "02_llm_tool_agent.ipynb"]:
    nb = json.loads(Path(name).read_text())
    scope = {"__name__": "__main__"}
    for cell in nb["cells"]:
        if cell["cell_type"] == "code":
            exec(compile("".join(cell["source"]), name, "exec"), scope)
    plt.close("all")
    print(name, "PASS")
assert "error" in json.loads(dispatch("unknown", "{}"))
assert Chatbot().ask("weather") == "Ask about schedule, setup, or homework."

# Verify the classroom statistics path without the optional distribution cell.
nb = json.loads(Path("01_statistics_regression.ipynb").read_text())
scope = {"__name__": "__main__"}
skip_next = False
for cell in nb["cells"]:
    if cell["cell_type"] == "markdown":
        skip_next = "".join(cell["source"]).startswith("## S3 ")
    elif cell["cell_type"] == "code" and not skip_next:
        exec(compile("".join(cell["source"]), "statistics core path", "exec"), scope)
plt.close("all")
print("Statistics core path without S3 PASS")

# Reproduce the learner's source edit in an isolated namespace, not the real file.
source = (root / "src" / "agent.py").read_text()
entry = '    "contact": "Contact training@example.com for this fictional workshop.",\n'
extension_scope = {"__name__": "contact_exercise"}
if "contact" not in FAQ:
    assert source.count('    "schedule":') == 1
    source = source.replace('    "schedule":', entry + '    "schedule":', 1)
exec(compile(source, "contact exercise agent", "exec"), extension_scope)
nb = json.loads(Path("02_llm_tool_agent.ipynb").read_text())
for cell in nb["cells"]:
    code = "".join(cell["source"])
    if cell["cell_type"] == "code" and "RUN_EXTENSION = False" in code:
        exec(compile(code.replace("RUN_EXTENSION = False", "RUN_EXTENSION = True", 1),
                     "enabled A4b", "exec"), extension_scope)
        break
else:
    raise AssertionError("Missing A4b contact exercise")
assert "error" in json.loads(extension_scope["dispatch"]("lookup_faq", "broken json"))
assert "error" in json.loads(extension_scope["dispatch"]("lookup_faq", '{"topic":"unknown"}'))
assert TOOLS[0]["function"]["parameters"]["properties"]["topic"]["enum"] == list(FAQ)
print("Guided contact extension and failure checks PASS")
print("Offline checks passed")
