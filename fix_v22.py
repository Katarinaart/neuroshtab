#!/usr/bin/env python3
"""
Нейроштаб v2.2 - Fix Structure
"""

import os

def main():
    print("\n🚀 Запуск исправления структуры v2.2\n")

    # 1. Переименовываем director_core.md → core.md
    old = "office/agents/director/director_core.md"
    new = "office/agents/director/core.md"

    if os.path.exists(old) and not os.path.exists(new):
        os.rename(old, new)
        print(f"✓ Переименовано: {old} → {new}")
    elif os.path.exists(new):
        print(f"· Файл {new} уже существует")
    else:
        print(f"! Файл {old} не найден")

    # 2. Создаём недостающих агентов
    agents_to_create = ["product", "content", "growth", "architect"]

    print("\n── Создание агентов ──")
    for agent in agents_to_create:
        path = f"office/agents/{agent}"
        if not os.path.exists(path):
            os.makedirs(path)
            print(f"+ Создана папка: {path}")
        else:
            print(f"· Папка уже существует: {path}")

        # Создаём layered memory файлы
        for filename in ["core.md", "overrides.md", "memory.md", "failures.md"]:
            filepath = os.path.join(path, filename)
            if not os.path.exists(filepath):
                open(filepath, 'w').close()
                print(f"  + {filename}")
            else:
                print(f"  · {filename} уже существует")

    print("\n✅ Готово!\n")
    print("Теперь выполни:")
    print("git add -A")
    print('git commit -m "fix: rename director_core.md and add missing agents"')
    print("git push origin main\n")

if __name__ == "__main__":
    main()
