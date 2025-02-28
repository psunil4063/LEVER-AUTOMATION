

# Here Both radio buttons are working good

# import csv
# import undetected_chromedriver as uc
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.chrome.options import Options
# import time
# import os
# import yaml
# import random
# from datetime import datetime
# from fake_useragent import UserAgent
# from anticaptchaofficial.recaptchav2proxyless import recaptchaV2Proxyless

# # Load credentials, resume path, and required questions from config.yaml
# with open("credentials/sunil.yaml", "r") as file:
#     config = yaml.safe_load(file)

# credentials = config["credentials"]
# resume_path = os.path.abspath(config["resume_path"])

# # Read answers from CSV
# answers = {}
# try:
#     with open("qa/answers.csv", mode="r") as file:
#         reader = csv.DictReader(file)
#         for row in reader:
#             answers[row["Question"]] = row["Answer"]
#             print(f"Read question: {row['Question']} with answer: {row['Answer']}")
# except FileNotFoundError:
#     print("Error: 'answers.csv' file not found. Please ensure the file exists in the correct directory.")
#     exit()

# # Set up Chrome options with a random user agent
# ua = UserAgent()
# chrome_options = Options()
# chrome_options.add_argument(f"user-agent={ua.random}")
# chrome_options.add_argument("--disable-blink-features=AutomationControlled")  # Prevent bot detection

# # Use undetected ChromeDriver
# driver = uc.Chrome(options=chrome_options)

# # File to save application data
# applications_file = "applications.csv"

# # Create applications file with headers if not present
# if not os.path.exists(applications_file):
#     with open(applications_file, mode="w", newline="") as file:
#         writer = csv.writer(file)
#         writer.writerow(["Company", "Job Title", "Application Link", "Date Applied", "Status", "Questions Answered"])

# # Read job links from the text file
# with open("job_links.txt", "r") as file:
#     job_links = file.read().splitlines()

# if not job_links:
#     print("No job links available. End of the links.")
# else:
#     for job_link in job_links:
#         retry_count = 0
#         max_retries = 3

#         while retry_count < max_retries:
#             try:
#                 print(f"Processing job link: {job_link}")

#                 # Open job link with human-like delay
#                 driver.get(job_link)
#                 time.sleep(random.uniform(5, 10))

#                 # Handle "Apply for this job" button (if present)
#                 try:
#                     apply_button = WebDriverWait(driver, 5).until(
#                         EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Apply for this job') or contains(text(), 'Apply Now')]"))
#                     )
#                     apply_button.click()
#                     print("Clicked 'Apply for this job' button.")
#                     time.sleep(random.uniform(3, 4))  # Wait for the form to load
#                 except Exception as e:
#                     print(f"No 'Apply for this job' button found. Proceeding to the form. Error: {e}")

#                 # Extract company name
#                 try:
#                     company_name = driver.find_element(By.CSS_SELECTOR, "a.main-header-logo img").get_attribute("alt")
#                     company_name = company_name.replace(" logo", "")
#                 except:
#                     company_name = "Unknown Company"

#                 # Extract job title
#                 try:
#                     job_title = driver.find_element(By.CSS_SELECTOR, "div.section.page-centered.posting-header h2").text.strip()
#                 except:
#                     job_title = "Unknown Job Title"

#                 # Fill out form
#                 WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "name"))).send_keys(credentials["name"])
#                 time.sleep(random.uniform(2, 5))

#                 WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "email"))).send_keys(credentials["email"])
#                 time.sleep(random.uniform(2, 5))

#                 WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.NAME, "phone"))).send_keys(credentials["phone"])
#                 time.sleep(random.uniform(2, 5))

#                 # Upload resume
#                 print(f"Uploading resume from: {resume_path}")
#                 file_input = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.NAME, "resume")))
#                 file_input.send_keys(resume_path)
#                 time.sleep(random.uniform(2, 5))

#                 # Fill LinkedIn profile (if exists)
#                 try:
#                     linkedin_field = WebDriverWait(driver, 5).until(
#                         EC.presence_of_element_located((By.NAME, "urls[LinkedIn]"))
#                     )
#                     driver.execute_script("arguments[0].scrollIntoView();", linkedin_field)
#                     linkedin_field.clear()
#                     linkedin_field.send_keys(credentials["linkedin_url"])
#                     print("LinkedIn profile filled successfully.")
#                     time.sleep(random.uniform(2, 3))
#                 except Exception as e:
#                     print(f"LinkedIn field not found or could not be filled. Error: {e}")

#                 # Handle required questions
#                 questions_answered = {}

#                 for question, answer in answers.items():
#                     try:
#                         print(f"Attempting to answer: {question} with {answer}")
                        
#                         # Find the question label using the question text
#                         question_label = WebDriverWait(driver, 10).until(
#                             EC.presence_of_element_located((By.XPATH, f"//div[contains(@class, 'application-label')]//div[contains(@class, 'text') and contains(text(), '{question}')]"))
#                         )
                        
#                         # Print the HTML of the question label for debugging
#                         print("Question Label HTML:", question_label.get_attribute("outerHTML"))


#                         question_parent = question_label.find_element(By.XPATH, "./ancestor::li[contains(@class, 'application-question')]")
#                         # Find all radio buttons for the question
#                         radio_buttons = driver.find_elements(By.XPATH, f"//div[contains(@class, 'application-label')]//div[contains(@class, 'text') and contains(text(), '{question}')]//following::ul[@data-qa='multiple-choice']//input[@type='radio']")
                        
#                         # Print the number of radio buttons found
#                         print(f"Found {len(radio_buttons)} radio buttons for question: {question}")
#                         selected =False
#                         # Loop through the radio buttons and click the one with the matching value
#                         for radio_button in radio_buttons:
#                             radio_value=radio_button.get_attribute("value")
#                             print(f"Radio Button Value: {radio_value}")
#                             if radio_value.lower() == answer.lower():
#                                 # Scroll the radio button into view (if needed)
#                                 driver.execute_script("arguments[0].scrollIntoView();", radio_button)
                                
#                                 # Wait for the radio button to be clickable
#                                 WebDriverWait(driver, 10).until(EC.element_to_be_clickable(radio_button))
                                
#                                 # Click the radio button using JavaScript (to avoid interception issues)
#                                 driver.execute_script("arguments[0].click();", radio_button)
                                
#                                 # Verify if the radio button is selected
#                                 if radio_button.is_selected():
#                                     print(f"Selected '{answer}' for question: {question}")
#                                     questions_answered[question] = answer
#                                     selected =True
#                                 else:
#                                     print(f"Failed to select '{answer}' for question: {question}")
#                                     questions_answered[question] = "Not Answered"
#                                 break

#                             if not selected:
#                                 print(f"NO matching radio button found for answer: {answer}")
#                                 questions_answered[question]="Not Answered"
                                
#                                   # Exit the loop once the desired radio button is clicked
                        
#                         time.sleep(random.uniform(2, 3))  # Random delay to mimic human behavior
#                     except Exception as e:
#                         print(f"Could not answer question: {question}. Error: {e}")
#                         questions_answered[question] = "Not Answered"

#                 # Handle CAPTCHA
#                 try:
#                     recaptcha_frame = WebDriverWait(driver, 10).until(
#                         EC.presence_of_element_located((By.XPATH, "//iframe[contains(@src, 'recaptcha')]"))
#                     )
#                     driver.switch_to.frame(recaptcha_frame)

#                     site_key = driver.find_element(By.CLASS_NAME, "g-recaptcha").get_attribute("data-sitekey")
#                     driver.switch_to.default_content()

#                     print("Solving CAPTCHA using 2Captcha...")

#                     solver = recaptchaV2Proxyless()
#                     solver.set_verbose(1)
#                     solver.set_key("YOUR_2CAPTCHA_API_KEY")  # Replace with your API key
#                     solver.set_website_url(job_link)
#                     solver.set_website_key(site_key)

#                     captcha_solution = solver.solve_and_return_solution()
#                     if captcha_solution:
#                         driver.execute_script(f'document.getElementById("g-recaptcha-response").innerHTML="{captcha_solution}"')
#                         time.sleep(3)
#                         print("CAPTCHA solved successfully!")
#                     else:
#                         print("Failed to solve CAPTCHA.")
#                         raise Exception("CAPTCHA Failed")
#                 except Exception as e:
#                     print("No CAPTCHA found or failed to solve:", e)

#                 # Simulate human-like mouse movement
#                 actions = ActionChains(driver)
#                 actions.move_by_offset(random.randint(5, 50), random.randint(5, 50)).perform()
#                 time.sleep(random.uniform(2, 5))

#                 # Submit the form
#                 submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "btn-submit")))
#                 submit_button.click()

#                 # Wait for success confirmation
#                 try:
#                     WebDriverWait(driver, 10).until(
#                         EC.any_of(
#                             EC.url_contains("success"),
#                             EC.presence_of_element_located((By.CSS_SELECTOR, "div.success-message"))
#                         )
#                     )
#                     print("Application submitted successfully!")
#                     status = "Success"
#                 except:
#                     status = "Failed"

#                 # Save to CSV
#                 with open(applications_file, mode="a", newline="") as file:
#                     writer = csv.writer(file)
#                     writer.writerow([company_name, job_title, job_link, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), status, questions_answered])

#                 time.sleep(random.uniform(5, 10))  # Delay before next application
#                 break  # Exit retry loop if successful

#             except Exception as e:
#                 print(f"Error for {job_link}: {e}")
#                 retry_count += 1
#                 if retry_count < max_retries:
#                     print(f"Retrying... ({retry_count}/{max_retries})")
#                     time.sleep(random.uniform(10, 20))
#                 else:
#                     print("Failed after multiple attempts.")
#                     with open(applications_file, mode="a", newline="") as file:
#                         writer = csv.writer(file)
#                         writer.writerow([company_name, job_title, job_link, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "Failed", questions_answered])

#     print("All job links processed.")

# # Close browser
# driver.quit()





# This code is working very very good 

# import csv
# import undetected_chromedriver as uc
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.chrome.options import Options
# import time
# import os
# import yaml
# import random
# from datetime import datetime
# from fake_useragent import UserAgent
# from anticaptchaofficial.recaptchav2proxyless import recaptchaV2Proxyless

# # Load credentials, resume path, and required questions from config.yaml
# with open("credentials/sunil.yaml", "r") as file:
#     config = yaml.safe_load(file)

# credentials = config["credentials"]
# resume_path = os.path.abspath(config["resume_path"])

# # Read answers from CSV
# answers = {}
# try:
#     with open("qa/answers.csv", mode="r") as file:
#         reader = csv.DictReader(file)
#         for row in reader:
#             answers[row["Question"]] = row["Answer"]
#             print(f"Read question: {row['Question']} with answer: {row['Answer']}")
# except FileNotFoundError:
#     print("Error: 'answers.csv' file not found. Please ensure the file exists in the correct directory.")
#     exit()

# # Set up Chrome options with a random user agent
# ua = UserAgent()
# chrome_options = Options()
# chrome_options.add_argument(f"user-agent={ua.random}")
# chrome_options.add_argument("--disable-blink-features=AutomationControlled")  # Prevent bot detection

# # Use undetected ChromeDriver
# driver = uc.Chrome(options=chrome_options)

# # File to save application data
# applications_file = "applications.csv"

# # Create applications file with headers if not present
# if not os.path.exists(applications_file):
#     with open(applications_file, mode="w", newline="") as file:
#         writer = csv.writer(file)
#         writer.writerow(["Company", "Job Title", "Application Link", "Date Applied", "Status", "Questions Answered"])

