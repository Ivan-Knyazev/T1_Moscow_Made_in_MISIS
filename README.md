# Free Line
## Решение задачи "Окно знаний: цифровой ассистент базы знаний" от компании T1 на хакатоне "Импульс Т1" от команды *СДЕЛАНО В МИСИС*

## Описание

**Large Images** — это проект, предназначенный для разработки пользователями окна взаимодействия с цифровым ассистентом, интегрируя собственные базы знаний.

## Функциональность

- **Интуитивный интерфейс**: простой и понятный сайт, работать с которым может и человек без особоых навыков
- **Поддержка разных типов**: возможность загрузить базу знаний формата docx, txt, pdf, импорт из Notion
- **Возможность кастомизации**: установка собственных шрифтов и цветов

## Установка

1. **Клонируйте репозиторий**:

   ```bash
   git clone -b dev https://github.com/JateSatis/large_images.git
   cd large_images
2. **Запустите docker контейнер**:
   ```bash
   docker compose up -d --build
Теперь наше решение доступно по *http://localhost:8080*

## Технологии и стек
- **Frontend**: TS, React, scss, vite
- **Backend**: python, FastAPI, Postgresql, s3, MinIO
- **ML**: pytorch, transformers, huggingface, langchain, ragfusion
- **Others**: docker, nginx, docker-compose, RabbitMQ

## Команда
- **Беспалов Вениамин**: Backend, Devops. Студент 2 курса Университета МИСИС
- **Князев Иван**: Backend. Студент 2 курса Университета МИСИС
- **Чашин Михаил**: ML. Студент 2 курса Университета МИСИС
- **Лисовская Анастасия**: Frontend. Студент 2 курса Университета МИСИС
- **Иванова Ксения**: Дизайнер. Студент 2 курса Университета МИСИС

## Архитектура
<img width="1069" alt="image" src="https://github.com/user-attachments/assets/22bc0810-d2b7-4ee6-8cd2-8bb3d53fee78" />


## Презентация решения
https://drive.google.com/file/d/15JBYkkhGy-LZjQ2P1IhaX5jXpC8twf81/view?usp=drive_link
