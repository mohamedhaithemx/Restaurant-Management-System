# 🍽️ Restaurant Management System (CLI) | نظام إدارة مطعم تفاعلي

> **A Python OOP project** — Interactive CLI restaurant management system built with clean OOP principles.  
> **مشروع تطبيقي بلغة Python** — نظام إدارة مطعم بواجهة سطر أوامر، مبني بأساسيات البرمجة الكائنية (OOP).

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![OOP](https://img.shields.io/badge/Architecture-OOP-green)
![CLI](https://img.shields.io/badge/Interface-CLI-lightgrey)

---

## 📑 Table of Contents | المحتويات

- [Overview | نظرة عامة](#overview--نظرة-عامة)
- [Features | المميزات](#features--المميزات)
- [Quick Start | بداية سريعة](#quick-start--بداية-سريعة)
- [Project Structure | هيكل المشروع](#project-structure--هيكل-المشروع)
- [Technical Concepts | المفاهيم التقنية](#technical-concepts--المفاهيم-التقنية)
- [Usage Example | مثال استخدام](#usage-example--مثال-استخدام)

---

## 📌 Overview | نظرة عامة

**English:**  
This project simulates a real-world restaurant ordering system via the command line. It applies core OOP concepts — encapsulation, composition, single responsibility — in a practical scenario: managing tables, tracking orders, calculating bills, and applying VIP discounts.

**العربية:**  
هذا المشروع يحاكي نظام طلبات مطعم واقعي عبر واجهة الأوامر. يطبق المفاهيم الأساسية للبرمجة الكائنية (OOP) في سيناريو عملي: إدارة الطاولات، تتبع الطلبات، حساب الفواتير، وتطبيق خصم العملاء المميزين (VIP). تم تصميم النظام بعزل المنطق البرمجي عن واجهة المستخدم، مما يسهل تحويله لاحقاً إلى تطبيق ويب أو واجهة رسومية.

---

## ✨ Features | المميزات

| English | العربية |
|:--------|:--------|
| ✅ Fully interactive CLI interface | ✅ واجهة تفاعلية كاملة عبر سطر الأوامر |
| ✅ Detailed receipt on checkout |  طباعة فاتورة مفصلة عند إتمام الطلب |
| 💎 VIP mode with 10% auto discount | 💎 دعم وضع VIP بخصم تلقائي 10% |
|  Auto table reset after payment |  إعادة تعيين الطاولة تلقائياً بعد الدفع |
| 🛡️ Defensive programming (input validation) | 🛡️ حماية من إدخال البيانات الخاطئة |
| 📦 Modular structure (classes, logic, UI separation) | 📦 هيكل معياري يفصل بين الأصناف والمنطق وواجهة المستخدم |

---

## 🚀 Quick Start | بداية سريعة

```bash
# Clone the repository | استنساخ المستودع
git clone https://github.com/mohamedhaithemx/app_restaurant.git
cd app_restaurant

# Run the application | تشغيل التطبيق
python managment.py
```

**Requirements:** Python 3.10+ (no external dependencies | لا يحتاج مكتبات خارجية)

---

## 📂 Project Structure | هيكل المشروع

```text
app_restaurant/
├── food.py          # 🧠 Core logic: classes (MenuItem, Table, Hall) & menu items
│                    #   المنطق الأساسي: الفئات وقائمة الأصناف
├── managment.py     # 🖥️ UI layer: user interface & main program flow
│                    #   واجهة المستخدم والتدفق الرئيسي للتطبيق
└── README.md        # 📖 Documentation (this file | هذا الملف)
```

---

## 🛠 Technical Concepts | المفاهيم التقنية

| Concept | Application in Code | التطبيق في الكود |
|:--------|:--------------------|:-----------------|
| **Encapsulation** | `@property` for dynamic total with VIP discount; `_total` is private | إخفاء `_total` ومنع التعديل المباشر |
| **Composition** | `Hall` contains a list of `Table` objects (not inheritance) | `Hall` يحتوي على قائمة `Table` بدلاً من التوريث |
| **Single Source of Truth** | `MENU_ITEMS` is the unified menu list | قائمة `MENU_ITEMS` موحدة كمصدر وحيد للأصناف |
| **Type Hints** | `-> str`, `-> float`, `-> None` annotations | توثيق الأنواع لتحسين القراءة |
| **Lifecycle Management** | Clear lifecycle: `init → add → checkout → reset` | دورة حياة واضحة لعزل الطلبات |
| **DRY Principle** | Centralized `get_int_input()` for input validation | دالة موحدة للتحقق من المدخلات ومنع التكرار |

---

## 💻 Usage Example | مثال استخدام

```
=== Welcome to the Restaurant ===

| Hall: 1 | | Hall: 2 | | Hall: 3 | | Hall: 4 |
Enter Hall Number (1-4): 1

=== Hall: 1 ===
| Table: 1 | | Table: 2 | | Table: 3 | | Table: 4 | | Table: 5 |
Enter Table Number (1-5): 2

--- Actions ---
1. Add Food
2. View Order
3. Checkout
4. VIP Mode (10% Off)
5. Exit
Enter Action: 1

Choose category:
1: Main
2: Extra
Choose category (1 or 2): 1

Main Dishes:
1: meat - 280 EGP
2: chicken - 185 EGP
3: rice - 30 EGP
4: pasta - 80 EGP
5: fish - 200 EGP
Choose item number: 2
Added: chicken - 185 EGP
```

---

## 📄 License

This project is for educational purposes — part of the CS50P course journey.  
هذا المشروع لأغراض تعليمية — ضمن رحلة دورة CS50P.
