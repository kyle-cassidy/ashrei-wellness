from fasthtml.common import *
from inspect import getsource
from home_components import accordion, col, inset, bnset

# TODO: Replace with relevant Ashrei Wellness content
eg_url = "https://github.com/AnswerDotAI/fasthtml-example/tree/main"
samples = [
    ("Game of life", "game-of-life.svg", f"{eg_url}/00_game_of_life"),
    ("To-do", "todo.svg", f"{eg_url}/01_todo_app"),
    ("Chat bot", "chat-bot.svg", f"{eg_url}/02_chatbot"),
    ("Pictionary AI", "pictionary-ai.svg", f"{eg_url}/03_pictionary"),
]


# Placeholder for weather app content
async def weather_table():
    return P("Lorem ipsum dolor sit amet, consectetur adipiscing elit.")


bgurl = "https://ucarecdn.com/35a0e8a7-fcc5-48af-8a3f-70bb96ff5c48/-/preview/750x1000/"
cardcss = (
    "font-family: 'Arial Black', 'Arial Bold', Gadget, sans-serif; perspective: 1500px;"
)


def card_3d_demo():
    def card_3d(text, background, amt, left_align):
        scr = ScriptX("card3d.js", amt=amt)
        align = "left" if left_align else "right"
        sty = StyleX("card3d.css", background=f"url({background})", align=align)
        return Div(text, Div(), sty, scr)

    card = card_3d("Mouseover me", bgurl, amt=1.5, left_align=True)
    return Div(card, style=cardcss)


a_cls = ("s-body text-black/80 col-span-full",)
c_cls = (f"{col} justify-between bg-purple/10 rounded-[1.25rem] {inset}",)
acc_cls = f"{col} gap-4 transition ease-out delay-[300ms]"
qas = [
    (
        "What is Ashrei Wellness?",
        "Ashrei Wellness, LLC is a community of spiritual and interfaith doctors and licensed mental health professionals.",
    ),
    (
        "What services do you offer?",
        "We offer counseling, psychiatry, education, career guidance, ADHD therapy, family consultation, and other wellness services.",
    ),
    (
        "Where are you located?",
        "We have locations in New Jersey, Maryland, and offer Zoom-based accessibility from anywhere in the world.",
    ),
]


def accordion_demo():
    accs = [
        accordion(
            id=id,
            question=q,
            answer=a,
            question_cls="text-black s-body",
            answer_cls=a_cls,
            container_cls=c_cls,
        )
        for id, (q, a) in enumerate(qas)
    ]
    return Div(*accs, cls=acc_cls)


list_class = "m-body text-black list-disc pl-5"
db = database("data/todos.db")


class Todo:
    id: int
    title: str
    done: bool

    def __ft__(self):
        return Li("✅ " if self.done else "", self.title)


todos = db.create(Todo)


def todos_table():
    return Ul(*todos(), cls=list_class)


def startup():
    if not todos():
        todos.insert(title="Create sample todos", done=True)
        todos.insert(title="Create a sample FastHTML app", done=True)
        todos.insert(title="Read this todo list")


async def components():
    return [
        ("Components", "card3d.py", getsource(card_3d_demo), card_3d_demo()),
        ("Dynamic", "weather.py", getsource(weather_table), await weather_table()),
        ("Reusable", "accordion.py", getsource(accordion_demo), accordion_demo()),
        (
            "Databases",
            "todos.py",
            f"{getsource(Todo)}\ntodos = db.create(Todo)\n{getsource(todos_table)}",
            Div(
                H2("DB-generated todo list", cls="text-2xl font-bold mb-4"),
                todos_table(),
            ),
        ),
    ]


stacked = [
    (
        "Build on solid foundations",
        "Ashrei Wellness stands on the shoulders of giants:",
        [
            (
                "Holistic Approaches",
                "holistic.svg",
                "https://ashreiwellness.com/foundation#sec2",
            ),
            (
                "Interfaith Practices",
                "interfaith.svg",
                "https://ashreiwellness.com/foundation#sec3",
            ),
            (
                "Community Support",
                "community.svg",
                "https://ashreiwellness.com/foundation#sec4",
            ),
        ],
    ),
    (
        "Use tools you already know",
        "Ashrei Wellness embraces the familiar:",
        [
            ("Counseling", "counseling.svg", "https://ashreiwellness.com/tech#sec1"),
            ("Psychiatry", "psychiatry.svg", "https://ashreiwellness.com/tech#sec2"),
            ("Education", "education.svg", "https://ashreiwellness.com/tech#sec3"),
            (
                "Career Guidance",
                "career-guidance.svg",
                "https://ashreiwellness.com/tech#sec4",
            ),
        ],
    ),
    (
        "Accessible Anywhere",
        "Ashrei Wellness services are accessible from anywhere:",
        [
            ("Zoom", "zoom.svg", "https://zoom.us/"),
            ("Telehealth", "telehealth.svg", "https://telehealth.com/"),
            ("In-Person", "in-person.svg", "https://ashreiwellness.com/locations"),
        ],
    ),
]

benefits = [
    (
        "Get started fast",
        "Our initial assessment is free and helps us understand your needs.",
    ),
    (
        "Flexibility",
        "We offer a range of services tailored to your specific requirements.",
    ),
    (
        "Experience",
        "Our team has over 30 years of experience in mental health and wellness.",
    ),
]

faqs = [
    (
        "What kinds of services do you offer?",
        "We offer counseling, psychiatry, education, career guidance, ADHD therapy, family consultation, and other wellness services.",
    ),
    (
        "Where are you located?",
        "We have locations in New Jersey, Maryland, and offer Zoom-based accessibility from anywhere in the world.",
    ),
    (
        "What is your mission?",
        "Ashrei Wellness, LLC is a community of spiritual and interfaith doctors and licensed mental health professionals dedicated to helping you navigate your journey.",
    ),
    (
        "Do you offer telehealth services?",
        "Yes, most of our services are delivered through telehealth and telepsychiatry media such as Zoom.",
    ),
    (
        "What is your inclusion policy?",
        "We work with everybody who seeks our guidance. We do not discriminate against anyone based on similarities, differences, or ethnic/cultural heritages.",
    ),
    (
        "How can I get started?",
        "Contact us through our website to schedule an initial assessment. We look forward to helping you on your journey.",
    ),
]

gr_test = Div(
    Ul(
        Li("professional"),
        Li("experienced"),
        Li("compassionate"),
        Li("dedicated"),
        style="list-style-type: square;",
        cls="m-body text-black",
    ),
    P(
        A(
            "(From a satisfied client)",
            href="#",
            cls="border-b-2 border-b-black/30 hover:border-b-black/80",
        )
    ),
)
testimonials = [
    (
        "Ashrei Wellness has been a beacon of hope for me. Their professional and compassionate approach is unparalleled.",
        "Daniel Roy",
        "Client",
        "assets/testimonials/daniel-roy.png",
    ),
    (
        "The team at Ashrei Wellness helped me navigate my career and personal challenges with great expertise.",
        "Giles Thomas",
        "Client",
        "assets/testimonials/giles-thomas.png",
    ),
    (
        "Their telehealth services are convenient and effective. I highly recommend Ashrei Wellness.",
        "Jake Cooper",
        "Client",
        "assets/testimonials/jake-cooper.png",
    ),
]
