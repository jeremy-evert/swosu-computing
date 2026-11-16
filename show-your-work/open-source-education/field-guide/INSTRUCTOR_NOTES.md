# Instructor notes: a first workshop from the LLM Dungeon

**Candidate teaching resource · November 16, 2026 · Not independently reviewed or pilot-tested**

Companion: [18-chapter Lesson Map](LESSON_MAP.md). This is a **sample** session and assessment skeleton, not an approved three-credit course or substitute for institution-specific information security training.

## Overview and intended audience

**Audience:** introductory computing students or educators who know how to open a browser but may not have written HTML.  
**Sample session:** **45 minutes**, one small, text-only webpage, optional demonstration audio.  
**Prerequisites:** computer with a modern browser; text editor; optional GitHub account. The instructor may project screenshots rather than request participants to create cloud accounts.  
**Lesson objective:** learners can design and verify a tiny accessible form, identify who can see its data, and explain why successful automated tests must match real user interaction.

### Learning objectives (observable)

By the end of this *sample workshop*, the learner can:
1. Explain one concrete risk of connecting an AI assistant to a real email account and name a safe mock-data alternative.
2. Create a minimal HTML clue/answer form with a button that submits on click **and** Enter.
3. Demonstrate a clear assisted/not-assisted state and describe why they should be distinguished.
4. Show a simple source record for a knowledge claim, with a human reviewer identified.
5. List two checks required before putting an educational page on the public web.

### Materials and accessibility

- A code editor and browser with developer tools (or printed source/code walkthrough).
- Fictional, instructor-generated email examples or source documents; **no real institutional inbox**.
- Instructor-provided starter HTML, optionally in a public class repository after checking rights.
- Captions/transcripts for any narration. Audio must be user-triggered and stoppable; the task must be doable entirely with visual text and keyboard.
- Large labeled targets, visible focus, no color-only error messages, reduced-motion option for animation, and a chance to work without Gmail or paid accounts.

## Proposed 45-minute workshop

| Minutes | Instructor action | Learner evidence |
|---|---|---|
| 0–5 | State the problem: an answer button works by Enter but not mouse; ask how we'd find it | One observable acceptance criterion |
| 5–10 | Show fictional inbox and discuss what changes when a connector gets OAuth rights | Three-sentence permission note |
| 10–20 | Demonstrate the HTML form and submit handling; let students modify a field/label | Working basic page |
| 20–30 | Test Enter, mouse, keyboard focus and touch or responsive view; compare scripts | A real bug reproduction and fixed behavior |
| 30–38 | Add a help hint and feedback; distinguish correct after help vs independent | A tiny state/output sketch |
| 38–45 | Review public release gates: no secrets/data, attribution, accessibility, URL outside local machine | Exit-ticket answers and a short publication checklist |

**Teacher discretion:** spread this across two lessons if participants are learning HTML syntax from zero. Do not require live Gmail setup or GitHub account creation as the first class activity.

## Two worked examples

### Worked example A: The Check it form

The following is **an original minimal demonstration** and not a copy of production WordWild source:

```html
<form id="practice">
  <label for="answer">Your answer</label>
  <input id="answer" name="answer" autocomplete="off" required>
  <button type="submit">Check it</button>
</form>
<p id="feedback" role="status" aria-live="polite"></p>
<script>
const form = document.getElementById("practice");
form.addEventListener("submit", (event) => {
  event.preventDefault();
  const answer = form.elements.namedItem("answer").value.trim();
  document.getElementById("feedback").textContent =
    answer ? "Answer received. Review the explanation next." : "Please enter an answer.";
});
</script>
```

**What to notice:** One `type="submit"` is sufficient. The browser's form submit event supports both mouse clicks and Enter; we don't need a separate scoring path for each. This example **does not grade spelling** and stores no answers. Do not add an answer in pre-reveal DOM or a secret data attribute.

**Failure experiment:** replace the button type with `type="button"`. The button no longer submits the form; Enter may continue to work. Try both methods. Restore the correct type and write a test that clicks the control.

**Question:** Which automated test could miss this? A test that exclusively presses Enter. Which test would expose it? A click or keyboard-activation test on the actual button.

### Worked example B: Evidence beats a convincing model answer

**Candidate claim:** “This spelling trick will improve children's learning.” A model can produce an appealing explanation and a child may enjoy the joke, but neither is evidence of a causal learning gain.

Build a miniature claim ledger:

