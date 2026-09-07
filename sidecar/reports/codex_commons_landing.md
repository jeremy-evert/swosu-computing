# Computing Commons landing page evidence

## Built

- Added `commons/index.html` and `commons/week-data.json` using the accepted vendored `assets/week-slider/` component.
- Added 16 ordered weeks with `week1_start_date: "2026-08-17"`.
- Updated the four course landing pages' Computing Commons href from `../commons.swosu-computing/` to `../commons/`.

## Title-source citations

Each displayed title is the first heading on line 1 of the cited Monday Moment activity, with the `Student Activity — AI I Week N:` prefix removed where present:

1. `ai_i/monday_moments/week_01_define_the_problem/student_activity.md:1` — Define the Problem
2. `ai_i/monday_moments/week_02_gather_context/student_activity.md:1` — Gather Context
3. `ai_i/monday_moments/week_03_plan_the_work/student_activity.md:1` — Plan the Work
4. `ai_i/monday_moments/week_04_decompose_the_task/student_activity.md:1` — Decompose the Task
5. `ai_i/monday_moments/week_05_select_the_right_model/student_activity.md:1` — Select the Right Model (heading omits the week number)
6. `ai_i/monday_moments/week_06_engineer_the_prompt/student_activity.md:1` — Engineer the Prompt
7. `ai_i/monday_moments/week_07_research_and_retrieve/student_activity.md:1` — Research and Retrieve
8. `ai_i/monday_moments/week_08_reason/student_activity.md:1` — Reason
9. `ai_i/monday_moments/week_09_generate/student_activity.md:1` — Generate
10. `ai_i/monday_moments/week_10_critique/student_activity.md:1` — Critique
11. `ai_i/monday_moments/week_11_verify/student_activity.md:1` — Verify
12. `ai_i/monday_moments/week_12_revise/student_activity.md:1` — Revise
13. `ai_i/monday_moments/week_13_decide/student_activity.md:1` — Decide
14. `ai_i/monday_moments/week_14_automate/student_activity.md:1` — Automate
15. `ai_i/monday_moments/week_15_measure/student_activity.md:1` — Measure
16. `ai_i/monday_moments/week_16_reflect_and_improve/student_activity.md:1` — Reflect and Improve

## Known placeholder

All 16 URLs intentionally repeat `https://swosu.instructure.com/courses/24298`, the Computing Commons course front page. Replace these with real per-week module links in a future real-link pass. No Canvas contact was made.

## Checks

- Fresh `git fetch origin` completed in both `swosu-computing` and `ai_fluency`.
- Verified all 16 Monday Moment files and heading shapes on `ai_fluency` `origin/main` (`022262c`).
- Verified Computing Commons 24298 in `foreman_interface/jobs/tasks/week04_readiness_campaign.md:24`.
- Validated both Commons JSON representations and all 16 ordered entries with the shared start date.
- Checked all five pages for slider CSS/JS includes, mount calls, and Commons links; checked the four course pages retain their existing slider data.
- `git diff --check` passed; no Canvas contact or browser-level render was performed.

## Branch-state note

The four accepted course landing pages and shared slider were present on `origin/ivy/week16-course-landings` as a direct child of `origin/main`, but not yet on `origin/main` at this run. They were carried into this isolated `origin/main` worktree unchanged except for the authorized Commons href update.