# # Read job links from the text file
# with open("job_links.txt", "r") as file:
#     job_links = file.read().splitlines()

# if not job_links:
#     print("No job links available. End of the links.")
# else:
#     for job_link in job_links:
#         retry_count = 0
#         max_retries = 3

#         while retry_count < max_retries:
#             try:
#                 print(f"Processing job link: {job_link}")

#                 # Open job link with human-like delay
#                 driver.get(job_link)
#                 time.sleep(random.uniform(5, 10))

#                 # Handle "Apply for this job" button (if present)
#                 try:
#                     apply_button = WebDriverWait(driver, 5).until(
#                         EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Apply for this job') or contains(text(), 'Apply Now')]"))
#                     )
#                     apply_button.click()
#                     print("Clicked 'Apply for this job' button.")
#                     time.sleep(random.uniform(3, 4))  # Wait for the form to load
#                 except Exception as e:
#                     print(f"No 'Apply for this job' button found. Proceeding to the form. Error: {e}")

#                 # Extract company name
#                 try:
#                     company_name = driver.find_element(By.CSS_SELECTOR, "a.main-header-logo img").get_attribute("alt")
#                     company_name = company_name.replace(" logo", "")
#                 except:
#                     company_name = "Unknown Company"

#                 # Extract job title
#                 try:
#                     job_title = driver.find_element(By.CSS_SELECTOR, "div.section.page-centered.posting-header h2").text.strip()
#                 except:
#                     job_title = "Unknown Job Title"

#                 # Fill out form
#                 WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "name"))).send_keys(credentials["name"])
#                 time.sleep(random.uniform(2, 5))

#                 WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "email"))).send_keys(credentials["email"])
#                 time.sleep(random.uniform(2, 5))

#                 WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.NAME, "phone"))).send_keys(credentials["phone"])
#                 time.sleep(random.uniform(2, 5))

#                 # Upload resume
#                 print(f"Uploading resume from: {resume_path}")
#                 file_input = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.NAME, "resume")))
#                 file_input.send_keys(resume_path)
#                 time.sleep(random.uniform(2, 5))

#                 # Fill LinkedIn profile (if exists)
#                 try:
#                     linkedin_field = WebDriverWait(driver, 5).until(
#                         EC.presence_of_element_located((By.NAME, "urls[LinkedIn]"))
#                     )
#                     driver.execute_script("arguments[0].scrollIntoView();", linkedin_field)
#                     linkedin_field.clear()
#                     linkedin_field.send_keys(credentials["linkedin_url"])
#                     print("LinkedIn profile filled successfully.")
#                     time.sleep(random.uniform(2, 3))
#                 except Exception as e:
#                     print(f"LinkedIn field not found or could not be filled. Error: {e}")

#                 # Handle required questions
#                 questions_answered = {}

#                 for question, answer in answers.items():
#                     try:
#                         print(f"Attempting to answer: {question} with {answer}")
                        
#                         # Find the question label using the question text
#                         question_label = WebDriverWait(driver, 10).until(
#                             EC.presence_of_element_located((By.XPATH, f"//div[contains(@class, 'application-label')]//div[contains(@class, 'text') and contains(text(), '{question}')]"))
#                         )
                        
#                         # Print the HTML of the question label for debugging
#                         print("Question Label HTML:", question_label.get_attribute("outerHTML"))
                        
#                         # Find the parent element of the question (the <li> containing the question and input field)
#                         question_parent = question_label.find_element(By.XPATH, "./ancestor::li[contains(@class, 'application-question')]")
                        
#                         # Check if the question is a text-based input field
#                         try:
#                             # Look for a textarea or input field
#                             text_input = question_parent.find_element(By.XPATH, ".//textarea | .//input[@type='text']")
                            
#                             # Scroll the input field into view (if needed)
#                             driver.execute_script("arguments[0].scrollIntoView();", text_input)
                            
#                             # Clear the input field (if necessary)
#                             text_input.clear()
                            
#                             # Enter the answer into the text field
#                             text_input.send_keys(answer)
                            
#                             print(f"Entered '{answer}' for question: {question}")
#                             questions_answered[question] = answer
#                         except:
#                             # If no text input is found, assume it's a radio button question
#                             print("No text input found. Assuming it's a radio button question.")
                            
#                             # Find all radio buttons under the question parent
#                             radio_buttons = question_parent.find_elements(By.XPATH, ".//input[@type='radio']")
                            
#                             # Print the number of radio buttons found
#                             print(f"Found {len(radio_buttons)} radio buttons for question: {question}")
                            
#                             # Flag to track if the correct radio button was selected
#                             selected = False
                            
#                             # Loop through the radio buttons and click the one with the matching value
#                             for radio_button in radio_buttons:
#                                 radio_value = radio_button.get_attribute("value")
#                                 print(f"Radio Button Value: {radio_value}")
                                
#                                 if radio_value.lower() == answer.lower():  # Case-insensitive comparison
#                                     # Scroll the radio button into view (if needed)
#                                     driver.execute_script("arguments[0].scrollIntoView();", radio_button)
                                    
#                                     # Wait for the radio button to be clickable
#                                     WebDriverWait(driver, 10).until(EC.element_to_be_clickable(radio_button))
                                    
#                                     # Click the radio button using JavaScript (to avoid interception issues)
#                                     driver.execute_script("arguments[0].click();", radio_button)
                                    
#                                     # Verify if the radio button is selected
#                                     if radio_button.is_selected():
#                                         print(f"Selected '{answer}' for question: {question}")
#                                         questions_answered[question] = answer
#                                         selected = True
#                                     else:
#                                         print(f"Failed to select '{answer}' for question: {question}")
#                                         questions_answered[question] = "Not Answered"
                                    
#                                     break  # Exit the loop for this question after selecting the correct radio button
                            
#                             if not selected:
#                                 print(f"No matching radio button found for answer: {answer}")
#                                 questions_answered[question] = "Not Answered"
                        
#                         time.sleep(random.uniform(2, 3))  # Random delay to mimic human behavior
#                     except Exception as e:
#                         print(f"Could not answer question: {question}. Error: {e}")
#                         questions_answered[question] = "Not Answered"

#                 # Handle CAPTCHA
#                 try:
#                     recaptcha_frame = WebDriverWait(driver, 10).until(
#                         EC.presence_of_element_located((By.XPATH, "//iframe[contains(@src, 'recaptcha')]"))
#                     )
#                     driver.switch_to.frame(recaptcha_frame)

#                     site_key = driver.find_element(By.CLASS_NAME, "g-recaptcha").get_attribute("data-sitekey")
#                     driver.switch_to.default_content()

#                     print("Solving CAPTCHA using 2Captcha...")

#                     solver = recaptchaV2Proxyless()
#                     solver.set_verbose(1)
#                     solver.set_key("YOUR_2CAPTCHA_API_KEY")  # Replace with your API key
#                     solver.set_website_url(job_link)
#                     solver.set_website_key(site_key)

#                     captcha_solution = solver.solve_and_return_solution()
#                     if captcha_solution:
#                         driver.execute_script(f'document.getElementById("g-recaptcha-response").innerHTML="{captcha_solution}"')
#                         time.sleep(3)
#                         print("CAPTCHA solved successfully!")
#                     else:
#                         print("Failed to solve CAPTCHA.")
#                         raise Exception("CAPTCHA Failed")
#                 except Exception as e:
#                     print("No CAPTCHA found or failed to solve:", e)

#                 # Simulate human-like mouse movement
#                 actions = ActionChains(driver)
#                 actions.move_by_offset(random.randint(5, 50), random.randint(5, 50)).perform()
#                 time.sleep(random.uniform(2, 5))

#                 # Submit the form
#                 submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "btn-submit")))
#                 submit_button.click()

#                 # Wait for success confirmation
#                 try:
#                     WebDriverWait(driver, 10).until(
#                         EC.any_of(
#                             EC.url_contains("success"),
#                             EC.presence_of_element_located((By.CSS_SELECTOR, "div.success-message"))
#                         )
#                     )
#                     print("Application submitted successfully!")
#                     status = "Success"
#                 except:
#                     status = "Failed"

#                 # Save to CSV
#                 with open(applications_file, mode="a", newline="") as file:
#                     writer = csv.writer(file)
#                     writer.writerow([company_name, job_title, job_link, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), status, questions_answered])

#                 time.sleep(random.uniform(5, 10))  # Delay before next application
#                 break  # Exit retry loop if successful

#             except Exception as e:
#                 print(f"Error for {job_link}: {e}")
#                 retry_count += 1
#                 if retry_count < max_retries:
#                     print(f"Retrying... ({retry_count}/{max_retries})")
#                     time.sleep(random.uniform(10, 20))
#                 else:
#                     print("Failed after multiple attempts.")
#                     with open(applications_file, mode="a", newline="") as file:
#                         writer = csv.writer(file)
#                         writer.writerow([company_name, job_title, job_link, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "Failed", questions_answered])

#     print("All job links processed.")

# # Close browser
# driver.quit()




# import csv
# import undetected_chromedriver as uc
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.chrome.options import Options
# import time
# import os
# import yaml
# import random
# from datetime import datetime
# from fake_useragent import UserAgent
# from anticaptchaofficial.recaptchav2proxyless import recaptchaV2Proxyless

# # Load credentials and required questions from config.yaml
# with open("credentials/sunil.yaml", "r") as file:
#     config = yaml.safe_load(file)

# credentials = config["credentials"]

# # Read answers from CSV
# answers = {}
# try:
#     with open("qa/answers.csv", mode="r") as file:
#         reader = csv.DictReader(file)
#         for row in reader:
#             answers[row["Question"]] = row["Answer"]
#             print(f"Read question: {row['Question']} with answer: {row['Answer']}")
# except FileNotFoundError:
#     print("Error: 'answers.csv' file not found. Please ensure the file exists in the correct directory.")
#     exit()

# # Set up Chrome options with a random user agent
# ua = UserAgent()
# chrome_options = Options()
# chrome_options.add_argument(f"user-agent={ua.random}")
# chrome_options.add_argument("--disable-blink-features=AutomationControlled")  # Prevent bot detection

# # Use undetected ChromeDriver
# driver = uc.Chrome(options=chrome_options)

# # File to save application data
# applications_file = "applications.csv"

# # Create applications file with headers if not present
# if not os.path.exists(applications_file):
#     with open(applications_file, mode="w", newline="") as file:
#         writer = csv.writer(file)
#         writer.writerow(["Company", "Job Title", "Application Link", "Date Applied", "Status", "Questions Answered"])

# # Read job links from the text file
# with open("job_links.txt", "r") as file:
#     job_links = file.read().splitlines()

# if not job_links:
#     print("No job links available. End of the links.")
# else:
#     for job_link in job_links:
#         retry_count = 0
#         max_retries = 3

#         while retry_count < max_retries:
#             try:
#                 print(f"Processing job link: {job_link}")

#                 # Open job link with human-like delay
#                 driver.get(job_link)
#                 time.sleep(random.uniform(5, 10))

#                 # Handle "Apply for this job" button (if present)
#                 try:
#                     apply_button = WebDriverWait(driver, 5).until(
#                         EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Apply for this job') or contains(text(), 'Apply Now')]"))
#                     )
#                     apply_button.click()
#                     print("Clicked 'Apply for this job' button.")
#                     time.sleep(random.uniform(3, 4))  # Wait for the form to load
#                 except Exception as e:
#                     print(f"No 'Apply for this job' button found. Proceeding to the form. Error: {e}")

