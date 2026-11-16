# Escape the LLM Dungeon: Build Something Playable Without Getting Fired

**Working draft v0.1 · November 16, 2026 · Not a completed or reviewed course**

**Audience:** SWOSU students, faculty, educators, curious builders, and anyone who wants to make an approachable interactive learning resource without putting real users, data, or institutional systems at risk. Some activities require a computer and personal or institutionally approved accounts. Other platforms are optional.

**What this really teaches:** how to direct multiple digital assistants and developer tools responsibly to produce a **working, usable, testable, safely published product**. WordWild is our worked example, **not** the subject every participant must build. A calculator, branching lesson, interactive binary display, practice quiz, portfolio site or public-data visualization is equally appropriate.

**One-sentence mission:** Pick one real problem; make a small interactive solution; ask assistants to help but demand evidence; make it accessible; test it the way people use it; publish only what you own and are authorized to share.

**Schedule:** Proposed as **six stages, eighteen checkpoints**. We have **not** assigned final hours, prerequisites, credential credit, or instructional effectiveness claims. Work at your own pace, or teach as a multi-session workshop. Each checkpoint has a small **artifact** that makes progress visible.

## Outcomes and safety promise

A participant who completes the eventual course should be able to:
1. Explain what information an assistant can and cannot access, use optional connected accounts responsibly, and remove access when no longer needed.
2. Write and version a product goal, source ledger, prompts and clear handoffs between human and AI collaborators.
3. Build, serve and publish a small HTML/CSS/JavaScript experience that is usable with keyboard, mouse and touch.
4. Compare text-to-speech workflows, produce or embed audio, and control playback without making audio mandatory.
5. Ground feedback and instruction in actual sources, identify unsupported rules, and demonstrate a simple **retrieval-augmented generation** workflow.
6. Distinguish a passing code test from real user experience or a claim of improved learning.
7. Publish an allow-listed, licensed, attributed artifact and record its known limitations and maintainership.

**Before opening any Gmail connector:** The safe course uses **fictional sample emails** and non-sensitive demo documents. Never authorize access to institutional mail, student records, grades, medical information, private contacts or third-party documents without the specific permissions, institutional approvals and legal basis required. Account features and administrator restrictions change. Students may complete the connectivity comparison using screenshots/official docs or a simulated inbox **without connecting any actual mailbox**. Never paste OAuth codes, API keys or passwords into prompts or public commits.

## Stage I. Learn the map: choose your assistants and protect your data (1–6)

### 1. Overview: what this process does
- **Skill:** distinguish problem, audience, interactive prototype, evidence, publication and maintenance. Decide who owns every approval.
- **Try:** describe a tiny learning activity in 100 words: what the learner tries, how they get help, how it ends, and what a working demonstration would prove.
- **Artifact:** `PROJECT_BRIEF.md` with objective, non-goals, learner, one-week vertical slice, safety boundaries and definition of done.
- **Check:** can a second person describe what success looks like without asking for your original chat?

### 2. Get started with ChatGPT and Gmail, safely
- **Skill:** compare ordinary chat to an optional connected Gmail/Google account; understand OAuth scopes, approval prompts, institutional policy and revocation.
- **Try:** first, use **three invented emails** pasted into an approved practice chat to summarize a schedule and draft a reply **without sending anything**. Optionally explore the current ChatGPT Gmail plugin using a permitted personal/test account and inspect permissions before connecting.
- **Artifact:** a one-page **access map**: what data was actually provided, which account was used (no address in the public report), what the assistant can read or change, where approvals happen, and how to disconnect.
- **Check:** no real student data, no unsolicited send, no credential in the prompt. Official setup: https://help.openai.com/en/articles/11487775-connected-apps-in-chatgpt

### 3. Start building your own system with ChatGPT
- **Skill:** move from a clever one-off prompt to a reproducible workspace: versioned instructions, `README`, task tracker, acceptance tests, evidence notes, and a human decision log.
- **Try:** ask an assistant for three possible designs; choose one; have it challenge the design; write a minimum-build plan that another agent could implement without the conversation.
- **Artifact:** `PROMPTS.md` (versioned request), `TASKS.md` (what is next), `DECISIONS.md` (reason for choices) and a repository folder outline.
- **Check:** is every human-vs-agent responsibility unambiguous, and can the current version be rolled back?

