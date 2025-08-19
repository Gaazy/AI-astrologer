# backend.py
# Simple rule-based astrology backend
# Requires: python-dateutil

from datetime import datetime
from dateutil import parser

ZODIAC_RANGES = [
    ("capricorn",  (12,22), ( 1,19)),
    ("aquarius",   ( 1,20), ( 2,18)),
    ("pisces",     ( 2,19), ( 3,20)),
    ("aries",      ( 3,21), ( 4,19)),
    ("taurus",     ( 4,20), ( 5,20)),
    ("gemini",     ( 5,21), ( 6,21)),
    ("cancer",     ( 6,22), ( 7,22)),
    ("leo",        ( 7,23), ( 8,22)),
    ("virgo",      ( 8,23), ( 9,22)),
    ("libra",      ( 9,23), (10,23)),
    ("scorpio",    (10,24), (11,21)),
    ("sagittarius",(11,22), (12,21)),
]

SIGN_INFO = {
    "aries":       {"element":"Fire", "mode":"Cardinal", "short":"Bold, energetic, initiating."},
    "taurus":      {"element":"Earth", "mode":"Fixed", "short":"Practical, steady, sensual."},
    "gemini":      {"element":"Air",  "mode":"Mutable", "short":"Curious, communicative, adaptable."},
    "cancer":      {"element":"Water","mode":"Cardinal", "short":"Caring, intuitive, home-oriented."},
    "leo":         {"element":"Fire", "mode":"Fixed", "short":"Confident, expressive, generous."},
    "virgo":       {"element":"Earth", "mode":"Mutable", "short":"Analytical, service-oriented, detail-focused."},
    "libra":       {"element":"Air",  "mode":"Cardinal", "short":"Diplomatic, partnership-focused, balanced."},
    "scorpio":     {"element":"Water","mode":"Fixed", "short":"Intense, transformative, private."},
    "sagittarius": {"element":"Fire", "mode":"Mutable", "short":"Adventurous, philosophical, freedom-loving."},
    "capricorn":   {"element":"Earth","mode":"Cardinal", "short":"Ambitious, disciplined, practical."},
    "aquarius":    {"element":"Air",  "mode":"Fixed", "short":"Innovative, community-minded, unconventional."},
    "pisces":      {"element":"Water","mode":"Mutable", "short":"Compassionate, imaginative, dreamy."},
}

def _month_day(dt):
    return dt.month, dt.day

def calculate_sun_sign(birth_date):
    """
    birth_date: datetime.date or datetime
    returns: sign name (str)
    """
    m, d = _month_day(birth_date)
    for sign, (start_m, start_d), (end_m, end_d) in ZODIAC_RANGES:
        start = (start_m, start_d)
        end = (end_m, end_d)
        if start_m <= end_m:
            # normal within same year span (e.g., Apr 20 to May 20)
            if (m, d) >= start and (m, d) <= end:
                return sign
        else:
            # spans year boundary (e.g., Dec 22 to Jan 19)
            if (m, d) >= start or (m, d) <= end:
                return sign
    # fallback
    return "capricorn"

def parse_datetime(date_str, time_str=None):
    """
    date_str: e.g. "1998-06-15" or "15 Jun 1998"
    time_str: optional "14:30"
    returns: timezone-naive datetime
    """
    if time_str:
        full = f"{date_str} {time_str}"
    else:
        full = date_str
    dt = parser.parse(full)
    return dt

def generate_report(name, date_str, time_str, place):
    """
    Return a dict with basic astrological outputs and a human-friendly short report.
    """
    try:
        dt = parse_datetime(date_str, time_str)
    except Exception as e:
        return {"error": f"Invalid date/time format: {e}"}

    sign = calculate_sun_sign(dt)
    info = SIGN_INFO.get(sign, {})
    age = None
    try:
        now = datetime.now()
        age = now.year - dt.year - ((now.month, now.day) < (dt.month, dt.day))
    except:
        age = None

    report = {
        "name": name,
        "birth_datetime": dt.isoformat(),
        "place": place,
        "sun_sign": sign,
        "element": info.get("element"),
        "mode": info.get("mode"),
        "age": age,
        "short_profile": info.get("short"),
        "full_text": (
            f"{name}, your Sun sign is {sign.title()} — {info.get('short')} "
            f"({info.get('element')} element, {info.get('mode')} modality)."
        )
    }
    return report

# very small "AI-like" free text responder
def answer_question(question, context):
    """
    question: free-text question from user
    context: dict returned by generate_report
    returns: short text answer
    """
    q = (question or "").lower().strip()
    sign = context.get("sun_sign", "unknown")
    # keyword rules
    if not q:
        return "Please type a question about your career, love life, or personality."

    if any(k in q for k in ["career", "job", "work", "promotion"]):
        templates = [
            "For a {sign} (element: {element}), steady progress and practical planning usually bring the best results. Focus on consistent effort and visible small wins.",
            "{name}, your sign {sign} suggests persistence will win—break big goals into monthly milestones and showcase measurable achievements.",
            "This period favors skill-building. For {sign}, sharpening practical skills and networking steadily helps career growth."
        ]
        return templates[0].format(sign=sign.title(), element=context.get("element"), name=context.get("name"))

    if any(k in q for k in ["love", "relationship", "partner", "marriage"]):
        templates = [
            "{name}, as a {sign}, you value {element}-style expression. Be clear about needs and listen; steady demonstrations of care matter more than grand gestures.",
            "For {sign}, compatible energy often comes from signs that complement your element. Prioritize honest conversations and shared values."
        ]
        return templates[0].format(name=context.get("name"), sign=sign.title(), element=context.get("element"))

    if any(k in q for k in ["health", "fitness", "wellness"]):
        return f"Small, regular routines suit {sign.title()} — aim for balanced sleep, moderate exercise, and mindful breaks."

    # fallback: sign-aware generic inspirational answer
    return (
        f"{context.get('name')}, {sign.title()} energy combines {context.get('element')} traits — "
        f"remember your strengths ( {context.get('short_profile')} ). Try to convert them into one concrete action this week."
    )

# Example usage when running as script
if __name__ == "__main__":
    demo = generate_report("Asha", "1995-08-01", "09:30", "Mumbai, India")
    print(demo["full_text"])
    print(answer_question("Will I get a promotion?", demo))