#                 # Extract company name
#                 try:
#                     company_name = driver.find_element(By.CSS_SELECTOR, "a.main-header-logo img").get_attribute("alt")
#                     company_name = company_name.replace(" logo", "")
#                 except:
#                     company_name = "Unknown Company"

#                 # Extract job title
#                 try:
#                     job_title = driver.find_element(By.CSS_SELECTOR, "div.section.page-centered.posting-header h2").text.strip()
#                 except:
#                     job_title = "Unknown Job Title"

#                 # Fill out form using YAML credentials
#                 WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "name"))).send_keys(credentials["name"])
#                 time.sleep(random.uniform(2, 5))

#                 WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "email"))).send_keys(credentials["email"])
#                 time.sleep(random.uniform(2, 5))

#                 WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.NAME, "phone"))).send_keys(credentials["phone"])
#                 time.sleep(random.uniform(2, 5))

#                 # Fill LinkedIn profile (if exists)
#                 try:
#                     linkedin_field = WebDriverWait(driver, 5).until(
#                         EC.presence_of_element_located((By.NAME, "urls[LinkedIn]"))
#                     )
#                     driver.execute_script("arguments[0].scrollIntoView();", linkedin_field)
#                     linkedin_field.clear()
#                     linkedin_field.send_keys(credentials["linkedin_url"])
#                     print("LinkedIn profile filled successfully.")
#                     time.sleep(random.uniform(2, 3))
#                 except Exception as e:
#                     print(f"LinkedIn field not found or could not be filled. Error: {e}")

#                 # Handle required questions
#                 questions_answered = {}

#                 for question, answer in answers.items():
#                     try:
#                         print(f"Attempting to answer: {question} with {answer}")
                        
#                         # Find the question label using the question text
#                         question_label = WebDriverWait(driver, 10).until(
#                             EC.presence_of_element_located((By.XPATH, f"//div[contains(@class, 'application-label')]//div[contains(@class, 'text') and contains(text(), '{question}')]"))
#                         )
                        
#                         # Print the HTML of the question label for debugging
#                         print("Question Label HTML:", question_label.get_attribute("outerHTML"))
                        
#                         # Find the parent element of the question (the <li> containing the question and input field)
#                         question_parent = question_label.find_element(By.XPATH, "./ancestor::li[contains(@class, 'application-question')]")
                        
#                         # Check if the question is a checkbox
#                         try:
#                             checkbox = question_parent.find_element(By.XPATH, ".//input[@type='checkbox']")
                            
#                             # Scroll the checkbox into view (if needed)
#                             driver.execute_script("arguments[0].scrollIntoView();", checkbox)
                            
#                             # Check the checkbox if the answer is "Yes" or "I acknowledge"
#                             if answer.lower() in ["yes", "i acknowledge"]:
#                                 if not checkbox.is_selected():
#                                     checkbox.click()
#                                 print(f"Checked '{answer}' for question: {question}")
#                                 questions_answered[question] = answer
#                             else:
#                                 print(f"Checkbox not selected for question: {question}")
#                                 questions_answered[question] = "Not Answered"
#                         except:
#                             # If no checkbox is found, assume it's a text-based or radio button question
#                             print("No checkbox found. Assuming it's a text-based or radio button question.")
                            
#                             # Handle text-based or radio button questions
#                             try:
#                                 # Look for a textarea or input field
#                                 text_input = question_parent.find_element(By.XPATH, ".//textarea | .//input[@type='text']")
                                
#                                 # Scroll the input field into view (if needed)
#                                 driver.execute_script("arguments[0].scrollIntoView();", text_input)
                                
#                                 # Clear the input field (if necessary)
#                                 text_input.clear()
                                
#                                 # Enter the answer into the text field
#                                 text_input.send_keys(answer)
                                
#                                 print(f"Entered '{answer}' for question: {question}")
#                                 questions_answered[question] = answer
#                             except:
#                                 # If no text input is found, assume it's a radio button question
#                                 print("No text input found. Assuming it's a radio button question.")
                                
#                                 # Find all radio buttons under the question parent
#                                 radio_buttons = question_parent.find_elements(By.XPATH, ".//input[@type='radio']")
                                
#                                 # Print the number of radio buttons found
#                                 print(f"Found {len(radio_buttons)} radio buttons for question: {question}")
                                
#                                 # Flag to track if the correct radio button was selected
#                                 selected = False
                                
#                                 # Loop through the radio buttons and click the one with the matching value
#                                 for radio_button in radio_buttons:
#                                     radio_value = radio_button.get_attribute("value")
#                                     print(f"Radio Button Value: {radio_value}")
                                    
#                                     if radio_value.lower() == answer.lower():  # Case-insensitive comparison
#                                         # Scroll the radio button into view (if needed)
#                                         driver.execute_script("arguments[0].scrollIntoView();", radio_button)
                                        
#                                         # Wait for the radio button to be clickable
#                                         WebDriverWait(driver, 10).until(EC.element_to_be_clickable(radio_button))
                                        
#                                         # Click the radio button using JavaScript (to avoid interception issues)
#                                         driver.execute_script("arguments[0].click();", radio_button)
                                        
#                                         # Verify if the radio button is selected
#                                         if radio_button.is_selected():
#                                             print(f"Selected '{answer}' for question: {question}")
#                                             questions_answered[question] = answer
#                                             selected = True
#                                         else:
#                                             print(f"Failed to select '{answer}' for question: {question}")
#                                             questions_answered[question] = "Not Answered"
                                        
#                                         break  # Exit the loop for this question after selecting the correct radio button
                                
#                                 if not selected:
#                                     print(f"No matching radio button found for answer: {answer}")
#                                     questions_answered[question] = "Not Answered"
                        
#                         time.sleep(random.uniform(2, 3))  # Random delay to mimic human behavior
#                     except Exception as e:
#                         print(f"Could not answer question: {question}. Error: {e}")
#                         questions_answered[question] = "Not Answered"

#                 # Handle CAPTCHA
#                 try:
#                     recaptcha_frame = WebDriverWait(driver, 10).until(
#                         EC.presence_of_element_located((By.XPATH, "//iframe[contains(@src, 'recaptcha')]"))
#                     )
#                     driver.switch_to.frame(recaptcha_frame)

#                     site_key = driver.find_element(By.CLASS_NAME, "g-recaptcha").get_attribute("data-sitekey")
#                     driver.switch_to.default_content()

#                     print("Solving CAPTCHA using 2Captcha...")

#                     solver = recaptchaV2Proxyless()
#                     solver.set_verbose(1)
#                     solver.set_key("YOUR_2CAPTCHA_API_KEY")  # Replace with your API key
#                     solver.set_website_url(job_link)
#                     solver.set_website_key(site_key)

#                     captcha_solution = solver.solve_and_return_solution()
#                     if captcha_solution:
#                         driver.execute_script(f'document.getElementById("g-recaptcha-response").innerHTML="{captcha_solution}"')
#                         time.sleep(3)
#                         print("CAPTCHA solved successfully!")
#                     else:
#                         print("Failed to solve CAPTCHA.")
#                         raise Exception("CAPTCHA Failed")
#                 except Exception as e:
#                     print("No CAPTCHA found or failed to solve:", e)

#                 # Simulate human-like mouse movement
#                 actions = ActionChains(driver)
#                 actions.move_by_offset(random.randint(5, 50), random.randint(5, 50)).perform()
#                 time.sleep(random.uniform(2, 5))

#                 # Submit the form
#                 submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "btn-submit")))
#                 submit_button.click()

#                 # Wait for success confirmation
#                 try:
#                     WebDriverWait(driver, 10).until(
#                         EC.any_of(
#                             EC.url_contains("success"),
#                             EC.presence_of_element_located((By.CSS_SELECTOR, "div.success-message"))
#                         )
#                     )
#                     print("Application submitted successfully!")
#                     status = "Success"
#                 except:
#                     status = "Failed"

#                 # Save to CSV
#                 with open(applications_file, mode="a", newline="") as file:
#                     writer = csv.writer(file)
#                     writer.writerow([company_name, job_title, job_link, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), status, questions_answered])

#                 time.sleep(random.uniform(5, 10))  # Delay before next application
#                 break  # Exit retry loop if successful

#             except Exception as e:
#                 print(f"Error for {job_link}: {e}")
#                 retry_count += 1
#                 if retry_count < max_retries:
#                     print(f"Retrying... ({retry_count}/{max_retries})")
#                     time.sleep(random.uniform(10, 20))
#                 else:
#                     print("Failed after multiple attempts.")
#                     with open(applications_file, mode="a", newline="") as file:
#                         writer = csv.writer(file)
#                         writer.writerow([company_name, job_title, job_link, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "Failed", questions_answered])

#     print("All job links processed.")

# # Close browser
# driver.quit()





# import csv
# import undetected_chromedriver as uc
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.chrome.options import Options
# import time
# import os
# import yaml
# import random
# from datetime import datetime
# from fake_useragent import UserAgent
# from anticaptchaofficial.recaptchav2proxyless import recaptchaV2Proxyless
# from selenium.common.exceptions import InvalidSessionIdException, TimeoutException, NoSuchElementException, WebDriverException
# from urllib3.exceptions import MaxRetryError, NewConnectionError

# # Load credentials and required questions from config.yaml
# with open("config/credentials.yaml", "r") as file:
#     config = yaml.safe_load(file)

# credentials = config["credentials"]
# resume_path = os.path.abspath(config["resume_path"])

# # Read answers from CSV
# answers = {}
# try:
#     with open("config/answers.csv", mode="r") as file:
#         reader = csv.DictReader(file)
#         for row in reader:
#             answers[row["Question"]] = row["Answer"]
#             print(f"Read question: {row['Question']} with answer: {row['Answer']}")
# except FileNotFoundError:
#     print("Error: 'answers.csv' file not found. Please ensure the file exists in the correct directory.")
#     exit()

# # File to save application data
# applications_file = "applications.csv"

# # Create applications file with headers if not present
# if not os.path.exists(applications_file):
#     with open(applications_file, mode="w", newline="") as file:
#         writer = csv.writer(file)
#         writer.writerow(["Company", "Job Title", "Application Link", "Date Applied", "Status", "Questions Answered"])

# # Read job links from the text file
# with open("data/job_links.txt", "r") as file:
#     job_links = file.read().splitlines()

# if not job_links:
#     print("No job links available. End of the links.")
# else:
#     for job_link in job_links:
#         retry_count = 0
#         max_retries = 3

#         while retry_count < max_retries:
#             try:
#                 # Set up Chrome options with a random user agent
#                 ua = UserAgent()
#                 chrome_options = Options()
#                 chrome_options.add_argument(f"user-agent={ua.random}")
#                 chrome_options.add_argument("--disable-blink-features=AutomationControlled")  # Prevent bot detection

#                 # Use undetected ChromeDriver
#                 driver = uc.Chrome(options=chrome_options)

#                 print(f"Processing job link: {job_link}")

#                 # Open job link with human-like delay
#                 driver.get(job_link)
#                 time.sleep(random.uniform(5, 10))

#                 # Handle "Apply for this job" button (if present)
#                 try:
#                     apply_button = WebDriverWait(driver, 10).until(
#                         EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Apply for this job') or contains(text(), 'Apply Now')]"))
#                     )
#                     apply_button.click()
#                     print("Clicked 'Apply for this job' button.")
#                     time.sleep(random.uniform(3, 4))  # Wait for the form to load
#                 except Exception as e:
#                     print(f"No 'Apply for this job' button found. Proceeding to the form. Error: {e}")

