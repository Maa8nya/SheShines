# ideas_data.py

# A dictionary mapping fields to a list of startup ideas
startup_ideas = {
    "Coding": [
        "An online platform for kids to learn coding through games.",
        "A tool that automates code reviews using AI.",
        "A marketplace for freelance developers specialized in niche tech."
    ],
    "Fashion Designing": [
        "A virtual try-on app for custom clothes.",
        "An eco-friendly fashion brand using recycled materials.",
        "A subscription box service with personalized styling."
    ],
    "Organic Farming": [
        "A farm-to-table delivery service for organic produce.",
        "A smart irrigation system for small farms.",
        "A community platform connecting organic farmers with buyers."
    ]
}

def get_ideas_for_field(field):
    # Return the list of ideas for the given field or a default message
    return startup_ideas.get(field, ["No ideas available for this field yet."])
