# Braille Encoder Pipeline

[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue.svg)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub Stars](https://img.shields.io/github/stars/VivanRajath/Braille-Encoder.svg)](https://github.com/VivanRajath/Braille-Encoder/stargazers)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)

A comprehensive Python pipeline that converts webpages, PDFs, and images into Braille-readable text for enhanced accessibility. The pipeline automatically generates image captions using state-of-the-art AI models and converts all content to Unicode Braille format for use with refreshable Braille displays.



## 🌟 Features

- **📄 Multi-format Support**: Extract text from webpages and PDF files
- **🖼️ Intelligent Image Captioning**: Auto-generate captions using Hugging Face's `vit-gpt2-image-captioning` model
- **⠁ Unicode Braille Conversion**: Convert all text to proper Unicode Braille format
- **💾 File Export**: Save Braille output to `.txt` files for refreshable Braille displays
- **🔧 Modular Architecture**: Easy to maintain, extend, and customize
- **♿ Accessibility Focused**: Designed specifically for blind and visually impaired users

## 🛠️ Installation

### Prerequisites

- Python 3.7 or higher
- Internet connection (required for image captioning model)

### Quick Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/VivanRajath/Braille-Encoder.git
   cd Braille-Encoder
   ```

2. **Create Virtual Environment**
   ```bash
   python -m venv venv
   ```

3. **Activate Virtual Environment**
   
   **Windows (Command Prompt):**
   ```cmd
   venv\Scripts\activate
   ```
   
   **Windows (PowerShell):**
   ```powershell
   venv\Scripts\Activate.ps1
   ```
   
   **Linux/macOS:**
   ```bash
   source venv/bin/activate
   ```

4. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Manual Installation

If you prefer to install packages manually:

```bash
pip install torch torchvision transformers pdfplumber pillow beautifulsoup4 requests
```

## 🚀 Usage

### Basic Usage

1. **Run the Pipeline**
   ```bash
   python main.py
   ```

2. **Choose Input Type**
   ```
   Choose input type:
   1 - Webpage
   2 - PDF
   ```

3. **Provide Input**
   - For webpages: Enter the complete URL (e.g., `https://example.com`)
   - For PDFs: Enter the file path (e.g., `./documents/sample.pdf`)

4. **Output**
   - Braille text is displayed in the terminal
   - Output is automatically saved to `braille_output.txt`

### Example

```bash
$ python main.py
Choose input type:
1 - Webpage
2 - PDF
Enter your choice: 1
Enter webpage URL: https://example.com

Processing webpage...
Extracting text and images...
Generating image captions...
Converting to Braille...

⠓⠑⠇⠇⠕ ⠺⠕⠗⠇⠙ (Hello World)

Output saved to braille_output.txt
```

## 🏗️ Architecture

```
Braille Encoder Pipeline
├── main.py              # Main entry point
│   ├── webpage_extractor.py    # Webpage text extraction
│   ├── pdf_extractor.py        # PDF text extraction
│   └── image_processor.py      # Image captioning
│   └── braille_converter.py    # Text to Braille conversion
└── requirements.txt     # Dependencies
```

## 📋 Requirements

The project depends on the following Python packages:

- `torch` - PyTorch for deep learning models
- `torchvision` - Computer vision utilities
- `transformers` - Hugging Face transformers library
- `pdfplumber` - PDF text extraction
- `pillow` - Image processing
- `beautifulsoup4` - HTML parsing
- `requests` - HTTP requests

## ⚙️ Configuration

### Image Captioning Model

The pipeline uses the `nlpconnect/vit-gpt2-image-captioning` model by default. You can modify this in the configuration:

```python
MODEL_NAME = "nlpconnect/vit-gpt2-image-captioning"
```

### Braille Settings

- Output format: Unicode Braille (Grade 1)
- Encoding: UTF-8
- Line length: Configurable (default: 80 characters)

## 🔍 How It Works

1. **Content Extraction**: Uses BeautifulSoup for webpage parsing and pdfplumber for PDF text extraction
2. **Image Processing**: Identifies images in content and processes them through the vision-to-text model
3. **Caption Generation**: Generates descriptive captions for all images using AI
4. **Braille Conversion**: Converts all text content (including captions) to Unicode Braille
5. **Output Generation**: Saves the final Braille text to a file for use with assistive devices

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

### Development Setup

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/Braille-Encoder.git

# Add upstream remote
git remote add upstream https://github.com/VivanRajath/Braille-Encoder.git

# Create development environment
python -m venv dev-env
source dev-env/bin/activate  # or dev-env\Scripts\activate on Windows
pip install -r requirements-dev.txt
```



## 🐛 Known Issues

- **Internet Dependency**: Requires internet connection for image captioning model on first run and proper GPU to handle heavy models
- **PDF Complexity**: Complex PDFs with embedded images may have slower processing times
- **Language Support**: Currently optimized for English text

## 🗺️ Roadmap

- [ ] **Word Document Support** - Add `.docx` file processing
- [ ] **Multiple Language Support** - Extend beyond English
- [ ] **Grade 2 Braille** - Advanced Braille contractions
- [ ] **Batch Processing** - Process multiple files simultaneously
- [ ] **Web Interface** - Browser-based GUI
- [ ] **API Endpoint** - RESTful API for integration

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Hugging Face](https://huggingface.co/) for the image captioning models
- [pdfplumber](https://github.com/jsvine/pdfplumber) for PDF processing capabilities
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/) for HTML parsing
- The accessibility community for inspiration and feedback

## 👨‍💻 Author

**Vivan Rajath**

- GitHub: [@VivanRajath](https://github.com/VivanRajath)
- Email: [your.email@example.com](mailto:vivanrajath999@gmail.com)


## 📞 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/VivanRajath/Braille-Encoder/issues) page
2. Create a new issue with detailed information
3. Join our [Discussion Forum](https://github.com/VivanRajath/Braille-Encoder/discussions)

---

<div align="center">
  <strong>⠓⠑⠇⠏⠊⠝⠛ ⠍⠁⠅⠑ ⠞⠓⠑ ⠺⠑⠃ ⠁⠉⠉⠑⠎⠎⠊⠃⠇⠑ ⠋⠕⠗ ⠑⠧⠑⠗⠽⠕⠝⠑</strong><br>
  <em>Helping make the web accessible for everyone</em>
</div>