#                 # Extract company name
#                 try:
#                     company_name = WebDriverWait(driver, 10).until(
#                         EC.presence_of_element_located((By.CSS_SELECTOR, "a.main-header-logo img"))
#                     ).get_attribute("alt")
#                     company_name = company_name.replace(" logo", "")
#                 except:
#                     company_name = "Unknown Company"

#                 # Extract job title
#                 try:
#                     job_title = WebDriverWait(driver, 10).until(
#                         EC.presence_of_element_located((By.CSS_SELECTOR, "div.section.page-centered.posting-header h2"))
#                     ).text.strip()
#                 except:
#                     job_title = "Unknown Job Title"

#                 # Initialize questions_answered dictionary
#                 questions_answered = {}

#                 # Fill out form using YAML credentials
#                 try:
#                     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "name"))).send_keys(credentials["name"])
#                     time.sleep(random.uniform(2, 5))

#                     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "email"))).send_keys(credentials["email"])
#                     time.sleep(random.uniform(2, 5))

#                     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "phone"))).send_keys(credentials["phone"])
#                     time.sleep(random.uniform(2, 5))
#                 except InvalidSessionIdException:
#                     print("Browser session lost. Restarting the browser...")
#                     driver.quit()
#                     continue  # Retry the current job link

#                 # Upload resume (without analyzing details)
#                 print(f"Uploading resume from: {resume_path}")
#                 try:
#                     file_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "resume")))
#                     file_input.send_keys(resume_path)
#                     time.sleep(random.uniform(2, 5))
#                 except Exception as e:
#                     print(f"Failed to upload resume. Error: {e}")

#                 # Fill LinkedIn profile (if exists)
#                 try:
#                     linkedin_field = WebDriverWait(driver, 10).until(
#                         EC.presence_of_element_located((By.NAME, "urls[LinkedIn]"))
#                     )
#                     driver.execute_script("arguments[0].scrollIntoView();", linkedin_field)
#                     linkedin_field.clear()
#                     linkedin_field.send_keys(credentials["linkedin_url"])
#                     print("LinkedIn profile filled successfully.")
#                     time.sleep(random.uniform(2, 3))
#                 except Exception as e:
#                     print(f"LinkedIn field not found or could not be filled. Error: {e}")

#                 # Handle required questions
#                 for question, answer in answers.items():
#                     try:
#                         print(f"Attempting to answer: {question} with {answer}")
                        
#                         # Find the question label using the question text
#                         question_label = WebDriverWait(driver, 10).until(
#                             EC.presence_of_element_located((By.XPATH, f"//div[contains(@class, 'application-label')]//div[contains(@class, 'text') and contains(text(), '{question}')]"))
#                         )
                        
#                         # Print the HTML of the question label for debugging
#                         print("Question Label HTML:", question_label.get_attribute("outerHTML"))
                        
#                         # Find the parent element of the question (the <li> containing the question and input field)
#                         question_parent = question_label.find_element(By.XPATH, "./ancestor::li[contains(@class, 'application-question')]")
                        
#                         # Check if the question is a checkbox (acknowledgement)
#                         try:
#                             # Locate the checkbox associated with the question
#                             checkbox = question_parent.find_element(By.XPATH, ".//input[@type='checkbox']")
                            
#                             # Scroll the checkbox into view (if needed)
#                             driver.execute_script("arguments[0].scrollIntoView();", checkbox)
                            
#                             # Check the checkbox if the answer is "I acknowledge"
#                             if answer.lower() == "i acknowledge":
#                                 if not checkbox.is_selected():
#                                     checkbox.click()
#                                 print(f"Checked '{answer}' for question: {question}")
#                                 questions_answered[question] = answer
#                             else:
#                                 print(f"Checkbox not selected for question: {question}")
#                                 questions_answered[question] = "Not Answered"
#                         except:
#                             # If no checkbox is found, assume it's a text-based or radio button question
#                             print("No checkbox found. Assuming it's a text-based or radio button question.")
                            
#                             # Handle text-based or radio button questions
#                             try:
#                                 # Look for a textarea or input field
#                                 text_input = question_parent.find_element(By.XPATH, ".//textarea | .//input[@type='text']")
                                
#                                 # Scroll the input field into view (if needed)
#                                 driver.execute_script("arguments[0].scrollIntoView();", text_input)
                                
#                                 # Clear the input field (if necessary)
#                                 text_input.clear()
                                
#                                 # Enter the answer into the text field
#                                 text_input.send_keys(answer)
                                
#                                 print(f"Entered '{answer}' for question: {question}")
#                                 questions_answered[question] = answer
#                             except:
#                                 # If no text input is found, assume it's a radio button question
#                                 print("No text input found. Assuming it's a radio button question.")
                                
#                                 # Find all radio buttons under the question parent
#                                 radio_buttons = question_parent.find_elements(By.XPATH, ".//input[@type='radio']")
                                
#                                 # Print the number of radio buttons found
#                                 print(f"Found {len(radio_buttons)} radio buttons for question: {question}")
                                
#                                 # Flag to track if the correct radio button was selected
#                                 selected = False
                                
#                                 # Loop through the radio buttons and click the one with the matching value
#                                 for radio_button in radio_buttons:
#                                     radio_value = radio_button.get_attribute("value")
#                                     print(f"Radio Button Value: {radio_value}")
                                    
#                                     if radio_value.lower() == answer.lower():  # Case-insensitive comparison
#                                         # Scroll the radio button into view (if needed)
#                                         driver.execute_script("arguments[0].scrollIntoView();", radio_button)
                                        
#                                         # Wait for the radio button to be clickable
#                                         WebDriverWait(driver, 10).until(EC.element_to_be_clickable(radio_button))
                                        
#                                         # Click the radio button using JavaScript (to avoid interception issues)
#                                         driver.execute_script("arguments[0].click();", radio_button)
                                        
#                                         # Verify if the radio button is selected
#                                         if radio_button.is_selected():
#                                             print(f"Selected '{answer}' for question: {question}")
#                                             questions_answered[question] = answer
#                                             selected = True
#                                         else:
#                                             print(f"Failed to select '{answer}' for question: {question}")
#                                             questions_answered[question] = "Not Answered"
                                        
#                                         break  # Exit the loop for this question after selecting the correct radio button
                                
#                                 if not selected:
#                                     print(f"No matching radio button found for answer: {answer}")
#                                     questions_answered[question] = "Not Answered"
                        
#                         time.sleep(random.uniform(2, 3))  # Random delay to mimic human behavior
#                     except Exception as e:
#                         print(f"Could not answer question: {question}. Error: {e}")
#                         questions_answered[question] = "Not Answered"

#                 # Handle CAPTCHA
#                 try:
#                     recaptcha_frame = WebDriverWait(driver, 10).until(
#                         EC.presence_of_element_located((By.XPATH, "//iframe[contains(@src, 'recaptcha')]"))
#                     )
#                     driver.switch_to.frame(recaptcha_frame)

#                     site_key = driver.find_element(By.CLASS_NAME, "g-recaptcha").get_attribute("data-sitekey")
#                     driver.switch_to.default_content()

#                     print("Solving CAPTCHA using 2Captcha...")

#                     solver = recaptchaV2Proxyless()
#                     solver.set_verbose(1)
#                     solver.set_key("YOUR_2CAPTCHA_API_KEY")  # Replace with your API key
#                     solver.set_website_url(job_link)
#                     solver.set_website_key(site_key)

#                     captcha_solution = solver.solve_and_return_solution()
#                     if captcha_solution:
#                         driver.execute_script(f'document.getElementById("g-recaptcha-response").innerHTML="{captcha_solution}"')
#                         time.sleep(3)
#                         print("CAPTCHA solved successfully!")
#                     else:
#                         print("Failed to solve CAPTCHA.")
#                         raise Exception("CAPTCHA Failed")
#                 except Exception as e:
#                     print("No CAPTCHA found or failed to solve:", e)

#                 # Simulate human-like mouse movement
#                 actions = ActionChains(driver)
#                 actions.move_by_offset(random.randint(5, 50), random.randint(5, 50)).perform()
#                 time.sleep(random.uniform(2, 5))

#                 # Submit the form
#                 submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "btn-submit")))
#                 submit_button.click()

#                 # Wait for success confirmation
#                 try:
#                     WebDriverWait(driver, 10).until(
#                         EC.any_of(
#                             EC.url_contains("success"),
#                             EC.presence_of_element_located((By.CSS_SELECTOR, "div.success-message"))
#                         )
#                     )
#                     print("Application submitted successfully!")
#                     status = "Success"
#                 except:
#                     status = "Failed"

#                 # Save to CSV
#                 with open(applications_file, mode="a", newline="") as file:
#                     writer = csv.writer(file)
#                     writer.writerow([company_name, job_title, job_link, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), status, questions_answered])

#                 time.sleep(random.uniform(5, 10))  # Delay before next application
#                 break  # Exit retry loop if successful

#             except (InvalidSessionIdException, WebDriverException, MaxRetryError, NewConnectionError) as e:
#                 print(f"Browser session lost or connection error. Restarting the browser... Error: {e}")
#                 try:
#                     driver.quit()
#                 except:
#                     pass
#                 retry_count += 1
#                 if retry_count < max_retries:
#                     print(f"Retrying... ({retry_count}/{max_retries})")
#                     time.sleep(random.uniform(10, 20))
#                 else:
#                     print("Failed after multiple attempts.")
#                     with open(applications_file, mode="a", newline="") as file:
#                         writer = csv.writer(file)
#                         writer.writerow([company_name, job_title, job_link, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "Failed", questions_answered])
#             except Exception as e:
#                 print(f"Error for {job_link}: {e}")
#                 retry_count += 1
#                 if retry_count < max_retries:
#                     print(f"Retrying... ({retry_count}/{max_retries})")
#                     time.sleep(random.uniform(10, 20))
#                 else:
#                     print("Failed after multiple attempts.")
#                     with open(applications_file, mode="a", newline="") as file:
#                         writer = csv.writer(file)
#                         writer.writerow([company_name, job_title, job_link, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "Failed", questions_answered])

#     print("All job links processed.")

# # Close browser
# try:
#     driver.quit()
# except:
#     pass





# import csv
# import undetected_chromedriver as uc
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.chrome.options import Options
# import time
# import os
# import yaml
# import random
# from datetime import datetime
# from fake_useragent import UserAgent
# from anticaptchaofficial.recaptchav2proxyless import recaptchaV2Proxyless
# from selenium.common.exceptions import InvalidSessionIdException, TimeoutException, NoSuchElementException, WebDriverException
# from urllib3.exceptions import MaxRetryError, NewConnectionError

# # Load credentials and required questions from config.yaml
# with open("config/credentials.yaml", "r") as file:
#     config = yaml.safe_load(file)

# credentials = config["credentials"]
# resume_path = os.path.abspath(config["resume_path"])

# # Read answers from CSV
# answers = {}
# try:
#     with open("config/answers.csv", mode="r") as file:
#         reader = csv.DictReader(file)
#         for row in reader:
#             answers[row["Question"]] = row["Answer"]
#             print(f"Read question: {row['Question']} with answer: {row['Answer']}")
# except FileNotFoundError:
#     print("Error: 'answers.csv' file not found. Please ensure the file exists in the correct directory.")
#     exit()

# # File to save application data
# applications_file = "applications.csv"

