from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
import pandas as pd
import json
import time

def iniciar_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--log-level=3")  # silencia logs do Chrome

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return driver

def extrair_vagas(driver):
    url = "https://remoteok.com/"
    driver.get(url)
    time.sleep(3)  # espera para a página carregar

    vagas = []

    elementos = driver.find_elements(By.CSS_SELECTOR, 'tr.job')
    print(f"[INFO] {len(elementos)} vagas encontradas.")

    for el in elementos:
        try:
            titulo = el.find_element(By.CSS_SELECTOR, 'h2').text.strip()
            empresa = el.find_element(By.CSS_SELECTOR, 'h3').text.strip()

            try:
                local = el.find_element(By.CLASS_NAME, 'location').text.strip()
            except:
                local = "Não informado"

            link = el.get_attribute('data-href')
            if link and not link.startswith("https://"):
                link = "https://remoteok.com" + link

            # Tags filtradas (sem vazias)
            tags = [tag.text.strip() for tag in el.find_elements(By.CSS_SELECTOR, '.tags h3') if tag.text.strip()]

            # Data de publicação formatada: dd-mm-aaaa / hh:mm
            try:
                raw_date = el.find_element(By.TAG_NAME, 'time').get_attribute('datetime')
                dt = datetime.fromisoformat(raw_date.replace("Z", "+00:00"))
                data_publicacao = dt.strftime("%d-%m-%Y / %H:%M")
            except:
                data_publicacao = "Não informado"

            vaga = {
                "titulo": titulo,
                "empresa": empresa,
                "local": local,
                "link": link,
                "tags": tags,
                "data_publicacao": data_publicacao
            }

            vagas.append(vaga)

        except Exception as e:
            print(f"[ERRO] Erro ao processar vaga: {e}")

    return vagas

def salvar_dados(vagas):
    with open("jobs.json", "w", encoding="utf-8") as f:
        json.dump(vagas, f, indent=4, ensure_ascii=False)
    print("[INFO] Dados salvos em jobs.json")

    df = pd.DataFrame(vagas)
    df.to_csv("jobs.csv", index=False, encoding="utf-8")
    print("[INFO] Dados salvos em jobs.csv")

def main():
    driver = iniciar_driver()
    vagas = extrair_vagas(driver)
    salvar_dados(vagas)
    driver.quit()

if __name__ == "__main__":
    main()
