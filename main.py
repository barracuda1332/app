from gtts import gTTS
from art import tprint
import pdfplumber
from pathlib import Path
from tqdm import tqdm


def pdf_to_mp3(file_path='test.pdf', language='en'):

    if Path(file_path).is_file() and Path(file_path).suffix == '.pdf':
        #return 'file exits!'
        print(f'[+] Original file: {Path(file_path).name}')
        print(f'[+] Reading PDF...')

        with pdfplumber.PDF(open(file=file_path, mode='rb')) as pdf:
            pages = []
            for page in tqdm(pdf.pages):
                pages.append(page.extract_text())
            # pages = [page.extract_text() for page in tqdm(pdf.pages)]

        text = ''.join(pages)
        text = text.replace('\n','')

        my_audio = gTTS(text=text, lang=language, slow=False)
        file_name = Path(file_path).stem
        my_audio.save(f'{file_name}.mp3')
        print(f'[+] Create file {file_name}.mp3')

        return f'[+] {file_name}.mp3 saved successfully!\n'

    else:
        return 'File not exist, check the file path!'


def main():
    tprint('ARTSOFT', font='bulbhead')
    file_path = input("\nEnter a file path: ")
    language = input("Choose your language, for example 'en' or 'ru': ")
    print(pdf_to_mp3(file_path=file_path, language=language))


if __name__ == '__main__':
    main()