# # Create applications file with headers if not present
# if not os.path.exists(applications_file):
#     with open(applications_file, mode="w", newline="") as file:
#         writer = csv.writer(file)
#         writer.writerow(["Company", "Job Title", "Application Link", "Date Applied", "Status", "Questions Answered"])

# # Read job links from the text file
# with open("data/job_links.txt", "r") as file:
#     job_links = file.read().splitlines()

# if not job_links:
#     print("No job links available. End of the links.")
# else:
#     for job_link in job_links:
#         retry_count = 0
#         max_retries = 3

#         while retry_count < max_retries:
#             try:
#                 # Set up Chrome options with a random user agent
#                 ua = UserAgent()
#                 chrome_options = Options()
#                 chrome_options.add_argument(f"user-agent={ua.random}")
#                 chrome_options.add_argument("--disable-blink-features=AutomationControlled")  # Prevent bot detection

#                 # Use undetected ChromeDriver
#                 driver = uc.Chrome(options=chrome_options)

#                 print(f"Processing job link: {job_link}")

#                 # Open job link with human-like delay
#                 driver.get(job_link)
#                 time.sleep(random.uniform(5, 10))

#                 # Handle "Apply for this job" button (if present)
#                 try:
#                     apply_button = WebDriverWait(driver, 10).until(
#                         EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Apply for this job') or contains(text(), 'Apply Now')]"))
#                     )
#                     apply_button.click()
#                     print("Clicked 'Apply for this job' button.")
#                     time.sleep(random.uniform(3, 4))  # Wait for the form to load
#                 except Exception as e:
#                     print(f"No 'Apply for this job' button found. Proceeding to the form. Error: {e}")

#                 # Extract company name
#                 try:
#                     company_name = WebDriverWait(driver, 10).until(
#                         EC.presence_of_element_located((By.CSS_SELECTOR, "a.main-header-logo img"))
#                     ).get_attribute("alt")
#                     company_name = company_name.replace(" logo", "")
#                 except:
#                     company_name = "Unknown Company"

#                 # Extract job title
#                 try:
#                     job_title = WebDriverWait(driver, 10).until(
#                         EC.presence_of_element_located((By.CSS_SELECTOR, "div.section.page-centered.posting-header h2"))
#                     ).text.strip()
#                 except:
#                     job_title = "Unknown Job Title"

#                 # Initialize questions_answered dictionary
#                 questions_answered = {}

#                 # Fill out form using YAML credentials
#                 try:
#                     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "name"))).send_keys(credentials["name"])
#                     time.sleep(random.uniform(2, 5))

#                     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "email"))).send_keys(credentials["email"])
#                     time.sleep(random.uniform(2, 5))

#                     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "phone"))).send_keys(credentials["phone"])
#                     time.sleep(random.uniform(2, 5))
#                 except InvalidSessionIdException:
#                     print("Browser session lost. Restarting the browser...")
#                     driver.quit()
#                     continue  # Retry the current job link

#                 # Upload resume (without analyzing details)
#                 print(f"Uploading resume from: {resume_path}")
#                 try:
#                     file_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "resume")))
#                     file_input.send_keys(resume_path)
#                     time.sleep(random.uniform(2, 5))
#                 except Exception as e:
#                     print(f"Failed to upload resume. Error: {e}")

#                 # Fill LinkedIn profile (if exists)
#                 try:
#                     linkedin_field = WebDriverWait(driver, 10).until(
#                         EC.presence_of_element_located((By.NAME, "urls[LinkedIn]"))
#                     )
#                     driver.execute_script("arguments[0].scrollIntoView();", linkedin_field)
#                     linkedin_field.clear()
#                     linkedin_field.send_keys(credentials["linkedin_url"])
#                     print("LinkedIn profile filled successfully.")
#                     time.sleep(random.uniform(2, 3))
#                 except Exception as e:
#                     print(f"LinkedIn field not found or could not be filled. Error: {e}")

#                 # Handle required questions
#                 for question, answer in answers.items():
#                     try:
#                         print(f"Attempting to answer: {question} with {answer}")
                        
#                         # Find the question label using the question text
#                         question_label = WebDriverWait(driver, 10).until(
#                             EC.presence_of_element_located((By.XPATH, f"//div[contains(@class, 'application-label')]//div[contains(@class, 'text') and contains(text(), '{question}')]"))
#                         )
                        
#                         # Print the HTML of the question label for debugging
#                         print("Question Label HTML:", question_label.get_attribute("outerHTML"))
                        
#                         # Find the parent element of the question (the <li> containing the question and input field)
#                         question_parent = question_label.find_element(By.XPATH, "./ancestor::li[contains(@class, 'application-question')]")
                        
#                         # Check if the question is a checkbox (acknowledgement)
#                         try:
#                             # Locate the checkbox associated with the question
#                             checkbox = question_parent.find_element(By.XPATH, ".//input[@type='checkbox']")
                            
#                             # Scroll the checkbox into view (if needed)
#                             driver.execute_script("arguments[0].scrollIntoView();", checkbox)
                            
#                             # Wait for the checkbox to be clickable
#                             WebDriverWait(driver, 10).until(EC.element_to_be_clickable(checkbox))
                            
#                             # Check the checkbox if the answer is "I acknowledge"
#                             if answer.lower() == "i acknowledge":
#                                 if not checkbox.is_selected():
#                                     checkbox.click()
#                                 print(f"Checked '{answer}' for question: {question}")
#                                 questions_answered[question] = answer
#                             else:
#                                 print(f"Checkbox not selected for question: {question}")
#                                 questions_answered[question] = "Not Answered"
#                         except Exception as e:
#                             # If no checkbox is found, assume it's a text-based or radio button question
#                             print(f"No checkbox found. Assuming it's a text-based or radio button question. Error: {e}")
                            
#                             # Handle text-based or radio button questions
#                             try:
#                                 # Look for a textarea or input field
#                                 text_input = question_parent.find_element(By.XPATH, ".//textarea | .//input[@type='text']")
                                
#                                 # Scroll the input field into view (if needed)
#                                 driver.execute_script("arguments[0].scrollIntoView();", text_input)
                                
#                                 # Clear the input field (if necessary)
#                                 text_input.clear()
                                
#                                 # Enter the answer into the text field
#                                 text_input.send_keys(answer)
                                
#                                 print(f"Entered '{answer}' for question: {question}")
#                                 questions_answered[question] = answer
#                             except:
#                                 # If no text input is found, assume it's a radio button question
#                                 print("No text input found. Assuming it's a radio button question.")
                                
#                                 # Find all radio buttons under the question parent
#                                 radio_buttons = question_parent.find_elements(By.XPATH, ".//input[@type='radio']")
                                
#                                 # Print the number of radio buttons found
#                                 print(f"Found {len(radio_buttons)} radio buttons for question: {question}")
                                
#                                 # Flag to track if the correct radio button was selected
#                                 selected = False
                                
#                                 # Loop through the radio buttons and click the one with the matching value
#                                 for radio_button in radio_buttons:
#                                     radio_value = radio_button.get_attribute("value")
#                                     print(f"Radio Button Value: {radio_value}")
                                    
#                                     if radio_value.lower() == answer.lower():  # Case-insensitive comparison
#                                         # Scroll the radio button into view (if needed)
#                                         driver.execute_script("arguments[0].scrollIntoView();", radio_button)
                                        
#                                         # Wait for the radio button to be clickable
#                                         WebDriverWait(driver, 10).until(EC.element_to_be_clickable(radio_button))
                                        
#                                         # Click the radio button using JavaScript (to avoid interception issues)
#                                         driver.execute_script("arguments[0].click();", radio_button)
                                        
#                                         # Verify if the radio button is selected
#                                         if radio_button.is_selected():
#                                             print(f"Selected '{answer}' for question: {question}")
#                                             questions_answered[question] = answer
#                                             selected = True
#                                         else:
#                                             print(f"Failed to select '{answer}' for question: {question}")
#                                             questions_answered[question] = "Not Answered"
                                        
#                                         break  # Exit the loop for this question after selecting the correct radio button
                                
#                                 if not selected:
#                                     print(f"No matching radio button found for answer: {answer}")
#                                     questions_answered[question] = "Not Answered"
                        
#                         time.sleep(random.uniform(2, 3))  # Random delay to mimic human behavior
#                     except Exception as e:
#                         print(f"Could not answer question: {question}. Error: {e}")
#                         questions_answered[question] = "Not Answered"

#                 # Handle CAPTCHA
#                 try:
#                     recaptcha_frame = WebDriverWait(driver, 10).until(
#                         EC.presence_of_element_located((By.XPATH, "//iframe[contains(@src, 'recaptcha')]"))
#                     )
#                     driver.switch_to.frame(recaptcha_frame)

#                     site_key = driver.find_element(By.CLASS_NAME, "g-recaptcha").get_attribute("data-sitekey")
#                     driver.switch_to.default_content()

#                     print("Solving CAPTCHA using 2Captcha...")

#                     solver = recaptchaV2Proxyless()
#                     solver.set_verbose(1)
#                     solver.set_key("YOUR_2CAPTCHA_API_KEY")  # Replace with your API key
#                     solver.set_website_url(job_link)
#                     solver.set_website_key(site_key)

#                     captcha_solution = solver.solve_and_return_solution()
#                     if captcha_solution:
#                         driver.execute_script(f'document.getElementById("g-recaptcha-response").innerHTML="{captcha_solution}"')
#                         time.sleep(3)
#                         print("CAPTCHA solved successfully!")
#                     else:
#                         print("Failed to solve CAPTCHA.")
#                         raise Exception("CAPTCHA Failed")
#                 except Exception as e:
#                     print("No CAPTCHA found or failed to solve:", e)

#                 # Simulate human-like mouse movement
#                 actions = ActionChains(driver)
#                 actions.move_by_offset(random.randint(5, 50), random.randint(5, 50)).perform()
#                 time.sleep(random.uniform(2, 5))

#                 # Submit the form
#                 submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "btn-submit")))
#                 submit_button.click()

#                 # Wait for success confirmation
#                 try:
#                     WebDriverWait(driver, 10).until(
#                         EC.any_of(
#                             EC.url_contains("success"),
#                             EC.presence_of_element_located((By.CSS_SELECTOR, "div.success-message"))
#                         )
#                     )
#                     print("Application submitted successfully!")
#                     status = "Success"
#                 except:
#                     status = "Failed"

#                 # Save to CSV
#                 with open(applications_file, mode="a", newline="") as file:
#                     writer = csv.writer(file)
#                     writer.writerow([company_name, job_title, job_link, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), status, questions_answered])

#                 time.sleep(random.uniform(5, 10))  # Delay before next application
#                 break  # Exit retry loop if successful

#             except (InvalidSessionIdException, WebDriverException, MaxRetryError, NewConnectionError) as e:
#                 print(f"Browser session lost or connection error. Restarting the browser... Error: {e}")
#                 try:
#                     driver.quit()
#                 except:
#                     pass
#                 retry_count += 1
#                 if retry_count < max_retries:
#                     print(f"Retrying... ({retry_count}/{max_retries})")
#                     time.sleep(random.uniform(10, 20))
#                 else:
#                     print("Failed after multiple attempts.")
#                     with open(applications_file, mode="a", newline="") as file:
#                         writer = csv.writer(file)
#                         writer.writerow([company_name, job_title, job_link, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "Failed", questions_answered])
#             except Exception as e:
#                 print(f"Error for {job_link}: {e}")
#                 retry_count += 1
#                 if retry_count < max_retries:
#                     print(f"Retrying... ({retry_count}/{max_retries})")
#                     time.sleep(random.uniform(10, 20))
#                 else:
#                     print("Failed after multiple attempts.")
#                     with open(applications_file, mode="a", newline="") as file:
#                         writer = csv.writer(file)
#                         writer.writerow([company_name, job_title, job_link, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "Failed", questions_answered])

