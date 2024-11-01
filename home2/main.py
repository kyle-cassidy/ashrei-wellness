from fasthtml.common import *

app, rt = fast_app()


def menu_bar():
    return Nav(
        Ul(
            Li(A("Home", href="#hero", cls="nav-link smooth-scroll")),
            Li(A("Services", href="#services", cls="nav-link smooth-scroll")),
            Li(A("Our Approach", href="#approach", cls="nav-link smooth-scroll")),
            Li(A("Resources", href="#resources", cls="nav-link smooth-scroll")),
            Li(A("Contact", href="#contact", cls="nav-link smooth-scroll")),
            cls="nav-list",
        ),
        cls="menu-bar",
    )


def hero_section():
    return Section(
        Div(
            H1("Ashrei Wellness, LLC", cls="hero-title"),
            P("“We help you navigate your journey.”", cls="hero-tagline"),
            cls="hero-content",
        ),
        cls="hero-section",
        id="hero",
    )


def services_section():
    services_list = Ul(
        Li(B("Counseling")),
        Li(B("Psychiatry")),
        Li(B("Educational & Career Guidance")),
        Li(B("ADHD Assessment & Therapy")),
        Li(B("Family Consultation")),
        Li(B("Wellness Services")),
        cls="services-list",
    )
    return Section(
        H2("Services", cls="section-title"),
        services_list,
        P(
            "We assist in balancing and regulating issues with anxiety, depression, addiction, trauma, ADHD, PTSD, and other challenges. Our psychiatric medication prescribers are among the best in South Jersey, available in-office or via telepsychiatry.",
            cls="section-text",
        ),
        cls="services-section",
        id="services",
    )


def approach_section():
    approaches = Ul(
        Li(B("Internal Family Systems (IFS)")),
        Li(B("Eye Movement Desensitization and Reprocessing (EMDR)")),
        Li(B("Dialectical Behavior Therapy (DBT)")),
        Li(B("Medication-Assisted Treatment (MAT)")),
        Li(B("Positive Psychology")),
        Li(B("Jungian Psychology")),
        Li(B("Cognitive Behavioral Therapy (CBT)")),
        Li(B("Storytelling")),
        Li(B("Therapeutic Dream Interpretation")),
        Li(B("Other Healing Practices")),
        cls="approach-list",
    )
    return Section(
        H2("Our Approach", cls="section-title"),
        P(
            "We rely on Evidence-Based Practice modalities and theoretical orientations, including:",
            cls="section-text",
        ),
        approaches,
        cls="approach-section",
        id="approach",
    )


def testimonials_section():
    testimonials = [
        (
            "A.A.",
            "Dr. Cassidy helped me develop my career as a Spanish and Russian interpreter. He assisted in shaping my resume, applying for positions, and conducting practice interviews for my current job.",
        ),
        ("Logan H.", "Thank you for everything you have helped me achieve."),
        (
            "Jana M.",
            "Dr. Don is really nice and kind. He helps me figure things out. We talk every week about my activities and goals and how to get along with staff at my group home.",
        ),
        (
            "Nancy M.",
            "Don Cassidy has served as our Family Consultant at various times over the past 20 years to help us make decisions about two of my adult children and one grandchild. Words cannot adequately describe how grateful I feel for his help.",
        ),
        (
            "E.K. and A.K.",
            "Dr. Cassidy is our family consultant, helping us by serving as a Life Coach for a family member. He assisted our family member in setting and meeting goals regarding relocation to New Jersey and finding a job while pursuing a healthy lifestyle.",
        ),
        (
            "Dave F.",
            "Dr. Cassidy provided an expert evaluation and treatment plan for me. He helped me heal my injury and get back to work. My family and I are grateful.",
        ),
    ]
    testimonial_items = [
        Div(
            Blockquote(P(f"“{text}”", cls="testimonial-text")),
            Cite(f"– {author}", cls="testimonial-author"),
            cls="testimonial-item",
        )
        for author, text in testimonials
    ]
    return Section(
        H2("Testimonials", cls="section-title"),
        Div(*testimonial_items, cls="testimonials-list"),
        cls="testimonials-section",
        id="testimonials",
    )


def resources_section():
    return Section(
        H2("Resources", cls="section-title"),
        H3("Career Assessment Tools", cls="resource-subtitle"),
        Ul(
            Li("Myers-Briggs Type Indicator (MBTI)"),
            Li("Enneagram"),
            Li("CliftonStrengths"),
            Li("VIA Signature Strengths Inventory"),
            cls="resource-list",
        ),
        H3("Recommended Reading", cls="resource-subtitle"),
        Ul(
            Li(Em("Scattered Minds")),
            Li(Em("The Gift of Adult ADD")),
            Li(Em("Relaxation and Stress Management Workbook")),
            Li(Em("What Color is Your Parachute?")),
            cls="resource-list",
        ),
        H3("Videos", cls="resource-subtitle"),
        Ul(
            Li(
                A(
                    "TED Talk: Start with Why",
                    href="https://www.ted.com/talks/simon_sinek_how_great_leaders_inspire_action",
                    target="_blank",
                )
            ),
            cls="resource-list",
        ),
        cls="resources-section",
        id="resources",
    )


def contact_section():
    return Section(
        H2("Contact Us", cls="section-title"),
        P(
            "Email: ",
            A(
                "Cassidyphd@gmail.com",
                href="mailto:Cassidyphd@gmail.com",
                cls="contact-link",
            ),
        ),
        P(
            "Text Message: ",
            A("301-466-4504", href="tel:3014664504", cls="contact-link"),
        ),
        cls="contact-section",
        id="contact",
    )


def footer():
    return Footer(
        P("© 2023 Ashrei Wellness, LLC"),
        A("Back to Top", href="#hero", cls="back-to-top smooth-scroll"),
        cls="footer",
    )


@rt("/")
def index():
    return Html(
        Head(
            Title("Ashrei Wellness, LLC"),
            Meta(name="viewport", content="width=device-width, initial-scale=1"),
            Link(rel="stylesheet", href="/assets/styles.css"),
            Script(src="https://cdn.jsdelivr.net/npm/htmx.org@1.9.2"),
            Script(
                """
                document.addEventListener('DOMContentLoaded', function() {
                    var scrollLinks = document.querySelectorAll('.smooth-scroll');
                    for (var i = 0; i < scrollLinks.length; i++) {
                        scrollLinks[i].addEventListener('click', function(e) {
                            e.preventDefault();
                            document.querySelector(this.getAttribute('href')).scrollIntoView({ behavior: 'smooth' });
                        });
                    }
                });
            """,
                type="text/javascript",
            ),
        ),
        Body(
            menu_bar(),
            hero_section(),
            services_section(),
            approach_section(),
            testimonials_section(),
            resources_section(),
            contact_section(),
            footer(),
            cls="main-body",
        ),
    )


serve()