### 4. Connect Claude to Gmail, or use the same mock inbox
- **Skill:** compare Claude's Google Workspace connector permissions and authorization with the ChatGPT route.
- **Try:** ask Claude to summarize the exact same three **fictional** sample emails; if you deliberately use an approved connector, inspect the authorized scopes and default approval for sends, but **do not send**.
- **Artifact:** side-by-side comparison of access, explanation quality, privacy controls, error handling, and cost/availability. Record **not tested** when a connector cannot be used.
- **Check:** connected is not the same as allowed. Follow administrator rules for organization accounts. Official guide: https://support.claude.com/en/articles/10166901-use-google-workspace-connectors

### 5. Connect Gemini to Gmail, or use the same mock inbox
- **Skill:** understand Google's Workspace-connected Gemini flow, account choices, required settings, and potential permissions for work/school accounts.
- **Try:** repeat the sample-inbox comparison. In an authorized account you may test a **read-only** question, verifying the cited source; no actual sending.
- **Artifact:** add Gemini results to the **same** comparison table; note prerequisites and whether the response can be traced to evidence.
- **Check:** a convincing answer does not mean the right message was retrieved. Official guide: https://support.google.com/gemini/answer/15229592

### 6. A fourth assistant or tool: compare, don't collect accounts
- **Skill:** evaluate an alternative such as a local model, NotebookLM, a coding agent, or a tool your instructor approves. Do **not** assume it integrates with Gmail.
- **Try:** run the **same fictional-input task** in two assistants and an alternative, then score transparency, permissions, accuracy and usefulness. An offline simulation is acceptable.
- **Artifact:** `ASSISTANT_COMPARISON.md` with source input, results, tool versions/date, failures, and a reasoned recommendation.
- **Check:** the winning answer is evaluated against the source messages, not preference or brand loyalty.

## Stage II. Give the system a face and a home (7–8)

### 7. Build your first website
- **Skill:** semantic HTML, CSS, responsive layouts, accessible buttons, labels, form submission and JavaScript behavior.
- **Try:** make a static page showing a short clue, an editable answer box and a **Check it** button. The button must work by mouse click, touch and Enter.
- **Artifact:** `index.html`, `style.css`, `app.js` and `README.md`; no framework required.
- **Check:** real browser, 375px mobile layout, keyboard focus, error handling, and no answer visible before the chosen reveal state.

### 8. Host the website with GitHub Pages
- **Skill:** repository, commit, branch, README, `.gitignore`, license, Pages publishing source, public URL and rollback.
- **Try:** publish an **allow-listed** static demo in a public repository, with **no secrets, real email, student data or other people's unpublished materials**. Verify in a private browser window.
- **Artifact:** a deployment receipt with the actual URL, commit hash, license, known limitations and date.
- **Check:** another person can open it without a GitHub login; the latest code is actually deployed. Guide: https://docs.github.com/en/pages/quickstart

## Stage III. Give the experience a voice (9–11)

### 9. What is text-to-speech?
- **Skill:** explain TTS input text, voice model, synthesis, audio formats, latency, pronunciation, consent, accessibility and cost.
- **Try:** narrate a **fictional, instructor-approved** sentence; compare reading silently and hearing it. Decide whether audio should be recorded ahead of time or generated when requested.
- **Artifact:** `AUDIO_PLAN.md` describing human-visible transcript, Play/Stop/Mute and pronunciation QA.
- **Check:** the page remains usable by someone who cannot hear or chooses not to play audio; label AI-generated narration honestly.

### 10. TTS options: local Kokoro versus hosted OpenAI speech
- **Skill:** compare a local/offline option (Kokoro + ONNX) with hosted API TTS on audio quality, direct costs, hardware, operational permissions, data exposure and reliability.
- **Try:** create a comparison grid; optionally render a **public/sample sentence** using an approved local model or a configured provider. **No API key should enter a website, repository, screenshot or chat.**
- **Artifact:** `TTS_DECISION.md` with model/license/source, dated documentation, estimated runtime workflow, sample-listening notes and fallback plan.
- **IMPORTANT dated update (2026-11-16):** The OpenAI `gpt-4o-mini-tts` Speech API model is **deprecated and scheduled for shutdown January 6, 2027**; current documentation points new work toward a Realtime model/API migration. Teach **model selection and migration**, not a fixed call that will expire. References: https://developers.openai.com/api/docs/guides/text-to-speech and https://github.com/thewh1teagle/kokoro-onnx
- **Check:** have you verified current provider docs on the day of implementation?