#     print("All job links processed.")

# # Close browser





# This code is working very very good 

# import csv
# import undetected_chromedriver as uc
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.chrome.options import Options
# import time
# import os
# import yaml
# import random
# from datetime import datetime
# from fake_useragent import UserAgent
# from anticaptchaofficial.recaptchav2proxyless import recaptchaV2Proxyless

# # Load credentials, resume path, and required questions from config.yaml
# with open("config/credentials.yaml", "r") as file:
#     config = yaml.safe_load(file)

# credentials = config["credentials"]
# resume_path = os.path.abspath(config["resume_path"])

# # Read answers from CSV
# answers = {}
# try:
#     with open("config/answers.csv", mode="r") as file:
#         reader = csv.DictReader(file)
#         for row in reader:
#             answers[row["Question"]] = row["Answer"]
#             print(f"Read question: {row['Question']} with answer: {row['Answer']}")
# except FileNotFoundError:
#     print("Error: 'answers.csv' file not found. Please ensure the file exists in the correct directory.")
#     exit()

# # Set up Chrome options with a random user agent
# ua = UserAgent()
# chrome_options = Options()
# chrome_options.add_argument(f"user-agent={ua.random}")
# chrome_options.add_argument("--disable-blink-features=AutomationControlled")  # Prevent bot detection

# # Use undetected ChromeDriver
# driver = uc.Chrome(options=chrome_options)

# # File to save application data
# applications_file = "applications.csv"

# # Create applications file with headers if not present
# if not os.path.exists(applications_file):
#     with open(applications_file, mode="w", newline="") as file:
#         writer = csv.writer(file)
#         writer.writerow(["Company", "Job Title", "Application Link", "Date Applied", "Status", "Questions Answered"])

# # Read job links from the text file
# with open("data/job_links.txt", "r") as file:
#     job_links = file.read().splitlines()

# if not job_links:
#     print("No job links available. End of the links.")
# else:
#     for job_link in job_links:
        
#         retry_count = 0
#         max_retries = 3

#         while retry_count < max_retries:
#             try:
#                 print(f"Processing job link: {job_link}")

#                 # Open job link with human-like delay
#                 driver.get(job_link)
#                 time.sleep(random.uniform(5, 10))

#                 # Handle "Apply for this job" button (if present)
#                 try:
#                     apply_button = WebDriverWait(driver, 5).until(
#                         EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Apply for this job') or contains(text(), 'Apply Now')]"))
#                     )
#                     apply_button.click()
#                     print("Clicked 'Apply for this job' button.")
#                     time.sleep(random.uniform(3, 4))  # Wait for the form to load
#                 except Exception as e:
#                     print(f"No 'Apply for this job' button found. Proceeding to the form. Error: {e}")

#                 # Extract company name
#                 try:
#                     company_name = driver.find_element(By.CSS_SELECTOR, "a.main-header-logo img").get_attribute("alt")
#                     company_name = company_name.replace(" logo", "")
#                 except:
#                     company_name = "Unknown Company"

#                 # Extract job title
#                 try:
#                     job_title = driver.find_element(By.CSS_SELECTOR, "div.section.page-centered.posting-header h2").text.strip()
#                 except:
#                     job_title = "Unknown Job Title"

#                 # Fill out form
#                 WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "name"))).send_keys(credentials["name"])
#                 time.sleep(random.uniform(2, 5))

#                 WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "email"))).send_keys(credentials["email"])
#                 time.sleep(random.uniform(2, 5))

#                 WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.NAME, "phone"))).send_keys(credentials["phone"])
#                 time.sleep(random.uniform(2, 5))

#                 # Upload resume
#                 print(f"Uploading resume from: {resume_path}")
#                 file_input = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.NAME, "resume")))
#                 file_input.send_keys(resume_path)
#                 time.sleep(random.uniform(2, 5))

#                 # Fill LinkedIn profile (if exists)
#                 try:
#                     linkedin_field = WebDriverWait(driver, 5).until(
#                         EC.presence_of_element_located((By.NAME, "urls[LinkedIn]"))
#                     )
#                     driver.execute_script("arguments[0].scrollIntoView();", linkedin_field)
#                     linkedin_field.clear()
#                     linkedin_field.send_keys(credentials["linkedin_url"])
#                     print("LinkedIn profile filled successfully.")
#                     time.sleep(random.uniform(2, 3))
#                 except Exception as e:
#                     print(f"LinkedIn field not found or could not be filled. Error: {e}")

#                 # Handle required questions
#                 questions_answered = {}
#                 try:
#                     # Locate all checkboxes associated with "I acknowledge" text
#                     checkboxes = WebDriverWait(driver, 10).until(
#                         EC.presence_of_all_elements_located(
#                             (By.XPATH, "//span[contains(text(), 'I acknowledge')]/preceding-sibling::input[@type='checkbox']")
#                         )
#                     )

#                     print(f"Found {len(checkboxes)} 'I acknowledge' checkboxes.")

#                     for checkbox in checkboxes:
#                         try:
#                             # Scroll the checkbox into view
#                             driver.execute_script("arguments[0].scrollIntoView();", checkbox)

#                             # Wait until checkbox is clickable
#                             WebDriverWait(driver, 5).until(EC.element_to_be_clickable(checkbox))

#                             # Click using JavaScript
#                             driver.execute_script("arguments[0].click();", checkbox)

#                             # Confirm selection
#                             if checkbox.is_selected():
#                                 print("✅ Checkbox checked successfully.")
#                             else:
#                                 print("❌ Failed to check the checkbox.")

#                         except Exception as e:
#                             print(f"⚠ Error clicking checkbox: {e}")

#                 except Exception as e:
#                     print(f"⚠ Error finding checkboxes: {e}")

#                 for question, answer in answers.items():
#                     try:
#                         print(f"Attempting to answer: {question} with {answer}")
                        
#                         # Find the question label using the question text
#                         question_label = WebDriverWait(driver, 10).until(
#                             EC.presence_of_element_located((By.XPATH, f"//div[contains(@class, 'application-label')]//div[contains(@class, 'text') and contains(text(), '{question}')]"))
#                         )
                        
#                         # Print the HTML of the question label for debugging
#                         print("Question Label HTML:", question_label.get_attribute("outerHTML"))
                        
#                         # Find the parent element of the question (the <li> containing the question and input field)
#                         question_parent = question_label.find_element(By.XPATH, "./ancestor::li[contains(@class, 'application-question')]")
                        
#                         # Check if the question is a text-based input field
#                         try:
#                             # Look for a textarea or input field
#                             text_input = question_parent.find_element(By.XPATH, ".//textarea | .//input[@type='text']")
                            
#                             # Scroll the input field into view (if needed)
#                             driver.execute_script("arguments[0].scrollIntoView();", text_input)
                            
#                             # Clear the input field (if necessary)
#                             text_input.clear()
                            
#                             # Enter the answer into the text field
#                             text_input.send_keys(answer[question])
                            
#                             print(f"Entered '{answer}' for question: {question}")
#                             questions_answered[question] = answer[question]
#                         except:
#                             # If no text input is found, assume it's a radio button question
#                             print("No text input found. Assuming it's a radio button question.")
                            
#                             # Find all radio buttons under the question parent
#                             radio_buttons = question_parent.find_elements(By.XPATH, ".//input[@type='radio']")
                            
#                             # Print the number of radio buttons found
#                             print(f"Found {len(radio_buttons)} radio buttons for question: {question}")
                            
#                             # Flag to track if the correct radio button was selected
#                             selected = False
                            
#                             # Loop through the radio buttons and click the one with the matching value
#                             for radio_button in radio_buttons:
#                                 radio_value = radio_button.get_attribute("value")
#                                 print(f"Radio Button Value: {radio_value}")
                                
#                                 if radio_value.lower() == answer.lower():  # Case-insensitive comparison
#                                     # Scroll the radio button into view (if needed)
#                                     driver.execute_script("arguments[0].scrollIntoView();", radio_button)
                                    
#                                     # Wait for the radio button to be clickable
#                                     WebDriverWait(driver, 10).until(EC.element_to_be_clickable(radio_button))
                                    
#                                     # Click the radio button using JavaScript (to avoid interception issues)
#                                     driver.execute_script("arguments[0].click();", radio_button)
                                    
#                                     # Verify if the radio button is selected
#                                     if radio_button.is_selected():
#                                         print(f"Selected '{answer}' for question: {question}")
#                                         questions_answered[question] = answer[question]
#                                         selected = True
#                                     else:
#                                         print(f"Failed to select '{answer}' for question: {question}")
#                                         questions_answered[question] = "Not Answered"
                                    
#                                     break  # Exit the loop for this question after selecting the correct radio button
                            
#                             if not selected:
#                                 print(f"No matching radio button found for answer: {answer}")
#                                 questions_answered[question] = "Not Answered"
                        
#                         time.sleep(random.uniform(2, 3))  # Random delay to mimic human behavior
#                     except Exception as e:
#                         print(f"Could not answer question: {question}. Error: {e}")
#                         questions_answered[question] = "Not Answered"

#                 # Handle CAPTCHA
#                 try:
#                     recaptcha_frame = WebDriverWait(driver, 10).until(
#                         EC.presence_of_element_located((By.XPATH, "//iframe[contains(@src, 'recaptcha')]"))
#                     )
#                     driver.switch_to.frame(recaptcha_frame)

#                     site_key = driver.find_element(By.CLASS_NAME, "g-recaptcha").get_attribute("data-sitekey")
#                     driver.switch_to.default_content()

#                     print("Solving CAPTCHA using 2Captcha...")

#                     solver = recaptchaV2Proxyless()
#                     solver.set_verbose(1)
#                     solver.set_key("YOUR_2CAPTCHA_API_KEY")  # Replace with your API key
#                     solver.set_website_url(job_link)
#                     solver.set_website_key(site_key)

#                     captcha_solution = solver.solve_and_return_solution()
#                     if captcha_solution:
#                         driver.execute_script(f'document.getElementById("g-recaptcha-response").innerHTML="{captcha_solution}"')
#                         time.sleep(3)
#                         print("CAPTCHA solved successfully!")
#                     else:
#                         print("Failed to solve CAPTCHA.")
#                         raise Exception("CAPTCHA Failed")
#                 except Exception as e:
#                     print("No CAPTCHA found or failed to solve:", e)

#                 # Simulate human-like mouse movement
#                 actions = ActionChains(driver)
#                 actions.move_by_offset(random.randint(5, 50), random.randint(5, 50)).perform()
#                 time.sleep(random.uniform(2, 5))

#                 # Submit the form
#                 submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "btn-submit")))
#                 submit_button.click()

#                 # Wait for success confirmation
#                 try:
#                     WebDriverWait(driver, 10).until(
#                         EC.any_of(
#                             EC.url_contains("success"),
#                             EC.presence_of_element_located((By.CSS_SELECTOR, "div.success-message"))
#                         )
#                     )
#                     print("Application submitted successfully!")
#                     status = "Success"
#                 except:
#                     status = "Failed"

#                 # Save to CSV
#                 with open(applications_file, mode="a", newline="") as file:
#                     writer = csv.writer(file)
#                     writer.writerow([company_name, job_title, job_link, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), status, questions_answered])