| Claim | Source | Supported? | Next human check |
|---|---|---|---|
| `supper` has two written P's | Check the literal word | Yes, a word-specific observation | Teacher confirms the exact spelling and cue |
| Double P means two distinct spoken /p/ sounds here | Ordinary pronunciation is not two separate /p/ phonemes | No | Remove misleading explanation |
| Learners remember it better because of a joke | No study of this game supplied | Not established | Try a controlled/appropriate assessment design and report limitations |

**Discussion:** What changed when we separated the spelling observation from the effectiveness claim? The first can be verified by inspecting the word; the second needs appropriate real learning evidence and cannot be inferred from an assistant's confidence.

## Six candidate formative questions and answer key

1. **Why use three fictional emails instead of connecting a real mailbox?**  
   **Key:** to practice the same summarization or response-planning workflow while avoiding disclosure of private mail, contacts, student information and unnecessary authorization. A real connection has permissions and potential actions the fictional task does not.
2. **What is a real browser action that can expose a bug Enter-only tests miss?**  
   **Key:** clicking the Check it button or tapping it on a phone; test the native submit path and actual UI behavior.
3. **Is an AI-generated explanation a reliable source for a phonics generalization?**  
   **Key:** no; check a qualified source, precisely state when a rule applies, and have an appropriate educator review it.
4. **What is the standard meaning of RAG and why require source citations?**  
   **Key:** Retrieval-Augmented Generation; it retrieves source material as context but the response can still be wrong. Citations let an evaluator inspect claims against retrieved evidence.
5. **A user likes an animated joke, and a unit test passes. What can we conclude?**  
   **Key:** the joke received positive feedback and the code satisfied a specific tested behavior; neither by itself demonstrates durable learning.
6. **A game loads on localhost but its public link is broken. Is it deployed?**  
   **Key:** not successfully for other users. Verify the actual public URL, asset paths, license and permissions from an independent browser.

**Use:** quick verbal check, exit ticket or peer conversation, not a high-stakes assessment. Questions and keys are draft teaching supports, **not validated psychometric items**.

## Suggested eventual course assessment rubric (draft)

| Criterion | What a satisfactory submission shows |
|---|---|
| **Problem and usefulness** | Named learner/task and one demonstrably functional interaction |
| **Responsibility** | Fictional/authorized data only, least privilege, human approvals, no public secrets |
| **Evidence** | Original source claims and known uncertainties distinguished from model-generated guesses |
| **Accessibility** | Keyboard, mouse, small screen, accessible error and optional/no audio |
| **Testing** | Real browser click path, failure state, reproducible test receipt |
| **Release** | Public link, documented rights/credits, honest limitations, version and correction plan |

Do not score a learner's personal choice to connect Gmail as better than a simulated exercise. Different providers and subscriptions must remain optional.

## Contributor rights, AI use and current limitations

- Lesson text and code above were drafted with ChatGPT assistance under instructor direction and remain pending human review and license selection.
- Before later OER Commons/OpenStax/Carpentries contributions, inspect the **recipient's** AI policy and rights rules. The Carpentries, in particular, restricts AI-automated upstream contributions and requires human-led descriptions.
- OpenAI's `gpt-4o-mini-tts` is deprecated as of this draft and scheduled to shut down on January 6, 2027. Never present API credentials or a soon-to-expire model endpoint as a permanent novice tutorial. Official guide: https://developers.openai.com/api/docs/guides/text-to-speech
- Gmail connector availability and permission controls may vary; refresh provider support pages just before class:
  - ChatGPT: https://help.openai.com/en/articles/11487775-connected-apps-in-chatgpt
  - Claude: https://support.claude.com/en/articles/10166901-use-google-workspace-connectors
  - Gemini: https://support.google.com/gemini/answer/15229592
- WordWild code, Kokoro audio and other assets have separate documented provenance; see https://github.com/jeremy-evert/oeqa_spell_roller_public/blob/main/wordwild/ASSETS.md. Do not assume public display gives unlimited reuse rights.
- No independent teacher/literacy specialist has approved this draft; no claim of measured learning improvement; no student account, research study or external OER publication was undertaken in preparation.

## Readiness for the next iteration

The **18-module map, this instructor sample, and the public guide page** together comprise a **proposed teacher-package outline**. To become a publishable OER course, add full lesson scripts, tested project files, step-by-step alternatives for no-account students, verified screenshots, disability/accessibility review, rights/licensing approval, and independent instructor feedback. Do not mark this complete simply because it is available at a public URL.
