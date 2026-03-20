import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytesseract
from PIL import Image
import time
import os
import io

# --- CONFIGURATION ---
SEMESTER = "8" # <--- CHECK THIS
TARGET_URL = "https://result.rgpv.ac.in/Result/BErslt.aspx"

# --- FILE SETUP ---
script_dir = os.path.dirname(os.path.abspath(__file__))
input_filename = "Roll No.xlsx"
output_filename = "RGPV_Results_Final.xlsx"

# Find file
path_1 = os.path.join(script_dir, input_filename)
path_2 = os.path.join(script_dir, "..", input_filename)

if os.path.exists(path_1):
    input_path = path_1
elif os.path.exists(path_2):
    input_path = path_2
else:
    print(f"❌ CRITICAL ERROR: Could not find '{input_filename}'.")
    exit()

print(f"📂 Loading: {input_path}")
df_input = pd.read_excel(input_path)

if 'Roll No' in df_input.columns:
    roll_list = df_input['Roll No'].tolist()
elif 'RollNo' in df_input.columns:
    roll_list = df_input['RollNo'].tolist()
else:
    print("❌ ERROR: Column 'Roll No' not found.")
    exit()

# --- BROWSER SETUP ---
chrome_options = Options()
# chrome_options.add_argument("--headless") 
driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 15) # Wait up to 15 seconds for elements

final_data = []

print(f"🚀 Starting automation for {len(roll_list)} students...")

for roll in roll_list:
    roll_str = str(roll)
    print(f"\nProcessing: {roll_str}")
    
    student_data = {"Roll No": roll_str, "Status": "Failed"} 
    success = False
    attempts = 0

    while not success and attempts < 3:
        try:
            driver.get(TARGET_URL)
            
            # --- STEP 1: FILL FORM ---
            try:
                # 1. Roll Number
                # We use 'wait.until' to make sure page is ready
                input_roll = wait.until(EC.presence_of_element_located((By.ID, "ctl00_ContentPlaceHolder1_txtrollno")))
                input_roll.clear()
                input_roll.send_keys(roll_str)

                # 2. Semester
                sem_dropdown = Select(driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_drpSemester"))
                sem_dropdown.select_by_visible_text(SEMESTER)
                
                # 3. CRITICAL FIX: Wait for Captcha to Refresh
                # When you select semester, the image ID stays the same, but the element refreshes.
                # We wait specifically for the image to be visible.
                time.sleep(2) # Small buffer for the refresh trigger
                img_captcha = wait.until(EC.visibility_of_element_located((By.ID, "ctl00_ContentPlaceHolder1_imgCaptcha")))

                # 4. Find Input Box (It is TextBox1 on this page)
                input_captcha = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_TextBox1")

                # --- STEP 2: SOLVE CAPTCHA ---
                captcha_screenshot = img_captcha.screenshot_as_png
                image = Image.open(io.BytesIO(captcha_screenshot))
                image = image.convert('L')
                captcha_text = pytesseract.image_to_string(image).strip()
                captcha_text = ''.join(e for e in captcha_text if e.isalnum())
                
                print(f"  > Captcha guess: {captcha_text}")

                input_captcha.clear()
                input_captcha.send_keys(captcha_text)

                # Click View
                driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_btnviewresult").click()
                
                # Wait for result or alert
                time.sleep(2)

            except Exception as e:
                print(f"  ⚠️ Error in form filling: {e}")
                # If window closed, break loop
                if "no such window" in str(e):
                    raise e
                break

            # --- STEP 3: EXTRACT RESULT ---
            try:
                # Check if we are on result page by looking for Name
                lbl_name = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_lblNameGrading")
                
                student_data["Name"] = lbl_name.text
                student_data["SGPA"] = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_lblSGPA").text
                student_data["CGPA"] = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_lblcgpa").text
                student_data["Result"] = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_lblResultNew").text
                student_data["Status"] = "Success"
                
                print(f"  ✅ SUCCESS: {student_data['Name']} | SGPA: {student_data['SGPA']}")

                # Grab Grades
                try:
                    tables = pd.read_html(driver.page_source)
                    for table in tables:
                        if "Subject Code" in str(table.columns) or "Grade" in str(table.columns):
                            grades_str = ""
                            for index, row in table.iterrows():
                                try:
                                    sub = row.get(1, row.get('Subject Name', ''))
                                    grd = row.get(4, row.get('Grade', ''))
                                    if pd.notna(sub) and pd.notna(grd):
                                        grades_str += f"{sub}: {grd} | "
                                except:
                                    pass
                            student_data["Grades"] = grades_str
                            break
                except:
                    pass

                success = True
            
            except:
                # Handle Alert (Wrong Captcha)
                try:
                    alert = driver.switch_to.alert
                    print(f"  > Alert: {alert.text}")
                    alert.accept()
                except:
                    pass
                raise Exception("Result not found (Captcha or Data missing)")

        except Exception as e:
            attempts += 1
            print(f"  > Attempt {attempts} failed.")
            if "no such window" in str(e):
                print("❌ Browser crashed. Restarting driver...")
                driver = webdriver.Chrome(options=chrome_options)
                wait = WebDriverWait(driver, 15)
            time.sleep(1)

    final_data.append(student_data)

# --- SAVE ---
df_output = pd.DataFrame(final_data)
output_path = os.path.join(script_dir, output_filename)
df_output.to_excel(output_path, index=False)
print(f"✅ Saved to: {output_path}")

driver.quit()
# --- CLEANUP ---
print("🏁 Automation complete.")
print(f"Total Students Processed: {len(final_data)}")
print(f"Successful: {len([d for d in final_data if d['Status'] == 'Success'])}")
print(f"Failed: {len([d for d in final_data if d['Status'] == 'Failed'])}")