#                 time.sleep(random.uniform(5, 10))  # Delay before next application
#                 break  # Exit retry loop if successful

#             except Exception as e:
#                 print(f"Error for {job_link}: {e}")
#                 retry_count += 1
#                 if retry_count < max_retries:
#                     print(f"Retrying... ({retry_count}/{max_retries})")
#                     time.sleep(random.uniform(10, 10))
#                 else:
#                     print("Failed after multiple attempts.")
#                     with open(applications_file, mode="a", newline="") as file:
#                         writer = csv.writer(file)
#                         writer.writerow([company_name, job_title, job_link, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "Failed", questions_answered])

#     print("All job links processed.")

# # Close browser
# driver.quit()




# import csv
# import undetected_chromedriver as uc
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.chrome.options import Options
# import time
# import os
# import yaml
# import random
# from datetime import datetime
# from fake_useragent import UserAgent
# from anticaptchaofficial.recaptchav2proxyless import recaptchaV2Proxyless

# # Load credentials, resume path, and required questions from config.yaml
# with open("config/credentials.yaml", "r") as file:
#     config = yaml.safe_load(file)

# credentials = config["credentials"]
# resume_path = os.path.abspath(config["resume_path"])

# # Read answers from CSV
# answers = {}
# try:
#     with open("config/answers.csv", mode="r") as file:
#         reader = csv.DictReader(file)
#         for row in reader:
#             answers[row["Question"]] = row["Answer"]
#             print(f"Read question: {row['Question']} with answer: {row['Answer']}")
# except FileNotFoundError:
#     print("Error: 'answers.csv' file not found. Please ensure the file exists in the correct directory.")
#     exit()

# # Set up Chrome options with a random user agent
# ua = UserAgent()
# chrome_options = Options()
# chrome_options.add_argument(f"user-agent={ua.random}")
# chrome_options.add_argument("--disable-blink-features=AutomationControlled")  # Prevent bot detection

# # Use undetected ChromeDriver
# driver = uc.Chrome(options=chrome_options)

# # File to save application data
# applications_file = "applications.csv"

# # Create applications file with headers if not present
# if not os.path.exists(applications_file):
#     with open(applications_file, mode="w", newline="") as file:
#         writer = csv.writer(file)
#         writer.writerow(["Company", "Job Title", "Application Link", "Date Applied", "Status", "Questions Answered"])

# # Read job links from the text file
# with open("data/job_links.txt", "r") as file:
#     job_links = file.read().splitlines()

# if not job_links:
#     print("No job links available. End of the links.")
# else:
#     for job_link in job_links:
#         retry_count = 0
#         max_retries = 3

#         while retry_count < max_retries:
#             try:
#                 print(f"Processing job link: {job_link}")

#                 # Open job link with human-like delay
#                 driver.get(job_link)
#                 time.sleep(random.uniform(5, 10))

#                 # Print current URL and title for debugging
#                 print(f"Current URL: {driver.current_url}")
#                 print(f"Page Title: {driver.title}")

#                 # Take a screenshot for debugging
#                 driver.save_screenshot("debug_page.png")

#                 # Handle "Apply for this job" button (if present)
#                 try:
#                     apply_button = WebDriverWait(driver, 10).until(
#                         EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Apply for this job') or contains(text(), 'Apply Now')]"))
#                     )
#                     apply_button.click()
#                     print("Clicked 'Apply for this job' button.")
#                     time.sleep(random.uniform(3, 4))  # Wait for the form to load
#                 except Exception as e:
#                     print(f"No 'Apply for this job' button found. Proceeding to the form. Error: {e}")

#                 # Take a screenshot after clicking the apply button
#                 driver.save_screenshot("debug_after_apply.png")

#                 # Extract company name
#                 try:
#                     company_name = driver.find_element(By.CSS_SELECTOR, "a.main-header-logo img").get_attribute("alt")
#                     company_name = company_name.replace(" logo", "")
#                 except:
#                     company_name = "Unknown Company"

#                 # Extract job title
#                 try:
#                     job_title = driver.find_element(By.CSS_SELECTOR, "div.section.page-centered.posting-header h2").text.strip()
#                 except:
#                     job_title = "Unknown Job Title"

#                 # Fill out form
#                 try:
#                     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "name"))).send_keys(credentials["name"])
#                     time.sleep(random.uniform(2, 5))
#                 except Exception as e:
#                     print(f"Error filling name field: {e}")

#                 try:
#                     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "email"))).send_keys(credentials["email"])
#                     time.sleep(random.uniform(2, 5))
#                 except Exception as e:
#                     print(f"Error filling email field: {e}")

#                 try:
#                     WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.NAME, "phone"))).send_keys(credentials["phone"])
#                     time.sleep(random.uniform(2, 5))
#                 except Exception as e:
#                     print(f"Error filling phone field: {e}")

#                 # Upload resume
#                 try:
#                     print(f"Uploading resume from: {resume_path}")
#                     file_input = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.NAME, "resume")))
#                     file_input.send_keys(resume_path)
#                     time.sleep(random.uniform(2, 5))
#                 except Exception as e:
#                     print(f"Error uploading resume: {e}")

#                 # Fill LinkedIn profile (if exists)
#                 try:
#                     linkedin_field = WebDriverWait(driver, 5).until(
#                         EC.presence_of_element_located((By.NAME, "urls[LinkedIn]"))
#                     )
#                     driver.execute_script("arguments[0].scrollIntoView();", linkedin_field)
#                     linkedin_field.clear()
#                     linkedin_field.send_keys(credentials["linkedin_url"])
#                     print("LinkedIn profile filled successfully.")
#                     time.sleep(random.uniform(2, 3))
#                 except Exception as e:
#                     print(f"LinkedIn field not found or could not be filled. Error: {e}")

#                 # Handle required questions
#                 questions_answered = {}

#                 # Handle "Gender" dropdown specifically
#                 try:
#                     gender_dropdown = WebDriverWait(driver, 10).until(
#                         EC.presence_of_element_located((By.NAME, "eeo[gender]"))
#                     )
#                     gender_dropdown.click()
#                     gender_option = WebDriverWait(driver, 10).until(
#                         EC.presence_of_element_located((By.XPATH, f"//option[contains(text(), '{answers['Gender']}')]"))
#                     )
#                     gender_option.click()
#                     questions_answered["Gender"] = answers["Gender"]
#                     print(f"Selected '{answers['Gender']}' for question: Gender")
#                 except Exception as e:
#                     print(f"Could not answer 'Gender' dropdown. Error: {e}")

#                 # Find all questions on the page and answer only those present in the form
#                 try:
#                     question_labels = driver.find_elements(By.XPATH, "//div[contains(@class, 'application-label')]//div[contains(@class, 'text')]")
#                     for label in question_labels:
#                         question_text = label.text.strip()
#                         if question_text in answers:
#                             try:
#                                 print(f"Attempting to answer: {question_text} with {answers[question_text]}")

#                                 # Find the parent element of the question
#                                 question_parent = label.find_element(By.XPATH, "./ancestor::li[contains(@class, 'application-question')]")

#                                 # Check if the question is a checkbox
#                                 try:
#                                     checkbox = question_parent.find_element(By.XPATH, ".//input[@type='checkbox']")
#                                     if not checkbox.is_selected():
#                                         checkbox.click()
#                                     questions_answered[question_text] = answers[question_text]
#                                     print(f"Checked '{answers[question_text]}' for question: {question_text}")
#                                 except:
#                                     # If no checkbox is found, assume it's a radio button question
#                                     radio_buttons = question_parent.find_elements(By.XPATH, ".//input[@type='radio']")
#                                     selected = False
#                                     for radio_button in radio_buttons:
#                                         radio_value = radio_button.get_attribute("value")
#                                         if radio_value.lower() == answers[question_text].lower():
#                                             driver.execute_script("arguments[0].scrollIntoView();", radio_button)
#                                             WebDriverWait(driver, 10).until(EC.element_to_be_clickable(radio_button))
#                                             driver.execute_script("arguments[0].click();", radio_button)
#                                             if radio_button.is_selected():
#                                                 print(f"Selected '{answers[question_text]}' for question: {question_text}")
#                                                 questions_answered[question_text] = answers[question_text]
#                                                 selected = True
#                                             else:
#                                                 print(f"Failed to select '{answers[question_text]}' for question: {question_text}")
#                                                 questions_answered[question_text] = "Not Answered"
#                                             break
#                                     if not selected:
#                                         print(f"No matching radio button found for answer: {answers[question_text]}")
#                                         questions_answered[question_text] = "Not Answered"

#                                 time.sleep(random.uniform(2, 3))  # Random delay to mimic human behavior
#                             except Exception as e:
#                                 print(f"Could not answer question: {question_text}. Error: {e}")
#                                 questions_answered[question_text] = "Not Answered"
#                 except Exception as e:
#                     print(f"Error finding questions on the page: {e}")

#                 # Handle CAPTCHA
#                 try:
#                     recaptcha_frame = WebDriverWait(driver, 10).until(
#                         EC.presence_of_element_located((By.XPATH, "//iframe[contains(@src, 'recaptcha')]"))
#                     )
#                     driver.switch_to.frame(recaptcha_frame)

#                     site_key = driver.find_element(By.CLASS_NAME, "g-recaptcha").get_attribute("data-sitekey")
#                     driver.switch_to.default_content()

#                     print("Solving CAPTCHA using 2Captcha...")

#                     solver = recaptchaV2Proxyless()
#                     solver.set_verbose(1)
#                     solver.set_key("YOUR_2CAPTCHA_API_KEY")  # Replace with your API key
#                     solver.set_website_url(job_link)
#                     solver.set_website_key(site_key)

#                     captcha_solution = solver.solve_and_return_solution()
#                     if captcha_solution:
#                         driver.execute_script(f'document.getElementById("g-recaptcha-response").innerHTML="{captcha_solution}"')
#                         time.sleep(3)
#                         print("CAPTCHA solved successfully!")
#                     else:
#                         print("Failed to solve CAPTCHA.")
#                         raise Exception("CAPTCHA Failed")
#                 except Exception as e:
#                     print("No CAPTCHA found or failed to solve:", e)

#                 # Simulate human-like mouse movement
#                 try:
#                     actions = ActionChains(driver)
#                     actions.move_by_offset(random.randint(5, 50), random.randint(5, 50)).perform()
#                     time.sleep(random.uniform(2, 5))
#                 except Exception as e:
#                     print(f"Error simulating mouse movement: {e}")

#                 # Submit the form
#                 try:
#                     submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "btn-submit")))
#                     submit_button.click()
#                 except Exception as e:
#                     print(f"Error submitting form: {e}")

#                 # Wait for success confirmation
#                 try:
#                     WebDriverWait(driver, 10).until(
#                         EC.any_of(
#                             EC.url_contains("success"),
#                             EC.presence_of_element_located((By.CSS_SELECTOR, "div.success-message"))
#                         )
#                     )
#                     print("Application submitted successfully!")
#                     status = "Success"
#                 except:
#                     status = "Failed"

#                 # Save to CSV
#                 with open(applications_file, mode="a", newline="") as file:
#                     writer = csv.writer(file)
#                     writer.writerow([company_name, job_title, job_link, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), status, questions_answered])

#                 time.sleep(random.uniform(5, 10))  # Delay before next application
#                 break  # Exit retry loop if successful

