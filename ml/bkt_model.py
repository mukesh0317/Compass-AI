def estimate_mastery(responses, p_learn=0.15, p_guess=0.20, p_slip=0.10, p_prior=0.20):
    """
    Simplified Bayesian Knowledge Tracing update.
    responses must be a sequence of 1 (correct) or 0 (incorrect).
    Returns the posterior probability of mastery after the final response.
    """
    p_mastery = float(p_prior)
    for response in responses:
        response = int(response)
        if response not in (0, 1):
            continue

        # Update belief using the observation likelihood.
        if response == 1:
            likelihood_mastered = 1 - p_slip
            likelihood_unmastered = p_guess
        else:
            likelihood_mastered = p_slip
            likelihood_unmastered = 1 - p_guess

        denominator = (p_mastery * likelihood_mastered) + ((1 - p_mastery) * likelihood_unmastered)
        if denominator > 0:
            p_mastery = (p_mastery * likelihood_mastered) / denominator

        # Knowledge may be acquired between attempts.
        p_mastery = p_mastery + ((1 - p_mastery) * p_learn)
        p_mastery = min(max(p_mastery, 0.0), 1.0)

    return p_mastery


def recommend_practice(profile_rows):
    recommendations = []
    for row in profile_rows:
        mastery = float(row.get("Estimated mastery (%)", 0))
        attempts = int(row.get("Attempts", 0))
        skill = str(row.get("Skill", "Unknown skill"))

        if attempts == 0:
            level = "Not assessed"
            message = "Complete a short diagnostic assessment to establish a baseline for this skill."
        elif mastery < 40:
            level = "Needs focused support"
            message = "Review the foundational concept, work through a guided example, then answer 3–5 beginner questions."
        elif mastery < 60:
            level = "Developing"
            message = "Practice a small set of targeted questions and review explanations for incorrect answers."
        elif mastery < 80:
            level = "Progressing"
            message = "Try mixed-difficulty practice and explain the solution steps before checking the answer."
        else:
            level = "Strong"
            message = "Maintain mastery with spaced revision and a few challenging application questions."

        if mastery < 80 or attempts == 0:
            recommendations.append({
                "skill": skill,
                "mastery": mastery,
                "attempts": attempts,
                "level": level,
                "recommendation": message
            })

    return sorted(recommendations, key=lambda item: item["mastery"])
