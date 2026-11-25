from django.db.models import Case, IntegerField, Value, When


SERVICE_CATEGORY_CHOICES = [
    ("Разработка", "Разработка"),
    ("Telegram и Mini Apps", "Telegram и Mini Apps"),
    ("AI и Автоматизация", "AI и Автоматизация"),
    ("Дизайн", "Дизайн"),
    ("Маркетинг", "Маркетинг"),
    ("Контент", "Контент"),
    ("Видео и Motion", "Видео и Motion"),
    ("SEO и Тексты", "SEO и Тексты"),
    ("Аналитика и Data", "Аналитика и Data"),
    ("Операции и Product Support", "Операции и Product Support"),
]


SKILL_CATALOG = [
    "HTML/CSS",
    "JavaScript",
    "TypeScript",
    "React",
    "Next.js",
    "Vue.js",
    "Node.js",
    "Python",
    "Django",
    "FastAPI",
    "PostgreSQL",
    "REST API",
    "React Native",
    "Flutter",
    "WordPress",
    "Shopify",
    "Telegram Bot API",
    "Telegram Mini Apps",
    "n8n",
    "Make",
    "Zapier",
    "Airtable",
    "Notion",
    "CRM Integrations",
    "Payment Integrations",
    "OpenAI API",
    "Figma",
    "UI Design",
    "UX Audit",
    "UX Research",
    "Design Systems",
    "Mobile App Design",
    "Web Design",
    "Brand Design",
    "Graphic Design",
    "Presentation Design",
    "Meta Ads",
    "Google Ads",
    "TikTok Ads",
    "Growth Strategy",
    "Marketing Analytics",
    "CRO",
    "Copywriting",
    "Sales Copy",
    "Content Writing",
    "SMM",
    "Content Strategy",
    "YouTube Packaging",
    "Video Editing",
    "Motion Design",
    "Short-form Content",
    "SEO",
    "Technical SEO",
    "Product Analytics",
    "Data Analysis",
    "Dashboarding",
    "Project Management",
    "Customer Support",
    "CRM Setup",
]


def skill_catalog_ordering():
    return Case(
        *[
            When(name=name, then=Value(index))
            for index, name in enumerate(SKILL_CATALOG)
        ],
        default=Value(len(SKILL_CATALOG)),
        output_field=IntegerField(),
    )
