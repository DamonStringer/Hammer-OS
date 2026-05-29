# 🔨 The Hammer OS

A Python-based daily tracking system and database engine using flat-file CSV architecture.

## 🎯 Purpose: A Living Engineering Log
This repository continues my "Shadow Curriculum," documenting my progression in Python, systems architecture, and data management. 

While my previous project focused on nested JSON dictionaries and Object-Oriented Programming (OOP), **The Hammer OS** is dedicated to mastering flat-file databases, local state persistence, and enterprise-standard CSV generation.

## 🚀 Current Build — Version 0.1: The CSV Foundation
This initial build establishes a fully functional, locally hosted CRU (Create, Read, Update) database application from the ground up, entirely through the terminal.

**Key Features**
- **Database Forging:** Utilizes `csv.DictWriter` to generate a fresh, cleanly formatted CSV file with standardized headers natively readable by Google Sheets or Excel.
- **Append Mode Tracking:** Securely adds new daily goals and logs to the bottom of the database without destroying historical data using Python's `'a'` file mode.
- **Data Retrieval:** Streams the CSV back into active memory using `csv.DictReader` to display current goals in the terminal.
- **The CSV Rewrite Maneuver:** Implements a full state-rewrite protocol to update existing records (reading the file to a list, modifying the target dictionary in memory, wiping the file, and dumping the updated list back via `writerows()`).

## 🧠 What I’m Learning (The Curriculum)
As of V0.1, I’ve applied and practiced:
- **File I/O Streams:** Mastering the critical differences and dangers of Python's `'w'` (Write), `'a'` (Append), and `'r'` (Read) file access modes.
- **Data Translation:** Mapping Python dictionaries directly to structured spreadsheet columns.
- **In-Memory State Modification:** Managing the challenge of flat-file text documents by pulling data into active memory arrays to execute updates before pushing back to disk.
- **UI Routing:** Building continuous `while True:` operating loops and clean terminal menus.

## 🗺️ Roadmap to V1.0
- **Phase 1 — The Database Engine:** Build the core CRU (Create, Read, Update) operations for a CSV file. *(Completed)*
- **Phase 2 — Analytics & Deletion:** Add the ability to safely delete rows and calculate overall progress percentages.
- **Phase 3 — Cloud Integration:** Streamline the handoff between the local Python engine and cloud dashboards (like Google Sheets).
- **Phase 4 — Graphical User Interface (GUI):** Transition the terminal loops into a visual dashboard using frameworks like CustomTkinter or Kivy.
