# Intern exercises

Use the core exercises only at the indicated pauses. The rest are homework. Restart and run notebooks from the top before editing. Keep a copy of your original working notebook.

## E1   Core   1 minute   Center and outliers

At minute 8, predict the mean and median of [1, 2, 3, 4, 100]. Which better describes the typical small value here? Then check S2. Explain why the outlier affects the mean.

## E2   Core   2 minutes   Association

At minute 13, inspect the scatterplot in S4. Is the association positive or negative? Name one reason real study hours and quiz scores might move together without proving causation. Does a near-zero Pearson r rule out every relationship?

## E3   Core   2 minutes   A new prediction

At minute 35, change the S7 input to eight hours and rerun that cell. Write the predicted score and its units. Explain why a 30-hour prediction deserves less trust. Do not refit on the test set.

## E4   Core   1 minute   Trace a tool call

At minute 65, ask about setup with trace=True. Identify the proposed tool name, JSON argument, tool result, and final answer. Which line of Python validates the call? Which component actually executes it?

## E5   Guided core activity   8 minutes, then homework   Extend the agent

At minutes 67–75, use A4b in the chatbot notebook:

1. Open `src/agent.py`. Inside `FAQ`, add `"contact": "Contact training@example.com for this fictional workshop.",` before the existing `"schedule"` entry. Save the file.
2. Restart the notebook kernel and run A1–A4 again in offline mode. A restart is necessary because Python caches imported modules.
3. In A4b, set `RUN_EXTENSION = True` and run the cell. It checks that the schema includes your topic and that the chatbot returns your answer.
4. Ask your partner: did you change the model, the tool's data, or both? Explain why no model retraining was needed.

Expected: a contact tool trace followed by `Contact extension passed`. If time is short, follow the instructor and finish locally later.

Homework (10–15 minutes): add checks for an unsupported topic and malformed JSON. Explain one limitation of the keyword matcher. Leave A4b enabled only after adding the topic; the supplied notebook skips the extension check by default.

## E6   Homework   10 to 15 minutes   Propose Chindi scope

Write five representative user questions and mark which the current FAQ can answer. Choose one deployment option from Architecture.md. Identify three assumptions that must be confirmed. Describe where credentials and session history belong.

## E7   Optional advanced   20 minutes   Residuals and baseline

Using S6 variables, make a scatterplot of predictions against residuals with a horizontal zero line. Compare the model’s MAE with the training-mean baseline. Try random_state=7 by rerunning S5 onward and explain why scores change with only five held-out observations. Do not choose a seed merely because its test score looks better.

## E8   Optional advanced   20 minutes   Tool failure cases

Inject a fake model that requests an unknown tool. Show that the loop receives an error result and then can answer. Test a model that never finishes and verify the round limit. Explain why input validation alone does not solve prompt injection in future document retrieval.
