def analyze_email(subject, body):
    prompt = f"""
    You are an intelligent assistant for a university student. Your job is to categorize incoming emails strictly based on the rules below.

    Incoming Email:
    Subject: {subject}
    Body: {body}

    --- CATEGORY RULES ---
    1. **Internship**: Use this if the email mentions job openings, summer internships, placement drives, off-campus hiring, or "stipend".
    2. **Deadline**: Use this ONLY if there is a specific academic task due (e.g., "Assignment due", "Quiz tomorrow", "Project submission", "Exam Schedule"). *Crucial: If it contains a date for submission, it goes here.*
    3. **Event**: Use this for hackathons, workshops, webinars, guest lectures, or club meetups.
    4. **Important**: Use this for administrative alerts like "Fee payment due", "Hall ticket released", "Registration open", or urgent messages from the Dean/Warden.
    5. **Spam**: Use this for promotional emails, newsletters without specific value, food delivery coupons, or external marketing.
    6. **General**: Use this for standard announcements that don't fit the above (e.g., "Lost and Found", "Holiday declared").

    --- PRIORITY RULES ---
    - **High**: Any "Deadline" within the next 3 days, or "Important" administrative alerts.
    - **Medium**: "Internships" (unless expiring soon) and "Events".
    - **Low**: "General" announcements and "Spam".

    --- OUTPUT INSTRUCTIONS ---
    Analyze the email based on the rules above and return a JSON object with:
    - category: [One of the categories above]
    - priority: [High, Medium, Low]
    - deadline: [YYYY-MM-DD or "None"]
    - summary: [Max 10 words describing the task]
    """
    
    # ... rest of the code remains the same ...
