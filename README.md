# 🚀 InputCheck - Ultimate Bug Bounty Recon & Scanning Toolkit 🔍🛡️

![Version](https://img.shields.io/badge/version-1.0-blue) ![Python](https://img.shields.io/badge/python-3.8%2B-green) ![License](https://img.shields.io/badge/license-MIT-yellow)

---

## 🌟 Overview

**InputCheck** is a **powerful**, **modular**, and **easy-to-use** bug bounty reconnaissance and scanning tool designed to help security researchers and pentesters automate and enhance their workflow. It covers everything from subdomain enumeration to port scanning, manual checklists, and AI-assisted vulnerability analysis — all wrapped in a clean, maintainable Python codebase.

---

## 🔥 Features

* 🌐 **Subdomain Enumeration**
  Discover hidden assets using [subfinder](https://github.com/projectdiscovery/subfinder).

* ⚡ **Live Host Detection**
  Quickly filter live domains with [httpx](https://github.com/projectdiscovery/httpx).

* 🔌 **Threaded Port Scanning**
  Speed up scanning using multi-threaded TCP probes to find open ports.

* 📋 **Interactive Bug Hunting Checklist**
  Follow a guided checklist to avoid missing critical manual testing steps.

* 🤖 **AI-Powered Insights**
  Integrate with OpenAI GPT API for smart vulnerability explanations & remediation tips.

* 📝 **Markdown Report Generator**
  Auto-generate professional reports perfect for bug bounty submissions.

* 🧩 **Modular Architecture**
  Clean separation of scanning, checklist, AI, and reporting modules for easy extension.

* 🖥️ **CLI & GUI Support**
  Use InputCheck from your terminal or via an intuitive GUI (Tkinter).

---

## 🛠️ Installation & Setup

### Prerequisites

* Python 3.8+
* Install external tools and add to your system PATH:

  * [subfinder](https://github.com/projectdiscovery/subfinder)
  * [httpx](https://github.com/projectdiscovery/httpx)
  * (Optional) [nuclei](https://github.com/projectdiscovery/nuclei) for vulnerability scanning

### Python Dependencies

```bash
pip install openai
```

### OpenAI API Setup

Get your API key from [OpenAI](https://platform.openai.com/account/api-keys) and export it:

```bash
export OPENAI_API_KEY="your_api_key_here"
```

Or set it in `ai_module.py` for local testing.

---

## 🚀 How to Use

### Command-Line Interface (CLI)

Scan a domain with subdomains and ports, plus AI insights and generate a report:

```bash
python main.py example.com
```

Your report will be saved as `InputCheck_Report_example.com.md`

### Graphical User Interface (GUI)

Run without parameters to launch GUI mode:

```bash
python main.py
```

Enter the target domain and click **Start Scan** — watch live progress and generate reports easily.

---

## 🧩 Project Structure

| File           | Purpose                                  |
| -------------- | ---------------------------------------- |
| `main.py`      | CLI & GUI entry point                    |
| `scanner.py`   | Subdomain enumeration, live check, ports |
| `checklist.py` | Interactive manual bug hunting checklist |
| `ai_module.py` | OpenAI GPT integration for vulnerability |
| `reporter.py`  | Markdown report generator                |
| `utils.py`     | Helper functions and utilities           |

---

## 🤝 Contribution

Love to see contributions! Feel free to:

* Add new scanning modules
* Improve AI integrations
* Enhance checklist guidance
* Fix bugs or improve docs

Open issues or submit pull requests anytime.

---

## ⚠️ Disclaimer

🔒 **Use responsibly!** Only test systems you have explicit permission to scan. Unauthorized scanning or hacking is illegal.

---

## 📬 Contact & Support

**Vaishnav4281** 
Stay curious. Stay persistent. Happy hunting! 🎯

---

**InputCheck** — Make every bug count! ⚡🔐
