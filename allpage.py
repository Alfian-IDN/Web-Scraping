from bs4 import BeautifulSoup
import requests
import os # use for store file in one folder 


def scrape_and_save_transcript(url,folder_path):
    result = requests.get(url)
    content = result.text
    soup = BeautifulSoup(content, 'lxml')

    box = soup.find('article',class_='main-article')
    title = box.find('h1').get_text()
    fix_title= title.replace('?', '').replace('\\', '').replace('/', '').replace(':', '')#or u can create regex
    transcript = box.find('div', class_='full-script').get_text(strip=True, separator=' ')
    
    file_path = os.path.join(folder_path, f'{fix_title}.txt')
    with open(file_path, 'w', encoding='utf-8', errors='ignore') as file:
         file.write(transcript)

def main():
        root = 'https://subslikescript.com'
        for page in range(1, 6): 
                url =f'{root}/movies/?page={page}'  
                print(url)    
                result = requests.get(url)
                content = result.text
                soup = BeautifulSoup(content, 'lxml')
                folder_path = 'multiple-pages' #store result in one folder

                box = soup.find('article',class_='main-article')
                links = [f'{root}/{link["href"]}' for link in box.find_all('a', href=True)]
                        

                for link in links:
                        print(f'printing_urls:{link}')
                        scrape_and_save_transcript(link, folder_path)
                        

if __name__=="__main__":
        main()
        
