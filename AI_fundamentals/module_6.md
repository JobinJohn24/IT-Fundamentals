# Low-Code AI Automation
---

### Low-Code AI Automation

- connecting applications together using visual flow builders
- define triggers and actions
- when a node is added, flows transform a simple task handoff into intelligent processing.
- e.g. `make.com` & `zapier`

### Nodes in automation flow

- Data from the trigger becomes the prompt.
- AI responses becomes the output
- Trigger -> AI processing -> action *foundation of 80% of practical business AI Automation*

### GPT Action & custom GPT's

- Custom GPTs are used to call external APIs directly
- e.g. a custom GPT that checks your google calender, query your company's database, or post to notion *NLP*

*Natural Language Processing:* language understanding layer.
- The NLP allows the GPT to understand the user's request, convert it to a API call, then use the tool to read or write data into systems (e.g. google calendar, company database or notion)

### Use Case

- Shopify - store owners uses `Make.com` to generate a `thank you + tips for your product` using it's AI module.
- 15-25% higher repeat purchase from the single automated touchpoint.

### Make vs Zapier

- Zapier is used to easier automations.
- make uses visual flowcharts/canvas

### Example automations using `Make.com` & `Zapier`

- Mark automation:

``` New Gmail attachment
→ Extract text
→ Send to OpenAI
→ Router:
   → If score > 8: add to Notion + Slack alert
   → If score 5–8: add to review queue
   → If score < 5: archive only
→ Error route if PDF extraction fails 
```

- Zapier Automation: 

```
New Gmail attachment
→ Extract text
→ Send to OpenAI
→ Add Notion item
→ Filter if score > 8
→ Send Slack message
```

### Repetitive Taks 

- e.g. of a repetitive task in my life that can become a automated flow:

1. Quiz generation
    > upload notes/PDF/md -> AI summarizes key points -> creates quiz questions -> save to google doc or notion
    > tool stack: google drive | notion | chatGPT | zapier or make

2. email summarizer & organizer
    > new email arrives -> AI checks based on the labeled categories -> labels it -> summarizes action needed
    > labels include: `internships`, `school`, `urgent`, `networking`, `receipts`, `ignore`

3. workout | running automation:
    > sunday -> AI asks/checks workouts completed -> summarizes progress -> suggests next weeks plan.
    > e.g. `you worked out 3 times this week`, `running volume: 6 miles`, `next week: increase to 7 miles, add one lower-body strength day.`

### Building working automation flow using AI processing step

## Dev Notes for automation flow via `Make.com`
