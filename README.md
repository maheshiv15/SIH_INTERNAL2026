# 🌾 AgriVision AI — Unified Agricultural Neural Vision & Livestock Clinical Triage Platform

[![SIH 2026](https://img.shields.io/badge/Smart%20India%20Hackathon-2026-brightgreen.svg)](https://sih-internal-2026-pi.vercel.app/)
[![IIT Jodhpur](https://img.shields.io/badge/Institute-IIT%20Jodhpur-blue.svg)](https://www.iitj.ac.in/)
[![Team](https://img.shields.io/badge/Team-NeoMedtech-emerald.svg)](https://sih-internal-2026-pi.vercel.app/)
[![Live Demo](https://img.shields.io/badge/Live%20Demo-Vercel%20Deployed-success.svg)](https://sih-internal-2026-pi.vercel.app/)
[![AI Engine](https://img.shields.io/badge/AI%20Engine-Gemini%203.5%20Flash%20Lite-orange.svg)](https://ai.google.dev/)

> **Smart India Hackathon 2026 — Internal Round Submission**  
> **Problem Statement ID:** `Problem Statement 1 (Software PS)`  
> **Title:** *Unified AI Agri-Vision Platform for Crop Advisory and Livestock Management*  
> **Theme:** Agriculture, FoodTech & Rural Development  
> **Team:** **NeoMedtech** (Indian Institute of Technology Jodhpur — AISHE: `U-0395`)  
> **Live Production URL:** [https://sih-internal-2026-pi.vercel.app/](https://sih-internal-2026-pi.vercel.app/)

---

## 📌 Executive Summary & Problem Formulation

Marginal and smallholder farmers in India operate in an integrated dual-livelihood ecosystem where **cash crop cultivation** and **dairy livestock rearing** co-exist. However, current digital agricultural tools are severely fragmented:
* Crop diagnostics and veterinary advisory exist in isolated, complex applications.
* India faces an acute shortage of rural veterinary and agricultural extension officers (**1 veterinarian per 15,000+ livestock**).
* Farmers frequently fall victim to predatory over-prescription by pesticide retailers or suffer catastrophic delays during contagious livestock epidemics (Lumpy Skin Disease, Foot & Mouth Disease).

**AgriVision AI** solves Problem Statement 1 by delivering a **unified, voice-first, dual-domain diagnostic ecosystem** in the farmer's pocket, combining **multimodal neural vision** for crop pathology with **AIIMS Jodhpur-grade clinical veterinary triage**.

---

## 🚀 Key Features & Capabilities

```
                       ┌────────────────────────────────────────┐
                       │           AgriVision AI Platform       │
                       │          (Team NeoMedtech - IITJ)      │
                       └───────────────────┬────────────────────┘
                                           │
         ┌───────────────────┬─────────────┴────────────┬───────────────────┐
         ▼                   ▼                          ▼                   ▼
┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐
│ 🌿 Crop Doctor  │ │ 🐄 Cattle Triage│ │ 📝 Farm Ledger  │ │ 🌦️ Weather/Mandi│
│  Multimodal     │ │  Clinical AIIMS │ │  Milk & Expense │ │  Live Open-Meteo│
│  Vision AI      │ │  Triage + 1962  │ │  Margin Tracker │ │  & Outbreak Hub │
└─────────────────┘ └─────────────────┘ └─────────────────┘ └─────────────────┘
         │                   │                          │                   │
         └───────────────────┴─────────────┬────────────┴───────────────────┘
                                           ▼
                       ┌────────────────────────────────────────┐
                       │  🗣️ Multilingual Voice AI Doctor (FAB) │
                       │    Hindi • Marwari • English Speech    │
                       └────────────────────────────────────────┘
```

### 1. 🌿 Neural Crop Vision & Healthy Leaf Certification
* **Dual-Tier Gemini Vision Core:** High-speed foliar pathology using **Google Gemini 3.5 Flash Lite** with automated fallback to **Gemini 3.1 Flash Lite**.
* **Zero-Chemical & Healthy Certification:** Distinguishes healthy leaves from infected ones, providing **organic bio-nutrition recipes** (Jeevamrut, fermented buttermilk) instead of unnecessary pesticide sprays.
* **Precision Chemical Dosage Calculator:** Computes exact tank water and fungicide chemical grams based on farmer's field size (**Bigha / Acre / Hectare**) and knapsack sprayer capacity.

### 2. 🐄 Clinical Livestock Health & Veterinary Triage
* **AIIMS Jodhpur-Standard Triage Protocols:** Severity triage matrix for epidemic livestock conditions (**Lumpy Skin Disease, Foot & Mouth Disease (FMD), Bovine Mastitis, Hemorrhagic Septicemia**).
* **Emergency Dispatch (1962):** 1-tap direct dialing of the **1962 National Animal Ambulance Helpline**.
* **Non-Harmful First-Aid Guidance:** Safe antiseptic wound management (Potassium Permanganate wash, Turmeric-Neem paste, quarantine isolation).

### 3. 📝 Digital Farm & Livestock Ledger
* **Daily Dairy Tracker:** Computes morning/evening milk yields, fat percentages, and direct revenues.
* **Agro-Expense Book:** Records fertilizer, seed, and feed costs to calculate net seasonal farm profits.

### 4. 🌦️ 100% Live Open-Meteo Weather & Live Mandi Hub
* **Live Satellite Telemetry:** Real-time temperature, humidity, wind, and precipitation probability for Western Rajasthan districts (**Jodhpur, Nagaur, Pali, Barmer, Jaisalmer, Bikaner**).
* **Dynamic Fungal Spore Risk Barometer:** Real-time epidemiological risk calculation based on live humidity (>75%) + heat index combinations.
* **Live APMC Mandi Rates:** Real-time wholesale spot prices for Jeera, Isabgol, Mustard, Wheat, Guar Gum, and Moong with holding/selling advisories.

### 5. 🗣️ Multilingual Voice Assistant & Farmer-First UX
* **Clean 2x2 Action Tile Dashboard:** Simplified navigation designed for low-literacy farmers and rural touch screens.
* **Sunlight-Readable High Contrast Theme:** Light mode default optimized for direct outdoor farm sunlight.
* **Speech-to-Speech Engine:** Web Speech Recognition and Conversational Audio Synthesis in **Hindi, Marwari (माड़वाड़ी), and English**.

---

## 🛠️ System Architecture & Technology Stack

| Layer | Technologies Used |
| :--- | :--- |
| **Frontend Framework** | React.js (Vite), Modern Vanilla CSS Design Tokens, Glassmorphism |
| **Multimodal Vision AI** | Google Gemini 3.5 Flash Lite (Primary) + Gemini 3.1 Flash Lite (Fallback) |
| **Speech & Audio Engine**| Web Speech Recognition API & Web Speech Synthesis (Hindi & Marwari phonetics) |
| **Camera & Vision Stream**| WebRTC Video Capture API & HTML5 Canvas Downscaling |
| **Meteorology & Mandi** | Open-Meteo Satellite REST API & APMC Wholesale e-NAM Ticker |
| **Hosting & CI/CD** | Vercel Global Edge Network, GitHub Automated Deployment |

---

## 👥 Team NeoMedtech (IIT Jodhpur)

* **Maheshiv Prajapat (Team Leader)** — *MMT Scholar, IIT Jodhpur & Asst. Nursing Superintendent, AIIMS Jodhpur* (`m26im1008@iitj.ac.in`)
* **Dr. Eshitaa Panwar** — *MMT Scholar, IIT Jodhpur & BDS Dental Surgeon* (`m26im1005@iitj.ac.in`)
* **Siddhant Shenvi** — *MMT Scholar, IIT Jodhpur & B.Tech Software Lead* (`m26im1012@iitj.ac.in`)
* **Mrunal Sonawale** — *MMT Scholar, IIT Jodhpur & B.Pharm Pharmacological Lead* (`m26im1010@iitj.ac.in`)
* **Kishore Vijayakumar** — *MMT Scholar, IIT Jodhpur & MedTech Integration Lead* (`m26im1006@iitj.ac.in`)
* **Megha** — *MMT Scholar, IIT Jodhpur & Rural UX Design Lead* (`m26im1009@iitj.ac.in`)

---

## 💻 Local Development & Installation

### Prerequisites
* **Node.js:** v18.0 or higher
* **npm:** v9.0 or higher
* **Gemini API Key:** (Get free key from [Google AI Studio](https://aistudio.google.com/))

### Steps to Run Locally

```bash
# 1. Clone the repository
git clone https://github.com/maheshiv15/SIH_INTERNAL2026.git
cd SIH_INTERNAL2026

# 2. Install dependencies
npm install

# 3. Create .env file for Gemini API Key (Optional: Can also be entered via in-app settings modal)
echo "VITE_GEMINI_API_KEY=your_gemini_api_key_here" > .env

# 4. Start local development server
npm run dev

# 5. Build production bundle
npm run build
```

---

## 🏆 SIH 2026 Evaluation Deliverables

* 🌐 **Live Web Application (Vercel):** [https://sih-internal-2026-pi.vercel.app/](https://sih-internal-2026-pi.vercel.app/)
* 💻 **GitHub Source Repository:** [https://github.com/maheshiv15/SIH_INTERNAL2026](https://github.com/maheshiv15/SIH_INTERNAL2026)
* 📄 **Official 6-Slide Pitch Deck (PDF — View Directly on GitHub):** [**`SIH_2026_AgriVision_AI_Submission.pdf`**](./SIH_2026_AgriVision_AI_Submission.pdf)
* 📊 **Official Presentation Source (PPTX — Editable File):** [**`SIH_2026_AgriVision_AI_Submission.pptx`**](./SIH_2026_AgriVision_AI_Submission.pptx)

---
*Developed with pride by **Team NeoMedtech**, Indian Institute of Technology Jodhpur (IIT Jodhpur) for Smart India Hackathon 2026.*