### 11. Embed the sounds in the website
- **Skill:** relative audio-file paths, user-initiated playback, Stop, Mute, readable text equivalent, caching and offline support.
- **Try:** add one prerecorded clip to the sample page with Play/Stop/Mute, never autoplay. Deliberately test a missing audio file.
- **Artifact:** a working sound panel and an audio-file manifest with attribution.
- **Check:** does sound stop immediately? Does a muted player remain usable? Can you read everything important without hearing it?

## Stage IV. Make the game respond intelligently without lying (12–13)

### 12. Add a script and an interaction
- **Skill:** two kinds of scripts: a **narrator's spoken text** and a **JavaScript program** that responds to user choices. Keep the answer, hint and submitted-attempt states separate.
- **Try:** create a three-step interaction: present a clue, accept a guess, then reveal a supporting explanation on request; add one visible animation after success.
- **Artifact:** tested `app.js` and a short `NARRATION_SCRIPT.md` with voice directions.
- **Check:** pre-answer hidden text and aria labels do not reveal the answer; clicking Check it and pressing Enter have identical outcomes.

### 13. Write useful feedback
- **Skill:** difference between correctness, encouragement, a helpful next hint, an explanation and evidence of learning.
- **Try:** design responses to correct, incorrect, skipped and help-requested attempts. Avoid ridicule and unreviewed phonics rules; show exactly what changed after assistance.
- **Artifact:** `FEEDBACK_RULES.md` with short messages, hint ladder, and a state diagram.
- **Check:** an assisted success must not be reported as a wholly independent success; a “liked the joke” vote is not the same as improved performance.

## Stage V. Connect the system to trustworthy sources (14–16)

### 14. Bring in rules from the real world
- **Skill:** distinguish **verified source facts**, **word-specific observations**, **memory tricks**, **unreviewed general rules**, and **organizational policies**.
- **Try:** pick two genuine educational statements (for example, a spelling observation and a course-policy claim); locate the original authority, summarize it accurately, document its limits, and identify the person who must approve its use.
- **Artifact:** `RULE_LEDGER.md` with exact claim, source URL, date, applicability, review status and known exceptions.
- **Check:** a model saying “that's the rule” is not independent evidence. Do not put real student records into outside AI tools.

### 15. Test teaching materials against research
- **Skill:** separate research findings, plausible learning mechanisms, software correctness and demonstrated learner outcomes.
- **Try:** choose one specific instructional claim; find a suitable primary source or reputable research synthesis; ask a skeptical assistant to challenge whether the study actually supports the proposed activity.
- **Artifact:** `EVIDENCE_REVIEW.md`: claim, citation, context/population, what study found, what it did **not** establish, and a proposed human test.
- **Check:** a passing quiz, high engagement or a synthetic learner's success does **not** prove a child learned more.

### 16. What is Retrieval-Augmented Generation (RAG)?
- **Skill:** the usual expansion is **Retrieval-Augmented Generation**: retrieve relevant materials from a known collection, supply passages with provenance, have a model answer using them, then verify the claims. “Reference” describes part of the idea but is not the standard expansion.
- **Try:** make a tiny local source library of **three approved, non-sensitive documents**. Ask one question answerable from them and one that isn't. Have the assistant cite the exact passage or say it cannot determine the answer.
- **Artifact:** `RAG_DEMO.md` documenting collection contents, retrieval method, citations, no-answer behavior and observed hallucinations. No vector database is required for the first exercise.
- **Check:** can you open the cited text and find the claimed support? Retrieved text is **untrusted data**, never new system instructions. Do not upload confidential classroom or personal files without authorization.

## Stage VI. Prove it works and publish it responsibly (17–18)

