import customtkinter as ctk
from tkinter import filedialog, messagebox
import os
import threading
from resume_parser import extract_text_from_path
from skill_extractor import extract_skills, clean_text
from ats_score import calculate_ats

# Set appearance mode and color theme
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class ATSApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("ATS Logic - Resume Analyzer")
        self.geometry("900x700")
        
        # Grid layout configuration
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Create sidebar
        self.sidebar_frame = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        
        self.logo_label = ctk.CTkLabel(self.sidebar_frame, text="ATS Analyzer", font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        
        self.desc_label = ctk.CTkLabel(self.sidebar_frame, text="Optimize your resume\nfor free.", font=ctk.CTkFont(size=12))
        self.desc_label.grid(row=1, column=0, padx=20, pady=10)

        # Main Content Area
        self.main_frame = ctk.CTkFrame(self, corner_radius=10)
        self.main_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure(3, weight=1) # Result area grows

        # 1. Resume Upload Section
        self.upload_label = ctk.CTkLabel(self.main_frame, text="1. Upload Resume (PDF, DOCX, TXT)", font=ctk.CTkFont(size=14, weight="bold"))
        self.upload_label.grid(row=0, column=0, padx=20, pady=(20, 5), sticky="w")

        self.file_path_var = ctk.StringVar(value="No file selected")
        self.file_entry = ctk.CTkEntry(self.main_frame, textvariable=self.file_path_var, width=400, state="readonly")
        self.file_entry.grid(row=1, column=0, padx=20, pady=5, sticky="ew")
        
        self.browse_btn = ctk.CTkButton(self.main_frame, text="Browse File", command=self.browse_file)
        self.browse_btn.grid(row=1, column=1, padx=20, pady=5)

        # 2. Job Description Section
        self.jd_label = ctk.CTkLabel(self.main_frame, text="2. Paste Job Description", font=ctk.CTkFont(size=14, weight="bold"))
        self.jd_label.grid(row=2, column=0, padx=20, pady=(20, 5), sticky="w")

        self.jd_text = ctk.CTkTextbox(self.main_frame, height=150)
        self.jd_text.grid(row=3, column=0, columnspan=2, padx=20, pady=5, sticky="nsew")

        # 3. Action Buttons
        self.action_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.action_frame.grid(row=4, column=0, columnspan=2, padx=20, pady=20)
        
        self.analyze_btn = ctk.CTkButton(self.action_frame, text="Analyze Resume", command=self.start_analysis, font=ctk.CTkFont(size=16, weight="bold"), height=40, width=200)
        self.analyze_btn.pack()

        # 4. Results Section
        self.result_frame = ctk.CTkFrame(self.main_frame, fg_color=("gray90", "gray20"), corner_radius=10)
        self.result_frame.grid(row=5, column=0, columnspan=2, padx=20, pady=(0, 20), sticky="nsew")
        self.result_frame.grid_columnconfigure(0, weight=1)
        
        self.score_label = ctk.CTkLabel(self.result_frame, text="ATS Score: --", font=ctk.CTkFont(size=24, weight="bold"))
        self.score_label.pack(pady=(20, 10))
        
        self.skills_label = ctk.CTkLabel(self.result_frame, text="Skills Found:", font=ctk.CTkFont(size=14, weight="bold"))
        self.skills_label.pack(pady=5)
        
        self.skills_text = ctk.CTkTextbox(self.result_frame, height=100, fg_color="transparent", text_color=("gray10", "gray90"))
        self.skills_text.pack(fill="both", expand=True, padx=20, pady=10)
        self.skills_text.insert("0.0", "Waiting for analysis...")
        self.skills_text.configure(state="disabled")

    def browse_file(self):
        filename = filedialog.askopenfilename(filetypes=[("Resume Files", "*.pdf;*.docx;*.txt")])
        if filename:
            self.file_path_var.set(filename)

    def start_analysis(self):
        # Run in thread to not freeze GUI
        threading.Thread(target=self.analyze, daemon=True).start()

    def analyze(self):
        resume_path = self.file_path_var.get()
        job_desc = self.jd_text.get("1.0", "end-1c")

        if resume_path == "No file selected" or not os.path.exists(resume_path):
            messagebox.showerror("Error", "Please select a valid resume file.")
            return

        if not job_desc.strip():
            messagebox.showerror("Error", "Please paste the job description.")
            return

        self.analyze_btn.configure(state="disabled", text="Processing...")
        
        try:
            # 1. Extract Text
            raw_text = extract_text_from_path(resume_path)
            cleaned_resume = clean_text(raw_text)
            
            # 2. Extract Skills
            resume_skills = extract_skills(cleaned_resume)
            
            # 3. Calculate Score
            cleaned_job = clean_text(job_desc)
            score = calculate_ats(cleaned_resume, cleaned_job)
            
            # 4. Update UI
            self.update_results(score, resume_skills)
            
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
        finally:
            self.analyze_btn.configure(state="normal", text="Analyze Resume")

    def update_results(self, score, skills):
        self.score_label.configure(text=f"ATS Score: {score}%", text_color="#2cc985" if score >= 50 else "#ff4b4b")
        
        self.skills_text.configure(state="normal")
        self.skills_text.delete("1.0", "end")
        if skills:
            self.skills_text.insert("0.0", ", ".join(skills))
        else:
            self.skills_text.insert("0.0", "No relevant technical skills found from our database.")
        self.skills_text.configure(state="disabled")

if __name__ == "__main__":
    app = ATSApp()
    app.mainloop()
