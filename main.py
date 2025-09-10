# main.py
from braille import text_to_braille
from webpage import process_webpage
from pdf_processor import process_pdf

def main():
    choice = input("Choose input type: 1-Webpage, 2-PDF: ").strip()
    if choice == "1":
        url = input("Enter webpage URL: ").strip()
        text = process_webpage(url)
    elif choice == "2":
        path = input("Enter PDF file path: ").strip()
        text = process_pdf(path)
    else:
        print("Invalid choice")
        return

    print("\n--- Extracted Content ---\n")
    print(text[:500], "...\n")
    
    braille_text = text_to_braille(text)
    print("\n--- Braille Output ---\n")
    print(braille_text[:200])

    # Save Braille
    with open("braille_output.txt", "w", encoding="utf-8") as f:
        f.write(braille_text)
    print("✅ Braille saved to braille_output.txt")

if __name__ == "__main__":
    main()