#             except Exception as e:
#                 print(f"Error for {job_link}: {e}")
#                 retry_count += 1
#                 if retry_count < max_retries:
#                     print(f"Retrying... ({retry_count}/{max_retries})")
#                     time.sleep(random.uniform(10, 20))
#                 else:
#                     print("Failed after multiple attempts.")
#                     with open(applications_file, mode="a", newline="") as file:
#                         writer = csv.writer(file)
#                         writer.writerow([company_name, job_title, job_link, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "Failed", questions_answered])

#     print("All job links processed.")

# # Close browser
# driver.quit()






import csv
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd
import os
import yaml
import random
from datetime import datetime
from fake_useragent import UserAgent
from anticaptchaofficial.recaptchav2proxyless import recaptchaV2Proxyless

# Load credentials, resume path, and required questions from config.yaml
with open("config/credentials.yaml", "r") as file:
    config = yaml.safe_load(file)

credentials = config["credentials"]
resume_path = os.path.abspath(config["resume_path"])

# Read answers from CSV
answers = {}
try:
    with open("config/answers.csv", mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            answers[row["Question"]] = row["Answer"]
            print(f"Read question: {row['Question']} with answer: {row['Answer']}")
except FileNotFoundError:
    print("Error: 'answers.csv' file not found. Please ensure the file exists in the correct directory.")
    exit()

# Set up Chrome options with a random user agent
ua = UserAgent()
chrome_options = Options()
chrome_options.add_argument(f"user-agent={ua.random}")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")  # Prevent bot detection

# Use undetected ChromeDriver
driver = uc.Chrome(options=chrome_options)

# File to save application data
applications_file = "applications.csv"

# Create applications file with headers if not present
if not os.path.exists(applications_file):
    with open(applications_file, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Company", "Job Title", "Application Link", "Date Applied", "Status", "Questions Answered"])


# Read job links from the file
with open("data/job_links.txt", "r") as file:
    job_links = [line.strip() for line in file.readlines()]  # Read and remove spaces

# Read the CSV file
csv_file = "job_questions.csv"  # Update with your actual CSV file path
df = pd.read_csv(csv_file)

# Ensure column names are correct
print(df.columns)  # Debugging step to verify column names

# Filter questions based on job links
filtered_df = df[df['job_link'].str.strip().isin(job_links)]

# Process only the filtered questions
for index, row in filtered_df.iterrows():
    question = row['Question']
    job_link = row['Answer']
    print(f"Processing question for {job_link}: {question}")

# Read job links from the text file
with open("data/job_links.txt", "r") as file:
    job_links = file.read().splitlines()

if not job_links:
    print("No job links available. End of the links.")
else:
    for job_link in job_links:
        
        retry_count = 0
        max_retries = 3

        while retry_count < max_retries:
            try:
                print(f"Processing job link: {job_link}")

                # Open job link with human-like delay
                driver.get(job_link)
                time.sleep(random.uniform(5, 10))

                # Handle "Apply for this job" button (if present)
                try:
                    apply_button = WebDriverWait(driver, 5).until(
                        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Apply for this job') or contains(text(), 'Apply Now')]"))
                    )
                    apply_button.click()
                    print("Clicked 'Apply for this job' button.")
                    time.sleep(random.uniform(3, 4))  # Wait for the form to load
                except Exception as e:
                    print(f"No 'Apply for this job' button found. Proceeding to the form. Error: {e}")

                # Extract company name
                try:
                    company_name = driver.find_element(By.CSS_SELECTOR, "a.main-header-logo img").get_attribute("alt")
                    company_name = company_name.replace(" logo", "")
                except:
                    company_name = "Unknown Company"

                # Extract job title
                try:
                    job_title = driver.find_element(By.CSS_SELECTOR, "div.section.page-centered.posting-header h2").text.strip()
                except:
                    job_title = "Unknown Job Title"

                # Fill out form
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "name"))).send_keys(credentials["name"])
                time.sleep(random.uniform(2, 5))

                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "email"))).send_keys(credentials["email"])
                time.sleep(random.uniform(2, 5))

                WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.NAME, "phone"))).send_keys(credentials["phone"])
                time.sleep(random.uniform(2, 5))

                # Upload resume
                print(f"Uploading resume from: {resume_path}")
                file_input = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.NAME, "resume")))
                file_input.send_keys(resume_path)
                time.sleep(random.uniform(2, 5))

                # Fill LinkedIn profile (if exists)
                try:
                    linkedin_field = WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.NAME, "urls[LinkedIn]"))
                    )
                    driver.execute_script("arguments[0].scrollIntoView();", linkedin_field)
                    linkedin_field.clear()
                    linkedin_field.send_keys(credentials["linkedin_url"])
                    print("LinkedIn profile filled successfully.")
                    time.sleep(random.uniform(2, 3))
                except Exception as e:
                    print(f"LinkedIn field not found or could not be filled. Error: {e}")

                # Handle required questions
                questions_answered = {}
                try:
                    # Locate all checkboxes associated with "I acknowledge" text
                    checkboxes = WebDriverWait(driver, 10).until(
                        EC.presence_of_all_elements_located(
                            (By.XPATH, "//span[contains(text(), 'I acknowledge')]/preceding-sibling::input[@type='checkbox']")
                        )
                    )

                    print(f"Found {len(checkboxes)} 'I acknowledge' checkboxes.")

                    for checkbox in checkboxes:
                        try:
                            # Scroll the checkbox into view
                            driver.execute_script("arguments[0].scrollIntoView();", checkbox)

                            # Wait until checkbox is clickable
                            WebDriverWait(driver, 5).until(EC.element_to_be_clickable(checkbox))

                            # Click using JavaScript
                            driver.execute_script("arguments[0].click();", checkbox)

                            # Confirm selection
                            if checkbox.is_selected():
                                print("✅ Checkbox checked successfully.")
                            else:
                                print("❌ Failed to check the checkbox.")

                        except Exception as e:
                            print(f"⚠ Error clicking checkbox: {e}")

                except Exception as e:
                    print(f"⚠ Error finding checkboxes: {e}")

                for question, answer in answers.items():
                    try:
                        print(f"Attempting to answer: {question} with {answer}")
                        
                        # Find the question label using the question text
                        question_label = WebDriverWait(driver, 10).until(
                            EC.presence_of_element_located((By.XPATH, f"//div[contains(@class, 'application-label')]//div[contains(@class, 'text') and contains(text(), '{question}')]"))
                        )
                        
                        # Print the HTML of the question label for debugging
                        print("Question Label HTML:", question_label.get_attribute("outerHTML"))
                        
                        # Find the parent element of the question (the <li> containing the question and input field)
                        question_parent = question_label.find_element(By.XPATH, "./ancestor::li[contains(@class, 'application-question')]")
                        
                        # Check if the question is a text-based input field
                        try:
                            # Look for a textarea or input field
                            text_input = question_parent.find_element(By.XPATH, ".//textarea | .//input[@type='text']")
                            
                            # Scroll the input field into view (if needed)
                            driver.execute_script("arguments[0].scrollIntoView();", text_input)
                            
                            # Clear the input field (if necessary)
                            text_input.clear()
                            
                            # Enter the answer into the text field
                            text_input.send_keys(answer[question])
                            
                            print(f"Entered '{answer}' for question: {question}")
                            questions_answered[question] = answer[question]
                        except:
                            # If no text input is found, assume it's a radio button question
                            print("No text input found. Assuming it's a radio button question.")
                            
                            # Find all radio buttons under the question parent
                            radio_buttons = question_parent.find_elements(By.XPATH, ".//input[@type='radio']")
                            
                            # Print the number of radio buttons found
                            print(f"Found {len(radio_buttons)} radio buttons for question: {question}")
                            
                            # Flag to track if the correct radio button was selected
                            selected = False
                            
                            # Loop through the radio buttons and click the one with the matching value
                            for radio_button in radio_buttons:
                                radio_value = radio_button.get_attribute("value")
                                print(f"Radio Button Value: {radio_value}")
                                
                                if radio_value.lower() == answer.lower():  # Case-insensitive comparison
                                    # Scroll the radio button into view (if needed)
                                    driver.execute_script("arguments[0].scrollIntoView();", radio_button)
                                    
                                    # Wait for the radio button to be clickable
                                    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(radio_button))
                                    
                                    # Click the radio button using JavaScript (to avoid interception issues)
                                    driver.execute_script("arguments[0].click();", radio_button)
                                    
                                    # Verify if the radio button is selected
                                    if radio_button.is_selected():
                                        print(f"Selected '{answer}' for question: {question}")
                                        questions_answered[question] = answer[question]
                                        selected = True
                                    else:
                                        print(f"Failed to select '{answer}' for question: {question}")
                                        questions_answered[question] = "Not Answered"
                                    
                                    break  # Exit the loop for this question after selecting the correct radio button
                            
                            if not selected:
                                print(f"No matching radio button found for answer: {answer}")
                                questions_answered[question] = "Not Answered"
                        
                        time.sleep(random.uniform(2, 3))  # Random delay to mimic human behavior
                    except Exception as e:
                        print(f"Could not answer question: {question}. Error: {e}")
                        questions_answered[question] = "Not Answered"

                # Handle CAPTCHA
                try:
                    recaptcha_frame = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, "//iframe[contains(@src, 'recaptcha')]"))
                    )
                    driver.switch_to.frame(recaptcha_frame)

                    site_key = driver.find_element(By.CLASS_NAME, "g-recaptcha").get_attribute("data-sitekey")
                    driver.switch_to.default_content()

                    print("Solving CAPTCHA using 2Captcha...")

                    solver = recaptchaV2Proxyless()
                    solver.set_verbose(1)
                    solver.set_key("YOUR_2CAPTCHA_API_KEY")  # Replace with your API key
                    solver.set_website_url(job_link)
                    solver.set_website_key(site_key)

                    captcha_solution = solver.solve_and_return_solution()
                    if captcha_solution:
                        driver.execute_script(f'document.getElementById("g-recaptcha-response").innerHTML="{captcha_solution}"')
                        time.sleep(3)
                        print("CAPTCHA solved successfully!")
                    else:
                        print("Failed to solve CAPTCHA.")
                        raise Exception("CAPTCHA Failed")
                except Exception as e:
                    print("No CAPTCHA found or failed to solve:", e)

                # Simulate human-like mouse movement
                actions = ActionChains(driver)
                actions.move_by_offset(random.randint(5, 50), random.randint(5, 50)).perform()
                time.sleep(random.uniform(2, 5))

                # Submit the form
                submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "btn-submit")))
                submit_button.click()

                # Wait for success confirmation
                try:
                    WebDriverWait(driver, 10).until(
                        EC.any_of(
                            EC.url_contains("success"),
                            EC.presence_of_element_located((By.CSS_SELECTOR, "div.success-message"))
                        )
                    )
                    print("Application submitted successfully!")
                    status = "Success"
                except:
                    status = "Failed"

                # Save to CSV
                with open(applications_file, mode="a", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerow([company_name, job_title, job_link, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), status, questions_answered])

                time.sleep(random.uniform(5, 10))  # Delay before next application
                break  # Exit retry loop if successful

            except Exception as e:
                print(f"Error for {job_link}: {e}")
                retry_count += 1
                if retry_count < max_retries:
                    print(f"Retrying... ({retry_count}/{max_retries})")
                    time.sleep(random.uniform(10, 10))
                else:
                    print("Failed after multiple attempts.")
                    with open(applications_file, mode="a", newline="") as file:
                        writer = csv.writer(file)
                        writer.writerow([company_name, job_title, job_link, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "Failed", questions_answered])

    print("All job links processed.")

# Close browser
driver.quit()

