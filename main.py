import sys
import threading
import tkinter as tk
from tkinter import messagebox, scrolledtext

from scanner import enumerate_subdomains, check_live_domains, port_scan
from checklist import run_checklist
from ai_module import get_ai_vuln_advice
from reporter import generate_report

def run_full_scan(domain, gui_callback=None):
    subdomains = enumerate_subdomains(domain)
    if gui_callback: gui_callback(f"Found {len(subdomains)} subdomains.")
    
    live_hosts = check_live_domains(subdomains)
    if gui_callback: gui_callback(f"{len(live_hosts)} live hosts detected.")
    
    port_results = {}
    for host in live_hosts:
        if gui_callback: gui_callback(f"Scanning ports on {host}...")
        ports = port_scan(host)
        port_results[host] = ports
    
    if gui_callback: gui_callback("Running manual checklist...")
    run_checklist()
    
    if gui_callback: gui_callback("Getting AI vulnerability advice...")
    ai_notes = get_ai_vuln_advice("SQL Injection")
    
    report = generate_report(domain, subdomains, live_hosts, port_results, True, ai_notes)
    
    if gui_callback: gui_callback("Scan complete. Report generated.")
    
    return report

# --- CLI mode ---
def cli_mode(domain):
    report = run_full_scan(domain)
    print(report)
    with open(f"InputCheck_Report_{domain}.md", "w") as f:
        f.write(report)
    print(f"\nReport saved to InputCheck_Report_{domain}.md")

# --- GUI mode ---
def gui_mode():
    root = tk.Tk()
    root.title("InputCheck")

    tk.Label(root, text="Enter domain to scan:").pack()
    domain_entry = tk.Entry(root, width=40)
    domain_entry.pack()

    status_box = scrolledtext.ScrolledText(root, height=15, width=60)
    status_box.pack()

    def gui_log(msg):
        status_box.insert(tk.END, msg + "\n")
        status_box.see(tk.END)
        root.update()

    def start_scan():
        domain = domain_entry.get().strip()
        if not domain:
            messagebox.showerror("Error", "Please enter a domain.")
            return

        def thread_scan():
            report = run_full_scan(domain, gui_log)
            with open(f"InputCheck_Report_{domain}.md", "w") as f:
                f.write(report)
            gui_log(f"Report saved to InputCheck_Report_{domain}.md")

        threading.Thread(target=thread_scan).start()

    tk.Button(root, text="Start Scan", command=start_scan).pack(pady=5)
    root.mainloop()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        cli_mode(sys.argv[1])
    else:
        gui_mode()
