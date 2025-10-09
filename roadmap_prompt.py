
learning_roadmap_prompt = """
You are an expert mentor. Create a **well-structured, interactive, beginner-friendly learning roadmap** for the topic: {topic}.

🕒 Duration: {num_days} days  
📆 Organize into weekly sections like "Week 1: Foundations (Days 1–7)" with weekly themes.

✅ For each day:
- Use **clickable HTML checkboxes** for progress tracking:  
  <input type="checkbox"> **Day X:** 🎯 Task Title – Short, engaging task description *(Approx. X mins/hr)*  
    📚 **Resources (open-access, reliable):**  
    [LINK1](https://example.com) | [LINK2](https://example.com)

💡 Include:
- Small **hands-on tasks** every day
- **Short quizzes or coding challenges** every 3–4 days
- **Reflection/review activity** every 7th day

🚀 Notes:
- **All resources must be reliable and freely accessible**, such as official docs, YouTube educational channels, and open-access blogs/tutorials.
- Use emojis for engagement (🎯, 📚, ✨, 🔧, 🧠, ✅, 💡, etc.)
- Checkboxes are for **personal progress tracking only** – no database is needed.

🎯 Output Format Example:

### Week 1: Foundations (Days 1–7)

<input type="checkbox"> **Day 1:** 🎯 Introduction to {topic} – What it is, why it matters, and real-world use cases *(Approx. 1 hr)*  
  📚 **Resources:** [freeCodeCamp Intro Video](https://www.youtube.com/watch?v=example) | [Official Documentation](https://example.com)

<input type="checkbox"> **Day 2:** 🔧 Setting Up – Tools, environments, and installations *(Approx. 45 mins)*  
  📚 **Resources:** [Official Setup Guide](https://example.com)

<input type="checkbox"> **Day 3:** 🧠 Basic Concepts – Core ideas explained with examples *(Approx. 1 hr)*  
  📚 **Resources:** [Tutorial Video](https://www.youtube.com/watch?v=example) | [Open-access Blog](https://example.com)

<input type="checkbox"> **Day 7:** 💡 Reflection & Review – Recap key concepts and try a mini challenge *(Approx. 1 hr)*  
  📚 **Resources:** [Quiz or Exercise](https://example.com)

...continue for all {num_days} days.
"""
