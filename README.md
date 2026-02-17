# 📄 ATS Analyzer - Resume Optimization Tool

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![CustomTkinter](https://img.shields.io/badge/CustomTkinter-5.0+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)

**Optimize your resume for Applicant Tracking Systems (ATS) with AI-powered analysis**

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [How It Works](#-how-it-works) • [Contributing](#-contributing)

</div>

---

## 🎯 Overview

**ATS Analyzer** is a powerful desktop application that helps job seekers optimize their resumes for Applicant Tracking Systems (ATS). By analyzing your resume against a job description, it provides an ATS compatibility score and identifies matching skills, helping you tailor your resume for better job application success.

### Why ATS Analyzer?

- 🚀 **Instant Analysis** - Get your ATS score in seconds
- 🎯 **Skill Matching** - Identify which skills from the job description match your resume
- 📊 **Percentage Score** - Know exactly how well your resume aligns with the job
- 💼 **Multiple Formats** - Supports PDF, DOCX, and TXT resume formats
- 🎨 **Modern UI** - Clean, intuitive interface built with CustomTkinter
- 🆓 **100% Free** - No subscriptions, no hidden costs

---

## ✨ Features

### 📤 **Multi-Format Resume Upload**
- Support for PDF, DOCX, and TXT file formats
- Easy drag-and-drop or browse file selection
- Secure local processing - your data never leaves your computer

### 🔍 **Intelligent Skill Extraction**
- Comprehensive skill database covering:
  - **Programming Languages**: Python, Java, C++, JavaScript, TypeScript, etc.
  - **Frameworks**: React, Angular, Vue, Django, Flask, Node.js, etc.
  - **Databases**: SQL, MySQL, PostgreSQL, MongoDB, Redis, etc.
  - **Cloud & DevOps**: AWS, Azure, GCP, Docker, Kubernetes, Jenkins, etc.
  - **AI/ML**: TensorFlow, PyTorch, Scikit-learn, NLP, Computer Vision, etc.
  - **Soft Skills**: Communication, Leadership, Problem Solving, Agile, Scrum

### 📊 **ATS Score Calculation**
- Calculates percentage match between your resume and job description
- Color-coded results (Green for ≥50%, Red for <50%)
- Based on skill overlap analysis

### 🎨 **Modern User Interface**
- Dark mode interface for comfortable viewing
- Responsive design that adapts to your screen
- Real-time processing with loading indicators
- Clear visual feedback for all actions

---

## 🛠️ Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Step 1: Clone the Repository

```bash
git clone https://github.com/nireekshanaik20/ATS-Analyzer.git
cd ATS-Analyzer
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Run the Application

```bash
python gui.py
```

---

## 📖 Usage

### Quick Start Guide

1. **Launch the Application**
   ```bash
   python gui.py
   ```

2. **Upload Your Resume**
   - Click the "Browse File" button
   - Select your resume (PDF, DOCX, or TXT format)

3. **Paste Job Description**
   - Copy the job description from the job posting
   - Paste it into the text area

4. **Analyze**
   - Click "Analyze Resume" button
   - Wait for processing (usually takes 2-5 seconds)

5. **Review Results**
   - Check your ATS Score percentage
   - Review the list of matching skills
   - Optimize your resume based on the feedback

### 💡 Tips for Best Results

- ✅ Use the exact job description from the posting
- ✅ Ensure your resume is well-formatted and readable
- ✅ Include relevant keywords from the job description
- ✅ List your skills clearly in a dedicated section
- ✅ Use standard skill names (e.g., "Python" instead of "Py")

---

## 🔧 How It Works

### Architecture

```
┌─────────────────┐
│   User Input    │
│  (Resume + JD)  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Text Extraction│ ◄── resume_parser.py
│  (PDF/DOCX/TXT) │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Text Cleaning & │ ◄── skill_extractor.py
│ Skill Extraction│
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  ATS Score      │ ◄── ats_score.py
│  Calculation    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Display Results│ ◄── gui.py
│   (GUI Output)  │
└─────────────────┘
```

### Core Components

1. **`gui.py`** - Main application interface
   - Built with CustomTkinter for modern UI
   - Handles user interactions and file uploads
   - Displays results with color-coded scores

2. **`resume_parser.py`** - Document processing
   - Extracts text from PDF, DOCX, and TXT files
   - Uses pdfminer.six for PDF parsing
   - Uses docx2txt for Word document parsing

3. **`skill_extractor.py`** - Skill identification
   - Maintains comprehensive skill database
   - Uses regex pattern matching for accuracy
   - Cleans and normalizes text for better matching

4. **`ats_score.py`** - Score calculation
   - Compares resume skills with job description skills
   - Calculates percentage match
   - Returns rounded score for clarity

---

## 📦 Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| `customtkinter` | Latest | Modern UI framework |
| `pdfminer.six` | Latest | PDF text extraction |
| `docx2txt` | Latest | DOCX text extraction |
| `nltk` | Latest | Natural language processing |
| `pillow` | Latest | Image processing support |
| `packaging` | Latest | Version handling |

---

## 🎨 Screenshots

### Main Interface
The application features a clean, modern dark-mode interface with:
- Sidebar with branding
- Resume upload section
- Job description input area
- Analysis button
- Results display with color-coded scores

---

## 🚀 Future Enhancements

- [ ] Add more comprehensive skill database
- [ ] Include keyword density analysis
- [ ] Generate resume improvement suggestions
- [ ] Support for multiple resume comparisons
- [ ] Export analysis reports as PDF
- [ ] Add resume formatting checker
- [ ] Include industry-specific skill sets
- [ ] Implement machine learning for better matching
- [ ] Add support for more file formats
- [ ] Create web-based version

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. **Commit your changes**
   ```bash
   git commit -m 'Add some AmazingFeature'
   ```
4. **Push to the branch**
   ```bash
   git push origin feature/AmazingFeature
   ```
5. **Open a Pull Request**

### Areas for Contribution

- 🐛 Bug fixes
- ✨ New features
- 📝 Documentation improvements
- 🎨 UI/UX enhancements
- 🧪 Test coverage
- 🌐 Internationalization

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Nireeksha Naik**
- GitHub: [@nireekshanaik20](https://github.com/nireekshanaik20)
- Masters in Artificial Intelligence

---

## 🙏 Acknowledgments

- CustomTkinter for the modern UI framework
- PDFMiner.six for PDF text extraction
- The open-source community for inspiration and support

---

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/nireekshanaik20/ATS-Analyzer/issues) page
2. Create a new issue with detailed description
3. Star ⭐ this repository if you find it helpful!

---

<div align="center">

**Made with ❤️ by Nireeksha Naik**

If this project helped you, please consider giving it a ⭐!

</div>
