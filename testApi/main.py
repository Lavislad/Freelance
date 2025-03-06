import json

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

moc_data = [
    {
        "id": 1,
        "title": "Веб-разработчик",
        "description": "Требуется опытный веб-разработчик для создания и поддержки веб-сайтов.",
        "skills": ["HTML", "CSS", "JavaScript", "React"],
        "budget": "2000-3000 USD",
        "duration": "3 месяца",
        "location": "Удаленная работа",
    },
    {
        "id": 2,
        "title": "Дизайнер UI/UX",
        "description": "Ищем талантливого дизайнера для разработки пользовательских интерфейсов.",
        "skills": ["Figma", "Adobe XD", "Photoshop"],
        "budget": "1500-2500 USD",
        "duration": "2 месяца",
        "location": "Удаленная работа",
    },
    {
        "id": 3,
        "title": "Копирайтер",
        "description": "Нужен копирайтер для написания контента для блога и социальных сетей.",
        "skills": ["Русский язык", "SEO", "Контент-маркетинг"],
        "budget": "1000-2000 USD",
        "duration": "1 месяц",
        "location": "Удаленная работа",
    },
    {
        "id": 4,
        "title": "Мобильный разработчик",
        "description": "Требуется разработчик мобильных приложений на платформе Android.",
        "skills": ["Java", "Kotlin", "Android SDK"],
        "budget": "2500-3500 USD",
        "duration": "4 месяца",
        "location": "Удаленная работа",
    },
    {
        "id": 5,
        "title": "Менеджер проектов",
        "description": "Ищем менеджера проектов для управления командой фрилансеров.",
        "skills": ["Agile", "Scrum", "JIRA"],
        "budget": "3000-4000 USD",
        "duration": "6 месяцев",
        "location": "Удаленная работа",
    },
]


@app.get("/moc")
async def get_moc():
    return moc_data


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8001, reload=True)
