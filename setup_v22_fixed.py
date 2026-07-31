#!/usr/bin/env python3
"""
Нейроштаб Katerina Art v2.2 — Setup Script (FIXED)
Запуск: python3 setup_v22_fixed.py

Что делает:
- НЕ перезаписывает существующие файлы с контентом (все overwrite=False)
- Создаёт только то чего нет
- Кладёт product_core.md и content_core.md из файлов (если есть рядом)
- Заглушки TODO для агентов без готового core.md
"""

import os, shutil

def write(path, content):
    """Создаёт файл только если не существует или пустой."""
    os.makedirs(os.path.dirname(path), exist_ok=True) if os.path.dirname(path) else None
    if os.path.exists(path) and os.path.getsize(path) > 0:
        print(f"  · {path} (пропущен — уже есть контент)")
        return False
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"  ✓ {path}")
    return True

def copy_if_exists(src, dst):
    """Копирует файл src → dst только если dst не существует или пустой."""
    if not os.path.exists(src):
        print(f"  ! {src} не найден — пропускаем")
        return
    os.makedirs(os.path.dirname(dst), exist_ok=True) if os.path.dirname(dst) else None
    if os.path.exists(dst) and os.path.getsize(dst) > 0:
        print(f"  · {dst} (пропущен — уже есть контент)")
        return
    shutil.copy2(src, dst)
    print(f"  ✓ {dst} (скопирован из {src})")