### 17. Test what you built
- **Skill:** layered testing: static HTML, unit checks, real browser, mouse, keyboard, touch/mobile, audio, network failures, content accuracy and usability with a human.
- **Try:** write a test that **clicks** Check it, not only one that presses Enter. Deliberately break the button or audio link; verify that the test catches the regression.
- **Artifact:** `TEST_REPORT.md` listing real test commands, what passed, what was not tested, screenshots, bug reproduction and fix.
- **Check:** **WordWild's real lesson:** a reported 69/69 passing suite had missed a broken click because the tests mostly used Enter. Automation proves only the behaviors actually exercised. WordWild itself has not established a learner-outcome effect.

### 18. Deploy, explain and maintain
- **Skill:** publication review, licenses and asset attribution, accessibility, privacy, secrets, versioned release, third-party links, smoke test, rollback and a person responsible for corrections.
- **Try:** rehearse a release checklist with a different reviewer; remove private material; publish only with deliberate human approval; verify the **live** URL from another browser.
- **Artifact:** `RELEASE.md` recording exact commit, date, live link, ownership, known limitations, fix/report process and next revision.
- **Check:** no emails/student data/API keys shipped, rights are documented, accessibility is usable, AI contributions are disclosed where required, and deployment succeeds outside your development machine. Our <a href="../../">Show Your Work</a> guide has the full safety checklist.

## Worked examples and sample materials (the real teaching part)

**Example A: “The mouse button that didn't work.”** A child-facing game allowed Enter to submit answers; clicking **Check it** did nothing. The reason was an HTML button with conflicting `type="button"` and `type="submit"` declarations. The fix was a single native submit type and a *click-based* regression test. Lesson: a test count without user-action coverage is false confidence. See the already published [WordWild worked example](https://jeremy-evert.github.io/oeqa_spell_roller_public/wordwild/) and its [known limits](https://github.com/jeremy-evert/oeqa_spell_roller_public/blob/main/wordwild/KNOWN_LIMITS.md).

**Example B: “The voice that was already there.”** A new game reused word/slow-word narration but forgot the original contextual sentence audio. Rather than purchase a TTS service or redo all writing, the team reused original local Kokoro audio, then filled missing joke clips with a repeatable script. Lesson: carry working features forward, audit manifests, and keep voice-only corrections separate from the on-screen educational text.

## Proposed formative assessment for the eventual instructor package

Use answers grounded in project evidence, not brand trivia:

1. Can you give two examples of data you must not put into an unapproved AI mail connection?
2. What is different about a Gmail-connected assistant versus fictional emails pasted as a practice exercise?
3. Which specific test would have caught a button that works with Enter but not by click?
4. What is the difference between a mnemonic, a word-specific spelling observation and a general phonics rule?
5. When should a RAG assistant decline to answer, and how do you verify citations?
6. What makes a public deployment different from a local development page?

A candidate key and facilitation notes belong in [INSTRUCTOR_NOTES.md](INSTRUCTOR_NOTES.md). This syllabus is still **working draft**, not certified training, institutional policy or a completed OER lesson.

## Publication, revision and attribution notes

- **Demo/source:** [WordWild public example](https://jeremy-evert.github.io/oeqa_spell_roller_public/wordwild/); review [assets and rights](https://github.com/jeremy-evert/oeqa_spell_roller_public/blob/main/wordwild/ASSETS.md) and [privacy](https://github.com/jeremy-evert/oeqa_spell_roller_public/blob/main/wordwild/PRIVACY.md).
- **Public safety checklist:** [Show Your Work](https://jeremy-evert.github.io/swosu-computing/show-your-work/).
- **Rights:** This new draft consists of original educator-directed instructional prose; determine a text-specific open license and reviewer approval **before uploading to a third-party OER publisher**. The public website's Git repository is not proof that every embedded component is licensed under that same license. Code and audio retain their own source licenses.
- **AI disclosure:** This draft was prepared with ChatGPT assistance under a human-directed brief. It has not been independently checked by an instructional specialist; provider connections, costs and interface labels may change.
- **Privacy:** No child identities, real inboxes, student records or confidential machine paths are included. This course asks for simulated data first.
- **Status:** All 18 modules are **drafted as a roadmap and exercise outline**, not authored as full instructor-ready lessons or tested with students.
- **Maintenance:** Recheck provider docs before instruction, especially TTS model deprecations and Gmail connector permissions.

