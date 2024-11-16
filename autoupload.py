import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import time
import shutil

def upload_file_to_whatsapp(driver, file_name):
    # Attach the document
    attachment_box = driver.find_element(By.XPATH, '//div[@title="Attach"]')
    attachment_box.click()

    # Select the document option
    document_option = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[3]/div[4]/div/footer/div[1]/div/span/div/div[1]/div/div/span/div/ul/div/div[1]/li'))
    )
    # document_option.click()

    # Wait for the file input to be present
    file_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[3]/div[4]/div/footer/div[1]/div/span/div/div[1]/div/div/span/div/ul/div/div[1]/li/div/input'))
    )

    # Use absolute path for the file
    file_path = os.path.abspath(file_name)
    file_input.send_keys(file_path)  # Update with the path to your audio file

    # Wait for the file to upload
    # time.sleep(20)

    # Send the text message
    # Send the file name as a message
    # try:
    #     message_box = WebDriverWait(driver, 10).until(
    #         EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[3]/div[2]/div[2]/span/div/div/div/div[2]/div/div[1]/div[3]/div/div[2]/div[1]/div/p/span'))
    #     )
    #     message_box.click()
    #     message_box.send_keys(file_name)
    #     message_box.send_keys(Keys.ENTER)
    # except Exception as e:
    #     print(f"Error: {e}")

    # Click the send button
    send_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div[2]/div[2]/span/div/div/div/div[2]/div/div[2]/div[2]/div/div/span')
    send_button.click()



def replace_spaces_in_paths(directory):
    file_paths = []

    for root, dirs, files in os.walk(directory, topdown=False):
        for file in files:
            old_file_path = os.path.join(root, file)
            new_file_name = old_file_path.replace(directory + os.sep, '').replace(os.sep, '_').replace(' ', '_')
            new_file_path = os.path.join(directory, new_file_name)

            if old_file_path != new_file_path:
                shutil.move(old_file_path, new_file_path)

            file_paths.append(new_file_path)

    return file_paths






# Example usage
if __name__ == "__main__":
    # Set up Firefox options
    # firefox_options = Options()
    # firefox_options.add_argument("--user-data-dir=firefox-data")  # Keep user data to stay logged in

    # # Set up the WebDriver
    # service = Service('./geckodriver.exe')  # Update with the path to your geckodriver
    # driver = webdriver.Firefox(service=service, options=firefox_options)

    # # Open WhatsApp Web
    # driver.get('https://web.whatsapp.com')

    # # Wait for the user to scan the QR code
    # print("Please scan the QR code to log in.")
    # input("Waiting for a key press : [c]")

    # # Search for the contact "Pappa"
    # search_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
    # search_box.click()
    # time.sleep(2)  # Wait for the search box to be ready

    # # Send keys one by one with a slight delay
    # for char in 'Sai Sardesai':
    #     search_box.send_keys(char)
    #     time.sleep(0.2)  # Adjust the delay as needed

    # search_box.send_keys(Keys.ENTER)

    # # Wait for the contact to open
    # time.sleep(2)

    # Upload multiple files

    # Example usage
    directory = './D'
    file_paths = replace_spaces_in_paths(directory)


    # for old_path in file_paths:
    #     upload_file_to_whatsapp(driver, old_path)
    #     time.sleep(1)
    # Close the browser
    # time.sleep(2)
    # driver.quit()