def touch(path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if not os.path.exists(path):
        open(path, 'w').close()
        print(f"  + {path}")

def mkdir(path):
    if not os.path.exists(path):
        os.makedirs(path, exist_ok=True)
        print(f"  + {path}/")

# ─────────────────────────────────────────────────────
# ЗАГЛУШКИ ДЛЯ АГЕНТОВ БЕЗ ГОТОВОГО CORE.MD
# ─────────────────────────────────────────────────────

STUBS = {
    "office/agents/growth/core.md":
        "# core.md — Growth v0.0 (TODO)\n# Скилы: marketingskills (cro, email-sequence, landing, seo, pricing)\n# MCP: Composio → GA4, Stripe, Mailchimp\n# Следующий шаг: написать полный core.md\n",

    "office/agents/architect/core.md":
        "# core.md — Architect v0.0 (TODO)\n# Роль: создаёт и удаляет агентов под конкретные задачи\n# Референс: VoltAgent subagents (10 категорий, 154+ агентов)\n# Следующий шаг: написать полный core.md\n",

    "archontum/agents/council/core.md":
        "# core.md — COUNCIL v0.0 (TODO)\n# Скил: llm-council (уже установлен в Claude)\n# Триггеры: 'council this', 'стоит ли мне X или Y'\n# Следующий шаг: написать полный core.md\n",

    "archontum/agents/meta-partner/core.md":
        "# core.md — META-PARTNER v0.0 (TODO)\n# Роль: видение, траектория, стратегическое распределение задач\n# Читает: archontum/vision.md\n# Следующий шаг: написать полный core.md\n",

    "archontum/agents/scout/core.md":
        "# core.md — SCOUT v0.0 (TODO)\n# Роль: разведка рынков, ниш, конкурентов\n# Инструменты: graphify add <url>, web search\n# Следующий шаг: написать полный core.md\n",

    "invisible-council/agents/personal-assistant/core.md":
        "# core.md — PERSONAL-ASSISTANT v0.0 (TODO)\n# Роль: расписание, письма, билеты, переводы\n# MCP: Google Calendar, Gmail, Drive\n# Следующий шаг: написать полный core.md\n",

    "invisible-council/agents/morning-check/core.md":
        "# core.md — MORNING-CHECK v0.0 (TODO)\n# Скил: morning-show-engine (уже установлен в Claude)\n# Роль: утренняя настройка дня — тон, вызов, практика\n# Следующий шаг: написать полный core.md\n",

    "invisible-council/agents/mirror/core.md":
        "# core.md — MIRROR v0.0 (TODO)\n# Роль: рефлексия и поддержка, личный контур\n# Следующий шаг: написать полный core.md\n",

    "office/agents/designer/core.md":
        "# core.md — Designer v0.0 (TODO)\n# ВНИМАНИЕ: старый файл designer от шаблона Русанова удалён\n# Скилы: brand-kit, creative-director, fashion-campaign-director\n# Следующий шаг: написать полный core.md для v2.2\n",
}

PROGRESS_TPL = """ПРОЕКТ: {name}
СТАТУС: в работе
ПОСЛЕДНЕЕ ОБНОВЛЕНИЕ: —

СДЕЛАНО:
- (пусто)

В РАБОТЕ:
- (пусто)

СЛЕДУЮЩЕЕ:
- (из TASKS.md)

БЛОКЕРЫ:
- нет

ИНЦИДЕНТЫ (errors/):
- нет
"""

PROGRESS_INDEX = """# office/progress-index.md
# Director читает в начале каждой сессии.

## Активные проекты
- [Fluxera](../projects/fluxera/progress.md) — в работе

## На паузе

## Завершённые
"""

BRAND_STUB = """# katerina-profile/identity/brand.md
# TODO: заполнить реальными данными из базы знаний Katerina Art

## Позиционирование
AI-предприниматель, архитектор AI-экосистем.

## Домены
- AI creators / creator economy
- AI-агенты и нейросистемы
- Бизнес-автоматизация через AI
- Онлайн-образование нового поколения
- SaaS-продукты

## Активные проекты
- Fluxera — Telegram-экосистема рекламных кругов

## Аудитория
— заполнить —

## Пиллары бренда
— заполнить —
"""

VOICE_STUB = """# katerina-profile/identity/voice.md
# TODO: дополнить при необходимости

## Тон
- Партнёрский, на равных
- Лёгкая ирония допустима
- Без менторских интонаций
- Без избыточного одобрения

## Язык
- Русский по умолчанию
- Технические термины на английском с пояснением

## Запрещено
- Мотивационные речи
- "в эпоху AI", "цифровой мир", "следующий уровень"
- "Отличный вопрос!", "С удовольствием!", "Конечно!"
- Поверхностные ответы
"""

VALUES_YAML = """core_principles:
  - data_over_assumptions
  - facts_over_opinions
  - execution_over_theory
  - depth_over_speed
  - structure_over_unstructured_creativity
"""


def main():
    print("\n🚀 Нейроштаб Katerina Art v2.2 — Setup (FIXED)\n")

    # ── 1. Структура агентов ──
    print("── Папки и layered memory агентов ──")
    agents = [
        "office/agents/director",
        "office/agents/product",
        "office/agents/developer",
        "office/agents/content",
        "office/agents/growth",
        "office/agents/architect",
        "archontum/agents/meta-partner",
        "archontum/agents/council",
        "archontum/agents/scout",
        "invisible-council/agents/personal-assistant",
        "invisible-council/agents/morning-check",
        "invisible-council/agents/mirror",
    ]
    for agent in agents:
        mkdir(agent)
        for f in ["overrides.md", "memory.md", "failures.md"]:
            touch(f"{agent}/{f}")

    # ── 2. Core.md — только для тех у кого пусто ──
    print("\n── Core.md агентов ──")

    # Director и Developer — НЕ перезаписываем (overwrite=False по умолчанию)
    # Если файл уже есть с контентом — пропускаем
    write("office/agents/director/core.md",
          "# core.md — Director\n# Файл уже должен быть в репозитории\n# Если пустой — скопируй вручную из чата\n")
    write("office/agents/developer/core.md",
          "# core.md — Developer\n# Файл уже должен быть в репозитории\n# Если пустой — скопируй вручную из чата\n")

    # Product и Content — копируем из файлов если они рядом, иначе пишем полные
    copy_if_exists("product_core.md", "office/agents/product/core.md")
    copy_if_exists("content_core.md", "office/agents/content/core.md")

    # Если файлы не найдены рядом — пишем TODO заглушку
    if not os.path.exists("office/agents/product/core.md") or \
       os.path.getsize("office/agents/product/core.md") == 0:
        write("office/agents/product/core.md",
              "# core.md — Product v0.0 (TODO)\n# Скачай product_core.md из чата и скопируй сюда\n")

    if not os.path.exists("office/agents/content/core.md") or \
       os.path.getsize("office/agents/content/core.md") == 0:
        write("office/agents/content/core.md",
              "# core.md — Content v0.0 (TODO)\n# Скачай content_core.md из чата и скопируй сюда\n")

    # Остальные агенты — заглушки TODO
    for path, content in STUBS.items():
        write(path, content)

    # ── 3. Katerina-profile ──
    print("\n── Katerina-profile ──")
    for d in [
        "katerina-profile/identity",
        "katerina-profile/content",
        "katerina-profile/knowledge/research",
        "katerina-profile/network",
        "katerina-profile/operations",
    ]:
        mkdir(d)

    write("katerina-profile/identity/brand.md", BRAND_STUB)
    write("katerina-profile/identity/voice.md", VOICE_STUB)
    write("katerina-profile/identity/values.yaml", VALUES_YAML)

    for path in [
        "katerina-profile/content/calendar.md",
        "katerina-profile/content/posts.jsonl",
        "katerina-profile/content/ideas.jsonl",
        "katerina-profile/network/contacts.jsonl",
        "katerina-profile/operations/todos.md",
    ]:
        touch(path)

    # ── 4. Структура проектов ──
    print("\n── Проекты ──")
    for d in ["projects/fluxera/errors", "projects/fluxera/notes", "projects/fluxera/docs"]:
        mkdir(d)
    for path in [
        "projects/fluxera/PRD.md",
        "projects/fluxera/TASKS.md",
        "projects/fluxera/docs/ARCHITECTURE.md",
        "projects/fluxera/docs/DEPLOYMENT.md",
        "projects/fluxera/docs/TESTING.md",
    ]:
        touch(path)
    write("projects/fluxera/progress.md", PROGRESS_TPL.replace("{name}", "Fluxera"))

    # ── 5. Office index ──
    print("\n── Office ──")
    write("office/progress-index.md", PROGRESS_INDEX)

    # ── 6. .gitignore ──
    gitignore_add = "\n# Нейроштаб v2.2\ngraphify-out/\n*.jsonl.bak\n.env.local\n"
    if os.path.exists(".gitignore"):
        with open(".gitignore", "r") as f:
            existing = f.read()
        if "graphify-out" not in existing:
            with open(".gitignore", "a") as f:
                f.write(gitignore_add)
            print("\n  ✓ .gitignore обновлён")
    else:
        write(".gitignore", gitignore_add)

    print("\n✅ Скрипт завершён!\n")
    print("СЛЕДУЮЩИЕ ШАГИ (сделать вручную):")
    print("  1. rm -rf .claude/skills/   ← удалить старые скилы Русанова")
    print("  2. rm -rf office/agents/designer/  ← удалить старого агента")
    print("  3. mv office/agents/director/director_core.md office/agents/director/core.md")
    print("     (если файл называется director_core.md а не core.md)")
    print("  4. Заполнить katerina-profile/identity/brand.md реальными данными")
    print("  5. git add . && git commit -m 'feat: neuroshtab v2.2' && git push\n")


if __name__ == "__main__":
    main()
